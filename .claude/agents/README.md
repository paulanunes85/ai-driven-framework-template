---
title: "Claude Code Subagents"
description: "Generalist subagents with model assignments that handle framework tasks in Claude Code."
---

# Claude Code Subagents

This directory contains subagent definitions for Claude Code. Each subagent is defined in a `SKILL.md` file inside its own directory and includes a model assignment that determines which Claude model handles its workload.

## Contents

| Agent | Directory | Model | Description |
|-------|-----------|-------|-------------|
| **Orchestrator** | `orchestrator/` | Opus | Routes user requests to the appropriate agent based on intent analysis |
| **Creator** | `creator/` | Sonnet | Generalist content creation agent. Creates documents, decks, business cases, engagement profiles, and image mirrors |
| **Analyst** | `analyst/` | Sonnet | Generalist analysis agent. Performs research, gap analysis, competitive intelligence, document review, and market research |

## Model Assignments

- **Opus** is reserved for the Orchestrator, which requires advanced reasoning for intent analysis and routing decisions
- **Sonnet** is used for both generalist agents, providing a balance of capability and efficiency for task execution

## Agent Routing

The Orchestrator delegates to generalist agents based on the user's intent:

- **Content creation** (documents, decks, business cases, client onboarding) goes to Creator
- **Analysis** (gap analysis, competitive intel, document review, market research) goes to Analyst

## Navigation

- [Root README](../../README.md)
- [Parent: .claude/](../README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: rules/](../rules/README.md)
