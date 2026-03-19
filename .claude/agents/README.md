---
title: "Claude Code Subagents"
description: "Specialized subagents with model assignments that handle framework tasks in Claude Code."
---

# Claude Code Subagents

This directory contains subagent definitions for Claude Code. Each subagent is defined in a `SKILL.md` file inside its own directory and includes a model assignment that determines which Claude model handles its workload.

## Contents

| Agent | Directory | Model | Description |
|-------|-----------|-------|-------------|
| **Orchestrator** | `orchestrator/` | Opus | Routes user requests to the appropriate specialized agent based on intent analysis |
| **Content Analyst** | `content-analyst/` | Sonnet | Analyzes content, identifies gaps, performs competitive intelligence, and builds business cases |
| **Engagement Builder** | `engagement-builder/` | Sonnet | Instantiates framework templates for a specific client engagement, replacing placeholders with client-specific values |
| **Markdown Writer** | `markdown-writer/` | Sonnet | Creates, updates, and formats framework and client documents following Markdown-first conventions |

## Model Assignments

- **Opus** is reserved for the Orchestrator, which requires advanced reasoning for intent analysis and routing decisions
- **Sonnet** is used for all specialized agents, providing a balance of capability and efficiency for task execution

## Agent Routing

The Orchestrator delegates to specialized agents based on the user's intent:

- **Content analysis** (gap analysis, business cases, market research) goes to Content Analyst
- **Client onboarding and template instantiation** goes to Engagement Builder
- **Document creation, formatting, and review** goes to Markdown Writer

## Navigation

- [Root README](../../README.md)
- [Parent: .claude/](../README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: rules/](../rules/README.md)
