# Format Specification: Step 11 Features-Needs Matrix

**Document Version:** 2.0
**Framework:** VIANEO Business Model Evaluation
**Phase:** Business Model Design
**Output Type:** Dual-file deliverable (HTML + Markdown)
**Last Updated:** 2025-11-21

---

## Overview

The Features-Needs Matrix (Step 11) produces two complementary outputs:
1. **Interactive HTML Matrix** - Visual grid showing feature-need alignment with export/print capabilities
2. **Strategic Analysis Document** - Markdown report with coverage metrics, findings, and recommendations

This specification defines exact formatting requirements, interactive behaviors, visual styling, content structure, and validation criteria for both outputs.

---

## 1. Document Header & Metadata

### 1.1 HTML File Header

**HTML Comment Block (Lines 8-15):**
```html
<!--
Generated: [YYYY-MM-DD]
Project: [Project Name]
Type: Features-Needs Matrix
Vianeo Framework Version: 2.0
Coverage: [XX%]
High Opportunity Needs: [X/Y]
-->
```

**Page Title Format:**
```html
<title>Features-Needs Matrix | [Project Name]</title>
```

**Meta Tags Required:**
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Encoding:** UTF-8 only
**Doctype:** HTML5 (`<!DOCTYPE html>`)

### 1.2 Markdown File Header

**Format:**
```markdown
# Features-Needs Matrix Analysis

**Project:** [Project Name]
**Generated:** [YYYY-MM-DD]
**Phase:** Business Model Design (Step 11)
```

**Required Fields:**
- Project name (from Step 1)
- Generation date (ISO 8601 format)
- Phase identifier
- Vianeo version (2.0)

---

## 2. Interactive HTML Matrix Specifications

### 2.1 Visual Layout

**Container Dimensions:**
- Max width: 1600px
- Height: 100vh (full viewport)
- Border radius: 12px
- Box shadow: `0 4px 6px rgba(0, 0, 0, 0.07), 0 10px 20px rgba(0, 0, 0, 0.05)`
- Background: `#ffffff`
- Outer page background: `#e8ebed`

**Layout Structure:**
```
┌─────────────────────────────────────┐
│ HEADER (Fixed)                      │ 10px padding
├─────────────────────────────────────┤
│                                     │
│ MATRIX TABLE (Scrollable)           │ Flex: 1
│                                     │
├─────────────────────────────────────┤
│ LEGEND FOOTER (Fixed)               │ 10px padding
└─────────────────────────────────────┘
```

### 2.2 Header Component

**Background:** Linear gradient `135deg, #1a365d 0%, #2c5282 100%`
**Color:** White
**Padding:** `10px 20px`
**Display:** Flex, space-between alignment

**Left Section Components:**

1. **Title Group:**
   - Primary title: 16px, weight 600, letter-spacing -0.02em
   - Subtitle: 10px, opacity 0.9
   - Format: "[Project Name] Features-Needs Matrix"

2. **Inline Stats (4 required):**
   - Value: 20px, weight 700
   - Label: 9px, opacity 0.85
   - Gap between stats: 20px

   Stats to display:
   - Total Features (X)
   - Total Needs (10)
   - Coverage Percentage (XX%)
   - High Opportunity Coverage (X/X)

**Right Section:**
- Export button (Ctrl+E)
- Print button (Ctrl+P)
- Button styling: See section 2.6

### 2.3 Table Structure

**HTML Structure:**
```html
<table class="matrix-table">
  <thead>
    <tr>
      <th>Customer Need</th>
      <th>[Feature 1]</th>
      <th>[Feature 2]</th>
      <!-- Additional feature columns -->
    </tr>
  </thead>
  <tbody>
    <!-- Needs rows grouped by opportunity level -->
  </tbody>
</table>
```

**Column Configuration:**
- First column (Needs): 200px fixed width, sticky left
- Feature columns: Auto width, minimum 80px
- Feature count: 5-10 typical, up to 15 maximum

**Row Configuration:**
- Needs: 10 total (from Step 7)
- Order: High → Medium → Low → Expected → Accessory
- Height: Auto with 8px vertical padding

### 2.4 Sticky Header Behavior

**Vertical Sticky (Column Headers):**
- Position: `sticky`
- Top: `0`
- Z-index: `10`
- Background: `#f8f9fa` (must be opaque)
- Border bottom: `2px solid #e2e8f0`

**Horizontal Sticky (Row Headers):**
- Position: `sticky`
- Left: `0`
- Z-index: `5`
- Background: Inherits from opportunity level
- Border right: `2px solid #e2e8f0`
- Box shadow: `2px 0 4px rgba(0,0,0,0.04)`

**Corner Cell (Top-left):**
- Position: `sticky`
- Top: `0`, Left: `0`
- Z-index: `20` (highest priority)
- Background: `#f8f9fa`
- Text: "Customer Need"

### 2.5 Opportunity Level Styling

**Color Palette (CSS Variables):**
```css
--color-opportunity-high: #0f9d58;      /* Green */
--color-opportunity-medium: #f4b400;    /* Yellow */
--color-opportunity-low: #ef6c00;       /* Orange */
--color-expected: #1a73e8;              /* Blue */
--color-accessory: #5f6368;             /* Gray */
```

**Row Background Colors:**
| Level | Background | Text Color |
|-------|------------|------------|
| High Opportunity | `#e8f5e9` | `#0f9d58` |
| Medium Opportunity | `#fff9e6` | `#f4b400` |
| Low Opportunity | `#fff3e0` | `#ef6c00` |
| Expected | `#e8f0fe` | `#1a73e8` |
| Accessory | `#f5f5f5` | `#5f6368` |

