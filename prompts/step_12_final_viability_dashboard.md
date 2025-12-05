# Step 12 Final: Viability Dashboard Generation

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 12 Final: Viability Dashboard Generation from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12_final_viability_dashboard.md`.

**Required Inputs:**
- Step 12 Initial: Viability Assessment (with gate recommendation)
- Step 12a: Product Market Fit Sheet
- Step 12b: Business Models per Segment
- Numeric viability indicators and thresholds (if available)

---

## Overview

Transform Step 12 viability outputs into a **dashboard specification** that can be translated into slides, platform views, or HTML dashboards. Focus on decision-ready summaries per segment.

## Purpose

Generate presentation-grade dashboards that visualize:
- **Per-segment viability status** with indicator tables
- **Cross-segment comparison** for portfolio decisions
- **Recommended next steps** in concise format

---

## Instructions for AI Assistant

You are a Vianeo dashboard designer. Using completed Step 12 Initial, 12a, and 12b outputs, generate a viability dashboard specification. You must not change any numeric indicators - you present them. Focus on per-segment clarity and cross-segment comparison.

---

## Output Structure

### 1. One-Slide Summary

Produce content that fits on one slide:
- A headline sentence stating viability status
- 3 bullet points:
  - Top strength
  - Top risk
  - Top opportunity or pathway

---

### 2. Per-Segment Dashboard Table

For each targeted segment, output:

```markdown
## Segment: [Segment name]

### Segment Viability Dashboard

| Indicator | Value | Threshold / Target | Status | Source Step(s) |
|-----------|-------|-------------------|--------|----------------|
| Desirability score | [from inputs] | [threshold] | Meets / Below | Step 2, Step 3 |
| Feasibility score | [from inputs] | [threshold] | Meets / Below | Step 2, Step 3 |
| Viability (economics) indicator | [from inputs] | [threshold] | Meets / Below | Step 12 Initial / 12b |
| Key network risk | [rating] | N/A | Low / Medium / High | Step 9 |
| Business model readiness | [rating] | N/A | Low / Medium / High | Step 12b |
```

**Guidelines:**
- Use only indicators that are actually available
- If some indicators are not provided, leave Value cell empty and mark Status as "Not assessed"
- Do NOT invent scores

---

### 3. Cross-Segment Comparison

Create a summary table:

```markdown
### Cross-Segment Comparison

