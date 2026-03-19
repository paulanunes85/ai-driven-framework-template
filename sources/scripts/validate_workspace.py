#!/usr/bin/env python3
"""
Validates the structural and editorial integrity of the framework
workspace. Zero external dependencies (pathlib, re, os, sys only).

Usage:
    python sources/scripts/validate_workspace.py
    python sources/scripts/validate_workspace.py --json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FRONTMATTER = {"title", "description", "author", "date", "version"}

# knowledge-base naming convention (warn only):
#   lowercase-kebab-case with optional version/date segments
KB_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*\.md$")

REQUIRED_ROOT_FILES = ["CLAUDE.md", "AGENTS.md", "FRAMEWORK.md", "README.md", "CONTRIBUTING.md"]
REQUIRED_DIRS = ["knowledge-base", "sources", "output", ".github", ".claude"]

BINARY_EXTENSIONS = {".pptx", ".pdf", ".docx", ".png", ".jpg", ".jpeg"}

# ---------------------------------------------------------------------------
# Terminal colours (no dependencies)
# ---------------------------------------------------------------------------

_USE_COLOR = sys.stdout.isatty()

def _color(code: str, text: str) -> str:
    if not _USE_COLOR:
        return text
    return f"\033[{code}m{text}\033[0m"

def green(text: str) -> str:
    return _color("32", text)

def red(text: str) -> str:
    return _color("31", text)

def yellow(text: str) -> str:
    return _color("33", text)

def bold(text: str) -> str:
    return _color("1", text)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse YAML frontmatter delimited by --- fences."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        end = text.find("\n---\r\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def kb_markdown_files(include_archive: bool = False) -> list[Path]:
    """Return all .md files under knowledge-base/, optionally excluding archive/."""
    kb = ROOT / "knowledge-base"
    if not kb.is_dir():
        return []
    paths = sorted(kb.rglob("*.md"))
    if not include_archive:
        paths = [p for p in paths if "archive" not in p.relative_to(kb).parts]
    return [p for p in paths if p.name != ".gitkeep"]


def kb_archive_files() -> list[Path]:
    """Return all .md files under knowledge-base/archive/."""
    archive = ROOT / "knowledge-base" / "archive"
    if not archive.is_dir():
        return []
    return sorted(p for p in archive.rglob("*.md") if p.name != ".gitkeep")


def collect_binaries_in_sources() -> list[Path]:
    """Return all binary files in sources/ by extension."""
    sources = ROOT / "sources"
    if not sources.is_dir():
        return []
    results: list[Path] = []
    for p in sorted(sources.rglob("*")):
        if p.is_file() and p.suffix.lower() in BINARY_EXTENSIONS:
            results.append(p)
    return results


# ---------------------------------------------------------------------------
# Check implementations
# ---------------------------------------------------------------------------

CheckResult = tuple[bool, str, list[str]]  # (passed, label, details)


def check_yaml_frontmatter() -> CheckResult:
    """Every .md in knowledge-base/ (not archive/) has required frontmatter."""
    label = "YAML Frontmatter"
    details: list[str] = []
    files = kb_markdown_files(include_archive=False)
    if not files:
        return True, label, ["No markdown files found in knowledge-base/ (skipped)"]

    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            details.append(f"  Could not read: {path.relative_to(ROOT)}")
            continue
        fm = parse_frontmatter(text)
        if not fm:
            details.append(f"  Missing frontmatter: {path.relative_to(ROOT)}")
            continue
        missing = sorted(REQUIRED_FRONTMATTER - set(fm))
        if missing:
            details.append(
                f"  {path.relative_to(ROOT)}: missing fields: {', '.join(missing)}"
            )

    passed = len(details) == 0
    return passed, label, details


def check_markdown_first() -> CheckResult:
    """Every binary in sources/ has at least one .md that references it."""
    label = "Markdown-First (binary coverage)"
    details: list[str] = []
    binaries = collect_binaries_in_sources()
    if not binaries:
        return True, label, ["No binary files in sources/ (skipped)"]

    # Build a lookup of all KB markdown content + frontmatter source_image values
    kb_files = kb_markdown_files(include_archive=True)
    all_text_lower: list[str] = []
    source_images: set[str] = set()
    for md_path in kb_files:
        try:
            text = md_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        all_text_lower.append(text.lower())
        fm = parse_frontmatter(text)
        si = fm.get("source_image", "")
        if si:
            source_images.add(si.lower())

    combined_text = "\n".join(all_text_lower)

    for binary in binaries:
        fname = binary.name.lower()
        stem = binary.stem.lower()
        rel = str(binary.relative_to(ROOT)).lower()
        # Check: filename substring in any KB markdown, or source_image reference
        found = (
            fname in combined_text
            or stem in combined_text
            or rel in combined_text
            or any(fname in si or stem in si for si in source_images)
        )
        if not found:
            details.append(f"  No KB reference found for: {binary.relative_to(ROOT)}")

    passed = len(details) == 0
    return passed, label, details


def check_naming_convention() -> CheckResult:
    """Files in knowledge-base/ follow kebab-case naming (warn only)."""
    label = "Naming Convention (advisory)"
    details: list[str] = []
    files = kb_markdown_files(include_archive=False)

    for path in files:
        if not KB_NAME_RE.match(path.name):
            details.append(f"  Non-standard name: {path.relative_to(ROOT)}")

    # This is advisory — always passes, details are warnings
    return True, label, details


def check_required_root_files() -> CheckResult:
    """Required root files exist."""
    label = "Required Root Files"
    details: list[str] = []

    for fname in REQUIRED_ROOT_FILES:
        if not (ROOT / fname).is_file():
            details.append(f"  Missing: {fname}")

    passed = len(details) == 0
    return passed, label, details


def check_required_directories() -> CheckResult:
    """Required directories exist."""
    label = "Required Directories"
    details: list[str] = []

    for dname in REQUIRED_DIRS:
        if not (ROOT / dname).is_dir():
            details.append(f"  Missing directory: {dname}/")

    passed = len(details) == 0
    return passed, label, details


def check_archive_duplicates() -> CheckResult:
    """No file in knowledge-base/archive/ has a duplicate in active KB folders."""
    label = "Archive Duplicates"
    details: list[str] = []

    active_names: set[str] = set()
    for path in kb_markdown_files(include_archive=False):
        active_names.add(path.name)

    for path in kb_archive_files():
        if path.name == "README.md":
            continue
        if path.name in active_names:
            details.append(
                f"  Duplicate in active KB: {path.name} (exists in both archive and active)"
            )

    passed = len(details) == 0
    return passed, label, details


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_all_checks() -> list[CheckResult]:
    return [
        check_yaml_frontmatter(),
        check_markdown_first(),
        check_naming_convention(),
        check_required_root_files(),
        check_required_directories(),
        check_archive_duplicates(),
    ]


def main() -> None:
    results = run_all_checks()

    if "--json" in sys.argv:
        output = []
        for passed, label, details in results:
            output.append({"check": label, "passed": passed, "details": details})
        print(json.dumps(output, indent=2, ensure_ascii=False))
        any_fail = any(not passed for passed, _, _ in results)
        raise SystemExit(1 if any_fail else 0)

    # Pretty terminal output
    print()
    print(bold("=== Framework Workspace Validation ==="))
    print(f"    Root: {ROOT}")
    print()

    total = len(results)
    passed_count = 0
    failed_count = 0
    warning_details: list[tuple[str, list[str]]] = []

    for passed, label, details in results:
        if label.endswith("(advisory)"):
            # Advisory checks always show as WARN if they have details
            if details:
                tag = yellow("WARN")
                warning_details.append((label, details))
            else:
                tag = green("PASS")
            passed_count += 1  # advisory does not count as failure
        elif passed:
            tag = green("PASS")
            passed_count += 1
        else:
            tag = red("FAIL")
            failed_count += 1

        print(f"  [{tag}] {label}")
        if not passed and details:
            for d in details:
                print(f"        {d}")

    # Print advisory warnings at the end
    if warning_details:
        print()
        print(yellow("--- Advisory Warnings ---"))
        for label, details in warning_details:
            print(f"  {label}:")
            for d in details:
                print(f"      {d}")

    print()
    summary = f"Summary: {passed_count}/{total} passed"
    if failed_count:
        summary += f", {red(str(failed_count) + ' failed')}"
        print(bold(red(summary)))
    else:
        print(bold(green(summary)))
    print()

    raise SystemExit(1 if failed_count > 0 else 0)


if __name__ == "__main__":
    main()
