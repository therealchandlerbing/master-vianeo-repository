# Step 3: Market Maturity Assessment - Output Format Specification

**Version**: 1.0
**Purpose**: Exact format specification for Step 3 outputs to ensure consistency

---

## Required Output Structure

### Document Header (Required)

```markdown
# Vianeo Market Maturity Assessment - [Exact Project Name from Step 0]

**Date**: YYYY-MM-DD (e.g., 2025-01-15)
**Project/Business Name**: [Full official name]
**Evaluator**: [Your name or "Assessment Team"]
**Assessment Version**: 1.0 (increment for revisions)
**Stage**: [From Step 0: Pre-Seed/Seed/Series A/etc.]

---
```

**Critical Rules:**
- Title MUST start with "Vianeo Market Maturity Assessment - "
- Use bold (**) for all metadata labels
- Date format: YYYY-MM-DD (ISO format)
- Three dashes for section breaks (---)

---

## PART 1: ASSESSMENT TABLE (Required)

### Exact Table Format:

```markdown
## PART 1: ASSESSMENT TABLE

| Q# | Score | Justification (One sentence) | Evidence Reference |
|----|-------|------------------------------|-------------------|
| Q1 | [1-5] | [Single sentence only, no period] | [Evidence ID or "Need: [action]"] |
| Q2 | [1-5] | [Single sentence only] | [Evidence or need] |
[Continue for all 29 questions]
```

**Critical Formatting Rules:**

1. **Q# Column**: "Q1" through "Q29" (no "Q" prefix for double digits: "Q10" not "Q 10")
2. **Score Column**: Integer 1-5 only (no decimals, no "N/A")
3. **Justification Column**:
   - ONE sentence maximum
   - NO period at end
   - Start with capital letter
   - Format: [What was assessed] + [Evidence status/level]
4. **Evidence Reference Column**:
   - If evidence exists: Cite specific document/data (e.g., "Interview notes dated Jan 2025")
   - If no evidence: Start with "Need: " followed by specific action needed
   - Be specific: "Need: 10+ customer interviews per segment" NOT "Need: More research"

**Example Rows:**
```markdown
| Q7 | 1 | Zero customer discovery interviews conducted | Need: 10+ customer interviews per segment |
| Q8 | 3 | Problem validated through 6 stakeholder conversations (clinic owners, office managers) | Pitch deck p.3-5, Interview notes folder |
| Q13 | 5 | Problem confirmed by 25+ parents and teachers, learning gap data supports urgency | Survey data n=127, Interview validation |
```

---

## PART 2: DIMENSION SCORES (Required)

### Exact Format Per Dimension:

```markdown
## PART 2: DIMENSION SCORES

### LEGITIMACY
**Formula**: (Q8 + Q13) / 2
**Calculation**: ([score] + [score]) / 2 = **[result]**
**Threshold**: 3.0
**Status**: [✓ PASS or ✗ FAIL] [optional: ⭐ EXCELLENT if ≥4.5]
```

**Critical Rules:**

1. **Dimension Order** (must be exact):
   - LEGITIMACY (all caps)
   - DESIRABILITY (all caps)
   - ACCEPTABILITY (all caps)
   - FEASIBILITY (all caps)
   - VIABILITY (all caps)

2. **Formula Line**: Show exact question numbers in formula
   - LEGITIMACY: (Q8 + Q13) / 2
   - DESIRABILITY: (Q2 + Q4 + Q5 + Q6 + Q7 + Q9 + Q11 + Q12 + Q21 + Q22 + Q25 + Q28) / 12
   - ACCEPTABILITY: (Q3 + Q10 + Q17 + Q20 + Q23 + Q24) / 6
   - FEASIBILITY: (Q1 + Q15 + Q16 + Q18 + Q26) / 5
   - VIABILITY: (Q14 + Q19 + Q27 + Q29) / 4

3. **Calculation Line**: Show arithmetic explicitly, result in bold
   - Format: `(X + X + ...) / N = **X.X**`
   - Round to 1 decimal place

4. **Threshold Line**: Use exact thresholds:
   - Legitimacy: 3.0
   - Desirability: 3.5 (HIGHEST)
   - Acceptability: 3.0
   - Feasibility: 3.0
   - Viability: 3.0

5. **Status Indicators**:
   - ✓ PASS (if score ≥ threshold)
   - ✗ FAIL (if score < threshold)
   - Optional: Add "⭐ EXCELLENT" if score ≥ 4.5
   - Optional: Add "(barely - needs strengthening)" if pass by ≤0.2

---

## PART 3: OVERALL SCORE (Required)

### Exact Format:

```markdown
## PART 3: OVERALL SCORE

**Formula**: (Legitimacy × 0.15) + (Desirability × 0.25) + (Acceptability × 0.20) + (Feasibility × 0.20) + (Viability × 0.20)

**Calculation**: ([L] × 0.15) + ([D] × 0.25) + ([A] × 0.20) + ([F] × 0.20) + ([V] × 0.20) = **[result]**

**Overall Weighted Score**: **[X.X]**

**Threshold**: 3.2
**Status**: [✓ PASS or ✗ FAIL]

### Category

**Your Category**: **[Category Name]** ([Recommendation text])
```

