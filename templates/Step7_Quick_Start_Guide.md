# Step 6 Quick Start Guide
## Needs Qualification Matrix & Analysis Report

**Time Required:** 45-90 minutes
**Prerequisites:** Step 5 (Desirability - Needs/Requesters Analysis) must be complete

---

## What You'll Create

**Two Deliverables:**

1. **Needs Qualification Matrix** (Landscape HTML/PDF)
   - Visual dashboard showing importance vs. satisfaction
   - Color-coded opportunity zones
   - Interview status tracking
   - Used for: Presentations, board meetings, team alignment

2. **Needs Analysis Report** (Portrait HTML/PDF, 9-12 pages)
   - Comprehensive strategic analysis
   - Three-act executive summary
   - 30-day action plan with ownership
   - Decision gates and success criteria
   - Used for: Planning, resource allocation, investor updates

---

## Quick Start Process

### Step 1: Gather Data (10-15 min)

**From Step 5 Desirability Analysis:**
- [ ] Requesters table (6-10 segments)
- [ ] Needs list (10 needs categorized)
- [ ] Existing solutions analysis
- [ ] Interview counts per segment
- [ ] Evidence gaps identified

**Additional Context Needed:**
- [ ] Beta user count and engagement metrics
- [ ] Efficacy measurements (time savings, quality improvements)
- [ ] Partnerships or paying customers
- [ ] Revenue potential estimates per segment
- [ ] Budget available for validation activities
- [ ] Decision-maker roles

---

### Step 2: Rate Each Need/Segment Combination (10-15 min)

For every cell in the matrix, determine:

**Importance (How critical is this need to this segment?):**
- Fundamental: Critical, business fails without it
- Important: Significant need, high priority
- Secondary: Useful but not essential
- None: Not relevant to this segment
- Don't Know: Insufficient data

**Satisfaction (How well do CURRENT solutions meet this need?):**
- Very Well: Current solutions work effectively
- Pretty Much: Current solutions adequate
- Rather Not: Current solutions poor
- Not At All: Current solutions fail completely
- N/A: Used only when importance is "None"
- Don't Know: Insufficient competitive data

**Critical Rule:** When importance is "None", satisfaction MUST be "N/A"

**Validation Rule:** Every rating requires evidence from Step 5. If you can't cite evidence, use "Don't Know".

---

### Step 3: Identify Patterns (5-10 min)

Look for:

**Hot Opportunities (Priority 1):**
- Red + Red (Fundamental + Not At All)
- Multiple segments affected
- High revenue potential
- → These are your highest priorities

**Strong Opportunities (Priority 2):**
- Orange/Red + Yellow/Red (Important + Rather Not/Not At All)
- Clear improvement potential
- → High-value differentiation areas

