# Step 12a: Product Market Fit Sheet

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 12a: Product Market Fit Sheet from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12a_product_market_fit.md`.

**Required Inputs:**
- Step 12 Initial: Viability Assessment (with gate recommendation)
- Relevant highlights from Steps 5-7 (Needs, Personas, Qualification)
- Features-Needs and Features-Means matrices (Step 11)
- Resource and partnership information from feasibility analysis

---

## Overview

Create a comprehensive **Product/Market Fit Sheet** that synthesizes desirability (Steps 5-7) and feasibility (Step 11) into a single document that defines the product configuration for a specific client segment.

## Purpose

Document and validate product-market fit by mapping:
- **Who**: Targeted requesters within the client segment
- **What**: Primary needs addressed and their validation levels
- **How**: MVP features that deliver against those needs
- **With What**: Resources and partnerships required

---

## Instructions for AI Assistant

You are a product strategy expert. Based on the desirability and feasibility analysis from prior steps, create a Product/Market Fit Sheet that:

1. Defines the product identity (name, description, target client)
2. Documents market validation from Steps 5-7
3. Specifies the MVP feature configuration from Step 11
4. Identifies resource requirements and gaps
5. Provides validation summary metrics

Use ONLY requesters, needs, and features from the prior steps. Do not invent new entities.

---

## Output Structure

### 1. Product Identity

```markdown
## Product Identity

**Product/Service Name**: [Name - max 60 characters]

