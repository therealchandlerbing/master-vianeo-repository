# Step 12a: Viability Pathways

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 12a: Viability Pathways from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12a_viability_pathways.md`.

**Required Inputs:**
- Step 12 Initial: Viability Assessment (with gate recommendation)
- Relevant highlights from Steps 5-7 (Needs, Personas, Qualification)
- Ecosystem and Value Network (Step 9)
- Features-Needs and Features-Means matrices (Step 11)

---

## Overview

Based on the viability assessment, propose **multiple concrete pathways** the project could follow to improve or realize viability. This is about strategic alternatives, not product definition.

## Purpose

Explore 2-4 distinct pathways that could change the viability outcome, helping stakeholders understand the range of strategic options available before committing to business model development.

---

## Instructions for AI Assistant

You are a strategic design and viability expert. Based on the viability assessment and earlier steps, propose multiple concrete pathways the project could follow. Do not recommend one pathway as the only choice unless evidence clearly supports that - instead highlight tradeoffs.

## Output Structure

### 1. Viability Context Recap

In 1-2 paragraphs, restate:
- The current viability status (Go / Conditional Go / Hold / No Go)
- The main reasons why (without repeating full Step 12 Initial text)

---

### 2. Pathways Definition

Propose 2-4 pathways. Examples of pathway types:
- **Segment focus**: Narrowing or changing the primary requester segment
- **Need focus**: Focusing on a subset of needs with strongest opportunity
- **Feature adjustment**: Adjusting the feature set for different market positioning
- **Ecosystem strategy**: Changing partnership or ecosystem approach
- **Business model shift**: Altering revenue model or pricing logic

**For each pathway, use this structure:**

```markdown
### Pathway X: [Short name]

**Description**
- What changes relative to the current baseline

**Requester segments in focus**
- [Segment A]
- [Segment B] (if any)

**Viability impact (qualitative)**
- Desirability: [Better / Similar / Worse and why]
- Feasibility: [Better / Similar / Worse and why]
- Viability (economics): [Better / Similar / Worse and why]

**Key advantages**
- [Advantage 1]
- [Advantage 2]

**Key risks and constraints**
- [Risk 1]
- [Risk 2]

**Evidence and open questions**
- Which steps support this pathway
- What we still need to validate
```

Base all reasoning on data already available. Do not assume new technology or partners unless clearly indicated as assumptions.

---

### 3. Pathways Comparison Table

Create a summary table:

| Pathway | Main Change Focus | Main Segment(s) | Relative Viability | Main Risks |
|---------|-------------------|-----------------|-------------------|------------|
| Pathway 1 | [e.g., segment] | [segment(s)] | [Higher / Similar] | [1-2 main risks] |
| Pathway 2 | [e.g., feature] | [segment(s)] | [Higher / Lower] | ... |
| ... | ... | ... | ... | ... |

Keep this table concise for direct reuse in Executive Report.

---

## Input Data Requirements

### From Step 12 Initial
- Viability assessment with gate recommendation
- Strengths and weaknesses analysis
- Key assumptions and open questions

### From Desirability Analysis (Steps 5-7)
- Validated client segments with evidence
- Requester personas
- Needs qualification matrix with opportunity zones

### From Ecosystem (Steps 8-9)
- Player and influencer landscape
- Value network relationships
- Acceptability ratings

### From Features Analysis (Step 11)
- Features-Needs coverage
- Features-Means mapping
- Resource and capability assessment

---

## Quality Standards

### Pathways Must Be:
- **Distinct**: Each pathway represents a meaningfully different strategic direction
- **Evidence-based**: Grounded in data from prior steps, not aspirational
- **Actionable**: Clear enough to inform business model development
- **Comparable**: Use consistent structure for easy decision-making

### Common Pitfalls to Avoid

1. **Single pathway bias**: Present genuine alternatives, not one preferred option
2. **Ungrounded optimism**: Base viability impact on evidence, not hope
3. **Missing tradeoffs**: Every pathway has downsides - document them
4. **Invented segments**: Use only segments from Steps 5/6
5. **Vague descriptions**: Be specific about what changes

---

## Timeline Expectations

- Viability context recap: 10-15 minutes
- Pathways definition: 30-45 minutes per pathway
- Comparison table: 10-15 minutes

---

## Output Files

Generate:
- `[ProjectName]_Viability_Pathways.md` - Primary deliverable
- `[ProjectName]_Viability_Pathways.docx` - If professional formatting requested

---

## Position in Workflow

**Inputs From**:
- Step 12 Initial: Viability Assessment with gate recommendation
- Steps 5-7: Needs and segment data
- Steps 8-9: Ecosystem analysis
- Step 11: Features analysis

**Feeds Into**:
- Step 12b: Business Model per Segment (informed by chosen pathway)
- Step 12 Final: Viability Dashboard
- Executive Report: Strategic options section

---

*This prompt focuses on exploring strategic pathways. After pathway exploration, proceed to Step 12b for segment-specific business model development.*
