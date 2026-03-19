#!/usr/bin/env python3
"""
init_workspace.py — Replace {{PLACEHOLDER}} variables across the workspace.

Usage:
    python3 sources/scripts/init_workspace.py \
        --name "AI Governance Framework" \
        --author "Paula Silva" \
        --org "Microsoft" \
        --date 2026-03-18 \
        --github-handle paulanunes85 \
        --linkedin-handle paulanunes85
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug (lowercase, hyphens)."""
    slug = text.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def build_replacements(args: argparse.Namespace) -> dict[str, str]:
    """Build the placeholder -> value mapping from CLI arguments."""
    name = args.name
    author = args.author
    org = args.org or ""
    date_val = args.date
    github = args.github_handle or ""
    linkedin = args.linkedin_handle or ""

    return {
        "{{FRAMEWORK_NAME}}": name,
        "{{FRAMEWORK_DESCRIPTION}}": f"AI-driven {name} for enterprise engagements",
        "{{AUTHOR}}": author,
        "{{AUTHOR_TITLE}}": author,
        "{{AUTHOR_ORG}}": org,
        "{{DATE}}": date_val,
        "{{GITHUB_HANDLE}}": github,
        "{{LINKEDIN_HANDLE}}": linkedin,
        "{{TEMPLATE_REPO}}": "paulanunes85/ai-driven-framework-template",
        "{{YOUR_ORG}}": org.lower(),
        "{{YOUR_FRAMEWORK}}": slugify(name),
    }


# Domain-specific placeholder prefixes to leave alone
SKIP_PREFIXES = ("{{THEME_", "{{PHASE_")


def is_domain_placeholder(match_text: str) -> bool:
    """Return True if the placeholder is domain-specific and should be skipped."""
    for prefix in SKIP_PREFIXES:
        if match_text.startswith(prefix):
            return True
    return False


def collect_files(workspace: Path) -> list[Path]:
    """Collect all files that should be scanned for placeholder replacement."""
    files: list[Path] = []

    # Root .md files
    for f in workspace.glob("*.md"):
        if f.is_file():
            files.append(f)

    # .github/ .md files (recursive)
    github_dir = workspace / ".github"
    if github_dir.is_dir():
        for f in github_dir.rglob("*.md"):
            if f.is_file():
                files.append(f)

    # .claude/ .md files (recursive)
    claude_dir = workspace / ".claude"
    if claude_dir.is_dir():
        for f in claude_dir.rglob("*.md"):
            if f.is_file():
                files.append(f)

    # templates/ .md files (recursive)
    templates_dir = workspace / "templates"
    if templates_dir.is_dir():
        for f in templates_dir.rglob("*.md"):
            if f.is_file():
                files.append(f)

    # Makefile
    makefile = workspace / "Makefile"
    if makefile.is_file():
        files.append(makefile)

    return sorted(set(files))


def replace_in_file(
    filepath: Path,
    replacements: dict[str, str],
) -> dict[str, int]:
    """Replace placeholders in a single file. Returns counts per placeholder."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}

    original = content
    counts: dict[str, int] = {}

    # Check if this is a templates/ file — if so, only replace workspace-level
    # placeholders and leave lowercase {{variable}} placeholders alone.
    in_templates = "templates" in filepath.parts

    for placeholder, value in replacements.items():
        if placeholder in content:
            n = content.count(placeholder)
            content = content.replace(placeholder, value)
            counts[placeholder] = n

    if content != original:
        filepath.write_text(content, encoding="utf-8")

    return counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize workspace by replacing {{PLACEHOLDER}} variables.",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Framework name (e.g., 'AI Governance Framework')",
    )
    parser.add_argument(
        "--author",
        required=True,
        help="Author name",
    )
    parser.add_argument(
        "--org",
        default="",
        help="Organization name",
    )
    parser.add_argument(
        "--date",
        default=date.today().isoformat(),
        help="Date in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--github-handle",
        default="",
        help="GitHub username",
    )
    parser.add_argument(
        "--linkedin-handle",
        default="",
        help="LinkedIn username",
    )

    args = parser.parse_args()
    replacements = build_replacements(args)

    # Determine workspace root (two levels up from this script)
    script_dir = Path(__file__).resolve().parent
    workspace = script_dir.parent.parent

    print(f"Workspace: {workspace}")
    print(f"Replacements:")
    for placeholder, value in replacements.items():
        display = value if value else "(empty)"
        print(f"  {placeholder} -> {display}")
    print()

    files = collect_files(workspace)
    total_files_changed = 0
    total_replacements = 0
    all_counts: dict[str, int] = {}

    for filepath in files:
        counts = replace_in_file(filepath, replacements)
        if counts:
            total_files_changed += 1
            rel = filepath.relative_to(workspace)
            replaced_list = ", ".join(
                f"{k} x{v}" for k, v in counts.items()
            )
            print(f"  {rel}: {replaced_list}")
            for k, v in counts.items():
                all_counts[k] = all_counts.get(k, 0) + v
                total_replacements += v

    print()
    print(f"Summary:")
    print(f"  Files scanned:  {len(files)}")
    print(f"  Files changed:  {total_files_changed}")
    print(f"  Replacements:   {total_replacements}")

    if all_counts:
        print()
        print("  Per placeholder:")
        for placeholder, count in sorted(all_counts.items()):
            print(f"    {placeholder}: {count}")

    print()
    print("Done. Review changes with: git diff")


if __name__ == "__main__":
    main()