**Print Color Preservation:**
```css
@media print {
  background: [color] !important;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

**SVG Icon Specifications:**
| Level | SVG Element | Size |
|-------|-------------|------|
| High Opportunity | `<circle r="7">` | Largest filled circle |
| Medium Opportunity | `<circle r="5">` | Medium filled circle |
| Low Opportunity | `<circle r="4">` | Small filled circle |
| Expected | `<path>` star outline | Star with stroke |
| Accessory | `<circle r="3">` | Tiny filled circle |

**Icon Dimensions:** 11×11px display, 14×14 viewBox
**Icon Color:** `currentColor` (inherits from row)

### 2.6 Checkmark Indicators

**Visual Specification:**
- Size: 14px × 14px
- Shape: Rectangle with 2px border-radius
- Background: `#1a365d` (primary blue)
- Content: White "✓" character
- Font size: 11px, weight 600
- Position: Centered in cell using flexbox
- Margin: `0 auto`

**CSS Implementation:**
```css
.check {
  width: 14px;
  height: 14px;
  background: var(--color-primary);
  border-radius: 2px;
  margin: 0 auto;
  position: relative;
}

.check::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-weight: 600;
  font-size: 11px;
}
```

**Usage Rules:**
- Only mark where feature **directly addresses** the need
- Conservative marking (defensible connections only)
- No checkmark = empty `<td></td>` cell

### 2.7 Need Name Display

**Structure:**
```html
<div class="need-name">
  <span class="need-indicator">
    <!-- SVG icon matching opportunity level -->
  </span>
  <div class="need-text">
    <span>[Need Statement]</span>
    <span class="need-category">[Opportunity Level]</span>
  </div>
</div>
```

**Styling:**
- Need statement: 11px, weight 500, `#1a202c`
- Category label: 9px, opacity 0.7, italic
- Icon-text gap: 8px
- Display: Flex with center alignment

### 2.8 Export to CSV Functionality

**Trigger Methods:**
1. Click "Export" button
2. Keyboard: Ctrl+E (Windows/Linux) or Cmd+E (Mac)

**CSV Format:**
```csv
"Customer Need","Opportunity Level","Feature 1","Feature 2","Feature 3"
"Need Statement 1","High Opportunity","✓","","✓"
"Need Statement 2","Medium Opportunity","","✓",""
```

**Specifications:**
- Header row: Need column, Opportunity column, Feature columns
- Need names: From `.need-text span:first-child` innerText
- Opportunity: From `.need-category` innerText
- Checkmarks: "✓" character for presence, "" for empty
- Escaping: Double quotes wrapped and escaped (`"" for "`)
- Encoding: UTF-8 with BOM
- Filename: `[project-name]-features-needs-matrix.csv`
- MIME type: `text/csv;charset=utf-8;`

**Error Handling:**
- Try-catch wrapper around export function
- Console error logging
- User alert on failure: "Export failed. Please try again."

### 2.9 Print Optimization

**Trigger Methods:**
1. Click "Print" button
2. Keyboard: Ctrl+P (Windows/Linux) or Cmd+P (Mac)

**Page Setup:**
```css
@page {
  size: landscape;
  margin: 0.3in;
}
```

**Print-Specific Adjustments:**
| Element | Screen | Print |
|---------|--------|-------|
| Card scale | 100% | 95% |
| Header padding | 10px 20px | 6px 16px |
| Title font | 16px | 14px |
| Subtitle font | 10px | 9px |
| Stat value | 20px | 16px |
| Table font | 11px | 9px |
| Header font | 10px | 8px |
| Cell padding | 8px 6px | 6px 5px |
| Checkmark size | 14px | 12px |

**Element Visibility:**
- Buttons: `display: none` in print
- Sticky positioning: Convert to `static`
- Box shadows: Remove
- Backgrounds: Preserve with print-color-adjust

### 2.10 Legend Footer

**Background:** `#f8f9fa`
**Border top:** `1px solid #e2e8f0`
**Padding:** `10px 20px`
**Layout:** Flex, centered, gap 16px

**Legend Items (5 required):**
Each item contains:
- Color square: 14px × 14px, 2px border-radius
- Label: 10px, weight 500, `#4a5568`
- Gap between square and label: 6px

**Order:** High → Medium → Low → Expected → Accessory

### 2.11 Typography System

**Font Stack:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
```

**Size Scale:**
| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Header title | 16px | 600 | 1.2 |
| Header subtitle | 10px | 400 | 1.2 |
| Stat value | 20px | 700 | 1 |
| Stat label | 9px | 400 | 1 |
| Table header | 10px | 600 | 1.3 |
| Table cell | 11px | 400 | 1.4 |
| Need name | 11px | 500 | 1.4 |
| Need category | 9px | 400 | 1.2 |
| Legend label | 10px | 500 | 1 |
| Button text | 11px | 500 | 1 |

**Color Scale:**
- Primary text: `#1a202c`
- Secondary text: `#4a5568`
- Tertiary text: `#718096`
- White text: `#ffffff`

### 2.12 Button Specifications

**Visual Style:**
```css
padding: 6px 12px;
font-size: 11px;
font-weight: 500;
border: 1px solid rgba(255,255,255,0.3);
background: rgba(255,255,255,0.15);
color: white;
border-radius: 5px;
backdrop-filter: blur(10px);
```

**Hover State:**
```css
background: rgba(255,255,255,0.25);
border-color: rgba(255,255,255,0.5);
```

**Icon Requirements:**
- Export: Download icon (arrow down into line)
- Print: Printer icon
- Stroke width: 2
- Size: 12×12px
- Color: currentColor
- Gap to text: 5px

**SVG Icons:**
```html
<!-- Export -->
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/>
</svg>

<!-- Print -->
<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
  <path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2"/>
  <rect x="6" y="14" width="12" height="8"/>
</svg>
```

### 2.13 Keyboard Shortcuts

**Implementation:**
```javascript
document.addEventListener('keydown', function(e) {
  // Ctrl/Cmd + E for export
  if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
    e.preventDefault();
    document.getElementById('exportBtn').click();
  }
  // Ctrl/Cmd + P for print
  if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
    e.preventDefault();
    document.getElementById('printBtn').click();
  }
});
```

