import unittest
from pathlib import Path

from tools.run_benchmark import run
from tools.validate_release import validate


ROOT = Path(__file__).resolve().parents[1]


class BenchmarkTest(unittest.TestCase):
    def test_public_gate_benchmark(self):
        report = run(ROOT / "benchmarks" / "gate-cases.json")
        self.assertGreaterEqual(report["cases"], 8)
        self.assertEqual(report["accuracy"], 1.0)
        committed = __import__("json").loads((ROOT / "benchmarks" / "results.json").read_text(encoding="utf-8"))
        self.assertEqual(committed, report)

    def test_release_integrity(self):
        self.assertEqual(validate(), [])


if __name__ == "__main__":
    unittest.main()
