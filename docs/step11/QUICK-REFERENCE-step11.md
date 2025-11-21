# Step 11 Features & Needs Matrix - Quick Reference Guide

## Quick Start (5 Minutes)

1. **Copy Template**: Start with `step11-features-needs-TEMPLATE.html`
2. **Update Project Info**: Change title, subtitle, and stats in header
3. **Define Columns**: Add your partner and means column headers
4. **Add Features**: Copy example rows, update feature names and timing
5. **Map Relationships**: Fill in partner names or add checkmarks for means
6. **Save & Test**: Open in browser, test toggle, export, and print

---

## Essential Structure

```html
<!DOCTYPE html>
<html>
<head>
    <style>/* CSS from template */</style>
</head>
<body>
    <div class="card">
        <header class="header">
            <!-- Title, stats, toggle, buttons -->
        </header>
        <main class="table-container">
            <div class="view-header">PARTNERS</div>
            <div class="table-scroll">
                <table class="matrix-table">
                    <!-- Your data here -->
                </table>
            </div>
        </main>
        <footer class="legend-footer">
            <!-- Opportunity legend -->
        </footer>
    </div>
    <script>/* JavaScript from template */</script>
</body>
</html>
```

---

## Critical Rules

### Column Matching
✅ **DO**: Ensure cell count matches column count in EVERY row
❌ **DON'T**: Add different number of cells per row

### Data-View Attributes
✅ **DO**: Add `data-view="partners"` to all partner columns/cells
✅ **DO**: Add `data-view="means"` to all means columns/cells
✅ **DO**: Add `class="hidden"` to means columns/cells initially

### Timing Badges
Use exactly four types:
- `timing-available` - Already Available (green)
- `timing-short` - Short-term 0-6 months (blue)
- `timing-mid` - Mid-term 6-12 months (yellow)
- `timing-long` - Long-term 12+ months (orange)

---

## Color Palette (Exact Hex Values)

### Primary Colors
```
Navy Blue:        #1a365d
Navy Light:       #2c5282
White:            #ffffff
Border Gray:      #e2e8f0
```

### Opportunity Colors
```
High (Green):     #0f9d58
Medium (Yellow):  #f4b400
Low (Orange):     #ef6c00
Expected (Blue):  #1a73e8
Accessory (Gray): #5f6368
```

### Row Backgrounds
```
High:             #e8f5e9 (light green)
Medium:           #fff9e6 (light yellow)
Low:              #fff3e0 (light orange)
Expected:         #e8f0fe (light blue)
Accessory:        #f5f5f5 (light gray)
```

---

## Typography Scale

```
Header Title:     16px, weight 600
Stats Values:     20px, weight 700
Stats Labels:     9px
View Header:      11px, weight 600
Table Headers:    10px, weight 600, uppercase
Table Cells:      11px
Timing Badges:    10px, weight 500
Partner Text:     11px, weight 500
```

---

## Spacing System (8px Base)

```
Extra Small:      4px
Small:            8px
Medium:           16px
Large:            24px
Extra Large:      32px

Cell Padding:     12px 16px
Header Padding:   10px 20px
```

---

## Common Customization Points

### 1. Header Section
```html
<h1 class="header-title">Features & Needs Matrix</h1>
<p class="header-subtitle">[YOUR PROJECT NAME]</p>

<div class="stat-inline">
    <span class="stat-inline-value">[NUMBER]</span>
    <span class="stat-inline-label">[LABEL]</span>
</div>
```

### 2. Column Headers
```html
<!-- Partners (5-7 columns) -->
<th scope="col" data-view="partners">[CATEGORY NAME]</th>

<!-- Means (7-10 columns) -->
<th scope="col" class="hidden" data-view="means">[RESOURCE TYPE]</th>
```

### 3. Feature Rows
```html
<tr data-opportunity="high">
    <th scope="row">[FEATURE NAME]</th>
    <td>
        <span class="timing-badge timing-[TYPE]">
            <svg viewBox="0 0 12 12">...</svg>
            [TIMING TEXT]
        </span>
    </td>
    <!-- Partner cells -->
    <td data-view="partners"></td>
    <td data-view="partners">
        <div class="partner-text">[Partner Name]</div>
    </td>
    <!-- Means cells -->
    <td class="hidden" data-view="means">
        <div class="check" role="img" aria-label="Required"></div>
    </td>
    <td class="hidden" data-view="means"></td>
</tr>
```

---

## Cell Type Options

### Empty Cell
```html
<td data-view="partners"></td>
```

### Partner Text
```html
<td data-view="partners">
    <div class="partner-text">AWS</div>
</td>
```

### Checkmark (Means)
```html
<td class="hidden" data-view="means">
    <div class="check" role="img" aria-label="Required"></div>
</td>
```

---

## Timing Badge SVG Icons

### Checkmark (Already Available)
```html
<svg viewBox="0 0 12 12" aria-hidden="true">
    <path d="M10 3L4.5 8.5L2 6"/>
</svg>
```

### Circle (All Others)
```html
<svg viewBox="0 0 12 12" aria-hidden="true">
    <circle cx="6" cy="6" r="5"/>
</svg>
```

---

## Opportunity Level Mapping

Set `data-opportunity` attribute on `<tr>`:

```html
<tr data-opportunity="high">      <!-- Green background -->
<tr data-opportunity="medium">    <!-- Yellow background -->
<tr data-opportunity="low">       <!-- Orange background -->
<tr data-opportunity="expected">  <!-- Blue background -->
<tr data-opportunity="accessory"> <!-- Gray background -->
```

---

## Keyboard Shortcuts

Built into every matrix:

- **Ctrl/Cmd + E**: Export CSV
- **Ctrl/Cmd + P**: Print
- **Ctrl/Cmd + T**: Toggle views
- **Tab**: Navigate to toggle
- **Enter/Space**: Activate toggle when focused

---

## Common Column Examples

### Partners View (External Dependencies)
- Technology Stack
- Data Sources
- IoT Hardware
- Integration Partners
- Design/UX Resources
- Service Providers
- Cloud Platform
- Analytics Tools
- Regulatory Bodies
- Payment Gateway

### Means View (Internal Resources)
- Internal Team
- Contractors/Freelancers
- Open Source Tools
- SaaS Platforms
- Cloud Services (AWS, Azure, GCP)
- Budget/Funding
- Equipment/Hardware
- Licenses
- Consulting
- Research Grants

---

## Recommended Scope

**Optimal Configuration**:
- **Features**: 10-12 (fits viewport without scrolling)
- **Partner Columns**: 5-7 (readable width)
- **Means Columns**: 7-10 (comprehensive coverage)

**Why These Numbers?**:
- More features = vertical scrolling (less ideal for presentations)
- More columns = horizontal scrolling or tiny text
- This balance = professional, readable, fits 16:9 screens

---

## Troubleshooting Quick Fixes

### Toggle Not Working
1. Check `data-view` attributes on ALL columns
2. Verify means columns have `class="hidden"`
3. Check browser console for JavaScript errors

### Columns Misaligned
1. Count cells in row, compare to header count
2. Look for missing or extra `<td>` tags
3. Use browser DevTools to inspect table

### Export Fails
1. Check for special characters (commas, quotes) in text
2. Verify table structure is valid HTML
3. Try different browser

### Visual Issues
1. Compare hex colors to reference guide
2. Check font sizes match typography scale
3. Verify spacing uses 8px multiples

---

## File Naming Convention

```
[project-name]-features-needs-matrix.html
[project-name]-features-partners-matrix.html
[project-name]-features-means-matrix.html
```

Examples:
- `marine-data-features-needs-matrix.html`
- `education-platform-features-partners-matrix.html`
- `healthcare-app-features-means-matrix.html`

---

## Testing Checklist

Before sharing:
- [ ] Title and subtitle correct
- [ ] Stats accurate
- [ ] All features listed
- [ ] Timing badges correct
- [ ] Toggle switches views smoothly
- [ ] Partner relationships mapped
- [ ] Means requirements identified
- [ ] CSV export works for both views
- [ ] Print preview looks good
- [ ] No browser console errors
- [ ] Keyboard navigation works
- [ ] Opens correctly when shared

---

## Integration with Vianeo Framework

**Upstream Dependencies**:
- Step 7: Requesters → Customer segments
- Step 8: Functionalities → Feature requirements
- Step 9: Solution Definition → Technical approach

**Downstream Uses**:
- Step 12: Features & Means → Detailed resource planning
- MVP Definition → High opportunity features
- Resource Planning → Means become budget items
- Timeline Development → Timing badges inform schedule

**This Matrix Answers**:
- Which features address which needs?
- What external partners are required?
- What internal resources are needed?
- What's the implementation timeline?
- What are the highest opportunity features?

---

## Pro Tips

1. **Start with Data**: Gather all feature info before building HTML
2. **Use Reference**: Copy working example, modify incrementally
3. **Test Early**: Verify toggle after adding just 2-3 rows
4. **Keep Consistent**: Use same structure across all project matrices
5. **Version Control**: Save dated backups before major changes
6. **Mobile Testing**: Check on smaller screens (responsive design included)
7. **Accessibility**: Never remove ARIA attributes or keyboard support
8. **Print Test**: Always check print preview before finalizing

---

## Common Mistakes to Avoid

❌ Mixing up `data-view="partners"` and `data-view="means"`
❌ Forgetting `class="hidden"` on means columns
❌ Different cell counts per row
❌ Removing JavaScript or breaking event listeners
❌ Changing CSS variable names without updating references
❌ Using more than 15 features (causes scrolling)
❌ More than 8 partner columns (width issues)
❌ Removing accessibility features

---

## When to Get Help

Contact support if:
- Toggle mechanism completely broken (not just data issues)
- Need more than 2 toggle views (requires significant JS changes)
- Need custom visualizations beyond checkmarks/text
- Need integration with external data sources
- Need real-time collaboration features

For simple issues:
- Check this guide first
- Review REBUILD-GUIDE-Features-Needs-Matrix.md
- Compare to working reference file
- Use browser DevTools to inspect elements

---

## Success Metrics

Your matrix is ready when:
- ✅ Looks professional (BCG/McKinsey grade)
- ✅ Toggle works smoothly
- ✅ Export produces valid CSV
- ✅ Print preview is clean
- ✅ No console errors
- ✅ Accessible via keyboard
- ✅ Opens correctly when shared
- ✅ Stakeholders can use it without questions

---

**Remember**: This is a presentation-grade deliverable. Every detail matters. When in doubt, reference the working example file.