**Shortcuts:**
- **Ctrl+E / Cmd+E:** Export to CSV
- **Ctrl+P / Cmd+P:** Print preview

**Platform Detection:**
- Windows/Linux: Check `e.ctrlKey`
- macOS: Check `e.metaKey`
- Prevent default browser behavior with `e.preventDefault()`

---

## 3. Strategic Analysis Document (Markdown)

### 3.1 Document Structure

**Required Sections (in order):**
1. Coverage Overview
2. Coverage by Opportunity Level (table)
3. Key Findings
   - Strengths
   - Critical Gaps
4. Strategic Recommendations
   - Priority Development
   - Feature Optimization
   - Partnership Opportunities
5. MVP Definition
   - Must-Have Features
   - Defer to Post-Launch
   - Development Priorities
6. Risk Assessment
   - Coverage Risks
   - Strategic Risks
7. Stakeholder Communication
   - For Founders/Product Team
   - For Investors/Committee
   - For Technical Teams
8. Next Steps (Step 12+)
   - Immediate Actions
   - Short-Term
   - Medium-Term
9. Appendix
   - Coverage Calculation Details
   - Feature-Need Matrix Summary
   - Methodology Notes

**Total Length:** 2,000-3,500 words typical

### 3.2 Coverage Overview Section

**Format:**
```markdown
## Coverage Overview

- **Total Features:** [X]
- **Total Needs:** 10
- **Overall Coverage:** [XX%]
- **High Opportunity Needs Addressed:** [X/X]

### Coverage by Opportunity Level

| Level | Total Needs | Covered | Coverage |
|-------|-------------|---------|----------|
| High Opportunity | [X] | [X] | [XX%] |
| Medium Opportunity | [X] | [X] | [XX%] |
| Low Opportunity | [X] | [X] | [XX%] |
| Expected | [X] | [X] | [XX%] |
| Accessory | [X] | [X] | [XX%] |
```

**Metrics Required:**
- Total features (5-10 typical)
- Total needs (always 10)
- Overall coverage percentage
- High-opportunity coverage (X/Y format and %)
- Per-level breakdown table

### 3.3 Key Findings Section

**Strengths Subsection:**
- **Well-Covered High-Opportunity Needs:** List 2-4 needs with multiple features
- **Multi-Need Features:** Identify features addressing 3+ needs
- **Core Value Proposition Evidence:** 2-3 sentence narrative

**Format:**
```markdown
### Strengths

**Well-Covered High-Opportunity Needs:**
1. **[Need Name]** - Addressed by [Feature 1, Feature 2]
   - [Why this coverage is strong - 1 sentence]
2. **[Need Name]** - Addressed by [Feature X]
   - [Why this coverage is strong - 1 sentence]

**Multi-Need Features (High Efficiency):**
- **[Feature Name]** addresses [X] needs including [high-priority ones]
- **[Feature Name]** addresses [X] needs including [high-priority ones]

**Core Value Proposition Evidence:**
[2-3 sentences describing what the solution excels at based on coverage patterns]
```

**Critical Gaps Subsection:**
```markdown
### Critical Gaps

**High-Opportunity Needs Without Coverage:**
1. **[Need Name]** - High Opportunity
   - Impact: [What happens without this?]
   - Recommended action: [Feature to build or partnership]

**Expected Needs With Weak Coverage:**
1. **[Need Name]** - Expected
   - Current coverage: [Limited/None]
   - Risk: [Market entry barrier, legitimacy concern]
   - Recommended action: [What to do]

**Pattern Observations:**
[2-3 sentences on concerning patterns]
```

### 3.4 Strategic Recommendations Section

**Priority Development:**
```markdown
### Priority Development (Immediate)

**1. [Feature to Build]**
- **Addresses:** [Gap need(s)]
- **Priority:** Critical - required for [reason]
- **Estimated effort:** [Sprints/weeks]
- **Dependencies:** [Technical or partner dependencies]
```

**Provide:** 2-4 priority features with structured details

**Feature Optimization:**
- Identify 1-3 features to simplify, refocus, or defer
- Explain rationale for each
- Suggest resource reallocation

**Partnership Opportunities:**
- List needs better served by partners
- Provide rationale (speed, expertise, resources)
- Suggest partner categories

### 3.5 MVP Definition Section

**Must-Have Features Table:**
```markdown
### Must-Have Features (Launch Requirements)

**For High-Opportunity Needs:**
| Feature | Needs Addressed | Coverage |
|---------|-----------------|----------|
| [Feature 1] | [Need A, Need B] | Critical |
| [Feature 2] | [Need C] | Critical |

**For Expected Needs (Table Stakes):**
| Feature | Needs Addressed | Coverage |
|---------|-----------------|----------|
| [Feature X] | [Expected Need 1] | Required |
```

**Total MVP Feature Set:** State total count

**Defer to Post-Launch Table:**
```markdown
| Feature | Needs Addressed | Rationale | Phase |
|---------|-----------------|-----------|-------|
| [Feature A] | [Accessory only] | Not essential | v2.0 |
| [Feature B] | [Low Opportunity] | Validate demand | v2.0 |
```

**Development Priorities:**
List phases with features and timelines

### 3.6 Risk Assessment Section

**Format:**
```markdown
### Coverage Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Specific risk] | H/M/L | H/M/L | [Specific action] |

### Strategic Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Specific risk] | H/M/L | H/M/L | [Specific action] |
```

**Include:** 3-5 coverage risks, 2-3 strategic risks

### 3.7 Stakeholder Communication Section

**Three Subsections Required:**

1. **For Founders/Product Team**
   - Key message (1-2 sentences)
   - Action items (3-5 specific tasks)

2. **For Investors/Committee**
   - Key message (value proposition evidence)
   - Highlights (4-6 bullet points)

