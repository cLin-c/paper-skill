#!/usr/bin/env python3
"""Capture auditable evidence from official journal policy pages."""

from __future__ import annotations

import argparse
import hashlib
import html
import ipaddress
import json
import re
import socket
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


USER_AGENT = "paper-skill/0.5 (+https://github.com/cLin-c/paper-skill)"


def _safe_public_https(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not parsed.hostname:
        raise ValueError("Policy URL must use HTTPS and include a hostname.")
    for info in socket.getaddrinfo(parsed.hostname, 443, type=socket.SOCK_STREAM):
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            raise ValueError(f"Refusing non-public policy host address: {ip}")


def _plain_text(raw: bytes, content_type: str) -> str:
    charset_match = re.search(r"charset=([\w-]+)", content_type, re.I)
    charset = charset_match.group(1) if charset_match else "utf-8"
    text = raw.decode(charset, errors="replace")
    text = re.sub(r"(?is)<(script|style|noscript).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def fetch_policy(url: str, timeout: float = 25.0) -> dict[str, Any]:
    _safe_public_https(url)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,text/plain"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final_url = response.geturl()
        _safe_public_https(final_url)
        raw = response.read(5_000_001)
        if len(raw) > 5_000_000:
            raise ValueError("Policy page exceeds 5 MB safety limit.")
        text = _plain_text(raw, response.headers.get("Content-Type", ""))
        return {
            "url": url,
            "final_url": final_url,
            "http_status": getattr(response, "status", 200),
            "retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "content_sha256": hashlib.sha256(raw).hexdigest(),
            "text": text,
        }


def _snippets(text: str, terms: list[str], radius: int = 180) -> list[str]:
    snippets = []
    lowered = text.casefold()
    for term in terms:
        index = lowered.find(term.casefold())
        if index >= 0:
            snippets.append(text[max(0, index - radius): min(len(text), index + len(term) + radius)].strip())
    return list(dict.fromkeys(snippets))[:5]


def verify_policy_config(config: dict[str, Any], timeout: float = 25.0) -> dict[str, Any]:
    journal = config.get("journal", "")
    pages = config.get("pages", [])
    results = []
    for page in pages:
        url = str(page.get("url", ""))
        categories = page.get("categories", {})
        try:
            fetched = fetch_policy(url, timeout)
            evidence = {}
            for category, terms in categories.items():
                hits = _snippets(fetched["text"], [str(term) for term in terms])
                evidence[category] = {"status": "EVIDENCE_FOUND" if hits else "UNVERIFIED", "terms": terms, "snippets": hits}
            fetched.pop("text")
            results.append({**fetched, "official_domain_confirmed_by_user": bool(page.get("official_domain_confirmed_by_user")), "evidence": evidence})
        except Exception as exc:
            results.append({"url": url, "status": "UNAVAILABLE", "error": str(exc), "evidence": {}})
    all_confirmed = results and all(item.get("official_domain_confirmed_by_user") for item in results if item.get("http_status"))
    any_unavailable = any(item.get("status") == "UNAVAILABLE" for item in results)
    evidence_states = [
        evidence.get("status")
        for item in results
        for evidence in item.get("evidence", {}).values()
    ]
    all_requested_evidence_found = bool(evidence_states) and all(state == "EVIDENCE_FOUND" for state in evidence_states)
    return {
        "journal": journal,
        "final_status": "PASS" if all_confirmed and not any_unavailable and all_requested_evidence_found else "WARN",
        "interpretation_rule": "Keyword hits are evidence excerpts, not automatic proof of policy compliance.",
        "all_requested_evidence_found": all_requested_evidence_found,
        "pages": results,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Capture journal policy evidence from supplied official URLs.")
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--timeout", type=float, default=25.0)
    args = parser.parse_args(argv)
    config = json.loads(args.config.read_text(encoding="utf-8"))
    report = verify_policy_config(config, args.timeout)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["final_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
