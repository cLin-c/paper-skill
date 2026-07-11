import unittest

from tools.paper_skill_gate import FAIL, PASS, WARN, as_json, evaluate


class PaperSkillGateTest(unittest.TestCase):
    def test_complete_package_passes(self):
        data = {
            "title": "Robust Graph Planning for Field Robots",
            "target_journal": "IEEE TRO",
            "paper_type": "methods",
            "chinese_source_summary": "本文提出一种面向野外机器人的鲁棒图规划方法。",
            "source_files": [{"name": "manuscript.docx", "version": "v3", "authoritative": True}],
            "study_design": "methods paper",
            "english_abstract": "Field robots often fail when planners are evaluated only in clean simulation settings. This study introduces a robust graph planning framework that combines uncertainty-aware edge weighting, online map repair, and route-level consistency checks. Experiments on outdoor navigation logs show improved completion rate and reduced replanning frequency across cluttered and partially observed environments. The results suggest that explicitly modeling graph uncertainty can improve deployment robustness without changing the robot hardware. The package also documents the remaining failure cases so that the final manuscript can avoid overstating generalization beyond the collected field logs.",
            "claims": [{"id": "C1", "text": "The method improves completion rate.", "evidence_ids": ["E1"]}],
            "evidence": [{"id": "E1", "type": "experiment", "summary": "Outdoor navigation benchmark."}],
            "references": [{"title": "Graph planning survey", "doi": "10.1000/test.1", "supports_claims": ["C1"]}],
            "cover_letter": "Dear Editor...",
            "highlights": ["Uncertainty-aware graph planning.", "Outdoor robot evaluation."],
            "declarations": {"conflict_of_interest": "None declared."},
        }

        statuses = [item.status for item in evaluate(data)]

        self.assertEqual(statuses, [PASS, PASS, PASS, PASS, PASS, PASS, PASS])

    def test_missing_evidence_fails(self):
        data = {
            "title": "Draft",
            "target_journal": "SCI journal",
            "paper_type": "methods",
            "chinese_source_summary": "中文摘要。",
            "english_abstract": "Too short.",
            "claims": [{"id": "C1", "text": "Strong claim.", "evidence_ids": []}],
            "evidence": [],
            "references": [],
        }

        statuses = [item.status for item in evaluate(data)]

        self.assertIn(FAIL, statuses)

    def test_suspicious_doi_warns(self):
        data = {
            "title": "Draft",
            "target_journal": "SCI journal",
            "paper_type": "methods",
            "chinese_source_summary": "中文摘要。",
            "english_abstract": "This abstract has enough context to pass the length warning only when it is expanded with problem, method, evidence, and contribution for a target journal submission. It remains synthetic but complete enough for the test fixture.",
            "claims": [{"id": "C1", "text": "Claim.", "evidence_ids": ["E1"]}],
            "evidence": [{"id": "E1", "summary": "Evidence."}],
            "references": [{"title": "Paper", "doi": "bad-doi", "supports_claims": ["C1"]}],
            "cover_letter": "Dear Editor...",
            "highlights": ["A highlight."],
            "declarations": {"conflict_of_interest": "None declared."},
        }

        statuses = [item.status for item in evaluate(data)]

        self.assertIn(WARN, statuses)

    def test_broken_evidence_link_fails(self):
        data = {
            "title": "Draft",
            "target_journal": "Journal",
            "paper_type": "methods",
            "chinese_source_summary": "中文摘要。",
            "claims": [{"id": "C1", "text": "Claim", "evidence_ids": ["E404"]}],
            "evidence": [{"id": "E1", "summary": "Existing evidence"}],
            "references": [{"title": "Paper", "supports_claims": ["C1"]}],
        }
        results = evaluate(data)
        self.assertEqual(next(item.status for item in results if item.gate == "claim-evidence"), FAIL)

    def test_verified_reference_requires_audit_trail(self):
        data = {
            "title": "Draft",
            "target_journal": "Journal",
            "paper_type": "methods",
            "chinese_source_summary": "中文摘要。",
            "claims": [{"id": "C1", "text": "Claim", "evidence_ids": ["E1"]}],
            "evidence": [{"id": "E1", "summary": "Evidence"}],
            "references": [{"title": "Paper", "supports_claims": ["C1"], "verification_status": "VERIFIED"}],
        }
        results = evaluate(data)
        citation_gate = next(item for item in results if item.gate == "citation-integrity")
        self.assertEqual(citation_gate.status, WARN)
        self.assertIn("verified_source", " ".join(citation_gate.fixes))

    def test_json_output_is_machine_readable(self):
        payload = as_json(evaluate({}))
        self.assertIn('"final_status": "FAIL"', payload)


if __name__ == "__main__":
    unittest.main()
