#!/usr/bin/env python3
"""Verify that response-letter claims exist in the revised manuscript."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
import zipfile
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any
from xml.etree import ElementTree


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".txt", ".md", ".tex", ".rst"}:
        return path.read_text(encoding="utf-8", errors="replace")
    if suffix == ".docx":
        with zipfile.ZipFile(path) as archive:
            root = ElementTree.fromstring(archive.read("word/document.xml"))
        paragraphs = []
        ns = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
        for paragraph in root.iter(ns + "p"):
            paragraphs.append("".join(node.text or "" for node in paragraph.iter(ns + "t")))
        return "\n".join(paragraphs)
    if suffix == ".pdf":
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as handle:
            output = Path(handle.name)
        try:
            subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(path), str(output)], check=True, capture_output=True)
            return output.read_text(encoding="utf-8", errors="replace")
        finally:
            output.unlink(missing_ok=True)
    raise ValueError(f"Unsupported manuscript format: {suffix}")


def _best_similarity(needle: str, manuscript: str) -> float:
    target = normalize(needle)
    text = normalize(manuscript)
    if not target:
        return 0.0
    if target in text:
        return 1.0
    words = text.split()
    size = max(1, len(target.split()))
    best = 0.0
    for start in range(0, max(1, len(words) - size + 1), max(1, size // 5)):
        candidate = " ".join(words[start:start + size])
        best = max(best, SequenceMatcher(None, target, candidate).ratio())
    return round(best, 4)


def verify_revision(manuscript_text: str, entries: list[dict[str, Any]], threshold: float = 0.9) -> dict[str, Any]:
    results = []
    normalized_manuscript = normalize(manuscript_text)
    for index, entry in enumerate(entries, start=1):
        comment_id = str(entry.get("comment_id") or f"ENTRY-{index}")
        revised_text = str(entry.get("revised_text", ""))
        location = str(entry.get("location", ""))
        issues = []
        if not revised_text:
            issues.append("Missing revised_text; cannot verify the claimed change.")
            similarity = 0.0
        else:
            similarity = _best_similarity(revised_text, manuscript_text)
            if similarity < threshold:
                issues.append(f"Revised text not found at threshold {threshold:.2f} (best={similarity:.2f}).")
        location_found = normalize(location) in normalized_manuscript if location else False
        if not location:
            issues.append("Missing location.")
        elif not location_found:
            issues.append("Declared location label was not found in the manuscript text.")
        results.append({
            "comment_id": comment_id,
            "status": "VERIFIED" if not issues else "MISMATCH",
            "location": location,
            "location_found": location_found,
            "text_similarity": similarity,
            "issues": issues,
        })
    return {
        "final_status": "PASS" if results and all(item["status"] == "VERIFIED" for item in results) else "FAIL",
        "entries": results,
        "verified_count": sum(item["status"] == "VERIFIED" for item in results),
        "total_count": len(results),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify response-letter revisions against a manuscript.")
    parser.add_argument("manuscript", type=Path, help="Revised manuscript (.txt/.md/.tex/.docx/.pdf).")
    parser.add_argument("response_matrix", type=Path, help="JSON array or object with a `responses` array.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--threshold", type=float, default=0.9)
    args = parser.parse_args(argv)
    payload = json.loads(args.response_matrix.read_text(encoding="utf-8"))
    entries = payload.get("responses", []) if isinstance(payload, dict) else payload
    if not isinstance(entries, list):
        raise SystemExit("Expected a JSON array or object with a `responses` array.")
    report = verify_revision(extract_text(args.manuscript), entries, args.threshold)
    report["manuscript"] = str(args.manuscript)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["final_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

