---
name: "Build Deck"
description: "Creates a structured Markdown presentation deck from provided content or topic."
agent: "creator"
mode: "generate"
---

# Build Deck

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

## Output

A complete Markdown deck with:
- YAML frontmatter
- One `## Section` per slide
- Bullet points for slide content
- Blockquote speaker notes
- No fabricated data or statistics
