# {{FRAMEWORK_NAME}} — Workspace Automation
# Usage: make <target> [ARGS]

SHELL := /bin/bash
WS := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
SCRIPTS := $(WS)/sources/scripts
VENV := $(WS)/.venv/bin/python3

.PHONY: help setup validate bump read index new-engagement new-framework clean

help: ## Show available commands
	@echo "{{FRAMEWORK_NAME}} — Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install Python dependencies (.venv)
	@bash $(SCRIPTS)/setup.sh

validate: ## Validate workspace integrity (frontmatter, markdown-first, structure)
	@python3 $(SCRIPTS)/validate_workspace.py

validate-json: ## Validate workspace (JSON output)
	@python3 $(SCRIPTS)/validate_workspace.py --json

bump: ## Bump document version. Usage: make bump FILE=path/to/doc.md LEVEL=minor
ifndef FILE
	$(error FILE is required. Usage: make bump FILE=path/to/doc.md LEVEL=minor)
endif
	@python3 $(SCRIPTS)/version_bump.py $(FILE) --bump $(or $(LEVEL),patch)

bump-dry: ## Dry-run version bump. Usage: make bump-dry FILE=path/to/doc.md LEVEL=minor
ifndef FILE
	$(error FILE is required. Usage: make bump-dry FILE=path/to/doc.md LEVEL=minor)
endif
	@python3 $(SCRIPTS)/version_bump.py $(FILE) --bump $(or $(LEVEL),patch) --dry-run

read: ## Read a document (PPTX, PDF, DOCX, XLSX, MD). Usage: make read FILE=path/to/file
ifndef FILE
	$(error FILE is required. Usage: make read FILE=path/to/file.pptx)
endif
	@python3 $(SCRIPTS)/read_doc.py $(FILE)

read-json: ## Read a document as JSON. Usage: make read-json FILE=path/to/file
ifndef FILE
	$(error FILE is required)
endif
	@python3 $(SCRIPTS)/read_doc.py $(FILE) --json

index: ## List all active knowledge-base documents with counts per theme
	@echo "=== Knowledge Base Index ==="
	@echo ""
	@for dir in $(WS)/knowledge-base/*/; do \
		name=$$(basename $$dir); \
		if [ "$$name" != "archive" ]; then \
			count=$$(find $$dir -maxdepth 1 -name '*.md' -type f | wc -l | tr -d ' '); \
			printf "  %-20s %s files\n" "$$name/" "$$count"; \
		fi; \
	done
	@echo ""
	@total=$$(find $(WS)/knowledge-base -not -path '*/archive/*' -maxdepth 2 -name '*.md' -type f | wc -l | tr -d ' '); \
	echo "  Total active: $$total documents"
	@archive=$$(find $(WS)/knowledge-base/archive -name '*.md' -type f 2>/dev/null | wc -l | tr -d ' '); \
	echo "  Archived:     $$archive documents"

new-engagement: ## Scaffold a new client engagement. Usage: make new-engagement CLIENT=clientname
ifndef CLIENT
	$(error CLIENT is required. Usage: make new-engagement CLIENT=serpro)
endif
	@mkdir -p $(WS)/output/md/$(CLIENT)
	@mkdir -p $(WS)/output/pdf/$(CLIENT)
	@mkdir -p $(WS)/output/pptx/$(CLIENT)
	@mkdir -p $(WS)/output/docx/$(CLIENT)
	@mkdir -p $(WS)/output/html/$(CLIENT)
	@if [ -f $(WS)/templates/CLIENT_ENGAGEMENT_TEMPLATE.md ]; then \
		today=$$(date +%Y-%m-%d); \
		sed "s/{{client_name}}/$(CLIENT)/g; s/{{date}}/$$today/g; s/{{author}}/Paula Silva/g" \
			$(WS)/templates/CLIENT_ENGAGEMENT_TEMPLATE.md \
			> $(WS)/output/md/$(CLIENT)/$(CLIENT)-engagement-profile_v1.0.0_$$today.md; \
	fi
	@echo "Engagement scaffold created:"
	@echo "  output/md/$(CLIENT)/"
	@echo "  output/pdf/$(CLIENT)/"
	@echo "  output/pptx/$(CLIENT)/"
	@echo "  output/docx/$(CLIENT)/"
	@echo "  output/html/$(CLIENT)/"
	@echo ""
	@echo "Next: edit output/md/$(CLIENT)/$(CLIENT)-engagement-profile_v1.0.0_$$(date +%Y-%m-%d).md"

new-framework: ## Scaffold a new framework workspace. Usage: make new-framework NAME=ai-governance
ifndef NAME
	$(error NAME is required. Usage: make new-framework NAME=ai-governance)
endif
	@target=$(WS)/../$(NAME); \
	mkdir -p $$target; \
	mkdir -p $$target/.claude/agents $$target/.claude/skills $$target/.claude/rules; \
	mkdir -p $$target/.github/agents $$target/.github/instructions $$target/.github/prompts $$target/.github/skills; \
	mkdir -p $$target/knowledge-base/archive; \
	mkdir -p $$target/sources/decks $$target/sources/pdfs $$target/sources/images $$target/sources/docs; \
	mkdir -p $$target/output/md/archive $$target/output/pdf/archive $$target/output/pptx/archive $$target/output/docx/archive $$target/output/html/archive; \
	mkdir -p $$target/templates $$target/config; \
	cp $(WS)/.editorconfig $$target/; \
	cp $(WS)/.gitignore $$target/; \
	cp $(WS)/LICENSE $$target/; \
	cp $(WS)/CONTRIBUTING.md $$target/; \
	cp $(WS)/Makefile $$target/; \
	cp -r $(WS)/sources/scripts $$target/sources/scripts; \
	cp -r $(WS)/templates/* $$target/templates/; \
	cp $(WS)/.claude/settings.json $$target/.claude/settings.json; \
	echo "Framework scaffold created at: $$target"; \
	echo ""; \
	echo "Next steps:"; \
	echo "  1. cd $$target"; \
	echo "  2. Create CLAUDE.md, AGENTS.md, FRAMEWORK.md, README.md"; \
	echo "  3. Add knowledge-base/ themes for your domain"; \
	echo "  4. Create agents in .github/agents/ and .claude/agents/"; \
	echo "  5. See templates/FRAMEWORK_SCAFFOLD.md for full guide"

clean: ## Remove generated artifacts (.venv, __pycache__)
	@rm -rf $(WS)/.venv $(WS)/.mypy_cache
	@find $(WS) -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned .venv and __pycache__"
