#!/usr/bin/env python3
"""Run the transparent deterministic safety-gate benchmark."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from paper_skill_gate import evaluate, final_status
except ModuleNotFoundError:  # Imported as tools.run_benchmark in the test suite.
    from tools.paper_skill_gate import evaluate, final_status


def run(path: Path) -> dict[str, object]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for case in cases:
        actual = final_status(evaluate(case["package"]))
        rows.append({"id": case["id"], "expected": case["expected"], "actual": actual, "correct": actual == case["expected"]})
    correct = sum(row["correct"] for row in rows)
    return {
        "benchmark": "paper-skill deterministic safety gates",
        "scope": "Structured package risk classification; not prose quality or acceptance prediction.",
        "cases": len(rows),
        "correct": correct,
        "accuracy": correct / len(rows) if rows else 0.0,
        "results": rows,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", nargs="?", type=Path, default=Path("benchmarks/gate-cases.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    report = run(args.cases)
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    print(payload)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    return 0 if report["correct"] == report["cases"] else 1


if __name__ == "__main__":
    sys.exit(main())
