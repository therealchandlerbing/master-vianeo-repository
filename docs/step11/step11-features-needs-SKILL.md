# Step 11: Features & Needs Matrix Builder

## Overview

This skill enables creation of professional, interactive HTML dashboards for Vianeo Innovation Framework Step 11 (Features & Needs/Feasibility). These matrices map product features against external dependencies (Partners) or internal resources (Means) with toggle functionality, export capabilities, and executive-grade visual design.

**Primary Use Case**: When users request Step 11 analysis, features/needs matrix, feasibility assessment, or partner/means mapping for any project.

## When to Use This Skill

Trigger this skill when users request:
- "Build a Step 11 matrix for [project]"
- "Create a features and needs analysis"
- "Map features to partners and means"
- "Generate a feasibility dashboard"
- "Build a features matrix with toggle views"

## Core Principles

### 1. Vianeo Framework Context
Step 11 sits at the intersection of customer needs and technical feasibility. It answers:
- Which features address which requester needs?
- What partners/dependencies does each feature require?
- What internal resources (means) are needed?
- What's the implementation timeline for each feature?

### 2. Visual Standards
- **Format**: 16:9 landscape, no scrolling in viewport
- **Design Quality**: BCG/McKinsey presentation grade
- **Color System**: Opportunity levels with exact hex colors
- **Typography**: Inter font family, 8px-based spacing
- **Interactivity**: Smooth toggle transitions, keyboard navigation

### 3. Dual-View Architecture
Every matrix has TWO views accessible via toggle:
- **Partners View**: External dependencies, third-party integrations, service providers
- **Means View**: Internal resources, team capacity, budget, tools, infrastructure

## Build Process

### Phase 1: Requirements Gathering

Ask the user to provide:

1. **Project Context**
   - Project name and description
   - Target industry/domain
   - Primary value proposition

2. **Features List (10-12 recommended)**
   - Core feature names
   - Brief descriptions
   - Implementation timing for each:
     * Already Available
     * Short-term (0-6 months)
     * Mid-term (6-12 months)
     * Long-term (12+ months)

3. **Partners View Data (5-7 columns)**
   Common categories:
   - Technology Stack (specific partner if known)
   - Data Sources
   - Integration Partners
   - Design/UX Resources
   - Service Providers
   - Regulatory/Compliance Bodies

4. **Means View Data (7-10 columns)**
   Common categories:
   - Internal Team
   - Contractors/Freelancers
   - Open Source Tools
   - SaaS Platforms
   - Budget/Funding
   - Equipment/Hardware
   - Licenses
   - Cloud Services
   - Consulting
   - Research/Grants

5. **Key Statistics**
   For header display (e.g., "12 Features", "5 Categories", "8 Partners")

### Phase 2: Data Validation

Before building, verify:
- Feature count is 10-12 (optimal for viewport fit)
- Partner columns: 5-7 (optimal width)
- Means columns: 7-10 (adequate coverage)
- Every feature has timing assigned
- Partner relationships are identified (checkmarks or partner names)
- Means requirements are mapped (checkmarks for required resources)

### Phase 3: HTML Construction

Build the complete self-contained HTML file:

