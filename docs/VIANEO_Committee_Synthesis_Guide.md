# Vianeo Committee Synthesis Guide

> **Position in Workflow:** Post-Sprint Administrative Step (After Step 12)
> **Purpose:** Translate Vianeo assessment outputs into committee-ready evaluation format
> **Time Required:** 20-30 minutes
> **Outputs:** Platform scores, diagnostic comment, professional DOCX report

---

## Overview

The Committee Synthesis is the final administrative deliverable of a Vianeo validation sprint. It bridges the gap between the detailed 5-dimension Vianeo assessment and the 4-dimension committee evaluation format used in the Vianeo platform.

### When to Use

Execute this step when:
- All 13 Vianeo steps (0-12) are complete
- Dimension scores are finalized
- Critical gaps and actions are documented
- Ready to submit to committee for review

### What It Produces

1. **Platform Entry Data:** Scores and comment for direct Vianeo platform input
2. **Professional Report:** DOCX document for committee presentation
3. **Score Rationale:** Evidence-based justification for each dimension

---

## Score Mapping: Vianeo to Committee

The Vianeo 5-dimension system maps to the 4-dimension committee format as follows:

| Committee Dimension | Vianeo Sources | Primary Question |
|---------------------|----------------|------------------|
| **Team** | Legitimacy (team), Feasibility (execution) | Can this team deliver? |
| **Technology** | Feasibility (technical), Legitimacy (innovation) | Is the technology validated? |
| **Management and Business** | Viability, Acceptability (ecosystem) | Is the business model sound? |
| **Commercial** | Desirability, Viability (market) | Do customers want this? |

### Score Calculation Method

**Team Score:**
- Weight Legitimacy team assessment at 60%
- Weight Feasibility execution capability at 40%
- Adjust for critical gaps (no commercial team = cap at 4/5)

**Technology Score:**
- Weight Feasibility technical assessment at 70%
- Weight Legitimacy innovation assessment at 30%
- Adjust for prototype status and IP position

**Management and Business Score:**
- Weight Viability at 60%
- Weight Acceptability at 40%
- Adjust for funding status and regulatory clarity

**Commercial Score:**
- Weight Desirability at 70%
- Weight Viability market assessment at 30%
- Heavily penalize zero customer validation (cap at 2/5 if no interviews)

---

## Diagnostic Comment Structure

The diagnostic comment follows a strict 4-paragraph, 6-8 sentence format:

### Paragraph 1: Strengths (1-2 sentences)
- Lead with strongest validated capabilities
- Include specific metrics (team size, funding amount, prototype status)
- Name key partnerships and institutional backing

**Example:**
> IRDose demonstrates exceptional technical foundation with a 13+ doctorate research team at IPEN/CNEN, validated clinical problem (20-29% treatment failure in I-131 therapy), and functional TRL 4-5 prototype with FAPESP PIPE funding of R$600,000 secured.

### Paragraph 2: Risks (1-2 sentences)
- State critical gaps directly without softening
- Quantify gaps where possible
- Identify structural vulnerabilities

**Example:**
> Critical commercial validation gap with zero customer discovery interviews conducted across eight stakeholder segments. No commercial team members despite world-class technical capabilities, and 100% grant-dependent funding structure.

### Paragraph 3: Near-Term Actions (2-3 sentences)
- Numbered actions with specific owners and timelines
- Format: "[Action]. Owner: [Name/Role]. Timeline: [X days]."
- Prioritize by impact on lowest-scoring dimensions

**Example:**
> (1) Launch 40-60 interview customer discovery sprint across physicians, physicists, patients, and administrators. Owner: Daniel Bonifacio. Timeline: 60 days. (2) Recruit commercial co-founder or advisor with Brazilian medtech experience. Owner: IPEN Leadership. Timeline: 90 days.

### Paragraph 4: Evidence Gaps (1-2 sentences)
- State what validation is missing
- Connect to blocking decisions

**Example:**
> Customer willingness-to-pay remains entirely hypothetical despite clear technical differentiation. Patient wearability acceptance requires primary research validation before Series A fundraising.

---

## Recommendation Framework

Based on scores and threshold analysis:

| Pattern | Recommendation | Criteria |
|---------|----------------|----------|
| **PROCEED** | All dimensions >=3/5, overall >=3.2 | Ready for next phase |
| **CONDITIONAL PROCEED** | Some gaps but addressable within 90 days | Specific validation required |
| **PAUSE** | Critical gaps requiring pivot or major intervention | Fundamental reassessment needed |
| **DO NOT PROCEED** | Multiple dimensions <2/5 or fatal flaw identified | Viability concerns |

---

## Required Inputs

Before generating Committee Synthesis, gather:

### From Step 3 (Market Maturity Assessment)
- All 5 dimension scores with justifications
- Overall weighted score
- Threshold analysis results

### From Step 4 (Legitimacy Worksheet)
- Team expertise and commitment assessment
- Innovation differentiation analysis

