# FORMAT SPECIFICATION: Step 2 - 40-Question Diagnostic Assessment

**Version:** 1.0
**Last Updated:** 2025-01-15
**Document Type:** Format Specification & Validation Guide
**Purpose:** Comprehensive format requirements for Step 2 Diagnostic Assessment outputs

---

## OVERVIEW

The Step 2 40-Question Diagnostic Assessment is a comprehensive evaluation framework that scores ventures across four critical dimensions: Team, Technology, Management, and Commercial. This format specification defines the exact structure, scoring methodology, validation requirements, and output standards for conducting and documenting Step 2 assessments.

**Key Characteristics:**
- **40 Questions Total:** Distributed across 4 dimensions with specific question counts per dimension
- **1-5 Scoring Scale:** Numeric scores with evidence requirements and special response codes
- **Two-Document Output:** Comprehensive Results + Executive Summary
- **Red Flags System:** Automated identification of critical gaps requiring attention
- **Stage-Aware Assessment:** Scoring considers venture maturity stage from Step 0

**Assessment Time:** 30-45 minutes for experienced evaluators
**Output Length:** Results document 8-12 pages, Summary document 3-5 pages

---

## 1. DOCUMENT HEADER REQUIREMENTS

### 1.1 Required Metadata Fields

Every Step 2 assessment document MUST include the following header fields:

```markdown
# 40-Question Diagnostic Assessment: [Company Name]

**Evaluation Date:** [YYYY-MM-DD]
**Evaluator:** [Name/Organization]
**Project Stage:** [From Step 0 Maturity Stage Classification]
**Source:** Executive Brief dated [Date]
```

### 1.2 Field Specifications

| Field | Format | Requirements | Example |
|-------|--------|--------------|---------|
| **Company Name** | Plain text | Legal or operating name, consistent across all documents | "HealthTech Innovations Inc." |
| **Evaluation Date** | YYYY-MM-DD | ISO 8601 format, date assessment completed | "2025-01-15" |
| **Evaluator** | Name/Organization | Person or team conducting assessment | "Sarah Chen / VIANEO Partners" |
| **Project Stage** | Stage classification | Must match Step 0 output exactly | "Prototype Stage - Technical Validation" |
| **Source** | Document reference | Reference to source Executive Brief | "Executive Brief dated 2025-01-10" |

### 1.3 Validation Rules

- **Company Name:** Must be consistent with Step 1 Executive Brief filename and content
- **Evaluation Date:** Cannot be earlier than source document date
- **Project Stage:** Must be one of: Idea / Prototype / Pilot / Early Commercialization / Growth
- **Source:** Must reference an actual Executive Brief document with matching date

---

## 2. ASSESSMENT RESULTS TABLE STRUCTURE

### 2.1 40-Question Breakdown by Dimension

The assessment comprises exactly 40 questions distributed across four dimensions:

| Dimension | Question Range | Count | Focus Area |
|-----------|---------------|-------|------------|
| **Team** | T1-T9 | 9 | Founder/team capabilities, experience, commitment |
| **Technology** | Tech1-Tech11 | 11 | Technical innovation, feasibility, development status |
| **Management** | M1-M12 | 12 | Strategic planning, operations, governance, execution |
| **Commercial** | C1-C8 | 8 | Market validation, business model, revenue, positioning |

**Total:** 40 questions

### 2.2 Team Dimension Questions (T1-T9)

Each question must be scored individually with evidence:

| Question ID | Question Label | Assessment Focus |
|------------|----------------|------------------|
| **T1** | Technical Completeness | Does the team have all necessary technical skills? |
| **T2** | Startup Experience | Do team members have startup/entrepreneurial experience? |
| **T3** | Domain Expertise | Do team members have deep domain knowledge? |
| **T4** | Talent Attraction | Can the team attract high-quality talent? |
| **T5** | Leadership/Vision | Is there clear leadership with compelling vision? |
| **T6** | Execution Capability | Does the team have track record of executing? |
| **T7** | Resilience/Adaptability | Can the team adapt to setbacks and changes? |
| **T8** | Network/Advisory | Does the team have strong networks and advisors? |
| **T9** | Commitment Level | Are team members fully committed (time, equity)? |

**Format per question:**
```markdown
| **T1: Technical Completeness** | [1-5 / INSUFFICIENT DATA / N/A] | [Evidence citation or gap description] |
```

### 2.3 Technology Dimension Questions (Tech1-Tech11)

| Question ID | Question Label | Assessment Focus |
|------------|----------------|------------------|
| **Tech1** | Innovation Level | How innovative/differentiated is the technology? |
| **Tech2** | Feasibility Validated | Is technical feasibility proven? |
| **Tech3** | Development Stage | What stage is the technology development at? |
| **Tech4** | IP Position | What IP protection exists or is planned? |
| **Tech5** | Scalability | Can the technology scale technically? |
| **Tech6** | Risk Mitigation | Are technical risks identified and mitigated? |
| **Tech7** | Roadmap Clarity | Is there a clear technical development roadmap? |
| **Tech8** | Partnerships/Resources | Are necessary technical partnerships/resources secured? |
| **Tech9** | Security/Privacy | Are security and privacy adequately addressed? |
| **Tech10** | Tech Stack | Is the technology stack appropriate and modern? |
| **Tech11** | QA/Testing | Are QA and testing processes established? |

### 2.4 Management Dimension Questions (M1-M12)

| Question ID | Question Label | Assessment Focus |
|------------|----------------|------------------|
| **M1** | Strategy Clarity | Is the overall strategy clear and coherent? |
| **M2** | Market Understanding | Do they understand their market deeply? |
| **M3** | Financial Planning | Is financial planning realistic and detailed? |
| **M4** | Risk Management | Are risks identified and actively managed? |
| **M5** | Operational Planning | Are operations planned and structured? |
| **M6** | Milestone Tracking | Are milestones defined and tracked? |
| **M7** | Resource Allocation | Are resources allocated effectively? |
| **M8** | Decision-Making | Is decision-making process effective? |
| **M9** | Stakeholder Mgmt | Are stakeholders managed effectively? |
| **M10** | Culture/Values | Are culture and values defined and lived? |
| **M11** | Learning/Iteration | Does the team learn and iterate based on feedback? |
| **M12** | Governance | Are governance structures appropriate for stage? |

### 2.5 Commercial Dimension Questions (C1-C8)

