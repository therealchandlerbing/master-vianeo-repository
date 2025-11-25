# Step 12: Viability Assessment - Output Format Specification

**Version**: 2.0
**Purpose**: Exact format specification for Step 12 outputs (Business model validation)
**Dimension**: Viability (20% of VIANEO score)

---

## Required Output Structure

### Deliverables Overview

| Deliverable | Format | Purpose |
|-------------|--------|---------|
| PMF Sheet | Markdown/DOCX | Product-Market Fit validation |
| Business Model Canvas | Markdown/Visual | 9-box model documentation |
| Financial Projections | Markdown + Reference | 3-year projections |
| Viability Dashboard | HTML | Interactive metrics visualization |
| Risk Assessment | Within analysis | Risk documentation |

---

## Deliverable 1: PMF (Product-Market Fit) Sheet

### Format

```markdown
# Product-Market Fit Analysis - [Project Name]

**Date**: YYYY-MM-DD
**Assessment Version**: 1.0

---

## Value Proposition

### Core Value Proposition

[2-3 sentences describing unique value delivered to customers]

### Value Proposition Canvas

| Customer Profile | Value Map |
|------------------|-----------|
| **Jobs to be done**: [From Step 5] | **Products/Services**: [What you offer] |
| **Pains**: [From Step 5/6] | **Pain Relievers**: [How you address pains] |
| **Gains**: [From Step 5/6] | **Gain Creators**: [How you create value] |

---

## Customer Segments

### Primary Segment

| Attribute | Description |
|-----------|-------------|
| **Segment Name** | [From Step 5] |
| **Size** | [TAM/SAM for this segment] |
| **Validation Status** | [X interviews conducted] |
| **Willingness to Pay** | [Evidence of WTP] |

### Secondary Segment(s)

[Repeat for additional segments]

---

## Problem-Solution Fit

### Problem Validation

| Question | Score | Evidence |
|----------|-------|----------|
| Is the problem real? | [1-5] | [Source] |
| Is it urgent? | [1-5] | [Source] |
| Are people actively seeking solutions? | [1-5] | [Source] |

### Solution Validation

| Question | Score | Evidence |
|----------|-------|----------|
| Does our solution address the problem? | [1-5] | [Source] |
| Is it better than alternatives? | [1-5] | [Source] |
| Have users validated the solution? | [1-5] | [Source] |

---

## PMF Score

**PMF Score**: [X.X] / 5.0

| Indicator | Status |
|-----------|--------|
| Problem validated | ✓/✗ |
| Solution validated | ✓/✗ |
| Customer willing to pay | ✓/✗ |
| Retention/engagement positive | ✓/✗ |

**PMF Status**: [Pre-PMF / Approaching PMF / PMF Achieved]
```

---

## Deliverable 2: Business Model Canvas

### Format

```markdown
# Business Model Canvas - [Project Name]

## 9-Box Model

### 1. Customer Segments
[From Step 5/6 personas - specific segments]

### 2. Value Propositions
[From PMF Sheet - differentiated value]

### 3. Channels
[From Step 8 - distribution and communication]

### 4. Customer Relationships
[How you acquire, retain, grow customers]

### 5. Revenue Streams
[Pricing model, revenue types, payment structure]

### 6. Key Resources
[From Step 4 means - critical assets]

### 7. Key Activities
[Core operations required]

### 8. Key Partnerships
[From Step 8 - critical partners]

### 9. Cost Structure
[Major cost categories]

---

## Model Validation Status

| Element | Validation Status | Evidence |
|---------|-------------------|----------|
| Customer Segments | [Validated/Partial/Hypothesis] | [Source] |
| Value Propositions | [Validated/Partial/Hypothesis] | [Source] |
| Channels | [Validated/Partial/Hypothesis] | [Source] |
| Revenue Streams | [Validated/Partial/Hypothesis] | [Source] |
| [Continue for all 9] | | |
```

---

## Deliverable 3: Financial Projections

### Format

```markdown
# Financial Projections - [Project Name]

## Revenue Projections

| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Customers | [#] | [#] | [#] |
| ARPU | [$] | [$] | [$] |
| Revenue | [$] | [$] | [$] |
| Growth Rate | — | [%] | [%] |

## Cost Projections

| Category | Year 1 | Year 2 | Year 3 |
|----------|--------|--------|--------|
| Personnel | [$] | [$] | [$] |
| Technology | [$] | [$] | [$] |
| Marketing | [$] | [$] | [$] |
| Operations | [$] | [$] | [$] |
| **Total Costs** | **[$]** | **[$]** | **[$]** |

## Profitability

| Metric | Year 1 | Year 2 | Year 3 |
|--------|--------|--------|--------|
| Gross Margin | [%] | [%] | [%] |
| Operating Margin | [%] | [%] | [%] |
| Net Income | [$] | [$] | [$] |

## Key Assumptions

1. [Assumption 1 with basis]
2. [Assumption 2 with basis]
3. [Assumption 3 with basis]
```

---

## Deliverable 4: Unit Economics

### Format

