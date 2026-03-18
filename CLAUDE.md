---
title: "Claude Code Session Brief — {{FRAMEWORK_NAME}}"
description: "Project instructions for Claude Code sessions in this workspace"
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
status: "active"
lang: "en"
---

# Claude Code Session Brief

## What This Workspace Contains

| Component | Location | Description |
|-----------|----------|-------------|
| Framework methodology | `FRAMEWORK.md` | 5-phase methodology definition (source of truth) |
| Agent rules | `AGENTS.md` | Agent roles, workspace conventions, naming standards |
| Knowledge base | `knowledge-base/` | Domain knowledge organized by theme |
| Source materials | `sources/` | Reference decks, PDFs, images, and documents |
| Templates | `templates/` | Reusable document and scaffold templates |
| Output | `output/` | Generated deliverables (Markdown-first, then export) |
| Automation | `Makefile` | Workspace commands: setup, validate, index, read, bump |
| AI primitives | `.claude/`, `.github/` | Agents, skills, prompts, rules for both platforms |

## Local Rules

1. **Language**: All content in English (`lang: "en"`) by default. Translations only when explicitly requested.
2. **Markdown-first**: Every deliverable starts as a Markdown file with YAML frontmatter. Binary exports (PDF, PPTX, DOCX) are secondary outputs.
3. **Naming convention**: `{descriptive-slug}_v{semver}_{YYYY-MM-DD}.md` for versioned documents. Root files (CLAUDE.md, AGENTS.md, FRAMEWORK.md, README.md) are uppercase by convention.
4. **Frontmatter required**: Every `.md` file must include at minimum: `title`, `author`, `date`, `version`.
5. **Archive before overwrite**: Move previous versions to `archive/` before updating a document.
6. **Knowledge base structure**: All domain knowledge lives in `knowledge-base/` organized by theme folders. Never place knowledge articles in `sources/` or `output/`.
7. **Image mirrors**: Every binary image must have a corresponding Markdown mirror for text searchability.

## Key Workflows

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/onboard-client` | Scaffolds a new client engagement with discovery templates | Starting a new client engagement |
| `/markdown` | Generates a structured Markdown document from a brief | Creating any new document |
| `/build-business-case` | Creates a business case with ROI analysis | Preparing client proposals |
| `/analyze-source` | Extracts and indexes content from source documents | Ingesting new reference materials |
| `/validate` | Runs workspace validation checks | After any structural changes |
| `/review` | Reviews a document for quality and compliance | Before finalizing deliverables |

## References

- [FRAMEWORK.md](FRAMEWORK.md) — 5-phase methodology (source of truth)
- [AGENTS.md](AGENTS.md) — Agent rules and workspace structure
- [README.md](README.md) — Full workspace documentation and document index
- [CONTRIBUTING.md](CONTRIBUTING.md) — Editorial policy and contribution guidelines
