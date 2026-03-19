---
title: "GitHub Copilot Agents"
description: "Specialized agents that orchestrate framework workflows in GitHub Copilot."
---

# GitHub Copilot Agents

This directory contains the agent definitions for GitHub Copilot. Agents are the top-level orchestrators in the primitives hierarchy. Each agent has a defined role, a set of tools, and coordinates skills to fulfill user requests.

## Contents

| Agent | File | Description |
|-------|------|-------------|
| **Orchestrator** | `orchestrator.agent.md` | Routes user requests to the appropriate specialized agent based on intent analysis |
| **Content Analyst** | `content-analyst.agent.md` | Analyzes content, identifies gaps, performs competitive intelligence, and builds business cases |
| **Engagement Builder** | `engagement-builder.agent.md` | Instantiates framework templates for a specific client engagement, replacing placeholders with client-specific values |
| **Markdown Writer** | `markdown-writer.agent.md` | Creates, updates, and formats framework and client documents following Markdown-first conventions |

## Agent Routing

The Orchestrator agent acts as the entry point and delegates to specialized agents:

- **Content analysis requests** (gap analysis, business cases, market research) go to Content Analyst
- **Client onboarding and template instantiation** go to Engagement Builder
- **Document creation, formatting, and review** go to Markdown Writer

## Navigation

- [Root README](../../README.md)
- [Parent: .github/](../README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: prompts/](../prompts/README.md)
- [Sibling: instructions/](../instructions/README.md)
