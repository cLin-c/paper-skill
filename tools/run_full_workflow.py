#!/usr/bin/env python3
"""Run paper-skill verification stages from one JSON configuration."""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

from journal_policy_verify import verify_policy_config
from paper_skill_gate import evaluate, final_status
from revision_trace import extract_text, verify_revision
from scholarly_verify import verify_references


def _load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run(config: dict[str, Any], base: Path) -> dict[str, Any]:
    stages: dict[str, Any] = {}

    package_path = base / config["submission_package"]
    package = _load(package_path)
    gates = evaluate(package)
    stages["submission_gates"] = {
        "final_status": final_status(gates),
        "gates": [{"gate": g.gate, "status": g.status, "message": g.message, "fixes": g.fixes} for g in gates],
    }

    references = package.get("references", [])
    stages["reference_verification"] = verify_references(
        references,
        os.getenv("CROSSREF_MAILTO", ""),
        os.getenv("OPENALEX_API_KEY", ""),
        float(config.get("network_timeout", 20)),
    )

    policy_path = config.get("journal_policy_config")
    if policy_path:
        stages["journal_policy_verification"] = verify_policy_config(_load(base / policy_path), float(config.get("network_timeout", 25)))
    else:
        stages["journal_policy_verification"] = {"final_status": "SKIPPED", "reason": "No journal_policy_config supplied."}

    manuscript_path = config.get("revised_manuscript")
    matrix_path = config.get("response_matrix")
    if manuscript_path and matrix_path:
        matrix = _load(base / matrix_path)
        entries = matrix.get("responses", []) if isinstance(matrix, dict) else matrix
        stages["revision_trace"] = verify_revision(extract_text(base / manuscript_path), entries, float(config.get("revision_threshold", 0.9)))
    else:
        stages["revision_trace"] = {"final_status": "SKIPPED", "reason": "No revised_manuscript/response_matrix pair supplied."}

    blocking = [name for name, value in stages.items() if value.get("final_status") in {"FAIL", "WARN"}]
    return {
        "workflow_version": "0.5",
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "final_status": "PASS" if not blocking else "NOT_READY",
        "blocking_or_warning_stages": blocking,
        "stages": stages,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the complete paper-skill verification workflow.")
    parser.add_argument("config", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    config_path = args.config.resolve()
    report = run(_load(config_path), config_path.parent)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["final_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

