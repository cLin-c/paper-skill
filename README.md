# paper-skill

> 面向中文科研作者的 evidence-first 英文投稿工作流。

[![GitHub stars](https://img.shields.io/github/stars/cLin-c/paper-skill?style=social)](https://github.com/cLin-c/paper-skill/stargazers)
[![CI](https://github.com/cLin-c/paper-skill/actions/workflows/toolchain.yml/badge.svg)](https://github.com/cLin-c/paper-skill/actions/workflows/toolchain.yml)
[![Version](https://img.shields.io/badge/version-0.8.0-2563EB)](VERSION)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-supported-111827)](https://github.com/openai/codex)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-supported-D97706)](https://claude.ai/code)

<p align="center">
  <img src="assets/paper-skill-hero.png" alt="paper-skill evidence-first publication workflow" width="100%">
</p>

把中文初稿、实验结果、图表和参考文献转换为可核查的英文投稿材料：

```text
中文研究材料
  → 论文故事线与 claim–evidence map
  → 英文摘要 / 正文 / Cover Letter
  → 引用、图表、审稿回复一致性检查
  → VERIFIED / UNVERIFIED / AUTHOR_INPUT_NEEDED
  → READY / READY_WITH_WARNINGS / NOT_READY
```

它不是“帮我写得更像论文”的提示词合集。它把论文视为一套可追踪的主张、证据、引用、图表和投稿要求，并明确拒绝编造数据、实验、DOI、政策与修改位置。

[English README](README_EN.md) · [安装说明](docs/installation.md) · [公开 benchmark](benchmarks/README.md) · [完整示例](examples/README.md)

## 30 秒开始

macOS / Linux：

```bash
curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
```

Windows PowerShell：

```powershell
irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
```

然后直接说：

```text
使用 $paper-skill。我的论文是中文初稿，目标期刊是 IEEE TRO。
先建立 claim–evidence map，再改写英文摘要；不要补写不存在的数据和引用，
最后列出 VERIFIED、UNVERIFIED、AUTHOR_INPUT_NEEDED 和投稿阻塞项。
```

Claude Code 等 slash-command 平台可使用 `/paper-skill`。安装器只写入本机已存在的平台目录；若没有检测到平台，则默认安装到 Codex。可选的命令行核验工具需要 Python 3.10+。

## 三个旗舰入口

| 入口 | 适用场景 | 核心产物 |
|---|---|---|
| `write` | 中文材料转英文稿、重构摘要或章节 | 故事线、claim–evidence map、英文稿、变更记录 |
| `review` | 投稿前审查、引用核验、图表核对 | 致命问题、证据缺口、引用风险、就绪状态 |
| `submit` | Rebuttal、R&R、Cover Letter、投稿包 | 逐点回复矩阵、精确修改位置、声明、最终门控 |

窄任务也可以直接调用 `literature`、`figures`、`citations`、`journal`、`reporting` 或 `full-verify`。主 [SKILL.md](SKILL.md) 仅负责路由，详细规则按需加载，避免一次塞入全部上下文。

### 中文粗稿到 T-RO 的首次运行顺序

1. 上传权威版本的稿件、图表、参考文献/BibTeX、结果表和补充材料；说明版本优先级。
2. `write`：建立研究问题、中央主张、claim–evidence map 和章节修改计划。
3. `review`：核对数字、图表、引用、过度主张和匿名化风险。
4. `journal`：按 [T-RO 官方来源快照](references/venues/ieee-tro.md) 重新访问官方页面并生成带访问日期的要求表。
5. `submit`：生成 Cover Letter、声明、投稿清单；只有关键证据全部解决后才能输出 `READY`。

理想输入还包括作者顺序、单位、ORCID、基金、伦理审批、COI、数据/代码可用性、相关预印本和截止日期。分享材料前请移除不必要的个人、患者、审稿或机构敏感信息。

## 为什么它不一样

| 常见问题 | paper-skill 的处理方式 |
|---|---|
| AI 把中文逐字翻成生硬英文 | 保留科学含义和修辞功能，维护术语表与歧义日志 |
| 为了“润色”强化了没有证据的结论 | 每项 material claim 映射到证据，超出证据时降级或删除 |
| 生成看起来真实的 DOI 或参考文献 | Crossref/OpenAlex 核验；未核验内容明确标记 `UNVERIFIED` |
| 回复称“已修改”，但稿件中找不到 | reviewer point → response → manuscript change → exact location |
| 图表数字与正文不一致 | figure/table ↔ claim ↔ manuscript consistency audit |
| 不知道稿件是否真的可以投稿 | 输出 `READY`、`READY_WITH_WARNINGS` 或 `NOT_READY` 及阻塞证据 |

## 可执行工具，而不只是提示词

```bash
python tools/paper_skill_gate.py examples/submission-package-check.json
python tools/run_full_workflow.py examples/full-workflow-config.json --output full-report.json
python tools/run_benchmark.py
python -m unittest discover -s tests
```

| 工具 | 用途 |
|---|---|
| [paper_skill_gate.py](tools/paper_skill_gate.py) | 身份、来源、主张证据、引用、报告规范、投稿包、未决输入七项门控 |
| [scholarly_verify.py](tools/scholarly_verify.py) | 使用 Crossref/OpenAlex 核验 DOI、标题和年份 |
| [journal_policy_verify.py](tools/journal_policy_verify.py) | 保存官方政策 URL、时间、证据片段和内容哈希 |
| [revision_trace.py](tools/revision_trace.py) | 核对审稿回复中的修改位置和修订文本 |
| [run_full_workflow.py](tools/run_full_workflow.py) | 串联投稿门控、引用、政策和修订一致性检查 |

## 公开、可复现的 benchmark

```bash
python tools/run_benchmark.py
```

当前确定性安全门控 benchmark：**8/8 分类正确**。

覆盖：完整投稿包、身份信息缺失、无证据主张、断裂证据链接、可疑 DOI、伪 `VERIFIED` 引用、未解决作者输入、报告规范缺口。所有用例位于 [benchmarks/gate-cases.json](benchmarks/gate-cases.json)，CI 会在 Windows 和 Linux 上重复运行。

这个结果只衡量结构化投稿包的风险分类，不代表语言质量、科学创新性或录用概率。项目不会用内部评分预测论文录用。

## 工作流结构

```text
SKILL.md                         concise router
├── references/section-guides/  Abstract → Discussion 的分节写作规则
├── workflows/                  文献、图表、引用、投稿包、完整核验
├── citation-integrity.md       引用真实性与 claim-source 匹配
├── journal-strategy.md         选刊、转投和政策核验
├── quality-gates.md            审稿、R&R 和投稿前门控
├── tools/                      确定性检查与在线核验脚本
├── benchmarks/                 公开评测用例
└── examples/                   合成、可复制的 before/after 示例
```

详细写作能力覆盖 Abstract、Introduction、Related Work、Method、Experiments/Results、Discussion/Conclusion、翻译、学术图表、CONSORT、PRISMA、STROBE、SPIRIT、ARRIVE、CARE、CRediT、伦理与利益冲突声明。

## 可靠安装与升级

从 v0.8.0 开始，安装器会：

- 对 Git 安装执行 fast-forward 更新；
- 识别早期复制式/非 Git 安装；
- 在迁移前创建带时间戳的备份；
- 克隆或验证失败时恢复原安装；
- 显示迁移前后版本；
- 在 CI 中验证 Windows 与 Linux 迁移路径。

如果你曾安装旧版，重新运行上面的单行命令即可。旧目录不会被静默覆盖。

## 项目质量门槛

每次 push 和 pull request 都必须通过：

- Windows + Linux 单元测试；
- 公开 benchmark；
- 示例投稿包门控；
- `SKILL.md` 长度与路由检查；
- UTF-8 与常见中文乱码检查；
- `VERSION` 和 `agents/openai.yaml` 一致性检查；
- 旧安装安全迁移测试。

## 社区

- [提交真实工作流需求](https://github.com/cLin-c/paper-skill/issues/new?template=example-request.yml)
- [报告问题](https://github.com/cLin-c/paper-skill/issues/new?template=bug-report.yml)
- [提出功能建议](https://github.com/cLin-c/paper-skill/issues/new?template=feature-request.yml)
- [路线图](ROADMAP.md)

项目优先接受可复现的真实科研场景、失败案例、匿名化 before/after 和 benchmark 用例，而不是继续堆叠泛化提示词。

## License

MIT。写作工作流的外部灵感与授权信息见 [ATTRIBUTIONS.md](ATTRIBUTIONS.md)。
