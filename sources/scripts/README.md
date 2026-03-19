---
title: "Scripts"
description: "Automation scripts for workspace setup, validation, document reading, and version management."
---

# Scripts

This directory contains Python and shell scripts that automate workspace operations. These scripts are invoked via the `Makefile` at the repository root.

## Contents

| Script | Description | Usage |
|--------|-------------|-------|
| `setup.sh` | Creates a Python virtual environment and installs all dependencies for reading and processing PPTX, DOCX, XLSX, PDF, MD, and VTT files | `make setup` |
| `init_workspace.py` | Replaces `{{PLACEHOLDER}}` variables across the entire workspace with actual values | `make init NAME="My Framework" AUTHOR="Name" ORG="Org"` |
| `validate_workspace.py` | Validates structural and editorial integrity of the workspace (zero external dependencies) | `make validate` |
| `read_doc.py` | Unified document reader that extracts structured text from PPTX, DOCX, XLSX, PDF, MD, and VTT files | `make read FILE=path/to/file` |
| `version_bump.py` | Detects semver version in a filename and bumps the specified level (major, minor, patch) | `make bump FILE=path/to/file LEVEL=minor` |

## Examples

```bash
# First-time setup: install dependencies
make setup

# Initialize workspace with your framework details
make init NAME="AI Strategy Framework" AUTHOR="Paula Silva" ORG="Acme Corp"

# Validate workspace structure after changes
make validate

# Read a source document
make read FILE=sources/pdfs/report.pdf

# Bump a document version
make bump FILE=output/md/discovery-report_v1.0.0_2026-03-18.md LEVEL=minor
```

## Navigation

- [Root README](../../README.md)
- [Parent: sources/](../README.md)
