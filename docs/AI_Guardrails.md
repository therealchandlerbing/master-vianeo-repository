# AI Guardrails for VIANEO Evaluation System

> **Version**: 2.0 | **Last Updated**: November 2025 | **Review Cycle**: Quarterly

## Core Principle

**"AI is an acceleration tool, not a validation tool."**

AI assistants can dramatically speed up analysis, synthesis, and documentation—but they cannot replace primary research, customer interviews, or real-world validation. Every AI-generated insight must be verified against actual evidence before being used in evaluation decisions.

---

## Five Fundamental Rules

### Rule 1: Citation Required
**Every factual claim must cite a specific source or be labeled as unverified.**

- ✅ "According to the pitch deck (p.3), the team has 5 full-time members"
- ✅ "Market size is estimated at $2B [UNVERIFIED - requires external validation]"
- ❌ "The market is growing rapidly" (no source)

### Rule 2: No Fabrication
**Never invent or fabricate citations—state when sources are unavailable.**

- ✅ "No market research was provided in the application materials"
- ✅ "Unable to verify this claim - source not available"
- ❌ "According to industry reports..." (when no reports were reviewed)

### Rule 3: Confidence Levels
**Assign explicit confidence levels to all claims.**

| Level | Label | Meaning | Use When |
|-------|-------|---------|----------|
| **L1** | Internal Only | Based on team's own statements | No external validation |
| **L2** | Partially Validated | Some external evidence | Limited interviews or secondary sources |
| **L3** | Externally Validated | Strong external evidence | 5+ interviews, market data, expert validation |

**Scoring Implications:**
- L1 evidence supports scores of 1-2 only
- L2 evidence supports scores of 2-3
- L3 evidence required for scores of 4-5

### Rule 4: Draft Status
**Mark all AI outputs as drafts until field-validated through primary research.**

Every AI-generated assessment should include:
```
⚠️ DRAFT - AI-ASSISTED ANALYSIS
This assessment requires validation through:
- [ ] Primary source verification
- [ ] Customer/stakeholder interviews
- [ ] Expert review
- [ ] Field testing of assumptions
```

### Rule 5: Disclose Limitations
**Explicitly disclose AI limitations and knowledge gaps.**

AI assistants should acknowledge:
- Information not available in provided materials
- Areas requiring specialized expertise
- Potential biases in analysis
- Confidence boundaries

---

## Quality Assurance Procedures

### Pre-Execution Checklist

Before running any VIANEO evaluation step with AI assistance:

- [ ] All source materials loaded and accessible
- [ ] Guardrails reminder included in prompt
- [ ] Output format specified
- [ ] Validation requirements clear
- [ ] Human reviewer identified

### Post-Execution Validation

After receiving AI-generated output:

- [ ] All citations verified against source materials
- [ ] Confidence levels appropriately assigned
- [ ] No fabricated statistics or quotes
- [ ] Assumptions clearly labeled
- [ ] Gaps and unknowns documented
- [ ] Draft status indicated

### Mandatory Human Oversight

The following decisions **require human validation** and cannot be delegated to AI:

1. **GO/MAYBE/NO recommendations** - Final investment/advancement decisions
2. **Score assignments of 4-5** - High scores require verified external evidence
3. **Red flag determinations** - Critical issues need human judgment
4. **Stakeholder communications** - All client-facing outputs
5. **Action plan commitments** - Resource allocation decisions

---

## Common Pitfalls to Avoid

### 1. Over-Confident Statements
❌ "This solution will definitely succeed in the market"
✅ "Based on available evidence [L2], the solution shows promise, but market validation is incomplete"

### 2. Hallucinated Statistics
❌ "The market is growing at 15% CAGR"
✅ "No market growth data was provided in application materials [requires external validation]"

### 3. Generic Recommendations
❌ "The team should focus on customer acquisition"
✅ "Given the Score 2 on Q7 (customer interviews), immediate action: conduct 10+ discovery interviews with target segment [clinic owners] within 2 weeks"

### 4. Cherry-Picking Evidence
❌ Highlighting only positive signals while ignoring contradictions
✅ "While the team claims strong traction (pitch deck p.5), no supporting metrics were provided [L1 only]"

### 5. Solution Bias in Problem Statements
❌ "The problem is that customers don't have access to our platform"
✅ "The problem is that small clinics spend 15+ hours/week on manual scheduling [validated with 6 clinic owners]"

