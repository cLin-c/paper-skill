# paper-skill Tools

These tools make paper-skill more than a prompt collection. They provide lightweight checks that can run before final submission.

## Stage-Gate Checker

Run:

```bash
python tools/paper_skill_gate.py examples/submission-package-check.json
```

The checker validates four gates:

| Gate | Checks |
|---|---|
| `identity` | Title, target journal, paper type, Chinese source summary |
| `claim-evidence` | Every claim links to evidence |
| `citation-integrity` | References include titles, supported claims, and DOI-shape checks |
| `submission-package` | English abstract, cover letter, highlights, declarations |

Exit code:

| Code | Meaning |
|---|---|
| `0` | No failing gate |
| `1` | At least one failing gate |

This is intentionally conservative. It does not prove that a manuscript is correct; it catches missing structure before a human or AI reviewer spends time polishing the wrong thing.
