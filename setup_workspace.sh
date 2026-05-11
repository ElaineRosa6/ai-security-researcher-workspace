#!/bin/bash
set -e

PROJECT_ROOT="/workspace/pen-test-workspace"

echo "[*] Creating project directory structure..."

mkdir -p "$PROJECT_ROOT"

mkdir -p "$PROJECT_ROOT/agent/core"
mkdir -p "$PROJECT_ROOT/agent/memory"
mkdir -p "$PROJECT_ROOT/agent/knowledge/vulnerability_db"
mkdir -p "$PROJECT_ROOT/agent/knowledge/attack_patterns"
mkdir -p "$PROJECT_ROOT/agent/knowledge/tool_knowledge"
mkdir -p "$PROJECT_ROOT/agent/knowledge/methodology"
mkdir -p "$PROJECT_ROOT/agent/workflow/definitions"
mkdir -p "$PROJECT_ROOT/agent/quality"
mkdir -p "$PROJECT_ROOT/agent/awareness"
mkdir -p "$PROJECT_ROOT/agent/prompts/system"
mkdir -p "$PROJECT_ROOT/agent/prompts/task"
mkdir -p "$PROJECT_ROOT/agent/prompts/tool"
mkdir -p "$PROJECT_ROOT/agent/prompts/reasoning"
mkdir -p "$PROJECT_ROOT/agent/prompts/quality"
mkdir -p "$PROJECT_ROOT/agent/meta"

mkdir -p "$PROJECT_ROOT/red-team/web-security/{tools,exploits,payloads,wordlists,templates}"
mkdir -p "$PROJECT_ROOT/red-team/binary-security/{pwn,reverse-engineering,fuzzing,debugger}"
mkdir -p "$PROJECT_ROOT/red-team/mobile-app/{android,ios,frida-scripts}"
mkdir -p "$PROJECT_ROOT/red-team/miniprogram/{unpack,audit,hooks}"
mkdir -p "$PROJECT_ROOT/red-team/domain-pentest/{enumeration,lateral-movement,privilege-escalation,persistence}"
mkdir -p "$PROJECT_ROOT/red-team/phishing/{templates,payload-generators,delivery}"
mkdir -p "$PROJECT_ROOT/red-team/anonymity/{proxies,chains,tor,i2p,vpn}"
mkdir -p "$PROJECT_ROOT/red-team/infrastructure/{cloud,network,wireless}"

mkdir -p "$PROJECT_ROOT/blue-team/incident-response/{playbooks,forensics,malware-analysis,reporting}"
mkdir -p "$PROJECT_ROOT/blue-team/threat-intel/{feeds,analysis,indicators}"
mkdir -p "$PROJECT_ROOT/blue-team/monitoring/{logs,alerts,dashboards}"
mkdir -p "$PROJECT_ROOT/blue-team/hardening/{benchmarks,checklists,scripts}"

mkdir -p "$PROJECT_ROOT/purple-team/{attack-simulation,defense-validation,training}"
mkdir -p "$PROJECT_ROOT/purple-team/forensics/{disk-forensics,memory-forensics,network-forensics,timeline}"

mkdir -p "$PROJECT_ROOT/compliance/recordings/{screen,terminal,network}"
mkdir -p "$PROJECT_ROOT/compliance/logs/{audit,command,session}"
mkdir -p "$PROJECT_ROOT/compliance/evidence/{chain-of-custody,hashes,signatures}"
mkdir -p "$PROJECT_ROOT/compliance/{policies,checklists}"

mkdir -p "$PROJECT_ROOT/shared/{tools,wordlists,templates,datasets,documentation}"

mkdir -p "$PROJECT_ROOT/ai-agent/skills/{red_team,blue_team,purple_team,compliance,general}"
mkdir -p "$PROJECT_ROOT/ai-agent/harness"
mkdir -p "$PROJECT_ROOT/ai-agent/prompts"
mkdir -p "$PROJECT_ROOT/ai-agent/workflows"

mkdir -p "$PROJECT_ROOT/workspace-data/current-session"
mkdir -p "$PROJECT_ROOT/workspace-data/sessions-history"
mkdir -p "$PROJECT_ROOT/workspace-data/knowledge-base/{vulnerabilities,techniques,best_practices,learned_lessons}"

mkdir -p "$PROJECT_ROOT/config/{agent,tools,environment,proxy,compliance,profiles}"
mkdir -p "$PROJECT_ROOT/output/{reports,logs,artifacts,screenshots}"
mkdir -p "$PROJECT_ROOT/docs"

echo "[+] Directory structure created successfully!"
echo "[*] Creating __init__.py files for Python packages..."

find "$PROJECT_ROOT" -type d -exec touch {}/__init__.py \;

echo "[+] Setup complete!"
