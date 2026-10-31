---
name: release-notes
description: Write release notes or a changelog for commits since a git tag. Use when asked for release notes, a changelog, or "what shipped" since a version.
---

# Release notes

Produce release notes in the team's standard format.

1. Run `python .agents/skills/release-notes/scripts/collect_changes.py <tag>`
   (use the latest tag if none is given). It prints the grouped changes and the suggested next version.
2. Write the notes to `release-notes/<next-version>.md` using the format in `references/format.md`.
   Use the script's output as-is: do not reword, add or drop entries.
3. Do not edit any other file.
4. Reply with the file path and one sentence: how many features, fixes and breaking changes.