1. **Document Structure**
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>Features & Needs Matrix | [Project Name]</title>
       <style>/* Complete CSS */</style>
   </head>
   <body>
       <div id="liveRegion" class="sr-only"></div>
       <div class="card">
           <header class="header">...</header>
           <main class="table-container">...</main>
           <footer class="legend-footer">...</footer>
       </div>
       <script>/* Complete JavaScript */</script>
   </body>
   </html>
   ```

2. **Header Section**
   - Project title and subtitle
   - Key statistics (inline, compact)
   - Toggle switch (Partners ↔ Means)
   - Export CSV button
   - Print button

3. **View Header**
   - Dynamic text: "PARTNERS" or "MEANS"
   - Updates automatically on toggle

4. **Table Structure**
   ```html
   <table class="matrix-table">
       <thead>
           <tr>
               <th>FEATURE</th>
               <th>IMPLEMENTATION TIMING</th>
               <!-- Partner columns with data-view="partners" -->
               <!-- Means columns with class="hidden" data-view="means" -->
           </tr>
       </thead>
       <tbody>
           <!-- Feature rows -->
       </tbody>
   </table>
   ```

5. **Feature Rows**
   Each row contains:
   - Feature name in row header
   - Timing badge with icon and text
   - Partner cells (visible by default)
   - Means cells (hidden by default with class="hidden")

   **Critical**: Cell count MUST match column count

6. **Footer Legend**
   Color-coded opportunity level indicators

### Phase 4: Visual Refinement

Apply Vianeo design system exactly:

**Color Palette** (use these exact hex values):
```css
--color-primary: #1a365d           /* Navy blue header */
--color-primary-light: #2c5282     /* Header gradient */
--color-opportunity-high: #0f9d58   /* Green (high priority) */
--color-opportunity-medium: #f4b400 /* Yellow (medium) */
--color-opportunity-low: #ef6c00    /* Orange (low) */
--color-expected: #1a73e8           /* Blue (expected) */
--color-accessory: #5f6368          /* Gray (accessory) */
```

**Row Backgrounds**:
```css
--bg-opportunity-high: #e8f5e9      /* Light green */
--bg-opportunity-medium: #fff9e6    /* Light yellow */
--bg-opportunity-low: #fff3e0       /* Light orange */
--bg-expected: #e8f0fe              /* Light blue */
--bg-accessory: #f5f5f5             /* Light gray */
```

**Typography Scale**:
- Header title: 16px, weight 600
- Stats values: 20px, weight 700
- Stats labels: 9px
- Table headers: 10px, weight 600
- Table cells: 11px
- Timing badges: 10px

**Spacing System**: 8px base unit
- Cell padding: 12px 16px
- Header padding: 10px 20px
- Gap between elements: 8px, 16px, 24px multiples

### Phase 5: Functionality Implementation

Ensure all interactive features work:

1. **Toggle Switch**
   - Click to switch between Partners/Means views
   - Keyboard accessible (Tab + Enter/Space)
   - Smooth transition with debounce (250ms)
   - Updates view header text
   - Shows/hides appropriate columns

2. **CSV Export**
   - Exports current view (Partners or Means)
   - Includes feature names, timing, and relationship data
   - Proper CSV escaping for special characters
   - Auto-downloads with timestamp in filename
   - Keyboard shortcut: Ctrl/Cmd + E

3. **Print Functionality**
   - Optimized print styles
   - Preserves colors and layout
   - Keyboard shortcut: Ctrl/Cmd + P

4. **Accessibility**
   - Screen reader announcements for view changes
   - ARIA labels and roles throughout
   - Keyboard navigation support
   - Focus indicators
   - Semantic HTML structure
   - WCAG 2.1 AA compliant

### Phase 6: Quality Assurance

Before delivering, verify:

**Visual Quality**:
- Colors match exact hex values
- Typography is consistent
- Spacing follows 8px system
- Timing badges display correctly with icons
- Row backgrounds alternate properly
- No horizontal scrolling required

**Functionality**:
- Toggle switches views smoothly
- All columns show/hide correctly
- CSV export works for both views
- Print preview looks professional
- No console errors in browser DevTools

**Content Accuracy**:
- All features listed
- Timing assignments correct
- Partner relationships mapped
- Means requirements identified
- Statistics accurate
- Headers and labels correct

**Accessibility**:
- Tab navigation works
- Screen reader announces changes
- Focus indicators visible
- All interactive elements keyboard accessible

## Data Structure Examples

### Example 1: Marine Data Analytics Platform

**Features** (12 core features):
1. Data Analytics Platform - Already Available
2. IoT Sensor Integration - Short-term
3. Compliance Automation - Mid-term
4. Fleet Management System - Short-term
5. Environmental Monitoring - Mid-term
6. Real-time Alerting - Short-term
7. Predictive Maintenance - Long-term
8. Catch Reporting - Already Available
9. Vessel Tracking - Already Available
10. Resource Optimization - Mid-term
11. Mobile Access - Short-term
12. API Integration - Mid-term

**Partners View Columns**:
- Technology Stack
- Data Sources
- IoT Hardware
- Cloud Platform
- Analytics Tools

**Means View Columns**:
- Internal Team
- Contractors
- Open Source
- SaaS Platforms
- Cloud Services
- Budget
- Equipment
- Licenses
- Consulting
- Grants

### Example 2: Education Platform

**Features** (10 core features):
1. Learning Management System
2. Video Conferencing
3. Assignment Submission
4. Grade Tracking
5. Parent Portal
6. Mobile App
7. Analytics Dashboard
8. Content Library
9. Discussion Forums
10. Integration APIs

**Partners View Columns**:
- LMS Provider
- Video Platform
- Content Partners
- Payment Gateway
- Authentication

**Means View Columns**:
- Dev Team
- Contractors
- Open Source
- Cloud Hosting
- CDN Services
- Database
- APIs
- Support Team

## Technical Implementation Details

### Toggle Mechanism

The toggle uses JavaScript to show/hide columns based on `data-view` attribute:

```javascript
// All elements with data-view="partners" visible by default
// All elements with data-view="means" have class="hidden" initially

