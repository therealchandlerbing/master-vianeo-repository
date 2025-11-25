# Step 4: Legitimacy Worksheet - Output Format Specification

**Version**: 2.0
**Purpose**: Exact format specification for Step 4 outputs (Legitimacy analysis)
**Dimension**: Legitimacy (15% of VIANEO score)

---

## Required Output Structure

### Document Header (Required)

```markdown
# Legitimacy Worksheet - [Project Name]

**Date**: YYYY-MM-DD
**Project/Business Name**: [Full official name]
**Evaluator**: [Name or "Assessment Team"]
**Assessment Version**: 1.0
**Source**: Step 0 Executive Brief + Additional Research

---
```

---

## Section 1: Problem Statement

### Format

```markdown
## PROBLEM STATEMENT

### Problem Description (250 characters max)

[Solution-neutral description of the problem, quantified where possible]

**Character Count**: [X]/250

### Affected Population

- **Who**: [Specific population]
- **How Many**: [Size estimate with source]
- **Where**: [Geographic scope]

### Problem Impact

- **Frequency**: [How often the problem occurs]
- **Severity**: [Quantified impact - time, cost, risk]
- **Current Cost**: [Dollar/time impact if available]

### Validation Status

| Aspect | Status | Evidence |
|--------|--------|----------|
| Problem exists | [Validated/Partial/Assumed] | [Source] |
| Affects population | [Validated/Partial/Assumed] | [Source] |
| Impact quantified | [Validated/Partial/Assumed] | [Source] |
```

### Quality Requirements

- Problem statement must be **solution-neutral** (no mention of your product)
- Must be **quantified** (numbers, not adjectives)
- Must be **specific** (who, what, where, how much)
- 250 character limit strictly enforced

---

## Section 2: Field of Application

### Format

```markdown
## FIELD OF APPLICATION

### Industry/Sector (250 characters max)

[Description of the field where this problem exists]

**Character Count**: [X]/250

### Context Details

| Dimension | Description |
|-----------|-------------|
| **Industry** | [Specific industry/sector] |
| **Geography** | [Target regions/markets] |
| **Company Size** | [Target company characteristics] |
| **Use Case** | [Specific application context] |

### Market Characteristics

- **Market Size**: [TAM if available]
- **Growth Rate**: [Trend data if available]
- **Key Trends**: [1-2 relevant trends]
```

---

## Section 3: Means Analysis

### Format

```markdown
## MEANS ANALYSIS

### Human Means

| Description (60 chars max) | Differentiating |
|----------------------------|-----------------|
| [Team capability/expertise] | Yes / No |
| [Team capability/expertise] | Yes / No |
| [Team capability/expertise] | Yes / No |

### Physical/Intellectual Means

| Description (60 chars max) | Differentiating |
|----------------------------|-----------------|
| [Technology/IP/Asset] | Yes / No |
| [Technology/IP/Asset] | Yes / No |
| [Technology/IP/Asset] | Yes / No |

### Financial Means

| Description (60 chars max) | Differentiating |
|----------------------------|-----------------|
| [Funding/Resources] | Yes / No |
| [Funding/Resources] | Yes / No |
```

### Format Requirements

- Each means description: **60 characters maximum**
- Every means must have **Differentiating: Yes/No** designation
- At least **1-2 differentiating means** should be identified
- Format: `[Description] | Differentiating: Yes/No`

---

## Section 4: Differentiation Assessment

### Format

```markdown
## DIFFERENTIATION ASSESSMENT

### Differentiating Means Summary

| Means | Type | Why Differentiating |
|-------|------|---------------------|
| [Means 1] | Human/Physical/Financial | [Brief explanation] |
| [Means 2] | Human/Physical/Financial | [Brief explanation] |

### Differentiation Validation

| Differentiator | Validation Status | Evidence |
|----------------|-------------------|----------|
| [Means 1] | [Validated/Claimed] | [Source if validated] |
| [Means 2] | [Validated/Claimed] | [Source if validated] |

### Non-Differentiating (Table Stakes)

- [Means that are necessary but not unique]
- [Means that competitors also have]
```

---

## Section 5: Evidence Summary

### Format

```markdown
## EVIDENCE SUMMARY

### Validation Status by Area

| Area | Confidence Level | Interview Count | Status |
|------|------------------|-----------------|--------|
| Problem | L1/L2/L3 | [#] | [Validated/Partial/Needs Validation] |
| Population | L1/L2/L3 | [#] | [Validated/Partial/Needs Validation] |
| Differentiation | L1/L2/L3 | [#] | [Validated/Partial/Needs Validation] |

### Key Evidence Documents

1. [Document name and date]
2. [Document name and date]
3. [Document name and date]

### Validation Gaps

- [ ] [Gap 1 - action needed]
- [ ] [Gap 2 - action needed]
```

---

## Section 6: Legitimacy Score

### Format

```markdown
## LEGITIMACY SCORE

### Score Calculation

**Legitimacy** = (Q8 + Q13) / 2

- Q8 (Problem validated with stakeholders): [1-5]
- Q13 (Problem confirmed by research): [1-5]

**Legitimacy Score**: **[X.X]** / 5.0

### Threshold Check

- **Required**: ≥3.0
- **Status**: ✓ PASS / ✗ FAIL

### Score Justification

[2-3 sentences explaining the score based on evidence reviewed]
```

---

## Output Files

### Required Deliverables

1. **Markdown Analysis** (primary)
   - Full analysis with all sections
   - File: `[ProjectName]_Legitimacy_Analysis.md`

2. **DOCX Format** (if requested)
   - Professional formatting
   - File: `[ProjectName]_Legitimacy_Worksheet.docx`

### File Naming Convention

```
[ProjectName]_Legitimacy_[Analysis/Worksheet]_YYYYMMDD.[md/docx]
```

---

## Downstream Dependencies

Step 4 data flows to:

| Downstream Step | Data Required | Format |
|-----------------|---------------|--------|
| **Step 11 (Means View)** | All means with differentiation status | Exact match required |
| **Step 10 (Diagnostic)** | Legitimacy score and key findings | Summary format |

---

## Quality Checklist

Before delivery, verify:

### Structure
- [ ] All 6 sections complete
- [ ] Header with metadata
- [ ] Horizontal rules between sections

### Problem Statement
- [ ] Solution-neutral (no product mention)
- [ ] Quantified impact
- [ ] ≤250 characters
- [ ] Validation status documented

### Means Analysis
- [ ] Human, Physical, Financial all covered
- [ ] Each description ≤60 characters
- [ ] Every means has Differentiating: Yes/No
- [ ] At least 1-2 differentiating means identified

### Evidence
- [ ] Confidence levels assigned (L1/L2/L3)
- [ ] Interview counts documented
- [ ] Validation gaps identified
- [ ] Sources cited

### Score
- [ ] Q8 and Q13 scored
- [ ] Calculation shown
- [ ] Threshold check completed
- [ ] Justification provided

---

## Common Mistakes to Avoid

1. ❌ Solution in problem statement → ✅ Problem only, no product
2. ❌ Vague problem ("inefficient processes") → ✅ Quantified ("12+ hours/week")
3. ❌ No differentiating means → ✅ At least 1-2 genuine differentiators
4. ❌ Means over 60 characters → ✅ Strict character limit
5. ❌ All means marked "Differentiating: Yes" → ✅ Be honest, some are table stakes
6. ❌ No evidence citations → ✅ Every claim needs source
7. ❌ L3 confidence without interviews → ✅ Match confidence to evidence

---

**This specification ensures every Step 4 output follows consistent format for legitimacy assessment.**
