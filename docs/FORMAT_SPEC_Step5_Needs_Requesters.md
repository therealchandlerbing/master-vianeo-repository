# FORMAT SPECIFICATION: Step 5 - Needs/Requesters Analysis
## VIANEO Business Model Evaluation Playbook - Desirability Assessment

**Framework Weight:** 25% of overall VIANEO score (HIGHEST WEIGHT)
**Version:** 1.0
**Last Updated:** 2025-01-15
**Document Status:** Official Format Specification

---

## TABLE OF CONTENTS

1. [Overview & Strategic Importance](#overview)
2. [Document Header Requirements](#document-header)
3. [Requesters Table Specification](#requesters-table)
4. [Needs Analysis Specification](#needs-analysis)
5. [Existing Solutions Specification](#existing-solutions)
6. [Four-File Output Package](#output-package)
7. [Validation Priority System](#validation-priority)
8. [Validation Checklist (40+ Items)](#validation-checklist)
9. [Common Mistakes to Avoid (10+)](#common-mistakes)
10. [File Naming Conventions](#file-naming)
11. [Quality Gates & Acceptance Criteria](#quality-gates)

---

## OVERVIEW & STRATEGIC IMPORTANCE {#overview}

### What Step 5 Assesses

**Core Question:** Do specific people need your specific solution?

**Framework:** WHO/WHAT/WHY/HOW
- **WHO** needs it? (Requesters/customers with validated needs)
- **WHAT** do they need? (Tasks, pains, expectations)
- **WHY** insufficient now? (Gaps in existing solutions)
- **HOW** validated? (Evidence quality and reliability)

### Why Step 5 Carries Highest Weight (25%)

**Legitimacy** (Step 4) validates a real problem exists.
**Desirability** (Step 5) validates specific segments need your specific approach.

**Common failure pattern:** Brilliant technology seeking market vs. market-driven innovation solving validated customer pain.

**This step prevents that** by forcing brutal honesty about validation status before significant investment.

### Critical Success Factor: Brutal Honesty

**LOW validation scores are VALUABLE signals.**

It's better to know you have weak validation NOW (when fixes cost $10K) than LATER (when fixes cost $10M).

**Rule:** Don't fabricate validation. "Not yet interviewed" is acceptable. Fake interviews are not.

---

## DOCUMENT HEADER REQUIREMENTS {#document-header}

### Mandatory Header Block

All Step 5 documents must begin with this metadata block:

```markdown
# Vianeo Desirability: Needs/Requesters Analysis
## [Project Title]

**Project:** [Full project name]
**Analysis Date:** [YYYY-MM-DD]
**Project Lead:** [Name, Organization]
**Maturity Stage:** [Idea / Prototype / Pilot / Early Commercialization / Growth]
```

### Header Field Specifications

**Project Title:**
- Maximum 80 characters
- Descriptive and specific
- Example: "Spherical NdFeB Powders for Brazilian Manufacturing"

**Analysis Date:**
- Format: YYYY-MM-DD (ISO 8601)
- Date analysis was completed
- Update when substantially revised

**Project Lead:**
- Name and organization
- Primary contact for questions
- Example: "Dr. Maria Silva, CDTN/CNEN"

**Maturity Stage:**
- Use EXACTLY one of these five stages:
  - **Idea** - Concept only, no prototype
  - **Prototype** - Working model/proof-of-concept
  - **Pilot** - Testing with real users
  - **Early Commercialization** - First customers, revenue
  - **Growth** - Scaling operations

### Section 1: INPUTS USED (Required Metadata)

**Four mandatory subsections:**

1. **Problem Statement (from Legitimacy)**
   - Copy from Step 4 Legitimacy Assessment
   - Must be solution-neutral
   - 250 characters maximum
   - If Step 4 not completed, note: "[To be completed in Step 4]"

2. **Field of Application**
   - Copy from Step 4
   - 60 characters maximum
   - If Step 4 not completed, create concise description

3. **Business Model Canvas Status**
   - Options: Complete / Draft / Not Yet Created
   - If available, note which sections are complete
   - Example: "Draft - Customer segments and value propositions complete"

4. **Interview/Research Data Status** ⚠️ CRITICAL
   - **BE BRUTALLY HONEST**
   - Specify: number of interviews, segments, average length, dates
   - Cite secondary research sources with dates
   - If zero interviews, state explicitly:
     > "No direct customer interviews conducted. Analysis based on secondary research, market analysis, and team's institutional knowledge. All requesters require validation through primary research."

**Quality Standard:**
- ✓ Specific numbers (not "some" or "several")
- ✓ Honest about gaps (weak validation is valuable data)
- ✓ Cites sources for all evidence
- ✗ Vague language ("research was conducted")
- ✗ Exaggeration (2 chats ≠ "extensive validation")

---

## REQUESTERS TABLE SPECIFICATION {#requesters-table}

### Structure & Requirements

**Format:** 3-column table

| Requester Role | Description | Reliability |
|---------------|-------------|-------------|

**Quantity:** 6-10 distinct requester types (no fewer than 6, no more than 10)

**Quality Standard:** Each requester must be DISTINCT with different needs or context

### Column 1: Requester Role

**Requirements:**
- 3-6 words maximum
- Professional title or role designation
- Specific, not generic
- Distinguish users from buyers when different (B2B contexts)

**Examples:**
- ✓ "Permanent Magnet Manufacturers"
- ✓ "Wind Turbine Component Suppliers"
- ✓ "University Research Laboratories"
- ✓ "Hospital Facilities Administrators"
- ✓ "Adult Children Managing Early Dementia"
- ✗ "Customers" (too generic)
- ✗ "People who need magnets" (too vague)
- ✗ "Various businesses" (not specific)

**B2B Contexts - Critical Distinction:**

When users ≠ buyers, create SEPARATE requester entries:

Example:
- "Hospital Facilities Administrators" (buyers, decision-makers, budget authority)
- "Clinical Staff / Nurses" (users, daily interaction, workflow impact)

**Why this matters:** Users care about usability; buyers care about ROI. Different needs require different value propositions.

### Column 2: Description

**Length:** 2-4 sentences (approximately 60-120 words)

**Required Elements:**
1. **Who they are** - Role, context, scale
2. **Why they matter** - Relationship to your solution
3. **Current situation** - What they do now, constraints
4. **Specifics** - Company size, sector, geography if relevant

**Strong Example:**
> "Companies producing finished NdFeB magnets for industrial applications. Currently import raw powders from China/Japan. Serve as critical intermediary between raw materials and end-use sectors. Scale: small to medium Brazilian manufacturers facing supply chain vulnerability due to geopolitical tensions and trade barriers."

**What makes it strong:**
- Specific role and industry context
- Current behavior documented
- Scale and geography specified
- Pain point mentioned (supply chain vulnerability)

**Poor Example:**
> "People who need magnets for various industrial uses in different sectors."

**What makes it poor:**
- Generic and vague
- No context or scale
- No current behavior
- No pain points

### Column 3: Reliability Rating

**Four-Tier System (use EXACTLY these phrases):**

| Rating | Exact Phrase | When to Use |
|--------|-------------|-------------|
| **Tier 1** | "More than 5 interviewed" | 6+ customer interviews with this requester profile |
| **Tier 2** | "Less than 5 interviewed [validate with interviews]" | 1-5 interviews completed, need more for statistical significance |
| **Tier 3** | "Not yet interviewed [validate with interviews]" | Logic/secondary research but zero direct customer contact |
| **Tier 4** | "Unspecified [validate with interviews]" | Unknown validation status or mixed evidence |

**Critical Rules:**

1. **Be ruthlessly honest** - Fabricating validation creates false confidence
2. **Zero interviews = Tier 3** - Not Tier 2
3. **Informal chats ≠ interviews** - Must be structured discovery conversations
4. **Industry contacts ≠ customer interviews** - Unless they fit requester profile
5. **5+ is the threshold** - Pattern identification requires statistical significance

**Why 5+ matters:**
- 1-2 interviews = anecdotes
- 3-4 interviews = preliminary patterns
- 5+ interviews = patterns become reliable
- 10+ interviews per segment = strong validation

### Requesters Table Quality Checks

Before finalizing, verify:

- [ ] Each requester is distinct with different needs or context (no overlaps)
- [ ] Users vs. buyers distinction clear where applicable (B2B contexts)
- [ ] Descriptions are specific, not generic (names, numbers, geography)
- [ ] Reliability ratings are honest and evidence-based (don't fabricate)
- [ ] Total count: 6-10 requesters (no more, no less)
- [ ] At least 3 requesters have descriptions >50 words (substance)
- [ ] Scale/scope specified for each requester (company size, market size, geography)

### Common Requesters Table Mistakes

**Mistake 1: Generic or Overlapping Requesters**

❌ Poor segmentation by size alone:
- "Small businesses"
- "Medium businesses"
- "Large businesses"

✓ Better segmentation by need difference:
- "R&D labs needing customized specifications"
- "Manufacturers needing consistent volume supply"
- "Strategic sectors needing domestic sourcing"

**Mistake 2: Confusing Users with Buyers**

❌ Single requester: "Hospital staff"

✓ Two distinct requesters:
- "Hospital administrators" (buyers, budget authority, ROI focus)
- "Clinical staff" (users, workflow integration, usability focus)

**Mistake 3: Treating Hypothesis as Validated**

❌ "Less than 5 interviewed" when actually zero interviews

✓ "Not yet interviewed [validate with interviews]"

---

## NEEDS ANALYSIS SPECIFICATION {#needs-analysis}

### Structure & Framework

**Total:** 10 needs (minimum 10, up to 12 acceptable)

**Distribution:** Across three categories

- **Tasks** (What They Need to Accomplish): 3-4 needs
- **Pains** (Problems to Eliminate): 3-4 needs
- **Expectations** (Desired Outcomes): 3-4 needs

**Format:** Bulleted lists under category headers

### The 60-Character Rule ⚠️ NON-NEGOTIABLE

**Every need statement MUST be 60 characters or less. No exceptions.**

**Why this constraint matters:**
- Forces clarity and precision
- Ensures needs are scannable
- Prevents embedded solutions
- Compatible with visualization tools (Step 6)

**Character counting:**
- Include spaces
- Include punctuation
- Exclude bullet points
- Exclude formatting symbols

**Validation:** Use character counter before finalizing

### Category 1: TASKS (What They Need to Accomplish)

**Definition:** Jobs to be done, activities they're trying to complete, goals they're working toward

**Structure:**
- Infinitive verb structure (action-oriented)
- Start with strong action verb
- Focus on outcome, not method
- Solution-neutral

**Examples:**
```
✓ 57 chars: "Access cost-competitive domestic raw materials"
✓ 60 chars: "Enable 3D printing applications with spherical powders"
✓ 58 chars: "Validate magnetic properties for specific applications"
✓ 53 chars: "Scale production with consistent quality standards"
```

**Anti-Patterns:**
```
❌ 72 chars: "Access affordable cost-competitive domestic raw materials supply"
❌ Embedded solution: "Need mobile app to track brain health"
❌ Too vague: "Do their job better"
❌ Not action: "Better performance"
```

### Category 2: PAINS (Problems to Eliminate)

**Definition:** Frustrations, obstacles, risks, barriers blocking progress, what keeps them up at night

**Structure:**
- Describe friction points
- Quantifiable when possible
- Focus on impact, not symptoms
- Evidence-based or explicitly hypothesized

**Examples:**
```
✓ 59 chars: "Eliminate dependency on Chinese/Japanese imports"
✓ 58 chars: "Reduce vulnerability to geopolitical trade disruptions"
✓ 56 chars: "Avoid long lead times from international suppliers"
✓ 58 chars: "Minimize exposure to volatile international pricing"
```

**Anti-Patterns:**
```
❌ Too long: "Eliminate complete dependency on foreign Chinese suppliers"
❌ Too vague: "Things don't work well"
❌ Not painful: "Interface could be prettier"
❌ Embedded solution: "Lack of mobile access to data"
```

### Category 3: EXPECTATIONS (Desired Outcomes)

**Definition:** Success criteria, desired state they want to reach, what gives confidence/satisfaction

**Structure:**
- Describe end state, not process
- Focus on outcomes and results
- Aspirational but realistic
- Connected to business impact

**Examples:**
```
✓ 59 chars: "Achieve strategic sovereignty in critical materials"
✓ 60 chars: "Support domestic manufacturing ecosystem development"
✓ 58 chars: "Enable circular economy through recycling integration"
✓ 52 chars: "Establish reliable domestic supply chain network"
```

**Anti-Patterns:**
```
❌ Process-focused: "Use a better system"
❌ Embedded solution: "Have cloud-based platform"
❌ Too vague: "Be successful"
❌ Unrealistic: "Dominate global market immediately"
```

### Needs Analysis Quality Standards

**Standard 1: Character Limit (60 chars max) - CRITICAL**

Techniques for staying under 60 characters:
- Start with strong verb: "Track performance" not "Need to track performance"
- Cut adjectives: "Access tools" not "Access affordable clinical-grade tools"
- Remove filler: "Reduce costs" not "Significantly reduce operational costs"
- Use abbreviations if universal: "NdFeB" not "Neodymium-Iron-Boron"

**Standard 2: Each Need Must Be DISTINCT**

**Test:** "Could I satisfy Need A without satisfying Need B?"

If the answer is NO, they're the same need worded differently.

❌ **Overlapping needs (all the same):**
- "Maintain cognitive health"
- "Keep brain sharp"
- "Prevent mental decline"

✓ **Distinct needs (different solutions required):**
- "Track cognitive performance objectively" (measurement need)
- "Practice evidence-based brain training" (intervention need)
- "Identify early decline signs" (detection need)

**Standard 3: No Embedded Solutions**

❌ "Need mobile app to track brain health" (embeds solution = mobile app)

✓ "Track cognitive performance objectively" (actual need)

The actual need is measurement. Mobile app is ONE possible solution among many (wearables, web platform, clinical visits, paper journals, etc.).

**Standard 4: Evidence-Based or Explicitly Hypothesized**

Mark validation status:

**If validated through customer interviews:**
```
• Eliminate dependency on Chinese/Japanese imports
  (Cited by 12/15 magnet manufacturers as primary concern)
```

**If hypothesis requiring validation:**
```
• Enable 3D printing applications with spherical powders
  [REQUIRES VALIDATION: Only 2/15 manufacturers mentioned 3D printing interest]
```

**Standard 5: Organized Correctly Across Categories**

Verify each need is in the correct category:

**Test Questions:**
- **Tasks:** "Is this something they actively need to accomplish?"
- **Pains:** "Is this a problem they want eliminated?"
- **Expectations:** "Is this a desired outcome or end state?"

### Needs Analysis Quality Checks

Before finalizing, verify:

- [ ] All 10 needs under 60 characters (use character counter)
- [ ] Each need is distinct - test: "Could I satisfy one without the other?"
- [ ] Organized correctly (Tasks/Pains/Expectations make logical sense)
- [ ] Based on evidence or clearly marked as hypothesis
- [ ] No embedded solutions (NOT "Need mobile app to...")
- [ ] Action-oriented verb structure for Tasks
- [ ] Problem-focused language for Pains
- [ ] Outcome-focused language for Expectations
- [ ] Distribution roughly balanced (3-4 per category)
- [ ] No duplicates across categories (same need worded differently)
- [ ] Connected to requester profiles (can map needs to requesters)

### Common Needs Analysis Mistakes

**Mistake 1: Embedded Solutions**

❌ "Need mobile app to track brain health"
❌ "Require cloud-based platform for data"
❌ "Use AI to predict outcomes"

These embed the HOW (solution) into the WHAT (need).

✓ "Track cognitive performance objectively"
✓ "Access data from multiple locations"
✓ "Predict likely outcomes with confidence"

**Mistake 2: Overlapping Needs**

❌ All the same need:
- "Reduce costs"
- "Lower expenses"
- "Save money"

✓ Distinct financial needs:
- "Reduce raw material procurement costs" (supply chain)
- "Lower production waste and defects" (operations)
- "Minimize inventory carrying costs" (logistics)

**Mistake 3: Exceeding Character Limit**

❌ 73 chars: "Access affordable cost-competitive domestic raw materials supply sources"

✓ 57 chars: "Access cost-competitive domestic raw materials"

Removed: "affordable" (redundant with cost-competitive), "supply sources" (implied)

**Mistake 4: Vague or Generic Needs**

❌ "Improve efficiency"
❌ "Increase performance"
❌ "Better outcomes"

✓ "Reduce production cycle time from 6 weeks to 2 weeks"
✓ "Achieve 99.5%+ purity in final product"
✓ "Maintain consistent spherical morphology"

**Mistake 5: Process vs. Outcome Confusion**

❌ "Use better tools" (process)
✓ "Complete analysis in <1 hour" (outcome)

❌ "Implement new system" (process)
✓ "Reduce data entry errors to <1%" (outcome)

---

## EXISTING SOLUTIONS SPECIFICATION {#existing-solutions}

### Structure & Requirements

**Format:** 3-column table

| Solution | Description | Limitations Identified |
|----------|-------------|----------------------|

**Quantity:** 5-6 solutions (minimum 5, maximum 6)

**Mandatory:** Always include "Doing Nothing" or "Status Quo" as final row

### Column 1: Solution Name/Type

**Requirements:**
- Specific names when possible
- Generic categories when needed
- 2-8 words maximum
- Last row MUST be "Doing Nothing (Status Quo)"

**Examples:**
- ✓ "Chinese/Japanese Suppliers (Dominant Players)"
- ✓ "Lumosity and Peak Brain Training Apps"
- ✓ "Conventional High-Temperature Production"
- ✓ "Manual Spreadsheet-Based Tracking"
- ✓ "Doing Nothing (Status Quo)" ← MANDATORY

**Solution Categories to Consider:**

1. **Direct Competitors** - Same approach, different vendor
2. **Indirect Competitors** - Different approach, same outcome
3. **Substitutes** - Non-obvious alternatives achieving similar results
4. **Manual/Legacy Methods** - What they did before any solution
5. **Doing Nothing** - Status quo, inaction (ALWAYS include this)

### Column 2: Description (2-3 sentences)

**Required Elements:**
1. **What it is** - Product, service, process, or approach
2. **Who uses it** - Market share, user base, geography
3. **How it works** - Key features, mechanism, or process

**Length:** 40-80 words

**Strong Example:**
> "Established global suppliers (primarily China) providing dense NdFeB alloy powders to Brazilian manufacturers. Dominant market solution with mature supply chains and competitive pricing due to economies of scale. Serve 80%+ of Brazilian magnet production with reliable delivery but limited customization."

**What makes it strong:**
- Specific geography (China, Brazil)
- Market position quantified (80%+)
- Key advantages named (mature supply chains, economies of scale)
- Limitations foreshadowed (limited customization)

**Poor Example:**
> "Some companies make similar products."

### Column 3: Limitations Identified (2-4 sentences)

⚠️ **THIS IS THE MOST CRITICAL COLUMN** ⚠️

This column explains WHY your opportunity exists. Without meaningful limitations, existing solutions are adequate.

**Required Elements:**
1. **Specific limitations** - Not vague complaints
2. **Evidence-based** - From user research, testing, or documented issues
3. **Meaningful gaps** - Not trivial issues
4. **Connected to unmet needs** - Link to needs from Section 3

**Length:** 40-100 words

**Strong Example:**
> "Trade barriers intensifying due to geopolitical tensions (23% tariff increase 2023-2024). No customization for Brazilian specifications - standardized products only. Supply chain vulnerable to export controls (China rare earth export restrictions). Prices subject to international market volatility (±40% fluctuations 2022-2024). No circular economy or recycling integration possible with import model."

**What makes it strong:**
- Multiple specific limitations (5 distinct gaps)
- Quantified when possible (23% tariff, ±40% fluctuations)
- Evidence of trends (export restrictions, geopolitical tensions)
- Connected to needs (customization, sovereignty, pricing stability)

**Poor Example:**
> "Not very good. Users seem unhappy. Could be better."

**What makes it poor:**
- Vague ("not very good")
- No evidence ("seem")
- No specifics (which users? unhappy about what?)

### The "Doing Nothing" Row - MANDATORY

**Always include this row.** Status quo is a REAL competitor.

Many customers choose inaction when:
- Switching costs > perceived benefit
- Current pain tolerable
- Risk of change > risk of staying
- No budget allocated

**Example:**

| Solution | Description | Limitations Identified |
|----------|-------------|----------------------|
| **Doing Nothing (Import Dependency Status Quo)** | Organizations continue relying entirely on imported NdFeB powders and finished magnets. Current state for majority of Brazilian manufacturers and institutions. Inaction remains a viable choice. | Strategic vulnerability to trade disruptions. No control over specifications or pricing. Technology dependence on foreign suppliers. Incompatible with Brazil's strategic sovereignty goals for defense and wind sectors. Limits domestic innovation in emerging magnet applications. Five-year trend shows increasing risk (export controls, tariffs, supply disruptions). |

**Critical Rule:** If you cannot articulate strong limitations for "Doing Nothing," you don't have a compelling value proposition.

If status quo is adequate, incremental improvements won't overcome switching costs. You need 10x improvement, not 10%.

### Existing Solutions Quality Standards

**Standard 1: Comprehensive Competitive Landscape**

Map all alternatives, not just obvious competitors:

**Example - Cognitive Health:**
- **Direct:** Brain training apps (Lumosity, Peak, Elevate)
- **Indirect:** Meditation apps (Headspace, Calm)
- **Substitutes:** Memory supplements, physical exercise programs
- **Legacy:** Pen-and-paper memory tests, clinical assessments
- **Status Quo:** Do nothing, accept natural decline

**Standard 2: Evidence-Based Limitations**

Source limitations from:
- ✓ Customer interviews ("8/15 users cited X as frustration")
- ✓ User testing (documented failures or gaps)
- ✓ Published reviews and complaints
- ✓ Competitive analysis with data
- ✗ Assumptions ("They probably don't like...")
- ✗ Marketing fluff ("We're better because...")

**Standard 3: Validated Customer Dissatisfaction**

Don't assume users hate existing solutions.

❌ Assumption: "Users must hate relying on imports"

✓ Validated finding:
> "8/15 manufacturers said import dependency is concerning, but current pricing and reliability make switching risky without proven domestic alternative. Price premium tolerance: <15%. Switching requires 6-12 month validation period due to quality assurance requirements."

This reveals:
- The pain exists (import dependency concern)
- Barriers to switching (risk, validation time)
- Constraints (price premium <15%)

**Standard 4: Non-Obvious Substitutes Included**

Look beyond direct competitors.

**Example - Project Management:**
- Direct: Asana, Monday.com, Jira
- Indirect: Spreadsheets, Notion, Airtable
- Substitutes: Email threads, paper notebooks, whiteboards
- Status Quo: Informal coordination, no formal PM

### Existing Solutions Quality Checks

Before finalizing, verify:

- [ ] 5-6 solutions total (not fewer, not more)
- [ ] "Doing Nothing" included as final row with honest assessment
- [ ] All major competitors included (direct and indirect)
- [ ] Non-obvious substitutes identified
- [ ] Limitations are specific and evidence-based (not "not very good")
- [ ] Each solution description includes market position or user base
- [ ] Limitations connect to unmet needs from Section 3
- [ ] Customer satisfaction assessed (not assumed)
- [ ] Switching costs acknowledged (financial, operational, psychological)
- [ ] Competitive advantages are honest, not exaggerated

### Common Existing Solutions Mistakes

**Mistake 1: Superficial Competitive Research**

❌ "We looked at their website and it seems outdated."

✓ "Tested Competitor X for 2 weeks. Interviewed 8 current users. 6/8 cited limited customization as reason for supplementing with alternative solutions. Documented 12 specific instances where customization requests were declined or required 6+ month development."

**Mistake 2: Missing Non-Obvious Competitors**

❌ Only listing direct brain training apps

✓ Including:
- Direct: Brain training apps
- Indirect: Meditation, memory supplements
- Substitutes: Physical exercise, social engagement
- Status quo: Do nothing

**Mistake 3: Assuming Dissatisfaction**

❌ "Their current solution is terrible so they'll definitely switch."

✓ "Current solution satisfaction: 6.2/10 (survey of 23 users). Key limitations cited: X, Y, Z. However, 18/23 said switching requires proven reliability over 6+ month period and <20% price increase. Inertia is strong."

**Mistake 4: Ignoring Status Quo**

❌ Omitting "Doing Nothing" row

✓ Including honest assessment:
> "Status quo remains attractive for 60% of potential customers due to: (1) acceptable current pain level, (2) no budget allocated for new solution, (3) change management burden, (4) uncertainty about new solution reliability."

**Mistake 5: Weak Limitations**

❌ "Some users don't like it very much."

✓ "32% of surveyed users (N=50) rated satisfaction ≤5/10. Top complaints: (1) slow performance on datasets >10K rows (cited by 89%), (2) limited API integrations (73%), (3) steep learning curve for non-technical users (64%). Churn rate 28% annually."

---

## FOUR-FILE OUTPUT PACKAGE {#output-package}

### Package Overview

Step 5 analysis produces FOUR complementary outputs:

1. **Markdown Analysis** (.md) - Master document, complete analysis
2. **DOCX Part 1** - Core Analysis (Sections 1-4)
3. **DOCX Part 2** - Strategic Analysis (Sections 5-11)
4. **DOCX Part 3** - Interview Guide (Section 12)

### File 1: Markdown Analysis (.md)

**Purpose:** Master working document

**Content:** All 12 sections
1. INPUTS USED
2. REQUESTERS TABLE
3. NEEDS ANALYSIS
4. EXISTING SOLUTIONS
5. EVIDENCE REQUIREMENTS & VALIDATION STATUS
6. REQUESTERS RELIABILITY ASSESSMENT
7. INTEGRATION WITH BUSINESS MODEL
8. COMPETITIVE POSITIONING INSIGHTS
9. RECOMMENDATIONS FOR IMMEDIATE ACTION
10. EVIDENCE-BASED VALIDATION CHECKLIST
11. CONCLUSION - PATH FORWARD
12. APPENDIX - CUSTOMER DISCOVERY INTERVIEW GUIDE

**Format:**
- Plain markdown (.md file)
- Headers: # for main sections, ## for subsections
- Tables: Use markdown table syntax
- Lists: Bullets (•) or dashes (-)
- Checklists: - [ ] for unchecked, - [x] for checked

**Audience:**
- Internal team (primary document)
- Collaborators providing feedback
- Version control and iteration

**Length:** 15-25 pages (markdown)

**Quality Requirements:**
- All content sections complete
- All tables properly formatted
- All character limits respected
- All checkboxes included
- All placeholders replaced with actual content

### File 2: DOCX Part 1 - Core Analysis

**Purpose:** Professional stakeholder summary

**Content:** Sections 1-4 only
- INPUTS USED
- REQUESTERS TABLE (6-10 roles)
- NEEDS ANALYSIS (10 needs)
- EXISTING SOLUTIONS (5-6 alternatives)

**Format:** Professionally formatted Microsoft Word (.docx)

**Styling Requirements:**

**Colors:**
- Primary Blue: #2E5C8A (section headers)
- Secondary Teal: #17A2B8 (subsection headers)
- Neutral Gray: #6C757D (body text accents)

**Typography:**
- Font: Calibri (or Arial)
- Section headers: 14pt, Bold, Blue
- Subsection headers: 12pt, Bold, Teal
- Body text: 11pt, Regular, Black
- Table headers: 11pt, Bold, White on Blue background

**Tables:**
- Style: Light Grid - Accent 1
- Header row: Blue background (#2E5C8A), white text
- Alternating row shading: White / Very light gray (#F8F9FA)
- All borders: 0.5pt, Light gray (#CCCCCC)

**Page Setup:**
- Margins: 1.0" all sides
- Orientation: Portrait
- Line spacing: 1.15
- Page numbers: Bottom center, "Page X of Y"

**Audience:**
- Executive team
- Investors and funders
- Committee members
- Strategic partners
- Board of directors

**Use Cases:**
- Investment committee meetings
- Board presentations
- Funding proposal appendix
- Partner due diligence

**Length:** 4-6 pages

### File 3: DOCX Part 2 - Strategic Analysis & Recommendations

**Purpose:** Internal planning and decision-making

**Content:** Sections 5-11
- EVIDENCE REQUIREMENTS & VALIDATION STATUS
- REQUESTERS RELIABILITY ASSESSMENT
- INTEGRATION WITH BUSINESS MODEL
- COMPETITIVE POSITIONING INSIGHTS
- RECOMMENDATIONS FOR IMMEDIATE ACTION
- EVIDENCE-BASED VALIDATION CHECKLIST
- CONCLUSION - PATH FORWARD

**Format:** Professionally formatted Microsoft Word (.docx)

**Special Formatting Elements:**

**Priority Badges:**
- High Priority: Red box (#DC3545), white text, 10pt bold
- Medium Priority: Orange box (#FD7E14), white text, 10pt bold
- Low Priority: Gray box (#6C757D), white text, 10pt bold

**Callout Boxes:**
- Background: Light blue (#E7F3FF) or light red (#FFF5F5)
- Border: 4pt solid left border, matching category color
- Padding: 12pt all sides
- Font: 12pt Bold for callouts

**Risk Badges:**
- Low Risk: Green (#28A745)
- Medium Risk: Orange (#FD7E14)
- High Risk: Red (#DC3545)

**Warning Boxes:**
- Background: Very light red (#FFF5F5)
- Icon: ⚠️ before text
- Border: 4pt solid red left border

**Audience:**
- Internal core team
- Leadership making investment decisions
- Board members needing strategic guidance
- Major investors (due diligence)

**Use Cases:**
- Internal planning sessions
- Go/no-go investment decisions
- Strategic partner negotiations
- Board strategy discussions

**Length:** 8-12 pages

### File 4: DOCX Part 3 - Customer Discovery Interview Guide

**Purpose:** Practical field tool for conducting interviews

**Content:** Section 12 - Interview Guide
- INTERVIEW STRUCTURE (6 phases, 45-60 minutes)
- KEY INSIGHTS TO CAPTURE
- INTERVIEW BEST PRACTICES
- COMMON PITFALLS TO AVOID
- TARGET INTERVIEW SEGMENTS
- INTERVIEW TRACKING FORM

**Format:** Field-optimized Microsoft Word (.docx)

**Special Formatting:**

**Phase Headers:**
- Light blue background (#E7F3FF)
- 13pt Bold, Teal text
- Left border: 4pt solid teal
- Timing badge: Gray box, right-aligned, "⏱ 5 min"

**Interview Questions:**
- Numbered lists
- Indented for easy scanning
- "Listen for:" in italics below each question

**Icons for Key Insights:**
- Use emojis for visual reference
- Example: 😣 Pain Intensity, 💰 Willingness to Pay, 🚫 Objections

**Page Setup (optimized for field use):**
- Margins: 0.75" all sides (narrower)
- Line spacing: 1.0 (tighter)
- Spacing after paragraphs: 3pt (tighter)
- Can be printed double-sided for compact field guide

**Audience:**
- Team members conducting interviews
- Sales/BD team
- External consultants
- Students/interns

**Use Cases:**
- Field interviews (print and bring)
- Training on interview methodology
- Standardizing process across team
- Documenting methodology for stakeholders

**Length:** 5-7 pages (approximately 3-4 sheets if printed double-sided)

### Output Package Quality Checks

Before delivering, verify:

- [ ] All 4 files created (1 MD + 3 DOCX)
- [ ] Markdown file includes all 12 sections
- [ ] DOCX Part 1 includes only Sections 1-4
- [ ] DOCX Part 2 includes only Sections 5-11
- [ ] DOCX Part 3 includes only Section 12
- [ ] All DOCX files have professional formatting applied
- [ ] All tables formatted consistently across files
- [ ] Content is identical across MD and DOCX versions (no discrepancies)
- [ ] File names follow naming convention (see File Naming section)
- [ ] All documents include proper headers and footers
- [ ] All documents include page numbers
- [ ] DOCX files compatible with Word 2016+ and Google Docs

---

## VALIDATION PRIORITY SYSTEM {#validation-priority}

### Three-Tier Prioritization Framework

**Purpose:** Identify which validation gaps threaten business model viability vs. refinement details

### Priority Tier Definitions

**HIGH PRIORITY [requires customer interviews]**

**Definition:** Questions directly affecting business model viability

**Characteristics:**
- Answers determine go/no-go decisions
- Directly impact revenue model or pricing
- Affect core value proposition
- Determine target segment selection
- Inform major investment decisions

**Must be validated BEFORE:**
- Major capital investment
- Production scale-up
- Fundraising rounds
- Strategic partnerships
- Team expansion

**Typical Questions:**
1. Do target customers experience significant pain from identified problem?
2. What specific price would they pay? (Not "interested" - actual dollar amounts)
3. Which segments have most urgent/intense needs?
4. What technical specifications are critical vs. nice-to-have?
5. What are realistic adoption timelines and decision processes?
6. Who makes purchasing decisions and what are their criteria?
7. How do they quantify value? (ROI expectations, payback periods)
8. What would cause them to reject solution? (Deal-breaker objections)

**Validation Method:**
- Customer discovery interviews (20-30 across segments)
- Pilot testing with paying customers
- Willingness-to-pay studies with specific price points

---

**MEDIUM PRIORITY [requires market research]**

**Definition:** Questions answerable through secondary research that inform strategy but don't determine viability

**Characteristics:**
- Can be answered without primary customer research
- Important for planning but not for go/no-go
- Inform operational details, not core model
- Can be refined during execution
- Available through reports, data, expert consultation

**Must be validated BEFORE:**
- Detailed business plan finalization
- Market entry execution
- Channel strategy implementation
- Marketing campaign launch

**Typical Questions:**
1. What's the addressable market size? (TAM, SAM, SOM)
2. What certifications or regulatory approvals required? (Timeline, cost)
3. What are typical contract terms and volumes in this industry?
4. Who are key influencers in purchase decisions? (not decision-makers)
5. What industry trends affect adoption? (macro trends)
6. What are competitive pricing norms? (published pricing)
7. What distribution channels dominate this market?
8. What marketing channels reach target segments effectively?

**Validation Method:**
- Industry reports and market studies
- Regulatory research
- Competitive intelligence
- Expert interviews (not customer interviews)
- Trade association data

---

**LOW PRIORITY [can be refined later]**

**Definition:** Nice-to-know details that don't affect go/no-go or major strategic decisions

**Characteristics:**
- Refinement details, not foundational questions
- Can be learned during execution
- Don't affect business model viability
- Minor optimizations vs. core strategy
- Often segment-specific nuances

**Can be validated DURING:**
- Initial market entry
- Pilot programs
- Early customer relationships
- Iterative product development

**Typical Questions:**
1. Detailed decision-making processes for each segment (beyond key criteria)
2. Specific technical preferences by application sub-type
3. Preferred communication channels for each persona
4. Detailed competitive feature comparisons
5. Brand perception nuances
6. Detailed user workflow variations

**Validation Method:**
- Learn through ongoing customer relationships
- Iterative feedback during pilots
- Analytics from early users
- A/B testing during execution

### Applying the Priority System

**Section 5 of Analysis:**

Under "Critical Validation Gaps," organize all open questions by priority:

```markdown
### Critical Validation Gaps

**HIGH PRIORITY [requires customer interviews]:**
1. [Question directly affecting business model viability]
2. [Question directly affecting business model viability]
...

**MEDIUM PRIORITY [requires market research]:**
6. [Question answerable through secondary research]
7. [Question answerable through secondary research]
...

**LOW PRIORITY [can be refined later]:**
11. [Nice-to-know detail that doesn't affect go/no-go]
12. [Nice-to-know detail that doesn't affect go/no-go]
```

**Numbering Convention:**
- HIGH: Numbers 1-5 (typically 5-8 questions)
- MEDIUM: Numbers 6-10 (typically 5-8 questions)
- LOW: Numbers 11-12 (typically 2-4 questions)

**Decision Rule:**

**If you have 5+ HIGH priority gaps unfilled:**
→ STOP further development
→ START customer discovery immediately
→ DO NOT proceed with major investment

**If you have 3+ MEDIUM priority gaps unfilled:**
→ PAUSE detailed planning
→ CONDUCT market research
→ CONSIDER contingency scenarios

**If only LOW priority gaps remain:**
→ PROCEED with execution
→ VALIDATE through pilots and early customers
→ ITERATE based on feedback

---

## VALIDATION CHECKLIST (40+ ITEMS) {#validation-checklist}

### Comprehensive Evidence-Based Checklist

**Purpose:** Systematic verification of validation completeness before claiming strong desirability

**Section 10 of Analysis:** Include this complete checklist

**Format:** Markdown checkboxes `- [ ]` for unchecked, `- [x]` for completed

### Requesters Validation (10 items)

**Before checking any box, have explicit evidence:**

- [ ] **5+ interviews per primary requester segment completed**
      Evidence: Interview transcripts, notes, or recordings for 5+ customers per segment

- [ ] **Users vs. buyers distinction clarified for B2B segments**
      Evidence: Documented roles, decision authority, and influence mapping

- [ ] **Decision-making authority identified (who makes purchasing decisions)**
      Evidence: Org charts, interview confirmations, or documented approval processes

- [ ] **Budget/purchasing power confirmed for each segment**
      Evidence: Stated budgets, historical spending, or budget cycle documentation

- [ ] **Timeline for purchase decisions understood**
      Evidence: Average sales cycle, decision factors triggering timeline, seasonal patterns

- [ ] **Pain intensity quantified for each segment**
      Evidence: Cost of problem (time, money, risk) stated in specific numbers

- [ ] **Segments prioritized by evidence (not gut feel)**
      Evidence: Scoring matrix with objective criteria, not team opinions

- [ ] **Requester profiles validated with real examples**
      Evidence: Specific companies/people matching each profile

- [ ] **Scale and scope verified for each segment**
      Evidence: Market size data, segment population, or addressable accounts

- [ ] **Alternative requesters explored and ruled out**
      Evidence: Considered adjacent segments and documented why excluded

### Needs Validation (12 items)

**Before checking any box, have explicit evidence:**

- [ ] **All 10 needs tested with customers (not just assumed from team knowledge)**
      Evidence: Interview quotes, survey data, or observational studies for each need

- [ ] **Needs ranked by importance across segments**
      Evidence: Forced-ranking exercises, MaxDiff analysis, or rated importance scores

- [ ] **Pain intensity quantified (cost, time, risk for each need)**
      Evidence: "This costs us $X/month" or "We lose Y hours/week" - specific numbers

- [ ] **Current workarounds documented (what do they do today)**
      Evidence: Detailed description of current state and processes for each need

- [ ] **Willingness to switch validated (not just "interested" but concrete commitment)**
      Evidence: "Would you commit to pilot?" or "Would you sign LOI?" - yes/no answers

- [ ] **Needs connected to willingness to pay specific amounts**
      Evidence: "I'd pay $X to solve Need A" - dollar amounts, not "that would be valuable"

- [ ] **Each need is distinct (tested with overlap analysis)**
      Evidence: Can satisfy one need without others - confirmed through customer feedback

- [ ] **All needs under 60 characters (verified with character counter)**
      Evidence: Character count for each need documented

- [ ] **Tasks/Pains/Expectations correctly categorized**
      Evidence: Customer language maps to categories (not forced by analyst)

- [ ] **No embedded solutions in need statements**
      Evidence: Needs describe problems/outcomes, not specific solutions

- [ ] **Needs frequency/severity documented**
      Evidence: Daily vs. monthly occurrence, critical vs. annoying severity

- [ ] **Unmet needs validated (not satisfied by existing solutions)**
      Evidence: Gap analysis showing how current solutions fail on each need

### Existing Solutions Validation (10 items)

**Before checking any box, have explicit evidence:**

- [ ] **All major competitors tested or researched directly (not just website reviews)**
      Evidence: Hands-on testing, demos, trials, or detailed competitive teardowns

- [ ] **Customer satisfaction with alternatives assessed through interviews**
      Evidence: "How satisfied are you with Solution X?" (1-10 scale) from 10+ customers

- [ ] **Switching costs quantified (financial, operational, psychological)**
      Evidence: Cost to switch ($, time, risk, training) stated in specific terms

- [ ] **Non-obvious substitutes identified (indirect competitors)**
      Evidence: Customer interviews revealing unexpected alternatives

- [ ] **"Doing nothing" appeal honestly evaluated**
      Evidence: Percentage who prefer status quo and why, from customer research

- [ ] **Competitive advantages tested with customers (not just assumed)**
      Evidence: "Which is more important: Feature A or B?" - validated preferences

- [ ] **Market share or adoption data for each competitor**
      Evidence: Published data, estimates from credible sources, or survey results

- [ ] **Why customers chose current solution documented**
      Evidence: Interview quotes about selection criteria and decision factors

- [ ] **Competitor limitations confirmed by users (not assumed)**
      Evidence: Customer complaints, documented gaps, or pain points from interviews

- [ ] **Competitive pricing validated with real data**
      Evidence: Actual pricing (not list pricing), including discounts and total cost

### Business Model Alignment (10 items)

**Before checking any box, have explicit evidence:**

- [ ] **Revenue streams tested with target customers (not just theoretical)**
      Evidence: "Would you pay per-use or subscription?" - actual preferences

- [ ] **Pricing validated through customer conversations (specific price points)**
      Evidence: Van Westendorp analysis or "Would you pay $X?" at multiple price points

- [ ] **Go-to-market sequence prioritized by evidence (not gut feel)**
      Evidence: Scored decision matrix with validation data, not opinions

- [ ] **Channel preferences confirmed (how do they want to buy)**
      Evidence: "How do you typically purchase solutions like this?" - interview data

- [ ] **Partnership requirements validated (what partnerships are truly needed)**
      Evidence: "Would you buy from us directly or through Partner X?" - stated preferences

- [ ] **Unit economics validated with real data (not just projections)**
      Evidence: Pilot customer data, actual costs, confirmed pricing, measured CAC

- [ ] **Value propositions tested with customers**
      Evidence: "Which benefit matters most?" - forced ranking or stated preferences

- [ ] **Sales cycle length validated**
      Evidence: Actual time from first contact to close (pilot customers or comparable sales)

- [ ] **Customer acquisition cost estimated from real channels**
      Evidence: Cost per lead from actual campaigns or industry benchmarks for channels

- [ ] **Lifetime value assumptions tested**
      Evidence: Retention rates, expansion revenue, churn from pilots or comparables

### Evidence Quality (5 items)

**Meta-validation of your validation process:**

- [ ] **Interview sample size meets statistical significance (20+ total)**
      Evidence: N ≥ 20 for pattern identification across segments

- [ ] **Interview quality assessed (average 45+ minutes, structured)**
      Evidence: Interview duration and structure documented, transcripts available

- [ ] **Multiple team members conducted interviews (not just one perspective)**
      Evidence: 2+ team members involved to reduce confirmation bias

- [ ] **Interview questions were open-ended (not leading)**
      Evidence: Question guide reviewed for neutrality, no "Wouldn't you love...?" questions

- [ ] **Negative feedback documented (not just positive validation)**
      Evidence: Objections, concerns, and rejections documented honestly

### Total Checklist Items: 47

**Scoring System:**

- **40+ checked (85%+):** Strong desirability validation → Proceed with confidence
- **30-39 checked (64-83%):** Moderate validation → Proceed cautiously, fill priority gaps
- **20-29 checked (43-62%):** Weak validation → Pause major investment, conduct discovery
- **<20 checked (<43%):** Very weak validation → STOP, hypothesis stage only

**Critical Rule:** Don't check boxes you can't defend with evidence. Self-deception is expensive.

---

## COMMON MISTAKES TO AVOID (10+) {#common-mistakes}

### Mistake 1: Fabricating Validation Status

**The Error:**
Claiming "Less than 5 interviewed" when actually zero interviews conducted

**Why It's Dangerous:**
- Creates false confidence in business model
- Leads to investment in unvalidated assumptions
- Discovered during due diligence, destroys credibility
- Causes expensive pivots later

**The Fix:**
Use "Not yet interviewed [validate with interviews]" if zero customer conversations

Mark validation status honestly:
- 0 interviews = "Not yet interviewed"
- 1-5 interviews = "Less than 5 interviewed"
- 6+ interviews = "More than 5 interviewed"

**Detection:**
Investors will ask: "Can I see interview transcripts?" If you can't produce them, you've lost credibility.

---

### Mistake 2: Confusing Users with Buyers (B2B)

**The Error:**
Treating "Hospital staff" as single requester when users ≠ buyers

**Why It's Dangerous:**
- Users care about usability; buyers care about ROI
- Different needs, different value propositions
- Wrong target = failed sales conversations
- Misaligned product development priorities

**The Fix:**
Create separate requester profiles:
- "Hospital Facilities Administrators" (buyers: budget authority, ROI focus)
- "Clinical Staff / Nurses" (users: workflow integration, usability focus)
- "IT Department" (influencers: integration, security, support focus)

**Detection:**
If you can't answer "Who signs the purchase order?" separately from "Who uses it daily?" - you have this problem.

---

### Mistake 3: Needs Exceeding 60 Characters

**The Error:**
"Access affordable cost-competitive domestic raw materials supply sources" (73 characters)

**Why It's Dangerous:**
- Breaks visualization compatibility (Step 6)
- Indicates unclear thinking (can't articulate concisely)
- Makes needs unscannable
- Suggests embedded solutions or compound needs

**The Fix:**
"Access cost-competitive domestic raw materials" (57 characters)

Techniques:
- Remove redundancies ("affordable" + "cost-competitive")
- Cut filler words ("supply sources" → implied)
- Use strong verbs (start with action)
- Split compound needs into distinct needs

**Detection:**
Use character counter. No exceptions to 60-character limit.

---

### Mistake 4: Overlapping/Duplicate Needs

**The Error:**
All the same need worded differently:
- "Maintain cognitive health"
- "Keep brain sharp"
- "Prevent mental decline"

**Why It's Dangerous:**
- Artificially inflates need count
- Masks gaps in understanding
- No distinct value propositions possible
- Fails distinctness test

**The Fix:**
Test: "Could I satisfy Need A without Need B?"

If NO → Same need, remove duplicate

Distinct needs:
- "Track cognitive performance objectively" (measurement)
- "Practice evidence-based brain training" (intervention)
- "Identify early decline signs" (detection)

**Detection:**
Can you satisfy one without the other? If not, they're duplicates.

---

### Mistake 5: Embedding Solutions in Needs

**The Error:**
"Need mobile app to track brain health" ← Embeds solution (mobile app)

**Why It's Dangerous:**
- Constrains solution space artificially
- Customers state solutions, not underlying needs
- Leads to feature-driven development
- Misses better alternatives

**The Fix:**
Extract the actual need: "Track cognitive performance objectively"

Mobile app is ONE possible solution. Others: wearable, web platform, clinical visits, paper journals.

**Detection:**
If your need statement includes a specific technology or method, you've embedded a solution.

---

### Mistake 6: Omitting "Doing Nothing" as Competitor

**The Error:**
Only listing active competitors, ignoring status quo

**Why It's Dangerous:**
- Status quo is the biggest competitor (inertia)
- Many customers choose "good enough" over switching
- Switching costs often exceed perceived benefit
- Leads to overconfident adoption projections

**The Fix:**
Always include final row: "Doing Nothing (Status Quo)"

Honest assessment:
- Why is status quo tolerable?
- What percentage prefer inaction?
- What would overcome inertia?

**Detection:**
If you can't articulate why "doing nothing" is painful, you don't have a compelling value proposition.

---

### Mistake 7: Generic/Vague Requester Descriptions

**The Error:**
"People who need magnets for various industrial uses in different sectors."

**Why It's Dangerous:**
- Can't identify them to interview
- Can't tailor value proposition
- Can't estimate market size
- Can't develop go-to-market strategy

**The Fix:**
"Permanent magnet manufacturers producing NdFeB magnets for industrial applications. Small-medium Brazilian companies importing raw powders from China/Japan. Scale: 15-20 manufacturers nationally facing supply chain vulnerability."

Includes:
- Specific role and industry
- Current behavior and suppliers
- Scale and geography
- Pain points

**Detection:**
Could you use this description to find 10 real companies that match? If not, too generic.

---

### Mistake 8: Superficial Competitive Analysis

**The Error:**
"We looked at their website and it seems outdated."

**Why It's Dangerous:**
- Underestimates competition
- Misses real competitive advantages
- Overestimates differentiation
- Surprises during market entry

**The Fix:**
- Test competitors yourself (trials, demos, purchases)
- Interview their customers (why did they choose? satisfaction?)
- Document specific gaps with evidence
- Quantify market position

"Tested Competitor X for 2 weeks. Interviewed 8 users. 6/8 cited limited customization. Documented 12 specific instances where requests declined."

**Detection:**
Have you actually used the competitor's product? Talked to their customers? If not, your analysis is superficial.

---

### Mistake 9: Treating Assumptions as Facts

**The Error:**
"Customers will pay premium for domestic supply" stated as fact when it's a hypothesis

**Why It's Dangerous:**
- Business model built on unvalidated assumptions
- Pricing strategy based on guesses
- Expensive to discover errors post-launch
- Creates false confidence for investors

**The Fix:**
Explicitly label:

**Strong Evidence:**
"Willingness to pay 15-20% premium for domestic supply (validated with 12/15 manufacturers in pricing study)"

**Weak Evidence / Hypothesis:**
"Assumed willingness to pay premium for domestic supply [REQUIRES VALIDATION: zero pricing studies conducted]"

**Detection:**
For each claim, ask: "What's my evidence?" If you can't cite a source or study, it's an assumption.

---

### Mistake 10: Ignoring Negative Feedback

**The Error:**
Only documenting positive validation, hiding objections and concerns

**Why It's Dangerous:**
- Confirmation bias leads to failed launches
- Objections will surface during sales
- Missed opportunity to refine value proposition
- Looks dishonest to sophisticated investors

**The Fix:**
**Document objections prominently:**

"Customer Objections (from 23 interviews):
- Price sensitivity: 18/23 said <15% premium acceptable (our model assumes 20%)
- Validation period: 15/23 require 6-12 month testing before commitment
- Risk aversion: 12/23 prefer proven reliability over cutting-edge features"

**Detection:**
If your analysis has zero objections, concerns, or negative feedback - you're not being honest or didn't listen.

---

### Mistake 11: Insufficient Interview Sample Size

**The Error:**
Claiming validation with 2-3 interviews per segment

**Why It's Dangerous:**
- 1-3 interviews = anecdotes, not patterns
- High individual variance
- Can't generalize to segment
- Different interviewer might get opposite feedback

**The Fix:**
**Minimum thresholds:**
- 5+ per segment for pattern identification
- 10+ per segment for confidence
- 20+ total across all segments

**Why 5+ matters:**
- Interview 1-2: Interesting anecdotes
- Interview 3-4: Initial patterns emerge
- Interview 5-7: Patterns confirmed or refuted
- Interview 8-10: Edge cases and nuances
- Interview 10+: Confidence in findings

**Detection:**
Count your interviews per segment. <5 = preliminary at best.

---

### Mistake 12: Leading Questions in Interviews

**The Error:**
"Wouldn't it be great if you had a domestic supplier?"

**Why It's Dangerous:**
- Plants ideas instead of discovering needs
- Customers tell you what you want to hear (politeness)
- False validation
- Leads to products nobody actually wants

**The Fix:**
**Open-ended, neutral questions:**
- ✓ "Tell me about your supply chain challenges"
- ✓ "Walk me through how you source materials today"
- ✓ "What's working well? What would you change?"
- ✗ "Wouldn't it be great if..."
- ✗ "Don't you think domestic supply would be better?"

**Detection:**
Review your interview questions. If they suggest the answer, they're leading.

---

### Mistake 13: Pitching Too Early in Interviews

**The Error:**
Introducing your solution in first 5 minutes of interview

**Why It's Dangerous:**
- Contaminates their feedback
- They react to your pitch, not share real needs
- You hear what they think you want to hear
- Miss discovering their actual priorities

**The Fix:**
**Interview structure (45-60 minutes):**
- Phase 1-3 (30-35 min): Understand their world, current solutions, problems
- Phase 4 (10 min): Validate pricing and decision factors
- Phase 5 (10 min): Introduce your solution LAST
- Phase 6 (5 min): Close with referrals

**Don't pitch until you've learned their needs.**

**Detection:**
If you introduce your solution before minute 30, you're pitching too early.

---

### Total Common Mistakes: 13

**Prevention Checklist:**

Review your analysis against all 13 mistakes before finalizing:
- [ ] No fabricated validation status
- [ ] Users vs. buyers distinguished (B2B)
- [ ] All needs ≤60 characters
- [ ] No overlapping/duplicate needs
- [ ] No embedded solutions in needs
- [ ] "Doing nothing" included as competitor
- [ ] Requester descriptions specific and detailed
- [ ] Competitive analysis based on testing and user interviews
- [ ] Assumptions explicitly labeled as hypotheses
- [ ] Negative feedback and objections documented
- [ ] Sample size ≥5 per segment (or marked as insufficient)
- [ ] Interview questions were open-ended, not leading
- [ ] Solution pitched AFTER understanding needs (not before)

---

## FILE NAMING CONVENTIONS {#file-naming}

### Standard Naming Format

**Pattern:** `Vianeo_Desirability_[PartNumber]_[Description]_[ProjectName].ext`

**Components:**
1. **Vianeo_Desirability** - Framework identifier (consistent across all files)
2. **[PartNumber]** - File number in package (Markdown, Part1, Part2, Part3)
3. **[Description]** - Content descriptor
4. **[ProjectName]** - Project identifier (abbreviated, no spaces)
5. **.ext** - File extension (.md or .docx)

### File-Specific Naming

**File 1: Markdown Analysis**
```
Vianeo_Desirability_Markdown_[ProjectName].md
```

**Examples:**
- `Vianeo_Desirability_Markdown_Rare_Earth_Brazil.md`
- `Vianeo_Desirability_Markdown_Cognitive_Health_Wearable.md`
- `Vianeo_Desirability_Markdown_Supply_Chain_Platform.md`

---

**File 2: DOCX Part 1 - Core Analysis**
```
Vianeo_Desirability_Part1_CoreAnalysis_[ProjectName].docx
```

**Examples:**
- `Vianeo_Desirability_Part1_CoreAnalysis_Rare_Earth_Brazil.docx`
- `Vianeo_Desirability_Part1_CoreAnalysis_Cognitive_Health_Wearable.docx`

---

**File 3: DOCX Part 2 - Strategic Analysis**
```
Vianeo_Desirability_Part2_StrategicAnalysis_[ProjectName].docx
```

**Examples:**
- `Vianeo_Desirability_Part2_StrategicAnalysis_Rare_Earth_Brazil.docx`
- `Vianeo_Desirability_Part2_StrategicAnalysis_Cognitive_Health_Wearable.docx`

---

**File 4: DOCX Part 3 - Interview Guide**
```
Vianeo_Desirability_Part3_InterviewGuide_[ProjectName].docx
```

**Examples:**
- `Vianeo_Desirability_Part3_InterviewGuide_Rare_Earth_Brazil.docx`
- `Vianeo_Desirability_Part3_InterviewGuide_Cognitive_Health_Wearable.docx`

---

### Project Name Guidelines

**Format Requirements:**
- Abbreviated but recognizable
- No spaces (use underscores)
- 2-5 words maximum
- CamelCase or underscore_separated
- Consistent across all files

**Examples:**
- ✓ `Rare_Earth_Brazil`
- ✓ `Cognitive_Health_Wearable`
- ✓ `Supply_Chain_Platform`
- ✓ `AI_Medical_Diagnosis`
- ✗ `Project` (too generic)
- ✗ `Spherical Neodymium Iron Boron Powders for Brazilian Additive Manufacturing Applications` (too long, has spaces)
- ✗ `REE_NDFE_BRAZIL_2025` (too many acronyms)

### Version Control (Optional)

If versioning is needed:

```
Vianeo_Desirability_Part1_CoreAnalysis_[ProjectName]_v[X.Y].docx
```

**Version numbering:**
- v1.0 - Initial release
- v1.1 - Minor updates (typos, formatting)
- v2.0 - Major revision (new interviews, changed segments)

**Example:**
- `Vianeo_Desirability_Part1_CoreAnalysis_Rare_Earth_Brazil_v1.0.docx`
- `Vianeo_Desirability_Part1_CoreAnalysis_Rare_Earth_Brazil_v2.0.docx` (after customer discovery)

### File Organization

**Recommended folder structure:**

```
project_name/
├── vianeo_analysis/
│   ├── step_5_desirability/
│   │   ├── Vianeo_Desirability_Markdown_[ProjectName].md
│   │   ├── Vianeo_Desirability_Part1_CoreAnalysis_[ProjectName].docx
│   │   ├── Vianeo_Desirability_Part2_StrategicAnalysis_[ProjectName].docx
│   │   ├── Vianeo_Desirability_Part3_InterviewGuide_[ProjectName].docx
│   │   └── supporting_materials/
│   │       ├── interview_transcripts/
│   │       ├── market_research/
│   │       └── competitive_analysis/
```

---

## QUALITY GATES & ACCEPTANCE CRITERIA {#quality-gates}

### Pre-Delivery Quality Gates

Before considering Step 5 analysis complete, pass ALL gates:

### Gate 1: Completeness

**Criteria:**
- [ ] All 4 files created (1 MD + 3 DOCX)
- [ ] Markdown includes all 12 sections
- [ ] All mandatory subsections present
- [ ] All tables complete (no empty rows with placeholders)
- [ ] All checklists included (checkboxes functional)
- [ ] All recommendations include metrics and timelines

**Failure condition:** Any section missing or placeholder content remaining

---

### Gate 2: Requesters Quality

**Criteria:**
- [ ] 6-10 distinct requesters (no fewer, no more)
- [ ] Each requester description 50-120 words
- [ ] Reliability ratings use exact prescribed phrases
- [ ] Users vs. buyers distinguished (B2B contexts)
- [ ] All descriptions include scale/scope
- [ ] No overlapping or duplicate requesters

**Failure condition:** Generic descriptions, fabricated reliability, overlapping profiles

---

### Gate 3: Needs Quality

**Criteria:**
- [ ] Exactly 10 needs (minimum) across 3 categories
- [ ] All needs ≤60 characters (character count documented)
- [ ] Each need is distinct (passes "Could I satisfy A without B?" test)
- [ ] No embedded solutions in need statements
- [ ] Distribution: 3-4 per category (Tasks/Pains/Expectations)
- [ ] Evidence status marked for each need

**Failure condition:** Any need >60 characters, overlapping needs, embedded solutions

---

### Gate 4: Competitive Analysis Quality

**Criteria:**
- [ ] 5-6 solutions documented
- [ ] "Doing Nothing" included as final row
- [ ] Limitations are specific and evidence-based
- [ ] Each solution includes market position or adoption data
- [ ] Non-obvious substitutes identified
- [ ] Tested competitors directly or interviewed users

**Failure condition:** Generic limitations ("not very good"), missing status quo, superficial research

---

### Gate 5: Validation Honesty

**Criteria:**
- [ ] Validation status is brutally honest (no fabrication)
- [ ] Evidence gaps explicitly identified and prioritized
- [ ] Weak validation acknowledged (not hidden)
- [ ] Interview/research data status specific and detailed
- [ ] Assumptions labeled as hypotheses
- [ ] Negative feedback documented

**Failure condition:** Fabricated interviews, hidden gaps, exaggerated validation

---

### Gate 6: Strategic Recommendations

**Criteria:**
- [ ] 3 priorities with clear timelines
- [ ] Each priority has specific, measurable success metrics
- [ ] Recommendations are actionable (not vague)
- [ ] Risk assessment included (technology risk, market risk)
- [ ] Clear bottom-line recommendation (go/no-go with conditions)
- [ ] Stop gates specified if validation is weak

**Failure condition:** Vague recommendations, missing metrics, no clear path forward

---

### Gate 7: Professional Formatting

**Criteria:**
- [ ] All DOCX files use consistent styling
- [ ] Tables formatted professionally with headers
- [ ] Color palette applied correctly
- [ ] Page numbers and footers included
- [ ] Headers and section breaks appropriate
- [ ] Files compatible with Word 2016+ and Google Docs

**Failure condition:** Inconsistent formatting, broken tables, missing page elements

---

### Gate 8: Internal Consistency

**Criteria:**
- [ ] Content identical across MD and DOCX versions
- [ ] Requesters in Section 2 match evidence discussion in Section 6
- [ ] Needs in Section 3 connect to competitor limitations in Section 4
- [ ] Validation gaps in Section 5 connect to recommendations in Section 9
- [ ] File names follow convention
- [ ] All cross-references accurate

**Failure condition:** Discrepancies between files, broken internal logic

---

### Gate 9: Validation Checklist

**Criteria:**
- [ ] 47-item validation checklist completed
- [ ] Score calculated (% checked)
- [ ] Honest assessment (no false checks)
- [ ] If score <65%, explicit warning included
- [ ] High-priority gaps identified

**Failure condition:** Checklist incomplete, dishonest checking, no score

---

### Gate 10: Stakeholder Readiness

**Criteria:**
- [ ] Core Analysis (Part 1) ready for executive presentation
- [ ] Strategic Analysis (Part 2) provides clear decision framework
- [ ] Interview Guide (Part 3) ready for field use
- [ ] Markdown version ready for team collaboration
- [ ] All files polished and professional

**Failure condition:** Documents not presentation-ready, unclear purpose

---

### Acceptance Scoring

**Pass all gates:** Ready for delivery

**Pass 8-9 gates:** Minor revisions needed, can proceed with caveats

**Pass 6-7 gates:** Significant revisions required, not ready for delivery

**Pass <6 gates:** Major rework needed, restart analysis

---

### Final Validation Statement

Include in Section 11 (Conclusion):

```markdown
### Quality Gate Assessment

**Gates Passed:** [X] / 10

**Status:** [Ready for Delivery / Revisions Needed / Major Rework Required]

**Validation Checklist Score:** [Y]% ([Z] of 47 items checked)

**Overall Desirability Assessment:** [Strong / Moderate / Weak / Very Weak]

**Recommendation:** [Proceed / Proceed with Caution / Pause / Stop]
```

---

## APPENDIX: CHARACTER COUNTER REFERENCE

### 60-Character Examples (EXACTLY at limit)

```
Access cost-competitive domestic raw materials supply  (59)
Enable 3D printing applications with spherical powders  (60)
Eliminate dependency on Chinese and Japanese imports    (60)
Reduce vulnerability to geopolitical trade disruptions  (60)
Support domestic manufacturing ecosystem development    (60)
```

### Over-Limit Examples (FAIL - must shorten)

```
Access affordable cost-competitive domestic raw materials supply sources  (73) ❌
Significantly reduce operational costs through process optimization      (71) ❌
Maintain cognitive health and prevent age-related mental decline         (68) ❌
```

### Shortening Techniques

**Remove redundancy:**
- "affordable cost-competitive" → "cost-competitive" (affordable implied)
- "raw materials supply sources" → "raw materials" (supply implied)

**Remove filler words:**
- "Significantly reduce" → "Reduce"
- "through process optimization" → delete (method, not outcome)

**Use strong verbs:**
- "Need to maintain" → "Maintain"
- "Work to reduce" → "Reduce"

**Result:**
- 73 chars → 57 chars: "Access cost-competitive domestic raw materials"
- 71 chars → 13 chars: "Reduce operational costs"
- 68 chars → 38 chars: "Maintain cognitive health with age"

---

## DOCUMENT METADATA

**Format Specification Version:** 1.0
**Release Date:** 2025-01-15
**Applicable Framework:** VIANEO 13-Step Business Model Evaluation Playbook
**Step:** 5 - Desirability: Needs/Requesters Analysis
**Weight in Framework:** 25% (highest weight)
**Document Length:** ~3,600 words
**Last Updated:** 2025-01-15

**Companion Documents:**
- Template: `Step5_NeedsRequesters_Markdown_Template.md`
- DOCX Format Spec Part 1: `Step5_NeedsRequesters_DOCX_Part1_Template.md`
- DOCX Format Spec Part 2: `Step5_NeedsRequesters_DOCX_Part2_Template.md`
- DOCX Format Spec Part 3: `Step5_NeedsRequesters_DOCX_Part3_Template.md`
- Reference Guide: `VIANEO_Desirability_Complete_Reference.md`

**Maintained by:** VIANEO Framework Core Team
**Questions/Feedback:** See repository documentation

---

**END OF FORMAT SPECIFICATION**