3. **For Technical Teams**
   - Key message (development clarity)
   - Development roadmap (sprint-level detail)

### 3.8 Next Steps Section

**Three Time Horizons:**

1. **Immediate Actions (Week 1-2):**
   - 3-4 specific tasks
   - Each with deliverable specified

2. **Short-Term (Month 1):**
   - 3-4 initiatives
   - Each with outcomes defined

3. **Medium-Term (Month 2-3):**
   - 3-4 workstreams
   - Each with success metrics

### 3.9 Appendix Section

**Coverage Calculation Details:**
```markdown
### Coverage Calculation Details

```
Overall Coverage = (Total Checkmarks) / (Features × Needs) × 100
                 = [X] / ([Features] × 10) × 100
                 = [XX%]

High Opportunity Coverage = (High needs with ≥1 feature) / (Total high needs)
                          = [X] / [Y]
                          = [X/Y] or [XX%]
```
```

**Methodology Notes:**
- Explain checkmark criteria (conservative marking)
- Note data sources (Step 7, Step 4)
- Clarify any assumptions

---

## 4. Coverage Metrics Calculation

### 4.1 Overall Coverage Percentage

**Formula:**
```
Overall Coverage (%) = (Total Checkmarks / (Total Features × Total Needs)) × 100
```

**Example:**
- Features: 7
- Needs: 10
- Checkmarks: 42
- Coverage: (42 / 70) × 100 = 60%

**Interpretation Ranges:**
- **<40%:** Narrow solution or missing needs
- **40-60%:** Focused, strategic coverage
- **60-80%:** Comprehensive coverage
- **>80%:** Potential over-engineering or broad features

### 4.2 High-Opportunity Coverage

**Formula:**
```
High-Opportunity Coverage = (High Needs with ≥1 Checkmark) / (Total High Needs)
```

**Format:** Display as "X/Y" and percentage

**Example:**
- Total high-opportunity needs: 3
- Covered high-opportunity needs: 2
- Coverage: 2/3 (67%)

**Target:** 100% (all high-opportunity needs must be addressed)

### 4.3 Coverage by Opportunity Level

**Calculation per Level:**
```
Level Coverage (%) = (Needs of Level with ≥1 Checkmark) / (Total Needs of Level) × 100
```

**Table Format:**
```
| Level              | Total | Covered | Coverage |
|--------------------|-------|---------|----------|
| High Opportunity   |   3   |    3    |   100%   |
| Medium Opportunity |   2   |    2    |   100%   |
| Low Opportunity    |   2   |    1    |    50%   |
| Expected           |   2   |    2    |   100%   |
| Accessory          |   1   |    0    |     0%   |
```

**Strategic Targets:**
- High Opportunity: 100%
- Expected: 100%
- Medium Opportunity: 70-100%
- Low Opportunity: 30-70%
- Accessory: 0-30%

### 4.4 Feature Efficiency Metric

**Formula:**
```
Feature Efficiency = Average Needs Addressed per Feature
                   = Total Checkmarks / Total Features
```

**Example:**
- Checkmarks: 42
- Features: 7
- Efficiency: 42/7 = 6.0 needs per feature

**Interpretation:**
- **<3:** Features may be too narrow
- **3-5:** Typical focused features
- **5-8:** High-efficiency features
- **>8:** Features may be too broad

### 4.5 Need Saturation Metric

**Formula:**
```
Need Saturation = Average Features per Need
                = Total Checkmarks / Total Needs
```

**Example:**
- Checkmarks: 42
- Needs: 10
- Saturation: 42/10 = 4.2 features per need

**Interpretation:**
- **<2:** Sparse coverage, potential gaps
- **2-4:** Balanced coverage
- **4-6:** Strong redundancy (good for critical needs)
- **>6:** Possible over-engineering

### 4.6 Display Requirements

**In HTML Header:**
- Overall coverage: Large stat (20px value)
- High-opportunity coverage: Large stat (X/Y format)
- Total features: Medium stat
- Total needs: Medium stat

**In Markdown:**
- All metrics in overview section
- Per-level breakdown in table
- Formulas in appendix with values filled in

---

## 5. Opportunity Level Definitions

### 5.1 High Opportunity

**Definition:** Fundamental need with poor current satisfaction and large impact potential

**Characteristics:**
- Importance: Very high to requester segment
- Current satisfaction: Rather not or not at all satisfied
- Impact: Core value proposition element
- Frequency: Often represents pain points

**Visual Indicators:**
- Color: `#0f9d58` (Green)
- Background: `#e8f5e9` (Light green)
- Icon: Large filled circle (r="7")

**Strategic Priority:** **MUST ADDRESS**
- Target coverage: 100%
- Include all in MVP
- First development priority

**Examples:**
- "Reduce inventory loss from 15% to <2%"
- "Cut patient wait times from 45min to <10min"
- "Automate manual data entry (currently 4hrs/day)"

### 5.2 Medium Opportunity

**Definition:** Important need with moderate satisfaction gap and differentiation potential

**Characteristics:**
- Importance: High to requester segment
- Current satisfaction: Somewhat satisfied to rather not satisfied
- Impact: Competitive differentiator
- Frequency: Valued but not critical

**Visual Indicators:**
- Color: `#f4b400` (Yellow/Gold)
- Background: `#fff9e6` (Light yellow)
- Icon: Medium filled circle (r="5")

**Strategic Priority:** **SHOULD ADDRESS**
- Target coverage: 70-100%
- Include some in MVP
- Second development priority

**Examples:**
- "Improve reporting from weekly to real-time"
- "Add mobile access to desktop-only system"
- "Integrate with existing tools (currently manual sync)"

### 5.3 Low Opportunity

**Definition:** Secondary need or already well-satisfied with smaller impact potential

**Characteristics:**
- Importance: Moderate OR already satisfied
- Current satisfaction: Somewhat satisfied or better
- Impact: Incremental improvement
- Frequency: Nice to have

