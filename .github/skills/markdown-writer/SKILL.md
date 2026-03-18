---
name: "Markdown Writer"
description: "Document creation conventions including frontmatter, versioning, and structure rules."
version: "1.0.0"
---

# Markdown Writer Skill

## Overview

This skill defines the conventions for creating and maintaining all Markdown documents within the framework.

## Frontmatter Requirements

Every document must begin with YAML frontmatter:

```yaml
---
title: "Document Title"
version: "1.0.0"
last_updated: "YYYY-MM-DD"
status: draft | review | approved
author: "{{author}}"
---
```

### Optional Frontmatter Fields

```yaml
client: "{{client_name}}"
engagement: "{{engagement_id}}"
phase: "{{phase_number}}"
tags: ["{{tag1}}", "{{tag2}}"]
```

## Versioning Rules

- **PATCH** (0.0.x): Typos, formatting, minor wording changes.
- **MINOR** (0.x.0): New sections, significant content additions.
- **MAJOR** (x.0.0): Structural reorganization, major rewrites.
- Always update `last_updated` when changing `version`.

## Document Structure

### Required Sections

1. **Title** (`# Level 1`) — One per document, matches frontmatter `title`.
2. **Overview / Introduction** (`## Level 2`) — Brief context and purpose.
3. **Body Sections** (`## Level 2`) — Organized by topic.
4. **Summary / Next Steps** (`## Level 2`) — Closing section.

### Formatting Rules

- Use `##` for major sections, `###` for subsections, `####` sparingly.
- Use tables for structured comparisons (minimum 2 columns).
- Use bullet lists for 3+ related items.
- Use numbered lists only for sequential steps.
- Use code blocks for technical content, templates, or examples.
- Use blockquotes (`>`) for callouts and important notes.
- Use horizontal rules (`---`) to separate major document sections.

### Naming Conventions

| Type           | Pattern                  | Example                        |
| -------------- | ------------------------ | ------------------------------ |
| Framework docs | `UPPER_SNAKE_CASE.md`   | `METHODOLOGY_OVERVIEW.md`      |
| Client docs    | `UPPER_SNAKE_CASE.md`   | `CLIENT_ASSESSMENT.md`         |
| Templates      | `UPPER_SNAKE_CASE.md`   | `CLIENT_ENGAGEMENT_TEMPLATE.md`|

## Placeholder Convention

- Use `{{UPPER_SNAKE_CASE}}` for placeholders that must be replaced.
- Document all placeholders in a section or comment at the end of templates.
- When a value is provided, replace the placeholder completely.
- When a value is unknown, leave the placeholder intact.

## Quality Checklist

Before finalizing any document:

- [ ] YAML frontmatter is present and complete
- [ ] Version number is correct
- [ ] All headings follow hierarchy (no skipped levels)
- [ ] No unreplaced placeholders (unless intentionally deferred)
- [ ] Tables are properly formatted
- [ ] No fabricated data or citations
