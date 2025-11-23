# STEP 10: Vianeo Diagnostic Comment & Report

**Time Required:** 25-35 minutes (10-15 min content creation, 5-10 min quality validation, 5 min format verification, 3-5 min final review)
**Output:** TWO documents - (1) Markdown Diagnostic Comment, (2) Professional DOCX Report
**Prerequisites:** Steps 2-5 recommended (40Q Diagnostic, 29Q Market Maturity, Legitimacy Worksheet, Desirability Analysis); Steps 6-9 optional but enhance insights

---

## Overview

Step 10 transforms your complete Vianeo assessment into an executive-ready diagnostic comment that synthesizes findings into actionable insights for stakeholders and investors.

**Philosophy:** Every sentence must add unique value. This is NOT a comprehensive report—it's a concise diagnostic (6-8 sentences) that highlights validated strengths, critical risks, immediate actions with owners, and material evidence gaps. Think "executive briefing" not "detailed analysis."

**Key Principle:** Conciseness over comprehensiveness, specificity over abstraction, actionability over analysis, evidence-based over aspirational.

---

## Why Diagnostic Comments Matter

Many assessments fail to drive decisions because they:
- Bury insights in lengthy reports
- Use generic language that could apply to any business
- Fail to assign clear ownership for actions
- Confuse evidence gaps with actual risks
- Downplay problems with hedging language

**This framework prevents that failure.** By distilling assessment findings into 6-8 specific, actionable sentences with professional formatting, you create a document that investors and stakeholders will actually read and act upon.

---

## Required Inputs

### Essential Data
- **Vianeo dimension scores** (Legitimacy, Desirability, Acceptability, Feasibility, Viability) from Step 3
- **Supporting evidence** from assessments (40Q diagnostic, legitimacy worksheet, needs analysis)
- **Interview data and reliability ratings** from Step 5
- **Team composition and resource information** from Steps 2 and 4
- **Identified information gaps** from all worksheets

### Optional Enhanced Data
- **Validated personas** from Step 6
- **Needs qualification matrix** from Step 7
- **Ecosystem mapping** from Steps 8-9
- **Financial position and runway data**
- **Competitive analysis and market validation data**

---

## Output Structure: TWO-FILE PACKAGE

### Output 1: Markdown Diagnostic Comment

**File Name:** `[ProjectName]_Vianeo_Diagnostic_Comment.md`

**Save Location:** `/mnt/user-data/outputs/`

Clean, portable format for version control and internal review containing:
- Title section with metadata (date, framework, maturity stage)
- **Executive Diagnostic** (6-8 sentences across 4 paragraphs)
  - Strengths (1-2 sentences)
  - Risks (1-2 sentences)
  - Near-term Actions (2-3 sentences)
  - Evidence Gaps (1-2 sentences)
- **Dimension Summary Table** (5 dimensions with scores and interpretations)
- **Critical Path Forward** (4 time horizons: Immediate/Short-term/Medium-term/Success Metrics)
- **Footer Metadata** (methodology, evidence sources, next review)

**Use for:** Internal reference, team discussions, version control, iteration

### Output 2: Professional DOCX Report

**File Name:** `[ProjectName]_Vianeo_Diagnostic_Comment.docx`

**Save Location:** `/mnt/user-data/outputs/`

