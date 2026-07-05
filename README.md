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

## Flagship Strengths

paper-skill 最强的能力是 **Chinese-first submission package**：从中文材料出发，生成英文投稿所需的一整套可核查材料。

| Strength | Why it matters |
|---|---|
| 中文初稿到英文投稿包 | 不是只改句子，而是重构标题、摘要、贡献点、Cover Letter、质量清单 |
| 审稿回复可追踪 | 回复审稿人时强制映射修改位置，避免“说改了但稿件没对应改” |
| 引用与主张诚信 | 检查 DOI、引用支撑、主张过强、AI 幻觉引用 |
| 投稿前质量门控 | 用 7 维度质量门控提前暴露拒稿风险 |
| 模块化组合 | `writing`、`translation`、`review-response`、`citation-integrity`、`quality-gates`、`figures` 可单独用，也可组合成完整流程 |

## Core Value

paper-skill 的核心不是“提示词多”，而是把论文投稿拆成可复用、可检查、可组合的模块：

| Core | What it protects | What you get |
|---|---|---|
| Storyline first | Avoid writing before the paper's argument is clear. | Paper type, narrative arc, contribution framing |
| Evidence before claims | Avoid over-claiming beyond experiments or citations. | Claim-evidence matrix, unsupported-claim warnings |
| Chinese-to-English submission | Avoid literal translation and Chinglish. | Journal-grade abstract, sections, cover letter |
| Reviewer traceability | Avoid vague or fabricated revision replies. | Point-by-point response, revision-location mapping |
| Citation integrity | Avoid hallucinated or mismatched references. | DOI/title checks, Trust-Chain notes, risk list |

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

## Modular Skill Architecture

paper-skill is organized as independent but composable modules. Use one module for a narrow task, or combine modules into a full submission workflow.

| Module | Use it when | Output |
|---|---|---|
| `writing` | Build or rewrite a paper from notes, thesis text, experiment records, or a rough draft. | Outline, section drafts, claim-evidence map, revision plan |
| `translation` | Convert Chinese manuscript text into journal-grade English. | English abstract, translated sections, Chinglish report |
| `review-response` | Reply to reviewer comments or prepare rebuttal / R&R materials. | Point-by-point response, revision matrix, risk triage |
| `citation-integrity` | Prevent hallucinated citations, unsupported claims, and DOI/title mismatch. | Citation audit, DOI checks, Trust-Chain notes |
| `quality-gates` | Check manuscript readiness before submission. | 7-dimension score, final checklist, rejection-risk list |
| `figures` | Design method figures, result figures, captions, or figure-review prompts. | Figure contract, prompt, caption, text-reference guidance |
| `journal-strategy` | Select or adapt to a target journal before writing or transferring. | Journal fit notes, FINER score, transfer plan |

## Workflow Overview

<p align="center">
  <img src="assets/paper-workflow.png" alt="paper-skill scientific paper writing workflow" width="100%">
</p>

The workflow is meant to be used end to end, but each stage can also be used independently:

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

The figure module focuses on scientific purpose before visual generation:

- Define what the figure must prove.
- Select method diagram, experiment result figure, table-to-figure, or graphical abstract style.
- Generate prompts for figure tools while preserving scientific constraints.
- Draft captions and in-text references.
- Audit whether the figure supports the manuscript claim.

## Why It Exists

paper-skill 的定位很聚焦：**为中文科研作者建立一套英文投稿工作流**。

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
| `main` | [SKILL.md](SKILL.md) | Routing and core scenarios |
| `writing` | [references/paper-writing-prompts.md](references/paper-writing-prompts.md) | Literature reading, SCI revision, sections, experiments, reviewer risks |
| `figures` | [references/figure-prompts.md](references/figure-prompts.md) | Method diagrams, result figures, captions, figure audits |
| `citation-integrity` | [citation-integrity.md](citation-integrity.md) | DOI checks, hallucination scan, Trust-Chain sourcing |
| `journal-strategy` | [journal-strategy.md](journal-strategy.md) | Journal-first planning, FINER scoring, transfer strategy |
| `quality-gates` | [quality-gates.md](quality-gates.md) | 7-dimension score, R&R traceability, final checks |