**Visual Indicators:**
- Color: `#ef6c00` (Orange)
- Background: `#fff3e0` (Light orange)
- Icon: Small filled circle (r="4")

**Strategic Priority:** **CONSIDER IF RESOURCES ALLOW**
- Target coverage: 30-70%
- Defer most from MVP
- Third development priority

**Examples:**
- "Enhance dashboard aesthetics"
- "Add keyboard shortcuts"
- "Customize color schemes"

### 5.4 Expected

**Definition:** Table stakes functionality required for market entry but not differentiating

**Characteristics:**
- Importance: Required for legitimacy
- Current satisfaction: Expected baseline
- Impact: Market entry requirement
- Frequency: Standard in category

**Visual Indicators:**
- Color: `#1a73e8` (Blue)
- Background: `#e8f0fe` (Light blue)
- Icon: Star outline (path with stroke, no fill)

**Strategic Priority:** **INCLUDE FOR LEGITIMACY**
- Target coverage: 100%
- Include in MVP
- Table stakes, not differentiators

**Examples:**
- "User authentication and security"
- "Data export to CSV/Excel"
- "Basic reporting functionality"

### 5.5 Accessory

**Definition:** Peripheral features or luxury enhancements not essential to core value

**Characteristics:**
- Importance: Low to requester segment
- Current satisfaction: N/A or satisfied
- Impact: Enhancement only
- Frequency: Edge cases

**Visual Indicators:**
- Color: `#5f6368` (Gray)
- Background: `#f5f5f5` (Light gray)
- Icon: Tiny circle (r="3")

**Strategic Priority:** **DEFER UNTIL VALIDATED**
- Target coverage: 0-30%
- Exclude from MVP
- Post-launch based on demand

**Examples:**
- "White-label branding options"
- "API access for third-party integrations"
- "Multi-language support (single market MVP)"

### 5.6 Classification Rules

**How to Classify a Need:**

1. **Assess Importance:**
   - Survey data (10-point scale)
   - Interview frequency mentions
   - Segment prioritization

2. **Assess Current Satisfaction:**
   - Survey data (5-point Likert)
   - Gap = Importance - Satisfaction

3. **Determine Opportunity:**
   - High: High importance + Low satisfaction
   - Medium: High importance + Medium satisfaction OR Medium importance + Low satisfaction
   - Low: Low importance OR High satisfaction
   - Expected: Industry standard requirement
   - Accessory: Peripheral to core value

4. **Validate Against Step 7:**
   - Must match Step 7 Needs Qualification Matrix
   - No reclassification without updating Step 7

---

## 6. Two-File Output Requirements

### 6.1 File Naming Convention

**HTML File:**
```
[project-name]-features-needs-matrix.html
```

**Markdown File:**
```
[project-name]-matrix-analysis.md
```

**Rules:**
- Project name: Lowercase, hyphens for spaces
- No special characters except hyphens
- Maximum 50 characters for project name portion
- .html and .md extensions required

**Examples:**
- `inventory-tracker-features-needs-matrix.html`
- `inventory-tracker-matrix-analysis.md`
- `patient-scheduling-features-needs-matrix.html`
- `patient-scheduling-matrix-analysis.md`

### 6.2 File Interdependencies

**Shared Data:**
- Coverage metrics must match exactly
- Need statements identical (from Step 7)
- Feature names identical (from Step 4)
- Opportunity classifications aligned

**Cross-References:**
- Markdown should reference HTML for visual detail
- HTML comment should note paired markdown file
- Both files should have same generation date

### 6.3 Delivery Format

**Package Contents:**
1. HTML file (interactive matrix)
2. Markdown file (strategic analysis)
3. Brief summary message (3-5 sentences)

**Summary Message Template:**
```
Features-Needs Matrix Complete

Coverage: XX% overall, X/X high-opportunity needs addressed

Key Insight: [1-2 sentence strategic finding]

Outputs:
- Interactive matrix: [filename].html (Ctrl+E to export, Ctrl+P to print)
- Strategic analysis: [filename].md

Critical Actions:
1. [Immediate priority]
2. [Resource allocation decision]
```

### 6.4 Quality Assurance

**Before Delivery, Verify:**
- [ ] HTML opens without errors in Chrome, Firefox, Safari
- [ ] Markdown renders correctly in standard viewers
- [ ] Metrics match between files
- [ ] Export function produces valid CSV
- [ ] Print layout fits on landscape page
- [ ] All checkmarks properly positioned
- [ ] Colors match specification exactly
- [ ] File sizes reasonable (<500KB HTML, <100KB MD)

---

## 7. Validation Checklist (40+ Items)

### 7.1 Data Integrity (Critical)

**Needs Validation:**
- [ ] All 10 needs from Step 7 included
- [ ] Opportunity classifications match Step 7 exactly
- [ ] Need statements verbatim from Step 7 (no paraphrasing)
- [ ] Needs ordered: High → Medium → Low → Expected → Accessory
- [ ] No duplicate or overlapping needs
- [ ] Each need has clear category label

**Features Validation:**
- [ ] 5-10 solution features identified
- [ ] Feature names specific and action-oriented
- [ ] Features describe capabilities, not technologies
- [ ] No generic features ("AI", "mobile app", "dashboard")
- [ ] Features align with Step 4 solution description
- [ ] Feature count matches header stat display

**Mapping Accuracy:**
- [ ] Checkmarks only where feature genuinely addresses need
- [ ] Conservative marking (defensible connections only)
- [ ] Empty cells indicate no coverage (not partial)
- [ ] At least one checkmark per row (or documented gap)
- [ ] No feature with zero checkmarks (useless feature indicator)
- [ ] Checkmark count matches coverage calculations

### 7.2 Coverage Metrics (Required)