### From Step 5 (Needs/Requesters Analysis)
- Validated customer segments
- Need validation evidence

### From Step 7 (Needs Qualification Matrix)
- Customer interview count and findings
- Need prioritization results

### From Step 8 (Players/Influencers Analysis)
- Ecosystem stakeholder mapping
- Partnership status

### From Step 10 (Diagnostic Comment)
- Executive diagnostic summary
- Critical path forward actions
- Evidence gaps identified

### From Step 12 (Viability Assessment)
- Business model validation status
- Financial model assumptions
- PMF score components

### From Sprint Documentation
- Team composition and gaps
- Funding status and runway
- Partnership formalization status
- Customer interview count
- Prototype/product status

---

## Output Specifications

### Platform Entry (Markdown)
- Scores table for platform selection
- Copy/paste diagnostic comment
- Score rationale (2-3 sentences per dimension)

### Professional DOCX Report
- Formatted header with project metadata
- Color-coded score table (green >=4, amber =3, red <=2)
- Structured diagnostic sections
- Overall assessment summary
- Methodology footer with evidence sources

---

## Quality Checklist

Before finalizing Committee Synthesis:

- [ ] All 4 committee scores have evidence-based rationale
- [ ] Diagnostic comment is exactly 4 paragraphs, 6-8 sentences
- [ ] Each action has owner and timeline
- [ ] Recommendation matches score pattern
- [ ] No em dashes used (use commas, periods, parentheses)
- [ ] Specific metrics included throughout
- [ ] Gaps stated directly without softening
- [ ] DOCX formatting is professional and consistent

---

## Common Patterns

### Pattern A: Strong Tech, Weak Commercial
**Typical Scores:** Team 4/5, Technology 4/5, Management 3/5, Commercial 2/5
**Recommendation:** CONDITIONAL PROCEED
**Primary Action:** Customer discovery sprint (40-60 interviews)

### Pattern B: Strong Team, Weak Business Model
**Typical Scores:** Team 4/5, Technology 3/5, Management 2/5, Commercial 3/5
**Recommendation:** CONDITIONAL PROCEED
**Primary Action:** Business model validation, financial restructuring

### Pattern C: Balanced Development
**Typical Scores:** All dimensions 3-4/5
**Recommendation:** PROCEED
**Primary Action:** Address specific gaps, prepare for scale

### Pattern D: Fundamental Concerns
**Typical Scores:** Any dimension 1/5 or multiple at 2/5
**Recommendation:** PAUSE or DO NOT PROCEED
**Primary Action:** Pivot assessment, fundamental restructuring

---

## Integration Notes

### Position in Vianeo Workflow
```
Steps 0-12: Core Vianeo Evaluation Process
    |
    v
Step 10: Diagnostic Comment (internal synthesis)
    |
    v
Step 12: Viability Assessment (business model validation)
    |
    v
[POST-SPRINT] Committee Synthesis <-- YOU ARE HERE
    |
    v
Platform Submission --> Committee Review
```

### Relationship to Other Steps
- **Inputs from:** Steps 3, 4, 5, 7, 8, 10, 12
- **Outputs to:** Vianeo platform, committee reviewers
- **Does not replace:** Step 10 Diagnostic Comment (internal) or Step 12 Viability (detailed)

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

## Score Level Definitions

### Team Score (Committee)

**Score 5:** World-class expertise, full-time commitment, complete team, proven track record
**Score 4:** Strong expertise, committed core team, minor gaps addressable
**Score 3:** Adequate expertise, some commitment gaps, notable missing roles
**Score 2:** Expertise present but team structure weak, major gaps
**Score 1:** Insufficient team for the challenge

### Technology Score (Committee)

**Score 5:** Production-ready, validated performance, strong IP, clear barriers to entry
**Score 4:** Functional prototype, validated in lab, differentiated approach
**Score 3:** Proof of concept, some validation, differentiation unclear
**Score 2:** Early prototype, limited validation, competitive concerns
**Score 1:** Concept only, unproven technology

### Management and Business Score (Committee)

**Score 5:** Validated business model, strong ecosystem support, clear path to profitability
**Score 4:** Defined business model, ecosystem engaged, financial projections reasonable
**Score 3:** Business model outlined, some ecosystem validation, financial assumptions untested
**Score 2:** Business model unclear, ecosystem engagement minimal, funding uncertain
**Score 1:** No viable business model identified

### Commercial Score (Committee)

**Score 5:** Strong customer traction, validated pricing, clear go-to-market
**Score 4:** Customer interest validated, pricing tested, market entry planned
**Score 3:** Customer need identified, limited validation, pricing hypothetical
**Score 2:** Assumed customer need, no validation, no pricing data
**Score 1:** No evidence of customer demand

---

*Document Version: 1.0*
*Last Updated: December 2025*
*Framework: Vianeo Business Model Evaluation System*
