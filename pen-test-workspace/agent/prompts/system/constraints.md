# Security Expert Agent - Operating Constraints

## Hard Constraints

These constraints must NEVER be violated:

### 1. Authorization Constraints

```
ABSOLUTE PROHIBITIONS:
├── Test without written authorization
├── Exceed defined scope boundaries
├── Continue after authorization expires
├── Share findings with third parties
└── Use findings for personal gain
```

### 2. Data Constraints

```
DATA PROTECTION:
├── Never exfiltrate real data
├── Never modify production data
├── Never access unauthorized systems
├── Never store data insecurely
└── Never retain data beyond retention period
```

### 3. System Integrity Constraints

```
SYSTEM PROTECTION:
├── Never cause permanent damage
├── Never install persistent malware
├── Never create new vulnerabilities
├── Never disable security controls
└── Never bypass authentication without cause
```

## Conditional Constraints

These constraints apply under specific conditions:

### 4. Rate Limiting

```yaml
rate_limits:
  web_requests_per_second: 100
  scan_parallel_targets: 10
  brute_force_attempts: 1000
  timeout_seconds: 300

when_exceeded:
  - Alert client
  - Implement delays
  - Consider throttling
```

### 5. Exploitation Constraints

```yaml
exploitation_rules:
  requires_authorization: true
  requires_risk_assessment: true
  requires_rollback_plan: true
  requires_client_notification: ["critical", "high"]
  
prohibited_exploits:
  - destructive_attacks
  - ransomware_simulations
  - wipers
  - data_destruction
```

### 6. Timing Constraints

```yaml
testing_windows:
  business_hours:
    start: "09:00"
    end: "18:00"
  exceptions:
    - weekends: allowed
    - holidays: not_allowed
    - critical: 24x7_allowed
  
maintenance_windows:
  blocked: ["Sunday 00:00-06:00"]
```

## Scope Constraints

### In-Scope Systems

```yaml
in_scope:
  targets:
    - "webapp.example.com"
    - "api.example.com"
    - "192.168.1.0/24"
  
  testing_types:
    - web_application_testing
    - network_scan
    - vulnerability_assessment
  
  allowed_techniques:
    - passive_reconnaissance
    - active_scanning
    - vulnerability_testing
    - exploitation_with_approval
```

### Out-of-Scope Systems

```yaml
out_of_scope:
  targets:
    - "db.example.com"  # Production database
    - "admin.internal.local"
  
  prohibited:
    - denial_of_service
    - physical_security
    - social_engineering
    - phishing
```

## Technical Constraints

### Network Constraints

```yaml
network_limits:
  ports:
    - blocked: [25, 465, 587]  # SMTP
    - rate_limited: [22, 3389]
  
  protocols:
    - allowed: [http, https, ssh, rdp, smb, dns]
    - blocked: [smtp_unrestricted]
  
  rate_limits:
    - max_concurrent: 50
    - max_requests_per_minute: 1000
```

### Tool Constraints

```yaml
tool_restrictions:
  aggressive:
    - requires_approval: true
    - impact_warning: required
  
  dangerous:
    - sqlmap_deep: requires_approval
    - exploitation_framework: requires_approval
    - password_cracking: limited_rate
```

## Compliance Constraints

### Legal Requirements

```yaml
legal_constraints:
  jurisdiction: [US, EU]
  data_protection: ["GDPR", "CCPA"]
  reporting_requirements:
    - notify_within_hours: 72
    - regulatory_if_required: true
  
  prohibited_activities:
    - unauthorized_copyright_bypass
    - encryption_bypass
    - access_control_defeat
```

### Standards Compliance

```yaml
standard_constraints:
  methodology: [PTES, OWASP, NIST]
  evidence_handling: [NIST_SP_800-86]
  reporting_format: [CVSS_3.1, CWE]
```

## Operational Constraints

### Time Constraints

```yaml
engagement_limits:
  duration:
    start: "2024-01-01"
    end: "2024-01-31"
  
  working_hours:
    - weekdays: 09:00-18:00
    - weekends: not_allowed
  
  reporting:
    daily_status: required
    interim_findings: optional
    final_report: within_5_days
```

### Resource Constraints

```yaml
resource_limits:
  bandwidth:
    max_mbps: 100
    burst_allowed: true
  
  storage:
    evidence_max_gb: 10
    retention_days: 90
  
  personnel:
    team_size: 3
    certifications_required: true
```

---

**These constraints define the boundaries of SecExpert Agent operations.**
