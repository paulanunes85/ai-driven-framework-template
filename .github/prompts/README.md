---
title: "GitHub Copilot Prompts"
description: "User-facing slash commands that trigger agent workflows in GitHub Copilot."
---

# GitHub Copilot Prompts

This directory contains prompt definitions for GitHub Copilot. Prompts are user-facing slash commands that trigger specific agent workflows. Each prompt specifies which agent handles the request and the interaction mode.

## Contents

| Prompt | File | Routes To | Mode | Description |
|--------|------|-----------|------|-------------|
| `/build-business-case` | `build-business-case.prompt.md` | Content Analyst | generate | Produces a structured business case analysis with costs, benefits, risks, and ROI |
| `/build-deck` | `build-deck.prompt.md` | Markdown Writer | generate | Creates a structured Markdown presentation deck from provided content or topic |
| `/gap-analysis` | `gap-analysis.prompt.md` | Content Analyst | analyze | Analyzes current state vs. desired state to identify gaps, risks, and recommendations |
| `/markdown` | `markdown.prompt.md` | Markdown Writer | generate | Creates or converts content into properly structured Markdown following framework conventions |
| `/onboard-client` | `onboard-client.prompt.md` | Engagement Builder | interactive | Initiates a new client engagement by collecting information and instantiating framework templates |
| `/review-document` | `review-document.prompt.md` | Markdown Writer | review | Reviews an existing Markdown document for quality, structure, completeness, and adherence to conventions |

## Routing Summary

- **Content Analyst** handles: `/build-business-case`, `/gap-analysis`
- **Markdown Writer** handles: `/build-deck`, `/markdown`, `/review-document`
- **Engagement Builder** handles: `/onboard-client`

## Navigation

- [Root README](../../README.md)
- [Parent: .github/](../README.md)
- [Sibling: agents/](../agents/README.md)
- [Sibling: skills/](../skills/README.md)
- [Sibling: instructions/](../instructions/README.md)
