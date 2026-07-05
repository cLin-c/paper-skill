#!/usr/bin/env python3
"""Zero-dependency stage-gate checker for paper-skill submission packages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass
class GateResult:
    gate: str
    status: str
    message: str
    fixes: list[str]


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _text(value: Any) -> str:
    return value.strip() if isinstance(value, str) else ""


def _has_author_input_marker(value: Any) -> bool:
    return "[AUTHOR_INPUT_NEEDED:" in json.dumps(value, ensure_ascii=False)


def _contains_cjk(value: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", value))


def gate_identity(data: dict[str, Any]) -> GateResult:
    required = ["title", "target_journal", "paper_type", "chinese_source_summary"]
    missing = [field for field in required if not _text(data.get(field))]
    if missing:
        return GateResult(
            "identity",
            FAIL,
            "Submission identity is incomplete.",
            [f"Fill `{field}` before drafting submission materials." for field in missing],
        )

    if not _contains_cjk(_text(data.get("chinese_source_summary"))):
        return GateResult(
            "identity",
            WARN,
            "Chinese-first source summary is missing or not visibly Chinese.",
            ["Add the original Chinese research summary so translation choices remain traceable."],
        )

    return GateResult("identity", PASS, "Paper identity and Chinese source summary are present.", [])


def gate_claim_evidence(data: dict[str, Any]) -> GateResult:
    claims = _as_list(data.get("claims"))
    evidence = _as_list(data.get("evidence"))
    unsupported = []

    evidence_ids = {str(item.get("id")) for item in evidence if isinstance(item, dict) and item.get("id")}
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        claim_id = str(claim.get("id", "unknown"))
        linked = {str(item) for item in _as_list(claim.get("evidence_ids"))}
        if not linked or not linked.intersection(evidence_ids):
            unsupported.append(claim_id)

    if not claims:
        return GateResult(
            "claim-evidence",
            FAIL,
            "No claim list found.",
            ["Add `claims` with `id`, `text`, and `evidence_ids` fields."],
        )

    if unsupported:
        return GateResult(
            "claim-evidence",
            FAIL,
            "Some claims are not linked to evidence.",
            [f"Add evidence mapping for claim `{claim_id}`." for claim_id in unsupported],
        )

    if _has_author_input_marker(data):
        return GateResult(
            "claim-evidence",
            WARN,
            "The package still contains AUTHOR_INPUT_NEEDED markers.",
            ["Resolve missing baselines, metrics, dataset details, or journal-specific requirements."],
        )

    return GateResult("claim-evidence", PASS, "All listed claims have evidence links.", [])


def gate_citations(data: dict[str, Any]) -> GateResult:
    refs = _as_list(data.get("references"))
    if not refs:
        return GateResult(
            "citation-integrity",
            FAIL,
            "No references found.",
            ["Add references with title, DOI if available, and supported claim ids."],
        )

    fixes: list[str] = []
    for index, ref in enumerate(refs, start=1):
        if not isinstance(ref, dict):
            fixes.append(f"Reference #{index} must be an object.")
            continue
        if not _text(ref.get("title")):
            fixes.append(f"Reference #{index} is missing title.")
        if not _as_list(ref.get("supports_claims")):
            fixes.append(f"Reference #{index} is not linked to any claim.")
        doi = _text(ref.get("doi"))
        if doi and not re.match(r"^10\.\S+/\S+$", doi):
            fixes.append(f"Reference #{index} DOI format looks suspicious: `{doi}`.")

    if fixes:
        return GateResult("citation-integrity", WARN, "Citation metadata needs review.", fixes)

    return GateResult("citation-integrity", PASS, "Reference metadata and claim links are present.", [])


def gate_submission_package(data: dict[str, Any]) -> GateResult:
    required = ["english_abstract", "cover_letter", "highlights", "declarations"]
    missing = [field for field in required if not data.get(field)]
    if missing:
        return GateResult(
            "submission-package",
            FAIL,
            "Submission package is incomplete.",
            [f"Add `{field}` before final submission." for field in missing],
        )

    abstract = _text(data.get("english_abstract"))
    if len(abstract.split()) < 80:
        return GateResult(
            "submission-package",
            WARN,
            "English abstract is very short for a journal submission.",
            ["Expand the abstract with problem, method, evidence, and contribution."],
        )

    return GateResult("submission-package", PASS, "Core submission artifacts are present.", [])


def evaluate(data: dict[str, Any]) -> list[GateResult]:
    return [
        gate_identity(data),
        gate_claim_evidence(data),
        gate_citations(data),
        gate_submission_package(data),
    ]


def render(results: list[GateResult]) -> str:
    lines = ["# paper-skill stage-gate report", ""]
    for result in results:
        lines.append(f"## {result.status} - {result.gate}")
        lines.append("")
        lines.append(result.message)
        if result.fixes:
            lines.append("")
            lines.extend(f"- {fix}" for fix in result.fixes)
        lines.append("")
    final = FAIL if any(item.status == FAIL for item in results) else WARN if any(item.status == WARN for item in results) else PASS
    lines.append(f"Final status: {final}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a paper-skill submission package JSON file.")
    parser.add_argument("package", type=Path, help="Path to a JSON submission package.")
    args = parser.parse_args(argv)

    with args.package.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Package root must be a JSON object.")

    results = evaluate(data)
    print(render(results))
    return 1 if any(item.status == FAIL for item in results) else 0


if __name__ == "__main__":
    sys.exit(main())
