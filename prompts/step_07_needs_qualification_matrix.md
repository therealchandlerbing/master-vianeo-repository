# STEP 7: Needs Qualification Matrix & Analysis Report

**Time Required:** 45-90 minutes
**Output:** TWO deliverables - (1) Needs Qualification Matrix (Landscape HTML/PDF), (2) Comprehensive Analysis Report (Portrait HTML/PDF, 9-12 pages)
**Prerequisite:** Step 5 Desirability - Needs/Requesters Analysis must be complete

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 7: Needs Qualification Matrix from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_07_needs_qualification_matrix.md`.

**Required Attachments:**
- Screenshot of the Needs/Requesters table from the Vianeo platform

**Entity Guardrails:**

> **CRITICAL: Do NOT create any new needs or requesters.**
>
> - Every row must correspond to a need in the attached table
> - Every column must correspond to a requester in the attached table
> - Copy need statements EXACTLY as shown (60-char limit preserved)
> - Copy requester names EXACTLY as shown
> - If the screenshot shows 10 needs and 6 requesters, your matrix has EXACTLY 10 rows and 6 columns
> - Do NOT paraphrase, abbreviate, or combine needs
> - Do NOT add "inferred" or "implied" needs

---

## Overview

Step 7 transforms the Needs/Requesters analysis from Step 5 into two powerful visual and strategic deliverables:

1. **Needs Qualification Matrix** - Visual dashboard showing importance vs. satisfaction across all segment/need combinations
2. **Needs Analysis Report** - Comprehensive 9-12 page strategic analysis with actionable recommendations

**Purpose:** These deliverables identify market opportunities where high-importance needs have low satisfaction with existing solutions, providing clear prioritization for product development and validation activities.

---

## Why This Step Matters

The Needs Qualification Matrix and Analysis Report serve different but complementary purposes:

**Matrix (Visual Overview):**
- Shows all segment/need combinations at a glance
- Identifies opportunity zones (Fundamental + Not At All = priority)
- Reveals patterns across segments (horizontal, vertical, diagonal)
- Tracks validation status via interview counts
- Used in: Presentations, board meetings, team alignment

**Report (Strategic Analysis):**
- Provides context and evidence for matrix patterns
- Translates insights into actionable recommendations
- Assigns ownership and deadlines
- Sets success criteria and decision gates
- Used in: Planning, resource allocation, investor updates

Together, they force honest assessment of validation status and create clear accountability for next steps.

---

## Instructions for AI Assistant

Using output from Step 5, create a Needs Qualification Matrix. Import all requester names and need statements exactly as written—do not paraphrase. Rate Importance and Satisfaction for each combination using the scales below. Generate two deliverables: HTML Matrix (landscape, color-coded) and Analysis Report (9-12 pages).

---

## Required Inputs

**From Step 5 (Desirability Analysis):**
- Requesters table (6-10 segments with interview status)
- Needs analysis (10 needs: Tasks, Pains, Expectations)
- Existing solutions analysis (5-6 alternatives with limitations)
- Evidence requirements and validation gaps
- Competitive positioning insights

**From Step 4 (Legitimacy Deep Dive):**
- Problem statement and validation
- Field of application
- Team capabilities and resources

**From Step 3 (Market Maturity 29Q):**
- Desirability dimension scores
- Evidence citations for customer validation

**From Step 0 (Executive Brief):**
- Project name
- Target market (B4)
- Traction/validation (B6)
- Team/resources (B7)

**Additional Research Data:**
- Beta user counts and engagement metrics
- Efficacy measurements (time savings, quality improvements, outcomes)
- Partnerships or paying customers
- Revenue potential estimates per segment
- Budget constraints for validation activities
- Risk identification from discovery

---

## CRITICAL: Data Dependencies

This step REQUIRES exact output from Step 5 (Needs/Requesters Analysis).

### Data to Pull from Step 5:

**Requester Segments** (become column headers):
- Copy ALL requester names exactly as written
- Include interview counts for reliability indicators
- Do NOT paraphrase or reword

**Need Statements** (become row labels):
- Copy ALL need statements verbatim
- Maintain exact wording (60-char limit preserved)
- Do NOT shorten, rephrase, or combine

### Output Format

**HTML Matrix Structure**:
- Title: "[Project Name] - Needs Qualification Matrix"
- Subtitle: "Visual Assessment of Importance & Satisfaction Across Requester Segments"
- Pre-validation warning banner (if no interviews conducted)
- Legend: Importance levels (Fundamental/Important/Secondary/None/Don't Know)
- Legend: Satisfaction levels (Very Well/Pretty Much/Rather Not/Not At All/Don't Know)

**Matrix Cells**: Each cell shows two values:
- Top: Importance level (color-coded)
- Bottom: Satisfaction level (color-coded)

**Column Headers**: Requester name + interview count

### Validation Check
- [ ] All requester names match Step 5 exactly
- [ ] All need statements match Step 5 exactly
- [ ] Interview counts match Step 5
- [ ] Number of columns = number of requesters in Step 5
- [ ] Number of rows = number of needs in Step 5

---

## Output 1: Needs Qualification Matrix

### Specifications

**Format:**
- Orientation: US Letter Landscape (11" × 8.5")
- Background: Gradient (purple to blue: #667eea to #764ba2)
- Container: White dashboard with rounded corners
- Typography: System fonts (Apple/BlinkMacSystemFont/Segoe UI/Roboto)

**Required Sections:**
1. Header with project name + "Needs Qualification Matrix"
2. Subtitle: "Visual Assessment of Importance & Satisfaction Across Requester Segments"
3. Validation notice (if pre-validation): "⚠ PRE-VALIDATION HYPOTHESIS - REQUIRES SYSTEMATIC INTERVIEW VALIDATION"
4. Two legend sections side-by-side (Importance Level | Satisfaction Level)
5. Matrix table with color-coded cells
6. Footer with project info, evidence basis, next steps

### Matrix Structure

**Rows:** Needs (10-12 from Step 5)
- Each need statement (max 60 characters)
- Numbered 1-12
- Left column with light gray background

**Columns:** Requester Segments (6-9 from Step 5)
- Segment name in header
- Interview status badge (e.g., "5 Interviews", "0 Interviews", "10+ interviewed")
- Each column represents a requester role

**Cells:** Two stacked indicator boxes
```
┌─────────────────┐
│  [FUNDAMENTAL]  │  ← Top: Importance (colored background)
│                 │
│  [NOT AT ALL]   │  ← Bottom: Satisfaction (colored background)
└─────────────────┘
```

### Rating Scales

**Importance Levels (How critical is this need?):**
- **Fundamental** (#dc3545 red): Critical, non-negotiable need. Business fails without this.
- **Important** (#fd7e14 orange): Significant need, high priority. Major impact on success.
- **Secondary** (#ffc107 yellow): Useful but not essential. Nice-to-have.
- **None** (#6c757d gray): Not relevant to this segment at all.
- **Don't Know** (#e9ecef light gray): Insufficient data to determine importance.

**Satisfaction Levels (How well do CURRENT solutions meet this need?):**
- **Very Well** (#28a745 green): Current solutions meet need effectively. No major gaps.
- **Pretty Much** (#20c997 teal): Current solutions adequately address need. Minor gaps.
- **Rather Not** (#ffc107 yellow): Current solutions poorly address need. Significant gaps.
- **Not At All** (#dc3545 red): Current solutions fail to meet need. Complete gap.
- **N/A** (#e9ecef light gray): Used when importance is "None" (need doesn't apply).
- **Don't Know** (#e9ecef light gray): Insufficient data to determine satisfaction.

**Critical Rule:** When importance is "None", satisfaction MUST be "N/A"

### Color Strategy

The intentional color overlap creates visual opportunity identification:
- **Red + Red** (Fundamental + Not At All) = Critical opportunity zone
- **Orange/Red + Yellow/Red** (Important + Rather Not/Not At All) = Strong opportunity
- **Light Gray clusters** (Don't Know) = Research gaps requiring immediate attention
- **Green areas** (Very Well) = Lower priority for innovation

### Footer Content

**Three Required Elements:**
1. **Title Line:** "[Project Name] System | Vianeo Business Validation Sprint"

2. **Evidence Description:** How the matrix was generated
   - Example: "Pre-validation hypothesis matrix generated from strategic analysis, policy research, technical gap assessment, and institutional knowledge (30+ years materials science)."

3. **Evidence Basis:** Specific sources of confidence
   - Example: "Brazil's complete import dependence, nanostructured microsphere technical gaps, INCT funding validation, strategic sector analysis."

4. **Next Step:** What action needs to happen
   - Example: "Systematic interview program (20-30 per segment) to validate or revise these hypotheses before pilot plant investment decision."

### File Naming

- HTML: `[project_name]_needs_matrix_landscape_YYYYMM.html`
- PDF: `[project_name]_needs_matrix_landscape_YYYYMM.pdf`

---

## Output 2: Needs Analysis Report

### Specifications

**Format:**
- Orientation: US Letter Portrait (8.5" × 11")
- Margins: 0.75" all sides
- Font: Arial throughout
- Base font size: 10.5pt body, 9.5pt tables
- Line height: 1.4
- Target length: 9-12 pages
- Footer: "Company Name | Vianeo Needs Qualification Validation | Page X" (9pt, gray)

**Color Palette (Use Consistently):**
- Primary Blue: #0066CC (headings, borders, key insights)
- Accent Orange: #FF6B35 (warnings, critical decisions)
- Success Green: #28A745 (validated items, success criteria)
- Warning Yellow: #FFC107 (in-progress items)
- Critical Red: #DC3545 (risks, missing items, red flags)
- Light Blue: #E8F4F8 (callout backgrounds)
- Light Gray: #F5F5F5 (table row shading)
- Medium Gray: #CCCCCC (borders)
- Dark Gray: #333333 (body text)

### Required Sections (9 Sections + Footer)

#### 1. Executive Summary

**A. Three-Act Structure** (3-4 lines each)
- **Act I: Where We Are Now** - What's validated (metrics, segments, partnerships)
- **Act II: What's Missing** - Unvalidated segments with revenue impact, critical gaps
- **Act III: What We Recommend** - Specific action (30-day sprint with conversion targets)

**B. Validation Snapshot Callout** (Light blue box)
- Product Efficacy (Proven): Key metrics with numbers
- Critical Gaps: What's missing (highlight zero revenue in yellow)

**C. Current State Table**
- 3 rows: Product, Beachhead, Institutional
- 3 columns: Dimension, Current State, Status
- Status badges: ✅ Validated, ⚠ Partial, ✗ Not tested

**D. Decision Ask** (1-2 paragraphs)
- What decision is required
- Budget allocation ($X-Y, X% of funding)
- Who owns it (specific role)
- Conditions for proceeding

**E. Critical Decision Point Callout** (Orange box)
- What's validated vs. missing
- Revenue impact (%)
- Risk of proceeding without validation
- Specific recommendation (30-day sprint)

#### 2. Customer Segment Needs Matrix

Visual representation with 3 rows:
- ✓ **PROVEN** (Revenue Level) - Green tags for validated segments
- ⏳ **HYPOTHESIS ONLY** (Revenue Level) - Yellow tags for unvalidated segments
- ⏸ **DEFERRED** (Timeframe) - Gray tags for deprioritized segments

**Required:** Insight paragraph stating the gap between validation and revenue potential

#### 3. Market Landscape & Opportunity

**A. Problem Definition Table** (5+ rows)
- Pain Point | Impact & Market Size
- Last row (Market Size): Light blue background, bold figures

**B. Competitive Positioning**
- Opening statement: "[White space/gap]: No competitor combines [differentiators]"
- Competitive Table (4+ competitors): Name/pricing | Limitations | Client's Advantage
- Client advantage column: Light blue background

**C. Key Insight Callout** (Green box, if applicable)
- Format: "💡 KEY INSIGHT: [Title]"
- 3 sentences: State insight, provide evidence, explain how it addresses opportunity

#### 4. Segment Validation & Priorities

**Full Segment Table** (5 columns minimum)
- Segment | Status | Evidence | Revenue | 30-Day Priority
- Status badges: ✓ PROVEN (green), ⏳ NOT TESTED (yellow)
- Priority levels: Critical, High, Monitor, Defer

**Order:**
1. All validated segments first (alphabetically)
2. All unvalidated segments second (by revenue potential, highest first)

**Required Callout:** "⚠ STRATEGIC IMPERATIVE" (red box)
- How many interviews needed (15-20 per segment)
- Which segments specifically
- % of revenue they represent
- What must be tested (procurement, compliance, pricing, integrations, decision hierarchies)

#### 5. Risk Assessment

**Critical Risks Table** (3-5 rows)
- Risk | Impact | Mitigation (30-Day Sprint)
- First row background: Light red (#F8D7DA)
- Risk name: Bold, red color
- Mitigation: Bold the action verb

**Required Risks for Validation Stage:**
1. Quality Threshold Risk (CRITICAL) - AI/product doesn't meet professional standards
2. Compliance/Safety Risk (CRITICAL, if applicable) - Regulatory or safety violations
3. Pricing Validation Risk (HIGH) - Zero paying customers, willingness to pay unknown
4. Channel Conflict Risk (MEDIUM, if applicable) - Partners perceive as threat
5. Data Privacy & Security Risk (MEDIUM, if applicable) - Sensitive data exposure

**Red Flags Section:** Bulleted list (5-7 items)
- Format: "[Metric/threshold] [consequence] → [action]"
- Example: "Less than 20% beta conversion after pricing launch → pause, reassess"

#### 6. Decision Framework

**A. Current State** (Grid Layout)
- Two-box side-by-side comparison
- Left box (Green border): ✓ VALIDATED - What's proven
- Right box (Red border): ⚠ MISSING - What's missing

**B. The Choice** (Option Comparison Table)
- Two-column table: Option A vs. Option B
- Include: PROS, RISKS, TIMELINE for each
- Recommended option: Light blue background, checkmark ✓

**C. Recommended Path Callout** (Blue box)
- Bold headline: "Option B with [specific approach]"
- How it works (one sentence)
- What this validates (numbered list with 4 items)

#### 7. 30-Day Action Plan

**A. Action Plan Table** (3 rows)
- Timeframe | Activities | Output
- Week 1-2: Institutional Research (15-20 interviews)
- Week 3-4: Beta Conversion (launch pricing, target X% conversion)
- Ongoing: Quality Validation (blind testing, competitive comparison)
- Output column: Light blue background, bold deliverable names

**B. Budget Allocation** (Paragraph)
- Format: "Budget Allocation ($X-Y): [Line item] ($X), [item] ($X), ..."
- Required line items: Interviews, competitive subscriptions, testing compensation, researchers, advisory stipends

**C. Decision Gates Table** (6+ rows)
- Gate | Current | Target | Owner | Deadline
- Status badges: ✅ Achieved, ⏳ Testing, ❌ Not started

**Required Gates:**
1. Beta engagement (should be ✅)
2. Efficacy metrics (should be ✅)
3. Quality validation (⏳ → target rating)
4. Pricing validation (❌ → target % conversion)
5. B2B segment validation (❌ → target # interviews)
6. Compliance validation (⏳ → 0 disqualifications)

**D. Success Criteria Callout** (Green box)
- Format: "✓ SUCCESS CRITERIA → PROCEED TO MVP"
- Bulleted list (5 items in bold)
- Red bold text at end: "IF THRESHOLDS MISSED → REASSESS PRODUCT-MARKET FIT"

#### 8. Validation Status Dashboard

**Three-Category Framework:**
- ✓ **PROVEN** (Ongoing Engagement) - Green row, segments with evidence
- ⏳ **NOT TESTED** (Sprint Priority) - Yellow row, segments needing validation
- ⏸ **DEFERRED** (6-12 Months) - Gray row, deprioritized segments

**Each category includes:**
- Segment names separated by pipes (|)
- Owner role (Product Lead, Biz Dev Lead, etc.)
- Specific action with timeframe
- Rationale for deferred items

**Final Decision Rule Callout** (Red box)
- Header: "FINAL DECISION RULE"
- "Do not lock MVP scope or major build budget until:"
- Numbered conditions with AND between them
- Consequences for failure
- Trigger language for red flags

#### 9. Footer

Format:
```
[Horizontal line: 2pt, Primary Blue]

