# Roadmap

## v0.3 - Workflow Structure

- Expand the new `workflows/` directory into a stable workflow layer.
- Add more workflow pages for:
  - Chinese draft to English submission package.
  - Reviewer response and R&R matrix.
  - Citation integrity audit.
  - Pre-submission quality gates.
- Tighten existing workflow pages:
  - `literature-review`
  - `submission-package`
  - `figure-audit`
  - `reference-tools`

## v0.4 - Toolchain and Visible Examples

- Add a runnable stage-gate checker for submission package structure.
- Add unit tests and CI for the checker.
- Add before/after examples for:
  - Chinese abstract rewriting.
  - Reviewer response.
  - Citation integrity audit.
- Add a runnable sample submission package.

## v0.5 - Stronger Automation

- Add Markdown package parsing.
- Add optional DOI lookup for reference verification.
- Add journal-specific gate profiles for SCI, IEEE, Nature-family, and conference submissions.
- Add cross-model review handoff notes for high-risk claims.
- Keep scripts optional; the skill should remain usable as prompt workflows.

## v1.0 - Stable Submission Skill Suite

- Stabilize core workflows.
- Document compatibility across Codex CLI, Claude Code, Qwen, Kimi, DeepSeek, Comate, Qoder / Lingma, and OpenClaw.
- Build a reliable example gallery for Chinese research authors.
