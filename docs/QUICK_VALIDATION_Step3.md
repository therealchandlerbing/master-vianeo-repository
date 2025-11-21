# Quick Validation Guide: Step 3 - Market Maturity Assessment

**Purpose**: Fast 5-minute quality check before delivery
**Pass Criteria**: All ✓ boxes must be checked

---

## 1. STRUCTURE (6 items)

- [ ] Header: "Vianeo Market Maturity Assessment - [Name]"
- [ ] All 5 metadata fields present (Date, Project, Evaluator, Version, Stage)
- [ ] PART 1: Assessment table with all 29 questions
- [ ] PART 2: All 5 dimension calculations
- [ ] PART 3: Overall weighted score
- [ ] PART 4: Key findings sections

## 2. TABLE FORMAT (5 items)

- [ ] Q# formatted correctly (Q1-Q29, no spaces or leading zeros)
- [ ] All 29 rows present (no gaps)
- [ ] Scores are 1-5 integers only (no decimals)
- [ ] Justifications are single sentences, NO period at end
- [ ] Evidence column: specific citation OR "Need: [action]"

## 3. DIMENSION CALCULATIONS (6 items)

- [ ] Legitimacy: (Q8 + Q13) / 2 = X.X
- [ ] Desirability: (Q2+Q4+Q5+Q6+Q7+Q9+Q11+Q12+Q21+Q22+Q25+Q28) / 12 = X.X
- [ ] Acceptability: (Q3+Q10+Q17+Q20+Q23+Q24) / 6 = X.X
- [ ] Feasibility: (Q1+Q15+Q16+Q18+Q26) / 5 = X.X
- [ ] Viability: (Q14+Q19+Q27+Q29) / 4 = X.X
- [ ] All formulas shown with explicit arithmetic

## 4. THRESHOLDS (6 items)

- [ ] Legitimacy threshold: 3.0
- [ ] **Desirability threshold: 3.5** (HIGHEST - not 3.0!)
- [ ] Acceptability threshold: 3.0
- [ ] Feasibility threshold: 3.0
- [ ] Viability threshold: 3.0
- [ ] Overall threshold: 3.2

## 5. CRITICAL CHECKS (5 items)

**THESE ARE MOST COMMONLY WRONG:**

- [ ] Desirability threshold is 3.5 (NOT 3.0)
- [ ] Justifications have NO period at end
- [ ] Status uses ✓ or ✗ symbols (not "Pass"/"Fail" text)
- [ ] Overall score weights: 0.15, 0.25, 0.20, 0.20, 0.20
- [ ] Category matches score range (Excellent 4.0-5.0, etc.)

## 6. MATH VERIFICATION (3 items)

- [ ] Dimension averages correct (add scores, divide by question count)
- [ ] Overall score = (L×0.15)+(D×0.25)+(A×0.20)+(F×0.20)+(V×0.20)
- [ ] Category assigned correctly for overall score

---

## QUICK DECISION MATRIX

| Checks Passed | Decision |
|--------------|----------|
| 31/31 (100%) | ✅ **APPROVED** - Deliver immediately |
| 28-30 (90-97%) | ⚠️ **FIX MINOR** - Quick corrections needed |
| 25-27 (81-87%) | ❌ **REVISE** - Significant issues, rework required |
| <25 (<81%) | 🛑 **REJECT** - Does not meet minimum standards |

---

## FASTEST CHECKS (Do These First)

**30-second scan:**
1. Count Q# rows → must be exactly 29
2. Check Desirability threshold → must say 3.5
3. Scan justification column → no periods at sentence ends

**If any fail → Stop and fix before full review**

---

## INSTANT RED FLAGS

**Stop immediately if you see:**
- ❌ Desirability threshold listed as 3.0
- ❌ Overall score weights don't sum to 1.0
- ❌ Q# has gaps (Q1, Q2, Q4... missing Q3)
- ❌ Justifications are 2+ sentences
- ❌ Status says "Pass" instead of ✓

---

## COMMON FIXES (2-minute corrections)

**Wrong Desirability threshold?**
- Change from 3.0 to 3.5
- Update status if score is 3.0-3.4 (should be ✗ FAIL)

**Periods at end of justifications?**
- Find/replace ". |" with " |" (space before pipe)
- Verify no justification ends with punctuation

**Wrong status symbols?**
- Replace "Pass" with "✓ PASS"
- Replace "Fail" with "✗ FAIL"
- Replace "Passed" with "✓ PASS"

**Calculation errors?**
- Recalculate each dimension manually
- Show arithmetic: (3 + 4 + 5) / 3 = **4.0**
- Verify weighted sum for overall

---

## SCORE CATEGORY REFERENCE

| Score Range | Category | Quick Check |
|-------------|----------|-------------|
| 4.0 - 5.0 | Excellent | Strong proceed |
| 3.5 - 3.9 | Promising | Proceed, strengthen gaps |
| 3.2 - 3.4 | Developing | Conditional proceed |
| 2.5 - 3.1 | Concerning | Validation needed |
| 1.0 - 2.4 | Non-viable | Pivot or stop |

---

**Time Budget**: 5 minutes maximum for this validation
**Format Spec**: `docs/FORMAT_SPEC_Step3_Market_Maturity.md`
