# paper-skill

Chinese-first academic paper skill for SCI / Nature / IEEE submissions.

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-supported-brightgreen)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-orange)](https://claude.ai/code)

paper-skill is designed for researchers who draft, think, and revise in Chinese but need to submit in academic English. It provides reusable workflows for manuscript writing, Chinese-to-English submission, reviewer response, citation integrity, academic figures, and final quality gates.

## Who It Is For

- Chinese researchers preparing SCI / IEEE / Nature-family submissions.
- Graduate students turning thesis text or Chinese drafts into English manuscripts.
- Authors preparing cover letters, reviewer responses, and revision matrices.
- Labs that need a reusable writing and submission workflow across AI coding agents.

## Quick Start

Install for Codex CLI:

```bash
git clone https://github.com/cLin-c/paper-skill ~/.codex/skills/paper-skill
```

Invoke:

```text
$paper-skill
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

## Why It Is Different

- Chinese-first workflows rather than English-only prompts.
- Submission-focused instead of general note-taking.
- Built-in refusal to invent data, DOI, experiments, journal policies, or reviewer identities.
- Citation integrity and over-claim checks before submission.
- Reviewer response workflow with traceable manuscript locations.
- Multi-platform support across Codex CLI, Claude Code, Qwen, Kimi, DeepSeek, Comate, Qoder / Lingma, and OpenClaw.

## Examples

See [examples/README.md](examples/README.md):

- Chinese abstract to academic English.
- Reviewer comment to point-by-point response.
- Citation integrity and over-claim audit.

## Core Files

| Module | File | Purpose |
|---|---|
| `main` | [SKILL.md](SKILL.md) | Routing and core scenarios |
| `citation-integrity` | [citation-integrity.md](citation-integrity.md) | Citation hallucination and Trust-Chain checks |
| `journal-strategy` | [journal-strategy.md](journal-strategy.md) | Journal-first strategy and FINER scoring |
| `quality-gates` | [quality-gates.md](quality-gates.md) | 7-dimension quality gates and R&R traceability |
| `writing` | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) | Writing and review prompts |
| `figures` | [references/figure-prompts.md](references/figure-prompts.md) | Academic figure prompts |

## Safety Principles

paper-skill should mark missing information as `[AUTHOR_INPUT_NEEDED: ...]`, distinguish supplied evidence from model inference, and avoid strengthening claims beyond the available evidence.

## License

MIT