| Question ID | Question Label | Assessment Focus |
|------------|----------------|------------------|
| **C1** | Customer Validation | Is there validated customer interest/demand? |
| **C2** | Market Size | Is the addressable market size quantified and attractive? |
| **C3** | Business Model Clarity | Is the business model clear and viable? |
| **C4** | Revenue Validation | Is the revenue model tested/validated? |
| **C5** | Sales/Marketing Strategy | Is there a clear go-to-market strategy? |
| **C6** | Partnership Development | Are strategic partnerships developed or planned? |
| **C7** | Competitive Positioning | Is competitive positioning clear and defensible? |
| **C8** | Growth Strategy | Is there a clear growth/scaling strategy? |

### 2.6 Table Format Requirements

Each dimension must include:

1. **Question Table** - All questions with scores and evidence
2. **Dimension Average** - Calculated average score
3. **Dimension Analysis** - Key strengths and critical gaps
4. **Red Flags Checklist** - Dimension-specific red flags

**Example Format:**
```markdown
### TEAM DIMENSION (T1-T9)

| Question | Score | Evidence/Gap |
|----------|-------|--------------|
| **T1: Technical Completeness** | [1-5 / INSUFFICIENT DATA / N/A] | [Evidence citation or gap description] |
| **T2: Startup Experience** | [1-5 / INSUFFICIENT DATA / N/A] | [Evidence citation or gap description] |
[... continues for all 9 questions]

**Team Average:** [___.___ / 5.0]
```

---

## 3. SCORING SCALE SPECIFICATION

### 3.1 Primary 1-5 Scoring Scale

All 40 questions use a standardized 1-5 scale with specific evidence requirements:

| Score | Label | Definition | Evidence Required |
|-------|-------|------------|-------------------|
| **5** | Exceptional | Significantly exceeds expectations for stage; best-in-class | Multiple concrete examples, verified achievements, quantifiable evidence |
| **4** | Strong | Exceeds expectations for stage; clear strength | Documented evidence, specific examples, demonstrable capability |
| **3** | Adequate | Meets expectations for stage; acceptable | Credible claims, reasonable evidence, meets basic requirements |
| **2** | Weak | Below expectations for stage; concerning gap | Limited evidence, vague claims, identifiable deficiency |
| **1** | Critical Gap | Significantly below expectations; major concern | No evidence, major deficiency, critical missing element |

### 3.2 Special Response Codes

In addition to numeric scores, evaluators may use special codes:

| Code | Usage | When to Use | Impact on Average |
|------|-------|-------------|-------------------|
| **INSUFFICIENT DATA** | Not enough information to score | Source document lacks necessary information to evaluate | Excluded from average calculation |
| **N/A** | Not applicable to this venture | Question doesn't apply to this specific business model/stage | Excluded from average calculation |
| **YES/NO** | Binary response needed | For questions where only presence/absence matters | Convert to 5 (YES) or 1 (NO) for average |
| **CONTEXTUAL NOTE** | Additional context required | Score given but requires significant context/caveat | Include note in Evidence/Gap column |

### 3.3 Evidence Requirements by Score Level

**For Scores 4-5 (Strong/Exceptional):**
- Specific examples with details
- Quantifiable metrics or achievements
- Third-party validation where available
- Direct quotes from source material
- Timeline of accomplishments

**For Scores 2-3 (Adequate/Weak):**
- Clear explanation of what exists vs. what's missing
- Specific gaps identified
- Comparison to stage expectations
- References to source material
- Context for the score

**For Score 1 (Critical Gap):**
- Explicit statement of what's completely missing
- Why this is critical for venture success
- Impact assessment
- Urgency level
- Recommendation for addressing

### 3.4 Stage-Adjusted Scoring Guidelines

Scores must be contextualized by venture stage. A score of 3 has different meanings:

**Idea Stage (Pre-Product):**
- Team 3.0 = Adequate: Basic team in place, some relevant experience
- Technology 3.0 = Strong: Concept validated, feasibility study complete
- Management 3.0 = Strong: Clear strategy, basic planning in place
- Commercial 3.0 = Strong: Problem validated, target market identified

**Prototype Stage:**
- Team 3.0 = Adequate: Team complete, relevant experience demonstrated
- Technology 3.0 = Adequate: Working prototype, technical validation begun
- Management 3.0 = Adequate: Roadmap exists, milestones defined
- Commercial 3.0 = Adequate: Early customer feedback, business model hypothesis tested

**Pilot Stage:**
- Team 3.0 = Concern: Should have stronger team by this stage
- Technology 3.0 = Adequate: Pilot-ready product, scaling considerations identified
- Management 3.0 = Adequate: Operational plans in place, tracking mechanisms exist
- Commercial 3.0 = Adequate: Pilot customers committed, revenue model being tested

**Early Commercialization:**
- Team 3.0 = Concern: Team gaps problematic at this stage
- Technology 3.0 = Concern: Product should be more mature
- Management 3.0 = Adequate: Basic operations running, improvement needed
- Commercial 3.0 = Adequate: Revenue coming in, growth plan exists

**Growth Stage:**
- Team 3.0 = Critical: Significant team gaps at growth stage
- Technology 3.0 = Concern: Technology should be proven and scaling
- Management 3.0 = Concern: Management sophistication should be higher
- Commercial 3.0 = Concern: Commercial execution should be stronger

---

## 4. DIMENSION AVERAGES CALCULATION

### 4.1 Calculation Methodology

**Formula:**
```
Dimension Average = (Sum of all numeric scores in dimension) / (Number of questions with numeric scores)
```

**Key Rules:**
1. Only numeric scores (1-5) are included in calculation
2. INSUFFICIENT DATA scores are excluded (reduce denominator)
3. N/A scores are excluded (reduce denominator)
4. YES converts to 5, NO converts to 1 for calculation
5. Round to two decimal places (e.g., 3.67, not 3.7 or 3.667)

### 4.2 Calculation Examples

**Example 1: Complete Data**
```
Team Dimension (9 questions):
T1=4, T2=3, T3=5, T4=3, T5=4, T6=3, T7=4, T8=2, T9=5

Average = (4+3+5+3+4+3+4+2+5) / 9 = 33 / 9 = 3.67
```

**Example 2: With INSUFFICIENT DATA**
```
Team Dimension (9 questions):
T1=4, T2=3, T3=5, T4=INSUFFICIENT DATA, T5=4, T6=3, T7=4, T8=2, T9=5

Average = (4+3+5+4+3+4+2+5) / 8 = 30 / 8 = 3.75
(Note: Denominator reduced to 8 because T4 excluded)
```

**Example 3: With N/A and INSUFFICIENT DATA**
```
Technology Dimension (11 questions):
Tech1=4, Tech2=5, Tech3=4, Tech4=N/A, Tech5=4, Tech6=3,
Tech7=INSUFFICIENT DATA, Tech8=3, Tech9=5, Tech10=4, Tech11=3

Average = (4+5+4+4+3+3+5+4+3) / 9 = 35 / 9 = 3.89
(Note: Denominator reduced to 9 because Tech4 and Tech7 excluded)
```

