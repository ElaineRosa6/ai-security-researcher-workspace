# Nmap Tool Usage Prompt

## Overview

Nmap ("Network Mapper") is the industry-standard tool for network discovery and security auditing.

## Basic Usage

### Syntax

```bash
nmap [Scan Type] [Options] {target}
```

### Common Scan Types

| Flag | Type | Description |
|------|------|-------------|
| `-sS` | SYN scan | Stealth scan (requires root) |
| `-sT` | TCP scan | Connect scan (no root) |
| `-sU` | UDP scan | UDP port scan |
| `-sV` | Version | Detect service versions |
| `-sC` | Script | Run default NSE scripts |
| `-O` | OS | Operating system detection |

### Quick Reference

**Single host scan:**
```bash
nmap 192.168.1.1
```

**Network scan:**
```bash
nmap 192.168.1.0/24
```

**Full port scan with scripts:**
```bash
nmap -sV -sC -p- 192.168.1.1
```

**Fast scan (top 100 ports):**
```bash
nmap -F 192.168.1.1
```

## Common Use Cases

### 1. Basic Service Discovery

```bash
# TCP SYN scan, version detection, default scripts
nmap -sS -sV -sC 192.168.1.1

# Output
# PORT     STATE  SERVICE  VERSION
# 22/tcp   open   ssh      OpenSSH 7.4
# 80/tcp   open   http     Apache 2.4.6
# 443/tcp  open   ssl      nginx 1.12.2
```

### 2. UDP Port Scan

```bash
# UDP scan (slow but thorough)
nmap -sU -p 53,67,123,161 192.168.1.1

# Note: UDP scans are slower than TCP
```

### 3. Aggressive Scan

```bash
# Enable OS detection, version detection, script scanning, traceroute
nmap -A 192.168.1.1

# Output includes:
# - OS detection
# - Traceroute
# - Service versions
# - Script results
```

### 4. Targeted Script Scan

```bash
# Run specific NSE categories
nmap --script vuln,exploit 192.168.1.1

# Run specific script
nmap --script http-enum 192.168.1.1

# Multiple scripts
nmap --script "http-* and not http-brute" 192.168.1.1
```

## Script Categories

| Category | Description | Examples |
|----------|-------------|----------|
| `auth` | Authentication tests | anonymous-ftp, imap-brute |
| `broadcast` | Broadcast discovery | broadcast-mssql-discover |
| `brute` | Brute force attacks | http-brute, snmp-brute |
| `default` | Default scripts | ssl-cert, http-title |
| `discovery` | Service discovery | snmp-info, afp-ls |
| `dos` | Denial of service | sip-methods-dis flood |
| `exploit` | Exploit vulnerabilities | smb-vuln-ms17-010 |
| `external` | External sources | whois |
| `fuzzer` | Fuzzing | http-form-fuzzer |
| `intrusive` | Potentially intrusive | http-aspnet-debug |
| `malware` | Malware detection | auth-spoof |
| `safe` | Safe tests | http-headers |
| `version` | Version detection | ftp-anon |
| `vuln` | Vulnerability detection | smb-vuln-ms08-067 |

## Output Formats

| Flag | Format | Use |
|------|--------|-----|
| `-oN` | Normal | Human readable |
| `-oX` | XML | Parsing, automation |
| `-oG` | Grepable | Text processing |
| `-oJ` | JSON | Modern parsing |
| `-oA` | All | All formats |

```bash
# Save in multiple formats
nmap -sV -oA scan_results 192.168.1.1
```

## Timing Templates

| Template | Time | Stealth | Completeness |
|----------|------|---------|--------------|
| `-T0` | Paranoid | Highest | Full |
| `-T1` | Sneaky | High | Full |
| `-T2` | Polite | Medium | Full |
| `-T3` | Normal | Low | Full |
| `-T4` | Aggressive | Lower | Fast |
| `-T5` | Insane | None | Fastest |

## Decoys and Spoofing

```bash
# Decoy scan (hide your IP among decoys)
nmap -D decoy1,decoy2,ME 192.168.1.1

# Source IP spoof (requires privileges)
nmap -S 10.0.0.1 192.168.1.1

# Source port (bypass firewall rules)
nmap -g 53 192.168.1.1
```

## Specific Port Scans

```bash
# Top 10 ports
nmap --top-ports 10 192.168.1.1

# Specific ports
nmap -p 22,80,443,3389 192.168.1.1

# Port ranges
nmap -p 1-1000 192.168.1.1

# All ports
nmap -p- 192.168.1.1
```

## Useful NSE Scripts

### Web Vulnerability Scanning

```bash
# HTTP enumeration
nmap --script http-enum 192.168.1.1

# HTTP methods
nmap --script http-methods 192.168.1.1

# Directory discovery
nmap --script http-dir-brute 192.168.1.1

# XSS detection
nmap --script http-stored-xss 192.168.1.1
```

### Database Scanning

```bash
# MySQL
nmap --script mysql-info,mysql-enum 192.168.1.1

# MSSQL
nmap --script ms-sql-info,ms-sql-empty-password 192.168.1.1

# MongoDB
nmap --script mongodb-info 192.168.1.1
```

### SMB Scanning

```bash
# SMB enumeration
nmap --script smb-enum-shares,smb-enum-users 192.168.1.1

# SMB vulnerabilities
nmap --script smb-vuln-* 192.168.1.1
```

### SSL/TLS Analysis

```bash
# SSL certificate info
nmap --script ssl-cert 192.168.1.1

# SSL vulnerabilities
nmap --script ssl-enum-ciphers,ssl-vuln-* 192.168.1.1

# Heartbleed check
nmap --script ssl-heartbleed 192.168.1.1
```

## One-Liners for Quick Recon

```bash
# Quick live hosts
nmap -sn 192.168.1.0/24

# Top 20 ports
nmap --top-ports 20 192.168.1.1

# Detect firewall
nmap --script firewalk 192.168.1.1

# DNS enumeration
nmap --script dns-zone-transfer,dns-brute 192.168.1.1
```

## Interpreting Results

### State Meanings

| State | Meaning |
|-------|---------|
| `open` | Service accepting connections |
| `closed` | Port accessible, no service |
| `filtered` | Firewall blocking detection |
| `unfiltered` | Port accessible, state unclear |
| `open|filtered` | Open or filtered |

### Risk Assessment

```
High Priority Ports to Investigate:
- 21 (FTP) - anonymous access, upload
- 22 (SSH) - brute force, key theft
- 23 (Telnet) - plaintext
- 25 (SMTP) - relay, enumeration
- 110 (POP3) - plaintext access
- 139/445 (SMB) - code execution
- 1433 (MSSQL) - SA access, xp_cmdshell
- 3306 (MySQL) - root access
- 3389 (RDP) - remote access
- 5432 (PostgreSQL) - command execution
```

## Best Practices

1. **Start Non-Invasive**: Begin with `-sn` (ping sweep) to discover hosts
2. **Use Timing Appropriately**: `-T4` for CTF, `-T2` for production
3. **Log Everything**: Always use `-oA` for complete logging
4. **Follow Scope**: Only scan authorized targets
5. **Be Patient with UDP**: UDP scans take time

---

**Use this guide for effective network reconnaissance with Nmap.**
