# STEP 12: Viability Dashboard Generation

**Purpose**: Transform Step 12 outputs into professional HTML dashboards for stakeholder presentations
**Output**: Interactive HTML dashboard (self-contained single file)
**Time**: 1-2 hours
**Prerequisites**: Completed Step 12 (all products with PMF + Business Model)

---

## When to Use This Dashboard

**Perfect for**:
- Board presentations on product portfolio strategy
- Investment committee reviews
- Executive summaries of viability assessments
- Strategic planning sessions with leadership
- Investor-facing deliverables
- Quarterly product strategy reviews

**Timing in VIANEO Process**:
- After completing Step 12 Viability Assessment (all products defined)
- When packaging evaluation for committee presentation
- Before entering financial modeling phase (Step 13)
- For ongoing portfolio strategy reviews

---

## Dashboard Generation Prompt Template

```
Generate Professional Viability Dashboard

Project: [Company/Initiative Name]
Purpose: [Viability Assessment Summary | Product Portfolio Strategy | Business Model Validation]

Please:
1. Read complete viability outputs:
   - Product/Market Fit Sheets (all products)
   - Business Model Canvases (all products)
   - Summary Dashboard (markdown version)

2. Use this source data:
   - From Step 12a: Product configurations (MVP features, requesters, resources)
   - From Step 12b: Business models (value props, revenue, distribution, costs)
   - From Steps 5-7: Desirability data (needs, intensity, validation levels)
   - From Step 11: Feasibility data (features, means, partnerships)

3. Dashboard structure needed:
   ☐ Header with project metadata and key portfolio metrics
   ☐ Executive Summary (2-3 paragraphs synthesizing viability)
   ☐ Product Portfolio Grid (interactive cards for each product)
   ☐ Need Coverage Analysis (table showing which products address which needs)
   ☐ Progress Metrics (validation, resource readiness, coherence, coverage)
   ☐ Strategic Insights (strengths, opportunities, concerns, recommendations)
   ☐ Product Detail Modals (full PMF and business model for each product)

4. Design specifications:
   - Single self-contained HTML file
   - Professional VIANEO design system (blue scale: #1a365d primary)
   - Fully responsive (desktop/tablet/mobile)
   - Interactive modals for product details
   - WCAG AA accessible
   - Print-optimized

5. Generate output:
   - Save as: [ProjectName]_Viability_Dashboard_[Date].html
   - Test all interactive elements
   - Verify responsive breakpoints
   - Validate accessibility

Target audience: [Board members / Investors / Executive team / Committee]
Tone: [Strategic / Executive / Investor-facing]
```

---

## Dashboard Structure Components

### 1. Header & Key Metrics

**Project Metadata**:
- Project/initiative name
- Assessment date
- Portfolio status (Planning/In Progress/Ready for Launch)
- Overall viability score (if calculated)

**4 Key Portfolio Metrics**:
1. **Products Defined**: Count of product configurations
2. **MVP Features**: Total features across all products
3. **Need Coverage**: Percentage of fundamental needs addressed
4. **Viability Score**: Overall assessment (if scored)

**Example**:
```html
<header>
  <h1>Acme Healthcare Platform - Viability Assessment</h1>
  <div class="metadata">
    <span>Assessment Date: November 21, 2025</span>
    <span>Status: MVP Ready</span>
    <span>Viability: 4.2/5 (Strong)</span>
  </div>
  <div class="key-metrics">
    <div class="metric">
      <span class="value">3</span>
      <span class="label">Products Defined</span>
    </div>
    <div class="metric">
      <span class="value">24</span>
      <span class="label">MVP Features</span>
    </div>
    <div class="metric">
      <span class="value">100%</span>
      <span class="label">Need Coverage</span>
    </div>
    <div class="metric">
      <span class="value">4.2/5</span>
      <span class="label">Viability Score</span>
    </div>
  </div>
</header>
```

---

### 2. Executive Summary

**Content**: 2-3 paragraphs (150-200 words total) synthesizing:

**Paragraph 1**: Portfolio overview
- Number of products
- Market coverage
- Validation strength

**Paragraph 2**: Product-market fit quality and business model coherence
- MVP validation rates
- Business model alignment
- Resource readiness

