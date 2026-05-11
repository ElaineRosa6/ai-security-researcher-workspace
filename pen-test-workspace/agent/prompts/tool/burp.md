# Burp Suite Tool Usage Prompt

## Overview

Burp Suite is the industry-standard web vulnerability testing platform by PortSwigger.

## Installation and Setup

### Quick Start

```bash
# Download from PortSwigger
https://portswigger.net/burp/releases

# Community Edition (limited)
# Professional Edition (full features)

# Start Burp Suite
java -jar burpsuite_pro.jar
```

### Proxy Configuration

```yaml
proxy_settings:
  listen_port: 8080
  bind_to_address: 127.0.0.1
  redirect_to_remote: false
  
  interception:
    mode: enabled  # or disabled for passive
    rules:
      - match_conditions
      - modify_requests
      - forward_drop
```

## Core Components

### 1. Proxy Tab

**Purpose**: Intercept and modify HTTP/S traffic

#### Intercept Controls

```
Forward     → Send request to server
Drop        → Discard request
Intercept On/Off → Toggle interception
Action      → Send to other tools
```

#### Options

```yaml
intercept_rules:
  automatically_fix:
    - content-type mismatches
    - invalid content lengths
    - SSL/PCT issues
  
  scope_rules:
    include_in_scope:
      - https://app.example.com/.*
    exclude_from_scope:
      - https://app.example.com/logout
```

### 2. Target Tab

**Purpose**: Define scope and view site map

#### Scope Configuration

```yaml
scope_definition:
  advanced_mode: true
  include_urls:
    - "^https://app\\.example\\.com/.*"
    - "^http://192\\.168\\.1\\..*"
  exclude_urls:
    - ".*\\.css$"
    - ".*\\.js$"
    - ".*\\.png$"
```

#### Site Map

```
Structure:
  ├── https://app.example.com
  │   ├── /login
  │   ├── /api/v1/users
  │   ├── /admin
  │   └── /static/*
```

### 3. Spider Tab

**Purpose**: Automatically discover content

```yaml
spider_settings:
  crawl_links: true
  parse_html: true
  submit_forms: true
  detect_application_walls: true
  
  form_submission:
    - fill_defaults: true
    - username: test@test.com
    - password: testpassword
  
  scope_control:
    - spider_only_in_scope: true
    - check_robots_txt: true
    - check_sitemap_html: true
```

### 4. Scanner Tab

**Purpose**: Automated vulnerability scanning

#### Scan Types

```yaml
scan_types:
  active:
    - sql_injection
    - cross_site_scripting
    - command_injection
    - path_traversal
  
  passive:
    - information_disclosure
    - missing_secure_headers
    - cookie_attributes
    - cross_domain_references
```

#### Scan Configuration

```yaml
scan_configuration:
  crawl_options:
    - link_depth: 5
    - page_count: 1000
    - form_submission: true
  
  audit_options:
    - insertion_points: standard
    - request_count_per_minute: 100
    - follow_redirects: true
  
  resource_pool:
    - threads: 5
    - delay_milliseconds: 100
```

### 5. Intruder Tab

**Purpose**: Custom automated attacks

#### Attack Types

| Position | Payload | Use Case |
|----------|---------|----------|
| Sniper | Single list | Simple fuzzing |
| Battering Ram | Single list | Multiple positions same value |
| Pitchfork | Multiple lists | Pairwise testing |
| Cluster Bomb | Multiple lists | Combinatorial |

#### Configuration Example

```yaml
intruder_attack:
  target:
    url: "https://app.example.com/login"
    method: POST
  
  positions:
    - §username§
    - §password§
  
  payloads:
    username:
      type: simple_list
      values:
        - admin
        - test
        - user
    
    password:
      type: simple_list
      values:
        - password
        - admin
        - 123456
  
  processing:
    - add_prefix: ""
    - add_suffix: ""
    - case_conversion: none
```

### 6. Repeater Tab

**Purpose**: Manual testing and request crafting

```yaml
repeater_usage:
  request_tabs:
    - name: SQLi Test
      method: POST
      url: /api/login
      body: username=test&password=test
    
    - name: XSS Test
      method: GET
      url: /search?q=<script>
  
  options:
    follow_redirects: false
    use_cookie_jar: true
    update_content_length: true
```

### 7. Decoder Tab

**Purpose**: Encode/decode data

```yaml
encoding_types:
  - URL encoding
  - HTML encoding
  - Base64
  - Hex
  - Unicode
  - GZIP
  
usage:
  - decode_jwt_tokens
  - encode_payloads
  - decode_obfuscated_data
```

### 8. Comparer Tab

**Purpose**: Compare responses/differences

```yaml
comparison_modes:
  - word_comparison
  - byte_comparison
  
usage:
  - compare_responses
    before_exploit
    after_exploit
  - identify_differences
  - validate_fixes
```

## Common Testing Workflows

### SQL Injection Testing

```yaml
workflow:
  1_reconnaissance:
    - browse_app_normally
    - identify_reflection_points
    - map_data_entry_points
  
  2_testing:
    repeater:
      url: /api/user?id=§§
      payloads:
        - "'"
        - "' OR '1'='1"
        - "'; DROP TABLE users--"
        - "1' AND 1=1--"
  
  3_validation:
    - error_based: look_for_db_errors
    - boolean_based: true_vs_false
    - time_based: sleep_commands
```

### XSS Testing

```yaml
workflow:
  1_reflection_analysis:
    - find_reflection_points
    - identify_context
    - determine_filtering
  
  2_payload_testing:
    basic:
      - "<script>alert(1)</script>"
      - "<img src=x onerror=alert(1)>"
      - "<svg onload=alert(1)>"
    
    bypass:
      - "<scr<script>ipt>"
      - "javascript:alert(1)"
      - "<body onload=alert(1)>"
  
  3_exploitation:
    - session_hijacking
    - credential_theft
    -蠕虫_propagation
```

### Authentication Testing

```yaml
workflow:
  1_auth_mapping:
    - identify_login_endpoints
    - map_password_reset_flows
    - find_mfa_bypasses
  
  2_weakness_testing:
    - default_credentials
    - weak_password_policy
    - username_enumeration
    - brute_force_protection
  
  3_session_testing:
    - session_prediction
    - session_fixation
    - session_timeout
    - logout_functionality
```

## Extender (Extensions)

### Popular Extensions

| Extension | Purpose |
|-----------|---------|
| BurpKit | Dynamic analysis |
| JSON Beautifier | JSON formatting |
| Retire.js | JavaScript scanning |
| Active Scan++ | Enhanced scanning |
| Autorize | Access control testing |

### Installing Extensions

```yaml
extensions:
  java:
    - download: .jar file
    - install: Extender → Add → Select file
  
  python:
    - install_jython: required
    - download: .jar or .py
    - install: same as java
```

## API Testing

### REST API Testing

```yaml
api_testing:
  base_url: "https://api.example.com/v1"
  
  authentication:
    - api_key: header
    - bearer_token: header
    - jwt: authorization
  
  common_tests:
    - endpoint_discovery
    - method_testing
    - parameter_fuzzing
    - auth_bypass
    - rate_limiting
```

## Command Line Usage

### Burp Scanner API

```bash
# Start headless scanner
java -jar burpsuite_pro.jar \
  --project-file=project.burp \
  --headless \
  --scan-url="https://app.example.com"

# Scan with config
--config-file=config.json
```

---

**Use Burp Suite for comprehensive web application security testing.**