**Research Gaps:**
- Light gray clusters (Don't Know ratings)
- → Require immediate interview validation

**Pattern Types:**
- Horizontal: Need poorly met across ALL segments (systemic market failure)
- Vertical: Segment has many unmet needs (underserved market)
- Diagonal: Certain needs correlate with certain segments (niche opportunity)

---

### Step 4: Create Needs Matrix (15-20 min)

**Use Template:** `/templates/Step6_Needs_Matrix_Template.html`

**Customization Checklist:**
- [ ] Replace all `[Project Name]` placeholders throughout
- [ ] Update segment column headers with names
- [ ] Add interview counts to each segment header (e.g., "5 Interviews", "0 Interviews", "10+ interviewed")
- [ ] Replace needs in first column (max 60 characters each, numbered 1-10)
- [ ] Fill every cell with TWO stacked indicators:
  - Top indicator: Importance level (use correct CSS class)
  - Bottom indicator: Satisfaction level (use correct CSS class)
- [ ] Update footer with three elements:
  - Evidence description (how matrix was generated)
  - Evidence basis (specific sources)
  - Next step (what validation is needed)
- [ ] Remove validation notice section if matrix is validated through interviews
- [ ] Save as `[project]_needs_matrix_landscape_YYYYMM.html`

**CSS Class Reference:**

```html
<!-- Importance -->
<div class="indicator importance-fundamental">FUNDAMENTAL</div>
<div class="indicator importance-important">IMPORTANT</div>
<div class="indicator importance-secondary">SECONDARY</div>
<div class="indicator importance-none">NONE</div>
<div class="indicator importance-dontknow">DON'T KNOW</div>

<!-- Satisfaction -->
<div class="indicator satisfaction-verywell">VERY WELL</div>
<div class="indicator satisfaction-prettymuch">PRETTY MUCH</div>
<div class="indicator satisfaction-rathernot">RATHER NOT</div>
<div class="indicator satisfaction-notatall">NOT AT ALL</div>
<div class="indicator satisfaction-na">N/A</div>
<div class="indicator satisfaction-dontknow">DON'T KNOW</div>
```

**Quality Check:**
- [ ] All cells have both importance AND satisfaction
- [ ] "None" always paired with "N/A"
- [ ] Two separate indicator boxes per cell (not split)
- [ ] Interview counts accurate
- [ ] Open in browser and verify visual appearance
- [ ] Print to PDF in landscape - text readable at print size

---

### Step 5: Create Analysis Report (30-40 min)

**Use Template:** `/templates/Step6_Analysis_Report_Template.md`

**Section-by-Section Approach:**

#### A. Executive Summary (10 min)
- [ ] Write Three-Act Structure (3-4 lines each):
  - Act I: Where We Are (what's validated)
  - Act II: What's Missing (unvalidated segments, gaps)
  - Act III: What We Recommend (30-day sprint, targets)
- [ ] Create Validation Snapshot callout (proven vs. gaps)
- [ ] Build Current State table (Product, Beachhead, Institutional)
- [ ] Write Decision Ask (who, what, budget, conditions)
- [ ] Create Critical Decision Point callout (validated vs. missing)

#### B. Customer Segment Needs Matrix (5 min)
- [ ] Create visual with three tiers:
  - ✅ PROVEN (validated segments)
  - ⏳ HYPOTHESIS ONLY (unvalidated segments)
  - ⏸ DEFERRED (deprioritized segments)
- [ ] Write insight paragraph about validation gap

#### C. Market Landscape (5 min)
- [ ] Build Problem Definition table (5+ pain points + market size)
- [ ] Create Competitive Positioning table (4+ competitors)
- [ ] Write Key Insight callout if applicable

#### D. Segment Validation & Priorities (5 min)
- [ ] Build full segment table (all segments with status, evidence, revenue, priority)
- [ ] Create Strategic Imperative callout (institutional validation needed)

#### E. Risk Assessment (5 min)
- [ ] Identify 3-5 critical risks with impacts and mitigations
- [ ] List 5-7 red flags (threshold → consequence → action)

#### F. Decision Framework (3 min)
- [ ] Create Current State grid (Validated vs. Missing)
- [ ] Build The Choice comparison table (Option A vs. Option B)
- [ ] Write Recommended Path callout

#### G. 30-Day Action Plan (5 min)
- [ ] Build Action Plan table (Week 1-2, Week 3-4, Ongoing)
- [ ] Write Budget Allocation paragraph with line items
- [ ] Create Decision Gates table (6+ gates with status)
- [ ] Write Success Criteria callout (5 criteria)

#### H. Validation Status Dashboard (3 min)
- [ ] Create three-category framework (Proven, Not Tested, Deferred)
- [ ] Write Final Decision Rule callout

#### I. Footer (2 min)
- [ ] Add data sources
- [ ] Add status summary (X validated, Y require research, Z paying customers)

---

### Step 6: Review & Polish (10 min)

**Matrix Review:**
- [ ] Open in browser - professional appearance?
- [ ] Print to PDF (landscape, background graphics ON)
- [ ] Colors render correctly?
- [ ] Text readable at print size?
- [ ] File size under 50KB?

**Report Review:**
- [ ] Three-Act Structure tells complete story in 30 seconds?
- [ ] All numbers specific (not "many", "some", "significant")?
- [ ] Every action has owner + deadline?
- [ ] Consequences stated for all decision gates?
- [ ] Page count 9-12 pages?
- [ ] No em dashes used?
- [ ] Color coding consistent?
- [ ] Status badges used correctly (✅⏳❌)?

**Executive Scan Test:**
- [ ] Can someone understand situation in 2 minutes?
- [ ] Are decisions clear and forcing function obvious?
- [ ] Would this hold up in board meeting?
- [ ] Is it investor-ready?

---

## File Naming Convention

**Matrix:**
- HTML: `[project_name]_needs_matrix_landscape_YYYYMM.html`
- PDF: `[project_name]_needs_matrix_landscape_YYYYMM.pdf`

**Report:**
- Markdown: `[project_name]_needs_analysis_report_YYYYMM.md`
- HTML: `[project_name]_needs_analysis_report_YYYYMM.html`
- PDF: `[project_name]_needs_analysis_report_YYYYMM.pdf`

**Example:**
- `rayla_ai_needs_matrix_landscape_202411.html`
- `rayla_ai_needs_analysis_report_202411.pdf`

---

## Common Mistakes to Avoid

### Matrix Mistakes

❌ **Split cells or half-and-half coloring**
✅ Use two separate `<div>` elements with full background colors

❌ **Rating satisfaction with your future solution**
✅ Rate CURRENT market solutions only

❌ **Vague need statements** ("Better workflow")
✅ Specific, measurable needs ("Reduce grant writing time by 50%")

❌ **Missing interview counts**
✅ Explicitly state "0 Interviews" or actual count for every segment

❌ **Wrong CSS classes**
✅ Copy exact class names from template

### Report Mistakes

❌ **Weak language** ("might consider", "could explore")
✅ Directive language ("must achieve", "do not proceed until")

❌ **Missing owners/deadlines**
✅ "Product Lead: Quality validation, Sprint end"

❌ **Vague criteria** ("some improvement")
✅ Specific thresholds ("40% beta conversion", "7+ quality rating")

❌ **Too many callout boxes** (15+)
✅ Use 6-8 callouts for critical information only

❌ **No consequences**
✅ "If thresholds missed → REASSESS PRODUCT-MARKET FIT"

---

## Execution Timelines

**Fast (45 min):**
- Data collection: 5 min
- Matrix analysis: 10 min
- Create matrix: 15 min
- Create condensed report: 15 min

**Standard (90 min):**
- Data collection: 15 min
- Matrix analysis: 15 min
- Pattern identification: 10 min
- Create matrix: 20 min
- Create full report: 30 min

**Complete (2-3 hours):**
- Thorough data collection: 30 min
- Deep pattern analysis: 20 min
- Matrix with iterations: 30 min
- Comprehensive report: 60 min
- Review and polish: 30 min

---

## How the Deliverables Work Together

**Matrix = Visual Overview**
- Shows all combinations at a glance
- Identifies opportunity zones
- Reveals patterns
- Tracks validation status

**Report = Strategic Analysis**
- Provides context for patterns
- Translates into recommendations
- Assigns ownership
- Sets success criteria

**Together:**
- Matrix shows WHERE opportunities are
- Report shows WHAT TO DO about them
- Both force honest validation assessment
- Both create accountability

---

## Success Criteria

✅ **Step 6 is complete when:**

1. Needs Matrix created with all cells filled
2. Matrix prints cleanly in landscape
3. Interview counts displayed for all segments
4. Evidence basis documented in footer
5. Analysis Report complete (9-12 pages)
6. Three-Act Structure tells coherent story
7. All actions have owner and deadline
8. Success criteria stated as go/no-go thresholds
9. Red flags identified (5-7 specific)
10. Both deliverables are board-ready

---

## Next Steps After Step 6

**You're ready for Step 7 (Ecosystem Mapping) when you can:**
- Identify priority segments from matrix hot zones
- Explain evidence gaps requiring stakeholder research
- Articulate specific validation activities needed
- Assign clear ownership for next 30 days

**How Step 6 Feeds Forward:**
- Step 7: Priority segments inform stakeholder priorities
- Step 8: Opportunity zones guide partnership strategy
- Final Report: Matrix and report excerpts included

---

## Support Files

**Templates:**
- `/templates/Step6_Needs_Matrix_Template.html` - Complete HTML template
- `/templates/Step6_Analysis_Report_Template.md` - Report structure reference
- `/templates/Step6_Quick_Start_Guide.md` - This guide

**Prompts:**
- `/prompts/step_6_needs_qualification_matrix.md` - Complete methodology

**Examples:**
- (To be added after first implementation)

---

## Troubleshooting

**Problem:** Matrix cells too small/text not readable
**Solution:** Reduce number of segments (max 10) or create two separate matrices

**Problem:** Report exceeds 12 pages
**Solution:** Be more concise, consolidate tables, remove less critical insights

**Problem:** Report under 9 pages
**Solution:** Add detail to risk assessment, expand success metrics, flesh out action plan

**Problem:** Weak or vague language throughout
**Solution:** Review writing standards in main prompt, strengthen all imperatives

**Problem:** Missing ownership or deadlines
**Solution:** Add "[Role]: [Action], [Deadline]" for every action item

**Problem:** No consequences stated
**Solution:** Add "If [threshold] not met → [SPECIFIC CONSEQUENCE]" for all gates

---

## Quick Reference: Color Palette

**Importance:**
- Fundamental: #dc3545 (red)
- Important: #fd7e14 (orange)
- Secondary: #ffc107 (yellow)
- None: #6c757d (gray)
- Don't Know: #e9ecef (light gray)

**Satisfaction:**
- Very Well: #28a745 (green)
- Pretty Much: #20c997 (teal)
- Rather Not: #ffc107 (yellow)
- Not At All: #dc3545 (red)
- N/A: #e9ecef (light gray)
- Don't Know: #e9ecef (light gray)

**Report Callouts:**
- Blue (#0066CC, #E8F4F8): Key insights
- Green (#28A745, #D4EDDA): Success criteria
- Orange (#FF6B35, #FFF3CD): Critical decisions
- Red (#DC3545, #F8D7DA): Risks, imperatives

---

**Ready to execute? Start with data collection from Step 5, then work through each phase systematically. The matrix and report transform analysis into visual clarity and strategic action.**