### 4.3 Minimum Scoring Requirements

For a dimension average to be valid and meaningful:

- **Minimum scored questions:** At least 50% of dimension questions must have numeric scores
- **Team Dimension:** Minimum 5 of 9 questions scored
- **Technology Dimension:** Minimum 6 of 11 questions scored
- **Management Dimension:** Minimum 6 of 12 questions scored
- **Commercial Dimension:** Minimum 4 of 8 questions scored

**If minimum not met:** Note "INSUFFICIENT DATA FOR VALID AVERAGE" instead of calculating

### 4.4 Status Classification

Each dimension average is classified into a status category:

| Status | Score Range | Meaning | Color Code |
|--------|-------------|---------|------------|
| **STRONG** | ≥ 4.0 | Exceeds expectations for stage | Green |
| **ADEQUATE** | 3.0 - 3.9 | Meets expectations for stage | Yellow |
| **CONCERN** | 2.0 - 2.9 | Below expectations, gaps need addressing | Orange |
| **CRITICAL** | < 2.0 | Major deficiencies, immediate action required | Red |

**Format:**
```markdown
| **Team** (T1-T9) | 3.67 / 5.0 | ADEQUATE | [7/9] | Limited startup experience, weak advisory network |
```

### 4.5 Dimensional Scores Table Format

**Required Format:**
```markdown
## DIMENSIONAL SCORES

| Dimension | Score | Status | Questions Scored | Key Gaps |
|-----------|-------|--------|------------------|----------|
| **Team** (T1-T9) | 3.67 / 5.0 | ADEQUATE | [7/9] | [List 1-2 main gaps] |
| **Technology** (Tech1-Tech11) | 4.11 / 5.0 | STRONG | [9/11] | [List 1-2 main gaps] |
| **Management** (M1-M12) | 2.83 / 5.0 | CONCERN | [12/12] | [List 1-2 main gaps] |
| **Commercial** (C1-C8) | 3.25 / 5.0 | ADEQUATE | [8/8] | [List 1-2 main gaps] |
```

---

## 5. SCORE SUMMARY FORMAT

### 5.1 Executive Summary Structure

The Score Summary (Document 2) must follow this exact structure:

**Required Sections (in order):**
1. Document Header
2. Executive Summary (3 paragraphs)
3. Dimensional Scores Table
4. Top 5 Strengths
5. Top 5 Gaps/Concerns
6. Red Flags
7. Strategic Recommendations
8. Stage Appropriateness Assessment
9. Recommendation
10. Next Steps
11. Key Insights for Discussion
12. Comparison to Portfolio/Cohort (optional)

### 5.2 Executive Summary Paragraph Requirements

**Paragraph 1: Overall Assessment (2-3 sentences)**
- Overall readiness across all four dimensions
- Strongest and weakest dimensions noted
- Overall impression relative to stated stage

**Example:**
"TechHealth Solutions demonstrates adequate overall readiness with notable strength in Technology (4.2/5.0) but significant concerns in Management (2.7/5.0). The team shows strong technical capabilities but lacks operational and strategic planning maturity. For a Prototype Stage venture, the profile is mixed with strong technical foundations undermined by execution concerns."

**Paragraph 2: Key Strengths (2-3 sentences)**
- 1-2 strongest dimensions or capabilities
- What gives competitive advantage
- Foundation for success

**Example:**
"The venture's greatest strength lies in its technical innovation and validated feasibility, with exceptional domain expertise (T3=5) and proven technical capabilities (Tech2=5, Tech3=4). The founding team brings deep healthcare industry knowledge and has successfully built a working prototype that addresses a validated pain point. This technical strength provides a solid foundation for commercialization if management capabilities can be developed."

**Paragraph 3: Critical Gaps and Recommendation (2-3 sentences)**
- 1-2 most critical gaps or risks
- Recommended next step
- Conditions or caveats if applicable

**Example:**
"The most critical gaps are weak financial planning (M3=2) and unclear go-to-market strategy (C5=2), both concerning for a venture seeking investment. Despite these gaps, the technical strengths warrant conditional progression to Step 3 Market Maturity Assessment, contingent on the team developing a comprehensive financial model and articulating a clear sales strategy within 30 days."

### 5.3 Top 5 Strengths Format

List the 5 highest-scoring individual questions (scores 4-5):

```markdown
## TOP 5 STRENGTHS

1. **T3: Domain Expertise** (Score 5): Founders have 15+ years combined healthcare experience, including clinical, regulatory, and operational expertise - critical for navigating complex healthcare market.

2. **Tech2: Feasibility Validated** (Score 5): Successful pilot study with 200 patients demonstrated technical feasibility and 40% improvement in target outcomes, validated by independent clinical research team.

3. **T5: Leadership/Vision** (Score 4): CEO presents compelling vision for transforming chronic disease management, with clear articulation of problem, solution, and impact - demonstrated ability to inspire team and early advisors.

4. **Tech3: Development Stage** (Score 4): Working prototype deployed in pilot environment, serving real users, with positive feedback on usability and functionality - de-risks technical execution.

5. **C1: Customer Validation** (Score 4): 12 healthcare providers have expressed strong interest, 3 have signed letters of intent for pilot participation, validating demand and willingness to adopt.
```

**Requirements:**
- Must list exactly 5 strengths (or state if fewer than 5 scores of 4+ exist)
- Question ID and label required
- Numeric score required
- Evidence-based description of WHY this is a strength
- Context of why it matters for this specific venture

### 5.4 Top 5 Gaps/Concerns Format

List the 5 lowest-scoring individual questions (scores 1-2, or scores of 3 if concerning for stage):

```markdown
## TOP 5 GAPS/CONCERNS

1. **M3: Financial Planning** (Score 2): No detailed financial model exists beyond rough revenue projections - concerning for investment readiness; founders need comprehensive 3-year financial plan with unit economics.

2. **C5: Sales/Marketing Strategy** (Score 2): Go-to-market strategy remains vague with no clear customer acquisition plan, sales process, or marketing approach defined - critical gap for commercialization.

3. **T8: Network/Advisory** (Score 2): Limited advisor network and no formal advisory board despite complex healthcare market requiring extensive industry connections and regulatory guidance.

4. **M6: Milestone Tracking** (Score 2): No formal milestone tracking system; team operates reactively rather than against defined goals - impacts ability to measure progress and make data-driven decisions.

5. **C4: Revenue Validation** (Score 2): Revenue model hypothesis not yet tested with actual customers willing to pay; pricing strategy based on assumptions rather than market validation - significant commercial risk.
```

### 5.5 Red Flags Section Format

