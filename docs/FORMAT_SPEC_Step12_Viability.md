# Step 12: Viability Assessment - Output Format Specification

**Version**: 3.0
**Purpose**: Exact format specification for Step 12 outputs (Business model validation)
**Dimension**: Viability (20% of VIANEO score)

---

## Required Output Structure

### Deliverables Overview

| Deliverable | Format | Prompt | Purpose |
|-------------|--------|--------|---------|
| PMF Sheet | Markdown/DOCX | Step 12a | Product-Market Fit validation |
| Business Model Canvas | Markdown/DOCX | Step 12b | 4-component model documentation |
| Viability Dashboard | HTML | Step 12 Dashboard | Interactive metrics visualization |
| Summary Dashboard | Markdown | Step 12 | Portfolio-level analysis |

---

## Deliverable 1: Product/Market Fit Sheet

### Format

```markdown
# Product/Market Fit Sheet: [Product Name]

**Project**: [Project Name]
**Date**: YYYY-MM-DD
**Client Segment**: [Client Type]
**Version**: 1.0

---

## Product Identity

**Product/Service Name**: [Name - max 60 characters]

**Description** (250 chars max):
[What the client understands they're buying - format: what it is, for whom, key capabilities, without what pain point]

**Target Client**: [Specific client segment from value network]

**Character Count Check**:
- Name: [X]/60 ✓
- Description: [X]/250 ✓

---

## Market Validation (from Desirability - Steps 5-7)

### Targeted Requesters

#### 1. [Requester Persona Name]

**Profile**: [Brief description - age range, role, context]

**Key Characteristics**:
- [Behavior/attitude 1]
- [Behavior/attitude 2]
- [Pain point/context]

**Primary Needs for This Product**:
- [Need 1 - intensity level]
- [Need 2 - intensity level]
- [Need 3 - intensity level]

[Continue for 2-4 total requesters]

---

### Primary Needs Addressed

| # | Need Statement | Intensity | Current Satisfaction | Validation | Targeted Requesters |
|---|----------------|-----------|---------------------|------------|---------------------|
| 1 | [Full need statement] | Fundamental | Not at all | >5 interviewed | [Requester 1, 2] |
| 2 | [Full need statement] | Fundamental | Rather not | >5 interviewed | [Requester 1] |
| 3 | [Full need statement] | Important | Rather not | >5 interviewed | [Requester 2] |

[Continue for 5-10 total needs]

**Need Coverage Summary**:
- **Total Needs Addressed**: [Number]
- **Fundamental**: [Count] needs
- **Important**: [Count] needs
- **Secondary**: [Count] needs
- **Overall Validation Level**: [>5 interviewed for X/Y needs]

---

## Solution Configuration (from Feasibility - Step 11)

### MVP Features (Must Have)

| Feature Name | Timeline | Needs Covered | Validation Level | MVP Rationale |
|--------------|----------|---------------|------------------|---------------|
| [Feature 1] | Already available | [Need 1, Need 2] | >5 interviewed | [Why MVP] |
| [Feature 2] | Short term (0-6 mo) | [Need 3] | >5 interviewed | [Why MVP] |

[Continue for 6-10 MVP features]

**MVP Features Summary**:
- **Total MVP Features**: [Number] *(target: 6-10)*
- **Available Now**: [Count]
- **Short-term (0-6 mo)**: [Count]
- **High Validation (>5)**: [Count]/[Total]

**MVP Coverage Check**:
- [ ] All fundamental needs have at least one MVP feature ✓
- [ ] All MVP features map to fundamental or important needs ✓
- [ ] MVP size is 6-10 features ✓
- [ ] Majority (>50%) of MVP features have >5 interviews validation ✓

---

### Configuration Rationale

**Why This Feature Set?**

[Paragraph 1: Core Value Focus - 3-4 sentences]
[Paragraph 2: Differentiation & Validation - 3-4 sentences]
[Paragraph 3: Phasing Strategy - 2-3 sentences]

---

## Resource Requirements (from Feasibility - Step 11)

### Means Required
- [Resource 1]
- [Resource 2]
- [Resource 3]

### Technical Partners Critical for MVP
- [Partner 1]: [Contribution]
- [Partner 2]: [Contribution]

### Resource Gaps & Mitigation
**Gap 1**: [Description]
- **Impact**: [Effect]
- **Mitigation**: [Strategy]

---

## Validation Summary

### Information Reliability
- MVP features with >5 interviews: [X]/[Total] = [%]
- Fundamental needs with >5 interviews: [X]/[Total] = [%]
- Overall assessment: [Strong/Moderate/Weak]

### Need Coverage
- Fundamental needs coverage: [X]/[Total] = 100%
- Important needs coverage: [X]/[Total] = [%]
- Overall PMF strength: [High/Medium/Low]

---

## Document Metadata

**Based On**: Steps 5-7 (Desirability), Step 11 (Feasibility)
**Feeds Into**: Step 12b (Business Model), Step 13 (Financial)
**Status**: [Draft | Review | Final]
**Date**: [YYYY-MM-DD]
```

