---
title: "GitHub Copilot Instructions"
description: "File-pattern-scoped rules that apply automatically to matching files in GitHub Copilot."
---

# GitHub Copilot Instructions

This directory contains instruction files for GitHub Copilot. Instructions are rules that apply automatically based on the `applyTo` glob pattern in their frontmatter. When a user edits a file matching the pattern, Copilot loads the corresponding instructions.

## Contents

| Instruction | File | applyTo Pattern | Description |
|-------------|------|-----------------|-------------|
| **Framework Markdown** | `framework-markdown.instructions.md` | `**/*.md` | Enforces YAML frontmatter requirements, naming conventions, version management, heading structure, and language rules for all Markdown files |
| **Mermaid Diagrams** | `mermaid-diagrams.instructions.md` | `**/*.md` | Defines preferred chart types, Azure-aligned color scheme, labeling conventions, and formatting rules for Mermaid diagrams |
| **Agent Files** | `agent-files.instructions.md` | `**/*.agent.md` | Enforces required sections (frontmatter, role, skills, rules, output), naming, and structure for agent definition files |

## How Instructions Work

Unlike prompts (which are user-triggered) or skills (which are agent-loaded), instructions activate **automatically** when Copilot detects a file matching the `applyTo` pattern. This ensures consistent conventions across the workspace without requiring manual invocation.

## Navigation

- [Root README](../../README.md)
- [Parent: .github/](../README.md)
- [Sibling: agents/](../agents/README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: prompts/](../prompts/README.md)
