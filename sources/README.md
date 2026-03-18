---
title: "Source Materials Index"
description: "Index and organization guide for reference materials in the sources directory"
author: "{{AUTHOR}}"
date: "{{DATE}}"
version: "1.0.0"
status: "active"
lang: "en"
---

# Source Materials Index

This directory contains all reference materials used to build and maintain the knowledge base. Source files are organized by format and ingested into `knowledge-base/` as structured Markdown articles.

---

## Directory Structure

```
sources/
|-- decks/          # Slide decks (PPTX, PDF exports of presentations)
|-- pdfs/           # PDF documents (reports, whitepapers, standards)
|-- images/         # Visual assets (PNG, SVG, JPG — diagrams, screenshots)
|-- docs/           # Word documents, spreadsheets (DOCX, XLSX)
|-- scripts/        # Automation scripts (Python: setup, validate, read, bump)
```

## How to Add Source Materials

1. **Place the file** in the correct subfolder based on its format.
2. **Extract content** using the document reader:
   ```bash
   make read FILE=sources/decks/my-presentation.pptx
   ```
3. **Create a knowledge article** in the appropriate `knowledge-base/{{THEME}}/` folder with proper YAML frontmatter.
4. **Create an image mirror** for any visual assets using `templates/IMAGE_MIRROR_TEMPLATE.md`.

## File Naming

Use descriptive, lowercase filenames with hyphens:

- `{{DOMAIN}}-architecture-overview.pptx`
- `{{DOMAIN}}-market-analysis-2026.pdf`
- `{{DOMAIN}}-workflow-diagram.png`
- `{{DOMAIN}}-requirements-matrix.xlsx`

## Source Inventory

| Subfolder | Format | Count | Description |
|-----------|--------|-------|-------------|
| `decks/` | PPTX, PDF | — | {{DECKS_DESCRIPTION}} |
| `pdfs/` | PDF | — | {{PDFS_DESCRIPTION}} |
| `images/` | PNG, SVG, JPG | — | {{IMAGES_DESCRIPTION}} |
| `docs/` | DOCX, XLSX | — | {{DOCS_DESCRIPTION}} |
| `scripts/` | Python, Shell | 4 | Workspace automation scripts |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/setup.sh` | Install Python dependencies in `.venv` |
| `scripts/validate_workspace.py` | Validate workspace integrity (frontmatter, structure, naming) |
| `scripts/read_doc.py` | Read and extract content from binary documents |
| `scripts/version_bump.py` | Bump semantic version in document frontmatter |

## References

- [README.md](../README.md) — Workspace overview
- [CONTRIBUTING.md](../CONTRIBUTING.md) — Guidelines for adding content
- [templates/IMAGE_MIRROR_TEMPLATE.md](../templates/IMAGE_MIRROR_TEMPLATE.md) — Image mirror template
- [templates/DOCUMENT_TEMPLATE.md](../templates/DOCUMENT_TEMPLATE.md) — Standard document template