function toggleColumnVisibility() {
    document.querySelectorAll('[data-view="partners"]')
        .forEach(el => el.classList.toggle('hidden'));
    document.querySelectorAll('[data-view="means"]')
        .forEach(el => el.classList.toggle('hidden'));
}
```

### Timing Badge System

Four timing types with specific colors and icons:

1. **Already Available** - Green (#0f9d58)
   - Icon: Checkmark
   - Use: Features already built

2. **Short-term** - Blue (#1a73e8)
   - Icon: Circle
   - Use: 0-6 months

3. **Mid-term** - Yellow (#f4b400)
   - Icon: Circle
   - Use: 6-12 months

4. **Long-term** - Orange (#ef6c00)
   - Icon: Circle
   - Use: 12+ months

### CSV Export Logic

The export function:
1. Reads current view state (Partners or Means)
2. Extracts table headers (excluding hidden columns)
3. Iterates through rows, extracting feature names, timing, and cell data
4. Handles three cell types: empty, partner text, checkmarks
5. Escapes CSV special characters (commas, quotes, newlines)
6. Creates Blob and triggers download
7. Filename format: `[project-name]-features-[view]-[date].csv`

## Common Customization Scenarios

### Scenario 1: Different Column Counts

If you need 8 partner columns instead of 5:
1. Add 3 more `<th>` in thead with `data-view="partners"`
2. Add 3 more `<td>` cells to EVERY feature row with same attribute
3. Adjust means columns similarly if needed

### Scenario 2: Custom Timing Categories

To use "Q1, Q2, Q3, Q4" instead of Short/Mid/Long:
1. Keep the CSS classes (`timing-short`, `timing-mid`, `timing-long`)
2. Change badge text: `<span class="timing-badge timing-short">Q1 2025</span>`
3. Update legend footer to match

### Scenario 3: Text Instead of Checkmarks

To show descriptions in Means view instead of checkmarks:
1. Replace `<div class="check" role="img" aria-label="Required"></div>`
2. With `<div class="partner-text">Description text</div>`
3. Keep all data-view attributes intact

### Scenario 4: More Than 12 Features

If you have 15+ features:
- Consider splitting into multiple matrices by category
- Or reduce scope to 10-12 highest priority features
- Scrolling is acceptable but less ideal for presentations

## Troubleshooting Guide

### Toggle Not Working
**Symptoms**: Clicking toggle doesn't switch views
**Solutions**:
- Verify `data-view` attributes on ALL th and td elements
- Check Means columns have `class="hidden"` initially
- Open browser console, look for JavaScript errors
- Ensure DOM element IDs match JavaScript selectors

### Columns Misaligned
**Symptoms**: Cells don't line up with headers
**Solutions**:
- Count cells in each row, must match header count
- Check for missing `<td>` or extra `</td>` tags
- Verify every row has identical structure
- Use browser DevTools to inspect table structure

### Export Fails
**Symptoms**: CSV download doesn't work or file is corrupted
**Solutions**:
- Check for special characters in cell text (especially commas, quotes)
- Verify table structure is intact
- Test in different browser
- Check JavaScript console for errors

### Visual Inconsistencies
**Symptoms**: Colors/spacing don't match reference
**Solutions**:
- Compare hex color values in CSS to reference
- Check typography sizes match specification
- Verify spacing uses 8px multiples
- Test in Chrome/Firefox/Safari for consistency

## File Delivery Checklist

Before delivering to user:

- [ ] HTML file is complete and self-contained
- [ ] File opens correctly in browser
- [ ] Toggle switches between views smoothly
- [ ] All features listed with correct timing
- [ ] Partner relationships mapped accurately
- [ ] Means requirements identified clearly
- [ ] Export produces valid CSV for both views
- [ ] Print preview looks professional
- [ ] No console errors in browser DevTools
- [ ] Statistics in header are accurate
- [ ] Colors match Vianeo design system
- [ ] Typography is consistent
- [ ] Accessibility features work (keyboard nav, screen reader)

## Best Practices

1. **Start with Data Collection**: Get complete feature list and relationship mappings before coding
2. **Use Reference File**: Copy structure from working example, modify incrementally
3. **Test Early**: Verify toggle works after adding just 2-3 rows
4. **Keep It Simple**: Stick to 10-12 features, 5-7 partner columns, 7-10 means columns
5. **Maintain Consistency**: Use same structure and styling across all project matrices
6. **Document Changes**: Add comments in HTML for project-specific customizations
7. **Version Control**: Save dated backups when making significant updates
8. **Accessibility First**: Never remove ARIA attributes or keyboard support

## Response Format

When building a matrix, follow this flow:

1. **Acknowledge Request**: Confirm you're building Step 11 matrix for [project]
2. **Ask for Data**: Request feature list, partners, means, timing (if not provided)
3. **Validate Scope**: Confirm 10-12 features, appropriate column counts
4. **Build HTML**: Create complete self-contained file
5. **Save to Outputs**: Place in `/mnt/user-data/outputs/[project-name]-features-needs-matrix.html`
6. **Provide Link**: Share clickable computer:// link
7. **Brief Summary**: 2-3 sentences on what's included, NO lengthy descriptions
8. **Offer Next Steps**: Ask if they want adjustments or ready for Step 12

## Example User Interactions

**Good Flow**:
```
User: "Build a Step 11 matrix for our Healthcare Records Platform"
Claude: "I'll create a Features & Needs matrix for Healthcare Records Platform.
To build this accurately, I need:
- List of 10-12 core features with implementation timing
- 5-7 partner categories (tech stack, integrations, etc.)
- 7-10 means categories (team, tools, budget, etc.)

