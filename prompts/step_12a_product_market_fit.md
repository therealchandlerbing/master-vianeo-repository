# Step 12a: Product/Market Fit Definition

## Overview

Transform validated customer needs (Steps 5-7) and confirmed capabilities (Step 11) into coherent product configurations. This step generates Product/Market Fit Sheets that form the foundation for business model development.

## Purpose

Define evidence-based product configurations by connecting validated needs with specific features, ensuring complete coverage of fundamental needs and clear resource requirements.

---

## Instructions for AI Assistant

Using validated inputs from Desirability (Steps 5-7) and Feasibility (Step 11), define product configurations. For each product, produce a complete Product/Market Fit Sheet with product identity, targeted requesters, needs addressed, MVP features, phased features, and resource requirements. Ensure 100% coverage of fundamental needs with MVP features. Flag all unvalidated assumptions.

---

## Input Data Requirements

### From Desirability Analysis (Steps 5-7)

**Required**:
- Validated client segments with evidence
- Requester personas (2-4 per product)
- Needs qualification matrix with:
  - Intensity ratings (Fundamental/Important/Secondary)
  - Current satisfaction levels
  - Interview validation counts (>5 interviewed / <5 interviewed / Not yet interviewed)

### From Feasibility Analysis (Step 11)

**Required**:
- Feature library with implementation timelines
  - Already available
  - Short term (0-6 months)
  - Mid term (6-18 months)
  - Long term (18+ months)
- Feature-to-need mappings
- Available means (resources, capabilities)
- Technical partnerships (confirmed or high-confidence)

### From Project Context

**Required**:
- Domain and problem statement (Step 4)
- Value network understanding (Steps 8-9)
- Organizational constraints

---

## Output Structure

For each product configuration, generate:

### 1. Product Identity

**Product Name** (max 60 characters):
- Clear, descriptive name
- Format: What it is + for whom

**Product Description** (max 250 characters):
- What the client understands they're buying
- Format: "[What it is] for [whom], combining [key capabilities], without [pain point]"

**Target Client**:
- Specific client segment from value network

### 2. Targeted Requesters

For each requester (2-4 per product):

- **Profile**: Brief description (role, context, characteristics)
- **Key Characteristics**: 2-3 behaviors or attitudes
- **Primary Needs**: 3-5 needs this product addresses for them

### 3. Primary Needs Addressed

Table format with 5-10 needs:

| # | Need Statement | Intensity | Current Satisfaction | Validation | Requesters |
|---|----------------|-----------|---------------------|------------|------------|
| 1 | [Full need statement from Step 7] | Fundamental | Not at all | >5 interviewed | [Requesters] |
| 2 | [Need statement] | Important | Rather not | <5 interviewed | [Requesters] |

**Coverage Summary**:
- Total needs addressed
- Fundamental/Important/Secondary counts
- Overall validation level

### 4. MVP Features (6-10 items)

Table format:

| Feature Name | Timeline | Needs Covered | Validation | MVP Rationale |
|--------------|----------|---------------|------------|---------------|
| [Feature 1] | Available | [Need 1, 2] | >5 interviewed | [Why MVP] |
| [Feature 2] | Short term | [Need 3] | >5 interviewed | [Why MVP] |

**MVP Summary**:
- Total MVP features (target: 6-10)
- Available now / Short term counts
- High validation (>5) percentage

**MVP Coverage Check**:
- All fundamental needs have MVP features
- All MVP features map to fundamental/important needs
- MVP size is 6-10 features
- Majority (>50%) have >5 interview validation

### 5. Phased Features (0-5 items)

Table format:

| Feature Name | Timeline | Needs Covered | Validation | Phasing Rationale |
|--------------|----------|---------------|------------|-------------------|
| [Feature X] | Mid term | [Need 6] | <5 interviewed | [Why phased] |

### 6. Configuration Rationale

**Core Value Focus** (3-4 sentences):
- Which fundamental need cluster prioritized
- Core capabilities composing MVP
- Validation evidence supporting choices

**Differentiation Strategy** (3-4 sentences):
- Competitive advantages
- Outcomes enabled that alternatives lack
- Satisfaction gaps addressed

**Phasing Logic** (2-3 sentences):
- Why features deferred
- Dependencies and constraints

### 7. Resource Requirements

**Means Required**:
- List 4-6 key resources from Feasibility

