---
title: "Framework Scaffold Guide"
description: "Step-by-step recipe to create a new framework workspace from scratch"
author: "Paula Silva"
date: "2026-03-18"
version: "1.0.0"
status: "active"
tags: [scaffold, setup, workspace, template]
lang: "en"
---

# Framework Scaffold Guide

This document is a complete recipe for creating a new framework workspace from this template. Follow the steps in order to scaffold a workspace for any domain (e.g., AI Governance, Cloud Migration, DevOps Transformation).

---

## 1. Complete Directory Tree

```
{{FRAMEWORK_NAME}}/
|
|-- .claude/                          # Claude Code configuration
|   |-- settings.json                 # Project-level Claude settings
|   |-- commands/                     # Custom slash commands
|       |-- discovery.md              # Discovery phase command
|       |-- review.md                 # Review command
|
|-- .github/                          # GitHub Copilot & Actions configuration
|   |-- copilot-instructions.md       # Copilot behavior instructions
|   |-- prompts/                      # Reusable prompt files
|   |   |-- discovery.prompt.md       # Discovery prompt
|   |   |-- review.prompt.md          # Review prompt
|   |-- workflows/                    # GitHub Actions CI/CD
|       |-- ci.yml                    # Continuous integration workflow
|
|-- config/                           # Workspace configuration files
|   |-- settings.json                 # Global workspace settings
|   |-- agents.json                   # Agent definitions and roles
|
|-- knowledge-base/                   # Core framework knowledge
|   |-- concepts/                     # Fundamental concepts and definitions
|   |-- playbooks/                    # Step-by-step guides per phase
|   |-- runbooks/                     # Operational procedures
|   |-- patterns/                     # Reusable patterns and anti-patterns
|   |-- images/                       # Diagrams and visual assets
|   |-- image-mirrors/                # Markdown mirrors for all images
|
|-- sources/                          # Reference materials and research
|   |-- articles/                     # External articles and papers
|   |-- case-studies/                 # Real-world case studies
|   |-- standards/                    # Industry standards references
|
|-- templates/                        # Reusable document templates
|   |-- DOCUMENT_TEMPLATE.md          # Standard document template
|   |-- IMAGE_MIRROR_TEMPLATE.md      # Image mirror template
|   |-- CLIENT_ENGAGEMENT_TEMPLATE.md # Client engagement template
|   |-- FRAMEWORK_SCAFFOLD.md         # This file (meta-scaffold)
|
|-- output/                           # Generated deliverables
|   |-- reports/                      # Assessment and analysis reports
|   |-- presentations/                # Slide decks and summaries
|
|-- archive/                          # Deprecated or superseded content
|
|-- README.md                         # Workspace overview and entry point
|-- FRAMEWORK.md                      # Framework definition and methodology
|-- AGENTS.md                         # Agent roles and responsibilities
|-- CLAUDE.md                         # Claude Code project instructions
|-- CONTRIBUTING.md                   # Contribution guidelines
|-- CHANGELOG.md                      # Version history (Keep a Changelog)
|-- LICENSE                           # License file (MIT)
```

## 2. File Descriptions

### Root Files

