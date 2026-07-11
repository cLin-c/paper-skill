import unittest
from unittest.mock import patch

from tools.scholarly_verify import normalize_doi, title_similarity, verify_reference


class ScholarlyVerifyTest(unittest.TestCase):
    def test_normalize_doi(self):
        self.assertEqual(normalize_doi("https://doi.org/10.1234/ABC.1"), "10.1234/abc.1")

    def test_title_similarity_normalizes_case_and_punctuation(self):
        self.assertGreater(title_similarity("A Study: of Robots", "a study of robots"), 0.99)

    @patch("tools.scholarly_verify.openalex_lookup")
    @patch("tools.scholarly_verify.crossref_lookup")
    def test_two_source_match_verifies(self, crossref, openalex):
        record = {"doi": "10.1234/a", "title": "Robot Planning", "authors": ["A Author"], "year": 2025, "venue": "Journal"}
        crossref.return_value = {"source": "Crossref", **record}
        openalex.return_value = {"source": "OpenAlex", **record}
        result = verify_reference({"doi": "10.1234/a", "title": "Robot Planning", "year": 2025})
        self.assertEqual(result["status"], "VERIFIED")

    @patch("tools.scholarly_verify.openalex_lookup")
    @patch("tools.scholarly_verify.crossref_lookup")
    def test_title_mismatch_is_reported(self, crossref, openalex):
        crossref.return_value = {"source": "Crossref", "doi": "10.1234/a", "title": "Different Paper", "year": 2025}
        openalex.return_value = {"source": "OpenAlex", "doi": "10.1234/a", "title": "Different Paper", "year": 2025}
        result = verify_reference({"doi": "10.1234/a", "title": "Robot Planning", "year": 2025})
        self.assertEqual(result["status"], "MISMATCH")


if __name__ == "__main__":
    unittest.main()

