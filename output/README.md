---
title: "Output"
description: "Generated deliverables organized by format with per-format archive directories."
---

# Output

This directory contains all generated deliverables produced by the framework. Output is organized by file format, with each format directory containing an `archive/` subfolder for previous versions.

## Structure

The workspace follows a **Markdown-first** policy: every deliverable starts as a `.md` file. Binary exports (PDF, PPTX, DOCX, HTML) are secondary outputs generated from the Markdown source.

```
output/
  md/           # Markdown source files (primary artifacts)
    archive/    # Previous versions of Markdown deliverables
  pdf/          # PDF exports
    archive/    # Previous versions of PDF exports
  pptx/         # PowerPoint exports
    archive/    # Previous versions of PPTX exports
  docx/         # Word document exports
    archive/    # Previous versions of DOCX exports
  html/         # HTML exports
    archive/    # Previous versions of HTML exports
```

## Contents

| Directory | Description |
|-----------|-------------|
| `md/` | Markdown deliverables -- the source of truth for all output |
| `md/archive/` | Archived previous versions of Markdown deliverables |
| `pdf/` | PDF exports generated from Markdown sources |
| `pdf/archive/` | Archived previous versions of PDF exports |
| `pptx/` | PowerPoint presentation exports |
| `pptx/archive/` | Archived previous versions of PPTX exports |
| `docx/` | Word document exports |
| `docx/archive/` | Archived previous versions of DOCX exports |
| `html/` | HTML exports |
| `html/archive/` | Archived previous versions of HTML exports |

## Archive Policy

- Before overwriting any deliverable, move the previous version to the corresponding `archive/` subfolder
- Archived files retain their version number and date in the filename
- Naming pattern: `{descriptive-title}_v{semver}_{YYYY-MM-DD}.{ext}`
- Run `make bump FILE=path/to/file LEVEL=minor` to increment versions before archiving

## Navigation

- [Root README](../README.md)
- [Sibling: knowledge-base/](../knowledge-base/README.md)
- [Sibling: templates/](../templates/README.md)
- [Sibling: sources/](../sources/README.md)
