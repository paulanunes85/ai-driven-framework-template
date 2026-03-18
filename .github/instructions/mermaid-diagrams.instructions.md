---
applyTo: "**/*.md"
---

# Mermaid Diagram Rules

These rules apply when creating Mermaid diagrams in any markdown file.

## Preferred Chart Types

- **flowchart TD** — Process flows, decision trees, phase progressions
- **sequenceDiagram** — Agent interactions, API call sequences, handoff protocols
- **classDiagram** — Data models, entity relationships, component structure
- **gantt** — Roadmaps, wave plans, timeline visualizations
- **pie** — Portfolio distribution, complexity tier breakdown
- **stateDiagram-v2** — Lifecycle states, phase transitions, status workflows

## Color Scheme

Use the Azure-aligned palette for consistency:

- Primary: `#0078D4` (Azure Blue) — main flow nodes
- Secondary: `#50E6FF` (Azure Light Blue) — supporting nodes
- Accent: `#FF8C00` (Azure Orange) — highlights, warnings, decision points
- Success: `#107C10` (Green) — completed states, success paths
- Neutral: `#737373` (Gray) — inactive, archived, optional paths

Apply via `style` directives or `classDef`:

```
classDef primary fill:#0078D4,stroke:#005A9E,color:#fff
classDef accent fill:#FF8C00,stroke:#CC7000,color:#fff
classDef success fill:#107C10,stroke:#0B5A0B,color:#fff
```

## Labeling Conventions

- Node labels: concise noun phrases (max 4 words), sentence case
- Edge labels: verb phrases describing the action or data flow
- Use short IDs for nodes: `A`, `B`, `C` or descriptive like `discover`, `plan`
- Wrap long labels with `<br/>` for line breaks inside nodes
- Always label decision branches (Yes/No, Pass/Fail, True/False)

## Formatting Rules

- Always wrap Mermaid code in triple backticks with `mermaid` language identifier
- Keep diagrams under 20 nodes for readability
- Use subgraphs to group related nodes when diagram exceeds 10 nodes
- Add a brief text description before every diagram for accessibility
- Left-to-right (`LR`) for timelines and sequences; top-down (`TD`) for hierarchies
- Do not use special characters in node IDs (letters, numbers, hyphens only)
