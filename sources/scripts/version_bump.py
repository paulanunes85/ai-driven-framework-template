#!/usr/bin/env python3
"""
Version bump for the framework workspace.

Detects a semver version in the filename, bumps the specified level,
updates the date to today, moves the old file to knowledge-base/archive/,
and renames with the new version and date. Also updates YAML frontmatter
if present.

Supported filename patterns:
    *_v{M.m.p}_*       e.g.  discovery-report_v1.2.0_2025-11-01.md
    *-v{M.m.p}-*       e.g.  planning-guide-v2.0.1-2025-11-01.md
    *_v{M.m.p}.*       e.g.  migration-guide_v1.0.0.md
    *-v{M.m.p}.*       e.g.  migration-guide-v1.0.0.md

Usage:
    python sources/scripts/version_bump.py <file> --bump major
    python sources/scripts/version_bump.py <file> --bump minor
    python sources/scripts/version_bump.py <file> --bump patch
    python sources/scripts/version_bump.py <file> --bump patch --dry-run
"""

import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

# Matches version segment in filenames using _ or - as delimiters:
#   prefix_v1.2.3_date.ext   or   prefix-v1.2.3-date.ext   or   prefix_v1.2.3.ext
VERSION_RE = re.compile(
    r"^(?P<prefix>.+?)"
    r"(?P<sep1>[_-])v(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
    r"(?:"
        r"(?P<sep2>[_-])(?P<date>\d{4}-\d{2}-\d{2})"
    r")?"
    r"(?P<ext>\.\w+)$"
)

# Frontmatter version and date patterns
FM_VERSION_RE = re.compile(r"^(version\s*:\s*[\"']?)(\d+\.\d+\.\d+)([\"']?\s*)$", re.MULTILINE)
FM_DATE_RE = re.compile(r"^(date\s*:\s*[\"']?)(\d{4}-\d{2}-\d{2})([\"']?\s*)$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def bump_version(major: int, minor: int, patch: int, level: str) -> tuple[int, int, int]:
    if level == "major":
        return major + 1, 0, 0
    elif level == "minor":
        return major, minor + 1, 0
    else:
        return major, minor, patch + 1


def find_archive_dir(filepath: Path) -> Path | None:
    """Walk up from the file's directory to find the nearest knowledge-base/archive/ path."""
    # If file is inside knowledge-base/, use knowledge-base/archive/
    try:
        rel = filepath.relative_to(ROOT / "knowledge-base")
        return ROOT / "knowledge-base" / "archive"
    except ValueError:
        pass

    # For files outside knowledge-base/, try sibling archive/ or parent archive/
    candidate = filepath.parent / "archive"
    if candidate.is_dir():
        return candidate

    candidate = filepath.parent.parent / "archive"
    if candidate.is_dir():
        return candidate

    # Default: knowledge-base/archive/ if it exists
    kb_archive = ROOT / "knowledge-base" / "archive"
    if kb_archive.is_dir():
        return kb_archive

    return None


def update_frontmatter(text: str, new_version: str, new_date: str) -> str:
    """Update version and date in YAML frontmatter if present."""
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        return text

    end = text.find("\n---\n", 4)
    if end == -1:
        end = text.find("\n---\r\n", 4)
    if end == -1:
        return text

    # We have frontmatter; update version and date within the full text
    text = FM_VERSION_RE.sub(rf"\g<1>{new_version}\g<3>", text)
    text = FM_DATE_RE.sub(rf"\g<1>{new_date}\g<3>", text)
    return text


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------

def version_bump(filepath_str: str, level: str = "patch", dry_run: bool = False) -> str:
    filepath = Path(filepath_str).resolve()

    if not filepath.is_file() and not dry_run:
        raise FileNotFoundError(f"File not found: {filepath}")

    filename = filepath.name
    match = VERSION_RE.match(filename)
    if not match:
        raise ValueError(
            f"No version pattern found in '{filename}'.\n"
            f"Expected patterns:\n"
            f"  name_v1.2.3_2025-01-01.md\n"
            f"  name-v1.2.3-2025-01-01.md\n"
            f"  name_v1.2.3.md"
        )

    prefix = match.group("prefix")
    sep1 = match.group("sep1")
    old_major = int(match.group("major"))
    old_minor = int(match.group("minor"))
    old_patch = int(match.group("patch"))
    sep2 = match.group("sep2") or sep1  # reuse separator style
    ext = match.group("ext")

    old_ver = f"{old_major}.{old_minor}.{old_patch}"
    new_major, new_minor, new_patch = bump_version(old_major, old_minor, old_patch, level)
    new_ver = f"{new_major}.{new_minor}.{new_patch}"
    today = date.today().isoformat()

    # Build new filename (always include date)
    new_filename = f"{prefix}{sep1}v{new_ver}{sep2}{today}{ext}"
    new_path = filepath.parent / new_filename

    archive_dir = find_archive_dir(filepath)

    if dry_run:
        print("[DRY RUN] Would bump:")
        print(f"  File:    {filepath}")
        print(f"  New:     {new_path}")
        print(f"  Version: v{old_ver} -> v{new_ver}")
        print(f"  Date:    {today}")
        if archive_dir:
            print(f"  Archive: {archive_dir / filename}")
        else:
            print(f"  Archive: (no archive directory found; old file would remain)")
        if ext == ".md":
            print(f"  Frontmatter: version and date fields would be updated if present")
        return str(new_path)

    if new_path.exists():
        raise FileExistsError(f"Target already exists: {new_path}")

    # Copy file to new name
    shutil.copy2(str(filepath), str(new_path))

    # Update frontmatter in the new file if it is markdown
    if ext.lower() == ".md":
        try:
            text = new_path.read_text(encoding="utf-8", errors="ignore")
            updated = update_frontmatter(text, new_ver, today)
            if updated != text:
                new_path.write_text(updated, encoding="utf-8")
                print(f"  Updated frontmatter: version={new_ver}, date={today}")
        except OSError as e:
            print(f"  Warning: could not update frontmatter: {e}")

    # Move old file to archive
    if archive_dir:
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / filename
        if archive_path.exists():
            # Avoid overwriting; add a suffix
            stem = filepath.stem
            archive_path = archive_dir / f"{stem}_superseded{ext}"
        shutil.move(str(filepath), str(archive_path))
        print(f"  Archived: {filename} -> {archive_path.relative_to(ROOT)}")
    else:
        print(f"  Warning: no archive directory found; old file left in place")

    print(f"  Version bump complete:")
    print(f"    {filename}  ->  {new_filename}")
    print(f"    Version: v{old_ver} -> v{new_ver}")
    print(f"    Date: {today}")
    print(f"    Path: {new_path}")
    return str(new_path)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def print_usage():
    print(__doc__.strip())


def main() -> None:
    args = sys.argv[1:]

    if not args or "--help" in args or "-h" in args:
        print_usage()
        sys.exit(0 if "--help" in args or "-h" in args else 1)

    filepath = args[0]
    dry_run = "--dry-run" in args

    level = "patch"  # default
    if "--bump" in args:
        idx = args.index("--bump")
        if idx + 1 < len(args):
            level = args[idx + 1].lower()
            if level not in ("major", "minor", "patch"):
                print(f"Error: --bump must be major, minor, or patch (got '{level}')")
                sys.exit(1)
        else:
            print("Error: --bump requires an argument (major|minor|patch)")
            sys.exit(1)

    try:
        version_bump(filepath, level=level, dry_run=dry_run)
    except (FileNotFoundError, ValueError, FileExistsError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
