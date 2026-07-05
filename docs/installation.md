# Installation

paper-skill can be installed into the common skill directories used by Codex CLI, Claude Code, Qwen Code, Kimi Code CLI, DeepSeek / Deep Code, Baidu Comate, Qoder / Lingma, and OpenClaw.

## One-Command Install

macOS / Linux / Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
```

The installer clones or updates this repository into all supported platform skill folders.

## Manual Install

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

## Windows Manual Paths

Use the same structure under your user profile:

```powershell
git clone https://github.com/cLin-c/paper-skill $env:USERPROFILE\.codex\skills\paper-skill
git clone https://github.com/cLin-c/paper-skill $env:USERPROFILE\.claude\skills\paper-skill
```

For other platforms, replace `.codex` or `.claude` with `.qwen`, `.kimi`, `.deepseek`, `.comate`, `.lingma`, or `.openclaw`.

## Verify

Codex CLI:

```text
$paper-skill
```

Claude Code and most slash-command platforms:

```text
/paper-skill
```

Kimi Code CLI:

```text
/skill:paper-skill
```

Test prompt:

```text
Use paper-skill. My manuscript is written in Chinese and targets an SCI / IEEE journal. First identify the paper type, then rewrite the abstract in academic English, flag unsupported claims, and list the information I must provide. Do not invent data or references.
```
