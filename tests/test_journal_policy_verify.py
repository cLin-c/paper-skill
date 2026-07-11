import unittest

from unittest.mock import patch

from tools.journal_policy_verify import _plain_text, _snippets, verify_policy_config


class JournalPolicyVerifyTest(unittest.TestCase):
    def test_html_text_and_snippet(self):
        text = _plain_text(b"<html><style>x</style><body>Authors must provide a data availability statement.</body></html>", "text/html; charset=utf-8")
        snippets = _snippets(text, ["data availability"])
        self.assertEqual(len(snippets), 1)
        self.assertIn("Authors must provide", snippets[0])

    def test_script_content_removed(self):
        text = _plain_text(b"<script>fake policy</script><p>Real policy</p>", "text/html")
        self.assertNotIn("fake", text)

    @patch("tools.journal_policy_verify.fetch_policy")
    def test_missing_evidence_is_warning(self, fetch):
        fetch.return_value = {
            "url": "https://journal.example/policy",
            "final_url": "https://journal.example/policy",
            "http_status": 200,
            "retrieved_at": "2026-01-01T00:00:00Z",
            "content_sha256": "abc",
            "text": "A page without the requested phrase.",
        }
        config = {
            "journal": "Example",
            "pages": [{
                "url": "https://journal.example/policy",
                "official_domain_confirmed_by_user": True,
                "categories": {"data": ["data availability"]},
            }],
        }
        report = verify_policy_config(config)
        self.assertEqual(report["final_status"], "WARN")
        self.assertFalse(report["all_requested_evidence_found"])


if __name__ == "__main__":
    unittest.main()
