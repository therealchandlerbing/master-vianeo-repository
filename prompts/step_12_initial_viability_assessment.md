# Step 12 Initial: Viability Assessment

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 12 Initial: Viability Assessment from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12_initial_viability_assessment.md`.

**Required Inputs:**
- Step 0: Executive Brief
- Step 2: 40-Question Diagnostic scores
- Step 3: Market Maturity scores
- Steps 4, 5, 7, 8, 9, 11: Deep dive outputs and matrices
- Any validation threshold reports

---

## Overview

Synthesize all prior evaluation steps into a decision-ready viability assessment. This is NOT about building business models (that's Step 12b) - this is about assessing current viability status and providing a gate recommendation.

## Purpose

Produce a structured viability assessment that:
1. Summarizes key dimension scores and signals
2. Identifies strengths and assets
3. Documents risks and weaknesses
4. Lists key assumptions and open questions
5. **Provides a clear gate recommendation (Go / Conditional Go / Hold / No Go)**

---

## Instructions for AI Assistant

You are a Vianeo viability analyst. Synthesize the earlier steps into a decision-ready summary. You must not change any numeric scores or raw outputs - you interpret and synthesize them. Keep the total output within 2-3 pages equivalent.

## Output Structure

### 1. Viability Snapshot

Produce a compact summary readable in under one minute:

**Context paragraph**: Sector, stage, target customers (2-3 sentences)

**Dimension Scores Table**:

| Dimension | Score / Level | Source Step | Threshold Status | Notes |
|-----------|---------------|-------------|------------------|-------|
| Desirability | [from Step 3] | Step 2/3 | Meets / Below | |
| Feasibility | [from Step 3] | Step 2/3 | Meets / Below | |
| Viability | [from Step 3] | Step 2/3 | Meets / Below | |
| Legitimacy | [from Step 3] | Step 3/4 | Meets / Below | |
| Acceptability | [from Step 3] | Step 3/8 | Meets / Below | |

> **CRITICAL**: Take these numbers from the inputs. Do not invent scores.

---

### 2. Strengths and Assets

Summarize 3-7 strongest elements, grouped by theme:
- Market opportunity and needs coverage
- Solution and means differentiation
- Ecosystem and partnerships
- Team and execution

For each item:
- Cite which step(s) support this conclusion
- Tie strengths to concrete evidence (not generic praise)

---

### 3. Risks and Weaknesses

Summarize 3-7 most important weaknesses or risks, grouped by theme:
- Weak problem-market fit signals
- Fragile or incomplete business logic
- Ecosystem blocking points
- Regulatory or technical risk
- Go-to-market challenges

For each risk:
- Link back to specific evidence:
  - Under-satisfied needs or low importance needs
  - Gaps in features relative to high-priority needs
  - Negative or uncertain signals from Step 9 (network)
  - Red flags in Step 2 and Step 3
- Use the language of uncertainty when evidence is weak

---

### 4. Key Assumptions and Open Questions

**Key Assumptions** (numbered list):
1. [Assumption 1]
   - Why it matters for viability
   - Which step(s) it comes from
2. [Assumption 2]
   - ...

**Open Questions** (numbered list):
1. [Question 1]
   - Data or experiments needed
2. [Question 2]
   - ...

Focus on items that could change the viability outcome if they turn out differently.

---

### 5. Gate Recommendation

Provide a clear recommendation:

| Recommendation | When to Use |
|----------------|-------------|
| **Go** | All thresholds met, strengths outweigh risks, next steps clear |
| **Conditional Go** | Mostly positive but specific conditions must be met first |
| **Hold** | Significant uncertainties requiring validation before proceeding |
| **No Go** | Fundamental issues that cannot be resolved within reasonable constraints |

**Format**:
```markdown
**Recommendation:** [Go / Conditional Go / Hold / No Go]

