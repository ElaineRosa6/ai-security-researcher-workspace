# Self-Check Prompt

## Purpose

Guide self-assessment and quality control during security operations.

## Pre-Task Checklist

Before starting any security test:

```
[ ] Authorization verified
[ ] Scope confirmed
[ ] Tools ready
[ ] Timeline clear
[ ] Backup/rollback plan ready
```

## During-Task Checks

### After Reconnaissance

```yaml
recon_check:
  coverage:
    - [ ] External footprint mapped
    - [ ] Subdomains enumerated
    - [ ] Email addresses collected
    - [ ] Technology fingerprint complete
  quality:
    - [ ] Findings documented
    - [ ] Evidence collected
    - [ ] Tools logged
  confidence: [0-100%]
```

### After Scanning

```yaml
scan_check:
  coverage:
    - [ ] All ports scanned
    - [ ] Services identified
    - [ ] OS detected
    - [ ] Vulnerabilities found
  quality:
    - [ ] Scan logs saved
    - [ ] Results validated
    - [ ] False positives marked
  confidence: [0-100%]
```

### After Exploitation

```yaml
exploit_check:
  authorization:
    - [ ] Within scope
    - [ ] Low risk confirmed
    - [ ] Client notified
  execution:
    - [ ] Exploit successful
    - [ ] Access obtained
    - [ ] Impact documented
  evidence:
    - [ ] Screenshots taken
    - [ ] Commands logged
    - [ ] Timestamps recorded
  cleanup:
    - [ ] No persistence left
    - [ ] Logs cleared
    - [ ] Backdoors removed
```

## Post-Task Quality Checks

### Finding Validation

```
Finding: [Title]
Severity: [Rating]

Validation Steps:
1. Can I reproduce this finding?
   → Steps to reproduce:
   → Result: [Reproducible/Not Reproducible]

2. Is this a false positive?
   → Evidence against:
   → Conclusion: [Real/False Positive]

3. Is the severity accurate?
   → CVSS calculation:
   → Adjustment (if needed):

4. Is the evidence complete?
   → Screenshots: [Yes/No]
   → Commands: [Yes/No]
   → Timestamps: [Yes/No]

5. Is remediation actionable?
   → Clear steps: [Yes/No]
   → Technical level appropriate: [Yes/No]

Final Status: [Confirm/Mark False Positive/Revise]
```

### Report Completeness

```
Report Section Review:

Executive Summary:
[ ] Overview written
[ ] Key findings highlighted
[ ] Business risk communicated
[ ] Recommendations included

Technical Findings:
[ ] All findings documented
[ ] Severity assigned
[ ] CVSS calculated
[ ] PoC included
[ ] Remediation provided

Appendices:
[ ] Raw evidence attached
[ ] Tool output included
[ ] Methodology documented

Quality Score: [0-100%]
```

## Self-Assessment Metrics

### Performance Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Findings per hour | > 2 | ? |
| False positive rate | < 10% | ? |
| Documentation completeness | > 90% | ? |
| Scope adherence | 100% | ? |

### Quality Metrics

```
Accuracy: [Did I get it right?]
Completeness: [Did I miss anything?]
Efficiency: [Was I thorough but efficient?]
Communication: [Was I clear?]
```

## Reflection Questions

After each engagement, ask:

```
1. What went well?
   → [List positive aspects]

2. What could be improved?
   → [List areas for improvement]

3. What did I learn?
   → [New techniques/approaches]

4. What should I do differently?
   → [Process improvements]

5. What should I remember?
   → [Lessons for future engagements]
```

## Red Flags to Watch

```
⚠️ Skipping documentation
⚠️ Working outside scope
⚠️ Ignoring safety limits
⚠️ Missing evidence
⚠️ False positives included
⚠️ Unrealistic severity ratings
⚠️ Vague remediation advice
```

## Confidence Calibration

| Situation | Expected Confidence |
|-----------|---------------------|
| Direct evidence | 95%+ |
| Tool output | 85-95% |
| Inferred | 60-85% |
| Guess | <60% |

---

**Use this self-check framework to maintain high-quality security assessments.**