```markdown
## RED FLAGS

**Total Red Flags:** 3

**Critical Red Flags:**
- Management: No clear strategy (M1=2) - venture lacks coherent strategic direction
- Management: Poor financial planning (M3=2) - significant gap for investment readiness
- Commercial: No revenue model validation (C4=2) - business model not proven with real customers

**Risk Level:** MODERATE

**Risk Assessment:**
Three red flags concentrated in Management and Commercial dimensions represent addressable but concerning gaps. Technical strengths are solid, but execution and commercialization capabilities need significant development before investment readiness. Risk is moderate because gaps are in areas that can be improved with focused effort over 1-3 months.
```

**Risk Level Definitions:**
- **LOW:** No red flags; gaps are typical for current stage
- **MODERATE:** 1-2 red flags or several Score 2 items; addressable but concerning
- **HIGH:** 3-4 red flags across dimensions; significant concerns about viability
- **CRITICAL:** 5+ red flags or multiple Score 1 items; fundamental viability questions

---

## 6. RED FLAGS SECTION SPECIFICATION

### 6.1 Red Flag Definition

A "Red Flag" is a critical gap or deficiency that raises significant concerns about venture viability or investment readiness. Red flags are identified through:

1. **Any score of 1** in any dimension
2. **Critical combination rules** based on dimension-specific criteria
3. **Stage-inappropriate gaps** (e.g., no customer validation at Pilot stage)

### 6.2 Team Dimension Red Flags

```markdown
**Team Dimension Red Flags:**
- [ ] Any score of 1 in Team dimension
- [ ] Three or more scores of 2
- [ ] No full-time commitment (T9 ≤ 2)
- [ ] No domain expertise (T3 ≤ 2)
- [ ] No technical capability (T1 ≤ 2)
```

**Rationale:**
- **No full-time commitment:** Part-time founders rarely succeed; commitment is fundamental
- **No domain expertise:** Deep domain knowledge critical for navigating market
- **No technical capability:** Technical ventures require technical team members
- **Multiple weak scores:** Pattern of team weakness across areas is concerning

### 6.3 Technology Dimension Red Flags

```markdown
**Technology Dimension Red Flags:**
- [ ] Any score of 1 in Technology dimension
- [ ] Technical feasibility unproven (Tech2 = 1)
- [ ] No working prototype (Tech3 ≤ 2)
- [ ] Cannot scale (Tech5 ≤ 2)
- [ ] Security/privacy not addressed in regulated sector (Tech9 ≤ 2)
```

**Rationale:**
- **Feasibility unproven:** Technical risk too high if basic feasibility not validated
- **No prototype:** Beyond Idea stage, ventures should have working prototype
- **Cannot scale:** Technical solution that cannot scale is fundamentally limited
- **Security/privacy:** Critical for regulated sectors like healthcare, finance, education

### 6.4 Management Dimension Red Flags

```markdown
**Management Dimension Red Flags:**
- [ ] Any score of 1 in Management dimension
- [ ] No clear strategy (M1 ≤ 2)
- [ ] Poor financial planning (M3 ≤ 2)
- [ ] No milestone tracking (M6 ≤ 2)
- [ ] No learning/iteration (M11 ≤ 2)
```

**Rationale:**
- **No strategy:** Ventures without clear strategy struggle to make coherent decisions
- **Poor financial planning:** Investment readiness requires solid financial understanding
- **No milestones:** Without milestones, progress is unmeasurable and drift likely
- **No learning:** Inability to learn and adapt is fatal in startup environment

### 6.5 Commercial Dimension Red Flags

```markdown
**Commercial Dimension Red Flags:**
- [ ] Any score of 1 in Commercial dimension
- [ ] No customer validation (C1 ≤ 2)
- [ ] Business model unclear (C3 ≤ 2)
- [ ] No revenue model validation (C4 ≤ 2)
- [ ] Market size unknown (C2 = 1)
- [ ] No competitive analysis (C7 ≤ 2)
```

**Rationale:**
- **No customer validation:** Ventures must validate customer demand early
- **Business model unclear:** Must articulate how value is created and captured
- **No revenue validation:** Revenue model hypothesis should be tested with real customers
- **Market size unknown:** Cannot assess opportunity without market sizing
- **No competitive analysis:** Must understand competitive landscape

### 6.6 Red Flags Summary Table Format

The Assessment Results document must include a comprehensive Red Flags Summary:

```markdown
## RED FLAGS SUMMARY

**Total Red Flags Identified:** 5

**Team Dimension:** ✓ 1 red flag
- [✓] No domain expertise (T3=2) - Founders lack direct healthcare experience

**Technology Dimension:** ✓ 2 red flags
- [✓] No working prototype (Tech3=2) - Only concept mockups exist
- [✓] Security/privacy not addressed (Tech9=2) - HIPAA requirements not planned

**Management Dimension:** ✓ 2 red flags
- [✓] No clear strategy (M1=2) - Strategy document vague and contradictory
- [✓] Poor financial planning (M3=2) - No detailed financial model exists

**Commercial Dimension:** ✓ 0 red flags
- No red flags identified in Commercial dimension
```

---

## 7. TWO-FILE OUTPUT SPECIFICATION

### 7.1 Output Requirements

Step 2 assessment MUST produce exactly two documents:

1. **Assessment Results (Document 1)** - Comprehensive detailed assessment
2. **Score Summary (Document 2)** - Executive summary for decision-makers

Both documents must be produced in both Markdown (.md) and DOCX (.docx) formats.

**Total outputs:** 4 files (2 Markdown, 2 DOCX)

### 7.2 Document 1: Assessment Results

**Purpose:** Comprehensive record of all 40 questions with scores, evidence, analysis

**Filename:** `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Results.md`

**Length:** 8-12 pages (2,500-4,000 words)

**Primary Audience:** Evaluators, program managers, detailed review team

**Required Sections:**
1. Document Header
2. Assessment Overview
3. Dimensional Scores Summary Table
4. Team Dimension (9 questions, analysis, red flags)
5. Technology Dimension (11 questions, analysis, red flags)
6. Management Dimension (12 questions, analysis, red flags)
7. Commercial Dimension (8 questions, analysis, red flags)
8. Top Strengths (scores 4-5)
9. Critical Gaps (scores 1)
10. Major Weaknesses (scores 2)
11. Red Flags Summary
12. Questions to Ask Founders
13. Overall Narrative Assessment (5 paragraphs)
14. Quality Check
15. File Outputs
16. Next Steps

**Key Characteristics:**
- Every score includes evidence or gap description
- Dimension-by-dimension detailed analysis
- All 40 questions visible with individual scores
- Comprehensive narrative assessment
- Action-oriented questions for founders
- Self-contained quality checklist

### 7.3 Document 2: Score Summary

