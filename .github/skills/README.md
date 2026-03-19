---
title: "GitHub Copilot Skills"
description: "Reusable skill definitions that agents invoke to perform specialized tasks."
---

# GitHub Copilot Skills

This directory contains skill definitions for GitHub Copilot. Skills are reusable capabilities that agents load to perform specific tasks. Each skill is defined in a `SKILL.md` file inside its own directory.

## Contents

### Domain Skills

| Skill | Directory | Description |
|-------|-----------|-------------|
| **Framework Methodology** | `framework-methodology/` | Core knowledge of the generic 5-phase delivery methodology |
| **Engagement Template** | `engagement-template/` | Generic client engagement instantiation rules and variable catalog for populating templates |
| **Market Intelligence** | `market-intelligence/` | Generic market research and citation methodology for competitive intelligence and business case support |
| **Markdown Writer** | `markdown-writer/` | Document creation conventions including frontmatter, versioning, and structure rules |

### Command Skills

| Skill | Directory | Description |
|-------|-----------|-------------|
| **Build Business Case** | `build-business-case/` | Produces a structured business case analysis with costs, benefits, risks, and ROI |
| **Build Deck** | `build-deck/` | Creates a structured Markdown presentation deck from provided content or topic |
| **Gap Analysis** | `gap-analysis/` | Analyzes current state vs. desired state to identify gaps, risks, and recommendations |
| **Markdown** | `markdown/` | Creates or converts content into properly structured Markdown following framework conventions |
| **Onboard Client** | `onboard-client/` | Initiates a new client engagement by collecting information and instantiating framework templates |
| **Review Document** | `review-document/` | Reviews an existing Markdown document for quality, structure, completeness, and adherence to conventions |

## Navigation

- [Root README](../../README.md)
- [Parent: .github/](../README.md)
- [Sibling: agents/](../agents/README.md)
- [Sibling: prompts/](../prompts/README.md)
- [Sibling: instructions/](../instructions/README.md)
