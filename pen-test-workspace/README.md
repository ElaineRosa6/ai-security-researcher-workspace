# Penetration Testing & Security Research Workspace

> An AI Agent-powered workspace for expert-level security testing and research operations.

## Overview

This workspace provides a comprehensive environment for conducting security assessments, penetration testing, and security research. It is designed to work with AI agents to automate and streamline security testing workflows.

## Directory Structure

```
pen-test-workspace/
├── agent/                    # AI Agent core system
│   ├── core/                 # Main agent components
│   ├── memory/               # Memory system (5-layer)
│   ├── knowledge/            # Knowledge graph
│   ├── workflow/             # Workflow engine
│   ├── quality/              # Quality control
│   ├── awareness/            # Self-awareness system
│   └── meta/                 # Meta monitoring system
│
├── red-team/                 # Red team operations
│   ├── web-security/         # Web application testing
│   ├── binary-security/      # Binary/PWN testing
│   ├── mobile-app/           # Mobile app security
│   ├── miniprogram/          # Mini-program security
│   ├── domain-pentest/       # Active Directory/Domain testing
│   ├── phishing/             # Phishing campaigns
│   ├── anonymity/            # Anonymity & proxy tools
│   └── infrastructure/       # Infrastructure testing
│
├── blue-team/                # Blue team operations
│   ├── incident-response/    # Incident response
│   ├── threat-intel/         # Threat intelligence
│   ├── monitoring/           # Security monitoring
│   └── hardening/            # System hardening
│
├── purple-team/              # Purple team operations
│   ├── attack-simulation/    # Attack simulation
│   ├── defense-validation/   # Defense validation
│   ├── forensics/            # Digital forensics
│   └── training/             # Training exercises
│
├── compliance/               # Compliance & recording
│   ├── recordings/           # Screen/terminal/network recordings
│   ├── logs/                 # Audit/command/session logs
│   ├── evidence/             # Evidence management
│   ├── policies/             # Compliance policies
│   └── checklists/           # Compliance checklists
│
├── shared/                   # Shared resources
│   ├── tools/                # Common tools
│   ├── wordlists/            # Wordlists and dictionaries
│   ├── templates/            # Report templates
│   ├── datasets/             # Test datasets
│   └── documentation/        # Shared documentation
│
├── ai-agent/                 # AI agent modules
│   ├── skills/               # Skill implementations
│   ├── harness/              # Harness framework
│   ├── prompts/              # Prompt templates
│   └── workflows/            # Workflow definitions
│
├── config/                   # Configuration files
│   ├── tools/                # Tool configurations
│   ├── environment/          # Environment configs
│   ├── proxy/                # Proxy/VPN configs
│   ├── compliance/           # Compliance configs
│   └── profiles/             # Testing profiles
│
├── output/                   # Output directory
│   ├── reports/              # Generated reports
│   ├── logs/                 # Execution logs
│   ├── artifacts/            # Testing artifacts
│   └── screenshots/          # Screenshots
│
└── workspace-data/           # Workspace data
    ├── sessions/             # Session data
    ├── cache/                # Cache files
    └── temp/                 # Temporary files
```

## Quick Start

### 1. Environment Setup

```bash
# Copy environment configuration
cp .env.example .env

# Edit .env with your API keys and settings
nano .env

# Run setup script
bash scripts/setup_env.sh
```

### 2. Install Tools

```bash
# Install security tools (requires root privileges)
sudo bash scripts/install_tools.sh
```

### 3. Activate Environment

```bash
source .venv/bin/activate
```

### 4. Run Agent

```bash
# Start the AI agent
python agent/start.py
```

## Workflows

Available workflows are defined in `ai-agent/workflows/`:

- `web_pentest.yaml` - Web application penetration testing
- `incident_response.yaml` - Security incident response
- `full_pentest_session.yaml` - Complete pentest with compliance
- `domain_pentest.yaml` - Active Directory testing
- `forensics.yaml` - Digital forensics analysis
- `anonymity_test.yaml` - Anonymity testing workflow

## Configuration

All configuration files are located in the `config/` directory:

- `config/agent/` - Agent core and memory settings
- `config/compliance/` - Recording and evidence management
- `config/proxy/` - Tor, proxy chains, and VPN settings
- `config/tools/` - Security tool configurations
- `config/profiles/` - Testing profile templates

## Compliance

This workspace enforces compliance requirements:

- Mandatory screen and terminal recording
- Evidence chain of custody tracking
- File integrity verification (SHA-256)
- Digital signature support
- Complete audit logging

## Security

- Never commit `.env` files with actual credentials
- Use `.env.example` as a template
- All evidence should be hashed and signed
- Maintain proper authorization before testing

## Requirements

- Python 3.9+
- Docker (optional, for tool isolation)
- Root access (for tool installation)
- Network access (for updates and API calls)

## License

[Appropriate License]

## Disclaimer

This workspace is intended for authorized security testing, research, and educational purposes only. Users must:
- Obtain explicit written authorization before testing
- Comply with all applicable laws and regulations
- Minimize potential damage
- Report all discovered vulnerabilities promptly