---

## Deliverable 2: Business Model Canvas (4-Component)

### Format

```markdown
# Business Model Canvas: [Product Name]

**Project**: [Project Name]
**Date**: YYYY-MM-DD
**Product**: [Product Name]
**Target Client**: [Client Segment]
**Version**: 1.0

---

## 1. VALUE PROPOSITION

*Why clients choose this offering over alternatives*

### Core Positioning Statement
[One sentence: "For [client type], [product] delivers [outcome] without [pain point]"]

### Competitive Advantages

#### Advantage 1: [Title]
**Description**: [Clear articulation]
**Addresses Need**: [Specific need from PMF]
**Evidence**: [Validation data]
**Why Better**: [Comparison to alternatives]

[Continue for 3-4 advantages]

### Client Benefits by Requester Type
#### For [Requester Type 1]:
**Primary Outcome**: [Measurable result]
**Supporting Outcomes**: [2-3 benefits]
**Value Delivered By**: [MVP features]

[Continue for all requesters]

### Platform Input ([X]/250 chars):
"[Concise value proposition within 250 characters]"

---

## 2. REVENUE STREAM

*How money is earned from this offering*

### Revenue Model Description
[2-3 sentences explaining monetization]

**Pricing Approach**: [Subscription/Per unit/Commission/etc.]
**Revenue Type**: [One-time/Recurring/Mixed]

### Pricing Mechanisms
#### Mechanism 1: [Primary]
**Pricing Example**: [$X/month per user]
**Rationale**: [Value alignment, market context]
**Tied To**: [Value element]

### Dependencies & Constraints
- Payment timing: [When collected]
- Minimum commitments: [Contracts, volumes]
- Churn assumptions: [Expected rates]

### Platform Input ([X]/250 chars):
"[Concise revenue stream within 250 characters]"

---

## 3. DISTRIBUTION CHANNEL

*How customers discover and purchase*

### Discovery Channels
**Primary**: [3-4 channels with approach]
**Supporting**: [2-3 secondary channels]

### Purchase Channels
**Primary**: [Direct web/Sales team/Marketplace/etc.]
**Transaction Process**: [Step-by-step]

### Intermediary Strategy
**Decision**: [Direct to customer / Through intermediaries]
[Rationale and details]

### Platform Input ([X]/250 chars):
"[Concise distribution within 250 characters]"

---

## 4. COST STRUCTURE

*Major costs to develop, produce, market, deliver*

### Cost Categories
**Development**: [Major items]
**Operations**: [Major items]
**Marketing/Sales**: [Major items]
**Human Resources**: [Team composition]

### Fixed vs. Variable
**Fixed Costs**: [Items that don't scale]
**Variable Costs**: [Items that scale with volume]

### Cost Drivers
[3-4 drivers with impact and scaling pattern]

### Platform Input ([X]/250 chars):
"[Concise cost structure within 250 characters]"

---

## 5. COHERENCE VALIDATION

### Alignment Checks

| Check | Question | Status |
|-------|----------|--------|
| Value-Features | Can MVP deliver value claims? | ✓ Aligned / ⚠️ Gap |
| Value-Revenue | Does pricing reflect value? | ✓ Aligned / ⚠️ Gap |
| Revenue-Distribution | Does channel match complexity? | ✓ Aligned / ⚠️ Gap |
| Distribution-Costs | Are CAC costs included? | ✓ Aligned / ⚠️ Gap |
| Costs-Revenue | Can revenue support costs? | ✓ Aligned / ⚠️ Gap |

### Red Flag Assessment
**Red Flags Identified**: [List or "None - coherent"]

### Coherence Summary
**Overall**: [Coherent / Minor Issues / Major Issues]
**Narrative**: [2-3 sentences]

---

## Document Metadata
**Based On**: Step 12a (PMF Sheet), Steps 5-11
**Feeds Into**: Step 13 (Financial Modeling)
**Status**: [Draft | Review | Final]
**Date**: [YYYY-MM-DD]
```