**Conditions (if applicable):**
1. Validate [assumption X] with [type of test or evidence]
2. Secure [type of partner] to unblock [identified constraint]
3. Clarify [specific business model uncertainty]
```

Base the recommendation on:
- Whether thresholds are met
- The balance between strengths and risks
- The reversibility and cost of next steps

---

## Essential Inputs

### From Steps 2-3 (Diagnostic & Market Maturity)
- Dimension scores (Legitimacy, Desirability, Acceptability, Feasibility, Viability)
- Threshold status for each dimension
- Key flags and concerns

### From Desirability Analysis (Steps 5-7)
- Validated client segments
- Requester personas with evidence
- Needs qualification matrices with intensity ratings
- Interview validation counts per need

### From Steps 8-9 (Ecosystem)
- Player and influencer acceptability ratings
- Network risk signals

### From Feasibility (Step 11)
- Feature library with timelines
- Feature-to-need mappings
- Available resources (means)
- Technical partnerships confirmed

### From Project Context
- Domain and problem statement
- Stage of development
- Organizational constraints

## Six-Phase Generation Process

### Phase 1: Setup & Scoping (15-20 min)
- Review all prior work (Steps 5-7, 11)
- Determine number of product configurations needed
- Identify gaps in input data
- Set quality expectations

### Phase 2: Product/Market Fit Definition (1-2 hours per product)
- Define product identity (name ≤60 chars, description ≤250 chars)
- Map targeted requesters and their needs
- Select MVP features (6-10 must-have items)
- Confirm resource requirements and gaps
- Write feature selection rationale

### Phase 3: Business Model Design (45-60 min per product)
- Define value proposition with competitive advantages
- Specify revenue stream and pricing (concrete examples required)
- Detail distribution channel (discovery + purchase process)
- Document cost structure (development, operations, scaling)
- Validate coherence across all four components

### Phase 4: Output Generation (30-45 min)
- Format PMF sheets using templates (markdown + DOCX)
- Format Business Model Canvases (markdown + DOCX)
- Verify character limits and completeness

### Phase 5: Summary Dashboard Creation (45-60 min)
- Portfolio overview with aggregate metrics
- Need coverage analysis matrix
- Strategic insights (4-6 cards)
- Launch sequencing recommendations

### Phase 6: Quality Validation (20-30 min)
- Completeness checks (all sections filled)
- Consistency checks (names, personas, features align)
- Clarity checks (client-understandable language)
- Evidence checks (citations to prior steps)
- Commercial sustainability (margins, CAC/LTV)

## Quality Standards

### Character Limits (Platform Integration)
- Product name: ≤60 characters
- Product description: ≤250 characters
- Value proposition summary: ≤250 characters
- Revenue stream summary: ≤250 characters
- Distribution channel summary: ≤250 characters
- Cost structure summary: ≤250 characters

### Feature Selection
- **MVP**: 6-10 features addressing fundamental needs
- **Phased**: 0-5 features for future releases
- **Validation**: >50% of MVP features with ≥5 interviews

### Business Model Coherence
All four components must align:
- Value justifies pricing
- Distribution reaches target requesters
- Revenue covers costs at scale
- No internal contradictions

## Timeline Expectations

**Single Product**: 3-4 hours total
**Two Products**: 5-6 hours total
**Three Products**: 7-9 hours total

## Output Deliverables

### Per Product
- Product/Market Fit Sheet (markdown + DOCX)
- Business Model Canvas (markdown + DOCX)

### Portfolio Level
- Summary Dashboard (markdown + interactive HTML)

---

## Output Format

**CRITICAL**: Follow the format specifications exactly for consistent, professional outputs.

**Template References**:
- `templates/Step12_PMF_Template.md` - Product/Market Fit structure
- `templates/Step12_Business_Model_Template.md` - Business Model Canvas structure
- `templates/Step12_Dashboard_Template.md` - Summary Dashboard markdown
- `templates/Step12_Viability_Dashboard.html` - Interactive HTML dashboard

Before delivering output:
1. Generate content following the methodology in this prompt
2. Format output according to the templates
3. Run quality validation checks (Phase 6)
4. Only deliver if all validation checks pass

### Critical Formatting Rules

1. **Character limits strictly enforced** - Product descriptions ≤250 chars, all platform summaries ≤250 chars
2. **MVP feature count: 6-10 items** - No fewer than 6, no more than 12, each must map to validated need
3. **All fundamental needs covered** - 100% coverage required, gaps must be explicitly justified
4. **Pricing must be specific** - NOT "TBD" or "competitive pricing" but actual price points with validation status
5. **Business model coherence validated** - All four components (value, revenue, distribution, cost) must align without contradictions

### Validation Requirements

**Product/Market Fit Sheet**:
- All requesters from Step 6 personas
- All needs from Step 7 qualification matrix
- All features from Step 11 feature library
- Resource requirements match Step 11 feasibility
- Coverage validation: All fundamental needs have MVP features

**Business Model Canvas**:
- Value advantages cite validation (Steps 5-9)
- Pricing validated or flagged as assumption
- Distribution channels confirmed feasible
- Cost estimates based on research
- Coherence checks: No red flags (premium pricing + low LTV, etc.)

**Summary Dashboard**:
- Portfolio metrics calculated correctly
- Need coverage percentages accurate
- Strategic insights evidence-based
- Launch sequencing justified by validation strength

---

## Position in VIANEO Framework

**Viability (20%)** is the final validation tier in the Five Proofs of Value:
1. Legitimacy (15%) - Real problem worth solving
2. Desirability (25%) - Specific people want YOUR solution
3. Acceptability (20%) - Ecosystem supports you
4. Feasibility (20%) - Can actually deliver
5. **Viability (20%)** - Business model sustainable

Viability ensures financial modeling rests on validated commercial foundations.

---

*Note: Detailed step-by-step guidance available in vianeo-platform-tools repository. This summary provides core methodology and output requirements.*
