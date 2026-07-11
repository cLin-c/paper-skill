# Executable Toolchain

paper-skill is moving from a prompt-only library toward a verifiable submission workflow.

## What Runs Today

| Tool | Command | Purpose |
|---|---|---|
| Stage-gate checker | `python tools/paper_skill_gate.py examples/submission-package-check.json` | Checks whether a submission package has the minimum structure for paper-skill review |
| JSON report | `python tools/paper_skill_gate.py package.json --format json` | Emits results suitable for CI and other agents |
| Strict gate | `python tools/paper_skill_gate.py package.json --strict` | Treats unresolved warnings as a nonzero result |
| Unit tests | `python -m unittest discover -s tests` | Guards the checker behavior |

## Stage-Gate Philosophy

The checker follows the same editorial policy as the skill:

- Do not polish unsupported claims.
- Do not let citations float without claim links.
- Do not treat an English abstract as submission-ready until the source, evidence, cover letter, highlights, and declarations are visible.
- Mark missing facts before improving style.

## Recommended Workflow

1. Use `$paper-skill` to build a submission package draft.
2. Save the package as JSON using the shape in `examples/submission-package-check.json`.
3. Run the stage-gate checker.
4. Resolve every `FAIL` before asking for final polishing.
5. Treat every `WARN` as a human-review item.

## Roadmap

- Add Markdown and DOCX package parsing.
- Add reference DOI lookup as an optional networked check.
- Add journal-policy profiles sourced from official pages with access dates.
- Add manuscript/rebuttal cross-file location verification.
