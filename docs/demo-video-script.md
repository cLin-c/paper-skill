# 2-Minute Demo Video Script

Use this script for Bilibili, Xiaohongshu, Douyin, Zhihu video, or Twitter/X.

## Title

```text
用 paper-skill 把中文论文摘要改成 SCI / IEEE 风格英文，并自动标出证据不足
```

## 0:00 - 0:15 Hook

很多中文科研作者不是不会做研究，而是卡在英文论文表达、审稿回复和引用可信度上。

paper-skill 是一个给中文科研作者用的 AI skill，目标是把中文初稿变成英文投稿包。

## 0:15 - 0:35 Input

展示这个 prompt：

```text
我的论文是中文初稿，目标期刊是 IEEE TRO。请先判断论文类型，重构核心故事线，然后给我一版英文摘要、投稿前风险清单和需要作者补充的信息。不要编造实验数据和引用。
```

## 0:35 - 1:15 Output

展示输出重点：

- 论文类型：methods paper
- 故事线：problem -> limitation -> method -> evidence -> contribution
- 英文摘要
- Unsupported claims
- `[AUTHOR_INPUT_NEEDED: ...]`

强调：它不会把缺失的数据硬编成实验结果。

## 1:15 - 1:40 Reviewer Response

展示第二个例子：

```text
审稿人说 robustness claim 太宽，但我不能补实验。请帮我英文回复并弱化论文表述。
```

输出应该包含：

- 同意审稿意见
- 不声称新增实验
- 给出摘要、引言、结论的修改位置占位

## 1:40 - 2:00 Close

总结：

paper-skill 不是只做润色。它更像一个论文投稿工作流：

- 中文转英文
- 审稿回复
- 引用幻觉检查
- 投稿前质量门控

GitHub: https://github.com/cLin-c/paper-skill
