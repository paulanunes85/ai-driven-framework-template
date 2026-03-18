---
name: "Markdown"
description: "Creates or converts content into properly structured Markdown following framework conventions."
agent: "markdown-writer"
mode: "generate"
---

# Markdown

## Input

- **Content**: Raw text, notes, or structured data to convert to Markdown.
- **Document Type** (optional): The type of document (e.g., report, template, guide).
- **Title** (optional): Desired document title.

## Instructions

1. Analyze the input content for structure and intent.
2. Create a well-structured Markdown document:
   - Add YAML frontmatter (title, version, date, status).
   - Organize content with proper heading hierarchy.
   - Convert unstructured text into bullet points, tables, or numbered lists as appropriate.
   - Apply code blocks for technical content.
   - Add blockquotes for callouts or important notes.
3. Follow all Markdown-First Policy rules.
4. Ensure the document follows naming and versioning conventions.

## Output

A complete, well-structured Markdown document with:
- Valid YAML frontmatter
- Proper heading hierarchy
- Appropriate use of Markdown elements (tables, lists, code blocks)
- No raw/unformatted text blocks
