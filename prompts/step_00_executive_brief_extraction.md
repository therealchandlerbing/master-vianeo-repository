# STEP 0: Executive Brief Extraction

**Time Required:** 20-30 minutes
**Output:** Executive Brief (Markdown + DOCX)
**Purpose:** Transform raw application materials into structured, standardized Executive Brief

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`. Full step context, templates, and examples are documented in the GITHUB Master Vianeo Repository.

**Standard Call Pattern:**
> Execute the Step 0: Executive Brief Extraction from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_00_executive_brief_extraction.md`.

**Required Attachments:**
- Raw application materials (PDF, DOCX, or text)
- Any supporting documents (pitch decks, business plans, etc.)

---

## Overview

Step 0 extracts and structures startup/project information into a standardized Executive Brief format with **strict character limits** to ensure clarity and conciseness. This brief becomes the foundation for all subsequent evaluation steps.

---

## Instructions for AI Assistant

Based on the uploaded application materials, extract and structure information into the Executive Brief format below. **Follow character limits exactly** - they are not suggestions.

---

## EXECUTIVE BRIEF STRUCTURE

### B1: Project Name and One-Line Description

**Project Name:** [Official name]

**One-Line Description (MAX 150 CHARACTERS):**

Requirements:
- Capture WHO benefits, WHAT problem is solved, HOW (general approach)
- No marketing fluff or buzzwords
- Specific and measurable when possible
- Must convey value proposition clearly

**Good Examples:**
- "AI-powered diagnostic tool helping rural clinics reduce misdiagnosis rates by 40% through automated triage" (110 chars)
- "Mobile platform connecting smallholder farmers to buyers, eliminating 3 intermediaries and doubling income" (108 chars)

**Bad Examples:**
- ❌ "Revolutionary platform transforming healthcare through innovation" (too vague, no specifics)
- ❌ "Using AI and ML to disrupt the market with our unique approach" (buzzwords, no substance)

---

### B2: Problem Statement (MAX 300 CHARACTERS)

**Focus:** What measurable problem exists? Who is affected? What is the current impact?

**Requirements:**
- **Solution-neutral** - NO mention of technology, product, or proposed solution
- **Specific population** identified with size estimates when possible
- **Quantifiable impact** - numbers, percentages, costs, time lost
- **Validated externally** or clearly marked as "Assumed" if not validated

**Structure:**
[Who] faces [specific problem] resulting in [measurable impact]. Currently, [describe gap/inadequacy].

**Good Example:**
"Rural primary care clinics serving 2.3M patients lack timely access to specialist expertise, resulting in 35% misdiagnosis rates for complex conditions. Current telemedicine options require 2+ weeks for consultation, causing treatment delays." (268 chars)

**Bad Examples:**
- ❌ "Patients need better healthcare technology" (not specific, solution-embedded)
- ❌ "The market lacks innovation in diagnostics" (vague, no impact quantified)