---

## Deliverable 3: Viability Summary Dashboard (Markdown)

### Format

```markdown
# Viability Summary Dashboard: [Project Name]

**Date**: YYYY-MM-DD
**Products Evaluated**: [Number]
**Assessment Phase**: Viability (Step 12)

---

## Executive Summary
[2-3 paragraphs: scope, validation strength, recommendations]

---

## Product Portfolio Overview

| Product Name | Target Client | MVP Features | Revenue Model | Status |
|-------------|--------------|--------------|---------------|--------|
| [Product 1] | [Client] | [Count] | [Type] | [Ready/In Progress] |

---

## Need Coverage Analysis

| Fundamental Need | Product 1 | Product 2 | Coverage |
|-----------------|-----------|-----------|----------|
| [Need statement] | ✓ MVP | ✓ Phased | Strong |

**Coverage Metrics**:
- Fundamental needs covered: [X]/[Total] = 100%
- Important needs covered: [X]/[Total] = [%]

---

## Portfolio Readiness

| Metric | Percentage | Detail |
|--------|------------|--------|
| MVP Validation | [X]% | [Y/Z] features with >5 interviews |
| Resource Readiness | [X]% | [Y/Z] resources secured |
| Business Model Coherence | [X]% | All products aligned |
| Need Coverage | 100% | All fundamental needs covered |

---

## Strategic Insights

### Strengths
1. [Strength with evidence]

### Opportunities
1. [Opportunity with impact]

### Concerns
1. [Concern with mitigation]

### Recommendations
1. [Action with priority]

---

## Viability Score

**Viability Score**: [X.X] / 5.0
**Status**: [Strong / Moderate / Weak]
**Threshold Check**: ≥3.0 required → [PASS/FAIL]
```

---

## Deliverable 4: Viability Dashboard (HTML)

### Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Viability Dashboard | [Project Name]</title>
    <!-- Inline CSS with VIANEO design system -->
</head>
<body>
    <!-- Skip Link for Accessibility -->
    <a href="#main-content" class="skip-link">Skip to main content</a>

    <div class="dashboard-container">
        <!-- Header with metrics -->
        <header class="dashboard-header">
            <h1>[Project Name]</h1>
            <div class="key-metrics">
                <!-- Products, Features, Coverage, Score -->
            </div>
        </header>

        <!-- Main Content -->
        <main id="main-content">
            <!-- Executive Summary -->
            <!-- Product Portfolio Grid -->
            <!-- Need Coverage Table -->
            <!-- Progress Metrics -->
            <!-- Strategic Insights -->
        </main>

        <!-- Footer -->
        <footer>[Footer with metadata]</footer>
    </div>

    <!-- Product Modals -->
    <!-- Inline JavaScript -->