**Paragraph 3**: Critical success factors and primary recommendation
- Key strengths
- Primary concerns
- Strategic recommendation

**Example**:
```
This viability assessment evaluates three product configurations serving distinct healthcare segments: Patient Portal (facilities), Provider Network (medical practices), and Analytics Suite (hospital systems). All 12 fundamental customer needs are addressed across the portfolio, with 85% of MVP features validated through 5+ customer interviews.

Product-market fit is strongest for the Patient Portal, with all 8 MVP features validated and a coherent subscription-based business model. Provider Network and Analytics Suite are in development, sharing 60% of cost structure (infrastructure, support) enabling portfolio efficiency. All business models demonstrate internal coherence and sustainable unit economics at scale.

Primary recommendation: Launch Patient Portal Q2 2026 (strongest validation, clearest market need), followed by Provider Network in Q4 2026. Critical success factor: Validate pricing assumptions ($49/month for Patient Portal) through willingness-to-pay research with 10 prospects before finalizing launch.
```

---

### 3. Product Portfolio Grid

**Interactive product cards** (one per product):

**Each card displays**:
- Product name
- Brief description (1-2 sentences)
- Status badge (MVP Ready / In Progress / Planning / Blocked)
- Key metrics:
  - MVP features count
  - Requesters targeted
  - Needs covered
- Business model tags:
  - Revenue model type
  - Distribution channel type
- "View Details" button → opens modal

**Example Card**:
```html
<div class="product-card mvp-ready" onclick="openModal('product1')">
  <div class="status-badge">MVP Ready</div>
  <h3>Patient Portal</h3>
  <p class="description">Compliance automation platform for healthcare facilities with pre-built regulatory templates.</p>
  <div class="metrics">
    <span>8 MVP Features</span>
    <span>2 Requesters</span>
    <span>5 Needs</span>
  </div>
  <div class="tags">
    <span class="tag revenue">Subscription</span>
    <span class="tag distribution">Direct + Partners</span>
  </div>
  <button>View Details</button>
</div>
```

---

### 4. Need Coverage Analysis

**Comparison table**: Needs (rows) × Products (columns)

**Shows**:
- All fundamental needs (from Step 7)
- Which products address each need
- Coverage strength (Strong / Partial / Gap)
- Overall coverage percentage

**Example**:
```html
<table class="need-coverage">
  <thead>
    <tr>
      <th>Fundamental Need</th>
      <th>Patient Portal</th>
      <th>Provider Network</th>
      <th>Analytics Suite</th>
      <th>Coverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Automate audit preparation</td>
      <td class="strong">✓ MVP</td>
      <td class="partial">Phased</td>
      <td class="none">—</td>
      <td class="strong">Strong</td>
    </tr>
    <tr>
      <td>Track regulatory changes</td>
      <td class="strong">✓ MVP</td>
      <td class="strong">✓ MVP</td>
      <td class="none">—</td>
      <td class="strong">Strong</td>
    </tr>
    <!-- More rows -->
  </tbody>
</table>
```

---

### 5. Progress Metrics (4 Categories)

**Visualized as progress bars**:

1. **MVP Validation**: % of MVP features with >5 interview validation
2. **Resource Readiness**: % of critical resources secured
3. **Business Model Coherence**: % of products with aligned models
4. **Need Coverage**: % of fundamental needs with feature coverage

**Example**:
```html
<div class="progress-metrics">
  <div class="metric">
    <label>MVP Validation</label>
    <div class="progress-bar">
      <div class="fill" style="width: 85%">85%</div>
    </div>
  </div>
  <div class="metric">
    <label>Resource Readiness</label>
    <div class="progress-bar">
      <div class="fill" style="width: 70%">70%</div>
    </div>
  </div>
  <div class="metric">
    <label>Business Model Coherence</label>
    <div class="progress-bar">
      <div class="fill" style="width: 95%">95%</div>
    </div>
  </div>
  <div class="metric">
    <label>Need Coverage</label>
    <div class="progress-bar">
      <div class="fill" style="width: 100%">100%</div>
    </div>
  </div>
</div>
```

---

### 6. Strategic Insights (4-6 Cards)

