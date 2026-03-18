---
applyTo: "**/*.agent.md"
---

# Agent File Rules

These rules apply when creating or editing `.agent.md` files.

## Required Sections

Every `.agent.md` file MUST contain these sections in order:

1. **YAML Frontmatter** — `name`, `description`, `model`, `version`
2. **Role Definition** (`## Role`) — Single paragraph stating the agent's purpose
3. **Skills** (`## Skills`) — List of skills to load, one per line as `- skill: skill-name`
4. **Tools** (`## Tools`) — Declared tool access (MCP servers, file system, code interpreter)
5. **Instructions** (`## Instructions`) — Behavioral rules and constraints
6. **Input/Output** (`## Input/Output`) — Expected input format and output schema

## Skill Loading Pattern

Load skills using the standard declaration format:

```markdown
## Skills

- skill: {{domain}}-framework
- skill: {{domain}}-analysis
- skill: markdown-writer
```

- Only load skills the agent actually needs (minimal context principle)
- Order skills by priority: primary skill first
- Maximum 4 skills per agent to avoid context dilution

## Tool Declarations

Declare tools with type and access scope:

```markdown
## Tools

- tool: file_search (scope: sources/, output/)
- tool: code_interpreter
- tool: mcp_server (url: https://mcp.example.com/{{domain}}-service)
```

- Explicitly scope file system access to required directories
- Declare MCP servers with their endpoint URLs
- Never grant broader access than the agent's role requires

## Model Selection

Specify the model in frontmatter based on task complexity:

- `claude-opus-4-20250514` — Orchestration, code transformation, complex reasoning
- `claude-sonnet-4-20250514` — Analysis, documentation, balanced tasks
- `claude-haiku-3-5-20241022` — Classification, scoring, high-throughput tasks

## Naming Convention

- Filename: `{role-name}.agent.md` (lowercase, hyphens)
- Examples: `discovery-agent.agent.md`, `orchestrator.agent.md`
- The `name` field in frontmatter must match the filename stem

## Behavioral Constraints

In the `## Instructions` section, always include:

- What the agent MUST do (positive instructions)
- What the agent MUST NOT do (guardrails and boundaries)
- How to handle errors or uncertain situations
- When to escalate or hand off to another agent
