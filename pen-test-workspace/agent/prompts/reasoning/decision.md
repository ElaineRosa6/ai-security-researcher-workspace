# Decision Making Prompt

## Purpose

Guide structured decision-making for complex security scenarios.

## Decision Framework

### 1. Problem Definition

```yaml
decision_problem:
  statement: "[What decision needs to be made?]"
  
  scope:
    - what_is_being_decided
    - what_is_not_being_decided
  
  constraints:
    - hard_constraints
    - soft_constraints
  
  stakeholders:
    - primary_affected
    - secondary_affected
```

### 2. Options Generation

```yaml
options_generation:
  brainstorming:
    - generate_minimum_3_options
    - include_standard_approach
    - include_innovative_approaches
    - include_conservative_approach
  
  options_structure:
    option_1:
      name: "[Name]"
      approach: "[Description]"
      pros: [list]
      cons: [list]
    
    option_2:
      name: "[Name]"
      approach: "[Description]"
      pros: [list]
      cons: [list]
```

### 3. Evaluation Criteria

```yaml
evaluation_criteria:
  primary:
    - effectiveness: weight_30
    - safety: weight_25
    - efficiency: weight_20
  
  secondary:
    - reversibility: weight_10
    - compliance: weight_10
    - maintainability: weight_5
```

### 4. Risk Assessment

```yaml
risk_assessment:
  option_1:
    risks:
      - risk_1:
          likelihood: low|medium|high
          impact: low|medium|high
          mitigation: "[How to mitigate]"
    residual_risk: low|medium|high
  
  option_2:
    risks: [...]
    residual_risk: ...
```

## Common Security Decisions

### 1. To Exploit or Not

```yaml
exploitation_decision:
  question: "Should we attempt exploitation?"
  
  authorization_check:
    - in_scope: true|false
    - technique_authorized: true|false
    - client_approved: true|false
  
  risk_factors:
    detection_risk: [low|medium|high]
    system_impact: [low|medium|high]
    data_risk: [low|medium|high]
  
  decision_matrix:
    high_impact_and_low_authorization:
      decision: "Do not exploit"
      reason: "Unacceptable risk"
    
    low_impact_and_high_authorization:
      decision: "Proceed with caution"
      reason: "Controlled environment"
    
    moderate_situation:
      decision: "Request explicit approval"
      reason: "Risk-benefit unclear"
```

### 2. Scope Escalation

```yaml
scope_decision:
  question: "Found something unexpected"
  
  assessment:
    - is_it_in_scope: yes|no|unclear
    - is_it_critical: yes|no
    - is_it_exploitable: yes|no
    
  options:
    option_1:
      name: "Stop testing"
      action: "Document and stop"
      pros: ["Safe", "Compliant"]
      cons: ["May miss findings"]
    
    option_2:
      name: "Continue limited testing"
      action: "Document and test minimally"
      pros: ["Can confirm impact"]
      cons: ["May exceed scope"]
    
    option_3:
      name: "Request scope expansion"
      action: "Contact client immediately"
      pros: ["Clear authorization"]
      cons: ["May delay engagement"]
  
  recommendation: "Based on severity and risk"
```

### 3. Tool Selection

```yaml
tool_selection:
  criteria:
    - effectiveness_on_target
    - stealth_level
    - required_privileges
    - potential_impact
  
  options_comparison:
    tool_a:
      effectiveness: high
      stealth: low
      privileges: low
      impact: medium
    
    tool_b:
      effectiveness: medium
      stealth: high
      privileges: medium
      impact: low
    
    tool_c:
      effectiveness: medium
      stealth: medium
      privileges: low
      impact: medium
  
  recommendation: "Based on engagement requirements"
```

### 4. Finding Severity

```yaml
severity_decision:
  factors:
    - cvss_score: [0-10]
    - exploitability: [easy|medium|hard]
    - business_impact: [low|medium|high|critical]
    - data_exposure: [none|limited|significant|complete]
  
  decision_tree:
    cvss_9_plus:
      severity: Critical
      action: Immediate remediation
    
    cvss_7_to_8:
      severity: High
      action: Urgent remediation
    
    cvss_4_to_6:
      severity: Medium
      action: Scheduled remediation
    
    cvss_below_4:
      severity: Low
      action: Future improvement
```

## Decision Documentation

```markdown
## Decision Record

**Date**: [YYYY-MM-DD]
**Decision Maker**: [Agent/Analyst]
**Engagement**: [Project Name]

### Situation

[Description of the situation requiring decision]

### Options Considered

1. **[Option Name]**
   - Approach: [Description]
   - Pros: [List]
   - Cons: [List]

2. **[Option Name]**
   - Approach: [Description]
   - Pros: [List]
   - Cons: [List]

### Evaluation

| Criteria | Weight | Option 1 | Option 2 |
|----------|--------|----------|----------|
| Effectiveness | 30% | Score | Score |
| Safety | 25% | Score | Score |
| Efficiency | 20% | Score | Score |
| **Total** | 100% | **Total** | **Total** |

### Risks

**[Option 1]**
- Risk 1: [Description] → [Mitigation]

**[Option 2]**
- Risk 1: [Description] → [Mitigation]

### Decision

**[Chosen Option]**

### Rationale

[Explanation of why this option was chosen]

### Approval

[Required approvals obtained]

### Review Date

[When this decision should be revisited]
```

## Escalation Protocol

```yaml
escalation_triggers:
  - critical_finding_discovered
  - scope_ambiguity_encountered
  - client_request_for_action
  - safety_threshold_exceeded
  - legal_compliance_question

escalation_levels:
  level_1:
    trigger: minor_questions
    contact: senior_tester
    response_time: 1_hour
  
  level_2:
    trigger: significant_findings
    contact: engagement_lead
    response_time: 30_minutes
  
  level_3:
    trigger: critical_issues
    contact: client_manager
    response_time: immediate

escalation_process:
  1: Document situation clearly
  2: Assess urgency and severity
  3: Contact appropriate escalation level
  4: Provide recommendations
  5: Document resolution
```

## Quick Decision Matrix

| Situation | Quick Decision | Review Required |
|-----------|---------------|----------------|
| Finding outside scope | Document only | Yes |
| Critical finding | Immediate report | Yes |
| Test causing issues | Stop test | Yes |
| Client requests new test | Get written approval | Yes |
| Tool not working | Try alternative | No |
| Time running out | Prioritize critical | Yes |

---

**Use this decision framework to make consistent, defensible security decisions.**
