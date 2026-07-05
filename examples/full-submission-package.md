# Example: Full Submission Package Workflow

## User Input

```text
Use $paper-skill. 我有一篇中文论文初稿，目标期刊是 IEEE TRO。请帮我做投稿前完整准备。

材料：
- 中文论文初稿：[粘贴或提供路径]
- 实验结果表：[粘贴或提供路径]
- 目标期刊：IEEE TRO
- 已有参考文献：[粘贴 BibTeX 或参考文献列表]

要求：
1. 判断论文类型和核心故事线。
2. 输出英文标题、摘要和贡献点。
3. 检查主张是否有实验支撑。
4. 检查引用是否可能存在幻觉或错配。
5. 生成 Cover Letter 草稿。
6. 生成投稿前质量门控清单。
不要编造实验数据、DOI、页码和期刊政策。
```

## Expected paper-skill Workflow

1. Load only the relevant modules:
   - `SKILL.md` for the main writing workflow.
   - `journal-strategy.md` for target-journal fit.
   - `citation-integrity.md` for citation checks.
   - `quality-gates.md` for submission readiness.
2. Separate author-provided evidence from model inference.
3. Mark missing information with `[AUTHOR_INPUT_NEEDED: ...]`.
4. Avoid writing claims stronger than the provided experiments can support.
5. Produce a submission package instead of only polished prose.

## Output Checklist

```text
1. Paper Type and Storyline
   - Type: methods / resource / review / discovery
   - Core problem:
   - Existing limitation:
   - Proposed method:
   - Evidence:
   - Contribution:

2. English Submission Text
   - Title:
   - Abstract:
   - Contributions:
   - Cover Letter:

3. Claim-Evidence Matrix
   - Claim:
   - Supporting figure/table/experiment:
   - Risk:
   - Revision:

4. Citation Integrity
   - Possibly unsupported citations:
   - Missing DOI/title details:
   - References that need author verification:

5. Quality Gate
   - Novelty:
   - Evidence:
   - Method clarity:
   - Experiments:
   - Figures/tables:
   - Citation integrity:
   - Submission readiness:

6. Author Input Needed
   - [AUTHOR_INPUT_NEEDED: baseline methods]
   - [AUTHOR_INPUT_NEEDED: exact numerical metrics]
   - [AUTHOR_INPUT_NEEDED: DOI or BibTeX for key references]
   - [AUTHOR_INPUT_NEEDED: page and line numbers after revision]
```

## Why This Demo Works

This is the highest-value workflow for stars because it communicates that paper-skill is not just a polishing prompt. It helps assemble a submission-ready package while protecting against fabricated evidence.
