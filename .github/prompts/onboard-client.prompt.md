---
name: "Onboard Client"
description: "Initiates a new client engagement by collecting information and instantiating framework templates."
agent: "engagement-builder"
mode: "interactive"
---

# Onboard Client

## Input

- **Client Name**: The name of the client organization.
- **Engagement Scope**: Brief description of the engagement objectives.
- **Key Stakeholders**: Sponsor, lead, and team members.
- **Timeline**: Desired start and end dates.
- **Industry** (optional): Client's industry vertical.

## Instructions

1. Collect all required client information (prompt for missing fields).
2. Generate a unique engagement ID following the pattern `ENG-YYYY-NNN`.
3. Load the `CLIENT_ENGAGEMENT_TEMPLATE.md` from `templates/`.
4. Replace all `{{PLACEHOLDER}}` variables with the collected values.
5. Generate the instantiated engagement plan.
6. Produce a substitution log showing all variables replaced.

## Output

- A fully instantiated client engagement document in Markdown.
- A substitution log listing each variable and its assigned value.
- A list of any deferred variables (still containing `{{placeholders}}`).
