# paper-skill v0.2

> Chinese-first academic paper skill for SCI / Nature / IEEE submissions.

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-supported-brightgreen)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-orange)](https://claude.ai/code)

paper-skill helps Chinese researchers turn research materials into a submission-ready package: manuscript structure, English polishing, citation integrity, reviewer response, figures, and final quality gates.

It is optimized for users who think and draft in Chinese but need to submit in academic English.

English overview: [README_EN.md](README_EN.md)

## Who It Is For

- Chinese graduate students preparing SCI / IEEE / Nature-family manuscripts.
- Researchers who draft in Chinese but need journal-grade English.
- Authors preparing reviewer responses, cover letters, and revision matrices.
- Labs that want reusable AI workflows for paper writing, citation checks, and submission QA.

## 60-Second Demo

Input:

```text
我的论文是中文初稿，目标期刊是 IEEE TRO。请先判断论文类型，重构核心故事线，然后给我一版英文摘要、投稿前风险清单和需要作者补充的信息。不要编造实验数据和引用。
```

Expected output:

```text
Paper type: methods paper
Storyline: problem -> limitation -> method -> evidence -> contribution
English abstract: ...
Unsupported claims: ...
AUTHOR_INPUT_NEEDED: baselines, metrics, scenario count, DOI list
Submission risk: claim-evidence mismatch, missing real-world details, broad robustness language
```

This demo shows the central behavior: paper-skill improves writing while forcing missing evidence to stay visible.

## Try It First

Install with Codex CLI:

```bash
git clone https://github.com/cLin-c/paper-skill ~/.codex/skills/paper-skill
```

Use it in Codex:

```text
$paper-skill
```

First prompt to try:

```text
我的论文是中文初稿，目标期刊是 IEEE TRO。请先判断论文类型，重构核心故事线，然后给我一版英文摘要、投稿前风险清单和需要作者补充的信息。不要编造实验数据和引用。
```

## Four Workflows

| Workflow | Use it when | Output |
|---|---|---|
| Manuscript Writing | You need to build or rewrite a paper from notes, thesis text, experiment records, or a rough draft. | Outline, section drafts, claim-evidence map, revision plan |
| Chinese-to-English Submission | You have a Chinese manuscript and need publishable English. | English abstract, translated sections, Chinglish report, cover letter |
| Reviewer Response | You received reviewer comments or want pre-submission review. | Point-by-point response, revision matrix, risk triage |
| Citation & Quality Gates | You need to prevent hallucinated citations and over-claims before submission. | Citation audit, DOI checks, 7-dimension score, final checklist |

## Why paper-skill

Most academic-writing skills assume the author already writes in English. paper-skill starts from the actual workflow of many Chinese researchers:

1. Draft in Chinese.
2. Clarify the scientific story.
3. Convert to journal-grade English.
4. Check citation and claim integrity.
5. Prepare cover letter, reviewer response, and submission statements.

The core value is not a larger prompt collection. It is a submission workflow that forces the model to separate provided evidence, author assumptions, and missing information.

## Example Gallery

See [examples/README.md](examples/README.md) for copyable demonstrations:

- Chinese abstract to journal-style English
- Reviewer comment to point-by-point response
- Citation integrity and over-claim audit
- Full submission package workflow

## Core Modules

| Module | File | Purpose |
|---|---|---|
| Main workflow | [SKILL.md](SKILL.md) | 22 academic paper scenarios |
| Writing and review | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) | Paper sections, SCI revision, reviewer-risk detection |
| Figures | [references/figure-prompts.md](references/figure-prompts.md) | Method figures, result figures, captions, figure audits |
| Citation integrity | [citation-integrity.md](citation-integrity.md) | DOI checks, hallucination scan, Trust-Chain sourcing |
| Journal strategy | [journal-strategy.md](journal-strategy.md) | Journal-first planning, FINER scoring, transfer strategy |
| Quality gates | [quality-gates.md](quality-gates.md) | 7-dimension manuscript score, R&R traceability, final checks |

## Positioning

| Project type | paper-skill positioning |
|---|---|
| General research suites | Lighter, submission-focused, easier to start |
| Nature-only writing skills | Broader journal coverage with Chinese-first workflows |
| Humanizer prompts | Focuses on quality, evidence, and Chinglish repair rather than hiding AI use |
| One-shot writing prompts | Adds quality gates, citation checks, reviewer response, and author placeholders |

## Star This Repo If

- You write papers in Chinese and submit in English.
- You want reviewer-response and citation-integrity workflows, not only polishing.
- You want a lightweight skill that works across Codex CLI, Claude Code, and Chinese AI coding tools.
- You want examples that can be copied into real academic workflows.

## Supported Platforms

| Platform | Invoke |
|---|---|
| Codex CLI | `$paper-skill` |
| Claude Code | `/paper-skill` |
| Qwen Code | `/paper-skill` |
| Kimi Code CLI | `/skill:paper-skill` |
| Deep Code | `/paper-skill` |
| Baidu Comate | `/paper-skill` |
| Qoder / Lingma | `/paper-skill` |
| OpenClaw | `/paper-skill` |

## Safety Rules

paper-skill should:

- Mark missing facts as `[AUTHOR_INPUT_NEEDED: ...]`.
- Avoid inventing data, experiments, DOI, page numbers, journal policies, and reviewer identities.
- Distinguish provided content, model inference, and writing suggestions.
- Keep reviewer replies traceable to manuscript locations.
- Check whether claims are supported before strengthening language.

## Release

This versioned README is part of the v0.2 growth iteration. It does not replace the original README yet. See [docs/v0.2.0-release-notes.md](docs/v0.2.0-release-notes.md) and [docs/v0.2.1-growth-notes.md](docs/v0.2.1-growth-notes.md).
