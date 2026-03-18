---
name: "Engagement Template"
description: "Generic client engagement instantiation rules and variable catalog for populating templates."
version: "1.0.0"
---

# Engagement Template Skill

## Overview

This skill defines how to instantiate generic framework templates for a specific client engagement. It includes the variable catalog, validation rules, and instantiation workflow.

## Variable Catalog

### Required Variables

| Variable                  | Description                          | Example Value               |
| ------------------------- | ------------------------------------ | --------------------------- |
| `{{client_name}}`         | Client organization name             | "Acme Corporation"          |
| `{{engagement_id}}`       | Unique engagement identifier         | "ENG-2026-001"              |
| `{{engagement_name}}`     | Descriptive engagement name          | "Digital Transformation"    |
| `{{start_date}}`          | Engagement start date                | "2026-04-01"                |
| `{{end_date}}`            | Projected end date                   | "2026-09-30"                |
| `{{sponsor}}`             | Executive sponsor name               | "Jane Smith, CTO"           |
| `{{lead}}`                | Engagement lead name                 | "John Doe"                  |

### Optional Variables

| Variable                  | Description                          | Default                     |
| ------------------------- | ------------------------------------ | --------------------------- |
| `{{industry}}`            | Client industry                      | "{{industry}}"              |
| `{{team_size}}`           | Engagement team size                 | "TBD"                       |
| `{{budget}}`              | Engagement budget                    | "TBD"                       |
| `{{phase_name}}`          | Name of a specific phase             | "Phase N"                   |
| `{{phase_duration}}`      | Duration of a specific phase         | "{{phase_duration}}"        |
| `{{deliverable_name}}`    | Name of a specific deliverable       | "{{deliverable_name}}"      |
| `{{risk_description}}`    | Description of a specific risk       | "{{risk_description}}"      |

## Instantiation Workflow

1. **Load** the template (e.g., `CLIENT_ENGAGEMENT_TEMPLATE.md`).
2. **Collect** all required variable values from the user.
3. **Validate** that all required variables have been provided.
4. **Replace** each `{{variable}}` with its corresponding value.
5. **Review** the instantiated document for:
   - No remaining required `{{variables}}` unreplaced.
   - Dates are consistent and logical (start < end).
   - Names and identifiers are correct.
6. **Output** the final instantiated document.

## Validation Rules

- All required variables must be replaced before marking status as `review`.
- Dates must be in `YYYY-MM-DD` format.
- `{{engagement_id}}` must follow pattern: `ENG-YYYY-NNN`.
- Phase numbers must be sequential (1 through 5).
- If a variable value is unknown, keep the placeholder and set status to `draft`.

## Template Locations

| Template                         | Path                                        |
| -------------------------------- | ------------------------------------------- |
| Client Engagement                | `templates/CLIENT_ENGAGEMENT_TEMPLATE.md`   |
| {{additional_template_name}}     | `templates/{{ADDITIONAL_TEMPLATE}}.md`      |

## Operating Rules

- Never assume client information — ask if not provided.
- Always generate a substitution log showing which variables were replaced.
- Flag any inconsistencies in provided data (e.g., end date before start date).
- Keep optional variables as placeholders if no value is provided.
