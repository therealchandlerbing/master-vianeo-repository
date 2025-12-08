# VIANEO Executive Sprint Report - Format Specification

**Version:** 1.0
**Document Type:** Technical Format Specification
**Purpose:** Define complete structure, formatting, and validation requirements for Executive Sprint Reports
**Last Updated:** December 8, 2025
**Maintained By:** 360 Social Impact Studios

---

## Table of Contents

1. [Overview](#overview)
2. [Document Properties](#document-properties)
3. [Typography & Styling](#typography--styling)
4. [Cover Page Structure](#cover-page-structure)
5. [Section 1: Executive Summary](#section-1-executive-summary)
6. [Section 2: Business Model Overview](#section-2-business-model-overview)
7. [Section 3: Evaluation Results](#section-3-evaluation-results)
8. [Section 4: Stakeholder Analysis](#section-4-stakeholder-analysis)
9. [Section 5: Recommendations](#section-5-recommendations)
10. [Section 6: Conclusion](#section-6-conclusion)
11. [Page Break Strategy](#page-break-strategy)
12. [Table Specifications](#table-specifications)
13. [Color Palette](#color-palette)
14. [Validation Checklist](#validation-checklist)
15. [Common Mistakes](#common-mistakes)
16. [File Naming Convention](#file-naming-convention)

---

## Overview

### Purpose

The Executive Sprint Report serves as the **culminating deliverable** for a complete Vianeo Business Model Evaluation Sprint (4-6 sessions). It synthesizes findings across all five proof-of-value dimensions into a committee-ready, investor-ready professional document.

### When to Use

- After completing a full Vianeo Sprint (minimum 4 sessions)
- When all five dimensions have been assessed with scores
- For committee presentations, investor pitches, or board reviews
- As the primary handoff document for stakeholders

### Output Formats

1. **DOCX (Primary):** Professional, print-ready format for presentation
2. **Markdown (Secondary):** Version-controllable format for collaboration

Both formats contain **identical content** with only formatting differences.

### Document Length

**Target:** 12-15 pages
**Minimum:** 10 pages
**Maximum:** 18 pages

Length is controlled by:
- Number of strengths/gaps per dimension (3-7 strengths, 3-5 gaps recommended)
- Number of personas (3-4 recommended)
- Number of priorities (3 immediate, 3 short-term, 3 medium-term recommended)

---

## Document Properties

### Page Setup

| Property | Value | Notes |
|----------|-------|-------|
| **Orientation** | Portrait | Never landscape |
| **Page Size** | Letter (8.5" × 11") | US standard |
| **Top Margin** | 1.0 inch (1440 DXA) | Consistent all pages |
| **Bottom Margin** | 1.0 inch (1440 DXA) | Consistent all pages |
| **Left Margin** | 1.0 inch (1440 DXA) | Consistent all pages |
| **Right Margin** | 1.0 inch (1440 DXA) | Consistent all pages |
| **Gutter** | 0 | No binding offset |

### Headers & Footers

**Header (all pages except cover):**
```
Right-aligned, 10pt Arial, Gray (#6C757D)
[Project Name] Vianeo Validation Sprint Report
```

**Footer (all pages):**
```
Center-aligned, 10pt Arial, Black
360 Social Impact Studios | Page X of Y
```

**Note:** Page numbers are automatic and update dynamically.

---

## Typography & Styling

### Font Family

**Primary:** Arial
**Fallback:** Helvetica, sans-serif

**Rationale:** Universal compatibility across Windows, Mac, and Google Docs.

### Font Sizes

| Element | Size (points) | Weight | Color |
|---------|---------------|--------|-------|
| **Cover Title (Line 1)** | 28 | Bold | Primary Blue (#1E3A5F) |
| **Cover Title (Line 2)** | 22 | Bold | Primary Blue (#1E3A5F) |
| **Tagline** | 14 | Italic | Gray (#6C757D) |
| **Assessment Type** | 12 | Regular | Secondary Blue (#2E5A7F) |
| **Heading 1** | 16 | Bold | Primary Blue (#1E3A5F) |
| **Heading 2** | 14 | Bold | Black (#000000) |
| **Heading 3** | 12 | Bold | Black (#000000) |
| **Body Text** | 11 | Regular | Black (#000000) |
| **Table Header** | 11 | Bold | White (#FFFFFF) on Blue |
| **Table Body** | 11 | Regular | Black (#000000) |
| **Metadata** | 9 | Regular | Light Gray (#757575) |
| **Footer** | 10 | Regular | Black (#000000) |

### Line Spacing

| Element | Spacing |
|---------|---------|
| **Body Paragraphs** | 1.15 (default) |
| **Before Heading 1** | 18 pt |
| **After Heading 1** | 12 pt |
| **Before Heading 2** | 12 pt |
| **After Heading 2** | 6 pt |
| **Before Heading 3** | 6 pt |
| **After Heading 3** | 6 pt |
| **After Body Paragraph** | 6 pt |

### Alignment

| Element | Alignment |
|---------|-----------|
| **Cover Title** | Center |
| **Cover Metadata Table** | Center (table), Left (labels), Left (values) |
| **Section Headings** | Left |
| **Body Text** | Left, Justified |
| **Table Headers** | Center |
| **Table Data (Text)** | Left |
| **Table Data (Numbers)** | Center |
| **Footer** | Center |

---

## Cover Page Structure

### Layout

```
[Vertical spacing: 1.5 inches from top]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         [PROJECT NAME] VIANEO VALIDATION
         (28pt, bold, primary blue, centered)

         EXECUTIVE SPRINT REPORT
         (22pt, bold, primary blue, centered)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [Project Tagline]
    (14pt, italic, gray, centered)

    Business Model Evaluation & Market Readiness Assessment
    (12pt, secondary blue, centered)

[Vertical spacing: 1 inch]

┌───────────────────────────────────────────────────┐
│ Principal Investigator │ [Name]                   │
├───────────────────────────────────────────────────┤
│ Institution            │ [Organization]           │
├───────────────────────────────────────────────────┤
│ Sprint Duration        │ [Dates and sessions]     │
├───────────────────────────────────────────────────┤
│ Evaluation Framework   │ Vianeo Business Model... │
├───────────────────────────────────────────────────┤
│ Prepared By            │ 360 Social Impact Studios│
├───────────────────────────────────────────────────┤
│ Report Date            │ [Date]                   │
└───────────────────────────────────────────────────┘
```

### Metadata Table Specifications

**Table Properties:**
- Rows: 6
- Columns: 2
- Border: 1pt solid #CCCCCC (all cells)
- Column 1 Width: 2.5 inches
- Column 2 Width: 4.0 inches
- Cell Padding: 8pt all sides
- Vertical Alignment: Middle

**Label Column (Column 1):**
- Font: 11pt Arial Bold
- Color: Black (#000000)
- Background: None (white)

**Value Column (Column 2):**
- Font: 11pt Arial Regular
- Color: Black (#000000)
- Background: None (white)

### Page Break

**Mandatory page break after cover page before Section 1.**

---

## Section 1: Executive Summary

### 1.1 Score Dashboard

**Heading:** "1.1 Score Dashboard" (Heading 2, 14pt bold)

**Table Structure:**

| Overall Vianeo Score | Market Maturity Score | Status |
|---------------------|----------------------|--------|
| **X.X / 5.0** | **X.X / 5.0** | **[STATUS]** |

**Table Specifications:**
- Rows: 2 (1 header + 1 data)
- Columns: 3
- Column Widths: Equal (~2.17 inches each, totaling 6.5 inches)
- Header Row:
  - Background: Primary Blue (#1E3A5F)
  - Text: 11pt Arial Bold, White (#FFFFFF)
  - Alignment: Center
- Data Row:
  - Background (columns 1-2): White (#FFFFFF)
  - Background (column 3): Yellow (#FFC107) if CONDITIONAL, Green (#28A745) if GO, Red (#DC3545) if NO-GO
  - Text: 11pt Arial Bold, Black (#000000)
  - Alignment: Center

**Spacing After:** 12pt

### 1.2 Project Overview

**Heading:** "1.2 Project Overview" (Heading 2, 14pt bold)

**Content:** 3 paragraphs of body text (11pt Arial Regular)

**Paragraph Guidelines:**
1. **Paragraph 1:** Sprint scope and methodology (1-2 sentences introducing the evaluation)
2. **Paragraph 2:** Key strengths and technical achievements (3-5 sentences)
3. **Paragraph 3:** Market readiness assessment and primary gap (2-3 sentences)

**Total Word Count:** 250-350 words
**Spacing Between Paragraphs:** 6pt

### 1.3 Key Findings

**Heading:** "1.3 Key Findings" (Heading 2, 14pt bold)

**Table Structure:**

| Dimension | Score | Status | Interpretation |
|-----------|-------|--------|----------------|
| **Legitimacy (15%)** | 4.7 | ✓ PASS | [One sentence] |
| **Desirability (25%)** | 4.2 | ✓ PASS | [One sentence] |
| **Acceptability (20%)** | 4.1 | ✓ PASS | [One sentence] |
| **Feasibility (20%)** | 4.4 | ✓ PASS | [One sentence] |
| **Viability (20%)** | 3.7 | ✓ PASS | [One sentence] |

**Table Specifications:**
- Rows: 6 (1 header + 5 data)
- Columns: 4
- Column Widths:
  - Dimension: 1.8 inches
  - Score: 0.8 inches
  - Status: 1.0 inches
  - Interpretation: 2.9 inches
- Header Row:
  - Background: Primary Blue (#1E3A5F)
  - Text: 11pt Arial Bold, White (#FFFFFF)
  - Alignment: Center
- Data Rows:
  - Column 1 (Dimension): 11pt Arial Bold, Black, Left-aligned
  - Column 2 (Score): 11pt Arial Bold, Black, Center-aligned
  - Column 3 (Status):
    - Text: "✓ PASS" or "✗ FAIL"
    - Font: 11pt Arial Bold
    - Color: Green (#28A745) for PASS, Red (#DC3545) for FAIL
    - Alignment: Center
  - Column 4 (Interpretation): 11pt Arial Regular, Black, Left-aligned
  - Alternating Row Background: White and Light Blue (#E8F4F8)

**Status Indicators:**
- ✓ PASS: Score meets or exceeds threshold
- ✗ FAIL: Score below threshold

**Interpretation Guidelines:**
- Maximum: 1 sentence (10-15 words)
- Focus: Key finding or status summary
- Tone: Objective, evidence-based

**Spacing After:** 12pt

### 1.4 Primary Recommendation

**Heading:** "1.4 Primary Recommendation" (Heading 2, 14pt bold)

**Structure:**

1. **Status Statement:**
   ```
   Status: [RECOMMENDATION TEXT]
   ```
   - "Status: " in 11pt Arial Regular
   - Recommendation text in 11pt Arial Bold
   - Examples: "CONDITIONAL PROCEED with mandatory customer discovery sprint"

2. **Summary Paragraph:**
   - 1-2 paragraphs (11pt Arial Regular)
   - 100-150 words total
   - Explains rationale for recommendation

3. **Critical Validation Gaps:**
   ```
   Critical validation gaps:
   ```
   - Label in 11pt Arial Bold
   - Followed by bulleted list
   - 4-6 bullets maximum
   - Each bullet: 1 sentence, specific gap with implications

4. **Immediate Next Steps:**
   ```
   Immediate next steps (0-90 days):
   ```
   - Label in 11pt Arial Bold
   - Followed by bulleted list
   - 4-6 bullets maximum
   - Each bullet: 1 sentence, actionable step with owner implied

**Bullet List Formatting:**
- Use Word's built-in bullet style (NOT unicode •)
- Indent: 0.25 inches from left margin
- Hanging indent: 0.25 inches
- Font: 11pt Arial Regular
- Color: Black (#000000)

**Spacing After Section:** 18pt before page break

---

## Section 2: Business Model Overview

**Page Break Before This Section**

### 2.1 Value Proposition

**Heading:** "2.1 Value Proposition" (Heading 2, 14pt bold)

**Content:**

1. **Value Proposition Summary:**
   - 1 paragraph, 2-3 sentences
   - 11pt Arial Regular
   - 50-75 words
   - Clearly states: What problem does the solution solve? For whom? How?

2. **Core Differentiation:**
   ```
   Core differentiation:
   ```
   - Label in 11pt Arial Bold
   - Followed by bulleted list
   - 4-6 bullets
   - Each bullet: 1 concise differentiator (5-10 words)

**Spacing After:** 12pt

### 2.2 Target Market Segments

**Heading:** "2.2 Target Market Segments" (Heading 2, 14pt bold)

**Table Structure:**

| Segment | Key Characteristics |
|---------|---------------------|
| **[Segment 1]** | [Description] |
| **[Segment 2]** | [Description] |
| ... | ... |

**Table Specifications:**
- Rows: 1 header + N data (typically 6-10 segments)
- Columns: 2
- Column Widths:
  - Segment: 2.0 inches
  - Key Characteristics: 4.5 inches
- Header Row:
  - Background: Primary Blue (#1E3A5F)
  - Text: 11pt Arial Bold, White (#FFFFFF)
  - Alignment: Center
- Data Rows:
  - Column 1 (Segment): 11pt Arial Bold, Black, Left-aligned
  - Column 2 (Characteristics): 11pt Arial Regular, Black, Left-aligned
  - Alternating Row Background: White and Light Blue (#E8F4F8)

**Segment Guidelines:**
- Name: 2-5 words, specific role or organization type
- Characteristics: 1 sentence (10-15 words)
- Order: Prioritize by importance (most critical segments first)

**Spacing After:** 12pt

### 2.3 Revenue Model

**Heading:** "2.3 Revenue Model" (Heading 2, 14pt bold)

**Content:**

1. **Model Type Statement:**
   ```
   [Model Type] (validated/unvalidated):
   ```
   - Example: "Proposed hybrid model (unvalidated):"
   - 11pt Arial Bold
   - Followed by bulleted list

2. **Revenue Components:**
   - Bulleted list (4-6 bullets)
   - Each bullet format: "[Component]: [Details] ([% of revenue])"
   - Example: "Platform subscription: $400-800/month per facility (60% of revenue)"
   - 11pt Arial Regular

3. **Pricing Warning (if applicable):**
   - Callout box with gray background (#F8F9FA)
   - Left and right indent: 0.25 inches
   - Border: None (background only)
   - Content:
     ```
     Critical pricing validation needed: [Explanation of gaps]
     ```
   - "Critical pricing validation needed: " in 11pt Arial Bold, Red (#DC3545)
   - Explanation in 11pt Arial Regular, Black
   - 1-2 sentences explaining validation gap

**Spacing After Section:** 18pt before page break

---

## Section 3: Evaluation Results

**Page Break Before This Section**

### Introduction

**Heading:** "3. Evaluation Results by Proof of Value" (Heading 1, 16pt bold)

**Introduction Paragraph:**
- 1 paragraph (11pt Arial Regular)
- 2-3 sentences
- Standard text: "The Vianeo evaluation assessed [Project Name] across five interconnected dimensions, each weighted according to importance for commercialization success. This section details findings, evidence, and validation gaps for each proof of value."

**Spacing After:** 12pt

### Dimension Structure (Repeated 5 Times)

**Each dimension follows this exact structure:**

#### Dimension Heading

```
3.X [Dimension Name] ([Weight]%) - Score: X.X/5.0
```

**Example:** "3.1 Legitimacy (15%) - Score: 4.7/5.0"

- Heading level: 2 (14pt bold)
- Format: Section number + dimension name + weight + score
- Color: Black (#000000)

#### Status Line

```
Status: ✓ PASS (Threshold: 3.0)
```

**Format:**
- "Status: " in 11pt Arial Bold
- "✓ PASS" or "✗ FAIL" in 11pt Arial Bold, Green (#28A745) or Red (#DC3545)
- "(Threshold: X.X)" in 11pt Arial Regular, Black

**Spacing After:** 6pt

#### Key Findings Subsection

**Subheading:** "Key Findings" (Heading 3, 12pt bold)

**Summary Paragraph:**
- 1-2 sentences
- 11pt Arial Regular
- 25-50 words
- Concise overview of dimension assessment

**Spacing After:** 6pt

#### Strengths

**Label:** "Strengths:" (11pt Arial Bold)

**Bulleted List:**
- 3-7 bullets (recommended: 5-6)
- Each bullet: 1-2 sentences
- Specific evidence with metrics where possible
- Format: "[Finding] ([Supporting evidence/metric])"
- Example: "13+ doctorate-level researchers with detector physics, Monte Carlo simulation, and nuclear medicine expertise"

**Content Guidelines:**
- Be specific, not generic
- Include quantitative evidence
- Cite sources implicitly (no footnotes)
- Focus on validated facts, not aspirations

**Spacing After:** 12pt

#### Gaps

**Label:** "Gaps:" (11pt Arial Bold)

**Bulleted List:**
- 3-5 bullets (recommended: 4)
- Each bullet: 1-2 sentences
- Specific deficiency with implications
- Format: "[Gap description] ([Implication or consequence])"
- Example: "Zero customer discovery interviews conducted across any stakeholder segment (fundamental assumption validation missing)"

**Content Guidelines:**
- Be direct and honest
- Explain why the gap matters
- Avoid euphemisms
- Balance criticism with constructiveness

**Spacing After:** 18pt before next dimension

### Dimension-Specific Formatting Notes

#### 3.1 Legitimacy (15%)
- Focus: Problem validity, solution credibility, team capability
- Threshold: 3.0
- Strengths typically include: problem validation, team credentials, institutional backing
- Gaps typically include: commercial structure, sustainability pathway

#### 3.2 Desirability (25%)
- Focus: Customer needs, market demand, value proposition fit
- Threshold: 3.5 (HIGHER than others - most important dimension)
- Strengths typically include: identified needs, value proposition clarity
- Gaps typically include: customer discovery completion, validation quality

#### 3.3 Acceptability (20%)
- Focus: Ecosystem support, stakeholder alignment, external validation
- Threshold: 3.0
- Strengths typically include: favorable players, partnerships, regulatory clarity
- Gaps typically include: unfavorable stakeholders, informal relationships

#### 3.4 Feasibility (20%)
- Focus: Technical capability, operational capacity, execution ability
- Threshold: 3.0
- Strengths typically include: prototype functionality, team skills, manufacturing economics
- Gaps typically include: scale-up pathway, regulatory compliance, quality systems

#### 3.5 Viability (20%)
- Focus: Business model sustainability, financial health, scalability
- Threshold: 3.0
- Strengths typically include: revenue model clarity, funding secured, unit economics
- Gaps typically include: pricing validation, customer acquisition, path to profitability

### Page Break Strategy for Dimensions

**Mandatory page breaks:**
- Before each dimension section (3.1, 3.2, 3.3, 3.4, 3.5)
- Exception: No page break before 3.1 (follows introduction on same page)

**Rationale:** Each dimension gets its own page for easy committee review and discussion.

---

## Section 4: Stakeholder Analysis

**Page Break Before This Section**

### 4.1 Priority Personas

**Heading:** "4.1 Priority Personas" (Heading 2, 14pt bold)

**Introduction:**
- 1 sentence introducing the personas
- Example: "Four primary personas identified for customer discovery validation (all hypothetical pending interviews):"
- 11pt Arial Regular

**Spacing After:** 12pt

#### Persona Structure (Repeated 3-4 Times)

**Persona Heading:**
```
[Number]. [Persona Name]
```
**Example:** "1. Nuclear Medicine Physician"

- Heading level: 3 (12pt bold)
- Format: Number + period + space + name
- Color: Black (#000000)

**Profile:**
```
Profile: [One sentence description]
```
- "Profile: " in 11pt Arial Bold
- Description in 11pt Arial Regular
- 10-15 words
- Describes role, context, and key characteristic

**Key Needs:**
```
Key needs (hypothesized/validated):
```
- Label in 11pt Arial Bold
- "(hypothesized)" if unvalidated, "(validated)" if confirmed through interviews
- Bulleted list (3-4 bullets)
- Each bullet: 1 concise need statement (5-10 words)

**Validation Required:**
```
Validation required: [Interview count and objectives]
```
- "Validation required: " in 11pt Arial Bold
- Details in 11pt Arial Regular
- 1 sentence specifying interview count and key objectives
- Example: "15-20 structured interviews to validate needs, understand workflow constraints, test pricing acceptance"

**Spacing After Each Persona:** 12pt

### 4.2 Critical Ecosystem Relationships

**Heading:** "4.2 Critical Ecosystem Relationships" (Heading 2, 14pt bold)

**Table Structure:**

| Relationship | Type | Criticality | Status |
|--------------|------|-------------|--------|
| **[Partner 1]** | [Type] | Critical | Active |
| **[Partner 2]** | [Type] | High | Informal |
| ... | ... | ... | ... |

**Table Specifications:**
- Rows: 1 header + N data (typically 5-8 relationships)
- Columns: 4
- Column Widths:
  - Relationship: 1.8 inches
  - Type: 1.5 inches
  - Criticality: 1.5 inches
  - Status: 1.7 inches
- Header Row:
  - Background: Primary Blue (#1E3A5F)
  - Text: 11pt Arial Bold, White (#FFFFFF)
  - Alignment: Center
- Data Rows:
  - Column 1 (Relationship): 11pt Arial Bold, Black, Left-aligned
  - Column 2 (Type): 11pt Arial Regular, Black, Left-aligned
  - Column 3 (Criticality):
    - Text: "Critical", "High", "Medium", or "Low"
    - Font: 11pt Arial Bold
    - Color:
      - Critical: Red (#DC3545)
      - High: Yellow/Orange (#FFC107)
      - Medium: Green (#28A745)
      - Low: Gray (#6C757D)
    - Alignment: Center
  - Column 4 (Status):
    - Text: "Active", "Funded", "Informal", "Not Engaged", etc.
    - Font: 11pt Arial Bold
    - Color:
      - Active/Funded: Green (#28A745)
      - Informal/Not Engaged: Yellow (#FFC107)
      - Other: Gray (#6C757D)
    - Alignment: Center
  - Alternating Row Background: White and Light Blue (#E8F4F8)

**Spacing After Section:** 18pt before page break

---

## Section 5: Recommendations

**Page Break Before This Section**

### 5.1 Immediate Priorities (0-30 Days)

**Heading:** "5.1 Immediate Priorities (0-30 Days)" (Heading 2, 14pt bold)

#### Priority Structure (Repeated 3 Times)

**Priority Heading:**
```
[Number]. [Action Name]
```
**Example:** "1. Launch Customer Discovery Sprint"

- Heading level: 3 (12pt bold)
- Format: Number + period + space + name
- Color: Black (#000000)

**Owner:**
```
Owner: [Name/Role]
```
- "Owner: " in 11pt Arial Bold
- Name/Role in 11pt Arial Regular

**Timeline:**
```
Timeline: [Specific timeframe]
```
- "Timeline: " in 11pt Arial Bold
- Timeframe in 11pt Arial Regular
- Example: "Initiate within 7 days, complete 40-60 interviews within 60 days"

**Items:**
```
[Success Metrics / Action Items / Required Terms]:
```
- Label in 11pt Arial Bold
- Choose appropriate label based on context:
  - "Success Metrics:" for outcome-focused priorities
  - "Action Items:" for task-focused priorities
  - "Required Terms:" for partnership/agreement priorities
- Bulleted list (4-7 bullets)
- Each bullet: 1 specific, measurable item

**Spacing After Each Priority:** 12pt

### 5.2 Short-Term Validation (30-90 Days)

**Heading:** "5.2 Short-Term Validation (30-90 Days)" (Heading 2, 14pt bold)

**Structure:** Same as 5.1 Immediate Priorities (3 priorities)

**Numbering:** Continue from previous section (e.g., if 5.1 had 3 items, 5.2 starts at "4.")

### 5.3 Medium-Term Priorities (90-180 Days)

**Page Break Before This Subsection**

**Heading:** "5.3 Medium-Term Priorities (90-180 Days)" (Heading 2, 14pt bold)

#### Priority Structure (Condensed - Repeated 3 Times)

**Priority Heading:**
```
[Number]. [Action Name]
```
**Example:** "7. Develop Reference Site Strategy"

- Heading level: 3 (12pt bold)
- Numbering continues from previous subsections

**Description:**
- 1-2 paragraphs (11pt Arial Regular)
- 50-100 words
- No Owner, Timeline, or Items (condensed format)
- Explains objective and approach

**Spacing After Each Priority:** 12pt

### 5.4 Risk Mitigation Strategies

**Heading:** "5.4 Risk Mitigation Strategies" (Heading 2, 14pt bold)

**Table Structure:**

| Risk | Impact | Mitigation Strategy |
|------|--------|---------------------|
| **[Risk 1]** | Critical | [Strategy description] |
| **[Risk 2]** | High | [Strategy description] |
| ... | ... | ... |

**Table Specifications:**
- Rows: 1 header + N data (typically 5-7 risks)
- Columns: 3
- Column Widths:
  - Risk: 2.0 inches
  - Impact: 1.0 inches
  - Mitigation Strategy: 3.5 inches
- Header Row:
  - Background: Primary Blue (#1E3A5F)
  - Text: 11pt Arial Bold, White (#FFFFFF)
  - Alignment: Center
- Data Rows:
  - Column 1 (Risk): 11pt Arial Bold, Black, Left-aligned
  - Column 2 (Impact):
    - Text: "Critical", "High", "Medium", or "Low"
    - Font: 11pt Arial Bold
    - Color:
      - Critical: Red (#DC3545)
      - High: Yellow/Orange (#FFC107)
      - Medium: Green (#28A745)
      - Low: Gray (#6C757D)
    - Alignment: Center
  - Column 3 (Mitigation Strategy): 11pt Arial Regular, Black, Left-aligned
  - Alternating Row Background: White and Light Blue (#E8F4F8)

**Risk Description Guidelines:**
- 1 sentence, 10-15 words
- Specific scenario, not generic
- Example: "Customer validation reveals pricing disconnect" (not "Pricing might be wrong")

**Mitigation Strategy Guidelines:**
- 1-2 sentences, 20-30 words
- Actionable, specific approach
- Includes contingency or alternative
- Example: "Develop dual pricing: international/private markets cross-subsidize SUS access. Explore grant/subsidy programs for public health impact."

**Spacing After Section:** 18pt before page break

---

## Section 6: Conclusion

**Page Break Before This Section**

### Summary Paragraphs

**Heading:** "6. Conclusion" (Heading 1, 16pt bold)

**Content:** 4 paragraphs (11pt Arial Regular)

**Paragraph 1:** Overall assessment and strengths
- 3-5 sentences
- Summarize key achievements
- Reference overall score and key strengths

**Paragraph 2:** Key gaps and their implications
- 3-5 sentences
- Explain primary challenges
- Connect to market maturity score if applicable

**Paragraph 3:** The path forward (bold emphasis on recommendation)
- 2-4 sentences
- Begin with "The path forward is clear:" in bold
- Outline immediate required actions

**Paragraph 4:** Final recommendation with sprint/validation requirements
- 2-4 sentences
- Begin with "The assessment recommends [RECOMMENDATION]" where recommendation is bold
- Specify conditions and timeline

**Spacing After:** 12pt

### 6.1 Next Review Checkpoint

**Heading:** "6.1 Next Review Checkpoint" (Heading 2, 14pt bold)

**Timing:**
```
Timing: [Date/timeframe]
```
- "Timing: " in 11pt Arial Bold
- Date/timeframe in 11pt Arial Regular
- Example: "February 2026 (post customer discovery sprint completion)"

**Expected Deliverables:**
```
Expected Deliverables:
```
- Label in 11pt Arial Bold
- Bulleted list (4-6 bullets)
- Each bullet: 1 specific deliverable
- Example: "Customer discovery report with validated pricing and needs"

**Success Criteria:**
```
Success Criteria for [Next Stage]:
```
- Label format: "Success Criteria for Series A Readiness:" (or relevant next stage)
- Label in 11pt Arial Bold
- Bulleted list (4-6 bullets)
- Each bullet: 1 measurable criterion with threshold
- Example: "Market maturity score improved to 3.2+ (currently 3.1)"

**Spacing After:** 18pt

### Footer

**Format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
— End of Report —
(Italic, centered)

Prepared by 360 Social Impact Studios
[Author Name], [Title]
Using Vianeo Business Model Evaluation Framework
[Date]
```

**Styling:**
- "— End of Report —" in 11pt Arial Italic, centered
- Spacing: 12pt before and after
- "Prepared by..." lines in 11pt Arial Regular/Bold, centered
- Bold: "Prepared by 360 Social Impact Studios" and author name
- Regular: Title, framework line, date
- Spacing between lines: 6pt

**No page break after conclusion - this is the final page.**

---

## Page Break Strategy

### Mandatory Page Breaks

**Location** | **Rationale**
-------------|---------------
After Cover Page | Start content on fresh page
Before Section 2: Business Model Overview | New major section
Before Section 3: Evaluation Results | New major section
Before 3.2 Desirability | Each dimension on own page
Before 3.3 Acceptability | Each dimension on own page
Before 3.4 Feasibility | Each dimension on own page
Before 3.5 Viability | Each dimension on own page
Before Section 4: Stakeholder Analysis | New major section
Before Section 5: Recommendations | New major section
Before 5.3 Medium-Term Priorities | Subsection separation
Before Section 6: Conclusion | New major section

### No Page Break

**Location** | **Rationale**
-------------|---------------
Before 3.1 Legitimacy | Follows introduction on same page
Between 5.1 and 5.2 | Related subsections flow together
Within personas | Keep each persona together
Within priorities | Keep each priority together
After Section 6 | Final page of document

### White Space Tolerance

**It is acceptable to have white space at the bottom of pages** when page breaks are used. This improves readability and allows committee members to easily navigate to specific sections.

**Do NOT artificially expand content to fill pages.** Concise, precise content is preferred.

---

## Table Specifications

### General Table Properties

**Property** | **Value**
-------------|----------
Border Style | Single solid line
Border Width | 1pt
Border Color | #CCCCCC (light gray)
Cell Padding (Top/Bottom) | 8pt
Cell Padding (Left/Right) | 12pt
Table Alignment | Left
Table Width | 6.5 inches (full text width)
Vertical Cell Alignment | Middle

### Column Width Guidelines

**Use absolute widths (inches or DXA), not percentages.**

**Common Column Widths:**
- Narrow (Dimension, Score): 0.8-1.0 inches
- Medium (Status, Criticality): 1.0-1.5 inches
- Wide (Description, Interpretation): 2.5-4.5 inches

**Total Must Equal:** 6.5 inches (text width between margins)

**DXA Conversion:**
- 1 inch = 1440 DXA
- 0.5 inches = 720 DXA
- 2.0 inches = 2880 DXA

### Header Row Styling

**Property** | **Value**
-------------|----------
Background Color | Primary Blue (#1E3A5F)
Text Color | White (#FFFFFF)
Font Weight | Bold
Font Size | 11pt
Alignment | Center
Vertical Alignment | Middle

### Data Row Styling

**Alternating Rows:**
- Odd rows (1st, 3rd, 5th...): White background (#FFFFFF)
- Even rows (2nd, 4th, 6th...): Light Blue background (#E8F4F8)

**Text Formatting:**
- Font Size: 11pt
- Base Color: Black (#000000)
- Special Colors: See color palette for status indicators

### Status Indicator Colors

**Status** | **Color** | **Hex Code**
-----------|-----------|-------------
PASS | Green | #28A745
FAIL | Red | #DC3545
Critical | Red | #DC3545
High | Yellow/Orange | #FFC107
Medium | Green | #28A745
Low | Gray | #6C757D
Active | Green | #28A745
Funded | Green | #28A745
Informal | Yellow | #FFC107
Not Engaged | Yellow | #FFC107

---

## Color Palette

### Primary Colors

**Name** | **Hex Code** | **RGB** | **Usage**
---------|-------------|---------|----------
Primary Blue | #1E3A5F | 30, 58, 95 | Headings, table headers
Secondary Blue | #2E5A7F | 46, 90, 127 | Accents, subtitles
Light Blue | #E8F4F8 | 232, 244, 248 | Alternating table rows

### Status Colors

**Name** | **Hex Code** | **RGB** | **Usage**
---------|-------------|---------|----------
Success Green | #28A745 | 40, 167, 69 | PASS, Active, Medium
Warning Yellow | #FFC107 | 255, 193, 7 | CONDITIONAL, High, Informal
Danger Red | #DC3545 | 220, 53, 69 | FAIL, Critical, NO-GO

### Neutral Colors

**Name** | **Hex Code** | **RGB** | **Usage**
---------|-------------|---------|----------
Black | #000000 | 0, 0, 0 | Body text
Gray | #6C757D | 108, 117, 125 | Secondary text, Low status
Light Gray | #F8F9FA | 248, 249, 250 | Backgrounds, callouts
White | #FFFFFF | 255, 255, 255 | Page background, table cells

### Color Application Rules

1. **Never use colors not in this palette** (except in charts/graphs if needed)
2. **Maintain WCAG AA contrast ratios:**
   - White text on Primary Blue: ✓ Pass (7.7:1)
   - Black text on White: ✓ Pass (21:1)
   - Black text on Light Blue: ✓ Pass (18.2:1)
3. **Color-code consistently:**
   - Green always means positive/pass/active
   - Red always means negative/fail/critical
   - Yellow always means caution/conditional/informal

---

## Validation Checklist

### Pre-Generation

- [ ] All data fields populated (no empty strings or nulls)
- [ ] Scores are valid floats between 0.0 and 5.0
- [ ] Status values are "PASS" or "FAIL" (exact case)
- [ ] All lists have minimum required items (e.g., 3 strengths per dimension)
- [ ] Dates are properly formatted (e.g., "December 8, 2025")
- [ ] No placeholder text (e.g., "[Insert X]") remains

### Document Structure

- [ ] Cover page present with complete metadata table
- [ ] All 6 sections present in correct order
- [ ] Page breaks occur at specified locations (11 total)
- [ ] Headers and footers appear on all pages (except cover for header)
- [ ] Page numbers are sequential and correct

### Typography & Formatting

- [ ] All headings use correct levels (H1 for sections, H2 for subsections, H3 for items)
- [ ] Font sizes match specification (Title 28pt, H1 16pt, H2 14pt, H3 12pt, Body 11pt)
- [ ] Colors match palette exactly (use hex codes, not "blue" or "green")
- [ ] Bullet lists use Word formatting (not unicode characters like •)
- [ ] No em dashes (—) anywhere in document (use commas or periods)

### Tables

- [ ] All tables have headers with blue background and white text
- [ ] Alternating row shading (white and light blue) applied
- [ ] Column widths specified and sum to 6.5 inches
- [ ] Status indicators use correct colors (green for PASS, red for FAIL)
- [ ] Cell alignment correct (center for headers and scores, left for text)

### Content Quality

- [ ] Executive summary accurately reflects overall assessment
- [ ] All dimension scores match key findings table
- [ ] Strengths are specific with evidence (not generic)
- [ ] Gaps are honest and constructive (not euphemistic)
- [ ] Recommendations have owners and timelines
- [ ] Risk mitigation strategies are actionable
- [ ] Conclusion paragraphs flow logically (strengths → gaps → path → recommendation)

### Technical Validation

- [ ] Document opens without errors in Microsoft Word
- [ ] Document opens without errors in Google Docs
- [ ] Document opens without errors in LibreOffice
- [ ] PDF conversion preserves formatting
- [ ] File size is reasonable (<5MB for DOCX, <10MB for PDF)

---

## Common Mistakes

### Content Mistakes

**❌ Mistake** | **✓ Correct**
--------------|-------------
"The team is strong" | "13+ doctorate-level researchers with detector physics, Monte Carlo simulation, and nuclear medicine expertise"
"We recommend customer discovery" | "Execute 40-60 structured customer discovery interviews across all stakeholder segments within 60 days (Owner: Daniel Bonifacio)"
"(hypothesized)" when interviews completed | "(validated)" with interview count
"Market need exists" | "20-29% treatment failure rates in current fixed-dose I-131 therapy documented in published literature"
"Pricing to be determined" | "Pricing assumptions ($400-800/month) untested against SUS budget constraints"

### Formatting Mistakes

**❌ Mistake** | **✓ Correct**
--------------|-------------
Using • for bullets | Use Word's built-in bullet formatting
Using em dashes (—) | Use commas, periods, or parentheses
Color names ("blue") | Hex codes (#1E3A5F)
Relative column widths (33%) | Absolute widths (2.0 inches)
Missing alternating row colors | White and light blue (#E8F4F8) alternating
Text alignment inconsistent | Center for headers/scores, left for text
Status text without color | Green for PASS, red for FAIL

### Structure Mistakes

**❌ Mistake** | **✓ Correct**
--------------|-------------
Missing page breaks | Page break before each major section
4 paragraphs in project overview | Exactly 3 paragraphs
8 strengths for a dimension | 5-6 strengths (3-7 range)
Generic persona names | Specific role names ("Nuclear Medicine Physician")
Priorities without owners | Every priority has "Owner: [Name/Role]"
Risks without impact ratings | Every risk has "Impact: [Critical/High/Medium/Low]"

### Data Quality Mistakes

**❌ Mistake** | **✓ Correct**
--------------|-------------
Score: "4" | Score: "4.0/5.0" or "4.0"
Status: "Pass" | Status: "PASS" (all caps)
Weight: "20" | Weight: "20%"
Empty validation gaps list | 4-6 specific validation gaps
No interview counts | "15-20 structured interviews to validate..."
Unvalidated marked as validated | Clearly mark "(unvalidated)" or "(hypothesized)"

---

## File Naming Convention

### DOCX Format

```
[ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].docx
```

**Examples:**
- `IRDose_Vianeo_Sprint_Executive_Report_20251208.docx`
- `NanoSense_Vianeo_Sprint_Executive_Report_20260115.docx`

### Markdown Format

```
[ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].md
```

**Examples:**
- `IRDose_Vianeo_Sprint_Executive_Report_20251208.md`
- `NanoSense_Vianeo_Sprint_Executive_Report_20260115.md`

### PDF Format (if converted)

```
[ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].pdf
```

**Examples:**
- `IRDose_Vianeo_Sprint_Executive_Report_20251208.pdf`

### Rules

1. **No spaces** in filename (use underscores)
2. **Consistent capitalization:** PascalCase for project name, consistent case for other parts
3. **Date format:** YYYYMMDD (sortable, unambiguous)
4. **Extensions:** Always lowercase (.docx, .md, .pdf)
5. **Version control:** Use git for versioning, not "_v2" suffixes

---

## Appendix: Python Implementation Notes

### Using the Generator

**Basic Usage:**
```bash
python tools/generators/generate_executive_sprint_report.py \
  --input examples/executive_sprint_report_irdose_sample.yaml \
  --output IRDose_Sprint_Report
```

**Options:**
- `--input, -i`: Path to YAML or JSON data file
- `--output, -o`: Output file path (without extension)
- `--format, -f`: Output format (`docx`, `md`, or `both` [default])

### Data File Structure

See `examples/executive_sprint_report_irdose_sample.yaml` for complete example.

**Key Sections:**
- Metadata (project_name, dates, authors)
- Scores (overall_vianeo_score, market_maturity_score, status)
- key_findings (list of DimensionScore objects)
- project_overview (list of 3 paragraphs)
- Dimension details (legitimacy, desirability, acceptability, feasibility, viability)
- personas (list of Persona objects)
- ecosystem_relationships (list of EcosystemRelationship objects)
- Priorities (immediate_priorities, short_term_validation, medium_term_priorities)
- risk_mitigation (list of RiskMitigation objects)
- conclusion (list of 4 paragraphs)
- next_review (NextReview object)

### Troubleshooting

**Issue:** python-docx not installed
**Solution:** `pip install python-docx`

**Issue:** YAML parsing error
**Solution:** Validate YAML syntax with online validator

**Issue:** Missing required field
**Solution:** Check data file against ExecutiveSprintReportData dataclass

**Issue:** Table columns don't align
**Solution:** Verify column widths sum to 6.5 inches

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-08 | Initial release |

---

## Maintainer Contact

**360 Social Impact Studios**
**Email:** contact@360socialimpact.com
**Documentation:** See `docs/` directory for additional guides

---

**End of Format Specification**
