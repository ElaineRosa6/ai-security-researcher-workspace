# Security Testing Methodology

## Overview

This methodology defines the systematic approach for conducting security assessments. It integrates multiple industry standards into a cohesive framework.

## Phase 1: Pre-Engagement

### 1.1 Authorization Verification

```
Requirements:
- Written scope document
- Defined target systems
- Time constraints
- Contact information
- Emergency contacts
```

### 1.2 Scope Definition

```yaml
scope:
  web_apps:
    - "https://app.example.com"
    - "https://api.example.com"
  network:
    - "192.168.1.0/24"
  excluded:
    - "192.168.1.100"  # Production database
```

### 1.3 Rules of Engagement

| Parameter | Value |
|-----------|-------|
| Testing Hours | Business hours (9AM-6PM) |
| Max Requests/sec | 100 |
| Dangerous Tests | Requires approval |
| Data Handling | Confidential |
| Reporting | Encrypted only |

## Phase 2: Intelligence Gathering

### 2.1 Passive Reconnaissance

**Objective**: Gather information without touching target

**Tools**:
- WHOIS lookups
- DNS enumeration
- Subdomain discovery
- Certificate transparency logs
- Search engine discovery (Shodan, Censys)

**Output**: Target list, technology fingerprinting

### 2.2 Active Reconnaissance

**Objective**: Discover live hosts and services

**Tools**:
- nmap for port scanning
- Service version detection
- OS fingerprinting
- traceroute

**Commands**:
```bash
nmap -sV -sC -O -p- <target>
```

### 2.3 OSINT Collection

**Categories**:
- Email addresses
- Employee names
- Technology stack
- Business relationships
- Historical vulnerabilities

## Phase 3: Vulnerability Analysis

### 3.1 Vulnerability Discovery

**Approaches**:

1. **Automated Scanning**
   - Nuclei templates
   - Nmap scripts
   - Burp Scanner

2. **Manual Testing**
   - Fuzzing
   - Code review
   - Configuration analysis

### 3.2 Vulnerability Categorization

| Category | Examples | Testing Method |
|----------|----------|----------------|
| Injection | SQLi, XSS, Command | Manual + Automated |
| Authentication | Bypass, Brute force | Manual |
| Authorization | IDOR, Privilege | Manual |
| Security Config | CORS, CSP, Headers | Automated |
| Cryptographic | Weak encryption | Manual |

### 3.3 False Positive Management

**Verification Steps**:
1. Confirm with second tool
2. Manual reproduction
3. Check business impact
4. Document evidence

## Phase 4: Exploitation

### 4.1 Exploitation Criteria

Before exploiting:
- [ ] Vulnerability is confirmed
- [ ] Exploit is reliable
- [ ] Impact is understood
- [ ] Authorization exists
- [ ] Safety measures in place

### 4.2 Exploitation Techniques

**Web Vulnerabilities**:
- SQL injection with sqlmap
- XSS with beef/xssf
- SSRF via collaborator

**Network Vulnerabilities**:
- SMB exploits (EternalBlue)
- SSH brute force
- LDAP injection

**Binary Exploitation**:
- Buffer overflow
- ROP chain building
- Format string attacks

### 4.3 Post-Exploitation

**Objectives**:
- Demonstrate real impact
- Access sensitive data
- Show lateral movement
- Document persistence

**Rules**:
- Don't exfiltrate real data
- Minimize system changes
- Document all actions

## Phase 5: Reporting

### 5.1 Report Structure

```markdown
# Executive Summary
- Engagement overview
- Key findings
- Business risk
- Recommendations

# Technical Findings
- Detailed vulnerabilities
- Proof of concept
- Remediation steps

# Appendices
- Raw evidence
- Tool output
- Methodology details
```

### 5.2 Finding Severity

| Rating | CVSS | Description |
|--------|------|-------------|
| Critical | 9.0-10 | Immediate action required |
| High | 7.0-8.9 | Urgent remediation |
| Medium | 4.0-6.9 | Scheduled remediation |
| Low | 0.1-3.9 | Minor issues |
| Info | 0.0 | No vulnerability |

### 5.3 Remediation Prioritization

1. **Immediate** (Critical): < 24 hours
2. **Short-term** (High): < 7 days
3. **Medium-term** (Medium): < 30 days
4. **Long-term** (Low): < 90 days

## Phase 6: Cleanup

### 6.1 Post-Engagement Tasks

- [ ] Remove all exploits
- [ ] Restore modified files
- [ ] Clear logs (if possible)
- [ ] Archive evidence
- [ ] Submit final report

### 6.2 Evidence Handling

```python
evidence_handling:
  retention_days: 90
  encryption: AES-256
  access_control: Need-to-know
  disposal: Secure delete
```

## Quality Assurance

### Pre-Report Review

- [ ] All findings verified
- [ ] Evidence is complete
- [ ] Severity is accurate
- [ ] Recommendations are actionable
- [ ] No false positives included

### Report Validation

- [ ] Technical accuracy checked
- [ ] Business impact validated
- [ ] Peer review completed
- [ ] Client feedback incorporated

---

**This methodology ensures consistent, thorough, and professional security assessments.**
