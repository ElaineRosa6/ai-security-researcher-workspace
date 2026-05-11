# Task Planning Prompt

## Purpose

Guide systematic planning for security testing engagements.

## Planning Framework

### 1. Requirement Analysis

```yaml
requirement_breakdown:
  inputs:
    - user_requirement
    - target_scope
    - constraints
  
  analysis_steps:
    1: Extract key objectives
    2: Identify target types
    3: Determine testing depth
    4: Map to methodology
    5: Identify dependencies
  
  outputs:
    - requirement_summary
    - target_list
    - constraints_list
```

### 2. Target Profiling

```yaml
target_profile:
  web_apps:
    - url_analysis
    - technology_detection
    - endpoint_mapping
    - authentication_analysis
  
  networks:
    - range_definition
    - topology_mapping
    - service_identification
    - segmentation_check
  
  apis:
    - endpoint_discovery
    - auth_method_analysis
    - data_flow_mapping
```

### 3. Resource Planning

```yaml
resource_allocation:
  time:
    - reconnaissance: 20%
    - scanning: 25%
    - exploitation: 30%
    - reporting: 25%
  
  tools:
    - reconnaissance: [nmap, subfinder, amass]
    - scanning: [nuclei, nmap, custom_scans]
    - exploitation: [burp, sqlmap, custom_exploits]
  
  personnel:
    - primary: main_tester
    - backup: review_specialist
```

## Phase Planning

### Phase 1: Reconnaissance

```yaml
reconnaissance_plan:
  passive:
    - whois_lookups
    - dns_enumeration
    - certificate_analysis
    - search_engine_discovery
    - shodan_censys_query
  
  active:
    - subdomain_enumeration
    - web_crawling
    - technology_fingerprinting
    - email_harvesting
  
  tools:
    - nmap, subfinder, amass
    - theHarvester, recon-ng
    - shodan, censys
  
  duration: typically 1-2 hours
  deliverable: target_profile
```

### Phase 2: Scanning

```yaml
scanning_plan:
  network_scan:
    - port_scan: full_or_targeted
    - service_detection: version_and_banner
    - os_fingerprinting: accurate
    - vulnerability_scan: template_based
  
  web_scan:
    - crawling: comprehensive
    - technology_detection: detailed
    - vulnerability_scan: automated_plus_manual
  
  duration: typically 2-4 hours
  deliverable: service_and_vulnerability_list
```

### Phase 3: Vulnerability Assessment

```yaml
vulnerability_assessment:
  automated:
    - nuclei_templates
    - nmap_scripts
    - burp_scanner
  
  manual:
    - injection_testing
    - auth_testing
    - business_logic
    - configuration_issues
  
  validation:
    - confirm_all_findings
    - assess_exploitability
    - determine_impact
  
  duration: typically 4-8 hours
  deliverable: validated_findings
```

### Phase 4: Exploitation

```yaml
exploitation_plan:
  preparation:
    - confirm_exploit_authorization
    - prepare_payloads
    - setup_environment
    - prepare_cleanup
  
  execution:
    - low_risk_first
    - document_each_step
    - monitor_impact
    - capture_evidence
  
  post_exploitation:
    - assess_access_level
    - document_impact
    - prepare_poc
    - cleanup_artifacts
  
  duration: typically 4-8 hours
  deliverable: exploitation_evidence
```

### Phase 5: Reporting

```yaml
reporting_plan:
  daily_updates:
    - status_summary
    - key_findings
    - blockers
  
  interim_report:
    - critical_findings
    - immediate_actions
  
  final_report:
    - executive_summary
    - technical_findings
    - remediation_plan
  
  duration: typically 2-4 hours
  deliverable: comprehensive_report
```

## Planning Template

```markdown
## Engagement Plan

### Overview
- **Target**: [Target(s)]
- **Type**: [Test Type]
- **Duration**: [Estimated Time]
- **Tester**: [Assigned Personnel]

### Phase Breakdown

#### Phase 1: Reconnaissance
- **Duration**: [Time]
- **Objectives**: [Goals]
- **Tools**: [List]
- **Deliverables**: [Expected Output]

#### Phase 2: Scanning
- **Duration**: [Time]
- **Objectives**: [Goals]
- **Tools**: [List]
- **Deliverables**: [Expected Output]

#### Phase 3: Vulnerability Assessment
- **Duration**: [Time]
- **Objectives**: [Goals]
- **Tools**: [List]
- **Deliverables**: [Expected Output]

#### Phase 4: Exploitation
- **Duration**: [Time]
- **Objectives**: [Goals]
- **Tools**: [List]
- **Deliverables**: [Expected Output]

#### Phase 5: Reporting
- **Duration**: [Time]
- **Objectives**: [Goals]
- **Deliverables**: [Expected Output]

### Risk Assessment
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

### Contingency Plans
- [What if X]: [Then do Y]

### Communication Plan
- Daily standup: [Time]
- Escalation: [Contact]
- Client updates: [Frequency]
```

## Decision Points

### When Planning

```
Check: Do I have complete scope?
  → No: Request clarification

Check: Do I understand constraints?
  → No: Document unknowns

Check: Do I have required tools?
  → No: Request installation

Check: Is timeline realistic?
  → No: Negotiate scope or timeline
```

### During Execution

```
Check: Am I on track?
  → No: Adjust priorities

Check: Did I find unexpected issues?
  → Yes: Assess and report

Check: Should I escalate?
  → Yes: Follow escalation path
```

---

**Use this planning framework for systematic, thorough security assessments.**
