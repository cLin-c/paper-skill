# paper-skill Tools

These tools make paper-skill more than a prompt collection. They provide lightweight checks that can run before final submission.

## Public Benchmark

```bash
python tools/run_benchmark.py --output benchmarks/results.json
```

This runs the public synthetic safety-gate cases and exits nonzero on any classification mismatch. It intentionally does not claim to measure prose quality or acceptance probability.

## Stage-Gate Checker

Run:

```bash
python tools/paper_skill_gate.py examples/submission-package-check.json
```

The checker validates seven gates:

| Gate | Checks |
|---|---|
| `identity` | Title, target journal, paper type, Chinese source summary |
| `provenance` | Authoritative source files and precedence |
| `claim-evidence` | Every claim links only to existing evidence records |
| `citation-integrity` | Titles, claim links, DOI shape, and verification audit trail |
| `reporting-guideline` | Study-design routing and item-level checklist presence |
| `submission-package` | English abstract, cover letter, highlights, declarations |
| `unresolved-inputs` | Remaining `AUTHOR_INPUT_NEEDED` markers |

Machine-readable and strict modes:

```bash
python tools/paper_skill_gate.py package.json --format json
python tools/paper_skill_gate.py package.json --strict
```

Exit code:

| Code | Meaning |
|---|---|
| `0` | No failing gate; warnings are allowed unless `--strict` is used |
| `1` | A gate failed, or a warning exists under `--strict` |

This is intentionally conservative. It does not prove that a manuscript is correct; it catches missing structure before a human or AI reviewer spends time polishing the wrong thing.

## Online and cross-file verification

| Tool | Purpose |
|---|---|
| `scholarly_verify.py` | Resolve DOI metadata from Crossref and OpenAlex; compare DOI, title, and year |
| `journal_policy_verify.py` | Fetch user-confirmed official HTTPS policy pages and preserve snippets, access time, and SHA-256 |
| `revision_trace.py` | Check response-matrix locations and revised text against TXT/Markdown/LaTeX/DOCX/PDF manuscripts |
| `run_full_workflow.py` | Run submission gates, references, policies, and revision tracing together |

See `workflows/full-verification.md` and `examples/full-workflow-config.json`.
