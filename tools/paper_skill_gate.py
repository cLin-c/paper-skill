#!/usr/bin/env python3
"""Zero-dependency, machine-readable stage gates for paper submission packages."""

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


def gate_provenance(data: dict[str, Any]) -> GateResult:
    sources = _as_list(data.get("source_files"))
    if not sources:
        return GateResult(
            "provenance",
            WARN,
            "No authoritative source-file manifest is recorded.",
            ["Add `source_files` with path/name, version, and role for every manuscript, dataset, figure, or response source."],
        )

    fixes = []
    authoritative = 0
    for index, source in enumerate(sources, start=1):
        if not isinstance(source, dict):
            fixes.append(f"Source #{index} must be an object.")
            continue
        if not _text(source.get("name")):
            fixes.append(f"Source #{index} is missing `name`.")
        if source.get("authoritative") is True:
            authoritative += 1
    if authoritative == 0:
        fixes.append("Mark at least one manuscript/source as `authoritative: true`.")
    if authoritative > 1 and not _text(data.get("source_precedence")):
        fixes.append("Multiple authoritative sources require a `source_precedence` rule.")

    if fixes:
        return GateResult("provenance", WARN, "Source provenance is ambiguous.", fixes)
    return GateResult("provenance", PASS, "Source provenance and authority are recorded.", [])


def gate_claim_evidence(data: dict[str, Any]) -> GateResult:
    claims = _as_list(data.get("claims"))
    evidence = _as_list(data.get("evidence"))
    unsupported = []
    broken_links = []

    evidence_ids = {str(item.get("id")) for item in evidence if isinstance(item, dict) and item.get("id")}
    for claim in claims:
        if not isinstance(claim, dict):
            continue
        claim_id = str(claim.get("id", "unknown"))
        linked = {str(item) for item in _as_list(claim.get("evidence_ids"))}
        if not linked:
            unsupported.append(claim_id)
        missing = linked.difference(evidence_ids)
        if missing:
            broken_links.append((claim_id, sorted(missing)))

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

    if broken_links:
        return GateResult(
            "claim-evidence",
            FAIL,
            "Some claims point to evidence records that do not exist.",
            [f"Claim `{claim_id}` has missing evidence ids: {', '.join(ids)}." for claim_id, ids in broken_links],
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
        if doi and not re.match(r"^10\.\d{4,9}/[-._;()/:A-Z0-9]+$", doi, re.IGNORECASE):
            fixes.append(f"Reference #{index} DOI format looks suspicious: `{doi}`.")
        verification = _text(ref.get("verification_status"))
        if verification and verification not in {"VERIFIED", "UNVERIFIED"}:
            fixes.append(f"Reference #{index} has invalid verification_status `{verification}`.")
        if verification == "VERIFIED" and not (_text(ref.get("verified_source")) and _text(ref.get("accessed_at"))):
            fixes.append(f"Reference #{index} is marked VERIFIED without verified_source and accessed_at.")

    if fixes:
        return GateResult("citation-integrity", WARN, "Citation metadata needs review.", fixes)

    return GateResult("citation-integrity", PASS, "Reference metadata and claim links are present.", [])


def gate_reporting(data: dict[str, Any]) -> GateResult:
    study_design = _text(data.get("study_design")).lower()
    if not study_design:
        return GateResult(
            "reporting-guideline",
            WARN,
            "Study design is not recorded, so reporting-guideline applicability cannot be checked.",
            ["Add `study_design` and, when applicable, `reporting_guideline` plus `reporting_checklist`."],
        )

    routed = {
        "randomized trial": "CONSORT",
        "trial protocol": "SPIRIT",
        "systematic review": "PRISMA",
        "meta-analysis": "PRISMA",
        "observational": "STROBE",
        "animal": "ARRIVE",
        "case report": "CARE",
        "diagnostic accuracy": "STARD",
        "prediction model": "TRIPOD",
    }
    expected = next((guide for key, guide in routed.items() if key in study_design), "")
    if not expected:
        return GateResult("reporting-guideline", PASS, "No built-in reporting guideline was inferred for this study design.", [])

    supplied = _text(data.get("reporting_guideline")).upper()
    checklist = _as_list(data.get("reporting_checklist"))
    fixes = []
    if supplied != expected:
        fixes.append(f"Expected `{expected}` for study design `{study_design}`; confirm the current official guideline.")
    if not checklist:
        fixes.append("Add an item-level `reporting_checklist` with manuscript locations and statuses.")
    if fixes:
        return GateResult("reporting-guideline", WARN, "Reporting-guideline evidence is incomplete.", fixes)
    return GateResult("reporting-guideline", PASS, f"{expected} routing and checklist are recorded.", [])


def gate_unresolved(data: dict[str, Any]) -> GateResult:
    encoded = json.dumps(data, ensure_ascii=False)
    count = encoded.count("[AUTHOR_INPUT_NEEDED:")
    if count:
        return GateResult(
            "unresolved-inputs",
            WARN,
            f"The package contains {count} unresolved author-input marker(s).",
            ["Resolve each marker or explicitly accept it as a submission blocker."],
        )
    return GateResult("unresolved-inputs", PASS, "No unresolved author-input markers were found.", [])


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
        gate_provenance(data),
        gate_claim_evidence(data),
        gate_citations(data),
        gate_reporting(data),
        gate_submission_package(data),
        gate_unresolved(data),
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


def final_status(results: list[GateResult]) -> str:
    return FAIL if any(item.status == FAIL for item in results) else WARN if any(item.status == WARN for item in results) else PASS


def as_json(results: list[GateResult]) -> str:
    return json.dumps(
        {
            "final_status": final_status(results),
            "gates": [
                {"gate": item.gate, "status": item.status, "message": item.message, "fixes": item.fixes}
                for item in results
            ],
        },
        ensure_ascii=False,
        indent=2,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a paper-skill submission package JSON file.")
    parser.add_argument("package", type=Path, help="Path to a JSON submission package.")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--strict", action="store_true", help="Return nonzero for WARN as well as FAIL.")
    args = parser.parse_args(argv)

    with args.package.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("Package root must be a JSON object.")

    results = evaluate(data)
    print(as_json(results) if args.format == "json" else render(results))
    status = final_status(results)
    return 1 if status == FAIL or (args.strict and status == WARN) else 0


if __name__ == "__main__":
    sys.exit(main())
