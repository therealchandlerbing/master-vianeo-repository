# STEP 12a: Product/Market Fit Definition

**Purpose**: Define product configurations connecting validated customer needs to specific offerings
**Output**: Product/Market Fit Sheet (Markdown + DOCX)
**Time**: 1-2 hours per product
**Part of**: Step 12 Viability Assessment

---

## When to Use This Prompt

Use after completing:
- ✅ Step 5-7 (Desirability): Validated client segments, personas, and needs
- ✅ Step 11 (Feasibility): Feature library, resources, technical partnerships
- ✅ Step 12 Phase 1: Scoping complete, ready to define product configurations

---

## Required Inputs

### From Desirability Analysis (Steps 5-7)
- Client segment definition
- Requester personas (validated with evidence)
- Needs qualification matrix (intensity, satisfaction, validation)
- Interview validation counts per need

### From Feasibility Analysis (Step 11)
- Feature library with implementation timelines
- Feature-to-need mappings
- Available resources (means)
- Technical partnerships confirmed

### From Project Context
- Domain and problem statement
- Stage of development
- Organizational constraints

---

## Product/Market Fit Sheet Structure

### 1. Product Identity

**Product Name** (≤60 characters)
- Client-facing name (not internal code name)
- Memorable and descriptive
- Example: "HealthCare Compliance Hub" not "HCC-Platform-v2"

**Product Description** (≤250 characters)
- Format: "[What it is] for [who] combining [key capabilities]"
- Example: "Compliance automation platform for healthcare providers combining audit preparation, regulatory tracking, and staff training in a single dashboard."

**Character count validation**: Verify both limits respected.

---

### 2. Targeted Requesters

Select 2-4 personas from Step 6 that this product serves.

For each persona:

**Persona Name**: [From Step 6]
**Profile**: [Brief description - 1 sentence]
**Key Characteristics**: [2-3 defining traits]
**Primary Needs**: [Top 3-5 needs this product addresses for this persona]

**Example**:
```
Persona: Sarah - Compliance Director
Profile: Mid-size hospital compliance officer managing regulatory requirements
Key Characteristics: Detail-oriented, time-pressured, audit-focused
Primary Needs:
- Automate audit preparation (reduce 40-hour process)
- Track regulatory changes across 15 frameworks
- Train staff on compliance requirements
```

---

### 3. Primary Needs Addressed

Create a table of 5-10 needs this product addresses:

