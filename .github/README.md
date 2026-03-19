---
title: "GitHub Copilot AI Primitives"
description: "GitHub Copilot agent configuration including agents, skills, prompts, and instructions."
---

# .github -- GitHub Copilot AI Primitives

This directory contains all GitHub Copilot AI primitives that power the framework's intelligent automation. The primitives follow a strict hierarchy:

```
Agents > Skills > Prompts > Instructions
```

## Primitives Hierarchy

| Level | Directory | Purpose | Count |
|-------|-----------|---------|-------|
| **Agents** | `agents/` | Top-level orchestrators that route requests and coordinate work | 4 |
| **Skills** | `skills/` | Reusable capabilities that agents invoke to perform specific tasks | 10 |
| **Prompts** | `prompts/` | User-facing slash commands that trigger agent workflows | 6 |
| **Instructions** | `instructions/` | File-pattern-scoped rules that apply automatically to matching files | 3 |

## How It Works

1. **Users** invoke a **prompt** (slash command) like `/onboard-client`
2. The prompt routes to an **agent** (e.g., `engagement-builder`)
3. The agent loads relevant **skills** (e.g., `engagement-template`, `framework-methodology`)
4. **Instructions** apply automatically based on the file being edited (via `applyTo` patterns)

## Other GitHub Config Files

| File | Description |
|------|-------------|
| `copilot-instructions.md` | Global Copilot workspace instructions (language, naming, frontmatter rules) |
| `pull_request_template.md` | Pull request template for contributions |
| `ISSUE_TEMPLATE/` | Issue templates for bug reports and feature requests |

## Navigation

- [Root README](../README.md)
- [Sibling: .claude/](../.claude/README.md)
- [Child: agents/](agents/README.md)
- [Child: skills/](skills/README.md)
- [Child: prompts/](prompts/README.md)
- [Child: instructions/](instructions/README.md)
