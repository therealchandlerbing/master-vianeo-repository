# Prompt: Committee Synthesis Generation

**Version**: 1.0
**Position in Workflow**: Post-Sprint Administrative Step (After Step 12)
**Purpose**: Generate the final Committee Synthesis for a completed Vianeo validation sprint

---

## Overview

This prompt generates the Committee Synthesis deliverable that translates a completed Vianeo 5-dimension assessment into the 4-dimension committee evaluation format for platform submission.

### Output Files

1. **Platform Entry Guide (Markdown):** Scores and comment for direct Vianeo platform input
2. **Professional DOCX Report:** Formatted document for committee presentation

---

## Full Prompt Template

```
You are generating the final Vianeo Committee Synthesis for a startup validation project. This is the culminating deliverable that synthesizes all assessment work into committee-ready scores and recommendations.

## Project Information

**Project Name:** [PROJECT NAME]
**Principal Investigator/Founder:** [NAME, ORGANIZATION]
**Date:** [DATE]
**Maturity Stage:** [e.g., Early Commercialization, TRL 4-5]

## Vianeo Dimension Scores (from completed assessment)

| Dimension | Score | Key Evidence |
|-----------|-------|--------------|
| Legitimacy | X.X/5 | [Brief evidence] |
| Desirability | X.X/5 | [Brief evidence] |
| Acceptability | X.X/5 | [Brief evidence] |
| Feasibility | X.X/5 | [Brief evidence] |
| Viability | X.X/5 | [Brief evidence] |

**Overall Vianeo Score:** X.X/5.0
**Market Maturity Score:** X.X/5.0

## Key Facts for Synthesis

**Team:**
- [Team size and composition]
- [Key expertise areas]
- [Gaps in team structure]

**Technology:**
- [Prototype/product status]
- [Technical validation achieved]
- [IP position]

**Business:**
- [Funding status and amount]
- [Revenue/traction if any]
- [Business model validation status]

**Commercial:**
- [Customer interview count]
- [Pricing validation status]
- [Go-to-market readiness]

**Partnerships:**
- [Key partnerships and status]
- [Regulatory pathway]

## Critical Gaps Identified

1. [Gap 1 with quantification]
2. [Gap 2 with quantification]
3. [Gap 3 with quantification]

## Recommended Actions (from Step 10/12)

1. [Action 1 with owner and timeline]
2. [Action 2 with owner and timeline]
3. [Action 3 with owner and timeline]

---

## Output Requirements

Generate:

1. **Committee Scores (4 dimensions)**
   - Team: X/5 with 2-3 sentence rationale
   - Technology: X/5 with 2-3 sentence rationale
   - Management and Business: X/5 with 2-3 sentence rationale
   - Commercial: X/5 with 2-3 sentence rationale

2. **Diagnostic Comment (4 paragraphs, 6-8 sentences total)**
   - Paragraph 1: Strengths (1-2 sentences)
   - Paragraph 2: Risks (1-2 sentences)
   - Paragraph 3: Near-Term Actions (2-3 sentences with owners/timelines)
   - Paragraph 4: Evidence Gaps (1-2 sentences)

3. **Recommendation**
   - PROCEED / CONDITIONAL PROCEED / PAUSE / DO NOT PROCEED
   - Brief justification

4. **Output Files**
   - Platform Entry Guide (Markdown for copy/paste)
   - Professional DOCX Report (committee presentation)

## Formatting Rules

- Never use em dashes (use commas, periods, parentheses)
- Include specific metrics throughout
- Name owners and timelines for all actions
- State gaps directly without softening
- Use color-coded score indicators in DOCX
```

---

## Minimal Input Version

For quick generation when full data is available in project knowledge:

```
Generate a Vianeo Committee Synthesis for:

**Project:** [Name]
**PI:** [Name, Organization]
**Date:** [Date]

**Vianeo Scores:**
- Legitimacy: X.X/5
- Desirability: X.X/5
- Acceptability: X.X/5
- Feasibility: X.X/5
- Viability: X.X/5
- Overall: X.X/5
- Market Maturity: X.X/5

**Key Facts:**
- [Fact 1]
- [Fact 2]
- [Fact 3]
- [Fact 4]
- [Fact 5]

**Critical Gaps:**
- [Gap 1]
- [Gap 2]
- [Gap 3]

Search project knowledge for additional context and generate Committee Synthesis with platform scores, diagnostic comment, and DOCX report.
```

---

## Score Mapping Guide

### Team Score (Committee) = Average of:
- Legitimacy team assessment (expertise, commitment)
- Feasibility execution capability
- Key question: "Can this team deliver?"

### Technology Score (Committee) = Average of:
- Feasibility technical assessment
- Legitimacy innovation assessment
- Key question: "Is the technology validated and differentiated?"

### Management and Business Score (Committee) = Average of:
- Viability business model assessment
- Acceptability ecosystem assessment
- Key question: "Is the business model sound and the ecosystem supportive?"

### Commercial Score (Committee) = Average of:
- Desirability customer validation
- Viability market assessment
- Key question: "Do customers want this and will they pay?"

---

## Score Level Definitions

### Team Score

| Score | Definition |
|:-----:|------------|
| 5 | World-class expertise, full-time commitment, complete team, proven track record |
| 4 | Strong expertise, committed core team, minor gaps addressable |
| 3 | Adequate expertise, some commitment gaps, notable missing roles |
| 2 | Expertise present but team structure weak, major gaps |
| 1 | Insufficient team for the challenge |

### Technology Score

