# Step 7: Needs Qualification Matrix - Output Format Specification

**Version**: 2.0
**Purpose**: Exact format specification for Step 7 outputs (Importance vs. Satisfaction matrix)
**Dimension**: Desirability (25% of VIANEO score - HIGHEST WEIGHT)

---

## Required Output Structure

### Primary Output: Interactive HTML Matrix

Full-featured interactive matrix with:
- Sortable columns
- Color-coded cells
- Hover tooltips
- Responsive layout

### Secondary Output: Markdown Analysis Report

Written analysis with:
- Quadrant summary
- Priority recommendations
- Evidence documentation

---

## HTML Matrix Structure

### File Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Needs Qualification Matrix - [Project Name]</title>
    <style>
        /* VIANEO Design Tokens */
        :root {
            --primary-navy: #1a365d;
            --primary-blue: #2E5C8A;
            --high-opportunity: #10b981;
            --monitor: #f59e0b;
            --low-priority: #9ca3af;
            --over-served: #ef4444;
        }
    </style>
</head>
<body>
    <header>
        <h1>Needs Qualification Matrix</h1>
        <p class="metadata">
            Project: [Name] | Date: [YYYY-MM-DD] | Requesters: [X] | Needs: [Y]
        </p>
    </header>

    <main>
        <table class="matrix">
            <!-- Header row with requester names -->
            <!-- Data rows with need statements and ratings -->
        </table>
    </main>
</body>
</html>
```

---

## Matrix Table Format

### Header Row

```html
<thead>
    <tr>
        <th class="need-column">Need Statement</th>
        <th class="requester-column">[Requester 1]<br><span class="interview-count">([X] interviews)</span></th>
        <th class="requester-column">[Requester 2]<br><span class="interview-count">([X] interviews)</span></th>
        <!-- Continue for all requesters -->
    </tr>
</thead>
```

### Data Rows

```html
<tbody>
    <tr>
        <td class="need-statement">[Need text - max 60 chars]</td>
        <td class="rating [importance-class]">
            <div class="importance">[Fundamental/Important/Nice-to-Have]</div>
            <div class="satisfaction">[Not At All/Partially/Completely]</div>
        </td>
        <!-- Continue for all requesters -->
    </tr>
</tbody>
```

---

## Rating System

### Importance Scale

| Rating | Definition | Display |
|--------|------------|---------|
| **Fundamental** | Blocking need, deal-breaker | Bold text |
| **Important** | Significant impact on decision | Regular text |
| **Nice-to-Have** | Appreciated but not critical | Italic text |

### Satisfaction Scale

| Rating | Definition | Display |
|--------|------------|---------|
| **Not At All** | Completely unmet | Red indicator |
| **Partially** | Some solutions exist but inadequate | Yellow indicator |
| **Completely** | Current solutions work well | Green indicator |

---

## Quadrant Classification

### Color Coding

| Quadrant | Importance | Satisfaction | Color | Action |
|----------|------------|--------------|-------|--------|
| **High Opportunity** | Fundamental | Not At All | #10b981 (Green) | Primary focus |
| **Monitor** | Fundamental/Important | Completely | #f59e0b (Yellow) | Maintain |
| **Low Priority** | Nice-to-Have | Any | #9ca3af (Gray) | Deprioritize |
| **Over-served** | Nice-to-Have | Completely | #ef4444 (Red) | Potential reduction |

---

## Data Requirements

### From Step 5 (Exact Match Required)

| Element | Source | Requirement |
|---------|--------|-------------|
| Requester names | Step 5 Requesters table | Verbatim match |
| Need statements | Step 5 Needs analysis | Verbatim match |
| Interview counts | Step 5 Validation | Exact numbers |

### Validation Rules

- Column count = Requester count from Step 5
- Row count = Need count from Step 5 (typically 10)
- Every cell must have both Importance and Satisfaction
- No empty cells allowed

---

## Markdown Report Structure

### Format

```markdown
# Needs Qualification Analysis - [Project Name]