**Purpose:** Executive brief for investment committees, program directors, decision-makers

**Filename:** `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Summary.md`

**Length:** 3-5 pages (1,200-2,000 words)

**Primary Audience:** Investment committee, executive team, decision-makers

**Required Sections:**
1. Document Header
2. Executive Summary (3 paragraphs)
3. Dimensional Scores Table
4. Top 5 Strengths
5. Top 5 Gaps/Concerns
6. Red Flags
7. Strategic Recommendations
8. Stage Appropriateness Assessment
9. Recommendation (Proceed / Conditional / Request Info / Concerns / Non-Viable)
10. Next Steps
11. Key Insights for Discussion
12. Comparison to Portfolio/Cohort (optional)
13. Document Control

**Key Characteristics:**
- Executive-level language and formatting
- Focus on insights and recommendations, not raw data
- Action-oriented with clear next steps
- Decision-ready with explicit recommendation
- Discussion questions for committee
- Standalone document (can be read without Results document)

### 7.4 Consistency Requirements

Both documents must be:
- **Scored Consistently:** Same scores for all 40 questions
- **Dated Identically:** Same evaluation date
- **Branded Consistently:** Same company name, evaluator, project stage
- **Synchronized:** Dimensional averages must match exactly
- **Aligned:** Top strengths and gaps must correspond to scores
- **Cross-Referenced:** Documents reference each other

**Validation Check:**
Before finalizing, verify:
1. Dimensional averages match in both documents
2. Red flag counts match
3. Top 5 strengths come from highest-scored questions in Results
4. Top 5 gaps come from lowest-scored questions in Results
5. Recommendation in Summary is supported by analysis in Results

### 7.5 Format Conversion Requirements

**Markdown to DOCX Conversion:**
- Preserve all tables with proper formatting
- Maintain header hierarchy (H1, H2, H3)
- Keep bullet points and checkboxes
- Preserve bold and italic formatting
- Include proper page breaks between major sections
- Use professional fonts (e.g., Calibri 11pt for body, 14pt for headers)
- Set margins to 1 inch on all sides
- Include footer with page numbers and document version

---

## 8. VALIDATION CHECKLIST

### 8.1 Document Header Validation (5 items)

- [ ] Company name matches Step 1 Executive Brief exactly
- [ ] Evaluation date in YYYY-MM-DD format
- [ ] Evaluator name and organization provided
- [ ] Project stage from Step 0 included and matches classification
- [ ] Source document reference included with date

### 8.2 Question Scoring Validation (10 items)

- [ ] All 40 questions present (T1-T9, Tech1-Tech11, M1-M12, C1-C8)
- [ ] Each question has a score (1-5) or special code (INSUFFICIENT DATA, N/A)
- [ ] Each numeric score (1-5) includes evidence citation or gap description
- [ ] Evidence descriptions are specific, not generic
- [ ] Low scores (1-2) include explanation of why concerning
- [ ] High scores (4-5) include concrete examples supporting the score
- [ ] INSUFFICIENT DATA codes are justified (truly no information available)
- [ ] N/A codes are appropriate (question genuinely not applicable)
- [ ] No placeholder text remains (e.g., "[Evidence citation]")
- [ ] Scores align with stage expectations (contextualized appropriately)

### 8.3 Dimension Average Validation (8 items)

- [ ] Team average calculated correctly (sum of numeric scores / count)
- [ ] Technology average calculated correctly
- [ ] Management average calculated correctly
- [ ] Commercial average calculated correctly
- [ ] All averages rounded to two decimal places
- [ ] INSUFFICIENT DATA and N/A scores excluded from calculations
- [ ] Each dimension has minimum 50% questions scored
- [ ] Status labels (STRONG/ADEQUATE/CONCERN/CRITICAL) match score ranges

### 8.4 Analysis Sections Validation (8 items)

- [ ] Each dimension has "Key Strengths" section with 2+ items
- [ ] Each dimension has "Critical Gaps" section with identified gaps
- [ ] Key strengths align with scores of 4-5 in that dimension
- [ ] Critical gaps align with scores of 1-2 in that dimension
- [ ] Top Strengths section lists 5 highest-scoring questions
- [ ] Top Gaps section lists 5 lowest-scoring questions or concerns
- [ ] Critical Gaps section includes all Score 1 items
- [ ] Major Weaknesses section includes all Score 2 items

### 8.5 Red Flags Validation (6 items)

- [ ] All dimension-specific red flags checked (checked or unchecked)
- [ ] Red flags align with actual scores (e.g., T9≤2 checked only if T9 scored 2 or lower)
- [ ] Total red flag count is accurate
- [ ] Red flags summary lists specific red flags identified
- [ ] Each checked red flag includes explanation
- [ ] Risk level (LOW/MODERATE/HIGH/CRITICAL) appropriate for red flag count

### 8.6 Questions for Founders Validation (3 items)

- [ ] All INSUFFICIENT DATA items converted to specific questions
- [ ] Follow-up questions address identified gaps
- [ ] Validation requests are specific and actionable (not vague)

### 8.7 Narrative Assessment Validation (5 items)

- [ ] All 5 paragraphs complete (Readiness, Strengths Pattern, Risks, Stage Appropriateness, Recommendation)
- [ ] Narrative aligns with quantitative scores
- [ ] Specific recommendation provided (Proceed / Conditional / Request Info / Concerns / Non-Viable)
- [ ] Recommendation is justified by scores and analysis
- [ ] Next steps are specific and actionable

### 8.8 Score Summary Validation (7 items)

- [ ] Executive summary complete (3 paragraphs)
- [ ] Dimensional scores match Assessment Results exactly
- [ ] Top 5 strengths match highest scores from Results document
- [ ] Top 5 gaps match lowest scores from Results document
- [ ] Red flag count matches Results document
- [ ] Stage appropriateness assessment complete
- [ ] Clear recommendation selected and justified

### 8.9 Two-Document Consistency Validation (6 items)

- [ ] Both documents have identical company name, date, evaluator
- [ ] Dimensional averages identical in both documents
- [ ] Red flag counts identical in both documents
- [ ] Top strengths in Summary come from Results document
- [ ] Top gaps in Summary come from Results document
- [ ] Both documents reference each other appropriately

### 8.10 File Output Validation (4 items)

- [ ] Filenames follow naming convention exactly
- [ ] Both .md and .docx versions created for each document
- [ ] Total 4 files created (2 Results, 2 Summary)
- [ ] DOCX formatting preserved (tables, headers, bullets)

**Total Validation Items:** 62 checks

---

## 9. COMMON MISTAKES

### 9.1 Scoring Mistakes (10 items)