**Insight types**:
- **Strengths** (green left border): Validated and ready
- **Opportunities** (blue left border): Portfolio efficiency, synergies
- **Concerns** (orange left border): Gaps, risks, dependencies
- **Recommendations** (primary border): Priority actions

**Each insight card includes**:
- Type indicator (color-coded)
- Title (5-8 words)
- Description (2-3 sentences with evidence)
- Products affected
- Priority level (High/Medium/Low)

**Example**:
```html
<div class="insights">
  <div class="insight strength">
    <h4>Patient Portal MVP Fully Validated</h4>
    <p>All 8 MVP features validated through 5+ customer interviews, with 100% of fundamental needs addressed. Ready for Q2 2026 launch.</p>
    <div class="meta">
      <span class="products">Patient Portal</span>
      <span class="priority high">High Priority</span>
    </div>
  </div>

  <div class="insight opportunity">
    <h4>60% Shared Cost Structure Across Products</h4>
    <p>Provider Network and Analytics Suite share infrastructure, support, and content updates, enabling portfolio efficiency and reduced per-product operational costs.</p>
    <div class="meta">
      <span class="products">Provider Network, Analytics Suite</span>
      <span class="priority medium">Medium Priority</span>
    </div>
  </div>

  <div class="insight concern">
    <h4>Pricing Unvalidated for Patient Portal</h4>
    <p>$49/month assumption not tested with prospects. Risk of pricing too high or too low, impacting conversion and revenue projections.</p>
    <div class="meta">
      <span class="products">Patient Portal</span>
      <span class="priority high">High Priority</span>
    </div>
  </div>

  <div class="insight recommendation">
    <h4>Launch Patient Portal Q2 2026</h4>
    <p>Prioritize Patient Portal (strongest validation) for Q2 2026 launch. Conduct willingness-to-pay research with 10 prospects before finalizing pricing.</p>
    <div class="meta">
      <span class="products">Patient Portal</span>
      <span class="priority high">High Priority</span>
    </div>
  </div>
</div>
```

---

### 7. Product Detail Modals

**Triggered by clicking product cards**

**Modal content for each product**:

**Product Identity** (4-metric grid):
- Client segment
- MVP features count
- Requesters targeted
- Timeline to launch

**MVP Features** (bulleted list):
- Feature name
- MVP/Phased badge
- Timeline

**Business Model** (4-component grid):
- Value proposition
- Revenue stream
- Distribution channel
- Cost structure

**Resource Requirements**:
- Means required
- Critical partners
- Identified gaps

**Example Modal Structure**:
```html
<div id="modal-product1" class="modal">
  <div class="modal-content">
    <h2>Patient Portal - Product Details</h2>

    <section class="product-identity">
      <div class="metric">
        <label>Client Segment</label>
        <span>Healthcare Facilities</span>
      </div>
      <div class="metric">
        <label>MVP Features</label>
        <span>8</span>
      </div>
      <div class="metric">
        <label>Requesters</label>
        <span>2</span>
      </div>
      <div class="metric">
        <label>Timeline</label>
        <span>Q2 2026</span>
      </div>
    </section>

    <section class="features">
      <h3>MVP Features</h3>
      <ul>
        <li>
          <span class="badge mvp">MVP</span>
          Automated Audit Checklist Generator (3 months)
        </li>
        <!-- More features -->
      </ul>
    </section>

    <section class="business-model">
      <h3>Business Model</h3>
      <div class="grid-4">
        <div>
          <h4>Value Proposition</h4>
          <p>Reduce audit prep time by 80% through pre-built templates</p>
        </div>
        <div>
          <h4>Revenue Stream</h4>
          <p>Subscription: $49/user/month</p>
        </div>
        <div>
          <h4>Distribution</h4>
          <p>Partner referrals + conferences</p>
        </div>
        <div>
          <h4>Cost Structure</h4>
          <p>$260k dev, $210k/year ops</p>
        </div>
      </div>
    </section>

    <section class="resources">
      <h3>Resource Requirements</h3>
      <p><strong>Means:</strong> 3 backend engineers, 2 frontend engineers, UX designer</p>
      <p><strong>Partners:</strong> Regulatory consulting firm (content validation)</p>
      <p><strong>Gaps:</strong> HIPAA compliance expertise (mitigation: engage auditor, $25k budgeted)</p>
    </section>

    <button class="close" onclick="closeModal('product1')">Close</button>
  </div>
</div>
```

