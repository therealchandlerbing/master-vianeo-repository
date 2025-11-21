# Step 11: Features-Needs Matrix Quick Reference
## Vianeo Business Model Evaluation Framework

---

## At a Glance

| Attribute | Value |
|-----------|-------|
| **Phase** | Business Model Design (First Step) |
| **Duration** | 30-45 minutes |
| **Prerequisites** | Steps 0-10 complete |
| **Inputs** | 10 needs + 5-10 features |
| **Outputs** | HTML matrix + MD analysis |
| **Key Metric** | High-opportunity coverage |
| **Success Threshold** | All critical needs addressed |

---

## Color Codes

| Level | Color | Hex | Icon |
|-------|-------|-----|------|
| **High Opportunity** | Green | #0f9d58 | Circle r="7" |
| **Medium Opportunity** | Yellow | #f4b400 | Circle r="5" |
| **Low Opportunity** | Orange | #ef6c00 | Circle r="4" |
| **Expected** | Blue | #1a73e8 | Star outline |
| **Accessory** | Gray | #5f6368 | Circle r="3" |

---

## Coverage Targets

| Metric | Target | Warning |
|--------|--------|---------|
| **Overall Coverage** | 40-80% | <30% or >85% |
| **High Opportunity** | 100% | <100% |
| **Expected** | 70%+ | <50% |
| **Accessory** | <30% | >50% |

---

## Coverage Formula

```
Coverage Rate = (Total Checkmarks / (Features × Needs)) × 100
```

**Example:** 8 features × 10 needs = 80 cells. 52 checkmarks = 65% coverage.

---

## Checkmark Criteria

**Mark ✓ ONLY when:**
1. Feature directly solves the need
2. User would find feature valuable for this need
3. Connection is obvious

**Leave empty when:**
- Connection is indirect
- Feature alone doesn't deliver value
- You have to rationalize the connection

---

## MVP Scoping

```
MVP = Features covering (All High + All Expected)
      minus Features only covering (Accessory + Low)
```

**Defer in order:**
1. Accessory features
2. Low-opportunity features
3. Medium non-differentiators
4. Partnership-dependent features

---

## 6-Phase Workflow

| Phase | Time | Action |
|-------|------|--------|
| 1. Gather Inputs | 5-10 min | Needs from Step 7 + features list |
| 2. Map Coverage | 10-15 min | Mark checkmarks conservatively |
| 3. Calculate Metrics | 2-3 min | Coverage %, high-opp count |
| 4. Build HTML | 5-10 min | Use template, add data |
| 5. Create Analysis | 5-10 min | Strengths, gaps, recommendations |
| 6. Quality Check | 5 min | Validate against checklist |

---

## Required Files

**Create:**
- `[project]-features-needs-matrix.html`
- `[project]-matrix-analysis.md`

**Reference:**
- `Step11_FeaturesNeeds_Matrix_Template.html`
- `Step11_FeaturesNeeds_Analysis_Template.md`

---

## HTML Structure

```html
<div class="card">
    <header class="header">
        <!-- Title, subtitle, inline stats, buttons -->
    </header>
    <div class="content">
        <div class="matrix-wrapper">
            <table class="matrix-table">
                <thead><!-- Feature columns --></thead>
                <tbody><!-- Need rows with checkmarks --></tbody>
            </table>
        </div>
    </div>
    <footer class="legend-footer">
        <!-- 5 opportunity levels -->
    </footer>
</div>
```

---

## CSS Classes by Opportunity

| Level | Row Class | Background |
|-------|-----------|------------|
| High | `opportunity-high` | #e8f5e9 |
| Medium | `opportunity-medium` | #fff9e6 |
| Low | `opportunity-low` | #fff3e0 |
| Expected | `expected` | #e8f0fe |
| Accessory | `accessory` | #f5f5f5 |

---

## Sticky Positioning

```css
/* Header row */
thead th { position: sticky; top: 0; z-index: 10; }

/* First column */
tbody th { position: sticky; left: 0; z-index: 5; }

/* Corner cell */
thead th:first-child { position: sticky; left: 0; top: 0; z-index: 20; }
```

---

## JavaScript Functions

```javascript
// Export CSV
document.getElementById('exportBtn').addEventListener('click', function() {
    // Extract table data, create CSV, download
});

// Print
document.getElementById('printBtn').addEventListener('click', function() {
    window.print();
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'e') {
        e.preventDefault();
        document.getElementById('exportBtn').click();
    }
    if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
        e.preventDefault();
        document.getElementById('printBtn').click();
    }
});
```

---

## Analysis Structure

```markdown
# Features-Needs Matrix Analysis

## Coverage Overview
- Total Features: X
- Total Needs: 10
- Overall Coverage: XX%
- High Opportunity: X/X

## Key Findings
### Strengths
### Critical Gaps

## Strategic Recommendations
### Priority Development
### Feature Optimization

## MVP Definition
### Must-Have
### Defer to Post-Launch

## Next Steps
```

---

## Critical Checks

- [ ] All 10 needs included
- [ ] Opportunity levels correct
- [ ] Checkmarks accurate
- [ ] Coverage % calculated
- [ ] Export button works
- [ ] Print button works
- [ ] Sticky headers function
- [ ] Analysis complete

---

## Warning Signs

| Pattern | Diagnosis | Action |
|---------|-----------|--------|
| Coverage <30% | Features too narrow or wrong solution | Review definitions |
| Coverage >85% | Features too broad | Decompose features |
| Scattered marks | Unfocused strategy | Define core value |
| High-opp gap | Critical failure | Priority development |

---

## Integration

**Pulls from:**
- Step 7: Validated needs
- Step 5: Need definitions
- Step 4: Solution description
- Step 10: Diagnostic insights

**Feeds into:**
- Technical feasibility
- Resource planning
- Partnership strategy
- Go-to-market
- Product roadmap

---

## Delivery Message Template

```
Created Features-Needs Matrix with X features × 10 needs.

**Metrics:** XX% coverage, X/X high-opportunity

**Files:**
- [Matrix HTML](link)
- [Analysis MD](link)

**Shortcuts:** Ctrl+E (export), Ctrl+P (print)

**Key Insight:** [Main finding]

**Action:** [Top priority]
```

---

*Step 11 Quick Reference | Vianeo Framework v2.0*
