---
title: "Workspace Map"
description: "Master overview document that maps the entire workspace — directories, documents, agents, skills, scripts, and templates"
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
status: "active"
lang: "en"
---

# Workspace Map

> This is the **single page to understand the entire workspace**. It maps every directory, document, agent, skill, script, and template in the repository. Start here if you are seeing this workspace for the first time.

---

## Table of Contents

- [Visual Directory Tree](#visual-directory-tree)
- [Document Registry](#document-registry)
- [Agent Registry](#agent-registry)
- [Skill Registry](#skill-registry)
- [Script Registry](#script-registry)
- [Template Registry](#template-registry)
- [Navigation Hub](#navigation-hub)
- [Cross-Reference](#cross-reference)
- [References](#references)

---

## Visual Directory Tree

The tree below shows ALL directories and key files in this workspace. Folders marked with `.gitkeep` are empty placeholders awaiting content.

```
{{FRAMEWORK_NAME}}/
|
|-- .claude/                                  # Claude Code AI primitives
|   |-- settings.json                         # Project-level Claude settings
|   |-- agents/                               # Claude Code agent definitions
|   |   |-- orchestrator/SKILL.md             #   Orchestrator agent
|   |   |-- content-analyst/SKILL.md          #   Content Analyst agent
|   |   |-- engagement-builder/SKILL.md       #   Engagement Builder agent
|   |   |-- markdown-writer/SKILL.md          #   Markdown Writer agent
|   |-- skills/                               # Claude Code skill files
|   |   |-- build-business-case/SKILL.md      #   Business case generation
|   |   |-- build-deck/SKILL.md               #   Presentation deck generation
|   |   |-- engagement-template/SKILL.md      #   Client engagement instantiation
|   |   |-- framework-methodology/SKILL.md    #   5-phase methodology knowledge
|   |   |-- gap-analysis/SKILL.md             #   Gap analysis skill
|   |   |-- markdown/SKILL.md                 #   Markdown content creation
|   |   |-- markdown-writer/SKILL.md          #   Document creation conventions
|   |   |-- market-intelligence/SKILL.md      #   Market research methodology
|   |   |-- onboard-client/SKILL.md           #   Client onboarding skill
|   |   |-- review-document/SKILL.md          #   Document review skill
|   |-- rules/                                # Claude Code behavioral rules
|       |-- agent-files.md                    #   Rules for .agent.md files
|       |-- editorial-style.md                #   Editorial/UX visual standards
|       |-- framework-markdown.md             #   Markdown formatting rules
|       |-- mermaid-diagrams.md               #   Mermaid diagram rules
|
|-- .github/                                  # GitHub Copilot & Actions configuration
|   |-- copilot-instructions.md               # Global Copilot instructions
|   |-- pull_request_template.md              # PR template
|   |-- ISSUE_TEMPLATE/                       # Issue templates
|   |   |-- bug_report.md                     #   Bug report template
|   |   |-- config.yml                        #   Issue template config
|   |   |-- feature_request.md                #   Feature request template
|   |-- agents/                               # GitHub Copilot agent definitions
|   |   |-- orchestrator.agent.md             #   Orchestrator agent
|   |   |-- content-analyst.agent.md          #   Content Analyst agent
|   |   |-- engagement-builder.agent.md       #   Engagement Builder agent
|   |   |-- markdown-writer.agent.md          #   Markdown Writer agent
|   |-- instructions/                         # GitHub Copilot behavioral instructions
|   |   |-- agent-files.instructions.md       #   Rules for agent files
|   |   |-- editorial-style.instructions.md   #   Editorial/UX visual standards
|   |   |-- framework-markdown.instructions.md#   Markdown formatting rules
|   |   |-- mermaid-diagrams.instructions.md  #   Mermaid diagram rules
|   |-- prompts/                              # Reusable slash command prompts
|   |   |-- build-business-case.prompt.md     #   /build-business-case
|   |   |-- build-deck.prompt.md              #   /build-deck
|   |   |-- gap-analysis.prompt.md            #   /gap-analysis
|   |   |-- markdown.prompt.md                #   /markdown
|   |   |-- onboard-client.prompt.md          #   /onboard-client
|   |   |-- review-document.prompt.md         #   /review-document
|   |-- skills/                               # GitHub Copilot skill files
|       |-- build-business-case/SKILL.md      #   Business case generation
|       |-- build-deck/SKILL.md               #   Presentation deck generation
|       |-- engagement-template/SKILL.md      #   Client engagement instantiation
|       |-- framework-methodology/SKILL.md    #   5-phase methodology knowledge
|       |-- gap-analysis/SKILL.md             #   Gap analysis skill
|       |-- markdown/SKILL.md                 #   Markdown content creation
|       |-- markdown-writer/SKILL.md          #   Document creation conventions
|       |-- market-intelligence/SKILL.md      #   Market research methodology
|       |-- onboard-client/SKILL.md           #   Client onboarding skill
|       |-- review-document/SKILL.md          #   Document review skill
|
|-- knowledge-base/                           # Domain knowledge by theme
|   |-- archive/                              # Deprecated content
|   |-- .gitkeep
|
|-- sources/                                  # Reference materials
|   |-- README.md                             # Source materials index
|   |-- decks/                                # Slide decks (PPTX, PDF)
|   |-- pdfs/                                 # PDF documents
|   |-- images/                               # Visual assets (PNG, SVG, JPG)
|   |-- docs/                                 # Word documents, spreadsheets
|   |-- scripts/                              # Automation scripts
|       |-- init_workspace.py                 #   Workspace initialization
|       |-- read_doc.py                       #   Document reader
|       |-- setup.sh                          #   Dependency installer
|       |-- validate_workspace.py             #   Workspace validator
|       |-- version_bump.py                   #   Version bump utility
|
|-- templates/                                # Reusable document templates
|   |-- CLIENT_ENGAGEMENT_TEMPLATE.md         # Client engagement scaffold
|   |-- DOCUMENT_TEMPLATE.md                  # Standard document template
|   |-- FRAMEWORK_SCAFFOLD.md                 # Framework scaffold guide
|   |-- IMAGE_MIRROR_TEMPLATE.md              # Image mirror template
|
|-- output/                                   # Generated deliverables
|   |-- md/archive/                           # Markdown output + archive
|   |-- pdf/archive/                          # PDF exports + archive
|   |-- pptx/archive/                         # PowerPoint exports + archive
|   |-- docx/archive/                         # Word exports + archive
|   |-- html/archive/                         # HTML exports + archive
|
|-- WORKSPACE_MAP.md                          # THIS FILE — master workspace overview
|-- README.md                                 # Entry point and overview
|-- FRAMEWORK.md                              # 5-phase methodology (source of truth)
|-- AGENTS.md                                 # Agent rules and workspace structure
|-- CLAUDE.md                                 # Claude Code session brief
|-- CONTRIBUTING.md                           # Contribution guidelines
|-- CHANGELOG.md                              # Version history
|-- LICENSE                                   # License file
|-- Makefile                                  # Workspace automation
|-- .editorconfig                             # Editor formatting rules
|-- .gitignore                                # Git ignore patterns
```

---

## Document Registry

The table below lists every Markdown file in the workspace with its purpose and which AI platform uses it.

| Path | Purpose | Platform |
|------|---------|----------|
| `README.md` | Entry point, overview, quick start, project structure | Both |
| `FRAMEWORK.md` | 5-phase methodology definition (source of truth) | Both |
| `AGENTS.md` | Agent rules, workspace conventions, naming standards | Both |
| `CLAUDE.md` | Claude Code session brief and workspace orientation | Claude |
| `CONTRIBUTING.md` | Editorial policy and contribution guidelines | Both |
| `CHANGELOG.md` | Version history (Keep a Changelog format) | Both |
| `WORKSPACE_MAP.md` | Master workspace overview (this file) | Both |
| `.github/copilot-instructions.md` | Global Copilot workspace instructions | Copilot |
| `.github/pull_request_template.md` | Pull request template | Both |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report issue template | Both |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request issue template | Both |
| `.github/agents/orchestrator.agent.md` | Orchestrator agent definition | Copilot |
| `.github/agents/content-analyst.agent.md` | Content Analyst agent definition | Copilot |
| `.github/agents/engagement-builder.agent.md` | Engagement Builder agent definition | Copilot |
| `.github/agents/markdown-writer.agent.md` | Markdown Writer agent definition | Copilot |
| `.github/instructions/agent-files.instructions.md` | Rules for agent file structure | Copilot |
| `.github/instructions/editorial-style.instructions.md` | Editorial/UX visual standards and Microsoft color palette | Copilot |
| `.github/instructions/framework-markdown.instructions.md` | Markdown formatting and frontmatter rules | Copilot |
| `.github/instructions/mermaid-diagrams.instructions.md` | Mermaid diagram rules and color scheme | Copilot |
| `.github/prompts/build-business-case.prompt.md` | `/build-business-case` slash command | Copilot |
| `.github/prompts/build-deck.prompt.md` | `/build-deck` slash command | Copilot |
| `.github/prompts/gap-analysis.prompt.md` | `/gap-analysis` slash command | Copilot |
| `.github/prompts/markdown.prompt.md` | `/markdown` slash command | Copilot |
| `.github/prompts/onboard-client.prompt.md` | `/onboard-client` slash command | Copilot |
| `.github/prompts/review-document.prompt.md` | `/review-document` slash command | Copilot |
| `.github/skills/build-business-case/SKILL.md` | Business case generation skill | Copilot |
| `.github/skills/build-deck/SKILL.md` | Deck generation skill | Copilot |
| `.github/skills/engagement-template/SKILL.md` | Engagement instantiation skill | Copilot |
| `.github/skills/framework-methodology/SKILL.md` | Methodology knowledge skill | Copilot |
| `.github/skills/gap-analysis/SKILL.md` | Gap analysis skill | Copilot |
| `.github/skills/markdown/SKILL.md` | Markdown creation skill | Copilot |
| `.github/skills/markdown-writer/SKILL.md` | Document conventions skill | Copilot |
| `.github/skills/market-intelligence/SKILL.md` | Market research skill | Copilot |
| `.github/skills/onboard-client/SKILL.md` | Client onboarding skill | Copilot |
| `.github/skills/review-document/SKILL.md` | Document review skill | Copilot |
| `.claude/agents/orchestrator/SKILL.md` | Orchestrator agent definition | Claude |
| `.claude/agents/content-analyst/SKILL.md` | Content Analyst agent definition | Claude |
| `.claude/agents/engagement-builder/SKILL.md` | Engagement Builder agent definition | Claude |
| `.claude/agents/markdown-writer/SKILL.md` | Markdown Writer agent definition | Claude |
| `.claude/rules/agent-files.md` | Rules for agent file structure | Claude |
| `.claude/rules/editorial-style.md` | Editorial/UX visual standards and Microsoft color palette | Claude |
| `.claude/rules/framework-markdown.md` | Markdown formatting and frontmatter rules | Claude |
| `.claude/rules/mermaid-diagrams.md` | Mermaid diagram rules and color scheme | Claude |
| `.claude/skills/build-business-case/SKILL.md` | Business case generation skill | Claude |
| `.claude/skills/build-deck/SKILL.md` | Deck generation skill | Claude |
| `.claude/skills/engagement-template/SKILL.md` | Engagement instantiation skill | Claude |
| `.claude/skills/framework-methodology/SKILL.md` | Methodology knowledge skill | Claude |
| `.claude/skills/gap-analysis/SKILL.md` | Gap analysis skill | Claude |
| `.claude/skills/markdown/SKILL.md` | Markdown creation skill | Claude |
| `.claude/skills/markdown-writer/SKILL.md` | Document conventions skill | Claude |
| `.claude/skills/market-intelligence/SKILL.md` | Market research skill | Claude |
| `.claude/skills/onboard-client/SKILL.md` | Client onboarding skill | Claude |
| `.claude/skills/review-document/SKILL.md` | Document review skill | Claude |
| `sources/README.md` | Source materials index and organization guide | Both |
| `templates/CLIENT_ENGAGEMENT_TEMPLATE.md` | Client engagement scaffold template | Both |
| `templates/DOCUMENT_TEMPLATE.md` | Standard document template | Both |
| `templates/FRAMEWORK_SCAFFOLD.md` | Framework scaffold step-by-step guide | Both |
| `templates/IMAGE_MIRROR_TEMPLATE.md` | Image mirror template | Both |

---

## Agent Registry

The table below lists all agents across both platforms. Each agent exists in both GitHub Copilot and Claude Code with equivalent functionality.

| Agent Name | Platform | Model | Phase Coverage | Description |
|------------|----------|-------|----------------|-------------|
| **Orchestrator** | Claude | `opus` | All phases | Routes user requests to specialized agents based on intent analysis. Does not generate content. |
| **Orchestrator** | Copilot | — | All phases | Routes user requests to specialized agents based on intent analysis. Does not generate content. |
| **Content Analyst** | Claude | `sonnet` | Phase 1, 3, 4 | Analyzes content, identifies gaps, performs competitive intelligence, and builds business cases. |
| **Content Analyst** | Copilot | — | Phase 1, 3, 4 | Analyzes content, identifies gaps, performs competitive intelligence, and builds business cases. |
| **Engagement Builder** | Claude | `sonnet` | Phase 2, 5 | Instantiates framework templates for specific client engagements, replacing placeholders with client values. |
| **Engagement Builder** | Copilot | — | Phase 2, 5 | Instantiates framework templates for specific client engagements, replacing placeholders with client values. |
| **Markdown Writer** | Claude | `sonnet` | Phase 3, 5 | Creates, updates, and formats framework and client documents following Markdown-first conventions. |
| **Markdown Writer** | Copilot | — | Phase 3, 5 | Creates, updates, and formats framework and client documents following Markdown-first conventions. |

> **Why dual-platform?** GitHub Copilot is used for IDE-integrated workflows (VS Code, GitHub.com). Claude Code is used for CLI-driven orchestration. Both share the same knowledge base, conventions, and rules.

---

## Skill Registry

Skills are domain-specific knowledge modules that agents load to perform tasks. Each skill exists on both platforms.

| Skill Name | Platform | Slash Command | Description |
|------------|----------|---------------|-------------|
| **Build Business Case** | Both | `/build-business-case` | Produces a structured business case analysis with costs, benefits, risks, and ROI |
| **Build Deck** | Both | `/build-deck` | Creates a structured Markdown presentation deck from provided content or topic |
| **Engagement Template** | Both | — | Generic client engagement instantiation rules and variable catalog for populating templates |
| **Framework Methodology** | Both | — | Core knowledge of the generic 5-phase delivery methodology |
| **Gap Analysis** | Both | `/gap-analysis` | Analyzes current state vs. desired state to identify gaps, risks, and recommendations |
| **Markdown** | Both | `/markdown` | Creates or converts content into properly structured Markdown following framework conventions |
| **Markdown Writer** | Both | — | Document creation conventions including frontmatter, versioning, and structure rules |
| **Market Intelligence** | Both | — | Generic market research and citation methodology for competitive intelligence and business case support |
| **Onboard Client** | Both | `/onboard-client` | Initiates a new client engagement by collecting information and instantiating framework templates |
| **Review Document** | Both | `/review-document` | Reviews an existing Markdown document for quality, structure, completeness, and adherence to conventions |

---

## Script Registry

All automation scripts live in `sources/scripts/` and are invoked through the `Makefile`.

| Script | Make Command | Description |
|--------|-------------|-------------|
| `init_workspace.py` | `make init NAME="..." AUTHOR="..." ORG="..."` | Replaces all `{{PLACEHOLDER}}` variables in root files to initialize a new workspace |
| `setup.sh` | `make setup` | Installs Python dependencies into a `.venv` virtual environment |
| `validate_workspace.py` | `make validate` | Validates workspace integrity: frontmatter, Markdown-first compliance, structural rules |
| `read_doc.py` | `make read FILE=...` | Reads and extracts content from documents (PPTX, PDF, DOCX, XLSX, MD) |
| `version_bump.py` | `make bump FILE=... LEVEL=...` | Bumps a document's semantic version (patch, minor, or major) |

> **Additional Makefile targets** that do not map to scripts: `make help`, `make index`, `make new-engagement CLIENT=...`, `make new-framework NAME=...`, `make clean`.

---

## Template Registry

Templates are reusable scaffolds in `templates/` that agents use to generate new documents.

| Template | When to Use | Output Location |
|----------|-------------|-----------------|
| `CLIENT_ENGAGEMENT_TEMPLATE.md` | Starting a new client engagement. Provides the full engagement profile scaffold with placeholders for client-specific information. | `output/md/{client}/` |
| `DOCUMENT_TEMPLATE.md` | Creating any new Markdown document. Provides standard frontmatter and section structure. | `output/md/` or `knowledge-base/` |
| `FRAMEWORK_SCAFFOLD.md` | Creating a brand-new framework workspace from scratch. Step-by-step guide for all required files and folders. | New workspace root |
| `IMAGE_MIRROR_TEMPLATE.md` | Creating a text-searchable Markdown mirror for a binary image (PNG, JPG, SVG). Ensures 100% text coverage. | `knowledge-base/` alongside the source image |

---

## Navigation Hub

Every README and key document in the workspace, organized by directory. Use these links to jump directly to any section.

### Root Documents

- [README.md](README.md) -- Entry point and workspace overview
- [FRAMEWORK.md](FRAMEWORK.md) -- 5-phase methodology (source of truth)
- [AGENTS.md](AGENTS.md) -- Agent rules and workspace structure
- [CLAUDE.md](CLAUDE.md) -- Claude Code session brief
- [CONTRIBUTING.md](CONTRIBUTING.md) -- Editorial policy and contribution guidelines
- [CHANGELOG.md](CHANGELOG.md) -- Version history
- [WORKSPACE_MAP.md](WORKSPACE_MAP.md) -- This file

### Source Materials

- [sources/README.md](sources/README.md) -- Source materials index

### Templates

- [templates/CLIENT_ENGAGEMENT_TEMPLATE.md](templates/CLIENT_ENGAGEMENT_TEMPLATE.md) -- Client engagement scaffold
- [templates/DOCUMENT_TEMPLATE.md](templates/DOCUMENT_TEMPLATE.md) -- Standard document template
- [templates/FRAMEWORK_SCAFFOLD.md](templates/FRAMEWORK_SCAFFOLD.md) -- Framework scaffold guide
- [templates/IMAGE_MIRROR_TEMPLATE.md](templates/IMAGE_MIRROR_TEMPLATE.md) -- Image mirror template

### Claude Code Primitives

- `.claude/settings.json` -- Project-level Claude settings
- `.claude/agents/` -- Agent definitions (orchestrator, content-analyst, engagement-builder, markdown-writer)
- `.claude/skills/` -- 10 skill files across domain areas
- `.claude/rules/` -- 4 rule files (agent-files, editorial-style, framework-markdown, mermaid-diagrams)

### GitHub Copilot Primitives

- [.github/copilot-instructions.md](.github/copilot-instructions.md) -- Global Copilot instructions
- `.github/agents/` -- 4 agent definitions (`.agent.md` format)
- `.github/skills/` -- 10 skill files (mirrored from Claude)
- `.github/instructions/` -- 4 instruction files (`.instructions.md` format)
- `.github/prompts/` -- 6 slash command prompts (`.prompt.md` format)

---

## Cross-Reference

The diagram below shows how the root documents connect to each other. Understanding this flow is key to navigating the workspace.

```
WORKSPACE_MAP.md ──> (links to everything below)
       |
       v
README.md ─────────> FRAMEWORK.md ──> knowledge-base/
    |                     |
    |                     v
    +──> AGENTS.md ──> CLAUDE.md
    |        |
    |        +──> .claude/ (agents, skills, rules)
    |        +──> .github/ (agents, skills, prompts, instructions)
    |
    +──> CONTRIBUTING.md
    +──> CHANGELOG.md
```

### Document Flow Explained

1. **WORKSPACE_MAP.md** (this file) is the master index. It links to every other document and provides the big picture.
2. **README.md** is the entry point for anyone visiting the repository. It provides quick start instructions and links to all root files.
3. **FRAMEWORK.md** is the **source of truth** for the 5-phase methodology. It defines phases, activities, deliverables, agent architecture, and governance.
4. **AGENTS.md** defines the rules that all agents must follow. It references `FRAMEWORK.md` for methodology context and governs the AI primitives in `.claude/` and `.github/`.
5. **CLAUDE.md** is the session brief loaded by Claude Code at the start of every session. It summarizes the workspace and points to `FRAMEWORK.md` and `AGENTS.md`.
6. **CONTRIBUTING.md** defines editorial policy for human contributors.
7. **CHANGELOG.md** tracks all notable changes using the Keep a Changelog format.

### Rule Mirroring

Rules are maintained in parallel across both platforms to ensure consistent behavior:

| Claude Code Rule | GitHub Copilot Instruction | Scope |
|------------------|---------------------------|-------|
| `.claude/rules/framework-markdown.md` | `.github/instructions/framework-markdown.instructions.md` | `**/*.md` |
| `.claude/rules/mermaid-diagrams.md` | `.github/instructions/mermaid-diagrams.instructions.md` | `**/*.md` |
| `.claude/rules/agent-files.md` | `.github/instructions/agent-files.instructions.md` | `**/*.agent.md` |
| `.claude/rules/editorial-style.md` | `.github/instructions/editorial-style.instructions.md` | `**/*.md` |

---

## References

- [README.md](README.md) -- Entry point and workspace overview
- [FRAMEWORK.md](FRAMEWORK.md) -- 5-phase methodology (source of truth)
- [AGENTS.md](AGENTS.md) -- Agent rules and workspace structure
- [CLAUDE.md](CLAUDE.md) -- Claude Code session brief
- [CONTRIBUTING.md](CONTRIBUTING.md) -- Editorial policy and contribution guidelines
- [CHANGELOG.md](CHANGELOG.md) -- Version history