**Calculation Verification:**
- [ ] Total features count correct
- [ ] Total needs = 10
- [ ] Overall coverage calculated: (Checkmarks / (Features × 10)) × 100
- [ ] High-opportunity coverage: X/Y format and percentage
- [ ] Per-level coverage table completed
- [ ] Metrics identical in HTML and Markdown

**Strategic Thresholds:**
- [ ] Overall coverage 30-85% (or explained if outside)
- [ ] High-opportunity coverage ≥70% (ideally 100%)
- [ ] Expected needs coverage ≥70%
- [ ] Accessory needs coverage ≤30%
- [ ] No high-opportunity need with zero coverage (or critical gap noted)

### 7.3 Visual Design (Professional Standards)

**HTML Structure:**
- [ ] Valid HTML5 with proper DOCTYPE
- [ ] UTF-8 charset specified
- [ ] Viewport meta tag for responsive
- [ ] Title format: "Features-Needs Matrix | [Project Name]"
- [ ] No console errors when opened
- [ ] Scrollable with sticky headers functional

**Typography:**
- [ ] System font stack used
- [ ] Header title: 16px, weight 600
- [ ] Stat values: 20px, weight 700
- [ ] Table cells: 11px
- [ ] Need categories: 9px, opacity 0.7
- [ ] All text readable and aligned properly

**Color Accuracy:**
- [ ] High Opportunity: #0f9d58 (green)
- [ ] Medium Opportunity: #f4b400 (yellow)
- [ ] Low Opportunity: #ef6c00 (orange)
- [ ] Expected: #1a73e8 (blue)
- [ ] Accessory: #5f6368 (gray)
- [ ] Row backgrounds match opportunity levels
- [ ] Print colors preserved (-webkit-print-color-adjust: exact)

**SVG Icons:**
- [ ] High: Circle r="7"
- [ ] Medium: Circle r="5"
- [ ] Low: Circle r="4"
- [ ] Expected: Star outline
- [ ] Accessory: Circle r="3"
- [ ] Icons 11×11px, currentColor
- [ ] Icons match row opportunity level

**Checkmarks:**
- [ ] 14×14px blue rectangles
- [ ] 2px border-radius
- [ ] White "✓" centered
- [ ] Print size: 12×12px
- [ ] Only where coverage exists

**Legend Footer:**
- [ ] All 5 levels represented
- [ ] Color squares match backgrounds exactly
- [ ] 14×14px squares with 2px radius
- [ ] Labels clear: 10px, weight 500
- [ ] Centered layout with 16px gaps

### 7.4 Interactive Features (Required)

**Export Functionality:**
- [ ] Export button visible and styled
- [ ] Click triggers CSV download
- [ ] Filename: [project-name]-features-needs-matrix.csv
- [ ] CSV header row includes all columns
- [ ] Need names extracted from .need-text span
- [ ] Opportunity level included as second column
- [ ] Checkmarks use "✓", empty use ""
- [ ] Quotes properly escaped
- [ ] Ctrl+E / Cmd+E keyboard shortcut works
- [ ] Error handling with try-catch and user alert

**Print Functionality:**
- [ ] Print button visible and styled
- [ ] Click triggers print dialog
- [ ] Landscape orientation (@page size)
- [ ] Margins: 0.3in
- [ ] Headers convert to static positioning
- [ ] Font sizes reduce appropriately
- [ ] Colors preserved (print-color-adjust)
- [ ] Fits on single page (or controlled breaks)
- [ ] Buttons hidden in print
- [ ] Ctrl+P / Cmd+P keyboard shortcut works

**Button Design:**
- [ ] SVG icons (download for export, printer for print)
- [ ] White text, semi-transparent background
- [ ] Border: rgba(255,255,255,0.3)
- [ ] Hover state increases opacity
- [ ] Backdrop blur effect
- [ ] 11px font, 6px vertical padding
- [ ] Icon-text gap: 5px

### 7.5 Content Quality (Strategic)

**Markdown Structure:**
- [ ] All 9 required sections present
- [ ] Coverage overview with metrics table
- [ ] Key findings: Strengths and Gaps subsections
- [ ] Strategic recommendations: 3 subsections
- [ ] MVP definition with tables
- [ ] Risk assessment with tables
- [ ] Stakeholder communication: 3 audiences
- [ ] Next steps: 3 time horizons
- [ ] Appendix with calculations and methodology

**Strategic Coherence:**
- [ ] MVP boundaries align with coverage
- [ ] High-opportunity needs prioritized
- [ ] Expected needs included for legitimacy
- [ ] Accessory features deferred/excluded
- [ ] Recommendations match coverage patterns
- [ ] Gaps acknowledged, not hidden
- [ ] 2,000-3,500 word count

**Stakeholder Readiness:**
- [ ] Clear story about solution-market fit
- [ ] Terminology accessible to non-technical readers
- [ ] Professional enough for committee presentation
- [ ] Insights actionable, not just descriptive
- [ ] Evidence-based recommendations
- [ ] Resource allocation clarity

### 7.6 File Management

**Naming and Location:**
- [ ] HTML filename: [project]-features-needs-matrix.html
- [ ] Markdown filename: [project]-matrix-analysis.md
- [ ] No spaces in filenames (use hyphens)
- [ ] Lowercase project name
- [ ] Files in correct output directory

**Metadata:**
- [ ] HTML comment block complete
- [ ] Generation date in ISO format (YYYY-MM-DD)
- [ ] Project name consistent across files
- [ ] Framework version: 2.0
- [ ] Coverage metrics in HTML comment

**Cross-File Consistency:**
- [ ] Metrics match exactly between HTML and MD
- [ ] Need statements identical
- [ ] Feature names identical
- [ ] Generation dates match
- [ ] Opportunity classifications aligned

---

## 8. Common Mistakes to Avoid (10+ Items)

### 8.1 Data Mistakes

