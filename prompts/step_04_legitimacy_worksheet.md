# STEP 4: Legitimacy Deep Dive Worksheet

**Time Required:** 20-30 minutes
**Output:** TWO documents - (1) Markdown worksheet, (2) DOCX formatted version
**Weight in VIANEO Score:** 15% of overall evaluation

---

## Overview

The Legitimacy Assessment validates the foundational justification for the business by examining:

1. **Problem Definition** - Is the problem clear, significant, and solution-neutral?
2. **Application Domain** - Is the scope appropriate and well-bounded?
3. **Team & Approach** - Does the team have relevant capabilities and exploratory posture?
4. **Available Resources** - Are there genuine competitive advantages in human, physical/intellectual, and financial resources?

**Philosophy:** Before evaluating market fit or financial projections, confirm the project starts from a solid foundation with a clear problem, appropriate scope, and sufficient means to pursue the opportunity.

---

## Required Inputs

From previous steps:
- **Step 0:** Executive Brief (B1-B7 fields, especially B2 Problem, B4 Market, B6 Traction, B7 Team)
- **Step 2:** 40-Question Diagnostic (especially Team section T1-T9, Technology Tech1-Tech11)
- **Additional materials:** Pitch deck, business plan, team bios, financial information

---

## Output Structure

### 1. Document Header

```markdown
# Vianeo Legitimacy Worksheet: [Project Name]
```

---

### 2. Core Project Information

Create a table with three rows:

| Field | Content |
|-------|---------|
| **Project Genesis** | [250 characters maximum] |
| **Problem to Solve** | [250 characters maximum] |
| **Field of Application** | [60 characters maximum] |

**Guidelines:**

**Project Genesis (250 chars):**
- Origin story, founding context, how the project started
- Include key dates, founders, initial partnerships, or funding if relevant
- Example: "Initiated 2019 by Kota Ageiwa after family experience with Alzheimer's and Mitsui partnerships with Kumon. Incubated within Fortune 500 Mitsui & Co. with $5.5M investment. Scientific validation from UC Santa Barbara and Dr. Kawashima."

**Problem to Solve (250 chars):**
- Define the problem clearly WITHOUT embedding the solution
- Focus on the gap, pain point, or unmet need
- Include evidence of significance (data, user research, market indicators)
- Example: "Cognitive decline threatens independence for aging populations. Current solutions either inaccessible (clinical-grade tools) or unvalidated (app-only). 35.9% of cognitive searches from adults seeking prevention, but no affordable real-time measurement exists."

**Field of Application (60 chars):**
- Specific socio-economic domain or sector
- Be precise but not overly narrow
- Include boundaries where helpful
- Example: "Cognitive health & wellness for aging populations (55-75)"
- NOT: "Healthcare" (too broad)
- NOT: "Alzheimer's disease treatment in Tokyo metropolitan area only" (too narrow)

---

### 3. Available Means: Human Resources

Create a table with columns: **Means | Differentiator? | Note**

