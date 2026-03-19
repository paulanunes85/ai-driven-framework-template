---
name: "Build Deck"
description: |
  Creates a structured Markdown presentation deck from provided content or topic.

  USE FOR:
  - Building slide decks for executive presentations, client meetings, or workshops
  - Converting existing content into a slide-ready Markdown format
  - Creating presentation outlines with speaker notes
  - Structuring a topic into a logical slide progression

  DO NOT USE FOR:
  - Creating standard documents or reports (use markdown)
  - Building business cases (use build-business-case)
  - Exporting to PowerPoint or PDF (use external tools)
  - Reviewing or editing existing decks
version: "1.0.0"
---

# Build Deck Skill

## Overview

Creates a structured Markdown presentation deck tailored to the specified topic and audience.

## Agent

Routes to: **markdown-writer**

## Input

- **Topic**: The subject of the presentation.
- **Audience**: Who will view the deck (e.g., executives, technical team, client).
- **Slide Count** (optional): Target number of slides (default: 10-15).
- **Key Messages** (optional): Specific points to emphasize.
- **Source Material** (optional): Existing documents or data to incorporate.

## Instructions

1. Analyze the topic and audience to determine appropriate depth and tone.
2. Create a Markdown document structured as a slide deck:
   - Each `## Heading` represents one slide.
   - Use concise bullet points (max 5 per slide).
   - Include speaker notes as blockquotes (`>`) below each slide.
3. Follow this slide structure:
   - Title Slide
   - Agenda / Overview
   - Context / Problem Statement
   - Key Content Slides (3-8 slides)
   - Summary / Key Takeaways
   - Next Steps / Call to Action
4. Add YAML frontmatter with title, version, date, and status.
5. Write the output file to the appropriate location.

## Output

A complete Markdown deck with:
- YAML frontmatter
- One `## Section` per slide
- Bullet points for slide content
- Blockquote speaker notes
- No fabricated data or statistics
