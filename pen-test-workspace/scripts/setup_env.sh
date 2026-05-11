#!/bin/bash
#====================================================================
# AI Agent Environment Setup Script
#====================================================================

set -e

WORKSPACE_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "========================================"
echo "  AI Agent Workspace Setup"
echo "========================================"

# Create necessary directories
mkdir -p "$WORKSPACE_ROOT/output/reports"
mkdir -p "$WORKSPACE_ROOT/output/logs"
mkdir -p "$WORKSPACE_ROOT/output/artifacts"
mkdir -p "$WORKSPACE_ROOT/output/screenshots"

mkdir -p "$WORKSPACE_ROOT/compliance/recordings/screen"
mkdir -p "$WORKSPACE_ROOT/compliance/recordings/terminal"
mkdir -p "$WORKSPACE_ROOT/compliance/recordings/network"
mkdir -p "$WORKSPACE_ROOT/compliance/logs/audit"
mkdir -p "$WORKSPACE_ROOT/compliance/logs/command"
mkdir -p "$WORKSPACE_ROOT/compliance/logs/session"
mkdir -p "$WORKSPACE_ROOT/compliance/evidence/chain-of-custody"
mkdir -p "$WORKSPACE_ROOT/compliance/evidence/hashes"
mkdir -p "$WORKSPACE_ROOT/compliance/evidence/signatures"

mkdir -p "$WORKSPACE_ROOT/workspace-data/current-session"
mkdir -p "$WORKSPACE_ROOT/workspace-data/sessions-history"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/vulnerabilities"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/techniques"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/best_practices"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/learned_lessons"

mkdir -p "$WORKSPACE_ROOT/shared/tools"
mkdir -p "$WORKSPACE_ROOT/shared/wordlists"
mkdir -p "$WORKSPACE_ROOT/shared/templates"
mkdir -p "$WORKSPACE_ROOT/shared/datasets"

echo "[+] Creating Python virtual environment..."
python3 -m venv "$WORKSPACE_ROOT/.venv"
source "$WORKSPACE_ROOT/.venv/bin/activate"

echo "[+] Installing Python dependencies..."
pip install --quiet pip --upgrade
pip install --quiet \
    requests \
    beautifulsoup4 \
    lxml \
    pyyaml \
    jinja2 \
    markdown \
    termcolor

echo "[+] Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source $WORKSPACE_ROOT/.venv/bin/activate"