**Description** (250 chars max):
[What the client understands they're buying - format: what it is, for whom, key capabilities, without what pain point]

**Target Client**: [Specific client segment from value network]

**Character Count Check**:
- Name: [X]/60 ✓
- Description: [X]/250 ✓
```

---

### 2. Market Validation (from Desirability - Steps 5-7)

#### Targeted Requesters

For each of 2-4 requesters from Step 6 personas:

```markdown
### [Requester Persona Name]

**Profile**: [Brief description - age range, role, context]

**Key Characteristics**:
- [Behavior/attitude 1]
- [Behavior/attitude 2]
- [Pain point/context]

**Primary Needs for This Product**:
- [Need 1 - intensity level]
- [Need 2 - intensity level]
- [Need 3 - intensity level]
```

#### Primary Needs Addressed

Create a table of 5-10 needs from Step 7:

| # | Need Statement | Intensity | Current Satisfaction | Validation | Targeted Requesters |
|---|----------------|-----------|---------------------|------------|---------------------|
| 1 | [Full need statement] | Fundamental | Not at all | >5 interviewed | [Requester 1, 2] |
| 2 | [Full need statement] | Important | Rather not | >5 interviewed | [Requester 1] |

**Need Coverage Summary**:
- **Total Needs Addressed**: [Number]
- **Fundamental**: [Count] needs
- **Important**: [Count] needs
- **Secondary**: [Count] needs
- **Overall Validation Level**: [>5 interviewed for X/Y needs]

---

### 3. Solution Configuration (from Feasibility - Step 11)

#### MVP Features (Must Have)

Define 6-10 MVP features from Step 11:

| Feature Name | Timeline | Needs Covered | Validation Level | MVP Rationale |
|--------------|----------|---------------|------------------|---------------|
| [Feature 1] | Already available | [Need 1, Need 2] | >5 interviewed | [Why MVP] |
| [Feature 2] | Short term (0-6 mo) | [Need 3] | >5 interviewed | [Why MVP] |

**MVP Features Summary**:
- **Total MVP Features**: [Number] *(target: 6-10)*
- **Available Now**: [Count]
- **Short-term (0-6 mo)**: [Count]
- **Mid-term (6-18 mo)**: [Count if any in MVP]
- **High Validation (>5)**: [Count]/[Total]

**MVP Coverage Check**:
- [ ] All fundamental needs have at least one MVP feature
- [ ] All MVP features map to fundamental or important needs
- [ ] MVP size is 6-10 features
- [ ] Majority (>50%) of MVP features have >5 interviews validation

#### Additional Features (Phased - Post-MVP)

| Feature Name | Timeline | Needs Covered | Validation Level | Phasing Rationale |
|--------------|----------|---------------|------------------|-------------------|
| [Feature X] | Mid term (6-18 mo) | [Need 6] | >5 interviewed | [Why phased] |

#### Configuration Rationale

**Why This Feature Set?**

[Paragraph 1: Core Value Focus - 3-4 sentences explaining which fundamental need cluster this configuration prioritizes]

[Paragraph 2: Differentiation & Validation - 3-4 sentences on competitive differentiation]

[Paragraph 3: Phasing Strategy - 2-3 sentences on what's MVP vs. enhancement]

---

### 4. Resource Requirements (from Feasibility - Step 11)

#### Means Required

- **[Resource Category 1]**: [Specific capability]
- **[Resource Category 2]**: [Specific capability]
- **[Resource Category 3]**: [Specific capability]

#### Technical Partners Critical for MVP

- **[Partner Name/Type 1]**: [Specific contribution]
- **[Partner Name/Type 2]**: [Specific contribution]

#### Resource Gaps & Mitigation

**Gap 1**: [Missing capability or uncertainty]
- **Impact**: [How this affects timeline, features, or viability]
- **Mitigation Strategy**: [Plan to address]

---

### 5. Validation Summary

#### Information Reliability

**Overall Validation Strength**:
- MVP features with >5 interviews: [X]/[Total] = [%]
- Fundamental needs with >5 interviews: [X]/[Total] = [%]
- Overall assessment: [Strong/Moderate/Weak validation]

#### Need Coverage

**Coverage Metrics**:
- Fundamental needs coverage: [X]/[Total] = [%]
- Important needs coverage: [X]/[Total] = [%]
- Overall PMF strength: [High/Medium/Low]

#### Feature Readiness

**Implementation Status**:
- Available now: [X] features
- Short-term (achievable 0-6 months): [Y] features
- Mid/long-term: [Z] features
- Readiness assessment: [Ready to start/Needs preparation/Long lead time]

#### Resource Status

**Resource Availability**:
- [ ] All means identified and available
- [ ] Critical partnerships secured or high-confidence
- [ ] Resource gaps have mitigation strategies
- [ ] Overall: [Ready/Prepared with gaps noted/Significant uncertainties]

---

## Input Data Requirements

### From Step 12 Initial
- Viability assessment with gate recommendation
- Strengths and weaknesses analysis

### From Desirability Analysis (Steps 5-7)
- Validated client segments with evidence
- Requester personas (Step 6)
- Needs qualification matrix with opportunity zones (Step 7)

### From Feasibility Analysis (Step 11)
- Features-Needs coverage matrix
- Features-Means mapping
- Resource and capability assessment

---

## Quality Standards

### PMF Sheet Must Include:
- **2-4 Requesters**: From Step 6 personas only
- **5-10 Needs**: From Step 7 with intensity and validation levels
- **6-10 MVP Features**: With clear rationale for inclusion
- **100% Fundamental Need Coverage**: All fundamental needs have at least one MVP feature
- **Resource Assessment**: Available means and gaps documented

### Common Pitfalls to Avoid

1. **Feature bloat**: Keep MVP to 6-10 focused features
2. **Orphan needs**: Ensure all fundamental needs have MVP features
3. **Invented requesters**: Use only personas from Step 6
4. **Missing validation**: Include interview counts and evidence basis
5. **Vague rationale**: Be specific about why features are MVP vs. phased

---

## Timeline Expectations

- Product identity: 10-15 minutes
- Market validation section: 20-30 minutes
- Solution configuration: 30-45 minutes
- Resource requirements: 15-20 minutes
- Validation summary: 10-15 minutes

---

## Output Files

Generate:
- `[ProjectName]_PMF_Sheet.md` - Primary deliverable
- `[ProjectName]_PMF_Sheet.docx` - Professional DOCX version

---

## Position in Workflow

**Inputs From**:
- Step 12 Initial: Viability Assessment with gate recommendation
- Steps 5-7: Needs, personas, and qualification data
- Step 11: Features analysis

**Feeds Into**:
- Step 12b: Business Model per Segment (builds on PMF configuration)
- Step 12 Final: Viability Dashboard
- Executive Report: Product-market fit section

---

*This prompt focuses on documenting product-market fit. After completing the PMF Sheet, proceed to Step 12b for business model development.*