| Need Statement | Intensity | Current Satisfaction | Validation | Requesters Affected |
|---------------|-----------|---------------------|------------|-------------------|
| [Need from Step 7] | Fundamental/Important/Secondary | Low/Medium/High | [# interviews] | [Persona names] |

**Intensity Levels**:
- **Fundamental**: Core problem, product fails without addressing this
- **Important**: Significant value, enhances product significantly
- **Secondary**: Nice-to-have, deferred to later phases

**Validation Levels**:
- Strong: ≥5 interviews
- Medium: 3-4 interviews
- Weak: 1-2 interviews
- Assumption: 0 interviews (flagged for validation)

**Example Row**:
```
| Automate audit prep | Fundamental | Low (1.5/5) | 8 interviews | Sarah, Mike, Jennifer |
```

---

### 4. Product Features

#### MVP Features (6-10 items - "Must Have")

For each feature:

**Feature Name**: [From Step 11 Feature Library]
**Addresses Need(s)**: [Which needs from table above]
**Timeline**: [Implementation estimate from Step 11]
**Validation Level**: [# interviews supporting this feature]

**Selection Criteria for MVP**:
- ✅ Addresses fundamental or important needs
- ✅ Strong validation (≥5 interviews preferred)
- ✅ Feasible within available resources (per Step 11)
- ✅ Short-term timeline (≤6 months)
- ✅ Provides differentiation vs. alternatives

**Example**:
```
Feature: Automated Audit Checklist Generator
Addresses Needs: Automate audit prep, Track regulatory changes
Timeline: 3 months (per Step 11)
Validation Level: 8 interviews (strong)
```

#### Phased Features (0-5 items - "Future Releases")

Features deferred to post-MVP phases:

**Feature Name**: [From Step 11]
**Addresses Need(s)**: [Which needs]
**Why Phased**: [Rationale for deferral]
**Target Phase**: [Phase 2, Phase 3, Future]

**Deferral Reasons**:
- Important needs, but longer timeline
- Secondary needs (not critical for MVP)
- Dependent on partnerships not yet confirmed
- Requires MVP validation first

**Example**:
```
Feature: AI-Powered Regulation Summarization
Addresses Needs: Track regulatory changes
Why Phased: Requires ML partnership validation (6-9 month timeline)
Target Phase: Phase 2 (post-MVP launch)
```

---

### 5. Feature Selection Rationale

Write 3 paragraphs explaining feature choices:

**Paragraph 1: Core Value Focus** (3-5 sentences)
- What is the primary value proposition?
- Which fundamental needs does the MVP prioritize?
- Why these needs first?

**Example**:
```
The MVP focuses on automating the audit preparation workflow, addressing the most time-intensive aspect of compliance management (40+ hours per audit cycle). This fundamental need scored highest in intensity (4.8/5 average) across 8 interviews and represents the clearest differentiation from existing tools. By reducing audit prep time by 80%, the product delivers immediate, measurable ROI that justifies adoption.
```

**Paragraph 2: Differentiation Strategy** (3-5 sentences)
- What makes this configuration unique vs. alternatives?
- Which validated advantages (from Step 8-9) inform feature selection?
- How do features create competitive moats?

**Example**:
```
Unlike general compliance software (which requires extensive configuration), our MVP includes pre-built templates for the 15 most common healthcare frameworks, validated through partnerships with 3 regulatory consulting firms. This "out-of-box readiness" addresses the primary pain point identified in Step 5: compliance officers lack time for complex software setup. Competitors require 2-3 months for configuration; our MVP deploys in 2 weeks.
```

**Paragraph 3: Phasing Logic** (3-5 sentences)
- Why were certain features deferred?
- What validation or resources do phased features require?
- What's the sequencing rationale?

**Example**:
```
AI-powered regulation summarization, while highly desired (requested in 6/8 interviews), requires ML partnership validation and extends timeline by 6 months. By launching the MVP with manual regulatory updates (still faster than current process), we can validate willingness-to-pay and gather training data for the AI model. This phased approach reduces upfront risk while preserving the path to full automation.
```

---

### 6. Resource Requirements

#### Required Means (from Step 11)

List critical resources needed:

**Technical**:
- [Development resources, infrastructure, tools]
- Example: "3 backend engineers (6 months), AWS hosting ($2k/month), HIPAA-compliant storage"

**Human**:
- [Team composition, expertise required]
- Example: "Compliance subject matter expert (part-time consultant), UX designer (3 months)"

**Financial**:
- [Development budget, operational costs]
- Example: "$180k development budget, $50k/year operational costs"

**Partnerships**:
- [Critical external relationships]
- Example: "Regulatory consulting firm partnership (content validation), HIPAA compliance auditor (security certification)"

#### Identified Gaps & Mitigation

For any resource shortfalls:

| Gap | Impact | Mitigation Strategy | Status |
|-----|--------|-------------------|--------|
| [Resource needed] | [Risk if not resolved] | [How to address] | [In progress/Planned/Blocked] |

**Example**:
```
| Gap: HIPAA compliance expertise | Impact: Cannot launch without certification | Mitigation: Engage compliance auditor (budgeted $25k) | Status: In progress (3 firms contacted) |
```

---

### 7. Coverage Validation

Create a matrix confirming all fundamental needs have feature coverage:

| Fundamental Need | MVP Feature(s) Addressing | Coverage Status |
|-----------------|------------------------|----------------|
| [Need 1] | [Feature A, Feature B] | ✅ Complete |
| [Need 2] | [Feature C] | ⚠️ Partial |
| [Need 3] | — | ❌ Gap (flagged) |

**Coverage Levels**:
- ✅ **Complete**: Multiple features address need fully
- ⚠️ **Partial**: One feature addresses need, but gaps remain
- ❌ **Gap**: Fundamental need without MVP feature (must justify or add feature)

**Rule**: All fundamental needs must have ✅ Complete or ⚠️ Partial coverage. Gaps require explicit justification.

---

## Quality Checks

Before finalizing Product/Market Fit sheet:

### Completeness
- [ ] Product identity defined (name ≤60 chars, description ≤250 chars)
- [ ] 2-4 targeted requesters specified
- [ ] 5-10 primary needs listed with intensity and validation
- [ ] 6-10 MVP features selected and mapped to needs
- [ ] 0-5 phased features documented (if applicable)
- [ ] 3-paragraph feature selection rationale written
- [ ] Resource requirements detailed
- [ ] Gaps identified with mitigation strategies
- [ ] Coverage validation matrix complete

### Consistency
- [ ] Requesters match personas from Step 6
- [ ] Needs match Step 7 qualification matrix
- [ ] Features match Step 11 feature library
- [ ] Resource requirements align with Step 11 feasibility analysis
- [ ] Product name and description consistent

### Clarity
- [ ] Language is client-understandable (no jargon)
- [ ] Value proposition clear from feature rationale
- [ ] Differentiation specific (not generic claims)
- [ ] Timelines realistic (validated by Step 11)

### Evidence
- [ ] All fundamental needs have ≥5 interview validation
- [ ] >50% of MVP features validated by ≥5 interviews
- [ ] All features tied to specific needs (no "nice to have" features without need mapping)
- [ ] Assumptions explicitly flagged where validation weak

### Coverage
- [ ] All fundamental needs have MVP feature coverage
- [ ] No MVP features address only secondary needs
- [ ] Gaps in fundamental need coverage justified or addressed

---

## Common Decision Points

### How Many Products to Define?

**Single Product** if:
- All validated requesters share similar needs
- Feature set coherent for single offering
- Business model consistent across segments

**Multiple Products** if:
- Distinct requester groups with divergent needs
- Feature sets incompatible (e.g., simple tool vs. enterprise platform)
- Different business models required (e.g., freemium vs. enterprise sales)

**Example**:
- Healthcare facilities need enterprise platform ($499/month)
- Individual practitioners need simple tool ($49/month)
- → Define 2 separate products

### How Many MVP Features?

**Target**: 6-10 features

**Too Few** (<6): May not address all fundamental needs → insufficient value
**Too Many** (>12): Feature bloat → delays launch, dilutes focus

**Rule**: Include minimum feature set to address all fundamental needs with differentiation.

### How to Prioritize Features?

**Priority Framework**:
1. **Must Have**: Addresses fundamental need + strong validation + short timeline
2. **Should Have**: Addresses important need + medium validation + feasible timeline
3. **Could Have**: Addresses important/secondary need + weak validation or long timeline
4. **Won't Have (This Phase)**: Secondary needs, unvalidated, or resource-constrained

**MVP = Must Have + select Should Have features (if resources allow)**

### When to Phase Features?

**Phase features if**:
- Addresses important (not fundamental) needs
- Requires partnerships not yet confirmed
- Timeline >6 months
- Validation weak (<3 interviews)
- MVP already addresses fundamental needs adequately

**Example**:
- MVP: Audit checklist automation (fundamental need, 8 interviews, 3-month timeline)
- Phase 2: AI summarization (important need, 6 interviews, 9-month timeline + partnership required)

---

## Output Format

### Markdown Template

Use: `templates/Step12_PMF_Template.md`

### DOCX Format

Use: `templates/Step12_PMF_Template.md` (convert to DOCX with formatting)

**DOCX Formatting Requirements**:
- Font: Calibri 11pt
- Headings: Bold, color #2C3E50
- Tables: Color-coded by status (green=ready, orange=in-progress, red=gap)
- Character limits: Enforced via form fields or validation

---

## Example Product/Market Fit Sheet (Abbreviated)

```markdown
# Product/Market Fit Sheet: HealthCare Compliance Hub

## Product Identity

**Product Name**: HealthCare Compliance Hub (28 chars ✓)

**Description**: Compliance automation platform for healthcare providers combining audit preparation, regulatory tracking, and staff training in a single dashboard. (179 chars ✓)

## Targeted Requesters

**Sarah - Compliance Director**
- Profile: Mid-size hospital compliance officer managing 15+ regulatory frameworks
- Key Characteristics: Detail-oriented, time-pressured, audit-focused
- Primary Needs: Automate audit prep, track regulatory changes, train staff

**Mike - Clinic Administrator**
- Profile: Small practice administrator handling compliance part-time
- Key Characteristics: Non-specialist, budget-conscious, seeks simplicity
- Primary Needs: Simplify compliance tracking, reduce setup time, affordable pricing

## Primary Needs Addressed

| Need Statement | Intensity | Current Satisfaction | Validation | Requesters |
|---------------|-----------|---------------------|------------|------------|
| Automate audit preparation | Fundamental | Low (1.5/5) | 8 interviews | Sarah, Mike |
| Track regulatory changes | Fundamental | Low (2.0/5) | 8 interviews | Sarah, Mike |
| Train staff on compliance | Important | Medium (3.0/5) | 6 interviews | Sarah |
| Simplify compliance tracking | Important | Low (2.2/5) | 5 interviews | Mike |
| Reduce software setup time | Important | Low (1.8/5) | 7 interviews | Mike |

## MVP Features (8 features)

1. **Automated Audit Checklist Generator**
   - Addresses: Automate audit prep
   - Timeline: 3 months
   - Validation: 8 interviews

2. **Regulatory Change Alerts**
   - Addresses: Track regulatory changes
   - Timeline: 2 months
   - Validation: 8 interviews

[... 6 more features ...]

## Phased Features (2 features)

1. **AI-Powered Regulation Summarization**
   - Addresses: Track regulatory changes
   - Why Phased: Requires ML partnership (6-9 month timeline)
   - Target: Phase 2

[... 1 more phased feature ...]

## Feature Selection Rationale

The MVP focuses on automating audit preparation, the highest-intensity need (4.8/5 average) validated across 8 interviews. This workflow currently consumes 40+ hours per audit cycle; our solution reduces this to 8 hours through pre-built checklists for 15 common frameworks...

[... 2 more paragraphs ...]

## Resource Requirements

**Technical**: 3 backend engineers (6 months), AWS hosting ($2k/month), HIPAA storage
**Human**: Compliance SME (part-time), UX designer (3 months)
**Financial**: $180k development, $50k/year operations
**Partnerships**: Regulatory consulting firm (content validation)

## Gaps & Mitigation

| Gap | Impact | Mitigation | Status |
|-----|--------|-----------|--------|
| HIPAA expertise | Cannot launch without cert | Engage auditor ($25k budgeted) | In progress |

## Coverage Validation

| Fundamental Need | MVP Features | Coverage |
|-----------------|-------------|----------|
| Automate audit prep | Checklist Generator, Template Library | ✅ Complete |
| Track reg changes | Change Alerts, Framework Database | ✅ Complete |

```

---

## Next Steps

After completing Product/Market Fit definition:

1. **Proceed to Step 12b**: Define Business Model Canvas for this product
2. **Repeat for additional products**: If defining multiple products, complete 12a for each
3. **Review portfolio**: Ensure products are distinct and complementary (not overlapping)
4. **Validate with stakeholders**: Confirm product definitions align with strategic goals

---

**Remember**: Product/Market Fit connects validated needs (Steps 5-7) to validated capabilities (Step 11). Every feature must map to a need; every fundamental need must have feature coverage.
