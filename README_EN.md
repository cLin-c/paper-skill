# paper-skill

> The evidence-first publication workflow for researchers who draft and think in Chinese.

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![CI](https://github.com/cLin-c/paper-skill/actions/workflows/toolchain.yml/badge.svg)](https://github.com/cLin-c/paper-skill/actions/workflows/toolchain.yml)
[![Version](https://img.shields.io/badge/version-0.8.2-2563EB)](VERSION)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

<p align="center">
  <img src="assets/paper-skill-hero.png" alt="paper-skill evidence-first publication workflow" width="100%">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Google%20Scholar-literature%20map-0B57D0?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar literature map">
  <img src="https://img.shields.io/badge/arXiv-preprint%20workflow-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv preprint workflow">
  <img src="https://img.shields.io/badge/LaTeX-manuscript%20ready-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX manuscript ready">
  <img src="https://img.shields.io/badge/IEEE-submission%20style-00629B?style=for-the-badge&logo=ieee&logoColor=white" alt="IEEE submission style">
  <img src="https://img.shields.io/badge/Overleaf-writing%20pipeline-47A141?style=for-the-badge&logo=overleaf&logoColor=white" alt="Overleaf writing pipeline">
</p>

paper-skill turns Chinese drafts, experiments, figures, and references into traceable English submission artifacts.

```text
Chinese research materials
  → storyline and claim–evidence map
  → manuscript / abstract / cover letter
  → citation, figure, and revision consistency checks
  → VERIFIED / UNVERIFIED / AUTHOR_INPUT_NEEDED
  → READY / READY_WITH_WARNINGS / NOT_READY
```

It is not a prompt dump or an acceptance predictor. It refuses to invent data, experiments, DOI values, journal policies, author declarations, or revision locations.

[中文说明](README.md) · [Installation](docs/installation.md) · [Benchmark](benchmarks/README.md) · [Examples](examples/README.md)

## Install

macOS / Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
```

The installer targets agent-platform directories already present on the machine and defaults to Codex if none are detected. It does not create all supported platform directories. Git is required; optional verification tools require Python 3.10+.

Then ask:

```text
Use $paper-skill. My source manuscript is Chinese and targets IEEE TRO.
Build a claim–evidence map before rewriting the abstract. Do not invent missing
data or references. Finish with verification states and submission blockers.
```

## Three flagship routes

| Route | Use it for | Output |
|---|---|---|
| `write` | Chinese materials to an English manuscript | Storyline, claim–evidence map, draft, change ledger |
| `review` | Pre-submission and evidence audit | Fatal issues, evidence gaps, citation risks, readiness |
| `submit` | Rebuttal, R&R, cover letter, final package | Response matrix, exact locations, declarations, gates |

Narrow routes include literature review, figures, citations, journal strategy, reporting guidelines, and full verification. [SKILL.md](SKILL.md) remains a concise router and loads detailed resources only when needed.

For the first-run IEEE T-RO path, use `write → review → journal → submit` and re-check the dated [official-source venue profile](references/venues/ieee-tro.md). Upload the authoritative manuscript, figures, reference library, result tables, supplements, author/declaration metadata, and version precedence; redact unnecessary sensitive information first.

## Executable verification

```bash
python tools/paper_skill_gate.py examples/submission-package-check.json
python tools/run_full_workflow.py examples/full-workflow-config.json --output full-report.json
python tools/run_benchmark.py
python -m unittest discover -s tests
```

The public deterministic safety benchmark currently classifies **8/8 cases correctly**. It covers missing identity, unsupported claims, broken evidence links, suspicious DOI metadata, false verification claims, unresolved author input, and reporting-guideline gaps. The fixtures are public in [benchmarks/gate-cases.json](benchmarks/gate-cases.json).

This benchmark measures structured package risk classification only—not prose quality, novelty, or acceptance probability.

### Figure 1: Citation detective — trace every claim to a real source

This visual explains the `citation-integrity` route: connect claims to references, check DOI/title metadata, and surface suspected hallucinations or mismatches for review.

<p align="center"><img src="assets/comic-citation-detective.png" alt="Citation verification comic: tracing claims to sources" width="100%"></p>

### Figure 2: The paper workflow — from scattered material to a traceable package

This diagram shows the main path: identify the paper type, build the storyline, write and translate, verify evidence and figures, then prepare reviewer responses and submission artifacts.

<p align="center"><img src="assets/paper-workflow.png" alt="Academic paper writing and submission workflow" width="100%"></p>

### Figure 3: Submission workflow — connect every stage

This comic presents the continuous submission process: clarify the research question, produce the English manuscript, audit citations and figures, address reviewer comments, and keep unresolved items visible before submission.

<p align="center"><img src="assets/comic-submission-workflow.png" alt="Submission workflow from a rough draft to a verified package" width="100%"></p>

### Figure 4: Academic figures — define the evidence before the visual

The figure workflow starts by asking what a visual must prove, then selects a method diagram, result figure, or graphical abstract and checks caption/text consistency.

<p align="center"><img src="assets/figure-generation.png" alt="Academic figure generation and audit workflow" width="100%"></p>

### Figure 5: The pig researcher story — a complete paper-skill example

The pig researcher moves through four fictional stages: a chaotic draft, storyline reconstruction, claim/experiment/citation/figure verification, and a final reviewer response and submission package. It explains the product value and is not an acceptance guarantee.

<p align="center"><img src="assets/comic-pig-paper-skill-story.png" alt="Four-panel story of a pig researcher using paper-skill to prepare a submission" width="100%"></p>

## Reliable upgrades

The v0.8.0 installers safely migrate early copy-based installations: they create a timestamped backup, install a Git-managed copy, restore the previous installation on failure, and report versions. Windows and Linux migration paths run in CI.

## Core guarantees

- Preserve scientific meaning before improving style.
- Map material claims to supplied evidence.
- Verify current policies and references against primary sources when possible.
- Keep reviewer replies traceable to actual manuscript changes.
- Label uncertainty instead of hiding it.
- Never call a package submission-ready while critical evidence is unresolved.

## License

MIT. See [ATTRIBUTIONS.md](ATTRIBUTIONS.md) for external workflow inspiration and licensing notes.