**Mistake 1: Generic Evidence Descriptions**
- **Wrong:** "Good team experience" for T2 score of 4
- **Right:** "CEO has founded two previous startups (1 exit, 1 ongoing), CTO has 8 years at scale-up, demonstrating relevant startup experience"

**Mistake 2: Scores Not Aligned with Evidence**
- **Wrong:** Score of 4 with evidence showing significant gaps
- **Right:** If evidence shows gaps, score should be 2-3, not 4

**Mistake 3: Ignoring Stage Context**
- **Wrong:** Score of 2 for no revenue at Idea Stage
- **Right:** Score of 3 (acceptable) or N/A for no revenue at Idea Stage

**Mistake 4: Overusing INSUFFICIENT DATA**
- **Wrong:** Marking INSUFFICIENT DATA when information could be inferred
- **Right:** Use inference and judgment; reserve INSUFFICIENT DATA for truly missing information

**Mistake 5: Not Distinguishing Between Absence and Weakness**
- **Wrong:** Score of 2 when something doesn't exist at all (should be 1)
- **Right:** Score of 1 = doesn't exist; Score of 2 = exists but weak

**Mistake 6: Inconsistent Scoring Across Similar Questions**
- **Wrong:** T3 (domain expertise) = 5 but M2 (market understanding) = 2 without explanation
- **Right:** If team has domain expertise, they likely understand market; scores should align or discrepancy explained

**Mistake 7: Treating All Dimensions Equally Regardless of Stage**
- **Wrong:** Expecting strong Management and Commercial scores at Idea Stage
- **Right:** Technical ventures at Idea Stage should be strong in Team/Tech, acceptable in Mgmt, weak in Commercial

**Mistake 8: Failing to Use the Full 1-5 Scale**
- **Wrong:** Only using scores of 2, 3, 4 (avoiding 1 and 5)
- **Right:** Use 1 for critical gaps, 5 for exceptional capabilities; don't cluster in middle

**Mistake 9: Circular Evidence**
- **Wrong:** "T5 Leadership scored 4 because team has good leadership"
- **Right:** "T5 Leadership scored 4 because CEO has articulated clear 3-year vision, aligned team around shared goals, and demonstrated decision-making in crisis (pivot in Q2 2024)"

**Mistake 10: Not Documenting Assumptions**
- **Wrong:** Scoring without noting when assumptions made
- **Right:** Use CONTEXTUAL NOTE when assumptions or interpretations required

### 9.2 Calculation Mistakes (5 items)

**Mistake 11: Including INSUFFICIENT DATA in Average**
- **Wrong:** Team dimension with T4=INSUFFICIENT DATA counted as 0 in average
- **Right:** Exclude INSUFFICIENT DATA from both numerator and denominator

**Mistake 12: Incorrect Rounding**
- **Wrong:** 3.666666 rounded to 3.7 or left as 3.666666
- **Right:** 3.666666 rounded to 3.67 (two decimal places)

**Mistake 13: Wrong Denominator**
- **Wrong:** Always dividing by total questions (e.g., 9 for Team) even when some excluded
- **Right:** Divide by number of questions actually scored with numeric values

**Mistake 14: Misapplying Status Thresholds**
- **Wrong:** Score of 3.0 labeled as CONCERN
- **Right:** Score of 3.0 is ADEQUATE (3.0-3.9 range)

**Mistake 15: Not Recalculating After Score Changes**
- **Wrong:** Changing individual score but forgetting to update dimension average
- **Right:** Always recalculate dimension average when any score in that dimension changes

### 9.3 Red Flags Mistakes (5 items)

**Mistake 16: Not Checking Red Flags That Apply**
- **Wrong:** T9=2 (commitment) but red flag not checked
- **Right:** If T9≤2, the "No full-time commitment" red flag must be checked

**Mistake 17: Checking Red Flags That Don't Apply**
- **Wrong:** Checking "No customer validation" when C1=3
- **Right:** Only check if threshold met (C1≤2)

**Mistake 18: Miscounting Total Red Flags**
- **Wrong:** 3 red flags checked but "Total: 5" stated
- **Right:** Count matches actual checked red flags

**Mistake 19: Ignoring Context for Red Flags**
- **Wrong:** Flagging "No customer validation" as red flag at Idea Stage
- **Right:** Consider stage; some red flags not critical at very early stages (note in context)

**Mistake 20: Not Explaining Red Flags**
- **Wrong:** Just checking boxes without explanation
- **Right:** Each checked red flag includes specific explanation of the issue

### 9.4 Document Structure Mistakes (5 items)

**Mistake 21: Incomplete Narrative Assessment**
- **Wrong:** Only 3 of 5 paragraphs completed
- **Right:** All 5 paragraphs must be complete

**Mistake 22: Missing Questions for Founders**
- **Wrong:** Multiple INSUFFICIENT DATA scores but no questions listed
- **Right:** Every INSUFFICIENT DATA should generate a specific question

**Mistake 23: Inconsistent Top Strengths/Gaps**
- **Wrong:** Top 5 strengths list includes questions scored 3
- **Right:** Top 5 should be highest scores; if only 3 questions scored 4+, list only 3

**Mistake 24: Vague Recommendations**
- **Wrong:** "Team needs improvement"
- **Right:** "Hire experienced CFO within 60 days to address financial planning gap (M3=2)"

**Mistake 25: Quality Checklist Not Used**
- **Wrong:** Leaving quality checklist blank
- **Right:** Check every item in quality checklist before finalizing

### 9.5 Two-Document Mistakes (5 items)

**Mistake 26: Inconsistent Scores Between Documents**
- **Wrong:** Results shows Team=3.67, Summary shows Team=3.89
- **Right:** Both documents must show identical dimensional averages

**Mistake 27: Summary Without Supporting Results**
- **Wrong:** Summary lists gaps not visible in Results document
- **Right:** Every insight in Summary must be traceable to Results data

**Mistake 28: Wrong Document for Audience**
- **Wrong:** Sending full Results document to busy executive
- **Right:** Summary for executives, Results for detailed analysis team

**Mistake 29: Filename Errors**
- **Wrong:** `CompanyName_Diagnostic_Summary.md` (missing date and step number)
- **Right:** `CompanyName_2025-01-15_02_Diagnostic_Summary.md`

**Mistake 30: Not Creating All Four Files**
- **Wrong:** Only creating .md files, no .docx
- **Right:** Must create both .md and .docx for both Results and Summary (4 files total)

**Total Common Mistakes Documented:** 30

---

## 10. FILE NAMING CONVENTION

### 10.1 Naming Convention Format

**Standard Format:**
```
[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_[Type].[extension]
```

