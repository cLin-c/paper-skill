# paper-skill Examples

These examples are designed for README links, GitHub visitors, and social sharing. Each example shows a practical input, the expected workflow, and the kind of output paper-skill should produce.

## Examples

| Example | Best for | File |
|---|---|---|
| Chinese abstract to English | Users who write in Chinese but submit in English | [chinese-abstract-to-english.md](chinese-abstract-to-english.md) |
| Reviewer response | Users preparing R&R or rebuttal replies | [reviewer-response.md](reviewer-response.md) |
| Citation integrity audit | Users worried about hallucinated citations and over-claims | [citation-integrity-audit.md](citation-integrity-audit.md) |
| Full submission package | Users preparing a complete pre-submission package | [full-submission-package.md](full-submission-package.md) |
| Before / after Chinese abstract | Visitors who want to see output quality immediately | [before-after-chinese-abstract.md](before-after-chinese-abstract.md) |
| Before / after reviewer response | Visitors comparing weak replies with traceable R&R replies | [reviewer-response-before-after.md](reviewer-response-before-after.md) |
| Before / after citation audit | Visitors evaluating citation safety behavior | [citation-audit-before-after.md](citation-audit-before-after.md) |
| Runnable submission package check | Users who want an executable validation example | [submission-package-check.json](submission-package-check.json) |
| Section-level before/after rewrites | Users improving Abstract, Introduction, Related Work, Method, Experiments, and Discussion | [section-rewrites.md](section-rewrites.md) |

## Recommended Demo Flow

1. Start with `chinese-abstract-to-english.md` because the pain point is immediate.
2. Show `reviewer-response.md` to demonstrate submission-stage value.
3. Finish with `citation-integrity-audit.md` to show quality and safety differentiation.
4. Use the before/after examples to make output quality visible without a long explanation.
5. Run `python tools/paper_skill_gate.py examples/submission-package-check.json` for the executable stage-gate demo.

## Copyable First Prompt

```text
Use $paper-skill. My manuscript is written in Chinese and targets an SCI / IEEE journal. First identify the paper type, then rewrite the abstract in academic English, flag unsupported claims, and list the information I must provide. Do not invent data or references.
```
