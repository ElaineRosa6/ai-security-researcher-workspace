# Chain of Thought (CoT) Prompt

## Purpose

Guide systematic reasoning for complex security problems.

## CoT Framework

### 1. Problem Decomposition

When facing a complex security challenge:

```
Step 1: What is being asked?
        → Break down into sub-problems

Step 2: What information do I have?
        → List available data

Step 3: What information is missing?
        → Identify knowledge gaps

Step 4: What approach should I take?
        → Select methodology

Step 5: What could go wrong?
        → Consider edge cases
```

### 2. Evidence-Based Reasoning

For each finding:

```
Claim: [What you believe is true]

Evidence:
  - [Evidence 1 with source]
  - [Evidence 2 with source]
  - [Evidence 3 with source]

Reasoning:
  - If [evidence 1] and [evidence 2], then [conclusion]
  - This suggests [finding]

Confidence: [0-100%]

Alternative explanations:
  - [Alternative 1]
  - [Alternative 2]
```

### 3. Attack Simulation

For exploitation decisions:

```
Target: [Vulnerability]

Attack Path:
  1. [Initial access method]
  2. [Escalation step]
  3. [Lateral movement]
  4. [Objective completion]

Requirements:
  - [Tool/skill needed]
  - [Access required]
  - [Time estimate]

Risks:
  - [Risk 1]
  - [Risk 2]

Mitigation:
  - [How to minimize risk]

Decision: [Proceed/Skip/Wait for approval]
```

### 4. Differential Diagnosis

When analyzing anomalies:

```
Observation: [What was detected]

Hypothesis 1: [Possible explanation]
  - Supporting evidence: [list]
  - Contradicting evidence: [list]
  - Probability: [0-100%]

Hypothesis 2: [Alternative explanation]
  - Supporting evidence: [list]
  - Contradicting evidence: [list]
  - Probability: [0-100%]

Most Likely: [Hypothesis X]

Next Steps to Confirm: [Actions]
```

### 5. Decision Tree

For tool/method selection:

```
Question: Which approach to use?

Check 1: Is target in scope?
  → No: Stop, document
  → Yes: Continue

Check 2: Is technique authorized?
  → No: Skip, note in report
  → Yes: Continue

Check 3: Is technique safe?
  → High risk: Get approval
  → Medium risk: Take precautions
  → Low risk: Proceed

Check 4: Will technique be effective?
  → Yes: Proceed
  → No: Try alternative

Final Decision: [Action]
```

## Security-Specific Templates

### Template: Vulnerability Assessment

```
Vulnerability: [Name]
Severity: [Rating]

Analysis:
1. What is the vulnerability?
   → [Technical explanation]

2. How can it be exploited?
   → [Attack scenario]

3. What is the impact?
   → [Business/technical impact]

4. Is it exploitable in this context?
   → [Evidence of exploitability]

5. What defenses exist?
   → [Existing mitigations]

Conclusion:
→ [Confirmed/Potential/False Positive]
→ [Confidence level]
```

### Template: Attack Path Analysis

```
Objective: [Goal]

Attack Path Options:

Path A:
  Entry → [Step] → [Step] → Objective
  Difficulty: [1-10]
  Detection Risk: [1-10]

Path B:
  Entry → [Step] → [Step] → Objective
  Difficulty: [1-10]
  Detection Risk: [1-10]

Recommendation:
→ [Best path with justification]

Contingency:
→ [Backup plan if primary fails]
```

## Reflection Protocol

After each major step, ask:

```
1. Am I making correct assumptions?
   → Verify with evidence

2. Could there be another explanation?
   → Consider alternatives

3. What am I missing?
   → Check knowledge gaps

4. Is my approach efficient?
   → Optimize if possible

5. Should I ask for guidance?
   → Escalate if needed
```

## Confidence Calibration

| Evidence Level | Confidence Range |
|----------------|------------------|
| Direct confirmation | 95-100% |
| Strong evidence | 80-95% |
| Moderate evidence | 60-80% |
| Weak evidence | 40-60% |
| Speculation | <40% |

## Example: SQL Injection Analysis

```
Observation: Error message reveals SQL syntax

Thought Process:
1. The error "You have an error in your SQL syntax near '1'"
   suggests user input is not sanitized.

2. This indicates potential SQL injection.

3. To confirm, I need to test with:
   - Single quote: '
   - Boolean: ' OR '1'='1
   - Comment: '--

4. If these payloads cause different responses,
   SQL injection is confirmed.

5. Exploitation approach depends on:
   - Database type (MySQL, PostgreSQL, etc.)
   - Error-based vs blind
   - User privileges

Decision: Proceed with safe SQLi testing
         (using OR 1=1, not destructive commands)
```

---

**Apply this Chain of Thought framework to ensure thorough, logical analysis.**
