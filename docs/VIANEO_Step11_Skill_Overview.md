# Step 11: Features-Needs Matrix | Vianeo Business Model Evaluation

## Skill Overview

**Phase:** Business Model Design (First Step)
**Duration:** 30-45 minutes
**Prerequisites:** Steps 0-10 complete (validated needs, ecosystem analysis, diagnostic)
**Complexity:** Medium (requires strategic thinking + technical execution)

---

## Purpose

Create an interactive visual matrix that maps solution features against validated customer needs, revealing:
- **Strategic fit** between solution and market
- **Coverage gaps** that need addressing
- **MVP boundaries** for focused development
- **Resource priorities** for next phase

This is the bridge from validation (Pre-Incubation) to execution (Business Model Design).

---

## What This Skill Does

### Primary Function
Generates a professional, interactive HTML presentation showing which solution features address which validated customer needs, with opportunity-level color coding and coverage analytics.

### Key Outputs

**1. Interactive HTML Matrix** (`[project]-features-needs-matrix.html`)
- Scrollable table with sticky headers
- Color-coded opportunity levels (High/Medium/Low/Expected/Accessory)
- Checkmarks showing feature-need alignment
- Export to CSV functionality
- Print-optimized layout
- Keyboard shortcuts (Ctrl+E, Ctrl+P)

**2. Strategic Analysis Summary** (`[project]-matrix-analysis.md`)
- Coverage overview with metrics
- Key findings (strengths & gaps)
- Strategic recommendations
- MVP scoping guidance
- Next steps for Step 12+

---

## When to Use This Skill

### Trigger Phrases
- "Create a features-needs matrix for [project]"
- "Map our solution features against validated needs"
- "Generate Step 11 output"
- "Show feature-need alignment for [client]"
- "Build an interactive Vianeo matrix"

### Context Requirements
You must have completed or have access to:
- **Step 7:** Needs Qualification Matrix (10 needs with opportunity levels)
- **Step 4-5:** Solution description (what features exist)
- **Step 10:** Vianeo diagnostic (strategic context)

If these aren't available, you'll need to gather them first.

---

## Workflow Summary

### 6-Phase Process

**Phase 1: Gather Inputs** (5-10 min)
- Retrieve 10 validated needs from Step 7
- Collect 5-10 solution features
- Get project name and context

**Phase 2: Map Coverage** (10-15 min)
- For each feature-need pair, determine if feature addresses need
- Be conservative (only mark clear alignments)
- Document gaps and patterns

**Phase 3: Calculate Metrics** (2-3 min)
- Overall coverage percentage
- High-opportunity coverage
- Critical gap count
- Coverage by opportunity level

**Phase 4: Build HTML** (5-10 min)
- Use Vianeo design system (exact colors, typography, spacing)
- Implement sticky headers and interactive features
- Include export/print functionality
- Add legend footer

**Phase 5: Create Analysis** (5-10 min)
- Write markdown summary
- Identify key insights
- Provide strategic recommendations
- Define next actions

**Phase 6: Quality Check** (5 min)
- Validate data accuracy
- Test interactive features
- Verify strategic coherence

---

## Technical Requirements

### Design Specifications (Non-Negotiable)

**Layout:**
- Max width: 1600px
- Scrollable content area
- Sticky header row (top: 0)
- Sticky first column (left: 0)
- Corner cell sticky both ways (z-index: 20)

**Typography:**
- Font: System fonts (-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif)
- Header title: 16px, 600 weight
- Header subtitle: 10px, 0.9 opacity
- Stats: 20px value, 9px label
- Table: 10px headers, 11px cells
- Need categories: 9px, italic

**Colors:**
```css
Primary: #1a365d, #2c5282
High Opportunity: #0f9d58 (green)
Medium Opportunity: #f4b400 (yellow)
Low Opportunity: #ef6c00 (orange)
Expected: #1a73e8 (blue)
Accessory: #5f6368 (gray)
```

**Interactivity:**
- Export button → CSV download (Ctrl+E)
- Print button → Print dialog (Ctrl+P)
- Hover states on buttons
- Smooth scrolling

### SVG Icon Specifications

**Opportunity indicators:**
- High: Circle r="7" (largest)
- Medium: Circle r="5" (medium)
- Low: Circle r="4" (small)
- Expected: Star outline (path stroke)
- Accessory: Circle r="3" (tiny)

**Button icons:**
- Export: Download arrow (24×24 viewBox)
- Print: Printer (24×24 viewBox)

---

## Strategic Guidance

### Coverage Interpretation

**Healthy Patterns:**
- 40-60% overall coverage (focused solution)
- 100% high-opportunity coverage (all critical needs met)
- 70%+ expected coverage (table stakes included)
- <30% accessory coverage (scope discipline)

**Warning Patterns:**
- <40% coverage + missing high-opportunity needs (gaps)
- >80% coverage with accessory features (over-engineered)
- Scattered checkmarks (unfocused strategy)
- High-opportunity row with zero checkmarks (critical gap)

### MVP Scoping Formula

```
MVP = Features covering (All High + All Expected)
      minus Features only covering (Accessory + Low)
```

**Deferral priorities:**
1. Accessory features (post-launch only)
2. Low-opportunity features (if resources allow)
3. Medium features not critical for differentiation
4. Features requiring significant partnerships

---

## Integration Points

### Backward References (What This Builds On)

**Step 7: Needs Qualification Matrix**
- Source of 10 needs
- Opportunity level classifications
- Importance/satisfaction ratings

**Step 5: Needs & Requesters Analysis**
- Need definitions and context
- Requester segment information

**Step 4: Legitimacy Deep Dive**
- Solution description
- Available resources

**Step 10: Vianeo Diagnostic**
- Strategic recommendations
- Risk areas to address

