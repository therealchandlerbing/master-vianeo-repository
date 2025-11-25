# Quick Validation Guide: Step 7 - Needs Qualification Matrix

**Purpose**: Fast 5-minute quality check before delivery
**Pass Criteria**: All ✓ boxes must be checked
**Dimension**: Desirability (25% of VIANEO score - HIGHEST WEIGHT)

---

## 1. STRUCTURE (5 items)

- [ ] Interactive HTML matrix generated
- [ ] Analysis report (Markdown) complete
- [ ] Header with all required metadata
- [ ] Quadrant analysis included
- [ ] Priority recommendations documented

## 2. DATA MATCHING (6 items - CRITICAL)

**Step 5 → Step 7 Exact Match Required:**
- [ ] All requesters from Step 5 appear as columns
- [ ] Requester names match Step 5 EXACTLY (verbatim)
- [ ] All 10 needs from Step 5 appear as rows
- [ ] Need statements match Step 5 EXACTLY (verbatim)
- [ ] Interview counts match Step 5 data
- [ ] No paraphrasing or combining of needs

## 3. MATRIX COMPLETENESS (5 items)

- [ ] Every cell has Importance rating (1-5 or Fundamental/Important/Nice-to-Have)
- [ ] Every cell has Satisfaction rating (1-5 or scale)
- [ ] No empty cells in the matrix
- [ ] Rating scale consistent throughout
- [ ] Totals/averages calculated correctly

## 4. QUADRANT ANALYSIS (4 items)

**Four quadrants identified:**
- [ ] High Opportunity (High Importance + Low Satisfaction) → Green
- [ ] Monitor (High Importance + High Satisfaction) → Yellow
- [ ] Low Priority (Low Importance + Low Satisfaction) → Gray
- [ ] Over-served (Low Importance + High Satisfaction) → Red

## 5. IMPORTANCE RATINGS (4 items)

- [ ] Ratings based on interview data (not assumptions)
- [ ] "Fundamental" = blocking need, deal-breaker
- [ ] "Important" = significant impact on decision
- [ ] "Nice-to-Have" = would appreciate but not critical

## 6. SATISFACTION RATINGS (4 items)

- [ ] Ratings reflect current solution performance
- [ ] "Not At All" = completely unmet need
- [ ] "Partially" = some solutions exist but inadequate
- [ ] "Completely" = current solutions work well

---

## QUICK DECISION MATRIX

| Checks Passed | Decision |
|--------------|----------|
| 28/28 (100%) | ✅ **APPROVED** - Deliver immediately |
| 24-27 (86-96%) | ⚠️ **FIX MINOR** - Quick corrections needed |
| 20-23 (71-82%) | ❌ **REVISE** - Significant issues, rework required |
| <20 (<71%) | 🛑 **REJECT** - Does not meet minimum standards |

---

## FASTEST CHECKS (Do These First)

**30-second scan:**
1. Count columns → must equal requester count from Step 5
2. Count rows → must equal 10 (needs from Step 5)
3. Spot-check one need → wording must match Step 5 exactly

**If any fail → Stop and fix before full review**

---

## INSTANT RED FLAGS

**Stop immediately if you see:**
- ❌ Requester names differ from Step 5
- ❌ Need statements paraphrased from Step 5
- ❌ Missing requesters or needs
- ❌ Empty cells in matrix
- ❌ All ratings are same (likely not real data)
- ❌ No high-opportunity quadrant items
- ❌ Ratings not based on interview data

---

## COMMON FIXES (2-minute corrections)

**Requester name mismatch?**
- Return to Step 5 output
- Copy names exactly as written
- Don't combine or rename

**Need statement changed?**
- ❌ "Reduce admin time" (paraphrased)
- ✅ "Reduce time on manual admin tasks by 50%+" (exact from Step 5)
- Copy needs verbatim - character for character

**All same ratings?**
- Indicates lack of differentiation
- Review interview notes for nuance
- Each need should have varied ratings across requesters

**No high-opportunity items?**
- Either all needs are met (rare)
- Or ratings too generous
- Apply conservative scoring

---

## OPPORTUNITY CLASSIFICATION

**High Opportunity (Priority Focus)**
- Importance: Fundamental
- Satisfaction: Not At All
- Action: Primary feature focus
- Color: Green (#10b981)

**Expected (Table Stakes)**
- Importance: Fundamental/Important
- Satisfaction: Completely
- Action: Must maintain
- Color: Gray (#6b7280)

**Low Priority**
- Importance: Nice-to-Have
- Satisfaction: Any level
- Action: Deprioritize
- Color: Light Gray (#9ca3af)

**Over-served**
- Importance: Nice-to-Have
- Satisfaction: Completely
- Action: Potential to reduce
- Color: Red (#ef4444)

---

## VALIDATION REQUIREMENTS

**For Importance ratings:**
- Based on interview responses
- "Would this be a deal-breaker?" → Fundamental
- "How much would this influence your decision?" → Important/Nice-to-Have

**For Satisfaction ratings:**
- Based on current solution performance
- "How well do existing tools meet this need?" → Scale 1-5
- Reference specific tools mentioned in interviews

---

## DOWNSTREAM DEPENDENCIES

**Step 7 feeds into:**
- **Step 11 (Needs View)**: Importance ratings determine column colors
- High Opportunity needs become green columns in Features-Needs Matrix
- Requester segments populate dropdown selectors

**Must maintain exact data match for:**
- Need statements (60-char limit preserved)
- Requester names (exact match)
- Importance classifications

---

## OUTPUT FILES CHECKLIST

**Must deliver:**
- [ ] Interactive HTML matrix
- [ ] Markdown analysis report

**HTML features:**
- [ ] Sortable columns
- [ ] Color-coded cells
- [ ] Hover tooltips (optional)
- [ ] Responsive layout

---

## MATRIX VALIDATION CHECKLIST

Before finalizing, verify against Step 5:

| Step 5 Element | Step 7 Must Match |
|----------------|-------------------|
| Requester 1 name | Column 1 header |
| Requester 2 name | Column 2 header |
| ... | ... |
| Need 1 statement | Row 1 label |
| Need 2 statement | Row 2 label |
| ... | ... |
| Interview count per requester | Shown in column header |

---

**Time Budget**: 5 minutes maximum for this validation
**Format Spec**: `docs/FORMAT_SPEC_Step7_Needs_Qualification.md` (if created)
**Template**: `templates/Step7_Needs_Matrix_Template.html`

**Scoring Impact**: Directly informs Desirability dimension (25% weight)
