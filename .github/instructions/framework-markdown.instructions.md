---
applyTo: "**/*.md"
---

# Framework Markdown Rules

These rules apply to all `.md` files in this workspace.

## YAML Frontmatter (Required)

Every markdown file MUST begin with YAML frontmatter containing at minimum:
- `title` — Document title in sentence case
- `description` — One-sentence summary
- `author` — Author name
- `date` — ISO 8601 format (YYYY-MM-DD)
- `version` — Semantic version (X.Y.Z)
- `status` — One of: `draft`, `review`, `approved`, `archived`
- `lang` — Language code: `en` or `pt-BR`

## Naming Conventions

- Filenames: lowercase, hyphens as separators, no spaces
- Pattern: `{descriptive-title}_v{version}_{YYYY-MM-DD}.md`
- Example: `discovery-report_v1.2.0_2026-03-18.md`
- SKILL.md, CLAUDE.md, and AGENTS.md are exceptions (uppercase by convention)

## Language Rules

- **All content must be written in English (`lang: "en"`) by default.**
- Translations to Portuguese (`lang: "pt-BR"`) or Spanish (`lang: "es"`) only when explicitly requested by the user.
- Never mix languages in a single document.
- Technical acronyms (API, MCP, AI, LLM) remain in English regardless of document language.
- When writing in pt-BR, use formal register (voce formal, not tu). When writing in es, use usted.

## Version Management

- Increment patch (1.0.X) for typos, formatting, minor fixes
- Increment minor (1.X.0) for new sections or significant additions
- Increment major (X.0.0) for rewrites or scope changes
- Update the Change Log table with every version change
- Archive previous version to `output/md/archive/` before overwriting

## Structure Requirements

- Exactly one H1 heading per document (the document title)
- Heading levels must be sequential (never skip from H2 to H4)
- Documents with 3+ sections must include a Table of Contents
- All code blocks must specify a language identifier
- All data claims must include a source hyperlink
- End every document with a `## References` section