</body>
</html>
```

### Required Dashboard Metrics

| Category | Metrics |
|----------|---------|
| **Portfolio** | Product count, MVP features total, Need coverage % |
| **Validation** | High validation %, Resource readiness %, Coherence % |
| **Status** | Per-product status (MVP Ready/In Progress/Planning) |
| **Insights** | Strengths, Opportunities, Concerns, Recommendations |

### Color Coding

| Status | Color | Usage |
|--------|-------|-------|
| Success/Ready | #10b981 | MVP Ready, High validation, Aligned |
| In Progress | #3b82f6 | Development ongoing |
| Warning/Attention | #f59e0b | Planning, Needs validation |
| Critical | #ef4444 | Blocked, Major issues |

---

## Output Files

### Required Deliverables

| File | Format | Naming Convention |
|------|--------|-------------------|
| PMF Sheet | .md/.docx | `[ProductName]_PMF_Sheet.md` |
| Business Model | .md/.docx | `[ProductName]_Business_Model.md` |
| Summary Dashboard | .md | `[ProjectName]_Viability_Summary.md` |
| Interactive Dashboard | .html | `[ProjectName]_Viability_Dashboard.html` |

### Optional Platform Inputs

| File | Purpose |
|------|---------|
| `[ProjectName]_Platform_Inputs.md` | All 250-char summaries for Vianeo platform entry |

---

## Quality Checklist

Before delivery, verify:

### PMF Sheet
- [ ] Product identity complete with character counts
- [ ] 2-4 requesters with profiles and needs
- [ ] 5-10 needs with intensity and validation levels
- [ ] 6-10 MVP features with rationale
- [ ] 100% fundamental need coverage
- [ ] Resource requirements documented

### Business Model Canvas
- [ ] All 4 components complete
- [ ] Platform inputs within 250 chars (4 total)
- [ ] Coherence validation performed
- [ ] No red flags OR mitigation documented
- [ ] Evidence basis included

### Dashboards
- [ ] Executive summary accurate
- [ ] Product metrics correct
- [ ] Need coverage calculated
- [ ] Progress percentages accurate
- [ ] Strategic insights evidence-based
- [ ] HTML accessibility compliant

---

## Character Limits (Enforced)

| Element | Limit |
|---------|-------|
| Product name | 60 characters |
| Product description | 250 characters |
| Value proposition (platform) | 250 characters |
| Revenue stream (platform) | 250 characters |
| Distribution channel (platform) | 250 characters |
| Cost structure (platform) | 250 characters |

---

## Validation Requirements

### PMF Sheet Validation
- All requesters trace to Step 6 personas
- All needs trace to Step 7 qualification matrix
- All features trace to Step 11 feature library
- 100% fundamental need coverage required

### Business Model Validation
- Value advantages cite validation evidence
- Pricing specific (not "TBD")
- Distribution matches client buying behavior
- Cost structure covers all implied activities
- Coherence checks pass (no contradictions)

### Dashboard Validation
- Metrics match source documents
- Coverage percentages accurate
- Insights evidence-based
- HTML renders correctly
- Accessibility requirements met

---

## Common Mistakes to Avoid

1. ❌ Feature bloat (>12 MVP) → ✅ 6-10 focused features
2. ❌ Orphan needs (no features) → ✅ 100% fundamental coverage
3. ❌ Vague pricing ("TBD") → ✅ Specific mechanisms
4. ❌ Incoherent model → ✅ All components aligned
5. ❌ Missing validation → ✅ Evidence for all claims
6. ❌ Generic value props → ✅ Specific, differentiating
7. ❌ Incomplete costs → ✅ All activities accounted

---

## Integration with VIANEO Dimensions

**Viability (20%)** synthesizes:
- **Legitimacy (15%)**: Problem worth solving economically?
- **Desirability (25%)**: Enough people want the solution?
- **Acceptability (20%)**: Ecosystem supports the model?
- **Feasibility (20%)**: Team can execute?

**Viability validates**: Commercial sustainability through evidence-based product-market fit and coherent business models.

---

**This specification ensures consistent, professional Step 12 outputs aligned with the VIANEO framework.**