**Components:**
- **[CompanyName]:** Company name without spaces (use CamelCase or underscores)
- **[YYYY-MM-DD]:** Evaluation date in ISO 8601 format
- **02:** Step number (always "02" for this assessment)
- **Diagnostic:** Assessment type (always "Diagnostic" for Step 2)
- **[Type]:** Either "Results" or "Summary"
- **[extension]:** Either "md" or "docx"

### 10.2 Required Files

For each assessment, create exactly four files:

1. `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Results.md`
2. `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Results.docx`
3. `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Summary.md`
4. `[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_Summary.docx`

### 10.3 Company Name Formatting

**Rules:**
- Remove spaces: Use CamelCase or underscores
- Remove special characters: No &, !, @, etc.
- Keep abbreviations: If commonly used (e.g., "AI", "ML", "IoT")
- Maximum 30 characters
- Consistent across all documents

**Examples:**
- "HealthTech Innovations, Inc." → `HealthTechInnovations`
- "AI-Driven Solutions LLC" → `AIDrivenSolutions`
- "Green Energy Systems & Co" → `GreenEnergySystems`
- "FinTech Solutions" → `FinTechSolutions`

### 10.4 Complete Filename Examples

**Example 1: Early-stage healthcare startup**
```
HealthTechInnovations_2025-01-15_02_Diagnostic_Results.md
HealthTechInnovations_2025-01-15_02_Diagnostic_Results.docx
HealthTechInnovations_2025-01-15_02_Diagnostic_Summary.md
HealthTechInnovations_2025-01-15_02_Diagnostic_Summary.docx
```

**Example 2: AI technology company**
```
AIDrivenSolutions_2025-02-20_02_Diagnostic_Results.md
AIDrivenSolutions_2025-02-20_02_Diagnostic_Results.docx
AIDrivenSolutions_2025-02-20_02_Diagnostic_Summary.md
AIDrivenSolutions_2025-02-20_02_Diagnostic_Summary.docx
```

**Example 3: Sustainability venture**
```
GreenEnergySystems_2025-03-10_02_Diagnostic_Results.md
GreenEnergySystems_2025-03-10_02_Diagnostic_Results.docx
GreenEnergySystems_2025-03-10_02_Diagnostic_Summary.md
GreenEnergySystems_2025-03-10_02_Diagnostic_Summary.docx
```

### 10.5 Version Control

**For revised assessments, append version number:**
```
[CompanyName]_[YYYY-MM-DD]_02_Diagnostic_[Type]_v[X].[extension]
```

**Example:**
```
HealthTechInnovations_2025-01-15_02_Diagnostic_Results_v2.md
```

**Versioning Rules:**
- v1 = Initial assessment (often omitted from filename)
- v2 = First revision after new information received
- v3 = Second revision, etc.
- Include revision note at top of document explaining changes

### 10.6 Folder Structure Recommendation

**Recommended file organization:**
```
/assessments/
  /[CompanyName]/
    /step0_classification/
    /step1_executive_brief/
    /step2_diagnostic/
      HealthTechInnovations_2025-01-15_02_Diagnostic_Results.md
      HealthTechInnovations_2025-01-15_02_Diagnostic_Results.docx
      HealthTechInnovations_2025-01-15_02_Diagnostic_Summary.md
      HealthTechInnovations_2025-01-15_02_Diagnostic_Summary.docx
    /step3_market_maturity/
    /step4_decision_scorecard/
```

---

## 11. ADVANCED GUIDANCE

### 11.1 Handling Edge Cases

**Edge Case 1: Extremely Limited Information**
- If < 30% of questions can be scored with confidence
- Recommendation: REQUEST ADDITIONAL INFO rather than proceeding
- Generate comprehensive questions list for founders
- Do not make up scores or over-infer from limited data

**Edge Case 2: Pivot or Major Change Mentioned**
- If venture has recently pivoted or undergone major change
- Score current state, not historical
- Note pivot in context
- Consider stage reset (post-pivot may be earlier stage than claimed)

**Edge Case 3: Multiple Business Lines**
- If venture has multiple distinct products/services
- Focus on primary/flagship offering
- Note diversification in context
- Consider if dilution of focus is a Management weakness

**Edge Case 4: Pre-Revenue but Advanced Stage Claim**
- If venture claims "Early Commercialization" but has no revenue
- Score truthfully (C4 will be low)
- Note stage mismatch in narrative
- May recommend stage reclassification

**Edge Case 5: Exceptional Strength in One Area, Critical Gaps in Others**
- If Tech=5.0 but Management=1.5
- Do not artificially balance scores
- Clearly articulate the imbalanced profile
- Recommendation should address whether exceptional strength compensates for critical gaps

### 11.2 Sector-Specific Considerations

**Healthcare/Biotech:**
- Tech9 (Security/Privacy) critical due to HIPAA/regulatory requirements
- Tech2 (Feasibility) often requires clinical validation
- Longer timelines expected; adjust stage expectations
- Regulatory pathway understanding part of M2 (Market Understanding)

**Deep Tech/Hardware:**
- Tech3 (Development Stage) may be extended due to complexity
- Higher capital requirements affect M3 (Financial Planning) expectations
- IP (Tech4) often critical differentiator
- Partnerships (Tech8) often necessary for manufacturing

**B2B SaaS:**
- C1 (Customer Validation) critical - need pilot customers
- C4 (Revenue Validation) achievable earlier - score accordingly
- M6 (Milestone Tracking) important for product development cadence
- Tech10 (Tech Stack) should be modern and scalable

**Consumer/B2C:**
- C2 (Market Size) critical - need large TAM for venture-scale returns
- C5 (Sales/Marketing Strategy) higher importance
- T4 (Talent Attraction) important for growth
- M10 (Culture/Values) affects brand and customer experience

**Impact/Social Enterprise:**
- M10 (Culture/Values) higher importance - mission-driven
- C3 (Business Model) may include non-profit elements
- Consider blended value proposition (financial + social return)
- M9 (Stakeholder Management) more complex with multiple stakeholder types

### 11.3 Scoring Calibration

To ensure consistent scoring across evaluators:

**Calibration Exercise:** Use benchmark ventures
- **Score 5 Benchmark:** [Example: Y Combinator top performers]
- **Score 4 Benchmark:** [Example: Accelerator graduates with strong traction]
- **Score 3 Benchmark:** [Example: Typical seed-stage venture]
- **Score 2 Benchmark:** [Example: Ventures with identifiable gaps]
- **Score 1 Benchmark:** [Example: Ventures with critical deficiencies]

**Calibration Process:**
1. Multiple evaluators independently score same venture
2. Compare scores and discuss discrepancies
3. Identify scoring patterns and biases
4. Align on interpretation of scoring rubric
5. Re-score with aligned understanding

