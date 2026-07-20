# Installation

paper-skill can be installed into the common skill directories used by Codex CLI, Claude Code, Qwen Code, Kimi Code CLI, DeepSeek / Deep Code, Baidu Comate, Qoder / Lingma, and OpenClaw.

Prerequisites: Git, network access to GitHub, and a supported agent host. The optional executable verification tools require Python 3.10 or newer. Restart or reload the agent host after first installation if the skill is not discovered immediately.

## One-Command Install

macOS / Linux / Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
```

The installer detects platform directories already present on the machine and installs only to those hosts; if none are detected, it defaults to Codex. It does not create eight unrelated platform installations. Since v0.8.0 it also detects legacy copy-based installs, clones and validates a replacement before switching, preserves the old copy as a timestamped backup, and rejects unrelated Git repositories.

## Update or migrate an existing install

Run the same one-command installer again. Git-managed installs receive a fast-forward update. A directory without `.git` is treated as a legacy install and preserved as `paper-skill.backup-YYYYMMDD-HHMMSS` before migration.

The Windows script also supports a preview:

```powershell
./install.ps1 -DryRun
```

Each installed copy includes [VERSION](../VERSION). Confirm that the target directory contains both `SKILL.md` and `VERSION` after installation.

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

Success means the response identifies a route, distinguishes supplied evidence from missing author input, and does not invent bibliographic or experimental facts. If the skill is not found, confirm that `SKILL.md` and `VERSION` exist under the host path above, then restart/reload the host.