**Evidence Tracking:**
- Validated with: [# interviews / studies cited / data sources] or "ASSUMED"
- Source: [Stakeholder interviews / Published research / Industry reports / None]

---

### B3: Proposed Solution (MAX 300 CHARACTERS)

**Focus:** What is the approach? What makes it innovative? How does it address the problem?

**Requirements:**
- Describe approach/method, not detailed features
- Highlight key innovation or differentiation
- Connect clearly to problem in B2
- Avoid excessive technical jargon

**Structure:**
[Solution approach] that enables [key benefit]. The innovation lies in [what's new/different]. This addresses the problem by [mechanism].

**Good Example:**
"AI-assisted triage system analyzing patient symptoms and medical history in real-time, providing rural clinics with specialist-level diagnostic recommendations within 15 minutes. Innovation: proprietary algorithm trained on 500K diverse case studies, achieving 92% accuracy." (298 chars)

**Bad Examples:**
- ❌ "A comprehensive platform with advanced features" (vague, no specifics)
- ❌ "Uses machine learning, blockchain, and IoT to revolutionize the industry" (buzzword soup)

**Evidence Tracking:**
- Technical validation: [Prototype tested / Proof-of-concept / Concept only]
- User testing: [# users tested with / pilots conducted / none]

---

### B4: Target Market and Users (MAX 300 CHARACTERS)

**Focus:** Who are the users? Who are the buyers/clients (if different)? How large is the addressable market?

**Requirements:**
- Clearly distinguish USERS from BUYERS/CLIENTS
- Provide market size estimates (TAM/SAM or user counts)
- Specify initial target segment with size
- Be realistic and defensible with numbers

**Structure:**
Primary users: [user segment] ([size]). Buyers: [buyer segment] ([size]). Initial target: [specific segment] representing [market size]. TAM: [total addressable market]. SAM: [serviceable addressable market].

**Good Example:**
"Users: Rural clinic physicians (45K in US). Buyers: Rural health systems (1,200 networks). Initial target: Federally Qualified Health Centers in Southeast US (280 clinics, 12M patient visits/year). TAM: $2.4B. SAM: $380M." (234 chars)

**Important Notes:**
- If users = buyers, state explicitly: "Users and buyers are the same: [segment]"
- If multi-sided market, list all sides with relationships
- Always specify initial beachhead market

**Evidence Tracking:**
- Market sizing method: [Bottom-up / Top-down / Comparable markets / Assumed]
- User interviews conducted: [#] or "None"
- Buyer validation: [# discussions / LOIs / None]

---

### B5: Business Model and Revenue (MAX 300 CHARACTERS)

**Focus:** How does money flow? What's the pricing strategy? What are the unit economics?

**Requirements:**
- Specify revenue streams clearly
- Include pricing model and tiers if applicable
- Provide unit economics if known (LTV, CAC, gross margin)
- Note if pre-revenue

**Structure:**
Revenue model: [how money is made]. Pricing: [strategy/tiers]. Unit economics: LTV $[X], CAC $[Y], LTV:CAC ratio [Z:1], gross margin [%]. Current status: [MRR/ARR or "Pre-revenue"].

**Good Example:**
"SaaS subscription: $299/month per clinic (tier 1: 5 providers), $599/month (tier 2: 10+ providers). Annual contracts with 15% discount. Est. LTV: $18K, CAC: $3.5K (5:1 ratio), 75% gross margin. Current: $12K MRR, 8 paying customers." (248 chars)

**Bad Examples:**
- ❌ "Freemium model with premium features" (not specific enough)
- ❌ "Revenue through multiple channels" (vague)

**Evidence Tracking:**
- Pricing tested with: [# customers / prospects / "Not tested"]
- Revenue status: [Paying customers: # / MRR: $X / "Pre-revenue"]
- Economics validated: [Yes with data / Projected / Assumed]

---

### B6: Traction and Validation (MAX 300 CHARACTERS)

**Focus:** What evidence exists of progress? Customer validation? Technical milestones? Partnerships? Revenue?

**Requirements:**
- Quantify everything with numbers
- Distinguish between pilots, paying customers, and interviews
- Note product development stage
- Highlight key partnerships or commitments

**Structure:**
Customer validation: [# interviews, # pilot users, # paying customers]. Product: [stage: Concept/Prototype/MVP/Beta/Production]. Partnerships: [key relationships]. Revenue: [MRR/ARR or growth %]. Funding: [amount raised, stage].

**Good Example:**
"Customer validation: 45 interviews, 8 pilot clinics (6 months), 3 paying customers. Product: Beta (launched Oct 2024), 92% uptime. Partnerships: MOU with State Rural Health Assoc. Revenue: $12K MRR, 140% QoQ growth. Funding: $250K pre-seed (friends/family)." (276 chars)

**Evidence Categories:**
- **Customer Discovery**: # interviews per segment
- **User Testing**: # users tested, # iterations
- **Pilots**: # active, duration, outcomes
- **Paying Customers**: # customers, MRR/ARR, retention %
- **Partnerships**: Names, commitment level (MOU/LOI/Contract)
- **Technical**: Development stage, performance metrics
- **Funding**: Amount, stage, investors

**Red Flags to Note:**
- Zero customer validation (no interviews)
- No working prototype or MVP
- Claims without supporting numbers
- "In discussions" without documentation

---

### B7: Team and Resources (MAX 200 CHARACTERS)

**Focus:** Who is building this? What relevant experience? What are the gaps? What resources are secured?

**Requirements:**
- List founders with relevant experience (1 line each)
- Note full-time vs. part-time commitment
- Identify critical skill/role gaps
- Mention key advisors if exceptional

**Structure:**
Founders: [Name, Role, relevant experience]. Commitment: [full-time/part-time]. Gaps: [missing capabilities]. Advisors: [if notable]. Funding: [runway].

**Good Example:**
"Founders: Dr. Sarah Chen (CEO, 15yr rural medicine, ex-Mayo Clinic), John Park (CTO, ML PhD, ex-Google Health). Both full-time. Gap: Sales/BD hire needed. Advisor: Dr. James Wilson (AMA Digital Health Committee). Runway: 14 months." (237 chars)

**Key Assessment Points:**
- **Domain Expertise**: Years in the problem space
- **Technical Capability**: Relevant skills for solution
- **Startup Experience**: Previous ventures or exits
- **Commitment Level**: Full-time vs. part-time (critical signal)
- **Completeness**: Are all necessary roles covered?

**Evidence Tracking:**
- Team commitment: [All full-time / Mixed / All part-time]
- Key gaps identified: [List 1-3 critical missing roles]
- Advisory support: [Names and engagement level or "None"]

---

## MATURITY STAGE CLASSIFICATION

After completing B1-B7, classify the project's maturity stage:

### Maturity Stages

**IDEA STAGE**
- Concept defined but not yet prototyped
- Problem validation: 0-10 interviews
- No working technology
- Team: Part-time or forming
- Funding: Pre-seed or bootstrapped
- TRL: 1-2 (Basic principles observed)

**PROTOTYPE STAGE**
- Working proof-of-concept or prototype
- Problem validation: 10-25 interviews
- Technology concept demonstrated
- Team: At least 1 founder full-time
- Funding: Pre-seed to early seed
- TRL: 3-4 (Proof-of-concept demonstrated)

**PILOT STAGE**
- Beta product or MVP in limited deployment
- User testing: 5-30 pilot users
- Problem-solution fit being validated
- Team: Core team full-time (2-4 people)
- Funding: Seed stage
- Some revenue possible (<$5K MRR)
- TRL: 5-6 (Technology validated in relevant environment)

**EARLY COMMERCIALIZATION**
- Product in market with paying customers
- 3-50 paying customers
- Product-market fit emerging
- Team: Scaling (5-15 people)
- Funding: Seed to Series A
- Revenue: $5K-$50K MRR
- TRL: 7-8 (System prototype demonstrated in operational environment)

**GROWTH STAGE**
- Established product with proven PMF
- 50+ paying customers
- Clear growth trajectory
- Team: Scaling rapidly (15+ people)
- Funding: Series A+
- Revenue: $50K+ MRR
- TRL: 9 (Actual system proven in operational environment)

**Classification:** [Select one stage above]

**TRL (Technology Readiness Level):** [1-9]

**Justification (100 words max):**
[Explain why this stage was selected, citing specific evidence from B1-B7]

---

## SUPPLEMENTARY NOTES

Use this section to capture important context that doesn't fit in the 300-character limits above. **Each subsection: 250 characters max.**

### Market Context (MAX 250 CHARS)
- Market dynamics and trends
- Competitive landscape overview
- Timing factors ("why now?")
- Regulatory environment if relevant

### Strategic National/Regional Importance (MAX 250 CHARS)
- Alignment with national priorities or regional development goals
- Potential economic impact
- Social impact considerations
- Contribution to SDGs if applicable

### Technology Platform Potential (MAX 250 CHARS)
- Potential for technology to address multiple use cases
- Scalability beyond initial market
- Platform vs. point solution assessment
- IP or technical moat considerations

### Key Dependencies and Risks (MAX 250 CHARS)
- Critical dependencies (partnerships, regulations, etc.)
- Technical risks and mitigation strategies
- Market risks and assumptions
- Resource constraints

### Evidence Quality Assessment (MAX 250 CHARS)
- Overall strength of validation conducted
- Major evidence gaps requiring attention
- Quality of data sources cited
- Recommendations for additional validation

---

## QUALITY CHECKLIST

Before finalizing the Executive Brief, verify:

### Character Limits
- [ ] B1 one-line description ≤ 150 characters
- [ ] B2 problem statement ≤ 300 characters
- [ ] B3 solution ≤ 300 characters
- [ ] B4 market/users ≤ 300 characters
- [ ] B5 business model ≤ 300 characters
- [ ] B6 traction ≤ 300 characters
- [ ] B7 team ≤ 200 characters
- [ ] Each supplementary note ≤ 250 characters

### Content Quality
- [ ] Problem statement (B2) is solution-neutral
  - No technology or product mentions
  - Focuses on measurable impact
  - Specific population identified

- [ ] Solution (B3) clearly addresses problem in B2
  - Innovation/differentiation articulated
  - Approach explained, not just features listed

- [ ] Users and buyers (B4) are clearly distinguished
  - If same, explicitly stated
  - If different, relationship explained
  - Market sizing is defensible

- [ ] Business model (B5) is specific
  - Clear revenue streams
  - Pricing strategy defined
  - Unit economics provided or noted as "TBD"

- [ ] Traction (B6) is quantified
  - Numbers provided for all claims
  - Stages clearly distinguished (interviews vs. pilots vs. paying)
  - No vague statements like "good traction"

- [ ] Team (B7) shows relevant capability
  - Domain expertise noted
  - Technical capability assessed
  - Gaps explicitly identified

### Evidence Documentation
- [ ] Every major claim has evidence tracking
  - Source documented or marked "ASSUMED"
  - Numbers provided (# interviews, # pilots, etc.)
  - No inflated claims without basis

- [ ] Red flags are noted explicitly
  - Zero customer validation flagged
  - No working technology flagged
  - Part-time team flagged
  - Missing critical evidence noted

### Maturity Stage
- [ ] Stage classification matches evidence in B1-B7
- [ ] TRL rating is defensible
- [ ] Justification cites specific evidence

### Supplementary Notes
- [ ] All subsections respect 250-char limits
- [ ] Important context captured
- [ ] Risks and dependencies noted
- [ ] Evidence quality honestly assessed

---

## OUTPUT FORMAT

### Required Files

**1. Executive Brief (Markdown)**
- File name: `[CompanyName]_[Date]_00_ExecutiveBrief.md`
- Format: All sections B1-B7 + Maturity Stage + Supplementary Notes
- Include: Evidence tracking for each section
- Include: Red flags identified

**2. Executive Brief (DOCX)**
- File name: `[CompanyName]_[Date]_00_ExecutiveBrief.docx`
- Format: Professional formatting with:
  - Company name as header
  - Each section (B1-B7) as separate formatted section
  - Supplementary Notes in smaller font
  - Page limit: 2-3 pages maximum
  - Font: Arial or Calibri, 11pt body text
  - Section headers: Bold, 12pt
  - Character counts shown in light gray for reference

### DOCX Formatting Specifications

**Page Setup:**
- Margins: 1 inch all sides
- Orientation: Portrait
- Page limit: 2-3 pages

**Typography:**
- Body text: Arial 11pt, black
- Section headers (B1-B7): Arial 12pt, bold, dark blue
- Subsection headers: Arial 11pt, bold, black
- Evidence notes: Arial 9pt, italic, dark gray
- Character count references: Arial 8pt, light gray, right-aligned

**Layout:**
- Company name: Centered, Arial 14pt bold, top of page
- Date: Right-aligned below company name, Arial 10pt
- Each section (B1-B7): Separate paragraph with 6pt spacing after
- Supplementary Notes: Start on new page if B1-B7 exceed 2 pages
- Evidence tracking: Indented, bullet points

**Visual Elements:**
- Maturity stage: Highlight in light blue or green box
- Red flags: Highlight in light red/pink box
- Section dividers: Light gray horizontal lines between major sections

### File Naming Convention

```
[CompanyName]_[YYYY-MM-DD]_00_ExecutiveBrief.[md/docx]
```

**Examples:**
- `HealthTech_2025-01-15_00_ExecutiveBrief.md`
- `RuralClinic_2025-01-15_00_ExecutiveBrief.docx`
- `AgriTech_2025-02-03_00_ExecutiveBrief.md`

---

## COMMON ISSUES AND FIXES

### Issue 1: Character Limit Violations

**Problem:** Section exceeds character limit

**Fixes:**
1. Remove adjectives and adverbs ("very", "extremely", "innovative")
2. Use active voice instead of passive
3. Replace phrases with single words where possible
4. Abbreviate where unambiguous (US vs United States, MRR vs Monthly Recurring Revenue)
5. Combine related sentences

**Example:**
- Before (325 chars): "The healthcare providers who are working in rural areas are facing significant challenges in accessing timely specialist expertise, which results in approximately 35% of complex medical conditions being misdiagnosed, causing substantial delays in treatment."
- After (268 chars): "Rural primary care clinics serving 2.3M patients lack timely access to specialist expertise, resulting in 35% misdiagnosis rates for complex conditions. Current telemedicine options require 2+ weeks for consultation, causing treatment delays."

### Issue 2: Solution-Embedded Problem Statement

**Problem:** B2 mentions the solution, technology, or product

**Fixes:**
1. Remove all technology references (AI, platform, app, etc.)
2. Focus on the GAP or NEED, not the solution
3. Add measurable impact
4. Describe current inadequate alternatives

**Example:**
- ❌ Before: "Rural clinics need an AI-powered diagnostic platform to improve accuracy"
- ✅ After: "Rural clinics serving 2.3M patients have 35% misdiagnosis rates for complex conditions due to lack of specialist access"

### Issue 3: Vague Traction Claims

**Problem:** B6 uses qualitative statements without numbers

**Fixes:**
1. Replace "good traction" with specific numbers
2. Replace "in discussions" with "# LOIs signed" or "# meetings held"
3. Replace "strong interest" with "# interviews showing intent to purchase"
4. If no numbers available, state: "No quantitative traction data available"

**Example:**
- ❌ Before: "Strong market validation with good user feedback and partner interest"
- ✅ After: "Customer validation: 45 interviews, 8 pilot clinics (6 months), 3 paying customers. Partnerships: MOU with State Rural Health Assoc."

### Issue 4: Missing Evidence Tracking

**Problem:** Claims made without noting evidence source

**Fixes:**
1. For every claim in B2-B7, add evidence tracking
2. If no evidence, explicitly state "ASSUMED" or "No data"
3. Provide numbers: # interviews, # studies cited, # pilots
4. Note source type: Stakeholder interviews / Published research / Internal analysis

**Example:**
- ❌ Before: Just stating "Rural clinics have 35% misdiagnosis rates"
- ✅ After: Adding "Validated with: 12 clinic interviews + published AMA study (2023)"

### Issue 5: Users and Buyers Not Distinguished

**Problem:** B4 doesn't clarify who uses vs. who pays

**Fixes:**
1. Explicitly state if users = buyers: "Users and buyers are the same"
2. If different, show both: "Users: [X]. Buyers: [Y]."
3. Explain relationship if multi-sided market
4. Identify decision-making unit for B2B

**Example:**
- ❌ Before: "Target market: Healthcare industry"
- ✅ After: "Users: Rural clinic physicians (45K in US). Buyers: Rural health systems (1,200 networks)"

---

## INTEGRATION WITH VIANEO SYSTEM

### How Step 0 Feeds Other Steps

**→ Step 1 (Application Forms):**
- B1-B7 content maps to application fields
- Supplementary notes provide additional context
- Evidence tracking shows validation depth

**→ Step 2 (40-Question Diagnostic):**
- B7 informs Team dimension questions
- B3/B5 inform Technology dimension
- B5/B6 inform Commercial dimension
- Maturity stage sets baseline expectations

**→ Step 3 (Market Maturity 29Q):**
- B2 informs Legitimacy dimension (problem validation)
- B4 informs Desirability dimension (customer segments)
- B5 informs Viability dimension (business model)
- B6 evidence tracking shows validation depth across all dimensions

**→ Steps 4-8 (Deep Dives):**
- Problem statement (B2) feeds Legitimacy deep dive
- Users/market (B4) feeds Desirability analysis
- Supplementary notes on ecosystem feed Acceptability mapping
- All evidence tracking identifies gaps for validation

### Quality Gate Before Proceeding

**Before moving to Step 1 or Step 2, ensure:**
- [ ] All character limits met
- [ ] Problem statement is solution-neutral
- [ ] Evidence is tracked for all major claims
- [ ] Red flags are explicitly noted
- [ ] Maturity stage classification is defensible
- [ ] Both MD and DOCX files generated

**If major evidence gaps exist:**
- Consider requesting additional information from founders
- Note specific questions for Step 2 (40Q) or Step 4 (Legitimacy Deep Dive)
- Flag for additional validation before investment decision

---

## EXECUTION TIME ESTIMATE

**Typical Duration:** 20-30 minutes

**Breakdown:**
- Initial read of application materials: 5-8 minutes
- B1-B7 extraction and drafting: 10-15 minutes
- Character limit optimization: 3-5 minutes
- Maturity stage classification: 2-3 minutes
- Supplementary notes: 3-5 minutes
- Quality check: 2-3 minutes
- DOCX formatting: 3-5 minutes

**Total:** 20-30 minutes per project

---

## NEXT STEPS

After completing Step 0:

1. **Save both files** (MD + DOCX) with proper naming convention
2. **Review quality checklist** - ensure all items checked
3. **Identify major evidence gaps** - note for later investigation
4. **Choose next step:**
   - **Step 1** if using formal application process (360 SIS or CNEN)
   - **Step 2** for 40-question diagnostic (recommended)
   - **Step 3** for full 29-question market maturity assessment

**File Outputs:**
- `[CompanyName]_[Date]_00_ExecutiveBrief.md`
- `[CompanyName]_[Date]_00_ExecutiveBrief.docx`

---

## NOTES FOR AI ASSISTANTS

When executing this prompt:

1. **Prioritize evidence-based statements** - If information isn't in the application, mark as "ASSUMED" or "No data"
2. **Enforce character limits strictly** - These are not suggestions; they ensure clarity and force prioritization
3. **Be solution-neutral in B2** - This is critical for objective problem validation
4. **Quantify everything in B6** - No vague traction claims
5. **Identify gaps honestly** - Missing evidence is valuable information for evaluators
6. **Flag red flags explicitly** - Zero customer validation, no prototype, part-time team, etc.
7. **Generate both MD and DOCX** - MD for editing, DOCX for professional presentation

**Common AI Assistant Mistakes to Avoid:**
- ❌ Exceeding character limits "just a bit" - NO, enforce strictly
- ❌ Assuming validation exists when application doesn't specify - Mark as "ASSUMED"
- ❌ Using marketing language from pitch deck - Translate to factual, evidence-based language
- ❌ Embedding solutions in problem statement - Keep B2 solution-neutral
- ❌ Vague traction statements - Always quantify with numbers

---

**Ready to extract your first Executive Brief? Provide application materials and I'll structure them into this format with strict character limits and evidence tracking.**
