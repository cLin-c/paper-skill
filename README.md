# paper-skill

> Chinese-first academic paper skill for SCI / Nature / IEEE submissions.

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-supported-brightgreen)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-orange)](https://claude.ai/code)

<p align="center">
  <img src="assets/paper-skill-hero.png" alt="paper-skill academic writing AI workflow" width="100%">
</p>

paper-skill 帮中文科研作者把研究材料整理成可投稿英文包：论文结构、英文表达、引用诚信、审稿回复、图表提示词和投稿前质量门控。

它不是单纯润色工具，而是面向真实投稿流程的 AI skill：**中文初稿 -> 英文摘要/正文 -> Cover Letter -> Reviewer Response -> Citation Audit -> Submission Checklist**。

English overview: [README_EN.md](README_EN.md)

## Quick Start

Codex CLI:

```bash
git clone https://github.com/cLin-c/paper-skill ~/.codex/skills/paper-skill
```

Claude Code:

```bash
git clone https://github.com/cLin-c/paper-skill ~/.claude/skills/paper-skill
```

Invoke:

```text
$paper-skill
```

First prompt:

```text
我的论文是中文初稿，目标期刊是 IEEE TRO。请先判断论文类型，重构核心故事线，然后给我一版英文摘要、投稿前风险清单和需要作者补充的信息。不要编造实验数据和引用。
```

Verify installation:

```text
请使用 $paper-skill，告诉我它支持哪些论文投稿工作流，并给我一个中文摘要转英文摘要的最小示例。
```

## Core Workflows

| Workflow | Use it when | Output |
|---|---|---|
| Manuscript Writing | You need to build or rewrite a paper from notes, thesis text, experiment records, or a rough draft. | Outline, section drafts, claim-evidence map, revision plan |
| Chinese-to-English Submission | You have a Chinese manuscript and need publishable English. | English abstract, translated sections, Chinglish report, cover letter |
| Reviewer Response | You received reviewer comments or want pre-submission review. | Point-by-point response, revision matrix, risk triage |
| Citation & Quality Gates | You need to prevent hallucinated citations and over-claims before submission. | Citation audit, DOI checks, 7-dimension score, final checklist |
| Academic Figures | You need method figures, result figures, captions, or figure review. | Figure contract, prompt, caption, text-reference guidance |

## Why It Exists

paper-skill 参考了 [nature-skills](https://github.com/Yuan1z0825/nature-skills) 的 skill 化科研理念，但定位更聚焦：**为中文科研作者建立一套英文投稿工作流**。

中文科研作者最缺的往往不是“让 AI 写得更华丽”，而是一个稳定流程，能把中文材料、实验结果、参考文献和审稿意见转换成可追踪、可核查、可投稿的英文材料。

Design principles:

- Identify paper type and storyline before writing.
- Check evidence before strengthening claims.
- Mark missing facts as `[AUTHOR_INPUT_NEEDED: ...]`.
- Do not invent experiments, DOI, page numbers, journal policies, or reviewer identities.
- Keep reviewer replies traceable to manuscript locations.

## Examples

Copyable demos:

- [Chinese abstract to academic English](examples/chinese-abstract-to-english.md)
- [Reviewer response](examples/reviewer-response.md)
- [Citation integrity and over-claim audit](examples/citation-integrity-audit.md)
- [Full submission package](examples/full-submission-package.md)

Demo output shape:

```text
Paper type: methods paper
Storyline: problem -> limitation -> method -> evidence -> contribution
English abstract: ...
Unsupported claims: ...
AUTHOR_INPUT_NEEDED: baselines, metrics, scenario count, DOI list
Submission risk: claim-evidence mismatch, missing real-world details, broad robustness language
```

## What's Inside

| Module | File | Purpose |
|---|---|---|
| Main skill | [SKILL.md](SKILL.md) | 22 paper-writing, revision, translation, and submission scenarios |
| Writing prompts | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) | Literature reading, SCI revision, sections, experiments, reviewer risks |
| Figure prompts | [references/figure-prompts.md](references/figure-prompts.md) | Method diagrams, result figures, captions, figure audits |
| Citation integrity | [citation-integrity.md](citation-integrity.md) | DOI checks, hallucination scan, Trust-Chain sourcing |
| Journal strategy | [journal-strategy.md](journal-strategy.md) | Journal-first planning, FINER scoring, transfer strategy |
| Quality gates | [quality-gates.md](quality-gates.md) | 7-dimension score, R&R traceability, final checks |

## Supported Platforms

| Platform | Invoke | Skill path |
|---|---|---|
| Codex CLI | `$paper-skill` | `~/.codex/skills/paper-skill/` |
| Claude Code | `/paper-skill` | `~/.claude/skills/paper-skill/` |
| Qwen Code | `/paper-skill` | `~/.qwen/skills/paper-skill/` |
| Kimi Code CLI | `/skill:paper-skill` | `~/.kimi/skills/paper-skill/` |
| Deep Code | `/paper-skill` | `~/.deepseek/skills/paper-skill/` |
| Baidu Comate | `/paper-skill` | `~/.comate/skills/paper-skill/` |
| Qoder / Lingma | `/paper-skill` | `~/.lingma/skills/paper-skill/` |
| OpenClaw | `/paper-skill` | `~/.openclaw/skills/paper-skill/` |

## Community

This project prioritizes real paper-writing scenarios over feature bloat.

- [Example request](https://github.com/cLin-c/paper-skill/issues/new?template=example-request.yml): request a new paper workflow example.
- [Feature request](https://github.com/cLin-c/paper-skill/issues/new?template=feature-request.yml): suggest a new reusable capability.
- [Bug report](https://github.com/cLin-c/paper-skill/issues/new?template=bug-report.yml): report unsafe or incorrect behavior.

Project docs:

- [Community guide](COMMUNITY.md)
- [Roadmap](ROADMAP.md)
- [Growth checklist](docs/github-growth-checklist.md)
- [Demo video script](docs/demo-video-script.md)

## Comparison

| Need | Better choice |
|---|---|
| Chinese-to-English SCI / IEEE submission workflow | paper-skill |
| Deep Nature-style writing and figure stack | [nature-skills](https://github.com/Yuan1z0825/nature-skills) |
| Large all-in-one research automation suite | [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) |
| General scholar assistant with coding and knowledge base workflows | [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) |

## Roadmap

- `v0.3`: add `workflows/` pages for the core submission journeys.
- `v0.4`: add anonymized screenshots and before/after examples.
- `v0.5`: explore optional scripts for citation and quality checks.
- `v1.0`: stabilize the Chinese-first English submission skill suite.

## License

MIT