Executive-ready format with professional design elevation:
- Professional typography scale (24pt/16pt/14pt/11pt)
- Strategic color palette (deep blue headers, semantic table colors)
- Generous spacing (1" margins, proper paragraph spacing)
- Formatted tables with color-coded scores
- Consistent styling throughout

**Use for:** Stakeholder presentations, investment discussions, board meetings, committee evaluations

---

## Generation Process (Follow Exactly)

### Phase 1: Data Collection (5-10 minutes)

Use project_knowledge_search to gather:

1. **Dimension Scores and Justifications**
   ```
   Query: "Vianeo assessment scores legitimacy desirability acceptability feasibility viability [project name]"
   ```

2. **Validation Evidence**
   ```
   Query: "customer interviews beta users paying customers revenue traction [project name]"
   ```

3. **Team and Resources**
   ```
   Query: "team composition founder expertise advisors resources IP patents [project name]"
   ```

4. **Risk Factors**
   ```
   Query: "risks gaps dependencies uncertainties assumptions [project name]"
   ```

5. **Evidence Gaps**
   ```
   Query: "missing information validation needed evidence gaps [project name]"
   ```

### Phase 2: Content Synthesis (10-15 minutes)

#### Paragraph 1: Strengths (1-2 sentences)
**Objective:** Highlight validated assets and competitive advantages.

**Process:**
1. Review all dimension scores ≥3.5
2. Identify top 3-4 differentiating advantages
3. Extract specific evidence (numbers, names, metrics)
4. Lead with strongest validation
5. Combine into 1-2 dense, specific sentences

**Quality Checks:**
- Every claim backed by assessment data?
- Specific numbers included (not "some" or "several")?
- Names of people, partners, technologies included?
- Leading with strongest validation first?
- No generic statements ("team seems capable")?

**Example:**
"Rayla AI demonstrates strong technical differentiation with patent-pending multi-model orchestration and grant-specific training data, creating barriers difficult for generic AI competitors to replicate. Founder brings rare 10+ year domain expertise in grant strategy, validated through prior service clients who secured millions in funding."

#### Paragraph 2: Risks (1-2 sentences)
**Objective:** Identify critical vulnerabilities that threaten viability.

**Process:**
1. Review all dimension scores ≤3.0
2. Identify systemic issues (not minor gaps)
3. Prioritize by impact on viability
4. Quantify whenever possible
5. Be direct and specific

**Quality Checks:**
- Focusing on systemic issues, not minor gaps?
- Risks quantified where possible?
- Connected to specific dimension scores?
- Direct language (not hedging with "may" or "might")?
- Prioritized by impact (highest first)?

**Example:**
"Revenue model remains entirely unvalidated with zero paying customers despite operational beta, indicating critical pricing and willingness-to-pay uncertainty. Team structure creates execution risk: CTO lacks distinctive AI/ML credentials, development outsourced to contractors, no technical co-founder, and missing nonprofit executive or regulatory expertise."

#### Paragraph 3: Near-term Actions (2-3 sentences)
**Objective:** List 3-4 concrete actions with responsible owners.

**Process:**
1. Identify actions that address critical risks
2. Prioritize by urgency and impact
3. Assign responsible owner (use actual names from team data)
4. Make delegation-ready (specific, time-bound)
5. Ensure each action has clear outcome

**Quality Checks:**
- Each action has responsible owner in parentheses?
- Actions are specific and measurable?
- Time-bound (30-60 day window)?
- Addresses critical risks or capitalizes on strengths?
- Delegation-ready language?

**Example:**
"Shawna should immediately convert 20+ beta users to paid subscriptions (target 40% conversion rate) to validate $20-50 ARPU pricing hypothesis and establish first revenue proof point. Leadership team (Shawna, Soufiane) must conduct 40-60 structured customer interviews (5-10 per segment) using standardized protocol to validate needs qualification matrix and refine ICP."

#### Paragraph 4: Evidence Gaps (1-2 sentences)
**Objective:** Note missing validation that limits decision-making confidence.

**Process:**
1. Review "information gaps" from all assessments
2. Filter to material gaps only (not minor documentation issues)
3. Group by category (customer, competitive, financial, team, ecosystem)
4. Be specific about what's missing and why it matters
5. Focus on gaps affecting scoring confidence

**Quality Checks:**
- Gaps are material, not nitpicking?
- Specific about what's missing (not "more research needed")?
- Clear why gap matters for decision-making?
- Grouped logically by category?
- No repetition of information from Risks paragraph?

**Example:**
"Customer interview methodology completely undocumented (sample sizes unclear, no validated needs prioritization framework, buyer vs. user distinction unmapped). Competitive intelligence lacks depth: no firsthand testing of Instrumentl or Grantable, pricing comparison incomplete, feature parity unassessed, churn drivers unknown."

### Phase 3: Dimension Summary Table

Create table with exact structure:

| Dimension | Score | Interpretation |
|-----------|-------|----------------|
| **Legitimacy** | X.X/5 | [Status] - [Brief explanation] |
| **Desirability** | X.X/5 | [Status] - [Brief explanation] |
| **Acceptability** | X.X/5 | [Status] - [Brief explanation] |
| **Feasibility** | X.X/5 | [Status] - [Brief explanation] |
| **Viability** | X.X/5 | [Status] - [Brief explanation] |

**Status mapping:**
- 4.5-5.0 → Strong
- 3.5-4.4 → Promising
- 3.0-3.4 → Developing
- 2.0-2.9 → Problematic
- <2.0 → Non-viable

**Add overall status statement:**
"Overall Status: [Status category] requiring [what's needed]. [Key trade-off or balance]."

### Phase 4: Critical Path Forward

**Structure with 4 time horizons:**

**Immediate Priority (Weeks 1-4):**
- 3 actions maximum
- Most urgent items addressing critical risks

**Short-term Priority (Months 2-3):**
- 4 actions maximum
- Focus on validation and capability building

**Medium-term Priority (Months 4-6):**
- 4 actions maximum
- Strategic positioning and infrastructure

**Success Metrics:**
- 6 metrics maximum
- Specific, measurable thresholds
- Timeframes where applicable

### Phase 5: Create Markdown Output

Follow the template exactly:
- See `templates/Step10_Diagnostic_Markdown_Template.md`
- Save to `/mnt/user-data/outputs/[ProjectName]_Vianeo_Diagnostic_Comment.md`

### Phase 6: Create DOCX Output

**CRITICAL: Read DOCX documentation first**
1. Read `/mnt/skills/public/docx/docx-js.md` COMPLETELY
2. Review `docs/VIANEO_Diagnostic_DOCX_Formatting.md` for design specifications
3. Verify all style definitions match specifications
4. Test color codes and measurements

**Apply professional formatting:**
- Typography: 24pt/16pt/14pt/11pt scale
- Colors: Deep blue (#1B365D) headers, semantic table colors
- Spacing: 1" margins, 1.6x line height
- Tables: Color-coded scores (green ≥3.5, yellow 3.0-3.4, red <3.0)

**Generate using docx-js:**
- Save to `/mnt/user-data/outputs/[ProjectName]_Vianeo_Diagnostic_Comment.docx`

### Phase 7: Quality Validation (5-10 minutes)

Before delivery, verify using the quality checklist:

**Content Quality:**
- [ ] 6-8 sentences total in Executive Diagnostic
- [ ] Every sentence adds unique value
- [ ] All claims backed by assessment data
- [ ] Specific numbers, names, concrete examples used
- [ ] Actions have owners and timeframes
- [ ] Evidence gaps are material

**Format Quality:**
- [ ] Markdown follows template exactly
- [ ] DOCX applies professional styling consistently
- [ ] Both outputs contain identical content
- [ ] No em dashes used anywhere
- [ ] Tables formatted correctly
- [ ] All lists use proper formatting

**Accuracy:**
- [ ] Dimension scores match source assessments
- [ ] Evidence sources correctly cited
- [ ] Owner names match team roster
- [ ] Timeframes are realistic
- [ ] Metrics are measurable

**The Five Essential Questions:**
1. **Actionable?** Can someone read this and know exactly what to do?
2. **Specific?** Is this clearly about THIS business, not any business?
3. **Balanced?** Does it acknowledge both strengths AND real problems?
4. **Evidence-based?** Is every claim supported by assessment data?
5. **Concise?** Could any sentence be cut without losing meaning?

If "no" to any question, revise before delivering.

---

## Key Principles

### 1. Conciseness Over Comprehensiveness
- 6-8 sentences total across 4 paragraphs in Executive Diagnostic
- Every sentence must add unique value
- Remove all redundancy and generic statements

### 2. Specificity Over Abstraction
- Use numbers, names, concrete examples
- "50+ beta users, zero revenue" not "early traction"
- "Shawna" and "Soufiane" not "the team"

### 3. Actionability Over Analysis
- Each action has responsible owner in parentheses
- Time-bound recommendations (30-60 days)
- Clear success metrics with specific thresholds

### 4. Evidence-Based Over Aspirational
- Only cite validated findings from assessments
- Flag gaps honestly in Evidence section
- Distinguish between proven and assumed

---

## Common Pitfalls to Avoid

**Content Mistakes:**
- ❌ Mixing aspirations with validated strengths
- ❌ Using generic praise or criticism
- ❌ Actions without owners
- ❌ Downplaying real problems
- ❌ Confusing evidence gaps with risks

**Format Mistakes:**
- ❌ Using em dashes (use commas or parentheses instead)
- ❌ Inconsistent styling between markdown and DOCX
- ❌ Missing table borders or colors
- ❌ Incorrect heading hierarchy
- ❌ Poor paragraph spacing

**Process Mistakes:**
- ❌ Skipping data collection phase
- ❌ Not reading DOCX documentation first
- ❌ Failing to validate against checklist
- ❌ Delivering only one output format
- ❌ Not using project_knowledge_search

---

## Delivery Protocol

**Standard delivery message:**
```
[View your markdown diagnostic](computer:///mnt/user-data/outputs/[filename].md)
[View your professional diagnostic document](computer:///mnt/user-data/outputs/[filename].docx)

Overall Status: [Brief status summary]
Key priorities: [Top 3 priorities with timeframes]
```

**Do not include:**
- Process explanation
- Design rationale
- Technical details
- Tool usage description

Present only the results unless specifically asked about process.

---

## Supporting Documentation

**Complete Reference Files:**
- Skill Overview: `docs/VIANEO_Diagnostic_Skill.md` (READ THIS FIRST)
- Generation Instructions: `docs/VIANEO_Diagnostic_Prompt.md` (detailed process)
- Decision Support: `docs/VIANEO_Diagnostic_Reference.md` (matrices and guidelines)
- Template Structure: `docs/VIANEO_Diagnostic_Template.md` (exact output format)
- DOCX Formatting: `docs/VIANEO_Diagnostic_DOCX_Formatting.md` (technical specs)
- Examples Library: `docs/VIANEO_Diagnostic_Examples.md` (good/bad examples)
- Quality Checklist: `docs/VIANEO_Diagnostic_Quality_Checklist.md` (pre-delivery validation)

**Templates:**
- Markdown Template: `templates/Step10_Diagnostic_Markdown_Template.md`
- DOCX Format Spec: `templates/Step10_Diagnostic_DOCX_Template.md`

---

## Quality Standards

Before delivery, every diagnostic must:
- ✓ Be actionable (reader knows what to do next)
- ✓ Be specific (clearly about THIS business)
- ✓ Be balanced (strengths AND problems acknowledged)
- ✓ Be evidence-based (claims supported by data)
- ✓ Be concise (no removable sentences)

---

## Integration with Other Steps

This step synthesizes insights from:
- **Step 2:** 40Q diagnostic scores (Team/Technology/Management/Commercial)
- **Step 3:** 29Q market maturity dimension scores
- **Step 4:** Legitimacy deep dive (problem validation, team expertise)
- **Step 5:** Desirability analysis (customer interviews, needs validation)
- **Step 6:** Persona development (validated customer segments)
- **Step 7:** Needs qualification matrix (priority opportunities)
- **Step 8:** Players & influencers (ecosystem readiness)
- **Step 9:** Value network map (strategic partnerships)

---

## Time Budget

- **Data collection:** 5-10 minutes
- **Content synthesis:** 10-15 minutes
- **Quality validation:** 5-10 minutes
- **Format verification:** 5 minutes
- **Final review:** 3-5 minutes
- **Total:** 25-35 minutes for complete diagnostic

---

## Red Flags Checklist

If ANY of these are present, revise immediately:

**Content Red Flags:**
- [ ] Generic praise ("team seems capable", "promising opportunity")
- [ ] Hedging language ("may", "might", "possibly", "could")
- [ ] Actions without owners
- [ ] Vague risks ("some concerns", "needs work")
- [ ] Evidence gaps that are actually risks
- [ ] Mixing aspirations with validated strengths

**Format Red Flags:**
- [ ] Em dashes used (— character)
- [ ] Inconsistent formatting between outputs
- [ ] Missing table borders or colors
- [ ] Incorrect heading hierarchy
- [ ] Unicode bullets instead of proper lists
- [ ] Poor paragraph spacing

**Quality Red Flags:**
- [ ] Longer than 8 sentences in Executive Diagnostic
- [ ] Generic statements that apply to any business
- [ ] Missing specific numbers in Strengths
- [ ] Downplayed or buried risks
- [ ] Unverified claims or data
- [ ] Contradictions between sections

---

## Example Use Cases

### For Investors/Stakeholders
- Initial assessment of investment opportunity
- Due diligence documentation
- Board presentation materials
- Investment committee briefings

### For Founders/Teams
- Strategic planning and prioritization
- Gap analysis and action planning
- Fundraising preparation
- Milestone tracking

### For Accelerators/Advisors
- Portfolio company assessment
- Mentoring and guidance
- Progress evaluation
- Resource allocation decisions

---

**Remember:** This diagnostic is often the first impression investors or stakeholders get. Quality, clarity, and professionalism matter significantly. Take the time to get it right.

**Next Steps After Completion:**
1. Share both outputs with stakeholders
2. Use Critical Path as 30-60-90 day roadmap
3. Schedule next review based on trigger events
4. Track progress on Success Metrics
5. Reassess after validation milestones achieved
