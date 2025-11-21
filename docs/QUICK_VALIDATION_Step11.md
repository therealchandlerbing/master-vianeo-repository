# Quick Validation Guide: Step 11 - Features-Needs Matrix

**Purpose**: Fast 5-minute quality check before delivery
**Pass Criteria**: All ✓ boxes must be checked

---

## 1. STRUCTURE (5 items)

- [ ] Interactive HTML matrix file created
- [ ] Strategic analysis markdown file created
- [ ] Both files reference same project/date
- [ ] HTML header includes inline stats
- [ ] Markdown includes all required sections

## 2. HTML MATRIX SPECS (7 items)

- [ ] Table structure: Features as columns, Needs as rows
- [ ] Sticky headers functional (top + left)
- [ ] All 10 needs from Step 7 included
- [ ] Features count: 5-10 (not more, not less)
- [ ] Checkmarks (✓) indicate coverage
- [ ] Color-coded opportunity levels (5 colors)
- [ ] Legend footer with all 5 opportunity levels

## 3. INTERACTIVE FEATURES (3 items)

- [ ] Export to CSV works (Ctrl+E or button)
- [ ] Print layout works (Ctrl+P or button)
- [ ] Buttons visible and functional

## 4. COVERAGE METRICS (6 items)

- [ ] Overall coverage calculated: (Checkmarks / (Features × Needs)) × 100
- [ ] High-opportunity coverage: X/Y format
- [ ] Coverage by opportunity level table included
- [ ] Metrics displayed in HTML header
- [ ] Metrics match between HTML and markdown
- [ ] Coverage targets noted (40-80% overall, 100% high-opportunity)

## 5. CHECKMARK VALIDATION (4 items)

**Conservative marking philosophy:**

- [ ] Checkmarks only when feature DIRECTLY solves need
- [ ] No "stretch" connections marked
- [ ] Coverage not inflated (≤85% overall)
- [ ] High-opportunity needs have coverage

## 6. STRATEGIC ANALYSIS (3 items)

- [ ] Coverage overview section complete
- [ ] Key findings (strengths + gaps) documented
- [ ] MVP scoping guidance provided

---

## QUICK DECISION MATRIX

| Checks Passed | Decision |
|--------------|----------|
| 28/28 (100%) | ✅ **APPROVED** - Deliver immediately |
| 25-27 (89-96%) | ⚠️ **FIX MINOR** - Quick corrections needed |
| 22-24 (79-86%) | ❌ **REVISE** - Significant issues, rework required |
| <22 (<79%) | 🛑 **REJECT** - Does not meet minimum standards |

---

## FASTEST CHECKS (Do These First)

**30-second scan:**
1. Open HTML → Ctrl+E → verify CSV downloads
2. Count needs in rows → must be exactly 10
3. Count features in columns → must be 5-10

**If any fail → Stop and fix before full review**

---

## INSTANT RED FLAGS

**Stop immediately if you see:**
- ❌ Export/Print buttons don't work
- ❌ Only 8 needs (missing 2 from Step 7)
- ❌ 15 features (too many, scope creep)
- ❌ Overall coverage >85% (over-marked)
- ❌ High-opportunity needs with 0% coverage
- ❌ Sticky headers not working (scroll test fails)

---

## COMMON FIXES (2-minute corrections)

**Export not working?**
```javascript
// Verify CSV export function exists
function exportToCSV() {
  // Should convert table to CSV format
  // Should trigger download
}
```
- Check function is defined
- Check button onclick handler
- Test Ctrl+E keyboard shortcut

**Print layout broken?**
```css
@media print {
  @page { size: landscape; }
  /* Should preserve colors and layout */
}
```
- Verify @media print rules
- Check landscape orientation
- Test color preservation

**Coverage too high (>85%)?**
- Review each checkmark critically
- Remove "stretch" connections
- Apply test: "Does this feature DIRECTLY solve the need?"
- Keep only strong connections

**Missing needs from Step 7?**
- Compare to Step 7 output
- All 10 needs must be included
- Same opportunity classifications
- Same need statements (may shorten if >60 chars)

---

## COVERAGE TARGET REFERENCE

| Opportunity Level | Target Coverage | Interpretation |
|-------------------|-----------------|----------------|
| **High Opportunity** | **100%** | MUST address all high-opportunity needs |
| **Medium Opportunity** | 70-100% | SHOULD address most |
| **Low Opportunity** | 30-70% | CONSIDER if resources allow |
| **Expected** | **100%** | Table stakes, must include |
| **Accessory** | 0-30% | DEFER until post-launch |

**Overall Target:** 40-80% (focused solution, not feature bloat)

**If below 40%** → Too narrow, may miss critical needs
**If above 80%** → Over-marked or too broad, check conservative marking

---

## OPPORTUNITY LEVEL COLORS

**Visual reference (must match in HTML):**

| Level | Color | Hex Code | Indicator Size |
|-------|-------|----------|----------------|
| High | Green | #0f9d58 | Circle r="7" |
| Medium | Yellow | #f4b400 | Circle r="5" |
| Low | Orange | #ef6c00 | Circle r="4" |
| Expected | Blue | #1a73e8 | Star outline |
| Accessory | Gray | #5f6368 | Circle r="3" |

**Verify:** HTML colors match this table exactly

---

## MVP SCOPING FORMULA

**From coverage analysis:**

```
MVP = Features covering (All High + All Expected)
      minus Features only covering (Low + Accessory)
```

**Test:**
1. List features that cover ≥1 high-opportunity need
2. Add features that cover ≥1 expected need
3. Remove features that ONLY cover low/accessory needs
4. Result = MVP feature set

**Markdown analysis should provide this breakdown explicitly**

---

## INTERACTIVE FEATURE TEST

**Export to CSV (Ctrl+E):**
1. Click Export button or press Ctrl+E
2. CSV file should download immediately
3. Open CSV → verify all data present
4. Check: headers, need names, checkmarks, opportunity levels

**Print (Ctrl+P):**
1. Click Print button or press Ctrl+P
2. Print preview should open
3. Verify: Landscape orientation, colors preserved, all text readable
4. Check: No content cut off, legend visible

**Sticky Headers:**
1. Scroll down → column headers should stick to top
2. Scroll right → first column (needs) should stick to left
3. Corner cell should have highest z-index (always visible)

---

## FILE NAMING CONVENTION

**Standard format:**
- HTML: `[project-name]-features-needs-matrix.html`
- Markdown: `[project-name]-matrix-analysis.md`

**Examples:**
- `techedu-features-needs-matrix.html`
- `techedu-matrix-analysis.md`

**Rules:**
- Project name: lowercase, hyphens (not spaces or underscores)
- No date in filename (Step 11 is iteration-friendly)
- Descriptive suffixes mandatory

---

## STRATEGIC ANALYSIS SECTIONS (Required)

**Markdown must include:**

1. **Coverage Overview**
   - Total features, total needs
   - Overall coverage %
   - Coverage by opportunity level

2. **Key Findings**
   - Top 3 strengths (well-covered areas)
   - Top 3 critical gaps (high-opportunity needs with no coverage)

3. **Strategic Recommendations**
   - Priority development (features to build for gaps)
   - Feature optimization (features to simplify/defer)

4. **MVP Definition**
   - Must-have features (based on formula)
   - Defer to post-launch features

5. **Next Steps**
   - What follows Step 11 (technical feasibility, resources, GTM)

---

**Time Budget**: 5 minutes maximum for this validation
**Format Spec**: `docs/FORMAT_SPEC_Step11_Features_Needs_Matrix.md`

**Note**: Step 11 bridges validation (Steps 0-10) to execution (MVP development)