**Date**: YYYY-MM-DD
**Requesters Analyzed**: [X]
**Needs Evaluated**: [Y]
**Source**: Step 5 Needs/Requesters Analysis

---

## Quadrant Summary

### High Opportunity (Prioritize)

| Need | Requester(s) | Importance | Satisfaction |
|------|--------------|------------|--------------|
| [Need] | [Who] | Fundamental | Not At All |

**Analysis**: [2-3 sentences on opportunity]

### Monitor (Maintain)

| Need | Requester(s) | Importance | Satisfaction |
|------|--------------|------------|--------------|
| [Need] | [Who] | Important | Completely |

### Low Priority (Deprioritize)

[List of nice-to-have needs]

### Over-served (Consider Reducing)

[List of over-served needs if any]

---

## Priority Recommendations

### Immediate Focus (High Opportunity)

1. **[Need 1]**: [Why this is priority, which requesters]
2. **[Need 2]**: [Why this is priority, which requesters]

### Secondary Focus (Important + Partially Satisfied)

1. **[Need 1]**: [Opportunity description]

### Table Stakes (Must Maintain)

- [Need that must be satisfied but isn't differentiating]

---

## Evidence Base

### Data Sources

- Step 5 Output: [Filename]
- Interview Data: [Source]

### Confidence Levels

| Requester | Interview Count | Confidence |
|-----------|-----------------|------------|
| [Name] | [X] | L1/L2/L3 |
```

---

## Output Files

### Required Deliverables

1. **Interactive HTML Matrix**
   - File: `[ProjectName]_Needs_Matrix.html`
   - Features: Sortable, color-coded, responsive

2. **Markdown Analysis Report**
   - File: `[ProjectName]_Needs_Analysis.md`
   - Content: Quadrant summary, recommendations, evidence

### File Naming Convention

```
[ProjectName]_Needs_Matrix_YYYYMMDD.html
[ProjectName]_Needs_Analysis_YYYYMMDD.md
```

---

## Downstream Dependencies

Step 7 feeds into:

| Downstream Step | Data Required | Purpose |
|-----------------|---------------|---------|
| **Step 11 (Needs View)** | Importance ratings | Column colors |
| **Step 11 (Needs View)** | Requester segments | Dropdown selectors |
| **Step 10 (Diagnostic)** | High opportunity needs | Key findings |

---

## Quality Checklist

Before delivery, verify:

### Data Integrity
- [ ] All requesters from Step 5 present
- [ ] All needs from Step 5 present
- [ ] Names match Step 5 exactly
- [ ] Need statements match Step 5 exactly
- [ ] Interview counts match Step 5

### Matrix Completeness
- [ ] Every cell has Importance rating
- [ ] Every cell has Satisfaction rating
- [ ] No empty cells
- [ ] Color coding applied correctly

### Quadrant Analysis
- [ ] High Opportunity items identified
- [ ] Monitor items identified
- [ ] Low Priority items identified
- [ ] Over-served items identified (if any)

### Report Quality
- [ ] Recommendations are specific
- [ ] Evidence sources cited
- [ ] Confidence levels documented
- [ ] Actionable next steps provided

---

## Common Mistakes to Avoid

1. ❌ Requester names differ from Step 5 → ✅ Copy verbatim
2. ❌ Need statements paraphrased → ✅ Exact match required
3. ❌ Missing requesters or needs → ✅ Complete coverage
4. ❌ Empty cells in matrix → ✅ Every cell filled
5. ❌ All same ratings → ✅ Differentiation expected
6. ❌ No high-opportunity items → ✅ Verify scoring accuracy
7. ❌ Colors don't match quadrant → ✅ Apply design tokens correctly
8. ❌ Generic recommendations → ✅ Specific, actionable items

---

**This specification ensures every Step 7 output follows consistent format for needs prioritization analysis.**