**1. Optimistic Checkmark Marking**
- **Mistake:** Marking checkmarks for indirect or aspirational connections
- **Impact:** Inflated coverage, false confidence, unrealistic MVP
- **Prevention:** Only mark where feature **directly solves** the need
- **Test:** "Would user with this need find this feature valuable?"

**2. Mismatched Opportunity Classifications**
- **Mistake:** Reclassifying needs from Step 7 without documentation
- **Impact:** Breaks framework continuity, undermines validation
- **Prevention:** Copy exact classifications from Step 7
- **Fix:** If reclassification needed, update Step 7 first

**3. Vague Feature Descriptions**
- **Mistake:** Using broad terms like "Mobile app", "AI", "Dashboard"
- **Impact:** Can't assess true coverage, features seem to cover everything
- **Prevention:** Use specific, action-oriented descriptions
- **Example:** "Mobile barcode scanning" not "Mobile app"

**4. Duplicate or Overlapping Needs**
- **Mistake:** Including variants of same need
- **Impact:** Artificially inflates coverage, obscures true gaps
- **Prevention:** Consolidate similar needs in Step 7
- **Test:** "Are these fundamentally different problems?"

### 8.2 Coverage Mistakes

**5. Over-Engineering Warning Ignored**
- **Mistake:** High coverage (>85%) seen as positive
- **Impact:** Unfocused solution, resource waste, slow development
- **Prevention:** Interpret >80% as potential over-engineering
- **Action:** Review if features are too broad or needs too granular

**6. Critical Gap Rationalization**
- **Mistake:** Explaining away high-opportunity needs with zero coverage
- **Impact:** MVP won't deliver core value, market entry failure
- **Prevention:** 100% high-opportunity coverage target (no exceptions)
- **Action:** Build features or find partnerships to fill gaps

**7. Expected Needs Neglected**
- **Mistake:** Focusing only on high-opportunity, ignoring expected
- **Impact:** Solution lacks legitimacy, users won't adopt
- **Prevention:** 100% expected needs coverage for MVP
- **Example:** Security, basic reporting, standard workflows

**8. Accessory Feature Inclusion in MVP**
- **Mistake:** Including low-priority features in initial scope
- **Impact:** Delayed launch, resource dilution, unfocused value prop
- **Prevention:** Defer all accessory to v2.0+
- **Test:** "Would MVP fail without this?"

### 8.3 Visual Mistakes

**9. Broken Sticky Headers**
- **Mistake:** Headers scroll away, losing context
- **Impact:** User can't track which row/column they're viewing
- **Prevention:** Test scrolling in actual browser
- **Fix:** position: sticky, proper z-index, opaque backgrounds

**10. Color Loss in Print**
- **Mistake:** Opportunity colors disappear when printed
- **Impact:** Matrix loses strategic meaning in hard copy
- **Prevention:** Use -webkit-print-color-adjust: exact
- **Test:** Print preview before delivering

**11. Non-Responsive Export Button**
- **Mistake:** Export function broken or untested
- **Impact:** Users can't extract data for further analysis
- **Prevention:** Test CSV download in Chrome, Firefox, Safari
- **Check:** Proper escaping, correct columns, UTF-8 encoding

**12. Incorrect SVG Icons**
- **Mistake:** All needs have same icon (usually largest circle)
- **Impact:** Visual differentiation lost, opportunity unclear
- **Prevention:** Match icon size to level (r=7/5/4/star/3)
- **Reference:** Section 2.5 of this spec

### 8.4 Content Mistakes

**13. Generic Recommendations**
- **Mistake:** "Improve features" or "Fill gaps" without specifics
- **Impact:** Not actionable, no decision support
- **Prevention:** Name specific features, needs, timelines, resources
- **Example:** "Build RFID integration (3 sprints) to address inventory loss"

**14. Missing MVP Definition**
- **Mistake:** Analysis without clear minimum feature set
- **Impact:** Development team doesn't know what to build
- **Prevention:** Explicit MVP section with must-have table
- **Include:** Feature list, addressed needs, defer rationale

**15. Calculation Errors**
- **Mistake:** Wrong coverage percentages displayed
- **Impact:** Misleads stakeholders, false strategic conclusions
- **Prevention:** Manual verification of formulas
- **Formula:** (Checkmarks / (Features × 10)) × 100

### 8.5 Process Mistakes

**16. Creating Matrix Before Validation**
- **Mistake:** Running Step 11 before Steps 7-10 complete
- **Impact:** Needs not validated, priorities uncertain, wasted work
- **Prevention:** Only after diagnostic shows "Recommended to Go"
- **Sequence:** Steps 1-10 → Matrix → Development

**17. Solo Matrix Creation**
- **Mistake:** One person marks checkmarks without team input
- **Impact:** Biased assessment, missing connections, blind spots
- **Prevention:** Workshop format with cross-functional team
- **Include:** Product, engineering, sales, customer success

---

## 9. File Naming Convention

### 9.1 Standard Format

**HTML File:**
```
[project-name]-features-needs-matrix.html
```

**Markdown File:**
```
[project-name]-matrix-analysis.md
```

### 9.2 Project Name Rules

**Transformation Process:**
1. Start with official project name from Step 1
2. Convert to lowercase
3. Replace spaces with single hyphen (-)
4. Remove all special characters except hyphens
5. Maximum 50 characters
6. No leading or trailing hyphens

**Examples:**

| Original Project Name | Transformed |
|----------------------|-------------|
| Inventory Tracker Pro | inventory-tracker-pro |
| Patient Scheduling System | patient-scheduling-system |
| SmartHome Energy Monitor | smarthome-energy-monitor |
| AI-Powered CRM Tool | ai-powered-crm-tool |
| Healthcare Analytics Platform | healthcare-analytics-platform |

### 9.3 Full Filename Examples

**Valid:**
- `inventory-tracker-features-needs-matrix.html`
- `patient-scheduling-features-needs-matrix.html`
- `smarthome-monitor-features-needs-matrix.html`
- `crm-tool-features-needs-matrix.html`

