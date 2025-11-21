# Format Specification: Step 10 - VIANEO Diagnostic Comment

**Version:** 1.0
**Last Updated:** 2025-11-21
**Purpose:** Complete format specification for creating VIANEO Main Diagnostic Comment outputs
**Time Budget:** 25-35 minutes total

---

## Overview

The VIANEO Diagnostic Comment is the final deliverable (Step 10) of the VIANEO Business Model Evaluation Playbook. It synthesizes findings from all prior assessments into a concise, actionable executive document that drives decision-making.

**Core Philosophy:**
- **Conciseness over comprehensiveness** (6-8 sentences total in executive diagnostic)
- **Specificity over abstraction** (numbers, names, concrete examples)
- **Actionability over analysis** (owners and deadlines)
- **Evidence-based over aspirational** (validated facts, not hopes)

**Deliverables:**
1. Markdown version (structured data, version-controllable)
2. Professional DOCX version (presentation-ready, design-elevated)

**Both outputs contain identical content.** The DOCX adds professional formatting but does not alter or supplement the markdown content.

---

## 1. Document Header

The header provides essential metadata and context for the diagnostic.

### Required Elements

```markdown
# [Project Name]: Vianeo Main Diagnostic Comment

**Date:** [Current Date in YYYY-MM-DD format]
**Assessment Framework:** Vianeo Business Model Evaluation Playbook
**Overall Maturity:** [Stage Classification]
```

### Project Name
- Use the official business/project name exactly as it appears in assessment materials
- Capitalize appropriately
- Examples: "Rayla AI", "TechVenture Solutions", "GreenPath Energy"

### Date
- Format: Full date (e.g., "November 21, 2025" or "2025-11-21")
- Use the date when the diagnostic is finalized, not when assessment began
- Consistency: Use same date format throughout all outputs

### Overall Maturity
Choose the stage that best reflects the venture's current state:
- **Concept Stage** - Idea validation, no product
- **Early Commercialization** - MVP built, seeking first customers
- **Growth Stage** - Product-market fit demonstrated, scaling
- **Scaling Stage** - Established operations, rapid expansion
- **Mature** - Established market position, optimization focus

### Markdown Formatting
```markdown
# [Project Name]: Vianeo Main Diagnostic Comment

**Date:** November 21, 2025
**Assessment Framework:** Vianeo Business Model Evaluation Playbook
**Overall Maturity:** Early Commercialization

---
```

