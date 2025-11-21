# Quick Validation Guide: All Steps - Master Checklist

**Purpose**: Universal quality gate for any VIANEO output
**Use**: Run this BEFORE the step-specific validation guide

---

## UNIVERSAL CHECKS (Apply to ALL Steps)

### 1. FILE BASICS (4 items)

- [ ] Correct filename format for this step
- [ ] Date in correct format (YYYY-MM-DD)
- [ ] Project name consistent across all files
- [ ] File extension correct (.md, .docx, .html as specified)

### 2. HEADER METADATA (4 items)

- [ ] All required metadata fields present
- [ ] Bold formatting on labels (if markdown)
- [ ] Consistent project name spelling
- [ ] Appropriate section separators (---)

### 3. CONTENT QUALITY (5 items)

- [ ] No vague language ("many", "some", "several", "various")
- [ ] All numbers quantified (specific counts, percentages)
- [ ] No marketing jargon or buzzwords
- [ ] Evidence cited for all claims OR gaps noted
- [ ] Professional tone (no emojis unless specified)

### 4. FORMAT CONSISTENCY (4 items)

- [ ] Headings use consistent hierarchy (##, ###, etc.)
- [ ] Tables formatted correctly (if applicable)
- [ ] Lists use consistent bullets or numbers
- [ ] No formatting errors (broken tables, misaligned text)

### 5. EVIDENCE STANDARDS (3 items)

- [ ] Specific citations when evidence exists
- [ ] Clear "Need:" statements when evidence missing
- [ ] No unsubstantiated claims

---

## STEP-SPECIFIC QUICK GUIDES

After passing universal checks, use the appropriate quick guide:

| Step | Quick Guide | Key Focus |
|------|-------------|-----------|
| 0 | `QUICK_VALIDATION_Step0.md` | Character limits (150/300/200) |
| 2 | `QUICK_VALIDATION_Step2.md` | 40 questions scored, red flags |
| 3 | `QUICK_VALIDATION_Step3.md` | 29 questions, Desirability 3.5 |
| 5 | `QUICK_VALIDATION_Step5.md` | 60-char needs, reliability ratings |
| 9 | `QUICK_VALIDATION_Step9.md` | Emojis, 250-char notes |
| 10 | `QUICK_VALIDATION_Step10.md` | 6-8 sentences, no em dashes |
| 11 | `QUICK_VALIDATION_Step11.md` | HTML functional, coverage metrics |

---

## QUICK DECISION FLOW

```
START
  ↓
Universal Checks (20 items)
  ↓
All Pass? → YES → Proceed to Step-Specific Guide
  ↓            ↓
  NO          Step-Specific Checks
  ↓            ↓
FIX         All Pass? → YES → APPROVED ✅
ISSUES         ↓
  ↓            NO
  ↓            ↓
Return      FIX ISSUES
to Start       ↓
            Return to
            Step-Specific
```

---

## FASTEST UNIVERSAL FIXES

**Vague language detected?**
- "many users" → "127 users"
- "some validation" → "5 customer interviews"
- "significant growth" → "340% YoY growth"
- "several iterations" → "3 iterations over 4 months"

**Missing evidence citations?**
- Add specific sources: "Interview transcripts dated Oct 2024"
- Or acknowledge gap: "Need: 10+ customer interviews per segment"
- Never claim without citation or gap acknowledgment

**Inconsistent project name?**
- Pick ONE spelling (e.g., "TechEd" not "Tech Ed" or "Teched")
- Search/replace across entire document
- Verify all metadata fields match

---

## QUALITY TIERS

| Tier | Criteria | Implication |
|------|----------|-------------|
| **Tier 1: Board-Ready** | 100% universal + 95%+ step-specific | Deliver to investors/board |
| **Tier 2: Professional** | 100% universal + 85%+ step-specific | Deliver to internal stakeholders |
| **Tier 3: Draft** | 90%+ universal + 75%+ step-specific | Acceptable for iteration |
| **Below Tier 3** | <90% universal OR <75% step-specific | Requires significant revision |

**Minimum Standard**: Tier 2 (Professional) for all VIANEO deliveries

---

## TIME BUDGET (Total: 8 minutes)

- Universal checks: 3 minutes
- Step-specific checks: 5 minutes
- **Total validation**: 8 minutes maximum

**If validation takes >10 minutes → Quality issues are systemic, not minor**

---

## UNIVERSAL RED FLAGS

**Stop immediately if ANY are true:**

1. ❌ Project name spelled differently in different sections
2. ❌ Vague quantifiers used more than 3 times
3. ❌ Marketing jargon ("revolutionary", "game-changing", "cutting-edge")
4. ❌ Claims without evidence and without "Need:" gaps
5. ❌ Formatting broken (tables not rendering, headers wrong)

---

## PRE-DELIVERY FINAL CHECK

**Before sending to anyone, confirm:**

- [ ] Passed universal checks (20/20)
- [ ] Passed step-specific checks (varies by step)
- [ ] Filename matches convention
- [ ] Both MD and DOCX created (if both required)
- [ ] Reviewed by second person (if high-stakes)

**If all checked → APPROVED FOR DELIVERY ✅**

---

## VALIDATION WORKFLOW

**For AI Generating Outputs:**
1. Generate content following step methodology
2. Format according to step format spec
3. Run this universal validation first (3 min)
4. Run step-specific validation (5 min)
5. Fix all identified issues
6. Re-validate after fixes
7. Deliver only if 100% universal + 90%+ step-specific

**For Humans Reviewing Outputs:**
1. Receive output from generator
2. Run universal validation (3 min)
3. If fails universal → return with feedback
4. Run step-specific validation (5 min)
5. Approve if meets Tier 2+ standards
6. Return for revision if below Tier 2

---

## MASTER FORMAT SPEC INDEX

All format specifications in `/docs/`:

- `FORMAT_SPEC_Step0_Executive_Brief.md`
- `FORMAT_SPEC_Step2_40Q_Diagnostic.md`
- `FORMAT_SPEC_Step3_Market_Maturity.md`
- `FORMAT_SPEC_Step5_Needs_Requesters.md`
- `FORMAT_SPEC_Step9_Ecosystem_Value_Network.md`
- `FORMAT_SPEC_Step10_Diagnostic_Comment.md`
- `FORMAT_SPEC_Step11_Features_Needs_Matrix.md`

For comprehensive specifications, consult the appropriate format spec above.

---

**This universal guide ensures baseline quality before step-specific validation.**
