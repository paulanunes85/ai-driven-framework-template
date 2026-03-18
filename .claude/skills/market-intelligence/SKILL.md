---
name: "Market Intelligence"
description: "Generic market research and citation methodology for competitive intelligence and business case support."
version: "1.0.0"
---

# Market Intelligence Skill

## Overview

This skill defines the methodology for conducting market research, citing sources, and producing competitive intelligence analysis. It is domain-agnostic and applies to any industry or technology area.

## Research Methodology

### Source Hierarchy

Prioritize sources in this order:

1. **Primary sources** — Direct data, interviews, official documentation.
2. **Analyst reports** — Gartner, Forrester, IDC, McKinsey, etc.
3. **Industry publications** — Peer-reviewed or editorially reviewed content.
4. **Vendor documentation** — Official product/service documentation.
5. **Community sources** — Blogs, forums, conference talks (lower confidence).

### Citation Format

All claims must be cited using the following notation:

```
[Source: Author/Organization, "Title", Date, URL (if available)]
```

When the exact source is not yet identified, use a placeholder:

```
[Source: {{source_description}}]
```

### Confidence Levels

Every analytical claim must carry a confidence rating:

| Level      | Definition                                    | Usage                           |
| ---------- | --------------------------------------------- | ------------------------------- |
| **High**   | Multiple credible sources confirm the claim   | Use in executive summaries      |
| **Medium** | One credible source or strong inference       | Use with caveats                |
| **Low**    | Estimate, extrapolation, or single weak source| Flag explicitly as estimate     |

## Competitive Analysis Framework

When analyzing competitors or alternatives:

1. **Identify** the comparison dimensions relevant to the domain.
2. **Gather** data for each dimension from credible sources.
3. **Normalize** data to enable fair comparison.
4. **Assess** strengths and weaknesses per entity.
5. **Synthesize** into actionable insights.

### Output Structure

```markdown
## Competitive Landscape

| Dimension          | {{Entity_A}} | {{Entity_B}} | {{Entity_C}} |
| ------------------ | ------------ | ------------ | ------------ |
| {{dimension_1}}    | ...          | ...          | ...          |
| {{dimension_2}}    | ...          | ...          | ...          |

### Key Differentiators
- ...

### Risks & Considerations
- ...
```

## Business Case Data Rules

- **Cost estimates** must include source and date of data.
- **ROI projections** must state assumptions explicitly.
- **Market size claims** must cite the research firm and report year.
- **Growth rates** must specify the time period and basis.
- Never round numbers in a way that changes their meaning.
- Never fabricate statistics to fill gaps — state that data is unavailable.

## Operating Rules

- If a data point cannot be verified, do not include it as fact.
- Always distinguish between "verified data" and "estimates."
- Update citations when newer data becomes available.
- Flag any data older than 2 years as potentially outdated.
