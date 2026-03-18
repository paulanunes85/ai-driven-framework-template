---
name: "Review Document"
description: "Reviews an existing Markdown document for quality, structure, completeness, and adherence to conventions."
agent: "markdown-writer"
mode: "review"
---

# Review Document

## Input

- **Document**: The Markdown document to review (file path or content).
- **Review Focus** (optional): Specific aspects to emphasize (e.g., structure, accuracy, completeness).

## Instructions

1. Load and parse the document.
2. Check against the following criteria:
   - **Frontmatter**: Present, complete, and valid YAML.
   - **Structure**: Proper heading hierarchy, no skipped levels.
   - **Content Quality**: Clear, concise, actionable writing.
   - **Completeness**: No missing sections relative to the document type.
   - **Placeholders**: Identify any unreplaced `{{PLACEHOLDER}}` variables.
   - **Citations**: All claims properly sourced.
   - **Formatting**: Tables, lists, and code blocks properly formatted.
   - **Naming**: File name follows conventions.
3. Produce a structured review with findings and recommendations.

## Output

A review report in Markdown:

```markdown
## Document Review: {{document_title}}

### Summary
[Overall assessment: Pass / Pass with Comments / Needs Revision]

### Findings

| #  | Category     | Severity | Finding              | Recommendation         |
| -- | ------------ | -------- | -------------------- | ---------------------- |
| 1  | ...          | ...      | ...                  | ...                    |

### Detailed Comments
[Section-by-section feedback if needed]
```
