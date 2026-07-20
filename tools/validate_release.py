#!/usr/bin/env python3
"""Validate version, encoding, routing, and release metadata."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".ps1", ".sh"}


def validate() -> list[str]:
    errors: list[str] = []
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", version):
        errors.append(f"VERSION is not semantic: {version!r}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if len(skill.splitlines()) > 500:
        errors.append("SKILL.md exceeds the 500-line progressive-disclosure limit")
    if not skill.startswith("---\nname: paper-skill\n"):
        errors.append("SKILL.md frontmatter/name is invalid")

    agent = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "$paper-skill" not in agent:
        errors.append("agents/openai.yaml default prompt must mention $paper-skill")

    for readme_name in ("README.md", "README_EN.md"):
        readme = (ROOT / readme_name).read_text(encoding="utf-8")
        if f"version-{version.replace('-', '--')}-" not in readme:
            errors.append(f"{readme_name} version badge does not match VERSION")

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        if markdown.is_relative_to(ROOT / "docs" / "releases"):
            continue  # Historical release snapshots retain their original link layout.
        text = markdown.read_text(encoding="utf-8")
        for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            if "://" in link or link.startswith(("#", "mailto:")):
                continue
            relative = link.split("#", 1)[0]
            if relative and not (markdown.parent / relative).resolve().exists():
                errors.append(f"broken Markdown link in {markdown.relative_to(ROOT)}: {link}")

    mojibake = ("\u951b", "\u922b", "\u93c2\u56e9\u7c12", "\u9428\u52e7")
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"not valid UTF-8: {path.relative_to(ROOT)} ({exc})")
            continue
        if any(marker in text for marker in mojibake):
            errors.append(f"possible mojibake: {path.relative_to(ROOT)}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(f"ERROR: {item}" for item in failures))
        sys.exit(1)
    print("release validation passed")
