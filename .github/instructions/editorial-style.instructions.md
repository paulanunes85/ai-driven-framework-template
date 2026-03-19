---
applyTo: "**/*.md"
---

# Editorial Style Rules

## Visual Standards

### Diagram Policy
- **Use SVG over Mermaid** for all diagrams. SVG provides better rendering, color control, and portability.
- When SVG is not feasible (quick drafts), Mermaid is acceptable as a fallback.
- Every diagram must have an explanatory text paragraph before or after it describing what the diagram shows.

### Microsoft Logo Color Palette
All visual elements must use the Microsoft logo 4-color palette:
- Red: `#F25022` — for borders, outlines, and accents
- Green: `#7FBA00` — for borders, outlines, and accents
- Blue: `#0078D4` — for borders, outlines, and accents
- Yellow: `#FFB900` — for borders, outlines, and accents
- White: `#FFFFFF` — always for fill/background
- Black: `#000000` — always for text

### Color Application Rules
- **Borders and outlines**: Use the 4 Microsoft colors, rotating per section/element
- **Fill/background**: Always white (`#FFFFFF`)
- **Text**: Always black (`#000000`)
- **No dark backgrounds, no gradient fills, no colored text**

## Document UX

### Icons and Highlights
- Use Unicode icons to improve scannability: checkmark, cross, warning, clipboard, link, chart, target, lightbulb, pin, magnifier
- Use **bold** for key terms on first use
- Use `inline code` for technical terms, file names, commands
- Use blockquotes `>` for callouts, tips, and important notes
- Use horizontal rules `---` to separate major sections

### Explanatory Text
- Every table must have a one-sentence introduction explaining what it shows
- Every diagram/image must have a descriptive paragraph (not just a caption)
- Every code block must have a comment or preceding text explaining what it does

### Educational/Didactic Tone
- Write for someone seeing this workspace for the first time
- Explain "why" not just "what"
- Use numbered steps for sequential processes
- Use bullet points for non-sequential items
- Prefer short paragraphs (3-4 sentences max)