```markdown
# Unit Economics - [Project Name]

## Core Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| **CAC** (Customer Acquisition Cost) | $[X] | $[Industry] | 🟢/🟡/🔴 |
| **LTV** (Lifetime Value) | $[X] | — | — |
| **LTV:CAC Ratio** | [X]:1 | ≥3:1 | 🟢/🟡/🔴 |
| **Payback Period** | [X] months | <12 months | 🟢/🟡/🔴 |
| **Gross Margin** | [X]% | [Industry]% | 🟢/🟡/🔴 |
| **Churn (Monthly)** | [X]% | <2% | 🟢/🟡/🔴 |

## LTV Calculation

```
LTV = ARPU × Gross Margin × Customer Lifetime
LTV = $[X] × [X]% × [X] months = $[X]
```

## CAC Calculation

```
CAC = Total Acquisition Spend / New Customers
CAC = $[X] / [X] = $[X]
```

## Status Assessment

| Metric | Healthy | Current | Gap |
|--------|---------|---------|-----|
| LTV:CAC | ≥3:1 | [X]:1 | [X or "On target"] |
| Payback | <12mo | [X]mo | [X or "On target"] |
| Gross Margin | >70% | [X]% | [X or "On target"] |
```

---

## Deliverable 5: Viability Dashboard (HTML)

### Structure

```html
<!DOCTYPE html>
<html>
<head>
    <title>Viability Dashboard - [Project Name]</title>
</head>
<body>
    <header>
        <h1>Viability Dashboard</h1>
        <p>Project: [Name] | Date: [YYYY-MM-DD]</p>
    </header>

    <section class="metrics-grid">
        <!-- Growth Metrics -->
        <div class="metric-card">
            <h3>Revenue</h3>
            <div class="value">$[X]</div>
            <div class="trend">↑ [X]% MoM</div>
        </div>

        <!-- Unit Economics -->
        <div class="metric-card">
            <h3>LTV:CAC</h3>
            <div class="value">[X]:1</div>
            <div class="status green/yellow/red">Healthy/Warning/Critical</div>
        </div>

        <!-- Continue for all key metrics -->
    </section>

    <section class="projections">
        <!-- Charts/visualizations -->
    </section>
</body>
</html>
```

### Required Metrics on Dashboard

| Category | Metrics |
|----------|---------|
| **Growth** | MRR/ARR, Customer count, Growth rate |
| **Economics** | LTV, CAC, LTV:CAC, Gross margin |
| **Efficiency** | Payback period, Burn rate, Runway |
| **Health** | Churn rate, NPS (if available), Retention |

### Color Coding

| Status | Color | Criteria |
|--------|-------|----------|
| Healthy | Green (#10b981) | Meets or exceeds benchmark |
| Warning | Yellow (#f59e0b) | Below benchmark but recoverable |
| Critical | Red (#ef4444) | Significantly below, action needed |

---

## Deliverable 6: Risk Assessment

### Format

```markdown
# Risk Assessment - [Project Name]

## Risk Matrix

| Risk | Category | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
| [Risk 1] | Market/Financial/Operational/Technical | H/M/L | H/M/L | [Strategy] |
| [Risk 2] | Market/Financial/Operational/Technical | H/M/L | H/M/L | [Strategy] |

## Risk Categories

### Market Risks
- [Risk and mitigation]

### Financial Risks
- [Risk and mitigation]

### Operational Risks
- [Risk and mitigation]

### Technical Risks
- [Risk and mitigation]
```

---

## Viability Score Calculation

### Format

```markdown
## VIABILITY SCORE

### Score Calculation

**Viability** = (Q14 + Q19 + Q27 + Q29) / 4

- Q14 (Business model defined): [1-5]
- Q19 (Pricing validated): [1-5]
- Q27 (Value capture mechanism): [1-5]
- Q29 (Path to profitability): [1-5]

**Viability Score**: **[X.X]** / 5.0

### Threshold Check

- **Required**: ≥3.0
- **Status**: ✓ PASS / ✗ FAIL
```

---

## Output Files

### Required Deliverables

| File | Format | Naming |
|------|--------|--------|
| PMF Sheet | .md/.docx | `[Project]_PMF_Sheet.md` |
| Business Model | .md | `[Project]_Business_Model.md` |
| Financial Projections | .md | `[Project]_Financial_Projections.md` |
| Viability Dashboard | .html | `[Project]_Viability_Dashboard.html` |

---

## Quality Checklist

Before delivery, verify:

### PMF Sheet
- [ ] Value proposition clearly articulated
- [ ] Customer segments from Step 5/6
- [ ] Problem-solution fit scores
- [ ] PMF status determined

### Business Model
- [ ] All 9 boxes complete
- [ ] Validation status for each element
- [ ] Integration with previous steps

### Financial Projections
- [ ] 3-year projections minimum
- [ ] Revenue and cost breakdown
- [ ] Assumptions documented
- [ ] Realistic growth rates

### Unit Economics
- [ ] CAC calculated
- [ ] LTV calculated
- [ ] LTV:CAC ratio ≥3:1 (or path to)
- [ ] Payback period documented

### Dashboard
- [ ] All key metrics present
- [ ] Color coding applied
- [ ] Interactive (if HTML)
- [ ] Professional appearance

---

## Common Mistakes to Avoid

1. ❌ No unit economics → ✅ Calculate CAC, LTV, ratio
2. ❌ Hockey stick projections → ✅ Justified growth rates
3. ❌ Missing assumptions → ✅ Document all assumptions
4. ❌ Incomplete canvas → ✅ All 9 boxes filled
5. ❌ No risk assessment → ✅ Identify and mitigate risks
6. ❌ Unrealistic margins → ✅ Industry-appropriate benchmarks
7. ❌ No validation status → ✅ Mark what's validated vs. hypothesis

---

**This specification ensures every Step 12 output follows consistent format for viability assessment.**
