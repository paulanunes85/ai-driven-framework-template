---
title: "Contributing to {{FRAMEWORK_NAME}}"
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
---

# Contributing

## Editorial Policy

- **Markdown-first**: every deliverable starts as Markdown with YAML frontmatter.
- **Naming**: `<slug>-v<semver>-YYYY-MM-DD.md`
- **Frontmatter required**: title, author, date, version, status, tags.
- **Archive before overwrite**: move previous version to `archive/` before updating.

## Adding Content

### Framework knowledge (knowledge-base/)
1. Identify the correct theme folder.
2. Create the Markdown file with proper frontmatter.
3. Update cross-references if the article cites external research or data sources.

### Source materials (sources/)
1. Place the binary in the correct subfolder (`decks/`, `pdfs/`, `images/`, `docs/`).
2. Create a Markdown mirror in the appropriate `knowledge-base/` theme folder.

### Client deliverables (output/)
1. Generate in `output/md/` first.
2. Export to the target format (`output/pdf/`, `output/pptx/`, etc.).

## Adding AI Primitives

### Agents (.github/agents/)
- One `.agent.md` per agent role.
- Reference skills via `## Step 0: Load Skill Knowledge`.
- Follow the existing orchestrator pattern.

### Skills (.github/skills/)
- One `SKILL.md` per domain.
- Include quality checklist at the end.

### Prompts (.github/prompts/)
- One `.prompt.md` per slash command.
- Route to an agent via the `agent` field in frontmatter.

## Commit Messages

- Format: `[component] description` (e.g., `[knowledge-base] add Azure AI monitoring deck extraction`)
- Keep commits focused on one change.

## References

- [README.md](README.md) — Full workspace documentation with document index
- [FRAMEWORK.md](FRAMEWORK.md) — 5-phase methodology (source of truth)
- [CLAUDE.md](CLAUDE.md) — Claude Code session conventions
- [AGENTS.md](AGENTS.md) — Agent rules and workspace structure
- [Knowledge Base](knowledge-base/) — Domain knowledge organized by theme
