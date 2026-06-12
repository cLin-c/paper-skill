# paper-skill

> 🎓 A Claude Code skill — AI prompt library for the full academic paper workflow.

Covers every stage from literature reading to journal submission, including writing, polishing, reviewing, translating, reference management, figure generation, and defense PPT.

Optimized for **SCI / IEEE / Nature / IJCAI / TRO** submissions.

---

## What's Inside

| Category | Prompts |
|----------|---------|
| 📖 文献阅读与分析 | 精读文献、综述撰写、领域现状总结 |
| ✍️ 论文写作与生成 | 从材料生成全文、引言/相关工作写作、写作规范 |
| 🔧 论文润色与修改 | 全文纠错、段落学术化、TRO风格润色、公式规范 |
| 🎯 论文审稿与投稿 | IJCAI/TRO/TII/Nature 审稿人视角、拒稿漏洞排查 |
| 🌐 论文翻译 | 中译英全文/部分章节、准确性校对（标蓝标红） |
| 📚 参考文献管理 | 编号排序、引用内容匹配、文献真实性核实 |
| 💻 代码相关 | 报错修复、定向代码修改、视频逐帧导出 |
| 🎨 绘图与可视化 | nano banana 方法图/实验图提示词、图注生成 |
| 📊 PPT制作与答辩 | 转博答辩PPT、演讲稿生成、评委问题预测 |
| 🗂️ 文件与桌面管理 | 桌面归类整理、合同分析、试卷解答生成 |

---

## Installation

### Option 1: Clone into your Claude skills directory

```bash
# macOS / Linux
git clone https://github.com/cLin-c/paper-skill ~/.claude/skills/paper-skill

# Windows (PowerShell)
git clone https://github.com/cLin-c/paper-skill "$env:USERPROFILE\.claude\skills\paper-skill"
```

### Option 2: Manual

Download `SKILL.md` and place it at:
```
~/.claude/skills/paper-skill/SKILL.md
```

---

## Usage

Once installed, Claude Code automatically discovers the skill.

**Invoke by name in any conversation:**
```
/paper-skill
```

**Or let Claude auto-detect** — the skill triggers automatically when you ask about:
- Writing / polishing / reviewing a paper
- SCI / IEEE / Nature / IJCAI / TRO submissions
- Translating a paper
- Creating figures or defense PPT
- Managing references

---

## Prompt Examples

### 🔧 Polishing — TRO Style
```
这个是论文方法部分，帮我按照SCI一区、TRO的学术语言风格进行润色，
要求逻辑缜密，如果原理不对的话请修改出来，生成修改后的完整方法部分
```

### 🎯 Reviewing — Find Fatal Flaws (IEEE TRO)
```
你是IEEE TRO审稿人，帮我找到会导致拒稿的致命漏洞，包括逻辑，理论，
实验，以及全文，在不补实验的基础上，给我一个修改清单，
包括修改哪里，如何修改，用什么描述语言替换，生成完整word
```

### 🌐 Translation — CN → EN (Nature Standard)
```
把论文全文翻译为英文，不要丢失参考文献标号和公式，你是nature主编，
需要百分百确保翻译后的英文意思和我原来的中文一模一样，
需要非常准确及学术化，生成完整word在桌面
```

### 🎨 Figure Prompt (nano banana)
```
这些是我的代码，我要投稿SCI一区，根据我的方法生成详细的AI提示词，
用于nano banana绘图（方法流程图），学术美观，nature级别，
包括配色、用什么元素、多加图标和元素图
```

### 📖 LaTeX Revision (TRO)
```
你是IEEE TRO审稿人和编委，给出审稿意见，修订直接在latex上修改，
给我可以复制进去替换的latex代码，精确告诉我修改哪一行，
修改前后对比都要给出来，生成完整word
```

---

## Tips

- **指定输出路径**：每个提示词记得加上"生成word在桌面上"或具体路径
- **LaTeX 修订**：务必加"精确告诉我修改哪一行，修改前后对比"，否则找不到位置
- **润色 vs 写作**：润色在原文基础上改；写作是让AI重新生成，角色定位要区分清楚
- **不补实验**：审稿类提示词加上"在不补实验的基础上给修改建议"限制范围

---

## File Structure

```
paper-skill/
├── SKILL.md      # Claude Code skill definition (prompt library)
└── README.md     # This file
```

---

## Contributing

If you have useful prompts to add, feel free to open a PR or issue.

---

## License

MIT