| File | Purpose |
|------|---------|
| `README.md` | Primary entry point. Describes the framework, links to all sections, lists supported platforms (Claude Code, GitHub Copilot). |
| `FRAMEWORK.md` | Defines the methodology: phases, principles, decision criteria, and lifecycle. |
| `AGENTS.md` | Lists all AI agents, their roles, scopes, and interaction rules. |
| `CLAUDE.md` | Project instructions loaded automatically by Claude Code. Contains workspace rules, conventions, and constraints. |
| `CONTRIBUTING.md` | Guidelines for adding or modifying content: naming conventions, frontmatter requirements, review process. |
| `CHANGELOG.md` | Tracks all notable changes following [Keep a Changelog](https://keepachangelog.com/) format. |
| `LICENSE` | MIT license (or your chosen license). |

### Configuration

| File | Purpose |
|------|---------|
| `.claude/settings.json` | Claude Code project settings: allowed tools, permissions, memory rules. |
| `.claude/commands/*.md` | Custom slash commands for Claude Code. Each file defines one command. |
| `.github/copilot-instructions.md` | Behavioral instructions for GitHub Copilot in this workspace. |
| `.github/prompts/*.prompt.md` | Reusable prompts for GitHub Copilot chat. |
| `config/settings.json` | Global settings: language policy, naming conventions, output formats. |
| `config/agents.json` | Agent definitions: name, role, scope, tools, constraints per agent. |

### Knowledge Base

| Directory | Purpose |
|-----------|---------|
| `knowledge-base/concepts/` | Core definitions and terminology for the framework domain. |
| `knowledge-base/playbooks/` | Phase-by-phase guides with steps, inputs, outputs, and checklists. |
| `knowledge-base/runbooks/` | Operational procedures for recurring tasks. |
| `knowledge-base/patterns/` | Proven patterns and documented anti-patterns. |
| `knowledge-base/images/` | Diagrams, flowcharts, and visual assets (PNG, SVG, etc.). |
| `knowledge-base/image-mirrors/` | Markdown mirrors for every image, ensuring 100% text-searchable coverage. |

### Supporting Directories

| Directory | Purpose |
|-----------|---------|
| `sources/` | External references organized by type (articles, case studies, standards). |
| `templates/` | Reusable templates for documents, image mirrors, and client engagements. |
| `output/` | Generated deliverables: reports, presentations, exported artifacts. |
| `archive/` | Content that has been superseded or deprecated but retained for history. |

## 3. Creation Order

Follow this order to build the workspace incrementally, validating at each step:

### Step 1: Foundation

1. Create the root directory
2. Create `LICENSE`
3. Create `README.md` with a minimal description
4. Create `CHANGELOG.md` with the initial `[1.0.0]` entry

### Step 2: Configuration

5. Create `.claude/settings.json`
6. Create `config/settings.json` with language and naming policies
7. Create `config/agents.json` with at least one agent definition

### Step 3: Framework Definition

8. Create `FRAMEWORK.md` defining your methodology and phases
9. Create `AGENTS.md` listing all agent roles
10. Create `CLAUDE.md` with project instructions
11. Create `CONTRIBUTING.md` with contribution rules

### Step 4: Knowledge Base

12. Create `knowledge-base/concepts/` with foundational definitions
13. Create `knowledge-base/playbooks/` with at least one playbook per phase
14. Create `knowledge-base/runbooks/` with operational procedures
15. Create `knowledge-base/patterns/` with key patterns

### Step 5: Visual Assets

16. Add diagrams to `knowledge-base/images/`
17. Create markdown mirrors in `knowledge-base/image-mirrors/` for every image

### Step 6: Templates and Sources

18. Copy templates from this workspace or create new ones in `templates/`
19. Add reference materials to `sources/`

### Step 7: Platform Integration

20. Create `.github/copilot-instructions.md`
21. Create `.github/prompts/` with reusable prompts
22. Create `.claude/commands/` with custom slash commands

### Step 8: Validation

23. Verify every image has a markdown mirror
24. Verify all cross-links resolve correctly
25. Verify frontmatter is present and valid on all markdown files
26. Update `CHANGELOG.md` with all changes made

## 4. Conventions to Apply

| Convention | Rule |
|------------|------|
| Language | All content in English (`lang: "en"`) |
| File format | Markdown-first for all documentation |
| Frontmatter | YAML frontmatter required on every `.md` file |
| Naming | Lowercase with hyphens for folders; UPPERCASE for root docs |
| Images | Every binary image must have a corresponding markdown mirror |
| Versioning | Semantic versioning for documents and the workspace |
| Changelog | Follow [Keep a Changelog](https://keepachangelog.com/) format |

## 5. Customization Checklist

When adapting this scaffold to a new framework topic:

- [ ] Replace all `{{PLACEHOLDER}}` variables with your domain-specific values
- [ ] Update `FRAMEWORK.md` with your specific phases and methodology
- [ ] Define agents relevant to your domain in `AGENTS.md` and `config/agents.json`
- [ ] Create playbooks for each phase of your framework
- [ ] Create runbooks for recurring operational tasks in your domain
- [ ] Define patterns and anti-patterns specific to your topic
- [ ] Update templates with domain-specific fields
- [ ] Add relevant sources and references
- [ ] Verify all cross-links and update `CHANGELOG.md`

---

> **Template version:** 1.0.0
> **Template source:** `templates/FRAMEWORK_SCAFFOLD.md`
