---
title: "GitHub Copilot Agents"
description: "Generalist agents that orchestrate framework workflows in GitHub Copilot."
---

# GitHub Copilot Agents

This directory contains the agent definitions for GitHub Copilot. Agents are the top-level orchestrators in the primitives hierarchy. Each agent has a defined role, a set of tools, and coordinates skills to fulfill user requests.

## Contents

| Agent | File | Description |
|-------|------|-------------|
| **Orchestrator** | `orchestrator.agent.md` | Routes user requests to the appropriate agent based on intent analysis |
| **Creator** | `creator.agent.md` | Generalist content creation agent. Creates documents, decks, business cases, engagement profiles, and image mirrors |
| **Analyst** | `analyst.agent.md` | Generalist analysis agent. Performs research, gap analysis, competitive intelligence, document review, and market research |

## Agent Routing

The Orchestrator agent acts as the entry point and delegates to generalist agents:

- **Content creation requests** (documents, decks, business cases, client onboarding) go to Creator
- **Analysis requests** (gap analysis, competitive intel, document review, market research) go to Analyst

## Navigation

- [Root README](../../README.md)
- [Parent: .github/](../README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: prompts/](../prompts/README.md)
- [Sibling: instructions/](../instructions/README.md)