**Critical Partners**:
- External partnerships needed for MVP
- Specific contributions from each

**Resource Gaps & Mitigation**:
- Identified gaps with impact assessment
- Mitigation strategies for each

---

## Feature Selection Decision Framework

### Include in MVP if:

1. **Need Coverage**: Addresses fundamental or important need
2. **Validation**: >5 interview support (or strong rationale if <5)
3. **Timeline**: Already available or achievable short term (0-6 months)
4. **Value**: Enables core differentiation OR is table-stakes requirement

### Defer to Phased if:

1. **Need**: Addresses secondary or enhancement needs
2. **Validation**: Limited validation (<5 interviews)
3. **Timeline**: Mid/long term implementation
4. **Value**: Nice-to-have vs. essential

### Exclude if:

1. No validated need mapping
2. Timeline incompatible with go-to-market
3. Resources unavailable
4. Contradicts core positioning

---

## Quality Standards

### Character Limits (Enforced)

- Product name: max 60 characters
- Product description: max 250 characters
- Ensure counts are verified

### Validation Requirements

- All requesters must trace to Step 6 personas
- All needs must trace to Step 7 qualification matrix
- All features must trace to Step 11 feature library
- Coverage: 100% of fundamental needs require MVP features

### Completeness Checks

- [ ] Product identity complete with character counts
- [ ] 2-4 requesters with profiles and needs
- [ ] 5-10 needs with intensity and validation
- [ ] 6-10 MVP features with rationale
- [ ] Phased features documented (or "None")
- [ ] Resource requirements with gaps and mitigation

### Evidence Basis

Every claim must cite source:
- "Based on Step 7 needs matrix..."
- "Step 11 confirms feature availability..."
- "Interview data (X/Y validated) supports..."

---

## Common Pitfalls to Avoid

1. **Feature Bloat**: MVP exceeding 12 features dilutes focus
2. **Unsupported Claims**: All advantages must tie to validated needs
3. **Orphan Needs**: Every fundamental need requires feature coverage
4. **Low Validation MVP**: Majority of MVP should have >5 interviews
5. **Timeline Optimism**: Respect Step 11 feasibility timelines
6. **Missing Gaps**: Document all resource gaps, don't hide uncertainties

---

## Timeline Expectations

**Per Product**:
- PMF Sheet creation: 1-1.5 hours
- Quality validation: 15-20 minutes

**Multi-Product Projects**:
- Add 45-60 minutes per additional product
- Consider shared elements across products

---

## Example Structure (Condensed)

```markdown
# Product/Market Fit Sheet: Thinkie Core

**Product Name**: Thinkie Core (12 chars)
**Description**: AI-powered cognitive training platform for seniors and caregivers, delivering personalized brain exercises with clinical-grade progress tracking. (155 chars)
**Target Client**: Senior care facilities

## Targeted Requesters
1. **Facility Activities Director**: Needs structured, easy-to-implement programs
2. **Adult Children Caregivers**: Needs peace of mind, engagement visibility
3. **Clinical Staff**: Needs objective assessment tools

## MVP Features (8 total)

| Feature Name | Needs Covered | Timeline | MVP Rationale |
|---|---|---|---|
| Personalized exercise engine | Fundamental needs 1,2 | Available | Core to training |
| Progress tracking dashboard | Fundamental need 3 | Short term | Key for caregivers |
| Caregiver notification system | Important needs 4,5 | Short term | Drives engagement |
| Clinical assessment integration | Fundamental need 6 | Short term | Clinical validation |
| [etc.] | | | |

## Resource Requirements
- Mobile development team (secured)
- Clinical advisory partnership (in discussion)
- Gap: HIPAA compliance consultant (mitigation: engage Q1)
```

---

## Output Files

Generate:
- `[ProductName]_PMF_Sheet.md` - Primary deliverable
- `[ProductName]_PMF_Sheet.docx` - If professional formatting requested

Use template: `templates/Step12_PMF_Template.md`

---

## Position in Workflow

**Inputs From**:
- Step 5-7: Validated needs and requesters
- Step 11: Feature library and resources

**Feeds Into**:
- Step 12b: Business Model Definition
- Step 12 Dashboard: Summary visualization
- Step 13: Financial Modeling

---

*This prompt focuses specifically on Product/Market Fit definition. Use Step 12b for Business Model development and Step 12 Dashboard for visualization generation.*