---

## Design System Standards

### VIANEO Color Palette

**Primary Blue Scale**:
- **Primary Dark**: `#1a365d` (headers, primary text)
- **Primary**: `#2c5282` (interactive elements, gradients)
- **Primary Light**: `#4a5d7f` (hover states)

**Neutral Scale**:
- **Surface**: `#ffffff` (cards, backgrounds)
- **Background**: `#f7fafc` (page background)
- **Border**: `#e2e8f0` (dividers, card borders)
- **Text**: `#2d3748` (body text)
- **Text Light**: `#4a5568` (secondary text)

**Status Colors**:
- **Success/Ready**: `#10b981` (green) - MVP ready, high validation
- **Warning/In Progress**: `#f59e0b` (orange) - in progress, medium priority
- **Info/Planning**: `#3b82f6` (blue) - planning phase
- **Danger/Blocked**: `#ef4444` (red) - high priority concerns, blocked

---

### Typography

**Font Stack**:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
```

**Sizes & Weights**:
- **H1**: 32px, weight 700, color #1a365d
- **H2**: 24px, weight 700, color #1a365d
- **H3**: 20px, weight 600, color #2d3748
- **H4**: 16px, weight 600, color #2d3748
- **Body**: 16px, weight 400, color #4a5568
- **Small**: 14px, weight 400, color #718096
- **Meta**: 12px, weight 500, color #718096

---

### Spacing System

**Base unit**: 8px

**Scale**:
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- 2xl: 48px

**Section margins**: 48px between major sections
**Card padding**: 24px internal
**Grid gaps**: 20px between grid items

---

### Components

**Product Cards**:
- Background: white
- Border: 2px solid #e2e8f0
- Border-radius: 12px
- Padding: 24px
- Hover: Border color #2c5282, subtle shadow, translateY(-2px)

**Status Badges**:
- Background: Status color with 0.1 opacity
- Text: Status color
- Border-radius: 12px
- Padding: 4px 12px
- Font-size: 11px
- Font-weight: 600
- Text-transform: uppercase

**Progress Bars**:
- Height: 8px
- Background: #e2e8f0
- Fill: Gradient (primary colors)
- Border-radius: 4px
- Animated fill (transition 0.3s ease)

**Modals**:
- Background: white
- Border-radius: 12px
- Max-width: 800px
- Padding: 32px
- Header: Gradient primary colors
- Overlay: rgba(0, 0, 0, 0.5)

**Buttons**:
- Background: #2c5282
- Color: white
- Border-radius: 8px
- Padding: 12px 24px
- Font-weight: 600
- Hover: Background #1a365d, translateY(-1px)

---

### Interactive States

**Hover**:
- Transition: 0.2s ease
- Border color change
- Subtle shadow: `0 4px 8px rgba(0,0,0,0.1)`
- TranslateY: -2px

**Focus**:
- Outline: 4px solid #2c5282 with 0.3 opacity
- Offset: 2px

**Active**:
- TranslateY: 0
- Shadow: none

**Transitions**:
- All: 0.15-0.3s ease
- Modal fade-in: 0.2s

---

## Responsive Design

### Desktop (1200px+)
- Product cards: 3-column grid
- Full comparison table visible
- Modals: 800px max-width, centered

### Tablet (768-1199px)
- Product cards: 2-column grid
- Comparison table: Horizontal scroll
- Modals: Full width with 20px margins

### Mobile (<768px)
- Product cards: Single column, stacked
- Header: Vertical layout
- Key metrics: Single column
- Modals: Full screen with scroll
- Comparison table: Horizontal scroll, sticky first column

---

## Accessibility Requirements

**WCAG AA Compliance**:
- Color contrast: 4.5:1 minimum (body text)
- Color contrast: 3:1 minimum (large text, UI components)
- Keyboard navigation: All interactive elements accessible via Tab
- Focus indicators: Visible on all focusable elements
- ARIA labels: On progress bars, modals, buttons
- Semantic HTML: Proper heading hierarchy, landmarks
- Alt text: On all images (if any)

**Keyboard Navigation**:
- Tab: Navigate through interactive elements
- Enter/Space: Activate buttons, open modals
- Escape: Close modals
- Focus trap: In modals (Tab cycles within modal)

---

## File Naming Convention

```
[ProjectName]_Viability_Dashboard_[YYYYMMDD]_[Version].html
```

**Examples**:
- `AcmeCorp_Viability_Dashboard_20251121_v1.html`
- `HealthTech_Viability_Dashboard_20251121_Board.html`
- `MVPStrategy_Viability_Dashboard_20251121_Investment.html`

---

## Quality Checklist

Before delivery, verify:

### Visual Standards
- [ ] VIANEO color palette consistent (#1a365d primary)
- [ ] Spacing system (8px base unit) throughout
- [ ] Typography hierarchy clear
- [ ] Status colors match conventions
- [ ] No placeholder text remaining

### Content Accuracy
- [ ] All product names correct and consistent
- [ ] All metrics have real values (no placeholders)
- [ ] All percentages verified against source data
- [ ] Character counts respected (≤250 chars where applicable)
- [ ] Need coverage table matches products

### Functionality
- [ ] Product cards clickable (all open modals)
- [ ] Modals close on button, overlay, and Escape
- [ ] Progress bars animate on page load
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Focus trap in modals working

### Responsive Design
- [ ] Desktop (1200px+): 3-column grid displays
- [ ] Tablet (768-1199px): 2-column reflow
- [ ] Mobile (<768px): Single column stack
- [ ] Modals readable on all devices
- [ ] Tables scroll horizontally on mobile

### Accessibility
- [ ] Keyboard accessible (Tab navigation)
- [ ] ARIA labels on progress bars and modals
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Semantic HTML structure
- [ ] Focus management in modals

### Performance
- [ ] Single file, no external dependencies
- [ ] File size <250KB
- [ ] Loads in <2 seconds
- [ ] No console errors
- [ ] Smooth animations

---

## Dashboard Variants

### Variant 1: Portfolio Summary (Standard)
**Focus**: Overall portfolio strategy
**Sections**: All sections included
**Audience**: Board, investment committee
**Time**: 1-2 hours

### Variant 2: Business Model Comparison
**Focus**: Commercial viability
**Sections**: Emphasize business model grid, revenue models, cost structure
**Audience**: CFO, finance leadership
**Time**: 1 hour

### Variant 3: MVP Strategy
**Focus**: Product development
**Sections**: Emphasize MVP features, resource requirements, timelines
**Audience**: Product team, engineering leadership
**Time**: 1 hour

### Variant 4: Strategic Viability
**Focus**: Comprehensive assessment
**Sections**: All sections + expanded insights
**Audience**: Board of directors, strategic advisors
**Time**: 2 hours

---

## Integration with VIANEO Workflow

**Standard Workflow**:
1. Complete Step 12 Viability (all products with PMF + Business Model)
2. Review all deliverables for dashboard-worthy content
3. Collect data using this guide (1-2 hours)
4. Generate dashboard (1-2 hours)
5. Quality check against validation checklist (30 min)
6. Stakeholder preview for feedback (optional)
7. Final delivery as single HTML file

**Fast Track** (single product, quick summary):
- Complete Step 12 for 1 core product
- Generate simplified dashboard (header, summary, 1 product card, key insights)
- Skip comparison tables
- Time: 1 hour

**Complete Track** (full board presentation):
- Complete Step 12 for all products (3+)
- Generate full dashboard with all sections
- Interactive modals with complete business models
- Full need coverage comparison
- 4-6 strategic insights
- Time: 2 hours

---

## Next Steps After Dashboard Generation

Once dashboard is generated:

1. **Present to Stakeholders**: Use in investment committee or board presentation
2. **Gather Feedback**: Document concerns or strategic questions
3. **Proceed to Financial Modeling** (if applicable): Quantify revenue, costs, projections
4. **Update Dashboard**: Revise as new validation data emerges
5. **Archive**: Save version-controlled copies as portfolio evolves

---

**The Viability Dashboard transforms analytical outputs into executive-ready visual portfolio strategy that drives investment and go-to-market decisions.**