**Critical Rules:**

1. **Formula**: Use exact weights (never change these):
   - Legitimacy: 0.15 (15%)
   - Desirability: 0.25 (25%) - HIGHEST
   - Acceptability: 0.20 (20%)
   - Feasibility: 0.20 (20%)
   - Viability: 0.20 (20%)

2. **Calculation**: Show full arithmetic, round result to 1 decimal place

3. **Category Classification**:
   - Score 4.0-5.0: **Excellent** (Strong proceed recommendation)
   - Score 3.5-3.9: **Promising** (Proceed, strengthen gaps)
   - Score 3.2-3.4: **Developing** (Conditional proceed, address gaps)
   - Score 2.5-3.1: **Concerning** (Validation needed before proceeding)
   - Score 1.0-2.4: **Non-viable** (Consider pivot or validation before proceeding)

---

## PART 4: KEY FINDINGS (Required)

### Minimum Required Sections:

```markdown
## PART 4: KEY FINDINGS

### Top Strengths (3 items)

1. **[Dimension/Area]**: [Specific strength with evidence]
2. **[Dimension/Area]**: [Specific strength with evidence]
3. **[Dimension/Area]**: [Specific strength with evidence]

### Critical Gaps (3-5 items)

1. **[Dimension/Area] (Score X.X)**: [Specific gap] → **Action**: [What needs to happen]
2. [Continue...]

### Red Flags

**[Count] red flags identified:**

- [ ] [Specific red flag with dimension reference]
- [ ] [Specific red flag with dimension reference]

### Recommendations

**[PROCEED / CONDITIONAL PROCEED / STOP]**: [Specific recommendation based on overall score]

**Priority Actions (Next 30 days):**
1. [Specific action with owner and deadline]
2. [Specific action with owner and deadline]
3. [Specific action with owner and deadline]
```

---

## Optional: Executive Summary

**When to include**: If overall score ≥ 3.2 (passing), add executive summary BEFORE Part 1

```markdown
## EXECUTIVE SUMMARY

**Overall Score**: X.X / 5.0 ([Category])
**Status**: X/5 dimensions pass thresholds, [characterization]
**Key Strength**: [Highest-scoring dimension or validated area]
**Key Gap**: [Lowest-scoring dimension or critical missing validation]
**Recommendation**: [Specific next step]

---
```

---

## Validation Checklist

Before delivering Step 3 output, verify:

### Structure Completeness
- [ ] Document header with all 5 metadata fields
- [ ] Horizontal rule (---) after header
- [ ] PART 1: Assessment table with all 29 questions
- [ ] PART 2: All 5 dimension calculations
- [ ] PART 3: Overall score with category
- [ ] PART 4: Key findings with required sections

### Format Accuracy
- [ ] Title starts with "Vianeo Market Maturity Assessment - "
- [ ] Date in YYYY-MM-DD format
- [ ] All Q# formatted correctly (Q1-Q29, no extra spaces)
- [ ] All justifications are single sentences
- [ ] All dimension names in ALL CAPS
- [ ] All formulas show exact question numbers
- [ ] All calculations show arithmetic explicitly
- [ ] Status uses ✓ or ✗ symbols
- [ ] Thresholds match specification (3.0 or 3.5 for Desirability)
- [ ] Overall score uses exact weights (0.15, 0.25, 0.20, 0.20, 0.20)

### Content Quality
- [ ] Every score 1-5 has specific justification
- [ ] Evidence column populated for every question
- [ ] "Need:" prefix used when evidence missing
- [ ] Dimension scores calculated correctly
- [ ] Overall weighted score calculated correctly
- [ ] Category matches score range
- [ ] Top 3 strengths identified with evidence
- [ ] Critical gaps listed with scores and actions
- [ ] Recommendations are specific and actionable

---

## File Naming Convention

**Format**: `[ProjectName]_MarketMaturity_Assessment_YYYYMMDD.md`

**Examples**:
- `HealthTech_MarketMaturity_Assessment_20250115.md`
- `EduLearn_MarketMaturity_Assessment_20250115.md`

**Rules**:
- No spaces in filename (use underscores or CamelCase)
- Date format: YYYYMMDD (no dashes)
- Always end with .md extension

---

## Common Mistakes to Avoid

1. ❌ Adding periods at end of justifications → ✅ No punctuation at end
2. ❌ Multi-sentence justifications → ✅ One sentence maximum
3. ❌ Vague evidence ("some research") → ✅ Specific ("Interview notes n=12, dated Oct 2024")
4. ❌ Wrong threshold for Desirability (3.0) → ✅ Must be 3.5
5. ❌ Incorrect weights in overall score → ✅ Use exact weights from formula
6. ❌ Missing horizontal rules (---) → ✅ Add after header and between major parts
7. ❌ Inconsistent Q# formatting ("Q 8" or "Q08") → ✅ Always "Q8" (no space, no leading zero)
8. ❌ Scores as text ("three") → ✅ Always numeric (3)
9. ❌ Missing **bold** on key labels → ✅ Bold all metadata labels, formulas, scores
10. ❌ Category not matching score range → ✅ Verify category against classification table

---

**This specification ensures every Step 3 output follows the exact same format for professional consistency and automated processing compatibility.**
