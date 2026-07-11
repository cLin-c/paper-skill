import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.revision_trace import extract_text, verify_revision


class RevisionTraceTest(unittest.TestCase):
    def test_exact_revision_and_location_pass(self):
        manuscript = "Section 3.2 Results\nThe proposed method reduced error by 12 percent."
        entries = [{"comment_id": "R1.1", "location": "Section 3.2", "revised_text": "The proposed method reduced error by 12 percent."}]
        self.assertEqual(verify_revision(manuscript, entries)["final_status"], "PASS")

    def test_missing_revision_fails(self):
        manuscript = "Section 3.2 Results\nNo new sentence here."
        entries = [{"comment_id": "R1.1", "location": "Section 3.2", "revised_text": "Added robustness experiment."}]
        self.assertEqual(verify_revision(manuscript, entries)["final_status"], "FAIL")

    def test_docx_extraction(self):
        xml = b'<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Section 2</w:t></w:r></w:p></w:body></w:document>'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "paper.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("word/document.xml", xml)
            self.assertIn("Section 2", extract_text(path))


if __name__ == "__main__":
    unittest.main()