| Segment | Overall Viability (qualitative) | Main Revenue Potential | Main Risk Level | Recommended Stance |
|---------|--------------------------------|------------------------|-----------------|-------------------|
| Segment A | [High / Medium / Low] | [Brief description] | [Low / Medium / High] | Go / Conditional / Hold / No Go |
| Segment B | [High / Medium / Low] | [Brief description] | [Low / Medium / High] | Go / Conditional / Hold / No Go |
| ... | ... | ... | ... | ... |
```

**Base qualitative judgments on:**
- Numeric indicators from inputs
- Business model strength from Step 12b
- Risk profile from earlier steps

Do NOT introduce new segments. Work only with segments from Steps 5/6.

---

### 4. Recommended Next Steps

In 1-2 short paragraphs, describe:
- What should happen next in the next 1-3 months for this project
- How this differs by segment, if relevant
- Which experiments or validations should be prioritized

Keep the language concise and decision-oriented. This section should be directly reusable in an Executive Report or Diagnostic Comment.

---

## Deployment Context

**When to Generate**:
- After completing all Step 12 viability analysis
- Before financial modeling (Step 13)
- For investment committee presentations
- For board strategy sessions

**Primary Audiences**:
- Executive leadership
- Investment committees
- Board members
- Strategic advisors

---

## HTML Dashboard Structure (Optional)

### 1. Header Section

**Required Elements**:
- Project name (h1)
- Subtitle: "Viability Assessment: Product-Market Fit & Business Model Portfolio"
- Date
- Assessment status (Complete/In Progress/Draft)

**Key Metrics Row** (4 cards):
1. Products Defined (count)
2. MVP Features (total across portfolio)
3. Need Coverage (percentage)
4. Viability Score (X.X/5.0)

### 2. Executive Summary

**Content** (2-3 paragraphs):
- Paragraph 1: Scope, product count, overall viability status
- Paragraph 2: Validation strength, business model alignment, key differentiator
- Paragraph 3: Critical success factors, primary recommendation, timeline

### 3. Product Portfolio Grid

**Card Format** (per product):
- Product name
- Target client
- Status badge (MVP Ready / In Progress / Planning)
- Description (250 chars)
- Metrics: MVP Features, Requesters
- Tags: Revenue model, Distribution type
- Click action: Open detailed modal

**Modal Content**:
- Product identity details
- MVP features list with badges
- Full business model (all 4 components)
- Resource requirements

### 4. Need Coverage Analysis

**Table Format**:

| Fundamental Need | Intensity | Product 1 | Product 2 | Product 3 | Coverage |
|-----------------|-----------|-----------|-----------|-----------|----------|
| [Need statement] | Fundamental | MVP/Phased/— | MVP/Phased/— | MVP/Phased/— | Strong/Partial |

**Coverage Metrics**:
- Fundamental needs total
- Covered by at least one MVP
- Covered by multiple products
- Gap identification

### 5. Portfolio Readiness

**Progress Bars** (4 items):
1. MVP Validation: [X]% (features with >5 interviews)
2. Resource Readiness: [X]% (resources secured/available)
3. Business Model Coherence: [X]% (alignment checks passed)
4. Need Coverage: [X]% (fundamental needs with features)

### 6. Strategic Insights Grid

**Card Types** (4 categories):
- **Strength** (green accent): Portfolio advantage with evidence
- **Opportunity** (blue accent): Market opportunity with impact
- **Concern** (orange accent): Risk with mitigation strategy
- **Recommendation** (purple accent): Action with priority and owner

**Card Format**:
- Icon
- Title
- Content (2-3 sentences)
- Products affected
- Priority/Impact badge

---

## Design Specifications

### Color System

**Primary Palette**:
```css
--color-primary: #1a365d;
--color-primary-light: #2c5282;
--color-surface: #ffffff;
--color-background: #f7fafc;
--color-border: #e2e8f0;
```

**Status Colors**:
```css
--color-success: #10b981;  /* MVP Ready, High validation */
--color-info: #3b82f6;     /* In Progress */
--color-warning: #f59e0b;  /* Planning, Needs attention */
--color-danger: #ef4444;   /* Blocked, Critical */
```

**Product Status**:
```css
--color-mvp-ready: #10b981;
--color-in-progress: #3b82f6;
--color-planning: #f59e0b;
```

### Typography

- **Headings**: System font stack (-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif)
- **h1**: 32px, 700 weight
- **h2**: 24px, 700 weight
- **h3**: 18-20px, 700 weight
- **Body**: 14-16px, 400 weight

### Spacing

- Base unit: 8px
- Section spacing: 48px
- Card padding: 24px
- Grid gaps: 24px

### Components

**Cards**:
- Border: 2px solid border color
- Border-radius: 12px
- Hover: Shadow + slight lift

**Progress Bars**:
- Height: 8px
- Border-radius: 4px
- Gradient fill

**Status Badges**:
- Padding: 4px 10px
- Border-radius: 12px
- Uppercase, small text

**Tables**:
- Header: Primary color background, white text
- Alternating rows: White / light gray
- Hover highlight

---

## Accessibility Requirements

**WCAG AA Compliance**:
- Skip to content link
- Proper heading hierarchy
- ARIA labels for interactive elements
- Keyboard navigation support
- Focus visible states
- Color contrast ratios met

**Required ARIA**:
- `role="dialog"` for modals
- `aria-labelledby` for sections
- `aria-modal="true"` for modals
- `role="progressbar"` with values

---

## Responsive Behavior

**Breakpoints**:
- Desktop: > 768px (full grid)
- Tablet: 768px (adjusted grids)
- Mobile: < 768px (single column)

**Mobile Adjustments**:
- Header stacks vertically
- Metrics cards single column
- Product cards full width
- Tables scroll horizontally
- Modals fullscreen

---

## Print Optimization

```css
@media print {
    .btn, .modal-overlay, .section-actions {
        display: none;
    }
    .product-card, .insight-card {
        box-shadow: none;
        border: 1px solid #ccc;
        page-break-inside: avoid;
    }
    body {
        color: black;
        background: white;
    }
}
```

---

## JavaScript Requirements

**Modal Functionality**:
- Open/close with keyboard (Enter, Escape)
- Focus trap within modal
- Click outside to close
- Prevent body scroll when open

**Progress Bar Animation**:
- Animate on load
- Smooth transitions

**Card Interactions**:
- Hover effects
- Keyboard accessibility (Enter/Space to activate)

---

## Data Requirements Checklist

Before generating dashboard, ensure availability of:

### Project Level
- [ ] Project name
- [ ] Assessment date
- [ ] Overall status
- [ ] Viability score

### Portfolio Metrics
- [ ] Product count
- [ ] Total MVP features
- [ ] Need coverage percentage
- [ ] Validation percentages

### Per Product
- [ ] Product name (60 chars)
- [ ] Target client
- [ ] Status (MVP Ready/In Progress/Planning)
- [ ] Description (250 chars)
- [ ] MVP feature count
- [ ] Requester count
- [ ] Needs covered count
- [ ] Revenue model type
- [ ] Distribution type
- [ ] Business model details (all 4 components)

### Coverage Analysis
- [ ] Fundamental needs list
- [ ] Per-product coverage (MVP/Phased/None)
- [ ] Coverage status

### Strategic Insights
- [ ] 1-2 Strengths
- [ ] 1-2 Opportunities
- [ ] 1-2 Concerns with mitigation
- [ ] 1-2 Recommendations with priority

---

## Quality Assurance

### Visual Standards
- [ ] Consistent color usage
- [ ] Typography hierarchy correct
- [ ] Spacing consistent
- [ ] Cards aligned properly
- [ ] Tables readable

### Content Accuracy
- [ ] Metrics match source documents
- [ ] Product details correct
- [ ] Coverage analysis accurate
- [ ] Insights evidence-based

### Functionality
- [ ] All modals open/close correctly
- [ ] Keyboard navigation works
- [ ] Progress bars animate
- [ ] No console errors

### Responsive
- [ ] Desktop layout correct
- [ ] Tablet adjustments work
- [ ] Mobile readable
- [ ] Tables scroll horizontally

### Accessibility
- [ ] Skip link present
- [ ] ARIA labels complete
- [ ] Focus states visible
- [ ] Heading hierarchy correct

### Performance
- [ ] Single HTML file (inline CSS/JS)
- [ ] No external dependencies
- [ ] Fast loading

---

## Workflow Options

### Standard Generation
1. Gather all Step 12 outputs
2. Verify data checklist complete
3. Generate full dashboard
4. Run quality assurance
5. Deliver HTML file

### Fast-Track (1-2 Products)
1. Use simplified template
2. Single product detail
3. Reduced insights section
4. Quick validation

### Comprehensive (Board Presentation)
1. Full dashboard generation
2. Extended executive summary
3. All product modals complete
4. Detailed coverage analysis
5. Multiple insights per category

---

## Output Files

**Primary Deliverable**:
- `[ProjectName]_Viability_Dashboard.html` - Interactive dashboard

**Template Reference**:
- `templates/Step12_Viability_Dashboard.html`
- `templates/Step12_Dashboard_Template.md` (content structure)

---

## Position in Workflow

**Inputs From**:
- Step 12a: All PMF Sheets
- Step 12b: All Business Model Canvases
- Steps 5-7: Need coverage data
- Step 11: Feature validation data

**Feeds Into**:
- Investment presentations
- Board meetings
- Strategic planning sessions
- Step 13: Financial modeling context

---

## Integration Notes

**Before Dashboard Generation**:
1. Verify all Step 12a PMF Sheets complete
2. Verify all Step 12b Business Model Canvases complete
3. Confirm coherence validation passed
4. Gather portfolio-level metrics

**After Dashboard Generation**:
1. Review with stakeholders
2. Incorporate feedback
3. Finalize for presentation
4. Archive with project documentation

---

*This prompt generates the visualization layer for Step 12. Ensure PMF Sheets (12a) and Business Model Canvases (12b) are complete before proceeding. The dashboard synthesizes all viability work into a stakeholder-ready format.*