### 6. Assuming Validation Exists
❌ "The business model has been validated"
✅ "Business model defined but pricing not tested with customers [Score 2, requires validation]"

---

## Step-by-Step Guardrails

### Steps 0-3: Foundation & Screening

| Step | Key Guardrails |
|------|----------------|
| **Step 0: Executive Brief** | Extract only what's stated; flag gaps; no invention |
| **Step 2: 40Q Diagnostic** | Score based on evidence provided; use "Don't Know" when uncertain |
| **Step 3: 29Q Market Maturity** | Require L3 evidence for scores ≥4; conservative scoring |

### Steps 4-9: Deep Dive Validation

| Step | Key Guardrails |
|------|----------------|
| **Step 4: Legitimacy** | Problem must be validated externally, not assumed |
| **Step 5: Needs/Requesters** | Only include requesters with documented evidence |
| **Step 6: Personas** | Validation badges required; no fictional personas |
| **Step 7: Needs Matrix** | Importance/satisfaction from actual interviews only |
| **Step 8: Players/Influencers** | Acceptability ratings based on actual engagement |
| **Step 9: Value Network** | Relationships must be confirmed, not assumed |

### Steps 10-12: Synthesis & Decision

| Step | Key Guardrails |
|------|----------------|
| **Step 10: Diagnostic** | Synthesize only verified findings; flag assumptions |
| **Step 11: Features-Needs** | Features must map to validated needs |
| **Step 12: Viability** | All business model elements require validation status |

---

## Prompt Templates for AI Safety

### Opening Guardrail Prompt
Include at the start of any AI-assisted evaluation:

```
You are assisting with a VIANEO business evaluation. Follow these guardrails:

1. Only cite information from provided materials
2. Assign confidence levels (L1/L2/L3) to all claims
3. Use "UNVERIFIED" or "REQUIRES VALIDATION" for unsupported statements
4. Never invent statistics, quotes, or citations
5. Mark output as DRAFT requiring human validation
6. When uncertain, use conservative scoring (lower score)
7. Explicitly note gaps in available information
```

### Closing Validation Prompt
Include at the end of any AI-assisted evaluation:

```
Before finalizing, verify:
- [ ] All citations traceable to source materials
- [ ] No fabricated statistics or quotes
- [ ] Confidence levels assigned to key claims
- [ ] Assumptions clearly labeled
- [ ] Gaps documented with "REQUIRES VALIDATION"
- [ ] Output marked as DRAFT
```

---

## Ethical Considerations

### Privacy Protection
- Never include personally identifiable information without consent
- Anonymize customer/stakeholder details in examples
- Protect confidential business information

### Bias Awareness
- Recognize potential biases in source materials
- Consider diverse stakeholder perspectives
- Avoid assumptions based on stereotypes
- Flag when sample sizes are too small for conclusions

### Transparency
- Disclose AI involvement in evaluation process
- Maintain audit trail of AI-assisted decisions
- Enable stakeholders to understand basis for conclusions

### Accountability
- Human evaluators remain responsible for final decisions
- AI outputs are advisory, not determinative
- Document rationale for overriding AI recommendations

---

## Continuous Improvement

### Feedback Loop
1. Track instances where AI outputs required significant correction
2. Identify patterns in guardrail violations
3. Update prompts and procedures based on learnings
4. Share best practices across evaluation team

### Quarterly Review
- Assess guardrail effectiveness
- Update for new AI capabilities and limitations
- Incorporate user feedback
- Align with evolving best practices

### Version Control
- Document all changes to guardrails
- Maintain history of prompt templates
- Track evaluation quality metrics over time

---

## Quick Reference Card

### Before AI-Assisted Evaluation
- [ ] Source materials loaded
- [ ] Guardrails included in prompt
- [ ] Human reviewer assigned

### During Evaluation
- [ ] Citations to specific sources
- [ ] Confidence levels (L1/L2/L3)
- [ ] "UNVERIFIED" labels where needed
- [ ] Conservative scoring when uncertain

### After Evaluation
- [ ] All citations verified
- [ ] No hallucinated content
- [ ] Draft status indicated
- [ ] Human review completed

### Red Flags to Watch
- Statistics without sources
- Overly confident language
- Missing confidence levels
- Generic recommendations
- Solution bias in problems

---

**Document Status**: Active
**Maintainer**: VIANEO Framework Team
**Next Review**: Q1 2026
