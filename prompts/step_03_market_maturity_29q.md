# STEP 3: 29-Question Market Maturity Assessment

**Time Required:** 45-60 minutes
**Output:** THREE documents - (1) Markdown Full Report, (2) Assessment Results DOCX, (3) Dimension Analysis DOCX
**Purpose:** Comprehensive market readiness evaluation across five VIANEO dimensions

---

## Overview

Step 3 evaluates business model readiness through 29 evidence-based questions organized into five dimensions:

- **Legitimacy** (15% weight, threshold ≥3.0) - Problem validation
- **Desirability** (25% weight, threshold ≥3.5) - Customer validation ⭐ HIGHEST BAR
- **Acceptability** (20% weight, threshold ≥3.0) - Ecosystem support
- **Feasibility** (20% weight, threshold ≥3.0) - Delivery capability
- **Viability** (20% weight, threshold ≥3.0) - Business sustainability

**Overall Threshold:** ≥3.2 (weighted average)

---

## Prerequisites

**Required Prior Steps:**
- Step 0: Executive Brief completed
- Step 2: 40-Question Diagnostic completed
- Customer discovery interviews conducted (5+ per segment minimum)

**Required Reference Documents:**
- `docs/VIANEO_29Question_Quick_Reference.md` - Question definitions
- `docs/VIANEO_Market_Maturity_System_Prompt.md` - Scoring methodology
- `docs/VIANEO_Evidence_Checklist.md` - Evidence requirements
- `templates/Evidence_Log_Template.md` - For evidence tracking

**When to Use Step 3:**
- After completing meaningful customer discovery (20+ interviews recommended)
- Before major investment decisions or scaling
- At quarterly checkpoints for ongoing projects
- Before Gate A decision (go/pivot/stop)

---

## Scoring Scale (1-5)

| Score | Label | Evidence Required |
|-------|-------|-------------------|
| **5** | Absolutely | Multiple external validation sources, comprehensive documentation, exceeds thresholds |
| **4** | Rather | Clear external validation, well-documented, meets thresholds with minor gaps |
| **3** | Rather not | Basic evidence, internal validation, some gaps remain |
| **2** | Not at all | Minimal evidence, work initiated but not validated |
| **1** | Don't know | No evidence available, must specify what's needed |

---

## Instructions for AI Assistant

Evaluate this startup using the 29-question framework below. Score each question 1-5, calculate weighted dimension averages, and check against thresholds. Generate three documents: Full Report (Markdown), Assessment Results (DOCX), and Dimension Analysis (DOCX). Flag any dimension below threshold as a red flag.

**IMPORTANT: Output Ordering Requirement**
When generating the assessment results table in outputs 1 and 2, display all 29 questions in **numerical order (Q1, Q2, Q3... Q29)**, NOT grouped by dimension. Include a "Dimension" column to indicate which dimension each question belongs to. Show dimension score summaries in a separate table after the main 29-question assessment.

---

## The 29 Questions by Dimension

### LEGITIMACY: Foundation and Problem Validation (2 questions, 15% weight)

**Q8.** Identified one or more markets or fields of application
- Score 5: Multiple markets clearly defined with boundaries and target segments
- Score 3: Primary market identified but boundaries unclear
- Score 1: Market not identified
- **Evidence:** Market definition documents, target segment lists

**Q13.** Validated with several people that the problem is real and important
- Score 5: 10+ validations with documented evidence
- Score 4: 5-9 validations
- Score 3: 3-4 validations
- Score 2: 1-2 validations
- Score 1: No validation beyond team belief
- **Evidence:** Interview transcripts, survey data, stakeholder confirmations

**Legitimacy Score** = (Q8 + Q13) ÷ 2

---

### DESIRABILITY: Customer Needs and Market Fit (12 questions, 25% weight)

