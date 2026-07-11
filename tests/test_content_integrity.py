import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ContentIntegrityTest(unittest.TestCase):
    def test_skill_relative_markdown_links_exist(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", text)
        missing = []
        for link in links:
            if "://" in link or link.startswith("#"):
                continue
            target = (ROOT / link.split("#", 1)[0]).resolve()
            if not target.exists():
                missing.append(link)
        self.assertEqual(missing, [])

    def test_all_section_guides_are_routed(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        guides = sorted((ROOT / "references" / "section-guides").glob("*.md"))
        self.assertGreaterEqual(len(guides), 7)
        for guide in guides:
            self.assertIn(f"references/section-guides/{guide.name}", skill)

    def test_examples_are_explicitly_synthetic(self):
        text = (ROOT / "examples" / "section-rewrites.md").read_text(encoding="utf-8").casefold()
        self.assertIn("synthetic", text)
        self.assertIn("author_input_needed", text)


if __name__ == "__main__":
    unittest.main()