**Structure:**
- List 4-8 key team members or advisors
- Format each row as: "[Name] ([Role]): [Years] [Key Experience]"
- Differentiator?: Yes/No (Is this person's background rare or uniquely valuable?)
- Note: Brief explanation of why they're valuable or ordinary (50-80 chars each)

**Example Row:**
```
Dr. Ryuta Kawashima (Advisor): Nintendo Brain Training creator | Yes | 36M copies sold, global neuroscience authority
```

**After the table, add:**

```markdown
**Overall Note (250 chars):** [Summary of team strengths, gaps, and differentiators]
```

**Evaluation Criteria:**
- Are there domain experts with deep relevant experience? (Score +1)
- Does anyone have rare credentials or networks? (Score +1)
- Are there critical gaps (e.g., no technical lead, no regulatory expert)? (Score -1)
- Is startup/scale experience present? (Score +0.5)
- What is commitment level (full-time vs. part-time)? (Full-time +0.5)

**Red Flags:**
- No domain expertise among core team
- No evidence of customer interviews or problem validation
- Part-time team members for full-time problem
- Missing critical functions
- Team turnover or instability

---

### 4. Available Means: Physical/Intellectual Resources

Create a table with columns: **Means | Differentiator? | Note**

**Structure:**
- List 4-10 key assets: patents, licenses, technology, data, partnerships, facilities, equipment
- Differentiator?: Yes/No (Is this asset rare, proprietary, or hard to replicate?)
- Note: Explain the asset's value or limitations (50-80 chars each)

**Example Row:**
```
Exclusive NeU/Hitachi NIRS sensor license | Yes | 30+ years R&D, proprietary dual-sensor noise reduction
```

**After the table, add:**

```markdown
**Overall Note (250 chars):** [Summary of IP position, technical assets, dependencies, and competitive moats]
```

**Evaluation Criteria:**
- Proprietary vs. standard technology? (Proprietary +1)
- Owned patents or exclusive licenses? (Yes +1)
- Validation through research, trials, or commercial use? (Yes +1)
- Manufacturing or infrastructure capacity? (Adequate +0.5)
- Data assets or network effects? (Yes +0.5)

**Red Flags:**
- Critical dependencies on partners without commitments
- No proprietary assets or defensible advantages
- Infrastructure requirements vastly exceed current resources

---

### 5. Available Means: Financial Resources

Create a table with columns: **Resource | Amount | Differentiator? | Note**

**Structure:**
- List 3-6 financial resources: funding raised, revenue, personal investment, grants
- Amount: Dollar figures or "N/A"
- Differentiator?: Yes/No (Is this funding source unusual or strategically valuable?)
- Note: Context about the funding (50-80 chars each)

**Example Row:**
```
Mitsui transfer at EBO | $5.5M (assets transferred) | Yes | Rare Fortune 500 backing for employee buyout
```

**After the table, add:**

```markdown
**Overall Financial Note:** [Summary of financial position, runway, dependencies, sustainability]
```

**Evaluation Criteria:**
- Current capital position and burn rate?
- Revenue generation (even if minimal)?
- Unusual funding sources (corporate backing, strategic investors)?
- Dependency on external fundraising?
- Runway: <6 months (poor), 6-12 months (adequate), 12-18 months (good), 18+ months (strong)

**Red Flags:**
- Running out of capital with no fundraising progress
- No revenue and no clear path to funding
- Heavy dependencies without commitments

---

## Required Output: Available Means (for Step 11 Features/Means Matrix)

The following must be captured in a structured format for use in Step 11:

### Human Means
List each human resource with differentiation status:
- [Description] | Differentiating: Yes/No

Example:
- 30+ years of sales relationship to manufacturing plants | Differentiating: Yes
- 1 developer | Differentiating: No

### Physical/Intellectual Means
List each physical or intellectual resource with differentiation status:
- [Description] | Differentiating: Yes/No

Example:
- Beta software for log sheets and log books | Differentiating: Yes

### Financial Means
- [Amount and context]

Example:
- 60,000 dollars

**Important**: These exact descriptions become column headers in the Step 11 Features/Means matrix. Write clearly and concisely.

---

### 6. Differentiating Advantages: Unique Barriers to Entry

```markdown
**Content (250 chars max):** [Synthesize the 2-4 strongest competitive moats from all resources above]
```

**Guidelines:**
- Focus on defensible advantages (not just "good team")
- Prioritize: exclusive partnerships, proprietary IP, validated data, regulatory approvals, rare networks
- Explain WHY each advantage is hard to replicate
- Connect advantages to the specific problem being solved

**Example:**
"Exclusive NeU/Hitachi sensor licensing creates hardware moat. Dr. Kawashima algorithms proven through 36M Nintendo sales unreplicable. Three RCTs plus longitudinal data rare for consumer neurotech. AARP validation signals difficult-to-achieve senior market access."

---

### 7. Assessment Summary

After completing all sections above, provide a comprehensive evaluation:

#### Legitimacy Score: X.X/5 (Category)

**Formula:** Average of 4 component scores (Problem Definition + Application Domain + Team & Approach + Resources) ÷ 4

**Categories:**
- **4.5-5.0:** Exceptional - Proceed with confidence
- **3.5-4.4:** Above Average - Proceed with focus areas
- **3.0-3.4:** Adequate - Conditional proceed
- **2.0-2.9:** Below Average - Major rework needed
- **<2.0:** Poor - Reconsider fundamentals

---

#### Strengths:

Bulleted list of 4-6 key strengths identified across all legitimacy components:
- Focus on validated strengths with evidence
- Include specific metrics or achievements
- Highlight genuine differentiators
- Note early traction or validation

**Example:**
- Crystal clear problem definition backed by search data (35.9% cognitive searches)
- Well-scoped application domain (55-75 age range, cognitive health)
- Multiple true differentiators (Kawashima, exclusive sensor license, RCT validation)
- Unusual corporate backing providing stability and credibility
- Problem validated through family experience + research data

---

#### Gaps:

Bulleted list of 5-8 critical gaps or weaknesses:
- Be honest about missing information
- Identify team capability gaps
- Note resource dependencies
- Highlight risks or uncertainties
- Flag areas requiring attention

**Example:**
- No in-house deep neuroscience expertise (reliant on advisors)
- Limited startup exit experience in team
- Modest revenue traction ($60-75K) insufficient for sustainability
- Manufacturing dependency on NeU partnership
- Missing clinical regulatory expertise for potential medical claims

---

#### Detailed Scoring:

**1. Problem Definition (X/5):**

**Scoring Rubric:**
- **5:** Precise definition with clear metrics and boundaries. Strong evidence of problem significance. Multiple sources validate problem existence.
- **4:** Clear problem statement with minor solution elements. Good evidence of significance. Some external validation.
- **3:** Basic problem clarity but some vagueness. Moderate evidence of significance. Limited validation beyond team belief.
- **2:** Problem definition includes solution elements or is vague. Weak evidence of significance. Mostly internal validation.
- **1:** Vague, solution-dependent, or scope constantly shifting. No evidence problem exists beyond innovator's perception.

**Write:** 2-3 sentence explanation of the score. Reference specific evidence or lack thereof. Note why points were added or deducted.

---

**2. Application Domain (X/5):**

**Scoring Rubric:**
- **5:** Well-defined domain with clear boundaries. Strong domain expertise evident. Appropriate scope for resources.
- **4:** Clear domain definition with minor boundary questions. Good domain understanding. Reasonable scope.
- **3:** Basic domain clarity but boundaries somewhat fuzzy. Adequate domain knowledge. Scope manageable but broad.
- **2:** Domain definition shifting or unclear. Limited domain understanding. Scope too broad or narrow.
- **1:** Overly broad domain or constantly shifting scope. No demonstrated domain knowledge.

**Write:** 2-3 sentence explanation of the score. Assess domain clarity, boundaries, and appropriateness for team resources.

---

**3. Team & Approach (X/5):**

**Scoring Rubric:**
- **5:** Team with rare expertise directly relevant to domain. Demonstrates exploratory methodology. Full-time commitment. No critical gaps.
- **4:** Strong relevant experience with some unique capabilities. Good balance of exploration and execution. Mostly committed. Minor gaps.
- **3:** Basic relevant experience without standout credentials. Some evidence of customer exploration. Partial commitment. Some gaps noted.
- **2:** Limited relevant experience or major gaps. Little evidence of user validation approach. Minimal commitment. Significant gaps.
- **1:** No relevant domain experience. Solution-obsessed without validation. No clear commitment. Critical gaps across functions.

**Write:** 2-3 sentence explanation of the score. Evaluate team differentiators, gaps, commitment level, and validation approach.

---

**4. Resources (X/5):**

**Scoring Rubric:**
- **5:** Comprehensive resources with multiple differentiating assets. Strong IP position. Adequate capital with unusual funding sources.
- **4:** Good resource base with some differentiators. Decent IP or partnerships. Sufficient capital for near-term milestones.
- **3:** Basic resources adequate for next phase. Standard assets. Minimal capital requiring fundraising soon.
- **2:** Significant resource gaps. Limited assets. Capital concerns or heavy dependencies.
- **1:** Major resource gaps across categories. No distinct assets. Critical capital shortage.

**Write:** 2-3 sentence explanation of the score. Assess IP position, financial stability, partnerships, and dependencies.

---

#### Overall Assessment:

Single paragraph (150-200 words) synthesizing the legitimacy evaluation. Address:
- Is the foundation solid enough to proceed?
- What are the critical dependencies for success?
- Should this project advance to deeper evaluation (Desirability, Acceptability, Feasibility, Viability)?
- What specific areas need attention in next phases?

**Example:**
"This is a strong legitimacy foundation. The problem is real and well-defined, the domain is appropriately scoped, and there are genuine competitive advantages. The gaps are acknowledged and manageable. This project warrants deeper evaluation in Desirability, Acceptability, Feasibility, and Viability dimensions."

---

#### Key Risk Factors:

Bulleted list of 4-6 primary risks that could undermine legitimacy:
- Founder/team concentration risks
- Financial/funding dependencies
- Competitive threats
- Partnership dependencies
- Regulatory uncertainties
- Technical execution risks

**Example:**
- Advisor dependency for deep technical expertise
- Manufacturing partnership dependency
- Revenue insufficient for near-term sustainability
- Regulatory pathway unclear for potential medical claims

---

#### Key Success Factors:

Bulleted list of 4-6 critical actions needed to strengthen legitimacy:
- Specific, actionable items
- Prioritized by importance
- Tied to identified gaps
- Achievable within 6-12 months

**Example:**
- Close current seed round to extend runway
- Hire in-house neuroscience/clinical expert
- Expand manufacturing capacity or diversify suppliers
- Accelerate user acquisition to build data moat
- Clarify regulatory strategy for medical vs. wellness positioning

---

## Critical Character Limits

Strictly enforce these limits. No exceptions.

| Field | Max Characters |
|-------|---------------|
| Project Genesis | 250 |
| Problem to Solve | 250 |
| Field of Application | 60 |
| Human Means Overall Note | 250 |
| Physical/Intellectual Means Overall Note | 250 |
| Financial Means Note per row | 80 |
| Differentiating Advantages | 250 |

**To Check Character Count:**
- In most text editors: Select text → Check status bar
- Online: Use charactercounttool.com or wordcounter.net
- In Python: `len("your text here")`

**If Over Limit:**
1. Remove filler words ("very," "really," "in order to")
2. Use strong verbs over weak verb + adverb combinations
3. Cut adjectives that don't add information
4. Use abbreviations only if universally understood in context

---

## Writing Quality Standards

**Conciseness:**
- Remove filler words
- Use strong verbs
- Cut unnecessary adjectives
- Use abbreviations sparingly

**Specificity:**
- Include numbers (years of experience, funding amounts, user counts)
- Name actual entities (partners, technologies, credentials)
- Avoid generic phrases ("various stakeholders," "significant experience")

**Evidence-Based:**
- Cite concrete facts over aspirations
- Distinguish between validated capabilities and hypothetical strengths
- Note gaps honestly (critical for assessment value)

**Good Examples:**
- ✅ "15+ yrs Mitsui M&A, healthcare strategy, INSEAD MBA, trilingual"
- ✅ "36M copies sold, global neuroscience authority"
- ✅ "30+ years R&D, proprietary dual-sensor noise reduction"

**Bad Examples:**
- ❌ "Very experienced leader with significant background in healthcare"
- ❌ "World-class team with exceptional capabilities"
- ❌ "Strong partnerships providing value"

---

## Execution Process

### Phase 1: Preparation (5 min)

**Gather Materials:**
- [ ] Step 0: Executive Brief (B1-B7)
- [ ] Step 2: 40-Question Diagnostic (Team, Tech sections)
- [ ] Pitch deck or business plan
- [ ] Team bios and LinkedIn profiles
- [ ] Financial information (funding, revenue, projections)
- [ ] Technical documentation or IP information

**Review:**
- Problem statement from Step 0 (B2)
- Team assessment from Step 2 (T1-T9)
- Technology/IP assessment from Step 2 (Tech1-Tech11)
- Traction evidence from Step 0 (B6)

---

### Phase 2: Core Information (5 min)

**Fill in the 3-row table:**

1. **Project Genesis (250 chars):**
   - When did it start?
   - Who founded it?
   - What was the catalyst?
   - Any notable backing or partnerships?

2. **Problem to Solve (250 chars):**
   - Extract from Step 0 (B2) if solution-neutral
   - Otherwise, rewrite to remove solution-embedding
   - Add evidence of significance
   - Test: Can someone imagine multiple solutions?

3. **Field of Application (60 chars):**
   - Extract from Step 0 (B4) if specific enough
   - Otherwise, narrow the scope
   - Include boundaries if space allows

---

### Phase 3: Human Resources (5 min)

**Create team table:**

1. List 4-8 key people (founders, executives, advisors)
2. For each, assess:
   - Years of relevant experience
   - Unique credentials or networks
   - Full-time vs. part-time
   - Critical gaps

3. Mark "Differentiator?" as Yes if:
   - Rare expertise (e.g., only 50 people in world with this background)
   - Unique credentials (e.g., Nobel Prize, founded unicorn)
   - Exceptional networks (e.g., direct access to Fortune 500 CEOs)

4. Write Overall Note (250 chars):
   - Summarize key differentiators
   - Acknowledge gaps honestly
   - Note commitment level

---

### Phase 4: Physical/Intellectual Resources (5 min)

**Create resources table:**

1. List 4-10 assets:
   - Patents (owned or licensed)
   - Technology (proprietary vs. standard)
   - Data (unique datasets)
   - Partnerships (exclusive agreements)
   - Facilities/equipment
   - Regulatory approvals

2. Mark "Differentiator?" as Yes if:
   - Proprietary (not available to competitors)
   - Exclusive (unique licensing or partnership)
   - Validated (through research, trials, or commercial use)

3. Write Overall Note (250 chars):
   - IP position (strong, adequate, weak)
   - Dependencies (partnerships, suppliers)
   - Competitive moats

---

### Phase 5: Financial Resources (3 min)

**Create financial table:**

1. List 3-6 resources:
   - Funding raised (by round)
   - Revenue (current, projected)
   - Personal investment
   - Grants or non-dilutive funding

2. Mark "Differentiator?" as Yes if:
   - Unusual source (corporate backing, government program)
   - Strategic value (investor brings partnerships)
   - Self-sustaining (profitable or near-profitable)

3. Write Overall Financial Note:
   - Current runway
   - Revenue status
   - Dependencies

---

### Phase 6: Differentiating Advantages (3 min)

**Synthesize competitive moats (250 chars):**

1. Review all "Differentiator? Yes" items across all tables
2. Select the 2-4 strongest
3. Explain WHY each is hard to replicate
4. Connect to the specific problem

---

### Phase 7: Assessment Summary (10-12 min)

**Calculate Component Scores:**

1. **Problem Definition (1-5):** Use rubric, write 2-3 sentences
2. **Application Domain (1-5):** Use rubric, write 2-3 sentences
3. **Team & Approach (1-5):** Use rubric, write 2-3 sentences
4. **Resources (1-5):** Use rubric, write 2-3 sentences

**Calculate Overall Score:**
- Formula: (Problem + Domain + Team + Resources) ÷ 4
- Example: (5 + 4 + 4 + 4) ÷ 4 = 4.25 → 4.3/5 (Above Average)

**Write Strengths (4-6 bullets):**
- Focus on validated strengths with evidence
- Include specific metrics

**Write Gaps (5-8 bullets):**
- Be brutally honest
- Identify capability gaps
- Note dependencies

**Write Overall Assessment (150-200 words):**
- Is foundation solid?
- Critical dependencies?
- Should it advance?
- Focus areas for next phases?

**Write Risk Factors (4-6 bullets):**
- Founder concentration
- Financial dependencies
- Competitive threats
- Partnership vulnerabilities
- Regulatory uncertainties

**Write Success Factors (4-6 bullets):**
- Specific, actionable items
- Tied to gaps
- Achievable in 6-12 months

---

### Phase 8: Quality Check (2 min)

**Verify:**
- [ ] All character limits respected
- [ ] Scoring calculated correctly
- [ ] Evidence-based (not aspirational)
- [ ] Gaps honestly identified
- [ ] Coherent story across sections
- [ ] Both markdown and DOCX files ready

---

## Integration with VIANEO Framework

**Links from Previous Steps:**

**From Step 0 (Executive Brief):**
- B2 (Problem) → Problem to Solve field
- B4 (Market) → Field of Application
- B6 (Traction) → Evidence of validation
- B7 (Team) → Human Resources table

**From Step 2 (40Q Diagnostic):**
- T1-T9 (Team questions) → Human Resources assessment
- Tech1-Tech11 (Technology questions) → Physical/Intellectual Resources assessment
- M8-M9 (Financial questions) → Financial Resources assessment

**Links to Evidence Log:**
- All claims should cite Evidence IDs (E###) where available
- Team credentials: E### (e.g., E012: LinkedIn profile showing 15+ yrs experience)
- Patents/IP: E### (e.g., E015: Patent filing documentation)
- Financial information: E### (e.g., E020: Investment agreement)

**Feeds into Overall VIANEO Score:**
- Legitimacy Weight: 15%
- If Legitimacy < 3.0, this is a red flag for overall evaluation
- Legitimacy gaps inform Desirability, Acceptability, Feasibility, Viability focus areas

**Feeds Gate A Decision:**
- Legitimacy assessment becomes Appendix D in Gate A Decision Brief
- Low legitimacy scores (< 3.0) may trigger reconsideration before full evaluation
- Identified gaps inform resource requirements and validation priorities

---

## Output Format

**CRITICAL: You must create TWO output files:**

### 1. Markdown File (.md)

**Filename:** `Vianeo_Legitimacy_Worksheet_[ProjectName].md`

**Example:** `Vianeo_Legitimacy_Worksheet_Thinkie_System.md`

**Structure:**
- All sections in markdown format
- Clean table formatting using pipes (|)
- All character limits respected
- Proper headers (#, ##, ###)
- Bullet lists with dashes (-)

---

### 2. Word Document (.docx)

**Filename:** `Vianeo_Legitimacy_Worksheet_[ProjectName].docx`

**Example:** `Vianeo_Legitimacy_Worksheet_Thinkie_System.docx`

**Formatting Requirements:**
- Identical content to markdown version
- Professional formatting:
  - Title: Calibri 14pt Bold
  - Section Headers: Calibri 12pt Bold
  - Body Text: Calibri 11pt Regular
  - Table Headers: Bold, shaded background
  - Tables: Light Grid Accent 1 style
  - Margins: 1" all sides
  - Spacing: 1.15 line spacing, 6pt after paragraphs

**See:** `templates/Step4_Legitimacy_DOCX_Template.md` for complete technical specifications

---

## Common Pitfalls

### Problem Definition Errors
- **Solution-embedding:** "How do we create a mobile app to..." (embeds solution)
  - Fix: "How might we enable [outcome] for [user]?"
- **Too vague:** "Help people be healthier" (no boundaries)
  - Fix: Add specifics about who, what, and evidence
- **Scope creep:** Problem keeps expanding as team learns
  - Fix: Use Step 0 (B2) as anchor, only update if fundamentally changed

### Domain Errors
- **Too broad:** "Healthcare" instead of "Post-acute cognitive rehabilitation"
  - Fix: Add boundaries (age range, geography, condition)
- **Shifting focus:** Started B2C, now pivoting to B2B
  - Fix: Document current domain, note pivot history
- **Mismatched resources:** Attacking complex regulated domain with lightweight team
  - Fix: Lower domain score, note gap in assessment

### Team/Resource Errors
- **Overstating capability:** "World-class team" with no evidence
  - Fix: Use specific metrics (years, achievements, credentials)
- **Ignoring gaps:** Not acknowledging missing functions
  - Fix: List gaps explicitly in assessment summary
- **Claiming differentiators:** Standard experience positioned as unique
  - Fix: Mark "Differentiator? No" unless truly rare

### Character Limit Violations
- **Verbosity:** Using 300 characters when limit is 250
  - Fix: Remove filler, use abbreviations, cut adjectives
- **Over-explaining:** Trying to include everything
  - Fix: Prioritize most important information

---

## Quality Checklist

Before finalizing:

**Problem Quality:**
- [ ] Problem stated without solution embedded
- [ ] Evidence of problem significance included
- [ ] Under 250 characters
- [ ] Clear and specific

**Domain Quality:**
- [ ] Application domain has clear boundaries
- [ ] Under 60 characters
- [ ] Specific enough to be meaningful
- [ ] Appropriate scope for resources

**Resources Quality:**
- [ ] Differentiators clearly marked (Yes/No)
- [ ] All tables properly formatted
- [ ] Overall notes provide synthesis, not repetition
- [ ] Gaps acknowledged honestly
- [ ] Character limits respected throughout

**Assessment Quality:**
- [ ] Legitimacy score calculated correctly (average of 4 components)
- [ ] Category label matches score range
- [ ] Strengths list is evidence-based (4-6 items)
- [ ] Gaps list is comprehensive and honest (5-8 items)
- [ ] Detailed scoring has explanations for each component
- [ ] Overall assessment paragraph is 150-200 words
- [ ] Risk factors are specific and relevant (4-6 items)
- [ ] Success factors are actionable and prioritized (4-6 items)

**Output Quality:**
- [ ] Both markdown and DOCX files created
- [ ] Identical content in both formats
- [ ] Professional formatting in DOCX
- [ ] Filenames follow convention
- [ ] Files open correctly in Word/Docs

---

## Tips for Accurate Scoring

1. **Default skeptical:** Without evidence, score ≤3
2. **Look for proof:** Rare expertise, unique credentials, proprietary IP
3. **Be honest about gaps:** Low scores are valuable signals
4. **Use rubrics:** Don't guess, follow the 1-5 scale definitions
5. **Evidence over aspirations:** "Has 15 yrs experience" not "Will be great at..."
6. **Compare to examples:** Review Thinkie System (4.2) vs. Rayla AI (3.5) scoring

---

## File Naming Conventions

**Markdown:**
- Format: `Vianeo_Legitimacy_Worksheet_[ProjectName].md`
- Example: `Vianeo_Legitimacy_Worksheet_Rayla_AI.md`
- Use underscores for spaces
- Use title case for project names

**DOCX:**
- Format: `Vianeo_Legitimacy_Worksheet_[ProjectName].docx`
- Example: `Vianeo_Legitimacy_Worksheet_Rayla_AI.docx`
- Same naming convention as markdown

---

## Next Step

After completing Step 4, proceed to **Step 5: Desirability Analysis** (prompts/step_05_needs_requesters.md) to evaluate:
- User segments and personas
- Needs statements and validation
- Priority ranking
- Customer discovery evidence

---

**Template Version:** 1.0
**Last Updated:** 2025-01-15
**Compatible With:** VIANEO 13-Step Evaluation System