**Q2.** Identified people with strong needs who are looking for solutions
- Score 5: Multiple segments identified with documented high-urgency needs
- Score 3: Some people identified but need strength not validated
- Score 1: No specific people identified
- **Evidence:** Customer discovery interviews, needs documentation

**Q4.** Offer and features defined to meet unmet needs today
- Score 5: Features directly mapped to validated unmet needs
- Score 3: Features defined but linkage to needs unclear
- Score 1: Features not defined
- **Evidence:** Feature-to-need mapping, product spec documents

**Q5.** Target easiest and most strategic customers to enter the market
- Score 5: Clear prioritization with documented access strategy
- Score 3: Some targeting logic but not validated
- Score 1: No targeting strategy
- **Evidence:** Customer prioritization matrix, beachhead strategy doc

**Q6.** Identified and studied solutions currently used to meet needs
- Score 5: Comprehensive competitive analysis with direct testing
- Score 3: Competitors identified but not studied in depth
- Score 1: No competitive analysis
- **Evidence:** Competitive analysis document, product testing notes

**Q7.** Verified through interviews with at least 5 people per profile that needs are expressed
- Score 5: 10+ interviews per segment
- Score 4: 5-9 interviews per segment
- Score 3: 3-4 interviews per segment
- Score 2: 1-2 interviews per segment
- Score 1: No interviews conducted
- **Evidence:** Interview transcripts (INT-###), interview log with counts

**Q9.** Defined product-market fit per customer segment
- Score 5: Clear fit for each segment, tested and validated
- Score 3: Fit defined but not tested
- Score 1: Fit not defined
- **Evidence:** Product-market fit hypothesis documents, validation data

**Q11.** Customers will easily perceive the interest of the offer compared to existing solutions
- Score 5: Tested with customers who immediately understood value
- Score 3: Value proposition exists but not tested with customers
- Score 1: No clear value proposition
- **Evidence:** Customer feedback on value prop, A/B testing results

**Q12.** Regularly test the offer with users at any stage of development
- Score 5: Continuous testing with documented feedback cycles
- Score 3: Occasional testing
- Score 1: No testing with users
- **Evidence:** Testing logs, user feedback database, iteration history

**Q21.** Offer meets key needs better than existing solutions
- Score 5: Clear superiority validated through comparative testing
- Score 3: Claimed advantages but not validated
- Score 1: No comparison to existing solutions
- **Evidence:** Comparative testing results, user preference data

**Q22.** Tested products or services with at least 3 customers per segment
- Score 5: 5+ customers per segment tested
- Score 4: 3-4 customers per segment tested
- Score 3: 2 customers per segment tested
- Score 2: 1 customer per segment tested
- Score 1: No customers tested per segment
- **Evidence:** Pilot test results, beta user feedback, usage data

**Q25.** Can accurately describe profiles, behaviors, and expectations of people who express needs
- Score 5: Detailed personas with observed behaviors and documented expectations
- Score 3: Basic demographic profiles without behavioral data
- Score 1: Cannot describe target users specifically
- **Evidence:** Persona documents, behavioral analysis, customer journey maps

**Q28.** Able to prioritize people with strong and poorly met needs
- Score 5: Clear prioritization framework with validated high-need segments
- Score 3: Some prioritization logic but not validated
- Score 1: No prioritization approach
- **Evidence:** Needs prioritization matrix (importance vs. satisfaction)

**Desirability Score** = (Q2 + Q4 + Q5 + Q6 + Q7 + Q9 + Q11 + Q12 + Q21 + Q22 + Q25 + Q28) ÷ 12

---

### ACCEPTABILITY: Ecosystem Alignment and Stakeholder Support (6 questions, 20% weight)

**Q3.** Know the market players beyond clients and competitors
- Score 5: Complete ecosystem map with all stakeholder types
- Score 3: Basic understanding of some players beyond direct customers
- Score 1: Only aware of direct customers and competitors
- **Evidence:** Ecosystem map, stakeholder analysis document

**Q10.** Regulations may help the project grow (legislation, standards)
- Score 5: Specific regulations identified that create favorable conditions
- Score 3: General awareness of regulatory environment
- Score 1: No regulatory analysis conducted
- **Evidence:** Regulatory analysis, policy documents, legal review

**Q17.** Identified players potentially unfavorable to the project
- Score 5: Potential detractors identified with mitigation strategies
- Score 3: Some potential resistance identified
- Score 1: No analysis of potential opposition
- **Evidence:** Risk assessment, stakeholder stance analysis

**Q20.** Able to represent market organization and links between groups of players
- Score 5: Detailed ecosystem map showing relationships and value flows
- Score 3: Basic understanding of market structure
- Score 1: Cannot map market organization
- **Evidence:** Ecosystem visualization, value flow diagrams

**Q23.** Identified market players who will support the project
- Score 5: Confirmed support from 3+ key players with documentation
- Score 3: Potential supporters identified but not confirmed
- Score 1: No supporters identified
- **Evidence:** Letters of support, MOUs, partnership agreements

**Q24.** Regulations may have a strong negative influence on the project (legislation, standards)
- Score 5: Comprehensive analysis shows no significant regulatory barriers
- Score 3: Some regulatory risks identified
- Score 1: No regulatory risk analysis conducted
- **Evidence:** Regulatory risk assessment, compliance analysis

**Acceptability Score** = (Q3 + Q10 + Q17 + Q20 + Q23 + Q24) ÷ 6

---

### FEASIBILITY: Technical and Operational Viability (5 questions, 20% weight)

**Q1.** Solid and tangible resources to launch and carry out the project (team, network, skills, patents, finances, equipment)
- Score 5: All necessary resources secured and available
- Score 3: Some resources available, significant gaps exist
- Score 1: Resources unidentified or unavailable
- **Evidence:** Resource inventory, team roster, funding documents, equipment list

**Q15.** Plan to use technical partners to focus on core project
- Score 5: Strategic partners identified and committed
- Score 3: Partnership strategy defined but partners not secured
- Score 1: No partnership strategy
- **Evidence:** Partnership agreements, MOUs, partner capability assessments

**Q16.** Fully committed team formed
- Score 5: Full team dedicated 100% with long-term commitment
- Score 3: Team formed but commitment levels vary
- Score 1: No team or frequent turnover
- **Evidence:** Employment contracts, commitment letters, team roster

**Q18.** Differentiating assets exist (expertise, patent, prototype, partnerships)
- Score 5: Multiple strong differentiators with IP protection
- Score 3: Some unique capabilities but not protected
- Score 1: No clear differentiating assets
- **Evidence:** Patent filings, prototype demonstrations, expertise documentation

**Q26.** Have the necessary means to develop the offer
- Score 5: All development resources secured
- Score 3: Basic development capability but resource constraints
- Score 1: Cannot develop offer with current means
- **Evidence:** Development plan, resource allocation, capability assessment

**Feasibility Score** = (Q1 + Q15 + Q16 + Q18 + Q26) ÷ 5

---

### VIABILITY: Business Model Sustainability (4 questions, 20% weight)

**Q14.** Defined revenue streams
- Score 5: Multiple streams defined, tested, and documented
- Score 3: Stream defined but not tested
- Score 1: Revenue model not defined
- **Evidence:** Business model canvas, revenue stream documentation

**Q19.** Tested the revenue model with at least 3 potential customers
- Score 5: Tested with 10+ customers
- Score 4: Tested with 5-9 customers
- Score 3: Tested with 3-4 customers
- Score 2: Tested with 1-2 customers
- Score 1: Not tested with any customers
- **Evidence:** Pricing test results, customer feedback, willingness-to-pay data

**Q27.** Able to express value proposition in one sentence per customer type
- Score 5: Clear, tested value propositions for each segment
- Score 3: Value propositions exist but not validated
- Score 1: Cannot articulate value proposition
- **Evidence:** Value proposition documents, customer validation interviews

**Q29.** Have the means to reach customers (sales force, marketing budget)
- Score 5: Established channels with proven customer access
- Score 3: Some customer reach capability but limited
- Score 1: No means to reach customers
- **Evidence:** GTM strategy, sales plan, marketing budget, channel partnerships

**Viability Score** = (Q14 + Q19 + Q27 + Q29) ÷ 4

---

## Calculation of Overall Weighted Score

**Formula:**
Overall Score = (Legitimacy × 0.15) + (Desirability × 0.25) + (Acceptability × 0.20) + (Feasibility × 0.20) + (Viability × 0.20)

**Example:**
- Legitimacy: 4.0 × 0.15 = 0.60
- Desirability: 3.2 × 0.25 = 0.80
- Acceptability: 3.5 × 0.20 = 0.70
- Feasibility: 3.8 × 0.20 = 0.76
- Viability: 2.5 × 0.20 = 0.50

**Total:** 0.60 + 0.80 + 0.70 + 0.76 + 0.50 = **3.36** (rounds to **3.4**)

---

## Minimum Thresholds

| Dimension | Minimum Threshold | Why This Matters |
|-----------|-------------------|------------------|
| Legitimacy | ≥ 3.0 | Must have validated problem and market |
| **Desirability** | **≥ 3.5** | **HIGHEST BAR - customer validation is critical** |
| Acceptability | ≥ 3.0 | Need ecosystem support to scale |
| Feasibility | ≥ 3.0 | Must have capability to execute |
| Viability | ≥ 3.0 | Business model must be sound |
| **Overall** | **≥ 3.2** | **Weighted average for proceed decision** |

**Threshold Interpretation:**
- **PASS (≥ threshold):** ✅ Dimension meets minimum requirements
- **FAIL (< threshold):** ❌ Critical gap requiring immediate attention

---

## Red Flag Questions

**These questions, if scored 1 or 2, indicate CRITICAL gaps:**

- **Q7** (No user interviews): Cannot validate desirability
- **Q13** (Problem not validated): Foundation questionable
- **Q19** (Revenue not tested): Business model unproven
- **Q22** (Not tested per segment): Product-market fit unvalidated

**Any Score 1 = Immediate action required**

---

## Three Required Outputs

### Output 1: Markdown Full Report
**Filename:** `[ProjectName]_MarketMaturity_Assessment_YYYYMMDD.md`

**Required Sections:**
1. Metadata block (assessment date, project lead, TRL, assessor)
2. Executive summary (overall score, category, key finding)
3. Assessment results: 29-question table **in numerical order (Q1-Q29)**, with dimension indicated for each question
4. Dimension analysis (5 sections, one per dimension)
5. Overall weighted score calculation
6. Comparison to minimum thresholds
7. Red flag analysis
8. Top 3 strengths
9. Top 3 critical gaps
10. Action plan (prioritized next steps)
11. Risk assessment
12. Commercial viability benchmarks
13. Historical context (similar projects)
14. Industry benchmarks
15. Success probability assessment
16. Questions for founders (10 questions)
17. Methodology and limitations
18. Conclusion with final recommendation

**Template:** `templates/Step3_MarketMaturity_Markdown_Template.md`

---

### Output 2: Assessment Results Table (DOCX)
**Filename:** `[ProjectName]_Assessment_Results_YYYYMMDD.docx`

**Required Sections:**
1. Document title and project subtitle
2. Metadata block
3. Executive summary
4. Key finding
5. Assessment results: 29-question table **in numerical order (Q1-Q29)**
   - Columns: Question # | Dimension | Question | Score | Justification | Evidence Reference
   - All borders, header row shaded gray
   - Question numbers and scores in bold
   - Questions listed 1-29 in numerical sequence (not grouped by dimension)

**Formatting:**
- Font: Calibri 11pt body, 12-14pt headings
- Margins: 1" all sides
- Professional appearance for committees/boards

**Template:** `templates/Step3_Assessment_Results_Template.md` (markdown version for reference)

---

### Output 3: Dimension Analysis (DOCX)
**Filename:** `[ProjectName]_Dimension_Analysis_YYYYMMDD.docx`

**Required Sections:**
1. Same header/metadata as Output 2
2. Five dimension analysis sections:
   - Dimension name and score
   - Question list
   - Assessment paragraph
   - Strengths (bullets)
   - Gaps/Critical Gaps (bullets)
   - Required Actions (numbered list)
3. Overall weighted score calculation
4. Comparison to minimum thresholds (table)
5. Red flag analysis
6. Top 3 strengths (detailed with related questions)
7. Top 3 critical gaps (detailed with actions)
8. Action plan (Priority 1, 2, 3 with objectives and success metrics)

**Formatting:** Same professional standards as Output 2

**Template:** `templates/Step3_Dimension_Analysis_Template.md` (markdown version for reference)

---

## Execution Process

### Step 1: Preparation (15 minutes)
- [ ] Review Executive Brief (Step 0)
- [ ] Review 40Q Diagnostic Results (Step 2)
- [ ] Review Evidence Log for available Evidence IDs
- [ ] Gather all project documentation
- [ ] Review 29-Question Quick Reference
- [ ] Review Evidence Checklist

### Step 2: Scoring (30 minutes)
- [ ] Score each of 29 questions (1-5)
- [ ] Write one-sentence justification per question
- [ ] Cite specific evidence or state what's needed
- [ ] Link to Evidence IDs when available (E###)
- [ ] Flag questions scored 1 or 2 as red flags

### Step 3: Calculations (10 minutes)
- [ ] Calculate 5 dimension scores (simple averages)
- [ ] Calculate overall weighted score
- [ ] Compare each dimension to threshold
- [ ] Determine pass/fail status

### Step 4: Analysis (45 minutes)
- [ ] Identify top 3 strengths
- [ ] Identify top 3 critical gaps
- [ ] Write dimension analysis sections
- [ ] Develop priority action plan
- [ ] Create risk assessment
- [ ] Draft questions for founders

### Step 5: Document Creation (60 minutes)
- [ ] Create Markdown full report (all sections)
- [ ] Create Assessment Results DOCX (table + summary)
- [ ] Create Dimension Analysis DOCX (detailed analysis)
- [ ] Ensure all three files have identical scores
- [ ] Apply proper formatting to DOCX files

### Step 6: Quality Review (20 minutes)
- [ ] Verify all 29 questions scored consistently
- [ ] Check calculations (dimension averages, weighted score)
- [ ] Confirm threshold comparisons accurate
- [ ] Review formatting (headings, tables, bold text)
- [ ] Validate evidence citations
- [ ] Check for typos and errors

**Total Time:** 3-3.5 hours for complete Step 3 assessment

---

## Integration with Other Steps

### From Step 0 (Executive Brief):
- B2 (Problem Statement) → Informs Q8, Q13 (Legitimacy)
- B4 (Target Market) → Informs Q2, Q5, Q25 (Desirability)
- B5 (Business Model) → Informs Q14, Q27 (Viability)
- B6 (Traction) → Informs Q7, Q19, Q22 (validation counts)
- B7 (Team) → Informs Q1, Q16 (Feasibility)

### From Step 2 (40Q Diagnostic):
- Team dimension → Informs Q1, Q16 (Feasibility)
- Technology dimension → Informs Q18, Q26 (Feasibility)
- Management dimension → Informs Q1, Q15 (Feasibility)
- Commercial dimension → Informs Q2, Q4, Q6, Q7, Q19 (Desirability/Viability)

### To Evidence Log:
- All scores ≥3 should cite Evidence IDs (E###)
- All scores 1 should specify what evidence is needed
- Interview counts (Q7, Q19, Q22) should reference INT-### series

### To Hypotheses Log:
- Low scores identify hypotheses needing validation
- High scores confirm validated hypotheses
- Critical gaps become new hypotheses with validation plans

### To Gate A Decision:
- Overall score ≥3.2 → Supports GO decision
- Critical dimension failures → Trigger PIVOT consideration
- Multiple Score 1 questions → May trigger STOP

---

## Scoring Best Practices

### DO:
- ✅ Score based on documented evidence only
- ✅ Be honest - Score 1 when evidence is truly absent
- ✅ Cite specific documents, data, or Evidence IDs
- ✅ When scoring 1, specify exactly what evidence is needed
- ✅ Use Evidence Log to track all sources
- ✅ Count interviews accurately (Q7, Q19, Q22)

### DON'T:
- ❌ Score based on potential or plans
- ❌ Accept claims without evidence
- ❌ Use vague language ("some work done")
- ❌ Inflate scores to look better
- ❌ Confuse activity with validation
- ❌ Score what you wish existed vs. what actually exists

---

## Quality Checklist

**Before Finalizing:**

**Content:**
- [ ] All 29 questions scored (1-5)
- [ ] Each score has one-sentence justification
- [ ] Evidence references are specific or state what's needed
- [ ] Dimension scores calculated correctly
- [ ] Overall weighted score uses correct formula
- [ ] Threshold comparisons accurate
- [ ] All Score 1 questions explained in Red Flag section
- [ ] Top 3 strengths/gaps identified
- [ ] Action plan is specific and measurable

**Formatting:**
- [ ] Markdown file follows template structure
- [ ] DOCX files use professional formatting
- [ ] Tables have borders and shaded headers
- [ ] Headings hierarchy consistent
- [ ] Bold text applied to Q numbers, scores, labels
- [ ] Consistent spacing throughout

**Integration:**
- [ ] Scores align with Step 0 and Step 2
- [ ] Evidence IDs cited from Evidence Log
- [ ] Hypotheses Log updated with findings
- [ ] Feeds into Gate A Decision Brief

---

## Output File Naming

**Standard Format:**
- Markdown: `[ProjectName]_MarketMaturity_Assessment_YYYYMMDD.md`
- DOCX 1: `[ProjectName]_Assessment_Results_YYYYMMDD.docx`
- DOCX 2: `[ProjectName]_Dimension_Analysis_YYYYMMDD.docx`

**Examples:**
- `RuralHealthAI_MarketMaturity_Assessment_20250115.md`
- `RuralHealthAI_Assessment_Results_20250115.docx`
- `RuralHealthAI_Dimension_Analysis_20250115.docx`

---

## Next Steps After Step 3

### If Overall Score ≥ 3.2 and All Dimensions Pass Thresholds:
1. Proceed to Step 4 (Legitimacy Deep Dive) - Optional
2. Proceed to Step 5 (Desirability Analysis) - Optional
3. Prepare for Gate A Decision Brief
4. Consider pilot or MVP launch

### If Overall Score < 3.2 or Any Dimension Fails Threshold:
1. Review critical gaps (Score 1-2 questions)
2. Create validation plan for failing dimensions
3. Execute validation work (interviews, testing, partnerships)
4. Reassess after 4-8 weeks
5. Do NOT proceed to MVP/pilot without addressing gaps

### If Desirability < 3.5 (CRITICAL):
1. STOP any product development
2. Conduct intensive customer discovery (20+ interviews per segment)
3. Test value proposition with real users
4. Validate product-market fit before building
5. Reassess Step 3 only after customer validation complete

---

**Prompt Version:** 1.0
**Last Updated:** 2025-01-15
**Compatible with:** VIANEO 13-Step Evaluation System
**Required References:** 29Q Quick Reference, Market Maturity System Prompt, Evidence Checklist
