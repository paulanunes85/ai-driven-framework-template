---
name: "Gap Analysis"
description: |
  Analyzes current state vs. desired state to identify gaps, risks, and recommendations.

  USE FOR:
  - Comparing current state against a target or desired state
  - Identifying capability, process, resource, or knowledge gaps
  - Producing prioritized recommendations for closing gaps
  - Creating structured assessment reports with severity ratings

  DO NOT USE FOR:
  - Reviewing document quality or formatting (use review-document)
  - Building business cases with ROI analysis (use build-business-case)
  - General document creation (use markdown)
  - Client onboarding (use onboard-client)
version: "1.0.0"
---

# Gap Analysis Skill

## Overview

Performs a structured gap analysis comparing current state against desired state, identifying gaps and producing prioritized recommendations.

## Agent

Routes to: **content-analyst**

## Input

- **Current State**: Description or documentation of the current situation.
- **Desired State**: Target state, goals, or requirements.
- **Domain** (optional): The area of focus (e.g., process, technology, capability).
- **Constraints** (optional): Known limitations or boundaries.

## Instructions

1. Read and understand both current state and desired state inputs.
2. Identify gaps across relevant dimensions:
   - **Capability Gaps**: What abilities or features are missing?
   - **Process Gaps**: What workflows or procedures need to change?
   - **Resource Gaps**: What people, tools, or budget is needed?
   - **Knowledge Gaps**: What expertise or training is required?
3. Assess each gap:
   - **Severity**: Critical / High / Medium / Low
   - **Effort to Close**: High / Medium / Low
   - **Priority**: Based on impact and effort
4. Provide recommendations for closing each gap.
5. Cite sources and state confidence levels.
6. Write the output as a Markdown document.

## Output

A structured gap analysis in Markdown:

```markdown
## Gap Analysis: {{analysis_title}}

### Executive Summary
[3-5 key findings]

### Gap Inventory

| #  | Gap Description | Category  | Severity | Effort | Priority | Recommendation       |
| -- | --------------- | --------- | -------- | ------ | -------- | -------------------- |
| 1  | ...             | ...       | ...      | ...    | ...      | ...                  |

### Detailed Findings
[Section per gap with full analysis]

### Roadmap Recommendations
[Prioritized action plan to close gaps]
```
