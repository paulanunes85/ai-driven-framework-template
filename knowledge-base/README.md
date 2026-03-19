---
title: "Knowledge Base"
description: "Theme-based knowledge organization for domain expertise and reference materials."
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
---

# Knowledge Base

This directory contains all domain knowledge organized by **theme folders**. Each theme folder groups related articles, research, and reference content that feeds into the framework methodology and deliverables.

## Structure

The knowledge base follows a theme-based organization pattern:

- Create a subfolder for each theme or domain area (e.g., `ai-strategy/`, `cloud-migration/`, `security/`)
- Place Markdown articles inside theme folders with proper YAML frontmatter
- Use the `archive/` subfolder for superseded versions of knowledge articles

All knowledge articles must follow the Markdown-first policy defined in [FRAMEWORK.md](../FRAMEWORK.md). Binary formats are never stored here; use `sources/` for PDFs, decks, and images.

## Contents

| Item | Description |
|------|-------------|
| `.gitkeep` | Placeholder to preserve the empty directory in Git |
| `archive/` | Stores superseded or deprecated versions of knowledge articles |

## Usage

1. Create a new theme folder: `knowledge-base/my-theme/`
2. Add Markdown articles with YAML frontmatter inside the theme folder
3. When updating an article, move the previous version to `archive/` before overwriting
4. Run `make index` to regenerate the knowledge base index in FRAMEWORK.md

## Related Documentation

- [FRAMEWORK.md](../FRAMEWORK.md) -- 5-phase methodology that consumes knowledge base content
- [CLAUDE.md](../CLAUDE.md) -- Workspace rules including knowledge base structure policy

## Navigation

- [Root README](../README.md)
- [Sibling: output/](../output/README.md)
- [Sibling: templates/](../templates/README.md)
- [Sibling: sources/](../sources/README.md)
