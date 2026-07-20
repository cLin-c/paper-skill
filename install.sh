#!/usr/bin/env bash
set -euo pipefail

REPO="${PAPER_SKILL_REPO:-https://github.com/cLin-c/paper-skill}"
SKILL="paper-skill"

if [[ -n "${PAPER_SKILL_TARGETS:-}" ]]; then
  IFS=':' read -r -a TARGETS <<< "$PAPER_SKILL_TARGETS"
else
  TARGETS=()
  for platform in .claude .codex .openclaw .qwen .kimi .deepseek .comate .lingma; do
    [[ -d "$HOME/$platform" ]] && TARGETS+=("$HOME/$platform/skills/$SKILL")
  done
  [[ "${#TARGETS[@]}" -gt 0 ]] || TARGETS=("$HOME/.codex/skills/$SKILL")
fi

version_of() { [[ -f "$1/VERSION" ]] && tr -d '\r\n' < "$1/VERSION" || printf 'legacy'; }
is_paper_skill() { [[ -f "$1/SKILL.md" ]] && grep -Eq '^name:[[:space:]]*paper-skill[[:space:]]*$' "$1/SKILL.md"; }

install_target() {
  local target="$1" backup="" before stamp candidate
  if [[ -d "$target/.git" ]]; then
    if ! is_paper_skill "$target"; then
      printf 'refusing to update a Git directory that is not paper-skill: %s\n' "$target" >&2
      return 1
    fi
    before="$(version_of "$target")"
    git -C "$target" pull --ff-only -q
    is_paper_skill "$target" || { printf 'identity check failed after update: %s\n' "$target" >&2; return 1; }
    printf 'updated  %s  %s -> %s\n' "$target" "$before" "$(version_of "$target")"
    return
  fi

  stamp="$(date +%Y%m%d-%H%M%S)-$$"
  candidate="${target}.installing-${stamp}"
  mkdir -p "$(dirname "$target")"
  if ! git clone --depth=1 -q "$REPO" "$candidate" || ! is_paper_skill "$candidate"; then
    [[ -e "$candidate" ]] && rm -rf -- "$candidate"
    printf 'installation failed; previous install was not changed: %s\n' "$target" >&2
    return 1
  fi
  if [[ -e "$target" ]]; then
    backup="${target}.backup-${stamp}"
    mv "$target" "$backup"
    printf 'migrating %s (backup: %s)\n' "$target" "$backup"
  fi
  if ! mv "$candidate" "$target"; then
    [[ -n "$backup" && -e "$backup" ]] && mv "$backup" "$target"
    return 1
  fi
  printf 'installed %s  version %s\n' "$target" "$(version_of "$target")"
}

printf 'paper-skill installer\n'
fail=0
for target in "${TARGETS[@]}"; do install_target "$target" || fail=$((fail + 1)); done
[[ "$fail" -eq 0 ]] || { printf '%s target(s) failed\n' "$fail" >&2; exit 1; }