Do you have this data ready, or should I suggest typical categories for healthcare platforms?"
```

**Bad Flow**:
```
User: "Make a features matrix"
Claude: [Immediately starts building without asking for project context or data]
```

## Integration with Other Steps

**Upstream Dependencies**:
- Step 7: Requesters (customer segments inform needs)
- Step 8: Functionalities (features derive from functional requirements)
- Step 9: Solution Definition (technical approach informs partners/means)

**Downstream Uses**:
- Step 12: Features & Means (extends this with detailed resource planning)
- MVP Definition (high opportunity features become MVP scope)
- Resource Planning (means become budget line items)
- Timeline Development (timing badges inform project schedule)

## Professional Communication Tips

**Do**:
- Ask clarifying questions about feature priorities
- Suggest typical partner/means categories for their industry
- Validate data completeness before building
- Offer to iterate based on feedback

**Don't**:
- Make assumptions about feature timing without input
- Guess at partner relationships
- Build with incomplete data
- Over-explain the HTML structure in response

## Final Reminders

- This is a **presentation-grade deliverable** for stakeholders
- Every detail matters: colors, spacing, typography, alignment
- The toggle is a key feature, test it thoroughly
- CSV export and print must work flawlessly
- Accessibility compliance is non-negotiable
- When in doubt, reference the working example file
- Save dated backups before making changes
- Test in multiple browsers before final delivery

---

**Success Metric**: User can present this matrix to executives or investors without any visual polish needed.
