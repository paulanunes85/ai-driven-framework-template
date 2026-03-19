---
title: "Templates"
description: "Reusable document and scaffold templates for framework deliverables and client engagements."
---

# Templates

This directory contains reusable Markdown templates that serve as starting points for framework documents, client engagements, and other deliverables. All templates use `{{PLACEHOLDER}}` variables that are replaced with actual values during instantiation.

## Contents

| Template | Description | When to Use |
|----------|-------------|-------------|
| `CLIENT_ENGAGEMENT_TEMPLATE.md` | Scaffolds a complete client engagement document with sections for discovery, planning, and delivery | Starting a new client engagement via `/onboard-client` |
| `DOCUMENT_TEMPLATE.md` | General-purpose document template with standard frontmatter and section structure | Creating any new Markdown document via `/markdown` |
| `FRAMEWORK_SCAFFOLD.md` | Step-by-step recipe to create a new framework workspace from scratch | Setting up a brand-new framework instance from the template |
| `IMAGE_MIRROR_TEMPLATE.md` | Markdown mirror for binary images, enabling text searchability of visual content | Every time a binary image is added to `sources/images/` |

## How Templates Work

1. Templates contain `{{PLACEHOLDER}}` variables (e.g., `{{client_name}}`, `{{title}}`, `{{date}}`)
2. The Engagement Builder agent or `init_workspace.py` script replaces placeholders with actual values
3. The instantiated document is saved to the appropriate location (usually `output/md/`)
4. All templates follow the Markdown-first policy and include required YAML frontmatter

## Navigation

- [Root README](../README.md)
- [Sibling: knowledge-base/](../knowledge-base/README.md)
- [Sibling: output/](../output/README.md)
- [Sibling: sources/](../sources/README.md)
