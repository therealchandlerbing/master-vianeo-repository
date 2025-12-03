# Step 12: Viability Dashboard Generation

## Overview

Transform Step 12 Viability Assessment outputs (PMF Sheets and Business Model Canvases) into professional HTML dashboards for executive stakeholders, investment committees, and board presentations.

## Purpose

Generate presentation-grade interactive dashboards that visualize product-market fit validation, business model coherence, and portfolio-level viability insights.

---

## Instructions for AI Assistant

Using completed PMF Sheets (Step 12a) and Business Model Canvases (Step 12b), generate a comprehensive Viability Dashboard. Include portfolio metrics, product cards with modals, need coverage analysis, progress indicators, and strategic insights. Follow the design specifications exactly. Output as responsive, accessible HTML.

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

## Dashboard Structure

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
