---
name: "Build Business Case"
description: "Produces a structured business case analysis with costs, benefits, risks, and ROI."
agent: "creator"
mode: "generate"
---

# Build Business Case

## Input

- **Initiative**: Description of the proposed initiative or project.
- **Current State**: Description of the current situation and pain points.
- **Desired Outcome**: What success looks like.
- **Budget Context** (optional): Available budget or investment range.
- **Timeline** (optional): Expected implementation timeline.
- **Data Sources** (optional): Any existing data, reports, or references.

## Instructions

1. Analyze the initiative against the current state.
2. Structure the business case with these sections:
   - **Executive Summary**: 3-5 bullet point overview.
   - **Problem Statement**: Current challenges and their business impact.
   - **Proposed Solution**: What is being recommended.
   - **Cost Analysis**: Implementation costs (use estimates with confidence levels if exact data unavailable).
   - **Benefit Analysis**: Quantified and qualitative benefits.
   - **Risk Assessment**: Key risks with likelihood and mitigation.
   - **ROI Projection**: Return on investment with stated assumptions.
   - **Recommendation**: Clear go/no-go recommendation with rationale.
3. Cite all data sources using `[Source: {{source}}]` notation.
4. State confidence levels for all projections and estimates.

## Output

A complete Markdown business case document with:
- YAML frontmatter
- All sections listed above
- Citations for all data points
- Confidence ratings for estimates
- Clear assumptions stated
