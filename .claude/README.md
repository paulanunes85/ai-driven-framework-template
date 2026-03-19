---
title: "Claude Code AI Primitives"
description: "Claude Code agent configuration including subagents, skills, and rules."
---

# .claude -- Claude Code AI Primitives

This directory contains all Claude Code AI primitives that power the framework's intelligent automation. Claude Code uses a three-tier hierarchy:

```
Agents (Subagents) > Skills > Rules
```

## Primitives Hierarchy

| Level | Directory | Purpose | Count |
|-------|-----------|---------|-------|
| **Agents** | `agents/` | Subagents with specific model assignments that handle specialized tasks | 3 |
| **Skills** | `skills/` | Reusable capabilities combining domain knowledge and command definitions | 10 |
| **Rules** | `rules/` | Path-pattern-scoped rules that apply automatically to matching files | 3 |

## Configuration

| File | Description |
|------|-------------|
| `settings.json` | Claude Code permissions configuration (allowed and denied operations) |

## How It Works

1. The **Orchestrator** agent (using Opus model) receives the user request
2. It delegates to a generalist **subagent** (Creator or Analyst)
3. Each subagent loads relevant **skills** for domain knowledge and command execution
4. **Rules** apply automatically based on file path patterns being edited

## Parallel with GitHub Copilot

The Claude Code primitives mirror the GitHub Copilot primitives in `.github/`:

| Claude Code | GitHub Copilot | Notes |
|-------------|----------------|-------|
| `agents/` | `agents/` | Same 3 agents; Claude uses model assignments, Copilot uses tool lists |
| `skills/` | `skills/` | Same 10 skills; identical SKILL.md content |
| `rules/` | `instructions/` | Same rules; Claude uses `paths:` patterns, Copilot uses `applyTo:` |

## Navigation

- [Root README](../README.md)
- [Sibling: .github/](../.github/README.md)
- [Child: agents/](agents/README.md)
- [Child: skills/](skills/README.md)
- [Child: rules/](rules/README.md)
