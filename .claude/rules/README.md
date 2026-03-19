---
title: "Claude Code Rules"
description: "Path-pattern-scoped rules that apply automatically to matching files in Claude Code."
---

# Claude Code Rules

This directory contains rule files for Claude Code. Rules apply automatically based on the `paths:` patterns in their YAML frontmatter. When Claude Code operates on a file matching a pattern, the corresponding rules are loaded to enforce conventions.

## Contents

| Rule | File | Path Patterns | Description |
|------|------|---------------|-------------|
| **Framework Markdown** | `framework-markdown.md` | `**/*.md` | Enforces YAML frontmatter requirements, naming conventions, semantic versioning, heading structure, and language rules for all Markdown files |
| **Mermaid Diagrams** | `mermaid-diagrams.md` | `**/*.md` | Defines preferred chart types, Azure-aligned color scheme, labeling conventions, and formatting rules for Mermaid diagrams in Markdown |
| **Agent Files** | `agent-files.md` | `**/*.agent.md`, `.claude/agents/**` | Enforces required sections, naming conventions, and structure for agent definition files |

## How Rules Work

Rules in Claude Code are the equivalent of **instructions** in GitHub Copilot. They activate automatically when Claude Code detects a file matching the `paths:` glob patterns defined in the rule's frontmatter. This ensures consistent conventions without requiring manual invocation.

## Comparison with GitHub Copilot Instructions

| Claude Code Rule | GitHub Copilot Instruction | Shared Content |
|------------------|---------------------------|----------------|
| `framework-markdown.md` | `framework-markdown.instructions.md` | Same Markdown conventions and requirements |
| `mermaid-diagrams.md` | `mermaid-diagrams.instructions.md` | Same diagram rules and color scheme |
| `agent-files.md` | `agent-files.instructions.md` | Same agent file structure requirements |

## Navigation

- [Root README](../../README.md)
- [Parent: .claude/](../README.md)
- [Sibling: agents/](../agents/README.md)
- [Sibling: skills/](../skills/README.md)
