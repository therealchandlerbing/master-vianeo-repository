# Quick Validation Guide: Step 2 - 40Q Diagnostic

**Purpose**: Fast 5-minute quality check before delivery
**Pass Criteria**: All ✓ boxes must be checked

---

## 1. STRUCTURE (5 items)

- [ ] Header with all 5 metadata fields
- [ ] All 40 questions present (T1-T9, Tech1-Tech11, M1-M12, C1-C8)
- [ ] All 4 dimension sections labeled correctly
- [ ] Dimension averages calculated for each
- [ ] Red flags section included

## 2. SCORING COMPLETE (5 items)

- [ ] All 40 questions have scores (1-5, INSUFFICIENT DATA, N/A, YES/NO, or CONTEXTUAL NOTE)
- [ ] No blank scores
- [ ] Score justifications provided for all numeric scores
- [ ] Evidence references cited or gaps noted
- [ ] Special codes used appropriately (not overused)

## 3. DIMENSION CALCULATIONS (4 items)

- [ ] Team average: (T1+T2+...+T9) / count (excluding special codes)
- [ ] Technology average: (Tech1+Tech2+...+Tech11) / count
- [ ] Management average: (M1+M2+...+M12) / count
- [ ] Commercial average: (C1+C2+...+C8) / count

## 4. RED FLAGS CHECK (6 items)

**Check for red flag triggers:**

- [ ] Any scores of 1? (CRITICAL red flag)
- [ ] Team: Multiple scores of 2, or T3/T5/T7 ≤2?
- [ ] Technology: Multiple scores of 2, or Tech2/Tech6 ≤2?
- [ ] Management: Multiple scores of 2, or M4/M8 ≤2?
- [ ] Commercial: Multiple scores of 2, or C2/C7 ≤2?
- [ ] Red flags documented with rationale in Red Flags section

## 5. TWO-DOCUMENT OUTPUT (4 items)

**Must produce 4 files total:**

- [ ] File 1: Assessment Results Markdown
- [ ] File 2: Assessment Results DOCX (converted from MD)
- [ ] File 3: Score Summary Markdown
- [ ] File 4: Score Summary DOCX (converted from MD)

## 6. CONSISTENCY CHECK (3 items)

- [ ] Dimension scores identical in both documents
- [ ] Red flags identical in both documents
- [ ] Project name/date identical in both documents

---

## QUICK DECISION MATRIX

| Checks Passed | Decision |
|--------------|----------|
| 27/27 (100%) | ✅ **APPROVED** - Deliver immediately |
| 24-26 (89-96%) | ⚠️ **FIX MINOR** - Quick corrections needed |
| 20-23 (74-85%) | ❌ **REVISE** - Significant issues, rework required |
| <20 (<74%) | 🛑 **REJECT** - Does not meet minimum standards |

---

## FASTEST CHECKS (Do These First)

**30-second scan:**
1. Count questions → must be exactly 40
2. Search for blank scores → must be zero
3. Check dimension labels → Team, Technology, Management, Commercial

**If any fail → Stop and fix before full review**

---

## INSTANT RED FLAGS

**Stop immediately if you see:**
- ❌ Less than 40 questions total
- ❌ Dimension has NO scores (all blank)
- ❌ Multiple scores of 1 with no red flags documented
- ❌ Only 2 output files instead of 4
- ❌ Scores different between Results and Summary docs

---

## COMMON FIXES (2-minute corrections)

**Missing questions?**
- Verify all ranges covered:
  - Team: T1-T9 (9 questions)
  - Technology: Tech1-Tech11 (11 questions)
  - Management: M1-M12 (12 questions)
  - Commercial: C1-C8 (8 questions)

**Calculation errors?**
- Exclude special codes from average
- Count only numeric scores (1-5)
- Formula: SUM(numeric scores) / COUNT(numeric scores)

**Missing red flags?**
- Any score of 1 → CRITICAL red flag (must document)
- Dimension with 3+ scores of 2 → red flag
- Critical questions ≤2 → red flag

**Wrong special codes?**
- Use INSUFFICIENT DATA when truly no information available
- Use N/A when question doesn't apply to this stage/model
- Use YES/NO for binary questions
- Use CONTEXTUAL NOTE sparingly (only when complexity requires explanation)

---

## DIMENSION THRESHOLDS

| Average | Status | Action |
|---------|--------|--------|
| 4.0-5.0 | STRONG | Highlight as strength |
| 3.0-3.9 | ADEQUATE | Acceptable, monitor |
| 2.0-2.9 | CONCERN | Requires improvement plan |
| 1.0-1.9 | CRITICAL | Immediate action required |

**Minimum threshold**: 50% of possible score (2.5 average if all questions scored)

---

## RED FLAG DECISION TREE

```
Score of 1 detected?
  ↓ YES → CRITICAL RED FLAG (document immediately)
  ↓ NO
  ↓
Multiple scores of 2 in one dimension?
  ↓ YES → Dimension-specific red flag
  ↓ NO
  ↓
Critical question (T3, T5, T7, Tech2, Tech6, M4, M8, C2, C7) ≤ 2?
  ↓ YES → Question-specific red flag
  ↓ NO
  ↓
No red flags
```

---

## FILE NAMING CONVENTION

**Standard format:**
- `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Results.md`
- `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Results.docx`
- `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Summary.md`
- `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Summary.docx`

**Examples:**
- `TechEd_2025-01-15_02_Diagnostic_Results.md`
- `TechEd_2025-01-15_02_Diagnostic_Summary.docx`

---

## SPECIAL CODES REFERENCE

| Code | When to Use | Example |
|------|-------------|---------|
| **1-5** | Numeric evidence available | "Team has 2 part-time founders" = 2 |
| **INSUFFICIENT DATA** | Cannot assess, no information | No team roster available |
| **N/A** | Question doesn't apply | "Patent filed?" for service business |
| **YES/NO** | Binary question answer | "Founders committed full-time?" |
| **CONTEXTUAL NOTE** | Requires nuanced explanation | Complex IP situation |

**Rule**: Use numeric scores (1-5) whenever possible. Special codes should be <20% of total.

---

**Time Budget**: 5 minutes maximum for this validation
**Format Spec**: `docs/FORMAT_SPEC_Step2_40Q_Diagnostic.md`
