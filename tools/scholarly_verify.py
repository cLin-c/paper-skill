#!/usr/bin/env python3
"""Crossref/OpenAlex metadata verification with no third-party dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


USER_AGENT = "paper-skill/0.5 (+https://github.com/cLin-c/paper-skill)"
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)


def normalize_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value, flags=re.I)
    match = DOI_RE.search(value)
    return match.group(0).rstrip(".,;)").lower() if match else ""


def normalize_title(value: str) -> str:
    return " ".join(re.findall(r"[\w]+", value.casefold(), flags=re.UNICODE))


def title_similarity(left: str, right: str) -> float:
    return round(SequenceMatcher(None, normalize_title(left), normalize_title(right)).ratio(), 4)


def _get_json(url: str, timeout: float = 20.0) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def crossref_lookup(doi: str, mailto: str = "", timeout: float = 20.0) -> dict[str, Any]:
    encoded = urllib.parse.quote(doi, safe="")
    query = urllib.parse.urlencode({"mailto": mailto}) if mailto else ""
    url = f"https://api.crossref.org/works/{encoded}" + (f"?{query}" if query else "")
    raw = _get_json(url, timeout)["message"]
    authors = [" ".join(filter(None, [a.get("given", ""), a.get("family", "")])).strip() for a in raw.get("author", [])]
    date_parts = (raw.get("published-print") or raw.get("published-online") or raw.get("issued") or {}).get("date-parts", [[]])
    return {
        "source": "Crossref",
        "doi": normalize_doi(raw.get("DOI", doi)),
        "title": (raw.get("title") or [""])[0],
        "authors": authors,
        "year": date_parts[0][0] if date_parts and date_parts[0] else None,
        "venue": (raw.get("container-title") or [""])[0],
        "type": raw.get("type"),
        "url": raw.get("URL"),
        "retrieved_from": url,
    }


def openalex_lookup(doi: str, api_key: str = "", timeout: float = 20.0) -> dict[str, Any]:
    external_id = urllib.parse.quote(f"https://doi.org/{doi}", safe="")
    query = urllib.parse.urlencode({"api_key": api_key}) if api_key else ""
    url = f"https://api.openalex.org/works/{external_id}" + (f"?{query}" if query else "")
    raw = _get_json(url, timeout)
    source = ((raw.get("primary_location") or {}).get("source") or {})
    return {
        "source": "OpenAlex",
        "doi": normalize_doi(raw.get("doi", doi)),
        "title": raw.get("title", ""),
        "authors": [item.get("author", {}).get("display_name", "") for item in raw.get("authorships", [])],
        "year": raw.get("publication_year"),
        "venue": source.get("display_name", ""),
        "type": raw.get("type"),
        "url": raw.get("id"),
        "retrieved_from": url.replace(api_key, "REDACTED") if api_key else url,
    }


def _error(source: str, exc: Exception) -> dict[str, Any]:
    status = getattr(exc, "code", None)
    return {"source": source, "status": "NOT_FOUND" if status == 404 else "UNAVAILABLE", "error": str(exc)}


def verify_reference(ref: dict[str, Any], mailto: str = "", openalex_key: str = "", timeout: float = 20.0) -> dict[str, Any]:
    doi = normalize_doi(str(ref.get("doi", "")))
    if not doi:
        return {"input": ref, "status": "AUTHOR_INPUT_NEEDED", "issues": ["Missing or invalid DOI."], "sources": []}

    sources = []
    for name, lookup in (
        ("Crossref", lambda: crossref_lookup(doi, mailto, timeout)),
        ("OpenAlex", lambda: openalex_lookup(doi, openalex_key, timeout)),
    ):
        try:
            sources.append(lookup())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError) as exc:
            sources.append(_error(name, exc))

    available = [item for item in sources if item.get("title")]
    if not available:
        return {"input": ref, "normalized_doi": doi, "status": "UNVERIFIED", "issues": ["No metadata source returned a record."], "sources": sources}

    issues = []
    input_title = str(ref.get("title", ""))
    similarities = {item["source"]: title_similarity(input_title, item["title"]) for item in available} if input_title else {}
    if input_title and max(similarities.values(), default=0) < 0.9:
        issues.append("Input title does not closely match returned metadata.")
    input_year = ref.get("year")
    years = {item.get("year") for item in available if item.get("year")}
    if input_year and years and int(input_year) not in years:
        issues.append(f"Input year {input_year} differs from source year(s) {sorted(years)}.")
    source_dois = {item.get("doi") for item in available if item.get("doi")}
    if source_dois != {doi}:
        issues.append(f"Source DOI disagreement: {sorted(source_dois)}.")
    if len(available) == 2 and title_similarity(available[0]["title"], available[1]["title"]) < 0.95:
        issues.append("Crossref and OpenAlex titles disagree.")

    return {
        "input": ref,
        "normalized_doi": doi,
        "status": "VERIFIED" if not issues else "MISMATCH",
        "issues": issues,
        "title_similarity": similarities,
        "sources": sources,
        "verified_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "record_hash": hashlib.sha256(json.dumps(available, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
    }


def verify_references(refs: list[dict[str, Any]], mailto: str = "", openalex_key: str = "", timeout: float = 20.0) -> dict[str, Any]:
    results = [verify_reference(ref, mailto, openalex_key, timeout) for ref in refs]
    final = "PASS" if all(item["status"] == "VERIFIED" for item in results) else "WARN"
    return {"final_status": final, "count": len(results), "results": results}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify DOI metadata against Crossref and OpenAlex.")
    parser.add_argument("references", type=Path, help="JSON array or object containing a `references` array.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mailto", default=os.getenv("CROSSREF_MAILTO", ""))
    parser.add_argument("--openalex-key", default=os.getenv("OPENALEX_API_KEY", ""))
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args(argv)
    payload = json.loads(args.references.read_text(encoding="utf-8"))
    refs = payload.get("references", []) if isinstance(payload, dict) else payload
    if not isinstance(refs, list):
        raise SystemExit("Expected a JSON array or an object with a `references` array.")
    report = verify_references(refs, args.mailto, args.openalex_key, args.timeout)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["final_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