| Score | Definition |
|:-----:|------------|
| 5 | Production-ready, validated performance, strong IP, clear barriers to entry |
| 4 | Functional prototype, validated in lab, differentiated approach |
| 3 | Proof of concept, some validation, differentiation unclear |
| 2 | Early prototype, limited validation, competitive concerns |
| 1 | Concept only, unproven technology |

### Management and Business Score

| Score | Definition |
|:-----:|------------|
| 5 | Validated business model, strong ecosystem support, clear path to profitability |
| 4 | Defined business model, ecosystem engaged, financial projections reasonable |
| 3 | Business model outlined, some ecosystem validation, financial assumptions untested |
| 2 | Business model unclear, ecosystem engagement minimal, funding uncertain |
| 1 | No viable business model identified |

### Commercial Score

| Score | Definition |
|:-----:|------------|
| 5 | Strong customer traction, validated pricing, clear go-to-market |
| 4 | Customer interest validated, pricing tested, market entry planned |
| 3 | Customer need identified, limited validation, pricing hypothetical |
| 2 | Assumed customer need, no validation, no pricing data |
| 1 | No evidence of customer demand |

---

## Threshold Reference

| Dimension | Vianeo Threshold | Committee Implication |
|-----------|------------------|----------------------|
| Legitimacy | >=3.0 | Affects Team, Technology |
| Desirability | >=3.5 (highest bar) | Affects Commercial heavily |
| Acceptability | >=3.0 | Affects Management and Business |
| Feasibility | >=3.0 | Affects Team, Technology |
| Viability | >=3.0 | Affects Management and Business, Commercial |
| Overall | >=3.2 | Determines recommendation |

---

## Recommendation Logic

| Pattern | Recommendation | Criteria |
|---------|----------------|----------|
| PROCEED | All dimensions >=3/5, overall >=3.2 | Ready for next phase |
| CONDITIONAL PROCEED | Some gaps but addressable within 90 days | Specific validation required |
| PAUSE | Critical gaps requiring pivot or major intervention | Fundamental reassessment needed |
| DO NOT PROCEED | Multiple dimensions <2/5 or fatal flaw identified | Viability concerns |

---

## Common Patterns

### Pattern A: Strong Tech, Weak Commercial
- Team: 4/5, Technology: 4/5, Management: 3/5, Commercial: 2/5
- Recommendation: CONDITIONAL PROCEED
- Key action: Customer discovery sprint

### Pattern B: Strong Team, Weak Business Model
- Team: 4/5, Technology: 3/5, Management: 2/5, Commercial: 3/5
- Recommendation: CONDITIONAL PROCEED
- Key action: Business model validation, financial restructuring

### Pattern C: Balanced Development
- All dimensions 3-4/5
- Recommendation: PROCEED
- Key action: Address specific gaps, prepare for scale

### Pattern D: Fundamental Concerns
- Any dimension 1/5 or multiple at 2/5
- Recommendation: PAUSE or DO NOT PROCEED
- Key action: Pivot assessment, fundamental restructuring

---

## Example Output Structure

See `templates/Committee_Synthesis_Template.md` and `templates/Committee_Synthesis_PlatformEntry.md` for complete output formats.

---

## Diagnostic Comment Writing Guide

### Paragraph 1: Strengths

**Formula:** [Core capability] + [Specific evidence/metrics] + [Key validation achieved]

**Good Example:**
> IRDose demonstrates exceptional technical foundation with a 13+ doctorate research team at IPEN/CNEN, validated clinical problem (20-29% treatment failure in I-131 therapy), and functional TRL 4-5 prototype with FAPESP PIPE funding of R$600,000 secured.

**Bad Example:**
> The team is strong and has good technology.

### Paragraph 2: Risks

**Formula:** [Critical gap] + [Quantification] + [Structural vulnerability]

**Good Example:**
> Critical commercial validation gap with zero customer discovery interviews conducted across eight stakeholder segments. No commercial team members despite world-class technical capabilities, and 100% grant-dependent funding structure.

**Bad Example:**
> Customer validation could be improved and the team could use some commercial experience.

### Paragraph 3: Near-Term Actions

**Formula:** (N) [Action verb + specific outcome]. Owner: [Name]. Timeline: [X days].

**Good Example:**
> (1) Launch 40-60 interview customer discovery sprint across physicians, physicists, patients, and administrators. Owner: Daniel Bonifacio. Timeline: 60 days. (2) Recruit commercial co-founder or advisor with Brazilian medtech experience. Owner: IPEN Leadership. Timeline: 90 days. (3) Develop SUS reimbursement pathway with validated pricing. Owner: Business Advisor TBD. Timeline: 120 days.

**Bad Example:**
> The team should do more customer research and hire some business people.

### Paragraph 4: Evidence Gaps

**Formula:** [What validation is missing] + [Blocking decision it affects]

**Good Example:**
> Customer willingness-to-pay remains entirely hypothetical despite clear technical differentiation. Patient wearability acceptance requires primary research validation before Series A fundraising.

**Bad Example:**
> More evidence would be helpful for investors.

---

## Quality Checklist

Before finalizing output:

- [ ] All 4 committee scores have evidence-based rationale (2-3 sentences each)
- [ ] Diagnostic comment is exactly 4 paragraphs, 6-8 sentences total
- [ ] Each action has specific owner and timeline
- [ ] Recommendation matches score pattern
- [ ] No em dashes used anywhere
- [ ] Specific metrics included throughout (not vague claims)
- [ ] Gaps stated directly without softening language
- [ ] DOCX formatting matches specification
- [ ] Character limits respected for platform compatibility

---

*Prompt Version: 1.0*
*Framework: Vianeo Business Model Evaluation System*