### DOCX Formatting
- **Title:** 24pt, bold, deep blue (#1B365D), left-aligned
- **Metadata lines:** 9pt, regular, light gray (#757575)
- **Spacing:** Title: 0pt before, 240pt after; Metadata: 60pt after each line
- **Font:** Calibri throughout

---

## 2. Executive Diagnostic

The Executive Diagnostic is the most critical section. It must be exactly **6-8 sentences total** across four paragraphs.

### Overall Structure

1. **Strengths** (1-2 sentences)
2. **Risks** (1-2 sentences)
3. **Near-term Actions** (2-3 sentences)
4. **Evidence Gaps** (1-2 sentences)

**Total: 6-8 sentences across all four paragraphs combined.**

### 2.1 Strengths Paragraph

**Purpose:** Highlight validated assets and competitive advantages that increase likelihood of success.

**Length:** 1-2 sentences

**Content Requirements:**
- Lead with strongest validation (external > internal > self-reported)
- Include specific numbers (e.g., "50+ beta users", "10+ years domain expertise")
- Name people, partners, technologies, or entities
- Use concrete examples (e.g., "1 documented funded grant proves real-world efficacy")
- Focus on evidence-backed capabilities across the 5 proofs of value
- No generic statements ("promising opportunity", "strong team")

**Evidence Hierarchy:**
1. **External validation** (paying customers, partnerships, funded grants, patents granted)
2. **Internal validation** (beta users, prototypes tested, provisional patents)
3. **Self-reported** (founder claims, aspirational partnerships)

**Good Example:**
> "Rayla AI demonstrates strong technical differentiation with patent-pending multi-model orchestration and grant-specific training data, creating barriers difficult for generic AI competitors to replicate. Founder brings rare 10+ year domain expertise in grant strategy, validated through prior service clients who secured millions in funding."

**Bad Example:**
> "The team has good experience and the technology seems promising. Early customer feedback has been positive and the market opportunity appears large."

**Quality Checks:**
- ✓ Can you replace generic terms with specific names/numbers?
- ✓ Does every claim have supporting evidence from assessment?
- ✓ Would this paragraph apply to a different business? (If yes, revise)
- ✓ Are you leading with the strongest proof point?

### 2.2 Risks Paragraph

**Purpose:** Identify critical vulnerabilities and misalignments that threaten viability.

**Length:** 1-2 sentences

**Content Requirements:**
- Prioritize systemic issues over minor gaps
- Be direct and specific (no hedging: "may", "might", "possibly")
- Quantify where possible (e.g., "zero paying customers", "3 ventures diluting focus")
- Connect to specific dimension scores
- Focus on material risks that affect viability
- No downplaying language

**Severity Hierarchy:**
1. **Critical** - Threatens venture existence (zero revenue, no technical capability)
2. **High** - Major execution blockers (fragmented focus, unvalidated pricing)
3. **Medium** - Significant gaps (thin evidence, missing expertise)

**Good Example:**
> "Revenue model remains entirely unvalidated with zero paying customers despite operational beta, indicating critical pricing and willingness-to-pay uncertainty. Team structure creates execution risk: CTO lacks distinctive AI/ML credentials, development outsourced to contractors, no technical co-founder, and missing nonprofit executive or regulatory expertise."

**Bad Example:**
> "There are some concerns about market adoption and the team could benefit from additional startup experience. Manufacturing timelines may need optimization."

**Quality Checks:**
- ✓ Would you bet your own money given these risks? (If no, they're stated correctly)
- ✓ Are you being direct without hedging?
- ✓ Is every risk quantified or specific?
- ✓ Do risks connect to dimension scores?

### 2.3 Near-term Actions Paragraph

**Purpose:** Provide concrete, delegation-ready actions with owners and measurable outcomes.

**Length:** 2-3 sentences covering 3-4 actions

**Content Requirements:**
- Format: "[Owner Name] should [specific action] to [measurable outcome]"
- Each action must have responsible owner in parentheses
- 30-60 day timeframe (immediate execution window)
- Measurable outcomes (numbers, thresholds, completion criteria)
- Address critical risks or capitalize on strengths
- Use delegation-ready language (can hand to owner as-is)

**Action Quality Standards:**
- **Specific:** Not "talk to customers" but "conduct 40-60 structured interviews"
- **Measurable:** Not "improve conversion" but "target 40% beta-to-paid conversion rate"
- **Time-bound:** Not "eventually" but "within 90 days"
- **Owned:** Not "the team" but "Shawna" or "Leadership team (Shawna, Soufiane)"

**Good Example:**
> "Shawna should immediately convert 20+ beta users to paid subscriptions (target 40% conversion rate) to validate $20-50 ARPU pricing hypothesis and establish first revenue proof point. Leadership team (Shawna, Soufiane) must conduct 40-60 structured customer interviews (5-10 per segment) using standardized protocol to validate needs qualification matrix and refine ICP. Shawna should clarify founder time allocation and establish plan to wind down or delegate Intention Labs and IPN within 90 days, demonstrating exclusive focus required for venture-scale execution."

**Bad Example:**
> "The team should talk to more customers to better understand the market. Consider adjusting pricing strategy. Continue building the product and exploring partnerships."

**Quality Checks:**
- ✓ Can you hand this directly to the owner? (If no, not specific enough)
- ✓ Does each action have a clear owner?
- ✓ Are outcomes measurable with specific numbers?
- ✓ Is the 30-60 day timeframe realistic?

### 2.4 Evidence Gaps Paragraph

**Purpose:** Note missing validation that limits confidence in scoring and decision-making.

**Length:** 1-2 sentences

**Content Requirements:**
- Focus on **material gaps** that affect decision-making
- Be specific about what's missing (not "more research needed")
- Group logically by category (customer, competitive, financial, team, ecosystem)
- Explain why each gap matters
- **Different from Risks section** (gaps are missing data, risks are known problems)
- No nitpicking or minor documentation issues

**Gap Categories:**
- **Customer:** Interview methodology, sample sizes, needs framework
- **Competitive:** Firsthand testing, feature parity, pricing comparison
- **Financial:** Unit economics, CAC measurement, LTV validation, burn rate
- **Team:** Equity structure, vesting schedules, domain credentials
- **Ecosystem:** Regulatory strategy, partnership terms, influencer mapping

**Good Example:**
> "Customer interview methodology completely undocumented (sample sizes unclear, no validated needs prioritization framework, buyer vs. user distinction unmapped). Competitive intelligence lacks depth: no firsthand testing of Instrumentl or Grantable, pricing comparison incomplete, feature parity unassessed, churn drivers unknown."

**Bad Example:**
> "Some additional documentation would be helpful. More customer interviews could provide useful insights. Team bios could be more detailed."

**Quality Checks:**
- ✓ Would having this information change your confidence in scores? (If no, not material)
- ✓ Are you specific about what's missing?
- ✓ Is this different from the Risks paragraph?
- ✓ Are gaps grouped logically?

### Markdown Formatting

```markdown
## Executive Diagnostic

### Strengths

[1-2 sentences with specific numbers, names, and evidence]

### Risks

[1-2 sentences with quantified, direct risks]

### Near-term Actions (30-60 days)

[2-3 sentences with 3-4 actions, each with owner in parentheses]

### Evidence Gaps

[1-2 sentences with material gaps grouped by category]

---
```

### DOCX Formatting

- **Section Header (Executive Diagnostic):** 16pt, bold, deep blue (#1B365D), 360pt before, 180pt after
- **Subsection Headers (Strengths, Risks, etc.):** 14pt, bold, medium gray (#4A4A4A), 240pt before, 120pt after
- **Body Paragraphs:** 11pt, body gray (#2D2D2D), line height 1.6x (360 DXA), 240pt after
- **Font:** Calibri

---

## 3. Dimension Summary Table

The Dimension Summary provides at-a-glance scoring across the five VIANEO dimensions.

### Required Elements

**Table Structure:**
- 3 columns: Dimension | Score | Interpretation
- 5 rows (one per dimension): Legitimacy, Desirability, Acceptability, Feasibility, Viability
- Header row with column labels
- Overall status statement below table

### 3.1 Dimension Scores

**Score Format:** X.X/5 (one decimal place)

**All five dimensions required:**
1. **Legitimacy** - Real problem, genuine solution, capable team
2. **Desirability** - Customer want, validated need, market demand
3. **Acceptability** - Ecosystem support, stakeholder alignment, external validation
4. **Feasibility** - Technical capability, operational capacity, execution ability
5. **Viability** - Business model sustainability, financial health, scalability

**Critical:** Scores must match source assessment data exactly. Do not round or adjust.

### 3.2 Status Keywords by Score Range

Use these exact keywords based on score:

- **4.5-5.0:** Strong
- **3.5-4.4:** Promising
- **3.0-3.4:** Developing
- **2.0-2.9:** Problematic
- **<2.0:** Non-viable

### 3.3 Interpretation Format

**Structure:** [Status Keyword] - [Brief specific explanation, 5-10 words]

**Requirements:**
- Use appropriate status keyword from score range
- Brief explanation specific to this venture (not generic)
- 5-10 words maximum
- Connects to key findings from detailed assessments

**Examples:**
- "Promising - Strong early signals, but thin evidence base requires validation"
- "Problematic - Pre-revenue, unvalidated unit economics, fundraising dependent"
- "Strong - Real problem, validated solution, experienced team, proven traction"

### 3.4 Overall Status Statement

**Location:** Immediately below table

**Format:** [Status category] requiring [what's needed]. [Key trade-off or balance statement].

**Requirements:**
- Synthesizes the five dimensions into overall assessment
- Balances strengths and weaknesses
- Provides clear implication for next steps
- Specific to this venture

**Example:**
> "**Overall Status:** Promising opportunity requiring significant de-risking before institutional investment. Strong market fit and differentiated technology offset by execution gaps and unvalidated business model."

### Markdown Formatting

```markdown
## Dimension Summary

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| **Legitimacy** | 3.5/5 | Promising - Real problem, genuine advantages, but team/financial gaps |
| **Desirability** | 3.5/5 | Promising - Strong early signals, but thin evidence base |
| **Acceptability** | 3.0/5 | Developing - Mixed ecosystem, key influencer positions undefined |
| **Feasibility** | 3.0/5 | Developing - Technical capability adequate, execution risk high |
| **Viability** | 2.5/5 | Problematic - Pre-revenue, unvalidated economics, fundraising dependent |

**Overall Status:** Promising opportunity requiring significant de-risking before institutional investment. Strong market fit and differentiated technology offset by execution gaps and unvalidated business model.

---
```

### DOCX Formatting

**Column Widths (DXA):**
- Dimension: 3120
- Score: 1560
- Interpretation: 4680
- **Total: 9360** (fits letter width with 1" margins)

**CRITICAL:** Set BOTH `columnWidths` array AND individual cell widths.

**All Cells:**
- Borders: Light gray (#CCCCCC), 1pt, all sides
- Cell margins: 100pt top/bottom, 180pt left/right

**Header Row:**
- Background: Soft blue-gray (#E8EDF2)
- Text: Bold, 11pt, centered

**Data Rows:**
- Dimension column: Bold text, left-aligned
- Score column: Bold text, centered, **color-coded background**
- Interpretation column: Regular text, left-aligned

**Score Cell Color Coding:**
- Score ≥3.5: Green background (#D4EDDA)
- Score 3.0-3.4: Yellow background (#FFF3CD)
- Score <3.0: Red background (#F8D7DA)

**Overall Status:**
- Regular paragraph below table
- 11pt, body gray (#2D2D2D)
- "Overall Status:" in bold

---

## 4. Critical Path Forward

The Critical Path provides phased, prioritized actions across four time horizons.

### Structure

Four required sections:
1. **Immediate Priority (Weeks 1-4)** - Max 3 actions
2. **Short-term Priority (Months 2-3)** - Max 4 actions
3. **Medium-term Priority (Months 4-6)** - Max 4 actions
4. **Success Metrics** - Max 6 metrics

### 4.1 Immediate Priority (Weeks 1-4)

**Purpose:** Urgent actions to address critical risks or capture quick wins

**Item Count:** Maximum 3 actions

**Requirements:**
- Address most critical risk identified in Risks section
- Quick wins with measurable outcomes
- Can be completed within 1-4 weeks
- Specific and actionable (not "explore" or "consider")

**Format:**
```markdown
### Immediate Priority (Weeks 1-4)

1. [First urgent action - most critical risk or quick win]
2. [Second urgent action]
3. [Third urgent action]
```

**Example:**
1. Launch paid tiers to beta cohort, target 20+ conversions
2. Begin systematic customer interview program (10 interviews/week)
3. Document team equity structure and founder time allocation plan

### 4.2 Short-term Priority (Months 2-3)

**Purpose:** Validation and capability-building actions

**Item Count:** Maximum 4 actions

**Requirements:**
- Build on immediate actions
- Focus on validation (customer, market, technical)
- Strengthen core capabilities
- Prepare for medium-term strategic moves

**Format:**
```markdown
### Short-term Priority (Months 2-3)

1. [First validation/capability building action]
2. [Second validation/capability building action]
3. [Third validation/capability building action]
4. [Fourth validation/capability building action]
```

**Example:**
1. Achieve $10K MRR from paying customers (200+ users at $50 ARPU)
2. Complete 40-60 customer interviews across all segments
3. Internalize technical development or hire VP Engineering
4. Test competitive solutions firsthand and update positioning

### 4.3 Medium-term Priority (Months 4-6)

**Purpose:** Strategic positioning and infrastructure development

**Item Count:** Maximum 4 actions

**Requirements:**
- Build on validated learnings from short-term
- Strategic positioning and differentiation
- Infrastructure and systems development
- Prepare for scaling or next funding

**Format:**
```markdown
### Medium-term Priority (Months 4-6)

1. [First strategic positioning/infrastructure action]
2. [Second strategic positioning/infrastructure action]
3. [Third strategic positioning/infrastructure action]
4. [Fourth strategic positioning/infrastructure action]
```

**Example:**
1. Demonstrate clear founder focus (Intention Labs/IPN transitioned)
2. Validate unit economics with actual cohort data (CAC, LTV, churn)
3. Strengthen IP position (file utility patent, document FTO analysis)
4. Map ecosystem gatekeepers and develop regulatory strategy

### 4.4 Success Metrics

**Purpose:** Measurable thresholds that indicate progress and validate strategy

**Item Count:** Maximum 6 metrics

**Requirements:**
- Specific thresholds (not "improve" or "increase")
- Measurable objectively
- Mix of input and output metrics
- Timeframes included where applicable
- Aligned with actions in critical path

**Format:**
```markdown
### Success Metrics

- [Metric 1 with specific threshold, e.g., "40%+ beta-to-paid conversion rate"]
- [Metric 2 with specific threshold, e.g., "<$300 CAC validated across channels"]
- [Metric 3 with specific threshold, e.g., "LTV:CAC ratio >3:1 within 18 months"]
- [Metric 4 with specific threshold]
- [Metric 5 with specific threshold]
- [Metric 6 with specific threshold]
```

**Example:**
- 40%+ beta-to-paid conversion rate
- <$300 CAC validated across channels
- LTV:CAC ratio >3:1 within 18 months
- <10% monthly churn rate
- NPS >50 from paying customers
- 10+ documented funded grants by end of Year 1

**Metric Quality Standards:**
- **Specific:** Not "improve NPS" but "NPS >50 from paying customers"
- **Measurable:** Not "better engagement" but "<10% monthly churn rate"
- **Time-bound:** Include timeframes where relevant
- **Threshold:** Use specific numbers with comparison operators (>, <, ≥, ≤)

### Markdown Formatting

```markdown
## Critical Path Forward

### Immediate Priority (Weeks 1-4)

1. [Action 1]
2. [Action 2]
3. [Action 3]

### Short-term Priority (Months 2-3)

1. [Action 1]
2. [Action 2]
3. [Action 3]
4. [Action 4]

### Medium-term Priority (Months 4-6)

1. [Action 1]
2. [Action 2]
3. [Action 3]
4. [Action 4]

### Success Metrics

- [Metric 1]
- [Metric 2]
- [Metric 3]
- [Metric 4]
- [Metric 5]
- [Metric 6]

---
```

### DOCX Formatting

**Section Header:** 16pt, bold, deep blue (#1B365D), 360pt before, 180pt after

**Subsection Headers:** 14pt, bold, medium gray (#4A4A4A), 240pt before, 120pt after

**Numbered Lists:**
- **CRITICAL:** Each section needs unique reference to restart numbering
- Left indent: 720pt, Hanging indent: 360pt
- Format: Decimal (1., 2., 3.)

**Example numbering references:**
- Immediate Priority: `{ reference: "immediate-list", level: 0, format: LevelFormat.DECIMAL }`
- Short-term Priority: `{ reference: "short-term-list", level: 0, format: LevelFormat.DECIMAL }`
- Medium-term Priority: `{ reference: "medium-term-list", level: 0, format: LevelFormat.DECIMAL }`

**Bullet List (Success Metrics):**
- Reference: `{ reference: "success-metrics-list", level: 0, format: LevelFormat.BULLET, text: "•" }`
- **CRITICAL:** Use `LevelFormat.BULLET` constant, NOT string "bullet"
- Left indent: 720pt, Hanging indent: 360pt

---

## 5. Footer Metadata

The footer provides methodological transparency and next steps.

### Required Elements

Three lines of metadata:
1. **Assessment Methodology**
2. **Evidence Sources**
3. **Next Review**

### 5.1 Assessment Methodology

**Purpose:** List all frameworks and tools used in the assessment

**Format:** Assessment Methodology: [Comma-separated list of frameworks]

**Common Frameworks:**
- Vianeo 40-Question Diagnostic Framework
- Legitimacy Worksheet
- Desirability/Needs Analysis
- Acceptability/Players-Influencers Mapping
- Feasibility Assessment
- Viability/Unit Economics Model
- Persona Development
- Customer Interview Analysis

**Example:**
> **Assessment Methodology:** Vianeo 40-Question Diagnostic Framework + Legitimacy Worksheet + Desirability/Needs Analysis + Players/Influencers Mapping + Persona Development + Unit Economics Model

### 5.2 Evidence Sources

**Purpose:** List all primary source documents reviewed

**Format:** Evidence Sources: [Comma-separated list of documents]

**Common Sources:**
- Investor pitch deck
- Business plan or executive summary
- Technical documentation
- Patent applications (provisional or utility)
- Business requirements document
- Unit economics model or financial projections
- Customer interview transcripts
- Beta metrics dashboard
- Partnership agreements
- Market research reports

**Example:**
> **Evidence Sources:** Investor pitch deck, provisional patent application, business requirements document, unit economics model, customer interview transcripts (n=15), beta metrics dashboard, partnership agreements with consulting firms

### 5.3 Next Review

**Purpose:** Schedule follow-up and define trigger event

**Format:** Next Review: [Trigger event description (Target: Date/timeframe)]

**Requirements:**
- Specific trigger event (not just "in 3 months")
- Target date or timeframe
- Connected to critical path actions

**Examples:**
- "Post-revenue validation (Target: January 15, 2026, after 60-day conversion sprint)"
- "Seed round completion (Target: Q2 2026)"
- "After 40+ customer interviews complete (Target: March 2026)"
- "6-month traction review (Target: May 31, 2026)"

### Markdown Formatting

```markdown
---

**Assessment Methodology:** [List all frameworks and tools used]

**Evidence Sources:** [List all primary source documents]

**Next Review:** [Target date and trigger event]
```

**Note:** Use horizontal rule (---) before footer to visually separate

### DOCX Formatting

**Horizontal Rule:**
- Border: Top only, light gray (#CCCCCC), 1pt
- Spacing: 360pt before, 120pt after

**Metadata Lines:**
- 9pt, light gray (#757575)
- Bold label, regular content
- 120pt spacing after each line

**Example paragraph structure:**
```javascript
new Paragraph({
  style: "Metadata",
  children: [
    new TextRun({ text: "Assessment Methodology: ", bold: true }),
    new TextRun("Vianeo 40-Question Diagnostic Framework...")
  ]
})
```

---

## 6. Two-File Output System

Both markdown and DOCX files are required deliverables with **identical content**.

### 6.1 Markdown Output

**Purpose:**
- Structured, version-controllable format
- Easy to edit and track changes
- Platform-independent
- Machine-readable for automation

**File Naming:** `[ProjectName]_Vianeo_Diagnostic_Comment.md`

**Save Location:** `/mnt/user-data/outputs/`

**Formatting Requirements:**
- Follow standard markdown syntax
- Heading hierarchy: # (H1), ## (H2), ### (H3)
- Tables use pipe (|) syntax with proper alignment
- Lists: numbered (1., 2., 3.) or bulleted (-)
- Bold: **text**, Italic: *text*
- No em dashes (—) anywhere

**Quality Checks:**
- [ ] All sections present and in correct order
- [ ] Proper heading hierarchy
- [ ] Table formatted correctly
- [ ] Lists use correct syntax
- [ ] No em dashes used
- [ ] File saved with correct naming convention

### 6.2 DOCX Output

**Purpose:**
- Professional presentation format
- Design-elevated for stakeholder delivery
- Print-ready
- Consistent corporate styling

**File Naming:** `[ProjectName]_Vianeo_Diagnostic_Comment.docx`

**Save Location:** `/mnt/user-data/outputs/`

**Generation Method:** Use docx-js library (see `/mnt/skills/public/docx/docx-js.md`)

**Critical Requirements:**
- Content must be IDENTICAL to markdown version
- No content added or removed
- Only formatting differs

**Quality Checks:**
- [ ] Content identical to markdown version
- [ ] All formatting specifications applied
- [ ] Typography hierarchy correct
- [ ] Colors applied appropriately
- [ ] Tables formatted with borders and colors
- [ ] Lists use proper Word formatting
- [ ] File generates without errors

---

## 7. Typography & Styling Specifications

Professional design specifications for DOCX output.

### 7.1 Typography Scale

**Font Family:** Calibri throughout (no exceptions)

**Type Hierarchy:**
- **Title:** 24pt, bold, deep blue (#1B365D), left-aligned
- **Heading 1 (H1):** 16pt, bold, deep blue (#1B365D)
- **Heading 2 (H2):** 14pt, bold, medium gray (#4A4A4A)
- **Body Text:** 11pt, regular, body gray (#2D2D2D)
- **Metadata:** 9pt, regular, light gray (#757575)

**Rationale:**
- Clear hierarchy for scanning
- Professional and readable
- Borrowed from Apple typography principles
- Meaningful size relationships (24→16→14→11→9)

### 7.2 Color Palette

**Primary Colors:**
```
primaryBlue: "1B365D"      // Headers - authority and trust
mediumGray: "4A4A4A"       // Subheadings - professional hierarchy
bodyGray: "2D2D2D"         // Body text - reading comfort (not pure black)
lightGray: "757575"        // Metadata - secondary information
```

**Table Colors:**
```
tableBorder: "CCCCCC"      // Subtle borders
tableHeaderBg: "E8EDF2"    // Soft blue-gray for headers
```

**Semantic Colors (Score Backgrounds):**
```
greenHighlight: "D4EDDA"   // Scores ≥3.5 (Strong/Promising)
yellowHighlight: "FFF3CD"  // Scores 3.0-3.4 (Developing)
redHighlight: "F8D7DA"     // Scores <3.0 (Problematic/Non-viable)
```

**Rationale:**
- Restrained palette (professional, not flashy)
- Semantic color (green=good, yellow=caution, red=concern)
- Accessibility-friendly (sufficient contrast)
- Borrowed from Stripe data presentation principles

### 7.3 Spacing System

**Unit:** DXA (1440 DXA = 1 inch)

**Page Setup:**
- Margins: 1" all sides (1440 DXA)
- Page size: Letter (8.5" × 11")

**Paragraph Spacing:**
- **Title:** 0pt before, 240pt after
- **H1:** 360pt before, 180pt after
- **H2:** 240pt before, 120pt after
- **Body:** 240pt after, line height 360 (1.6x)
- **Metadata:** 60pt after each line

**Rationale:**
- Generous whitespace (professional appearance, easier reading)
- Consistent spacing multiples (60pt base unit)
- Breathing room between sections
- Borrowed from Swiss design principles

### 7.4 List Formatting

**Numbered Lists:**
- Format: Decimal (1., 2., 3.)
- Left indent: 720pt (0.5")
- Hanging indent: 360pt (0.25")
- **Each section needs unique reference to restart numbering**

**Bullet Lists:**
- Bullet character: "•"
- Left indent: 720pt (0.5")
- Hanging indent: 360pt (0.25")
- **Use LevelFormat.BULLET constant, NOT string "bullet"**

**CRITICAL ERRORS TO AVOID:**
- ❌ Using same numbering reference across sections (prevents restart)
- ❌ Using unicode bullets instead of proper Word lists
- ❌ Using string "bullet" instead of LevelFormat.BULLET constant

### 7.5 Table Specifications

**Column Widths (DXA):**
- Dimension: 3120 (33.3%)
- Score: 1560 (16.7%)
- Interpretation: 4680 (50%)
- **Total: 9360** (100% of content width)

**Borders:**
- All cells: Light gray (#CCCCCC), 1pt, all sides
- No thick borders or double lines

**Cell Margins:**
- Top/Bottom: 100pt
- Left/Right: 180pt
- Provides comfortable padding

**Header Row:**
- Background: Soft blue-gray (#E8EDF2)
- Text: Bold, 11pt, centered
- Column labels: "Dimension", "Score", "Interpretation"

**Data Rows:**
- Dimension: Bold, left-aligned
- Score: Bold, centered, **color-coded background**
- Interpretation: Regular, left-aligned

**Score Color Coding:**
- Score ≥3.5: Green (#D4EDDA)
- Score 3.0-3.4: Yellow (#FFF3CD)
- Score <3.0: Red (#F8D7DA)

**CRITICAL:** Set BOTH `columnWidths` array AND individual cell widths

---

## 8. Validation Checklist

Complete validation before delivery. All items must pass.

### 8.1 Content Quality (20 items)

**Executive Diagnostic:**
- [ ] Total length is 6-8 sentences across 4 paragraphs
- [ ] Strengths: 1-2 sentences with specific numbers and names
- [ ] Strengths leads with strongest validation
- [ ] Risks: 1-2 sentences with direct, quantified language
- [ ] Risks prioritized by severity (critical first)
- [ ] Near-term Actions: 2-3 sentences covering 3-4 actions
- [ ] Each action has owner in parentheses
- [ ] Each action has measurable outcome
- [ ] Evidence Gaps: 1-2 sentences with material gaps
- [ ] Evidence Gaps different from Risks section

**Dimension Summary:**
- [ ] All 5 dimensions included
- [ ] Scores match source assessment data exactly
- [ ] Status keywords match score ranges
- [ ] Interpretations specific to this venture (not generic)
- [ ] Overall status balances strengths and weaknesses

**Critical Path:**
- [ ] Immediate Priority: max 3 actions
- [ ] Short-term Priority: max 4 actions
- [ ] Medium-term Priority: max 4 actions
- [ ] Success Metrics: max 6 metrics with specific thresholds
- [ ] Actions are specific, measurable, time-bound

### 8.2 Format Quality (15 items)

**Markdown:**
- [ ] Filename: `[ProjectName]_Vianeo_Diagnostic_Comment.md`
- [ ] Saved to `/mnt/user-data/outputs/`
- [ ] Heading hierarchy correct (# for H1, ## for H2, ### for H3)
- [ ] Table formatted with proper pipe syntax
- [ ] Lists use correct syntax (numbered: `1.`, bullet: `-`)
- [ ] No em dashes anywhere
- [ ] All sections present in correct order

**DOCX:**
- [ ] Filename: `[ProjectName]_Vianeo_Diagnostic_Comment.docx`
- [ ] Saved to `/mnt/user-data/outputs/`
- [ ] Content identical to markdown version
- [ ] Typography matches specifications
- [ ] Colors applied correctly
- [ ] Table has borders and color-coded scores
- [ ] Lists use proper Word formatting (not unicode)
- [ ] File generates without errors

### 8.3 Accuracy & Evidence (10 items)

- [ ] All dimension scores match source assessments
- [ ] Numbers cited are accurate (not approximated)
- [ ] Names spelled correctly
- [ ] Dates current and accurate
- [ ] Evidence sources exist and cited correctly
- [ ] Every claim in Strengths backed by assessment data
- [ ] Every risk identified in source materials
- [ ] All actions address documented gaps or risks
- [ ] Evidence gaps verified in source assessments
- [ ] No hallucinated information or assumptions

### 8.4 Writing Quality (10 items)

- [ ] Every sentence adds unique value
- [ ] No redundancy between sections
- [ ] No unnecessary adjectives or qualifiers
- [ ] Can't remove any sentence without losing meaning
- [ ] Uses concrete examples (not abstractions)
- [ ] Includes real numbers (not "some" or "many")
- [ ] Names actual people and things
- [ ] Avoids generic business speak
- [ ] Reader knows exactly what to do next
- [ ] Could not apply to a different business

### 8.5 The Five Essential Questions

**Answer these honestly. If "no" to any, revise before delivering.**

1. **Actionable?** Can someone read this and know exactly what to do?
2. **Specific?** Is this clearly about THIS business, not any business?
3. **Balanced?** Does it acknowledge both strengths AND real problems?
4. **Evidence-based?** Is every claim supported by assessment data?
5. **Concise?** Could any sentence be cut without losing meaning?

---

## 9. Common Mistakes

Avoid these frequent errors.

### 9.1 Content Mistakes (10 items)

1. **Generic praise** - "Team seems capable", "promising opportunity", "strong potential"
   - ✗ BAD: "The team has good experience"
   - ✓ GOOD: "Founder brings 10+ years domain expertise validated through prior clients"

2. **Hedging language** - "may", "might", "possibly", "could", "seems", "appears"
   - ✗ BAD: "Revenue model may need validation"
   - ✓ GOOD: "Revenue model entirely unvalidated with zero paying customers"

3. **Actions without owners** - "The team should...", "Consider...", "It would be good to..."
   - ✗ BAD: "The team should talk to more customers"
   - ✓ GOOD: "Shawna should conduct 40-60 structured customer interviews"

4. **Vague risks** - "Some concerns", "needs improvement", "could be better"
   - ✗ BAD: "Team structure could benefit from additional expertise"
   - ✓ GOOD: "CTO lacks distinctive AI/ML credentials, development outsourced to contractors"

5. **Mixing risks and gaps** - Evidence gaps in Risks section, or vice versa
   - ✗ BAD: In Risks: "Customer interview data is incomplete"
   - ✓ GOOD: That belongs in Evidence Gaps section

6. **Too long** - Executive Diagnostic exceeds 8 sentences
   - ✗ BAD: 12 sentences across 4 paragraphs
   - ✓ GOOD: 6-8 sentences total

7. **Missing numbers** - No quantification in Strengths or Risks
   - ✗ BAD: "Several beta users showing good engagement"
   - ✓ GOOD: "50+ beta users show 60% time reduction and 30% quality improvement"

8. **Non-measurable actions** - "Improve customer understanding", "Optimize pricing"
   - ✗ BAD: "Improve conversion rates"
   - ✓ GOOD: "Target 40% beta-to-paid conversion rate"

9. **Missing timeframes** - Actions without time bounds
   - ✗ BAD: "Eventually hire a CTO"
   - ✓ GOOD: "Internalize development or hire VP Engineering within 90 days"

10. **Generic interpretations** - Dimension interpretations could apply to any business
    - ✗ BAD: "Viability: 2.5/5 | Needs work"
    - ✓ GOOD: "Viability: 2.5/5 | Problematic - Pre-revenue, unvalidated economics"

### 9.2 Format Mistakes (10 items)

11. **Em dashes** - Using — character anywhere
    - ✗ BAD: "The team — despite limited resources — shows promise"
    - ✓ GOOD: "The team, despite limited resources, shows promise"

12. **Inconsistent content** - Markdown and DOCX differ
    - ✗ BAD: Additional content in DOCX not in markdown
    - ✓ GOOD: Identical content in both files

13. **Wrong file naming** - Incorrect naming convention
    - ✗ BAD: `diagnostic.md` or `Rayla-AI-Diagnostic.md`
    - ✓ GOOD: `Rayla_AI_Vianeo_Diagnostic_Comment.md`

14. **Missing table borders** - DOCX table without borders
    - ✗ BAD: No visible cell borders
    - ✓ GOOD: All cells have light gray borders

15. **Unicode bullets** - Using • character instead of proper Word lists
    - ✗ BAD: Paragraph with "• " prefix
    - ✓ GOOD: Proper numbered/bulleted list with LevelFormat

16. **String "bullet"** - Using string instead of constant
    - ✗ BAD: `format: "bullet"`
    - ✓ GOOD: `format: LevelFormat.BULLET`

17. **Same numbering reference** - Not restarting numbering in each section
    - ✗ BAD: All numbered lists use "default-list" reference
    - ✓ GOOD: Each section has unique reference

18. **Missing column widths** - Only setting columnWidths array OR individual cells
    - ✗ BAD: Set columnWidths array but not individual cell widths
    - ✓ GOOD: Set BOTH columnWidths array AND individual cell widths

19. **Wrong color codes** - Typos in hex values
    - ✗ BAD: `#1B365D` typed as `#1B356D`
    - ✓ GOOD: Copy exact hex codes from specification

20. **Incorrect spacing** - DXA values wrong or inconsistent
    - ✗ BAD: Random spacing values
    - ✓ GOOD: Follow exact spacing specification (multiples of 60pt)

### 9.3 Quality Mistakes (5 items)

21. **Not specific to this venture** - Could swap in any business name
    - ✗ BAD: Generic observations that apply broadly
    - ✓ GOOD: Specific details unique to this venture

22. **Unverified claims** - Making statements without assessment backing
    - ✗ BAD: "The market is growing rapidly"
    - ✓ GOOD: "TAM of $2.1B validated by 3 independent market reports"

23. **Aspirational strengths** - Listing hopes as validated facts
    - ✗ BAD: "Plans to partner with major consultancies"
    - ✓ GOOD: "2 consulting partnerships provide channel validation"

24. **Downplayed risks** - Making serious problems sound minor
    - ✗ BAD: "Revenue generation could benefit from additional focus"
    - ✓ GOOD: "Zero paying customers despite operational beta"

25. **Mismatched scores** - Status keywords don't match score ranges
    - ✗ BAD: Score 3.8/5 labeled "Developing" (should be "Promising")
    - ✓ GOOD: Score 3.8/5 labeled "Promising"

---

## 10. File Naming Convention

Consistent, descriptive file naming for both outputs.

### Format

**Markdown:**
```
[ProjectName]_Vianeo_Diagnostic_Comment.md
```

**DOCX:**
```
[ProjectName]_Vianeo_Diagnostic_Comment.docx
```

### Rules

1. **Project Name:**
   - Use official business/project name
   - Replace spaces with underscores
   - Maintain capitalization (e.g., "Rayla_AI" not "rayla_ai")
   - Remove special characters except underscores

2. **Separator:**
   - Use underscores (_) not hyphens or spaces

3. **Constant Suffix:**
   - Always: "_Vianeo_Diagnostic_Comment"
   - Exactly as shown (capitalization matters)

4. **Extension:**
   - `.md` for markdown
   - `.docx` for Word document

### Examples

**Good:**
- `Rayla_AI_Vianeo_Diagnostic_Comment.md`
- `TechVenture_Solutions_Vianeo_Diagnostic_Comment.md`
- `GreenPath_Energy_Vianeo_Diagnostic_Comment.docx`

**Bad:**
- `diagnostic.md` (too generic)
- `Rayla-AI-Diagnostic.md` (wrong separators, missing framework name)
- `rayla_ai_vianeo_diagnostic_comment.md` (wrong capitalization)
- `Rayla AI Vianeo Diagnostic Comment.md` (spaces not allowed)

### Save Location

**Both files must be saved to:**
```
/mnt/user-data/outputs/
```

**Never save to:**
- Current working directory
- Templates folder
- Docs folder
- Any other location

---

## 11. Quality Standards & Time Budget

### Quality Hierarchy

**Non-negotiable (Must Have):**
1. Accurate scores from source data
2. 6-8 sentences in Executive Diagnostic
3. Specific numbers and names (no generic language)
4. Owners assigned to all actions
5. No em dashes
6. Identical content in markdown and DOCX

**High Priority (Should Have):**
7. Evidence-backed claims throughout
8. Direct language without hedging
9. Material evidence gaps (not minor issues)
10. Proper status keywords by score range
11. Color-coded table scores in DOCX
12. Professional typography and spacing

**Nice to Have (Could Have):**
13. Particularly elegant phrasing
14. Additional formatting polish
15. Extra validation checks

**If time-constrained, prioritize Non-negotiable items first.**

### Time Budget Allocation

**Total: 25-35 minutes**

**Content Creation (10-15 minutes):**
- Review source assessments: 3-5 min
- Draft Executive Diagnostic: 4-6 min
- Create Dimension Summary: 2-3 min
- Build Critical Path: 3-5 min
- Write footer metadata: 1-2 min

**Markdown Output (3-5 minutes):**
- Format in markdown syntax: 2-3 min
- Quality check: 1-2 min

**DOCX Generation (5-10 minutes):**
- Set up document structure: 2-3 min
- Apply typography and colors: 2-3 min
- Create table with formatting: 2-3 min
- Generate and verify: 1-2 min

**Final Validation (5-8 minutes):**
- Content quality check: 2-3 min
- Format verification: 1-2 min
- Accuracy validation: 1-2 min
- Five essential questions: 1 min

**If over time budget:**
- Cut polish, not substance
- Reduce validation iterations
- Simplify DOCX formatting (but maintain specs)
- Do NOT cut content quality or accuracy

### Efficiency Tips

1. **Prepare templates in advance** - Have markdown structure ready
2. **Extract data first** - Pull all numbers/names before writing
3. **Write Executive Diagnostic first** - Hardest section when mind is fresh
4. **Reuse DOCX code** - Have base formatting code ready
5. **Validate as you go** - Don't wait until end
6. **Use checklist systematically** - Check off items in real-time

---

## 12. Design Principles

Professional design elevation for DOCX output.

### Core Principles

1. **Typography Scale** - Clear hierarchy through meaningful size relationships
2. **Strategic Color** - Restrained palette with semantic meaning
3. **Generous White Space** - Professional margins and breathing room
4. **Systematic Approach** - Consistent application across document
5. **Borrowed Excellence** - Learning from Apple, Swiss design, Stripe

### Inspiration Sources

**Apple Typography:**
- Clear hierarchy (24→16→14→11→9)
- Generous line height (1.6x)
- Restrained but purposeful

**Swiss Design:**
- Grid-based layout
- White space as design element
- Functional elegance

**Stripe Data Presentation:**
- Semantic color (green/yellow/red for data)
- Clean tables with subtle borders
- Professional without being corporate

### Why Professional Design Matters

**Credibility:**
- First impression on investors/stakeholders
- Signals attention to detail
- Communicates professionalism

**Readability:**
- Easier to scan and digest
- Clear hierarchy guides reader
- Comfortable reading experience

**Impact:**
- Key findings stand out
- Color coding aids quick understanding
- Professional package increases perceived value

### Design Don'ts

- ❌ No gradients or shadows
- ❌ No multiple font families
- ❌ No pure black (#000000) for text
- ❌ No rainbow colors or excessive palette
- ❌ No tight spacing or cramped layouts
- ❌ No inconsistent application

---

## 13. Reference Materials

### Core Documents

**Templates:**
- `/home/user/master-vianeo-repository/templates/Step10_Diagnostic_Markdown_Template.md`
- `/home/user/master-vianeo-repository/templates/Step10_Diagnostic_DOCX_Template.md`

**Documentation:**
- `/home/user/master-vianeo-repository/docs/VIANEO_Diagnostic_Template.md`
- `/home/user/master-vianeo-repository/docs/VIANEO_Diagnostic_Examples.md`
- `/home/user/master-vianeo-repository/docs/VIANEO_Diagnostic_Quality_Checklist.md`
- `/home/user/master-vianeo-repository/docs/VIANEO_Diagnostic_DOCX_Formatting.md`

**Technical References:**
- `/mnt/skills/public/docx/docx-js.md` (DOCX generation library documentation)

### Workflow Integration

**Prerequisites (Steps 1-9):**
1. Legitimacy Assessment
2. Desirability Assessment
3. Acceptability Assessment
4. Feasibility Assessment
5. Viability Assessment
6. Persona Development
7. Players/Influencers Mapping
8. Customer Interview Analysis
9. Competitive Analysis

**Step 10 synthesizes all prior work into executive summary.**

### Support Resources

**Examples:**
- See VIANEO_Diagnostic_Examples.md for good/bad examples
- Rayla AI diagnostic used as reference throughout

**Checklists:**
- VIANEO_Diagnostic_Quality_Checklist.md for complete validation
- Use systematically before delivery

**Formatting:**
- VIANEO_Diagnostic_DOCX_Formatting.md for complete technical specs
- Reference for all DXA measurements and color codes

---

## 14. Summary

### Key Takeaways

**Content Philosophy:**
- Conciseness over comprehensiveness (6-8 sentences total)
- Specificity over abstraction (numbers, names, examples)
- Actionability over analysis (owners, deadlines, outcomes)
- Evidence-based over aspirational (validated facts only)

**Format Requirements:**
- Two files: markdown + DOCX
- Identical content in both
- Professional design elevation in DOCX
- No em dashes anywhere

**Quality Standards:**
- Answer "yes" to all five essential questions
- Pass complete validation checklist
- Specific to this venture (not generic)
- Evidence-backed claims throughout

**Time Investment:**
- 25-35 minutes total
- Quality over speed, but don't over-polish
- Use templates and checklists for efficiency

### Success Criteria

**A successful Step 10 Diagnostic:**
1. Provides clear, actionable direction
2. Balances strengths and weaknesses honestly
3. Uses specific evidence and quantification
4. Assigns ownership and accountability
5. Looks professional and credible
6. Takes 25-35 minutes to create
7. Passes all validation checks
8. Could be handed directly to stakeholders

### Final Reminders

- **This document makes first impressions** - Quality matters
- **Evidence-based claims only** - No speculation or assumption
- **Specific, not generic** - Should only fit THIS business
- **Actionable, not passive** - Reader knows what to do next
- **Validate before delivery** - Use checklist systematically

---

**Version History:**
- v1.0 (2025-11-21): Initial comprehensive format specification

**Maintained by:** VIANEO Framework Development Team

**For questions or updates:** Refer to repository documentation or raise issue