## Typical Use Cases

| Scenario | Recommended modules |
|---|---|
| 中文初稿转英文投稿稿 | `writing` + `translation` + `quality-gates` |
| 审稿意见回复 | `review-response` + `quality-gates` |
| 担心引用幻觉或错引 | `citation-integrity` + `quality-gates` |
| 论文故事线混乱 | `journal-strategy` + `writing` |
| 方法图/实验图不够学术 | `figures` + `writing` |
| 拒稿后转投 | `journal-strategy` + `writing` + `review-response` |

## High-Star Skill Comparison

Stars checked on 2026-07-06 via GitHub API.

| Project | Stars | Main focus | paper-skill difference |
|---|---:|---|---|
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 36,372 | Large academic research pipeline: research, write, review, revise, finalize | Lighter and more focused on Chinese-to-English submission packages |
| [nature-skills](https://github.com/Yuan1z0825/nature-skills) | 26,143 | High-impact paper expression, research figures, and skill-based research workflows | Broader Chinese-first submission workflow: translation, reviewer response, citation integrity, quality gates, and journal transfer |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 4,506 | Semi-automated research assistant across literature, coding, experiments, writing, and knowledge management | Less infrastructure-heavy; easier to use as a paper submission skill |
| [claude-prism](https://github.com/delibae/claude-prism) | 1,646 | Offline-first scientific writing workspace with LaTeX, Python, and many scientific skills | Not a workspace; focuses on reusable manuscript workflows |
| [codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 1,471 | Chinese academic skills for writing, Office documents, and scientific computing | More submission-centered: reviewer response, citation integrity, and quality gates |
| [academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | 994 | Academic paper planning and writing with strategist/composer workflow | Broader Chinese-to-English, reviewer reply, citation audit, and figure prompt coverage |
| [paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) | 774 | Paper reading, deep analysis, summaries, and visual explanation | More focused on preparing manuscripts for submission |
| [paper-skill](https://github.com/cLin-c/paper-skill) | 40 | Chinese-first English submission workflow | Modular submission suite for writing, translation, review response, citation integrity, figures, and quality gates |

The goal is not to become the largest research automation suite. paper-skill aims to be the clearest path from Chinese research materials to an English submission package.

## Benchmark Capability Map

paper-skill will keep absorbing the best patterns from high-star academic skill projects, but package them around its own strongest use case: **Chinese research materials -> English submission package**.

| High-star pattern | Why users like it | paper-skill implementation |
|---|---|---|
| End-to-end research pipeline | Users want one workflow from idea to final manuscript | `writing` + `journal-strategy` + `quality-gates` compose the manuscript pipeline |
| High-impact journal style | Users want polished, concise, journal-grade expression | `translation` and `writing` focus on non-literal English, Chinglish repair, and contribution framing |
| Scientific figure workflow | Users need method diagrams, result figures, and captions | `figures` uses figure contracts, figure prompts, captions, and claim-support audits |
| Reviewer-response workflow | R&R replies are high-stakes and easy to mishandle | `review-response` generates point-by-point replies with manuscript-location mapping |
| Citation verification | AI-written references can hallucinate or mismatch claims | `citation-integrity` checks DOI/title support and claim-reference alignment |
| Quality gates | Authors need a pre-submission stop/go signal | `quality-gates` provides 7-dimension scoring and rejection-risk lists |
| Community examples | Users trust concrete before/after workflows | `examples/` collects copyable submission scenarios |

Next modules to strengthen:

- `literature-review`: more structured related-work matrices and gap extraction.
- `submission-package`: one-command checklist for title, abstract, cover letter, highlights, declarations, references, and figures.
- `figure-audit`: stronger rules for whether a figure actually supports the claim.
- `reference-tools`: optional scripts for reference consistency and DOI checking.

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
| Large all-in-one research automation suite | [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) |
| General scholar assistant with coding and knowledge base workflows | [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) |

## Roadmap

- `v0.3`: add `workflows/` pages for the core submission journeys.
- `v0.4`: add anonymized screenshots and before/after examples.
- `v0.5`: explore optional scripts for citation and quality checks.
- `v1.0`: stabilize the Chinese-first English submission skill suite.

## License

MIT
