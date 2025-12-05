# STEP 0a: Canvas Extraction

**Time Required:** 15-30 minutes
**Output:** Platform-aligned Vianeo Canvas (structured data entry)
**Purpose:** Transform raw venture materials into the initial Vianeo platform canvas structure

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 0a: Canvas Extraction from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_00a_canvas_extraction.md`.

**Required Attachments:**
- Raw venture materials (pitch deck, business plan, one-pager)
- Screenshot of empty or partially-complete Vianeo canvas (if available)

**Output Destination:** Vianeo platform canvas fields

---

## Overview

Step 0a is the **foundation step** that aligns raw venture materials with the Vianeo platform's canvas structure. This step ensures all subsequent evaluation steps have properly structured input data.

**Relationship to Step 0b:**
- **Step 0a (this step):** Populates Vianeo platform canvas fields
- **Step 0b:** Generates the structured Executive Brief document from canvas data

Step 0a must be completed before Step 0b.

---

## Instructions for AI Assistant

Transform the provided venture materials into structured canvas entries. For each canvas field:

1. **Extract** relevant information from source materials
2. **Condense** to platform field character limits
3. **Preserve** factual accuracy - do not embellish or infer beyond evidence
4. **Flag** where information is missing or unclear

---

## Canvas Structure

### Section 1: Project Identity

**Field 1.1: Project Name**
- Character limit: 50
- Source: Company/project name from materials
- Format: Official name as it appears in legal/branding

**Field 1.2: One-Line Description**
- Character limit: 150
- Source: Tagline, mission statement, or first sentence of pitch
- Format: "[What it is] that [what it does] for [who]"
- Example: "AI-powered maintenance platform that predicts equipment failures for industrial manufacturers"

**Field 1.3: Problem Statement**
- Character limit: 300
- Source: Problem section of pitch deck, pain points from business plan
- Format: Specific, measurable problem with scope indicator
- Must answer: What problem? Who has it? How big is it? Why unsolved?

**Field 1.4: Solution Overview**
- Character limit: 300
- Source: Solution section of pitch deck, product description
- Format: How the solution addresses the problem
- Must answer: What does it do? How does it work? Why is it better?

---

### Section 2: Market Context

**Field 2.1: Target Market**
- Character limit: 200
- Source: Market section of pitch, customer segments
- Format: Primary market segment with geographic/industry scope
- Must include: Segment name, size indicator, geography

**Field 2.2: Customer Segments**
- Character limit: 250
- Source: Customer personas, target audience section
- Format: List 2-4 primary customer segments
- Example: "1) Plant managers at mid-size manufacturers, 2) Maintenance directors at industrial facilities, 3) Operations VPs seeking cost reduction"

**Field 2.3: Market Size**
- Character limit: 150
- Source: Market size analysis, TAM/SAM/SOM
- Format: TAM with methodology source
- Example: "TAM: $4.2B predictive maintenance market (Gartner 2024), SAM: $800M industrial segment, SOM: $50M initial target"

---

### Section 3: Solution Details

**Field 3.1: Key Features**
- Character limit: 300
- Source: Product features, technical specifications
- Format: 3-5 bullet points of core features
- Focus: Differentiating features, not generic capabilities

**Field 3.2: Technology/Approach**
- Character limit: 250
- Source: Technical approach, methodology section
- Format: Brief description of how it works technically
- Include: Key technologies, algorithms, or methodologies

**Field 3.3: Differentiation**
- Character limit: 200
- Source: Competitive advantages, unique selling points
- Format: 2-3 specific differentiators vs. alternatives
- Must answer: Why this solution over competitors?

---

### Section 4: Business Model

**Field 4.1: Revenue Model**
- Character limit: 200
- Source: Business model, monetization strategy
- Format: How money is made (subscription, transaction, license, etc.)
- Include: Pricing approach if available

**Field 4.2: Go-to-Market**
- Character limit: 200
- Source: Sales strategy, distribution approach
- Format: Primary channels and sales approach
- Example: "Direct enterprise sales + channel partnerships with equipment vendors"

---

### Section 5: Team

**Field 5.1: Founding Team**
- Character limit: 250
- Source: Team bios, LinkedIn profiles
- Format: Founder names with relevant credentials
- Include: Most relevant experience for this venture

**Field 5.2: Key Hires/Gaps**
- Character limit: 150
- Source: Org chart, hiring plans
- Format: Current key team + identified gaps
- Be honest about gaps if evident

---

### Section 6: Traction & Stage

**Field 6.1: Current Stage**
- Character limit: 100
- Source: Stage indicators throughout materials
- Options: Idea / Prototype / Pilot / Early Commercialization / Growth
- Include: Key milestone achieved at this stage

**Field 6.2: Traction Metrics**
- Character limit: 200
- Source: Traction section, KPIs, milestones
- Format: Quantified achievements
- Example: "3 pilot customers, 12 LOIs, $50K ARR, 40% MoM growth"

**Field 6.3: Funding Status**
- Character limit: 150
- Source: Funding section, cap table hints
- Format: Current raise, prior funding, investors
- Example: "Raising $1.5M seed; Prior: $200K pre-seed from angels"

---

## Output Format

Generate canvas entries in this format for easy platform input:

```
## VIANEO CANVAS - [Project Name]

### Section 1: Project Identity
**1.1 Project Name:** [Entry]
**1.2 One-Line Description:** [Entry - 150 chars]
**1.3 Problem Statement:** [Entry - 300 chars]
**1.4 Solution Overview:** [Entry - 300 chars]

### Section 2: Market Context
**2.1 Target Market:** [Entry - 200 chars]
**2.2 Customer Segments:** [Entry - 250 chars]
**2.3 Market Size:** [Entry - 200 chars]

### Section 3: Solution Details
**3.1 Key Features:** [Entry - 300 chars]
**3.2 Technology/Approach:** [Entry - 250 chars]
**3.3 Differentiation:** [Entry - 200 chars]

### Section 4: Business Model
**4.1 Revenue Model:** [Entry - 200 chars]
**4.2 Go-to-Market:** [Entry - 200 chars]

### Section 5: Team
**5.1 Founding Team:** [Entry - 250 chars]
**5.2 Key Hires/Gaps:** [Entry - 150 chars]

### Section 6: Traction & Stage
**6.1 Current Stage:** [Entry - 100 chars]
**6.2 Traction Metrics:** [Entry - 200 chars]
**6.3 Funding Status:** [Entry - 150 chars]

---

## MISSING INFORMATION

[List any fields where information was not available in source materials]

## ASSUMPTIONS MADE

[List any inferences or assumptions required to complete fields]

## QUESTIONS FOR FOUNDERS

[List clarifying questions for missing or unclear information]
```

---

## Validation Checklist

Before completing Step 0a:

- [ ] All 15 canvas fields populated (or marked as missing)
- [ ] Character limits respected for each field
- [ ] No information invented - only extracted from source materials
- [ ] Missing information explicitly flagged
- [ ] Assumptions documented
- [ ] Questions for founders listed (if applicable)

---

## Next Step

After completing Step 0a, proceed to:

**Step 0b: Executive Brief Extraction**
- Uses canvas data as primary input
- Generates the 7-section structured Executive Brief
- See: `prompts/step_00_executive_brief_extraction.md`

---

## File Naming

Save canvas output as:
- `[ProjectName]_[YYYY-MM-DD]_00a_Canvas.md`

Example:
- `AcmeMonitoring_2025-01-15_00a_Canvas.md`

---

**Version:** 1.0
**Created:** 2025-12-05
**Framework:** VIANEO Business Model Evaluation Methodology
