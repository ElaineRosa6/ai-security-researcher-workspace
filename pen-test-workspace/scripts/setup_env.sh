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
mkdir -p "$WORKSPACE_ROOT/workspace-data/sessions"
mkdir -p "$WORKSPACE_ROOT/workspace-data/cache"
mkdir -p "$WORKSPACE_ROOT/workspace-data/temp"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/vulnerabilities"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/techniques"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/best_practices"
mkdir -p "$WORKSPACE_ROOT/workspace-data/knowledge-base/learned_lessons"

mkdir -p "$WORKSPACE_ROOT/shared/tools"
mkdir -p "$WORKSPACE_ROOT/shared/wordlists"
mkdir -p "$WORKSPACE_ROOT/shared/templates"
mkdir -p "$WORKSPACE_ROOT/shared/datasets"
mkdir -p "$WORKSPACE_ROOT/shared/documentation"

# Red team directories
mkdir -p "$WORKSPACE_ROOT/red-team/web-security/{tools,exploits,payloads,wordlists,templates}"
mkdir -p "$WORKSPACE_ROOT/red-team/binary-security/{pwn,reverse-engineering,fuzzing,debugger}"
mkdir -p "$WORKSPACE_ROOT/red-team/mobile-app/{android,ios,frida-scripts}"
mkdir -p "$WORKSPACE_ROOT/red-team/miniprogram/{unpack,audit,hooks}"
mkdir -p "$WORKSPACE_ROOT/red-team/domain-pentest/{enumeration,lateral-movement,privilege-escalation,persistence}"
mkdir -p "$WORKSPACE_ROOT/red-team/phishing/{templates,payload-generators,delivery}"
mkdir -p "$WORKSPACE_ROOT/red-team/anonymity/{proxies,chains,tor,i2p,vpn}"
mkdir -p "$WORKSPACE_ROOT/red-team/infrastructure/{cloud,network,wireless}"

# Blue team directories
mkdir -p "$WORKSPACE_ROOT/blue-team/incident-response/{playbooks,forensics,malware-analysis,reporting}"
mkdir -p "$WORKSPACE_ROOT/blue-team/threat-intel/{feeds,analysis,indicators}"
mkdir -p "$WORKSPACE_ROOT/blue-team/monitoring/{logs,alerts,dashboards}"
mkdir -p "$WORKSPACE_ROOT/blue-team/hardening/{benchmarks,checklists,scripts}"

# Purple team directories
mkdir -p "$WORKSPACE_ROOT/purple-team/attack-simulation"
mkdir -p "$WORKSPACE_ROOT/purple-team/defense-validation"
mkdir -p "$WORKSPACE_ROOT/purple-team/forensics/{disk-forensics,memory-forensics,network-forensics,timeline}"
mkdir -p "$WORKSPACE_ROOT/purple-team/training"

# Config directories
mkdir -p "$WORKSPACE_ROOT/config/tools"
mkdir -p "$WORKSPACE_ROOT/config/environment"
mkdir -p "$WORKSPACE_ROOT/config/proxy"
mkdir -p "$WORKSPACE_ROOT/config/compliance"
mkdir -p "$WORKSPACE_ROOT/config/profiles"

# AI agent directories
mkdir -p "$WORKSPACE_ROOT/ai-agent/skills/{red_team,blue_team,purple_team,compliance,general}"
mkdir -p "$WORKSPACE_ROOT/ai-agent/harness"
mkdir -p "$WORKSPACE_ROOT/ai-agent/prompts"
mkdir -p "$WORKSPACE_ROOT/ai-agent/workflows"

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