**Acceptable Variance:**
- Within same evaluator over time: ±0.3 points
- Between different evaluators: ±0.5 points
- If variance exceeds thresholds, re-calibration needed

### 11.4 Integration with VIANEO Framework

**Step 0 → Step 2 Connection:**
- Project Stage from Step 0 used for stage-adjusted scoring
- More mature stages should have higher scores across all dimensions
- Stage mismatches identified and noted

**Step 1 → Step 2 Connection:**
- Executive Brief is primary source document
- All scores must be evidenced from Brief content
- INSUFFICIENT DATA indicates Brief gaps, triggers questions

**Step 2 → Step 3 Connection:**
- Proceed to Step 3 if dimensional scores adequate (most ≥ 3.0)
- Step 3 will provide market validation of Step 2 assumptions
- Team and Technology strengths from Step 2 necessary but not sufficient

**Step 2 → Step 4 Connection:**
- Dimensional scores feed into Step 4 Decision Scorecard
- Red flags from Step 2 become risk factors in Step 4
- Top strengths become competitive advantages in Step 4

---

## 12. QUALITY ASSURANCE

### 12.1 Pre-Submission Checklist

Before finalizing assessment, complete this checklist:

**Completeness:**
- [ ] All 40 questions scored or marked with special code
- [ ] All scores have supporting evidence
- [ ] All dimension averages calculated
- [ ] All required sections present in both documents
- [ ] All 4 files created (2 .md, 2 .docx)

**Accuracy:**
- [ ] Calculations verified (spot-check 3-4 averages)
- [ ] Red flags match scores
- [ ] Top strengths/gaps align with actual scores
- [ ] Filename conventions followed exactly

**Consistency:**
- [ ] Dimensional scores identical in both documents
- [ ] Company name consistent across all 4 files
- [ ] Dates consistent
- [ ] No contradictions between documents

**Quality:**
- [ ] Evidence is specific, not generic
- [ ] Narrative is coherent and well-written
- [ ] Recommendations are clear and actionable
- [ ] No placeholder text remains
- [ ] DOCX formatting preserved properly

### 12.2 Peer Review Process

**For high-stakes assessments, conduct peer review:**

1. **Reviewer checks:**
   - Score appropriateness given evidence
   - Calculation accuracy
   - Logic of recommendations
   - Consistency between documents

2. **Reviewer provides:**
   - Confirmation of acceptance OR
   - Specific requested changes

3. **Original evaluator:**
   - Addresses reviewer feedback
   - Re-submits for final approval

### 12.3 Common Quality Issues

**Issue 1: Inconsistent Tone**
- Results document uses evaluator perspective; Summary uses executive perspective
- Maintain appropriate tone for each document's audience

**Issue 2: Over-Inference**
- Scoring based on assumptions rather than evidence
- Solution: If uncertain, use INSUFFICIENT DATA and generate question

**Issue 3: Under-Specification**
- Vague recommendations like "improve team"
- Solution: Be specific - "Hire CFO with SaaS experience by Q2"

**Issue 4: Defensive Scoring**
- Avoiding low scores to not offend founders
- Solution: Score truthfully; low scores with specific gaps are actionable feedback

---

## 13. TEMPLATES AND EXAMPLES

### 13.1 Template Locations

**Primary Templates:**
- `/templates/40Q_Assessment_Results_Template.md` - Comprehensive assessment template
- `/templates/40Q_Score_Summary_Template.md` - Executive summary template

**Supporting Documents:**
- `/guides/Step2_Assessment_Guide.md` - Detailed assessment methodology
- `/examples/[CompanyName]_02_Diagnostic_Results.md` - Example completed assessment

### 13.2 Template Usage

**Do's:**
- Start with template for structure
- Customize content for specific venture
- Remove all placeholder text before finalizing
- Adapt narrative to venture's unique characteristics

**Don'ts:**
- Leave placeholder text (e.g., "[Evidence citation]")
- Copy-paste generic descriptions across ventures
- Change section structure or ordering
- Skip required sections

### 13.3 Example Scoring Pattern

**Prototype Stage Healthcare Venture - Typical Profile:**

| Dimension | Average | Status | Pattern |
|-----------|---------|--------|---------|
| Team | 3.78 | ADEQUATE | Strong domain expertise (T3=5), good technical skills (T1=4), but limited startup experience (T2=2) |
| Technology | 3.91 | ADEQUATE | Proven feasibility (Tech2=5), working prototype (Tech3=4), but scalability untested (Tech5=3) |
| Management | 2.67 | CONCERN | Clear vision (M1=4) but weak financial planning (M3=2), no milestone tracking (M6=2) |
| Commercial | 2.88 | CONCERN | Good customer validation (C1=4), but business model unclear (C3=2), no revenue validation (C4=2) |

**Interpretation:** Strong technical foundation with execution and commercialization gaps typical for Prototype stage but needing attention before investment.

---

## 14. DOCUMENT HISTORY & UPDATES

**Version 1.0 - 2025-01-15**
- Initial format specification created
- 40-question framework established
- Two-document output structure defined
- 62-item validation checklist created
- 30 common mistakes documented

**Future Updates:**
- Version 1.1: Add sector-specific scoring guidance
- Version 1.2: Include scoring calibration examples
- Version 1.3: Add international venture considerations

---

## 15. REFERENCES & RESOURCES

**Related Documents:**
- `FORMAT_SPEC_Step0_Classification.md` - Project stage classification format
- `FORMAT_SPEC_Step1_Executive_Brief.md` - Source document format for Step 2
- `FORMAT_SPEC_Step3_Market_Maturity.md` - Next assessment after Step 2
- `FORMAT_SPEC_Step4_Decision_Scorecard.md` - Final decision framework

**Methodology Resources:**
- VIANEO 13-Step Evaluation Framework Overview
- Scoring calibration benchmarks
- Stage-specific expectations guide

**Templates:**
- `40Q_Assessment_Results_Template.md`
- `40Q_Score_Summary_Template.md`

**Examples:**
- Example completed assessments (anonymized)
- Scoring pattern libraries
- Red flag case studies

---

## 16. CONTACT & SUPPORT

**For questions about this format specification:**
- Review related documentation in `/docs/`
- Consult templates in `/templates/`
- Reference examples in `/examples/`
- Contact VIANEO Framework team for clarification

**Document Feedback:**
If you identify errors, ambiguities, or areas for improvement in this format specification, please document and submit for next version update.

---

**END OF FORMAT SPECIFICATION**

**Document Word Count:** ~7,800 words
**Validation Items:** 62 checks
**Common Mistakes Documented:** 30 items
**Template Compatibility:** VIANEO 13-Step Framework v1.0

**Document Status:** FINAL
**Last Reviewed:** 2025-01-15
**Next Review Date:** 2025-07-15
