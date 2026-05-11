# Validation Prompt

## Purpose

Guide systematic validation of security findings.

## Validation Framework

### 1. Finding Classification

```yaml
finding_types:
  confirmed:
    - evidence_direct
    - reproduction_verified
    - impact_documented
  
  potential:
    - evidence_indirect
    - partial_reproduction
    - requires_additional_testing
  
  false_positive:
    - evidence_contradicted
    - reproduction_failed
    - legitimate_behavior
```

### 2. Validation Checklist

```yaml
validation_checklist:
  technical_validation:
    - [ ] Vulnerability confirmed
    - [ ] Reproduction successful
    - [ ] Root cause identified
    - [ ] Attack vector valid
  
  evidence_validation:
    - [ ] Screenshots captured
    - [ ] Commands logged
    - [ ] Timestamps recorded
    - [ ] Hashes generated
  
  impact_validation:
    - [ ] Business impact assessed
    - [ ] Data exposure evaluated
    - [ ] System compromise scope
    - [ ] Attack chain documented
  
  remediation_validation:
    - [ ] Fix is technically sound
    - [ ] Fix is practically implementable
    - [ ] Alternative fixes considered
    - [ ] Priority correctly assigned
```

## Technical Validation

### SQL Injection Validation

```yaml
sqli_validation:
  detection_methods:
    error_based:
      - payload: "'"
      - expected: database_error
      
    boolean_based:
      - payload_true: "1' AND '1'='1"
      - payload_false: "1' AND '1'='2"
      - expected: different_response
      
    time_based:
      - payload: "1' AND SLEEP(5)--"
      - expected: delayed_response
  
  exploitation_potential:
    - data_extraction_possible: true|false
    - privilege_escalation: yes|no
    - os_execution: yes|no
  
  confirmation_steps:
    1: inject_single_quote
    2: observe_error_response
    3: inject_boolean_condition
    4: verify_true_vs_false
    5: document_findings
```

### XSS Validation

```yaml
xss_validation:
  reflection_analysis:
    - find_reflection_point
    - identify_context
    - determine_encoding
  
  context_testing:
    html_context:
      - payload: "<script>alert(1)</script>"
      - expected: script_execution
    
    attribute_context:
      - payload: "\" onmouseover=\"alert(1)\""
      - expected: event_handler_injection
    
    javascript_context:
      - payload: "';alert(1);//"
      - expected: script_injection
  
  filter_bypass:
    - case_bypass: "<ScRiPt>"
    - encoding_bypass: "%3cscript%3e"
    - mutation_testing: check_filter_limits
  
  impact_assessment:
    session_hijacking: yes|no
    credential_theft: yes|no
   蠕虫_propagation: yes|no
```

### Authentication Bypass Validation

```yaml
auth_bypass_validation:
  bypass_techniques:
    - direct_page_access
    - parameter_modification
    - session_hijacking
    - credential_stuffing
  
  test_cases:
    test_1:
      description: "Access admin without auth"
      steps:
        - browse_to: /admin
        - expected: access_denied_or_redirect
        - actual: access_granted
      
    test_2:
      description: "Modify user ID"
      steps:
        - login_as: user1
        - modify_cookie: user_id=1 to user_id=2
        - expected: still user1 context
        - actual: now user2 context
  
  impact_validation:
    - unauthorized_data_access
    - privilege_escalation
    - account_takeover
```

## Evidence Validation

### Evidence Requirements

```yaml
evidence_standards:
  minimum:
    - screenshot_of_vulnerability
    - url_or_target
    - timestamp
    - request_response_pair
  
  preferred:
    - multiple_screenshots
    - video_recording
    - tool_output
    - network_capture
    - poc_code
  
  comprehensive:
    - all_minimum_items
    - all_preferred_items
    - exploit_script
    - impact_demonstration
```

### Evidence Quality Checklist

```yaml
evidence_quality:
  screenshots:
    - [ ] Clear and readable
    - [ ] Shows vulnerability
    - [ ] Includes timestamp
    - [ ] Has context (URL, etc)
    - [ ] No sensitive_data_exposed
  
  documentation:
    - [ ] Steps_to_reproduce_clear
    - [ ] Expected_vs_actual
    - [ ] Technical_details
    - [ ] Business_impact
    - [ ] Remediation_advice
  
  poc_code:
    - [ ] Works_exploit_code
    - [ ] No_false_positive_risk
    - [ ] Can_be_verified
    - [ ] Not_destructive
```

## False Positive Management

```yaml
false_positive_detection:
  indicators:
    - tool_error_in_output
    - inconsistent_results
    - no_direct_evidence
    - requires_impossible_prerequisites
  
  verification_steps:
    1: rerun_with_different_tool
    2: manual_test_confirmation
    3: source_code_review
    4: configuration_verification
  
  resolution:
    confirm_false_positive:
      - document_reason
      - mark_in_report
      - explain_why_false
    
    still_potential:
      - additional_testing
      - escalate_for_review
      - document_uncertainty
```

## Impact Validation

### Business Impact Assessment

```yaml
impact_assessment:
  confidentiality:
    - data_types_accessible
    - data_volume
    - regulatory_implications
    - reputational_risk
  
  integrity:
    - modification_possible
    - data_corruption_risk
    - service_availability
  
  availability:
    - service_disruption
    - dos_possible
    - recovery_requirements
  
  cvss_calculation:
    attack_vector: [network|adjacent|local|physical]
    attack_complexity: [low|high]
    privileges_required: [none|low|high]
    user_interaction: [none|required]
    scope: [unchanged|changed]
    confidentiality_impact: [none|low|high]
    integrity_impact: [none|low|high]
    availability_impact: [none|low|high]
```

## Remediation Validation

```yaml
remediation_review:
  technical_soundness:
    - fix_addresses_root_cause
    - fix_does_not_break_functionality
    - fix_is_complete
  
  implementation_feasibility:
    - resource_requirements
    - timeline_realistic
    - expertise_required
    - testing_required
  
  alternative_review:
    - multiple_fix_options
    - pros_cons_evaluated
    - best_practice_considered
  
  priority_confirmation:
    - matches_severity
    - considers_exploitability
    - considers_business_impact
```

---

**Use this validation framework to ensure findings are accurate, evidence is complete, and reports are reliable.**
