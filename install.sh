#!/usr/bin/env bash
# paper-skill universal installer — installs to all supported AI coding platforms
# Usage: curl -fsSL https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.sh | bash
set -e

REPO="https://github.com/cLin-c/paper-skill"
SKILL="paper-skill"

TARGETS=(
  "$HOME/.claude/skills/$SKILL"
  "$HOME/.codex/skills/$SKILL"
  "$HOME/.openclaw/skills/$SKILL"
  "$HOME/.qwen/skills/$SKILL"
  "$HOME/.kimi/skills/$SKILL"
  "$HOME/.deepseek/skills/$SKILL"
  "$HOME/.comate/skills/$SKILL"
  "$HOME/.lingma/skills/$SKILL"
)

ok=0; upd=0; fail=0

echo "📦  paper-skill installer"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

for TARGET in "${TARGETS[@]}"; do
  LABEL=$(echo "$TARGET" | sed "s|$HOME/||")
  if [ -d "$TARGET/.git" ]; then
    printf "↻  %-45s" "$LABEL"
    if git -C "$TARGET" pull --ff-only -q 2>/dev/null; then
      echo " updated"
      upd=$((upd + 1))
    else
      echo " (already up to date)"
      upd=$((upd + 1))
    fi
  else
    printf "✓  %-45s" "$LABEL"
    mkdir -p "$(dirname "$TARGET")"
    if git clone --depth=1 -q "$REPO" "$TARGET" 2>/dev/null; then
      echo " installed"
      ok=$((ok + 1))
    else
      echo " FAILED"
      fail=$((fail + 1))
    fi
  fi
done

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅  $ok installed, $upd updated, $fail failed"
echo ""
echo "Invoke in any supported platform:"
echo "  /paper-skill"