**Invalid:**
- `Inventory Tracker-features-needs-matrix.html` (not lowercase, has space)
- `patient_scheduling-features-needs-matrix.html` (uses underscore)
- `smarthome-monitor.html` (missing suffix)
- `features-needs-matrix.html` (missing project name)

### 9.4 Extension Requirements

**HTML File:**
- Extension: `.html` (not .htm)
- MIME type: `text/html`
- Encoding: UTF-8

**Markdown File:**
- Extension: `.md` (not .markdown or .txt)
- MIME type: `text/markdown`
- Encoding: UTF-8

### 9.5 Storage and Organization

**Recommended Directory Structure:**
```
project-root/
├── vianeo-outputs/
│   ├── step-11/
│   │   ├── [project]-features-needs-matrix.html
│   │   └── [project]-matrix-analysis.md
│   ├── step-07/
│   ├── step-10/
│   └── ...
```

**File Versioning (if needed):**
```
[project]-features-needs-matrix-v1.html
[project]-features-needs-matrix-v2.html
[project]-features-needs-matrix-final.html
```

**Dated Versions:**
```
[project]-features-needs-matrix-2025-11-21.html
```

---

## 10. Quality Standards Summary

### 10.1 Must-Have Requirements (Blockers)

These items must be 100% complete for delivery:

**Data Integrity:**
- All 10 needs from Step 7 included
- Opportunity classifications match Step 7
- Features align with Step 4 solution
- Conservative checkmark marking
- Metrics calculated correctly

**Interactive Features:**
- Export to CSV functional (Ctrl+E)
- Print optimization complete (Ctrl+P)
- Sticky headers working
- No JavaScript errors

**Dual Output:**
- HTML matrix file delivered
- Markdown analysis file delivered
- Files cross-referenced and consistent
- Proper naming convention

**Strategic Content:**
- Coverage overview with metrics
- Key findings (strengths and gaps)
- MVP definition clear
- Recommendations actionable

### 10.2 High-Priority Requirements (Should Have)

Target 90%+ completion:

**Visual Design:**
- Color palette exact per spec
- Typography scale consistent
- SVG icons match opportunity levels
- Legend footer complete
- Print layout optimized

**Coverage Quality:**
- High-opportunity: 100% coverage
- Expected needs: 100% coverage
- Overall coverage: 40-80%
- Strategic pattern evident

**Content Depth:**
- Stakeholder communication sections complete
- Risk assessment included
- Next steps with timelines
- Appendix with methodology

### 10.3 Nice-to-Have Requirements (Optional)

Target 80%+ completion:

**Advanced Features:**
- Weighted coverage analysis
- Feature efficiency metrics
- Competitive overlay (if data available)
- Time-series roadmap

**Polish:**
- Custom project branding
- Additional visualizations in markdown
- Extended appendix sections
- Supplementary tables

### 10.4 Success Criteria

**The matrix has succeeded when:**

1. **Product team has clarity:**
   - Knows exactly what to build for MVP
   - Understands priority order
   - Can estimate development timeline

2. **Stakeholders have confidence:**
   - See evidence of solution-market fit
   - Understand scope management
   - Trust resource allocation

3. **Coverage tells a story:**
   - High-opportunity needs addressed
   - Expected needs covered for legitimacy
   - Gaps acknowledged with plans
   - Accessory features deferred

4. **Outputs are professional:**
   - HTML renders perfectly in all browsers
   - Export and print work flawlessly
   - Markdown formats cleanly
   - Suitable for external presentation

5. **Decisions are enabled:**
   - MVP boundaries clear and defensible
   - Build vs. partner choices evident
   - Resource allocation priorities set
   - Go-to-market messaging emerges

### 10.5 Final Validation Questions

Before delivery, answer affirmatively:

- [ ] Would a founder use this to plan sprints?
- [ ] Would an investor find this convincing for due diligence?
- [ ] Would a product team know what to build?
- [ ] Would a committee understand strategic fit?
- [ ] Is this professional enough for external presentation?
- [ ] Do the metrics tell a coherent story?
- [ ] Are all gaps acknowledged with plans?
- [ ] Does the MVP make market sense?

**If any answer is "no," revise before delivery.**

---

## Appendix A: Quick Reference

### Color Codes
```css
High Opportunity:    #0f9d58 / #e8f5e9
Medium Opportunity:  #f4b400 / #fff9e6
Low Opportunity:     #ef6c00 / #fff3e0
Expected:            #1a73e8 / #e8f0fe
Accessory:           #5f6368 / #f5f5f5
Primary:             #1a365d
Primary Light:       #2c5282
```

### Icon Sizes
```
High: r="7"
Medium: r="5"
Low: r="4"
Accessory: r="3"
Expected: Star path
```

### Typography Scale
```
Header Title: 16px / 600
Stat Value: 20px / 700
Table Cell: 11px / 400
Need Name: 11px / 500
Category: 9px / 400
Button: 11px / 500
```

### Keyboard Shortcuts
```
Ctrl+E / Cmd+E: Export CSV
Ctrl+P / Cmd+P: Print
```

### Coverage Targets
```
Overall: 40-80%
High Opportunity: 100%
Expected: 100%
Medium: 70-100%
Low: 30-70%
Accessory: 0-30%
```

### File Extensions
```
HTML: .html
Markdown: .md
CSV Export: .csv
```

---

## Appendix B: Version History

**v2.0 (2025-11-21):**
- Initial comprehensive format specification
- Dual-file output (HTML + Markdown)
- Interactive features (export, print, keyboard shortcuts)
- Strategic analysis framework
- 40+ validation checklist items
- 10+ common mistakes documented

---

**End of Format Specification**

*This specification is part of the VIANEO Business Model Evaluation Framework v2.0*
*For questions or clarifications, refer to Step 11 Reference Guide and Quality Checklist*
