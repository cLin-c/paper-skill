# paper-skill

Chinese-first academic paper skill for SCI / Nature / IEEE submissions.

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-supported-brightgreen)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-orange)](https://claude.ai/code)
[![Chinese-first](https://img.shields.io/badge/Chinese--first-submission%20workflow-red)](#flagship-strengths)
[![Citation Integrity](https://img.shields.io/badge/citation-integrity-blue)](citation-integrity.md)
[![Quality Gates](https://img.shields.io/badge/quality-gates-purple)](quality-gates.md)
[![Reviewer Response](https://img.shields.io/badge/reviewer-response-teal)](#what-it-does)
[![Academic Figures](https://img.shields.io/badge/academic-figures-yellow)](references/figure-prompts.md)

<p align="center">
  <img src="assets/paper-skill-hero.png" alt="paper-skill academic writing AI workflow" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Google%20Scholar-literature%20map-0B57D0?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar literature map">
  <img src="https://img.shields.io/badge/arXiv-preprint%20workflow-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="arXiv preprint workflow">
  <img src="https://img.shields.io/badge/LaTeX-manuscript%20ready-008080?style=for-the-badge&logo=latex&logoColor=white" alt="LaTeX manuscript ready">
  <img src="https://img.shields.io/badge/IEEE-submission%20style-00629B?style=for-the-badge&logo=ieee&logoColor=white" alt="IEEE submission style">
  <img src="https://img.shields.io/badge/Overleaf-writing%20pipeline-47A141?style=for-the-badge&logo=overleaf&logoColor=white" alt="Overleaf writing pipeline">
</p>

paper-skill is designed for non-native English researchers who draft, think, and revise in Chinese but need to submit in academic English. It provides reusable workflows for manuscript writing, Chinese-to-English submission, reviewer response, citation integrity, academic figures, and final quality gates.

<p align="center">
  <a href="#what-it-does"><img src="https://img.shields.io/badge/Storyline-paper%20arc-111827?style=for-the-badge&logo=readme&logoColor=white" alt="storyline module"></a>
  <a href="#what-it-does"><img src="https://img.shields.io/badge/Translation-Chinese%20to%20English-D64545?style=for-the-badge&logo=deepl&logoColor=white" alt="translation module"></a>
  <a href="#what-it-does"><img src="https://img.shields.io/badge/Reviewer%20Response-R%26R%20matrix-8B5CF6?style=for-the-badge&logo=gitbook&logoColor=white" alt="review response module"></a>
  <a href="citation-integrity.md"><img src="https://img.shields.io/badge/Citation%20Integrity-DOI%20audit-2563EB?style=for-the-badge&logo=zotero&logoColor=white" alt="citation integrity module"></a>
  <a href="quality-gates.md"><img src="https://img.shields.io/badge/Quality%20Gates-7D%20check-0F766E?style=for-the-badge&logo=checkmarx&logoColor=white" alt="quality gates module"></a>
  <a href="references/figure-prompts.md"><img src="https://img.shields.io/badge/Figures-visual%20contract-F59E0B?style=for-the-badge&logo=figma&logoColor=white" alt="figures module"></a>
</p>

## Flagship Strengths

paper-skill's strongest capability is the **Chinese-first submission package**: it starts from Chinese research materials and produces traceable English submission artifacts.

| Strength | Why it matters |
|---|---|
| Chinese draft to English submission package | Not only sentence polishing; it rebuilds title, abstract, contributions, cover letter, and quality checklist |
| Traceable reviewer response | Maps replies to manuscript changes and avoids vague revision claims |
| Citation and claim integrity | Checks DOI, citation support, over-claims, and AI hallucination risks |
| Pre-submission quality gates | Exposes rejection risks before submission |
| Modular composition | `writing`, `translation`, `review-response`, `citation-integrity`, `quality-gates`, and `figures` can be used separately or together |

## Core Value

paper-skill is not a large prompt dump. It turns submission preparation into reusable modules.

| Core | What it protects | What you get |
|---|---|---|
| Storyline first | Writing before the argument is clear | Paper type, narrative arc, contribution framing |
| Evidence before claims | Over-claiming beyond experiments or citations | Claim-evidence matrix, unsupported-claim warnings |
| Chinese-to-English submission | Literal translation and Chinglish | Journal-grade abstract, sections, cover letter |
| Reviewer traceability | Vague or fabricated revision replies | Point-by-point response, revision-location mapping |
| Citation integrity | Hallucinated or mismatched references | DOI/title checks, Trust-Chain notes, risk list |

## Who It Is For

- Chinese researchers preparing SCI / IEEE / Nature-family submissions.
- Graduate students turning thesis text or Chinese drafts into English manuscripts.
- Authors preparing cover letters, reviewer responses, and revision matrices.
- Labs that need a reusable writing and submission workflow across AI coding agents.

## Quick Start

One-command install for Codex CLI, Claude Code, Qwen Code, Kimi Code CLI, DeepSeek / Deep Code, Baidu Comate, Qoder / Lingma, and OpenClaw:

```bash
curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
```

Manual install:

| Platform | Install command | Invoke |
|---|---|---|
| Codex CLI | `git clone https://github.com/cLin-c/paper-skill ~/.codex/skills/paper-skill` | `$paper-skill` |
| Claude Code | `git clone https://github.com/cLin-c/paper-skill ~/.claude/skills/paper-skill` | `/paper-skill` |
| Qwen Code | `git clone https://github.com/cLin-c/paper-skill ~/.qwen/skills/paper-skill` | `/paper-skill` |
| Kimi Code CLI | `git clone https://github.com/cLin-c/paper-skill ~/.kimi/skills/paper-skill` | `/skill:paper-skill` |
| DeepSeek / Deep Code | `git clone https://github.com/cLin-c/paper-skill ~/.deepseek/skills/paper-skill` | `/paper-skill` |
| Baidu Comate | `git clone https://github.com/cLin-c/paper-skill ~/.comate/skills/paper-skill` | `/paper-skill` |
| Qoder / Lingma | `git clone https://github.com/cLin-c/paper-skill ~/.lingma/skills/paper-skill` | `/paper-skill` |
| OpenClaw | `git clone https://github.com/cLin-c/paper-skill ~/.openclaw/skills/paper-skill` | `/paper-skill` |

Full installation guide: [docs/installation.md](docs/installation.md)

Invoke in Codex CLI:

```text
$paper-skill
```

Invoke in Claude Code and most slash-command platforms:

```text
/paper-skill
```

First prompt:

```text
Use $paper-skill. My manuscript is written in Chinese and targets an SCI / IEEE journal. First identify the paper type, then rewrite the abstract in academic English, flag unsupported claims, and list the information I must provide. Do not invent data or references.
```

## What It Does

paper-skill is modular. Use one module directly or combine modules into a full submission workflow.

| Module | Output |
|---|---|
| `writing` | Outline, section drafts, claim-evidence map, revision plan |
| `translation` | English abstract, translated sections, Chinglish report |
| `review-response` | Point-by-point response, revision matrix, risk triage |
| `citation-integrity` | Citation audit, DOI checks, Trust-Chain notes |
| `quality-gates` | 7-dimension score, final checklist, rejection-risk list |
| `figures` | Figure contract, method/result figure prompts, captions, figure audit |
| `journal-strategy` | Journal fit notes, FINER score, transfer plan |
| `literature-review` | Literature matrix, gap map, citation role table |
| `submission-package` | Title, abstract, cover letter, highlights, declarations, checklist |
| `figure-audit` | Figure-claim audit, caption fixes, missing evidence list |
| `reference-tools` | DOI/title checklist, duplicate/missing reference warnings |

## Executable Toolchain

paper-skill now includes a runnable stage-gate checker, so it is not only a prompt library.

```bash
python tools/paper_skill_gate.py examples/submission-package-check.json
python -m unittest discover -s tests
```

| Tool | Purpose |
|---|---|
| [tools/paper_skill_gate.py](tools/paper_skill_gate.py) | Checks identity, claim-evidence mapping, citation integrity, and submission package completeness |
| [examples/submission-package-check.json](examples/submission-package-check.json) | Runnable sample input for the checker |
| [docs/toolchain.md](docs/toolchain.md) | Explains the stage-gate workflow and roadmap |

## Workflow Overview

<p align="center">
  <img src="assets/paper-workflow.png" alt="paper-skill scientific paper writing workflow" width="100%">
</p>

The workflow can be used end to end or module by module:

1. Identify paper type and target journal.
2. Build the scientific storyline.
3. Draft or rewrite manuscript sections.
4. Translate and polish for English submission.
5. Audit citations and claim-evidence alignment.
6. Prepare figures, cover letter, reviewer response, and final checks.

## Academic Figures & Visualization

<p align="center">
  <img src="assets/figure-generation.png" alt="paper-skill academic figure generation workflow" width="100%">
</p>

The figure module defines scientific purpose before visual generation: what the figure must prove, which figure type fits, how to caption it, and whether it supports the manuscript claim.

## Why It Is Different

- Built for non-native English researchers, with Chinese-first workflows rather than English-only prompts.
- Submission-focused instead of general note-taking.
- Runnable stage-gate checks for submission package completeness.
- Built-in refusal to invent data, DOI, experiments, journal policies, or reviewer identities.
- Citation integrity and over-claim checks before submission.
- Reviewer response workflow with traceable manuscript locations.
- Multi-platform support across Codex CLI, Claude Code, Qwen, Kimi, DeepSeek, Comate, Qoder / Lingma, and OpenClaw.

## Examples

See [examples/README.md](examples/README.md):

- Chinese abstract to academic English.
- Reviewer comment to point-by-point response.
- Citation integrity and over-claim audit.
- Before / after examples that show weak output versus paper-skill output.

## Core Files

| Module | File | Purpose |
|---|---|
| `main` | [SKILL.md](SKILL.md) | Routing and core scenarios |
| `installation` | [docs/installation.md](docs/installation.md) | One-command and manual installation across supported AI platforms |
| `citation-integrity` | [citation-integrity.md](citation-integrity.md) | Citation hallucination and Trust-Chain checks |
| `journal-strategy` | [journal-strategy.md](journal-strategy.md) | Journal-first strategy and FINER scoring |
| `quality-gates` | [quality-gates.md](quality-gates.md) | 7-dimension quality gates and R&R traceability |
| `workflows` | [workflows/README.md](workflows/README.md) | Modular workflow pages for submission package, literature review, figure audit, and references |
| `tools` | [tools/README.md](tools/README.md) | Runnable stage-gate checker and validation workflow |
| `writing` | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) | Writing and review prompts |
| `figures` | [references/figure-prompts.md](references/figure-prompts.md) | Academic figure prompts |
| `literature-review` | [workflows/literature-review.md](workflows/literature-review.md) | Related-work matrix, gap extraction, citation roles |
| `submission-package` | [workflows/submission-package.md](workflows/submission-package.md) | Final submission artifact checklist |
| `figure-audit` | [workflows/figure-audit.md](workflows/figure-audit.md) | Figure-to-claim alignment checks |
| `reference-tools` | [workflows/reference-tools.md](workflows/reference-tools.md) | Lightweight reference consistency workflow |

## Typical Use Cases

| Scenario | Recommended modules |
|---|---|
| Chinese draft to English submission | `writing` + `translation` + `quality-gates` |
| Reviewer response | `review-response` + `quality-gates` |
| Citation hallucination or mismatch concerns | `citation-integrity` + `quality-gates` |
| Weak paper storyline | `journal-strategy` + `writing` |
| Academic method/result figures | `figures` + `writing` |
| Transfer after rejection | `journal-strategy` + `writing` + `review-response` |
| Related work lacks logic | `literature-review` + `writing` + `citation-integrity` |
| Submission package is incomplete | `submission-package` + `quality-gates` |
| Figures do not support the claims | `figure-audit` + `figures` + `quality-gates` |

## Benchmark Capability Map

paper-skill follows the strongest patterns from high-star academic skill projects, but organizes them around its own primary use case: **Chinese research materials -> English submission package**.

| Benchmark pattern | Why users like it | paper-skill implementation |
|---|---|---|
| End-to-end research pipeline | Users want one workflow from idea to final manuscript | `writing` + `journal-strategy` + `quality-gates` compose the manuscript pipeline |
| High-impact journal style | Users want polished, concise, journal-grade expression | `translation` and `writing` focus on non-literal English, Chinglish repair, and contribution framing |
| Scientific figure workflow | Users need method diagrams, result figures, and captions | `figures` uses figure contracts, figure prompts, captions, and claim-support audits |
| Reviewer-response workflow | R&R replies are high-stakes and easy to mishandle | `review-response` generates point-by-point replies with manuscript-location mapping |
| Citation verification | AI-written references can hallucinate or mismatch claims | `citation-integrity` checks DOI/title support and claim-reference alignment |
| Quality gates | Authors need a pre-submission stop/go signal | `quality-gates` provides 7-dimension scoring and rejection-risk lists |
| Community examples | Users trust concrete before/after workflows | `examples/` collects copyable submission scenarios |

## Safety Principles

paper-skill should mark missing information as `[AUTHOR_INPUT_NEEDED: ...]`, distinguish supplied evidence from model inference, and avoid strengthening claims beyond the available evidence.

## License

MIT
