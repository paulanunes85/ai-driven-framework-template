# Copilot Workspace Instructions

## Purpose

This is an **AI-Driven Framework** workspace. All content, templates, and deliverables are designed to be domain-agnostic and customizable through `{{PLACEHOLDER}}` variables.

## Language

- **Default language**: English (EN).
- Translate content only when explicitly requested by the user.

## Markdown-First Policy

1. **All deliverables** must be authored in Markdown (`.md`) unless the user explicitly requests another format.
2. **No binary formats** (`.docx`, `.pptx`, `.pdf`) should be generated as primary artifacts. Markdown is the source of truth; export is a secondary step.
3. **Structured headings** (`#`, `##`, `###`) must be used to organize every document. Flat walls of text are not acceptable.

## Factual Policy

- Never fabricate data, statistics, citations, or references.
- When a fact is uncertain, state the uncertainty explicitly.
- Prefer verifiable, sourced claims. Use `[Source: {{source}}]` notation when citing.

## Naming Conventions

| Artifact Type     | Convention                          | Example                          |
| ----------------- | ----------------------------------- | -------------------------------- |
| Framework docs    | `UPPER_SNAKE_CASE.md`              | `METHODOLOGY_OVERVIEW.md`        |
| Client docs       | `UPPER_SNAKE_CASE.md`              | `CLIENT_ENGAGEMENT_TEMPLATE.md`  |
| Skills            | `kebab-case/SKILL.md`              | `markdown-writer/SKILL.md`       |
| Agents            | `kebab-case.agent.md`              | `orchestrator.agent.md`          |
| Prompts           | `kebab-case.prompt.md`             | `onboard-client.prompt.md`       |
| Templates         | `UPPER_SNAKE_CASE.md`              | `CLIENT_ENGAGEMENT_TEMPLATE.md`  |

## Frontmatter

Every Markdown document must include YAML frontmatter with at least:

```yaml
---
title: "Document Title"
version: "1.0.0"
last_updated: "YYYY-MM-DD"
status: draft | review | approved
---
```

## Versioning

- Use **Semantic Versioning** (`MAJOR.MINOR.PATCH`).
- Increment `PATCH` for minor edits, `MINOR` for new sections, `MAJOR` for structural changes.

## Response Style

- Be concise and actionable.
- Use bullet points and tables over long paragraphs.
- Lead with the most important information.
- When generating documents, follow the templates in `templates/`.

## Factual Integrity

- Do not hallucinate vendor names, product capabilities, or market data.
- If information is not available in the knowledge base, say so explicitly.
- All market claims must include a citation placeholder: `[Source: {{source}}]`.