[Centered, 9pt gray text]
[Bold, 10pt, Primary Blue] Framework Name

[Bold] Data Sources: [source 1] | [source 2] | [source 3] | [source 4]

[Bold] Status: [green] X segments validated | [yellow] X require research | [red] 0 paying customers
```

### Writing Standards

**Use Directive Language:**
- ✅ "Product Lead must achieve 7+ rating before MVP launch."
- ✅ "Do not proceed until 40% beta conversion validated."
- ❌ "It might be advisable to validate quality."

**Be Specific with Numbers:**
- ✅ "50+ active beta users", "60% time reduction measured"
- ❌ "Many users engaged", "Significant time savings"

**Assign Clear Ownership:**
- ✅ "Product Lead: Quality validation, Sprint end"
- ❌ "Team should validate quality"

**State Consequences:**
- ✅ "If conversion below 40% → REASSESS PRICING & VALUE PROP"
- ❌ "If thresholds not met, reconsider approach"

### File Naming

- Markdown: `[project_name]_needs_analysis_report_YYYYMM.md`
- HTML: `[project_name]_needs_analysis_report_YYYYMM.html`
- PDF: `[project_name]_needs_analysis_report_YYYYMM.pdf`

---

## Execution Process

### Phase 1: Data Collection (10-15 min)

**Gather from Step 5:**
- Complete requesters table with interview counts
- Full needs list (10 needs with categorization)
- Existing solutions analysis
- Evidence gaps identified

**Gather Additional Context:**
- Beta user count and engagement data
- Efficacy metrics (time reduction, quality improvement, documented outcomes)
- Partnerships or paying customers (even if $0)
- Revenue potential per segment ($X/mo or $XK/yr)
- Budget constraints for validation activities
- Risk identification from discovery calls
- Decision-maker names/roles

### Phase 2: Analyze Matrix Data (10-15 min)

**For Each Need/Segment Combination, Determine:**

**Importance Level:**
- Based on Step 5 requesters analysis
- Consider: Is this need critical, significant, useful, or irrelevant to this segment?
- Use "Don't Know" honestly when lacking data
- Mark "None" only when truly not applicable

**Satisfaction Level:**
- Based on Step 5 existing solutions analysis
- Rate CURRENT market solutions, not your future product
- Consider: How well do existing solutions meet this need TODAY?
- Use "Don't Know" when insufficient competitive data
- Use "N/A" only when importance is "None"

**Validation Rule:** Every rating requires evidence from Step 5 or research. If you can't cite evidence, use "Don't Know" and flag for research.

### Phase 3: Identify Patterns (5-10 min)

**Hot Opportunities (Priority 1):**
- Importance: Fundamental
- Satisfaction: Not At All or Rather Not
- Multiple segments affected
- High revenue potential

**Strong Opportunities (Priority 2):**
- Importance: Important
- Satisfaction: Not At All or Rather Not
- Clear improvement potential

**Research Gaps:**
- Any "Don't Know" ratings
- Clusters of uncertainty
- Require immediate interview validation

**Pattern Types:**
- **Horizontal:** Need poorly met across ALL segments (systemic market failure)
- **Vertical:** Segment has many unmet needs (underserved market)
- **Diagonal:** Correlation between certain needs and segments (niche opportunity)

### Phase 4: Create Matrix HTML (15-20 min)

**Use Template:** `/templates/Step6_Needs_Matrix_Template.html`

**Customization Steps:**
1. Replace all [Project Name] placeholders
2. Update segment column headers with names and interview counts
3. Replace needs in first column (max 60 chars each)
4. Fill every cell with two stacked indicators (importance + satisfaction)
5. Update footer with evidence basis and next steps
6. Remove validation notice if matrix is validated through interviews
7. Save as `[project]_needs_matrix_landscape_YYYYMM.html`

**Quality Check:**
- All cells have both importance AND satisfaction
- "None" always paired with "N/A"
- Interview counts accurate
- Two separate indicator boxes per cell (not split)
- Prints cleanly in landscape

### Phase 5: Create Analysis Report (30-40 min)

**Section-by-Section Approach:**

1. **Executive Summary** (10 min)
   - Write Three-Act Structure first
   - Create Validation Snapshot callout
   - Build Current State table
   - Write Decision Ask
   - Create Critical Decision Point callout

2. **Customer Segment Needs Matrix** (5 min)
   - Create visual with tags (✓ PROVEN, ⏳ HYPOTHESIS, ⏸ DEFERRED)
   - Write insight paragraph about validation gaps

3. **Market Landscape** (5 min)
   - Build Problem Definition table
   - Create Competitive Positioning table
   - Write Key Insight callout (if applicable)

4. **Segment Validation & Priorities** (5 min)
   - Build full segment table with status badges
   - Create Strategic Imperative callout

5. **Risk Assessment** (5 min)
   - Identify 3-5 critical risks
   - List 5-7 red flags

6. **Decision Framework** (3 min)
   - Create Current State grid
   - Build The Choice comparison table
   - Write Recommended Path callout

7. **30-Day Action Plan** (5 min)
   - Build Action Plan table (Week 1-2, Week 3-4, Ongoing)
   - Write Budget Allocation paragraph
   - Create Decision Gates table
   - Write Success Criteria callout

8. **Validation Status Dashboard** (3 min)
   - Create three-category framework
   - Write Final Decision Rule callout

9. **Footer** (2 min)
   - Add data sources
   - Add status summary

### Phase 6: Review and Polish (10 min)

**Matrix Review:**
- Open in browser, check visual appearance
- Print to PDF, verify landscape layout
- Confirm colors render correctly
- Check text readability at print size

**Report Review:**
- Read Three-Act Structure - complete story in 30 seconds?
- Verify all numbers are specific (not "many", "some")
- Confirm every action has owner and deadline
- Check consequences stated for all decision gates
- Count pages (should be 9-12)
- Verify no em dashes used
- Check color coding consistency

**Executive Scan Test:**
- Can someone understand situation in 2 minutes?
- Are decisions clear and forcing function obvious?
- Would this hold up in board meeting?
- Is it investor-ready?

---

## Quality Checklist

### Matrix Quality

**Visual Excellence:**
- [ ] Professional appearance (board-ready)
- [ ] Colors distinct and meaningful
- [ ] Text readable at print size
- [ ] Two separate indicator boxes per cell
- [ ] Landscape orientation optimized
- [ ] Prints cleanly with background graphics

**Data Integrity:**
- [ ] Every cell has both importance and satisfaction
- [ ] "None" always paired with "N/A"
- [ ] Interview counts accurate for all segments
- [ ] Need statements under 60 characters
- [ ] Evidence basis specific and credible

**Technical Quality:**
- [ ] Valid HTML5
- [ ] No external dependencies
- [ ] Print CSS optimized (@page rules)
- [ ] File size under 50KB
- [ ] Converts cleanly to PDF

### Report Quality

**Content Completeness:**
- [ ] All 9 sections present
- [ ] Three-Act Structure clear
- [ ] All numbers quantified
- [ ] Every action has owner + deadline
- [ ] 6-8 callout boxes strategically placed
- [ ] Budget detailed by line item

**Visual Design:**
- [ ] Color coding consistent
- [ ] Status badges used correctly (✅⏳❌)
- [ ] Tables properly formatted
- [ ] No em dashes anywhere
- [ ] Page count 9-12 pages

**Decision Clarity:**
- [ ] Decision ask states requirements
- [ ] Success criteria as go/no-go thresholds
- [ ] Red flags listed (5-7 specific)
- [ ] Final decision rule uses strong language
- [ ] Consequences stated for all gates

**Professional Polish:**
- [ ] McKinsey/BCG quality output
- [ ] Executive can scan in 2 minutes
- [ ] File size under 100KB
- [ ] No awkward page breaks

---

## Integration with Vianeo Framework

**How Step 6 Fits:**

**Feeds Into:**
- Step 7: Ecosystem Mapping (priority segments inform stakeholder priorities)
- Step 8: Network Visualization (opportunity zones guide partnership strategy)
- Final Committee Report (matrix and report excerpts)

**Builds Upon:**
- Step 5: Needs/Requesters Analysis (provides all base data)
- Step 4: Legitimacy Deep Dive (problem context)
- Step 3: Market Maturity 29Q (desirability scores)
- Step 0: Executive Brief (project fundamentals)

**Decision Impact:**
- Forces honest assessment of validation status
- Identifies specific research gaps requiring investment
- Provides clear accountability for next steps
- Sets measurable success criteria for validation activities

---

## Common Mistakes to Avoid

### Matrix Mistakes

❌ **Split cells or half-and-half coloring**
✅ Use two separate div elements with full background colors

❌ **Rating current satisfaction with your future solution**
✅ Rate what exists TODAY in the market

❌ **Vague need statements** ("Better workflow")
✅ Specific, measurable needs ("Reduce grant writing time by 50%+")

❌ **Missing or incorrect interview counts**
✅ Explicitly state "0 Interviews" or actual count

❌ **Using wrong CSS classes or hex codes**
✅ Copy exact class names from template

### Report Mistakes

❌ **Weak, passive language** ("might consider", "could explore")
✅ Directive language ("must achieve", "do not proceed until")

❌ **Missing owners and deadlines**
✅ "Product Lead: Quality validation, Sprint end"

❌ **Vague success criteria** ("some improvement")
✅ Specific thresholds ("40% beta conversion", "7+ quality rating")

❌ **Too many callout boxes** (15+)
✅ Use 6-8 callouts for truly critical information only

❌ **No consequences stated**
✅ "If thresholds missed → REASSESS PRODUCT-MARKET FIT"

❌ **Generic competitive analysis**
✅ Test competitors yourself, document specific limitations

❌ **Padding to reach page count**
✅ Be concise. 8 substantive pages beats 12 fluffy pages

---

## Typical Timeline

**Fast Execution (45 min):**
- Data collection: 5 min
- Matrix analysis: 10 min
- Create matrix: 15 min
- Create condensed report: 15 min

**Standard Execution (90 min):**
- Data collection: 15 min
- Matrix analysis: 15 min
- Pattern identification: 10 min
- Create matrix: 20 min
- Create full report: 30 min

**Complete Execution (2-3 hours):**
- Thorough data collection: 30 min
- Deep pattern analysis: 20 min
- Matrix creation with iterations: 30 min
- Comprehensive report: 60 min
- Review and polish: 30 min

---

## Support Files

**Templates:**
- `/templates/Step6_Needs_Matrix_Template.html` - Complete HTML template
- `/templates/Step6_Analysis_Report_Template.md` - Report structure reference
- `/templates/Step6_Quick_Start_Guide.md` - Complete methodology guide

**Examples:**
- (To be added after first implementation)

---

## Output Delivery

**File Package:**
1. `[project]_needs_matrix_landscape_YYYYMM.html` - Matrix HTML
2. `[project]_needs_matrix_landscape_YYYYMM.pdf` - Matrix PDF
3. `[project]_needs_analysis_report_YYYYMM.html` - Report HTML
4. `[project]_needs_analysis_report_YYYYMM.pdf` - Report PDF
5. (Optional) `[project]_needs_analysis_report_YYYYMM.docx` - Report DOCX for editing

**Usage:**
- **Matrix:** Presentations, board meetings, team alignment, quick reference
- **Report:** Planning, resource allocation, investor updates, decision-making

**Update Frequency:**
- Quarterly: After completing interview sprints
- After milestones: When beta converts to paid, when segments validated
- Before fundraising: To show current validation state

---

## Success Criteria

**Step 6 is complete when:**

1. ✅ Needs Matrix created with all cells filled (importance + satisfaction)
2. ✅ Matrix prints cleanly in landscape with readable text
3. ✅ Interview counts displayed for all segments
4. ✅ Evidence basis and next steps documented in footer
5. ✅ Analysis Report complete (9-12 pages)
6. ✅ Three-Act Structure tells coherent story
7. ✅ All actions have owner and deadline
8. ✅ Success criteria stated as go/no-go thresholds
9. ✅ Red flags identified (5-7 specific)
10. ✅ Both deliverables are board-ready and investor-ready

**You're ready for Step 7 (Ecosystem Mapping) when you can:**
- Identify priority segments from matrix hot zones
- Explain evidence gaps requiring stakeholder research
- Articulate specific validation activities needed
- Assign clear ownership for next 30 days of work

---

**This step transforms analysis into visual clarity and strategic action. The matrix shows WHERE opportunities are. The report shows WHAT TO DO about them.**
