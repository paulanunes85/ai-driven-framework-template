#!/usr/bin/env bash
# =============================================================================
# Framework Workspace — Environment Setup
# Creates a Python virtual environment with all dependencies for
# reading and processing PPTX, DOCX, XLSX, PDF, MD, and VTT files.
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
VENV_DIR="$WORKSPACE_DIR/.venv"

echo "Setting up framework toolkit environment..."
echo "   Workspace: $WORKSPACE_DIR"
echo "   Venv:      $VENV_DIR"

# ---- Check Python version >= 3.10 ----
PYTHON=""
for candidate in python3 python; do
    if command -v "$candidate" &>/dev/null; then
        PYTHON="$candidate"
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python not found. Please install Python 3.10 or later."
    exit 1
fi

PYTHON_VERSION=$("$PYTHON" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$("$PYTHON" -c 'import sys; print(sys.version_info.major)')
PYTHON_MINOR=$("$PYTHON" -c 'import sys; print(sys.version_info.minor)')

if [ "$PYTHON_MAJOR" -lt 3 ] || { [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]; }; then
    echo "ERROR: Python >= 3.10 is required (found $PYTHON_VERSION)."
    exit 1
fi

echo "   Python:    $PYTHON ($PYTHON_VERSION)"

# ---- Create virtual environment if it doesn't exist ----
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    "$PYTHON" -m venv "$VENV_DIR"
fi

# ---- Activate and install dependencies ----
echo "Installing dependencies..."
"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet \
    python-pptx \
    python-docx \
    openpyxl \
    pymupdf \
    lxml

echo ""
echo "Setup complete!"
echo ""
echo "To activate the environment:"
echo "  source $VENV_DIR/bin/activate"
echo ""
echo "Then you can run:"
echo "  python sources/scripts/read_doc.py <file>"
echo "  python sources/scripts/read_doc.py <file> --json"
