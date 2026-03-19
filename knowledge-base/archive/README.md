---
title: "Knowledge Base Archive"
description: "Storage for superseded and deprecated versions of knowledge base articles."
---

# Knowledge Base Archive

This directory stores previous versions of knowledge base articles that have been superseded by newer revisions.

## Purpose

Following the workspace rule "archive before overwrite," every time a knowledge article is updated, the previous version must be moved here before the new version takes its place. This ensures a complete audit trail and the ability to recover prior content.

## Version Management

- Files are archived with their original filename, preserving the version number and date in the name
- Naming pattern: `{descriptive-title}_v{semver}_{YYYY-MM-DD}.md`
- Archived files retain their original YAML frontmatter with `status: "archived"`
- Use `version_bump.py` from `sources/scripts/` to increment versions before archiving

## Contents

| Item | Description |
|------|-------------|
| `.gitkeep` | Placeholder to preserve the empty directory in Git |

## Navigation

- [Root README](../../README.md)
- [Parent: knowledge-base/](../README.md)
