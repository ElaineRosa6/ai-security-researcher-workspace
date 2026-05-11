# Requirement Parsing Prompt

## Purpose

Parse user security testing requirements into structured, actionable task definitions.

## Input Format

```
[User Requirement Text]
```

## Parsing Process

### Step 1: Intent Classification

Determine the primary intent:

| Intent | Keywords |
|--------|----------|
| Penetration Test | pentest, penetration, 渗透测试 |
| Vulnerability Scan | scan, vulnerability, 漏洞扫描 |
| Incident Response | incident, breach, 应急响应 |
| Security Audit | audit, compliance, 审计 |
| Red Team | red team, 红队 |
| Forensic | forensic, 取证, investigation |

### Step 2: Target Extraction

Extract target information:

```yaml
target:
  type: web | network | mobile | api | domain | all
  value: "[specific target]"
  scope: "[scope description]"
```

### Step 3: Constraint Identification

Identify constraints:

| Constraint | Detection | Action |
|------------|-----------|--------|
| Passive Only | "passive", "只收集信息" | Skip exploitation |
| Time Limited | "time", "时间" | Prioritize critical |
| Specific Test | "API only", "API测试" | Narrow scope |
| No Exploit | "no exploit", "不利用" | Assessment only |

### Step 4: Deliverable Definition

Determine expected outputs:

- Executive report
- Technical report
- Finding list
- Remediation plan
- Presentation

## Output Template

```markdown
## Parsed Requirement

**Type**: [penetration_test | vulnerability_scan | ...]
**Priority**: [Critical | High | Medium | Low]
**Target**:
  - Primary: [target]
  - Secondary: [targets]
**Scope**:
  - Included: [list]
  - Excluded: [list]
**Constraints**:
  - [constraint 1]
  - [constraint 2]
**Deliverables**:
  - [deliverable 1]
  - [deliverable 2]
**Timeline**: [duration]

## Confidence Score: [0.0-1.0]

## Missing Information:
- [info 1]
- [info 2]
```

## Examples

### Example 1: Web Pentest

**Input**:
```
测试 https://app.example.com 的安全性，重点关注认证漏洞
```

**Output**:
```yaml
type: penetration_test
priority: high
target:
  primary: https://app.example.com
scope:
  included:
    - authentication
    - authorization
    - session_management
  excluded:
    - denial_of_service
constraints:
  - focus_on_authentication
deliverables:
  - vulnerability_report
  - remediation_guide
confidence: 0.85
```

### Example 2: Full Network Assessment

**Input**:
```
对 192.168.1.0/24 网段进行全面渗透测试，包括内网
```

**Output**:
```yaml
type: penetration_test
priority: critical
target:
  primary: 192.168.1.0/24
scope:
  included:
    - all_services
    - internal_network
    - privilege_escalation
constraints: []
deliverables:
  - executive_summary
  - technical_report
  - finding_details
confidence: 0.95
```

### Example 3: Incident Response

**Input**:
```
发现可疑活动，需要进行应急响应和取证分析
```

**Output**:
```yaml
type: incident_response
priority: critical
target:
  primary: affected_systems
scope:
  included:
    - evidence_collection
    - malware_analysis
    - timeline_creation
constraints:
  - preserve_evidence
deliverables:
  - incident_report
  - forensic_evidence
  - timeline
confidence: 0.90
```

## Edge Cases

### Unclear Scope

When scope is vague:
```
"Please test the security"
```

Response:
```yaml
clarification_needed:
  - "What specific systems should be tested?"
  - "What testing types are authorized?"
  - "Are exploitation techniques allowed?"
```

### Conflicting Requirements

When requirements conflict:
```
"Test thoroughly but don't break anything"
```

Resolution:
```
acknowledge_conflict: true
resolution: "Will prioritize non-destructive testing.
            Destructive tests will be requested for confirmation."
```

## Confidence Scoring

| Score | Meaning |
|-------|---------|
| 0.9-1.0 | Fully clear requirement |
| 0.7-0.9 | Mostly clear, minor clarifications |
| 0.5-0.7 | Some ambiguity, need clarification |
| <0.5 | Significant clarification needed |

---

**Use this prompt to consistently parse and structure user requirements.**
