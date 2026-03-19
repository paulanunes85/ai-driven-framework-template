---
title: "Agent Rules — {{FRAMEWORK_NAME}}"
description: "Agent definitions, workspace conventions, and structural rules for the framework"
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
status: "active"
lang: "en"
---

# Agent Rules

## Table of Contents

- [Workspace Scope](#workspace-scope)
- [Essential Structure](#essential-structure)
- [Mandatory Rules](#mandatory-rules)
- [AI Primitives — Dual-Platform](#ai-primitives--dual-platform)
- [Naming Conventions](#naming-conventions)
- [Recommended Workflow](#recommended-workflow)
- [References](#references)

---

## Workspace Scope

This is the **{{FRAMEWORK_NAME}}** workspace. All agents operating in this workspace must follow the rules defined in this document. The workspace contains a knowledge base, source materials, templates, and automation tooling to support the framework methodology defined in `FRAMEWORK.md`.

---

## Essential Structure

```
{{FRAMEWORK_NAME}}/
|
|-- .claude/                          # Claude Code AI primitives
|   |-- agents/                       # Agent definitions
|   |-- skills/                       # Skill files
|   |-- rules/                        # Behavioral rules
|
|-- .github/                          # GitHub Copilot AI primitives
|   |-- agents/                       # Agent definitions
|   |-- instructions/                 # Behavioral instructions
|   |-- prompts/                      # Slash command prompts
|   |-- skills/                       # Skill files
|
|-- knowledge-base/                   # Domain knowledge by theme
|   |-- {{THEME_1}}/                  # {{THEME_1_DESCRIPTION}}
|   |-- {{THEME_2}}/                  # {{THEME_2_DESCRIPTION}}
|   |-- {{THEME_N}}/                  # {{THEME_N_DESCRIPTION}}
|   |-- archive/                      # Deprecated content
|
|-- sources/                          # Reference materials
|   |-- decks/                        # Slide decks
|   |-- pdfs/                         # PDF documents
|   |-- images/                       # Visual assets
|   |-- docs/                         # Word documents, spreadsheets
|   |-- scripts/                      # Automation scripts
|
|-- templates/                        # Reusable templates
|-- output/                           # Generated deliverables
|   |-- md/ | pdf/ | pptx/ | docx/ | html/
|
|-- README.md                         # Workspace overview
|-- FRAMEWORK.md                      # Methodology (source of truth)
|-- AGENTS.md                         # This file
|-- CLAUDE.md                         # Claude Code session brief
|-- CONTRIBUTING.md                   # Contribution guidelines
|-- CHANGELOG.md                      # Version history
```

---

## Mandatory Rules

### Markdown-First Policy

1. **Every deliverable starts as Markdown** with YAML frontmatter. Binary exports (PDF, PPTX, DOCX) are secondary outputs generated from the Markdown source.
2. **Every binary image must have a Markdown mirror** in the knowledge base. This ensures 100% text-searchable coverage across all visual assets.
3. **Frontmatter is required** on every `.md` file. At minimum: `title`, `author`, `date`, `version`. Additional fields (`status`, `tags`, `lang`, `description`) are recommended.

### Structural Rules

4. **One H1 per document**: Every Markdown file has exactly one H1 heading (the document title). Use H2 and below for sections.
5. **Sequential headings**: Never skip heading levels (e.g., do not jump from H2 to H4).
6. **Archive before overwrite**: Move the previous version of a document to `archive/` before updating. Never silently overwrite.
7. **Knowledge base integrity**: All domain knowledge lives in `knowledge-base/` organized by theme. Source materials (raw decks, PDFs) stay in `sources/`. Generated outputs go to `output/`.

### Agent Behavioral Rules

8. **Scope awareness**: Each agent must operate within its defined role. Do not perform tasks assigned to another agent without explicit delegation from the orchestrator.
9. **Minimal context**: Load only the skills and knowledge required for the current task. Maximum 4 skills per agent.
10. **Explicit handoff**: When a task requires a different agent, hand off explicitly with context (what was done, what remains, relevant file paths).
11. **Error escalation**: If an agent encounters an error or ambiguity it cannot resolve, escalate to the orchestrator rather than guessing.

### Visual and Editorial Standards

12. **SVG over Mermaid**: Prefer SVG for all diagrams. SVG provides better rendering, color control, and portability. Mermaid is acceptable as a fallback for quick drafts only.
13. **Microsoft logo color palette**: All visual elements must use the Microsoft 4-color palette — Red `#F25022`, Green `#7FBA00`, Blue `#0078D4`, Yellow `#FFB900` — with white (`#FFFFFF`) fill and black (`#000000`) text. No dark backgrounds, no gradient fills, no colored text.
14. **Explanatory context**: Every table, diagram, and code block must include a preceding or following sentence explaining what it shows and why.

---

## AI Primitives — Dual-Platform

### GitHub Copilot

| Primitive | Count | Location | Pattern |
|-----------|-------|----------|---------|
| Agents | 3 | `.github/agents/` | `{role-name}.agent.md` |
| Skills | 4 | `.github/skills/` | `{domain-name}/SKILL.md` |
| Prompts | 6 | `.github/prompts/` | `{command-name}.prompt.md` |
| Instructions | 3 | `.github/instructions/` | `{rule-name}.instructions.md` |

### Claude Code

| Primitive | Count | Location | Pattern |
|-----------|-------|----------|---------|
| Agents | 3 | `.claude/agents/` | `{role-name}.agent.md` |
| Skills | 4 | `.claude/skills/` | `{domain-name}/SKILL.md` |
| Prompts | 6 | `.claude/commands/` | `{command-name}.md` |
| Rules | 3 | `.claude/rules/` | `{rule-name}.md` |

---

## Naming Conventions

| Element | Pattern | Example |
|---------|---------|---------|
| Knowledge article | `{descriptive-slug}_v{semver}_{YYYY-MM-DD}.md` | `discovery-checklist_v1.0.0_2026-03-18.md` |
| Agent file | `{role-name}.agent.md` | `orchestrator.agent.md` |
| Skill file | `SKILL.md` (inside domain folder) | `.github/skills/{{DOMAIN}}/SKILL.md` |
| Prompt file | `{command-name}.prompt.md` | `build-business-case.prompt.md` |
| Instruction file | `{rule-name}.instructions.md` | `framework-markdown.instructions.md` |
| Rule file (Claude) | `{rule-name}.md` | `framework-markdown.md` |
| Root docs | UPPERCASE | `README.md`, `FRAMEWORK.md`, `AGENTS.md` |
| Folders | lowercase, hyphens | `knowledge-base/`, `source-materials/` |
| Image mirror | `{image-name}_mirror.md` | `architecture-diagram_mirror.md` |

---

## Recommended Workflow

> **First-time setup:** After creating a repo from this template, run `make init NAME="..." AUTHOR="..." ORG="..."` to replace all `{{PLACEHOLDER}}` variables. Then run `make setup` and `make validate` before starting any work.

The following workflow applies to any task executed within this workspace:

### 1. Understand the Request

- Read the user's request carefully.
- Identify which agent role is best suited for the task.
- Check `FRAMEWORK.md` for methodology context if the task relates to a specific phase.

### 2. Gather Context

- Use `make index` to review knowledge base coverage.
- Use `make read FILE=...` to extract content from source documents.
- Check existing documents in `knowledge-base/` and `output/` to avoid duplication.

### 3. Execute

- Follow the Markdown-First Policy for all content creation.
- Apply proper frontmatter, naming conventions, and versioning.
- Reference source materials with hyperlinks.

### 4. Validate

- Run `make validate` to check workspace integrity.
- Verify all cross-references resolve.
- Ensure the document meets the quality checklist for its type.

### 5. Deliver

- Place the deliverable in the correct `output/` subfolder.
- Update `CHANGELOG.md` if the change is notable.
- Notify the user with a summary of what was produced and where it lives.

---

## References

- [WORKSPACE_MAP.md](WORKSPACE_MAP.md) — Master workspace overview (directory tree, registries, navigation)
- [FRAMEWORK.md](FRAMEWORK.md) — 5-phase methodology (source of truth)
- [CLAUDE.md](CLAUDE.md) — Claude Code session brief
- [README.md](README.md) — Full workspace documentation and document index
- [CONTRIBUTING.md](CONTRIBUTING.md) — Editorial policy and contribution guidelines
- [templates/FRAMEWORK_SCAFFOLD.md](templates/FRAMEWORK_SCAFFOLD.md) — Framework scaffold guide