### Forward References (What This Enables)

**Step 12+: Business Model Design Continuation**
- Technical feasibility for prioritized features
- Resource planning and estimates
- Partnership strategy for gaps
- Go-to-market messaging (focus on covered high needs)
- Product roadmap with phased releases

---

## Success Metrics

### Quantitative Indicators

**Coverage:**
- Overall: 40-80% (optimal range)
- High Opportunity: 100% (all critical needs addressed)
- Expected: 70%+ (table stakes met)
- Accessory: <30% (focused scope)

**Quality Score:**
- Checklist completion: >90%
- Critical sections: 100%
- Stakeholder readiness: Passes review

### Qualitative Indicators

**Product Team:**
- Clear development priorities
- Confident MVP definition
- Understood trade-offs

**Stakeholders:**
- Evidence-based confidence
- Clear value proposition
- Realistic expectations

**Strategic Alignment:**
- Fits with Step 10 diagnostic
- Builds on Step 7 validation
- Enables Step 12+ execution

---

## Troubleshooting Guide

### Problem: Coverage Too Low (<30%)

**Diagnosis:**
- Features too narrow
- Needs too broad
- Fundamental solution-need mismatch

**Solution:**
- Review feature definitions (decompose if too specific)
- Validate needs are from Step 7 (not new requirements)
- Consider if this is wrong solution for these needs

### Problem: Coverage Too High (>85%)

**Diagnosis:**
- Features too broad
- Over-engineering
- Needs not distinct

**Solution:**
- Break features into specific capabilities
- Apply MVP scoping discipline
- Consolidate overlapping needs

### Problem: Matrix Won't Generate

**Likely Causes:**
- Missing CSS content
- JavaScript syntax error
- Invalid HTML structure

**Solution:**
- Copy complete CSS from template
- Validate JavaScript in console
- Check HTML against template structure

### Problem: Export Not Working

**Likely Causes:**
- Event listener not attached
- CSV generation logic error
- Filename has spaces

**Solution:**
- Verify getElementById('exportBtn') finds button
- Test CSV generation with simple data
- Use hyphens in filename, not spaces

### Problem: Sticky Headers Not Sticky

**Likely Causes:**
- position: sticky not applied
- z-index hierarchy wrong
- Parent container overflow: hidden

**Solution:**
- Verify CSS: position: sticky; top: 0; or left: 0;
- Check z-index: corner(20) > top(10) > left(5)
- Ensure parent has overflow: auto, not hidden

---

## Quality Standards

### Delivery Criteria (Must Meet All)

**Data Integrity:**
- All 10 needs from Step 7 included correctly
- Opportunity classifications accurate
- Checkmarks only where features genuinely address needs
- Coverage metrics calculated correctly

**Professional Design:**
- Exact Vianeo color palette
- Sticky headers functional
- Export and print working
- Print layout optimized for landscape

**Strategic Value:**
- Clear insights about coverage and gaps
- Actionable recommendations
- MVP scoping guidance
- Next steps defined

**Technical Excellence:**
- Valid HTML5
- No console errors
- Responsive design
- Cross-browser compatible

### Common Pitfalls to Avoid

1. **Over-marking coverage**: Be conservative with checkmarks
2. **Missing opportunity classifications**: Every need needs a color-coded level
3. **Vague feature names**: "Mobile app" is too generic, "Barcode scanning via camera" is specific
4. **Ignoring gaps**: Critical gaps are valuable insights, not failures
5. **Wrong metrics**: Double-check coverage calculations
6. **Static headers**: Headers must be sticky for usability
7. **No JavaScript**: Export and print are required, not optional
8. **Missing analysis**: HTML alone isn't enough, needs strategic summary

---

## Related Documentation

### Primary References
- `step_11_features_needs_matrix.md` - Generation prompt
- `VIANEO_Step11_Implementation_Guide.md` - Detailed workflow
- `VIANEO_Step11_Reference_Guide.md` - Methodology and interpretation
- `VIANEO_Step11_Quality_Checklist.md` - Validation criteria
- `VIANEO_Step11_Quick_Reference.md` - Quick lookup

### Templates
- `Step11_FeaturesNeeds_Matrix_Template.html` - HTML template
- `Step11_FeaturesNeeds_Analysis_Template.md` - Analysis template

### Examples
- `Step11_Example_MarineData_Matrix.html` - Working example
- `Step11_Example_MarineData_Analysis.md` - Analysis example

### Context Documents
- Step 7 Output: Source of validated needs
- Step 10 Output: Strategic diagnostic context

---

## Key Takeaways

**What This Skill Enables:**
1. Evidence-based product decisions
2. Clear MVP boundaries
3. Stakeholder-ready presentations
4. Strategic resource allocation
5. Foundation for next development phase

**Critical Success Factors:**
1. Conservative checkmark marking (accuracy over optimism)
2. Complete high-opportunity coverage (non-negotiable)
3. Professional design quality (stakeholder-ready)
4. Strategic interpretation (insights, not just data)
5. Actionable next steps (enables execution)

**Remember:**
- This bridges validation to execution
- Gaps are insights, not failures
- Focus beats comprehensive coverage
- Visual tells the strategic story
- Quality over speed matters here

---

*Step 11 | Vianeo Business Model Evaluation Framework*
*Phase: Business Model Design*
*Version: 2.0*

---

## Quick Reference Card

**Duration:** 30-45 minutes
**Prerequisites:** Steps 0-10 complete
**Inputs:** 10 needs + 5-10 features
**Outputs:** HTML matrix + MD analysis
**Key Metric:** High-opportunity coverage
**Success Threshold:** All critical needs addressed
**Next Step:** Technical feasibility assessment
