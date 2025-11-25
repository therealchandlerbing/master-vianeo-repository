# Step 6: Persona Development - Output Format Specification

**Version**: 2.0
**Purpose**: Exact format specification for Step 6 outputs (Evidence-based personas)
**Dimension**: Desirability (25% of VIANEO score - HIGHEST WEIGHT)

---

## Required Output Structure

### Document Format

**Primary Output**: Professional DOCX document
**Secondary Output**: Markdown version for version control
**Page Limit**: Maximum 11 pages

---

## Page 1: Cover Page

### Format

```
[COMPANY LOGO - if available]

────────────────────────────────────────

[Company Name]
Vianeo Business Model Evaluation

USER PERSONA ANALYSIS

[Project subtitle or domain description]

────────────────────────────────────────

Prepared: [Month Year]
Validation Status: [X] personas based on [Y] total interviews
Evaluation Phase: Desirability Assessment

VIANEO Framework v2.0
```

### Formatting Specifications

| Element | Font | Size | Style | Color |
|---------|------|------|-------|-------|
| Company Name | Calibri | 28pt | Bold | #2E5C8A |
| "Vianeo Business Model Evaluation" | Calibri | 14pt | Regular | #6C757D |
| "USER PERSONA ANALYSIS" | Calibri | 24pt | Bold | #1a365d |
| Subtitle | Calibri | 14pt | Italic | #4a5568 |
| Metadata | Calibri | 11pt | Regular/Bold | #1a202c |

---

## Page 2: Evidence Base Summary

### Format

```markdown
## Evidence Base Summary

### Research Overview

[2-3 sentences describing research approach, total interviews, date range, methodology]

### Validation Breakdown

| Persona | Interview Count | Date Range | Validation Status |
|---------|-----------------|------------|-------------------|
| [Name 1] | [X] | [Mon-Mon Year] | ✓ VALIDATED / ⚠ PARTIAL / ✗ NEEDS |
| [Name 2] | [X] | [Mon-Mon Year] | ✓ VALIDATED / ⚠ PARTIAL / ✗ NEEDS |
| [Name 3] | [X] | [Mon-Mon Year] | ✓ VALIDATED / ⚠ PARTIAL / ✗ NEEDS |

### Critical Gaps & Next Steps

[2-3 sentences identifying validation gaps and priority actions]
```

---

## Pages 3+: Individual Personas

### Persona Page Structure

Each persona occupies 1-2 pages with these sections:

#### 1. Header & Validation Badge

```markdown
## PERSONA [NUMBER]: [FIRST NAME]

┌────────────────────────────────────────────────────┐
│ [STATUS ICON] [STATUS TEXT]                        │
│ [Details - interview count and dates]              │
└────────────────────────────────────────────────────┘
```

#### Validation Badge Specifications

| Status | Criteria | Background | Text Color | Icon |
|--------|----------|------------|------------|------|
| VALIDATED | 5+ interviews | #E8F4EA | #2D7A3E | ✓ |
| PARTIALLY VALIDATED | 1-4 interviews | #FFF4E6 | #CC7A00 | ⚠ |
| NEEDS VALIDATION | 0 interviews | #FFEBEE | #C62828 | ✗ |

#### 2. Requester Profile

```markdown
### Requester Profile

**First Name:** [Single name only]
**Age:** [Specific number, not range]

**Life & Motivations:**
[2-3 sentences - professional context, career motivations, decision drivers]

**Personality & Values:**
[2-3 sentences - work style, decision-making approach, core values]
```

#### 3. Field of Application

```markdown
### Field of Application

**Thinks & Feels:**
[2-3 sentences - internal thought process, concerns, emotional state]

**Observes:**
[2-3 sentences - trends, competitor actions, peer behavior]

**Does:**
[2-3 sentences - actual behaviors, daily activities, current approaches]

**Others Say:**
[2-3 sentences - colleague/leadership/customer influence]
```

#### 4. Activities & Challenges

```markdown
### Activities & Challenges

**Tasks (Jobs to be done):** ≤60 chars each
- [Task 1]
- [Task 2]
- [Task 3]
- [Task 4]
- [Task 5]
- [Task 6]

**Pains (Problems to eliminate):** ≤60 chars each
- [Pain 1]
- [Pain 2]
- [Pain 3]
- [Pain 4]
- [Pain 5]
- [Pain 6]

**Expectations (Desired outcomes):** ≤60 chars each
- [Expectation 1]
- [Expectation 2]
- [Expectation 3]
- [Expectation 4]
```

#### 5. Current Solutions

```markdown
### Current Solutions

[2-3 sentences describing specific tools, products, or services with limitations]

**Current Tools:**
- **[Tool 1]:** [Specific limitation]
- **[Tool 2]:** [Specific limitation]
- **[Manual workaround]:** [Why insufficient]
```

---

## Character Limits (STRICTLY ENFORCED)

| Field | Limit | Notes |
|-------|-------|-------|
| Tasks bullets | **60 chars** | Each individual bullet |
| Pains bullets | **60 chars** | Each individual bullet |
| Expectations bullets | **60 chars** | Each individual bullet |
| First name | Single name | No surnames or initials |
| Age | Specific number | Not a range (42, not 40-45) |
| All paragraphs | 2-3 sentences | Consistent throughout |

---

## Activities Distribution

**Target for each persona:**
- Tasks: 4-6 bullets
- Pains: 4-6 bullets
- Expectations: 2-4 bullets

**Total**: 10-16 bullets per persona

---

## Output Files

### Required Deliverables

1. **Professional DOCX** (primary)
   - Cover page + Evidence base + Personas
   - Maximum 11 pages
   - File: `[CompanyName]_Vianeo_Personas.docx`

2. **Markdown Version** (secondary)
   - Same content in markdown format
   - File: `[CompanyName]_Personas.md`

### File Naming Convention

```
[CompanyName]_Vianeo_Personas_YYYYMMDD.docx
[CompanyName]_Personas_YYYYMMDD.md
```

---

## Persona Count Requirements

| Count | Status |
|-------|--------|
| 3-5 personas | Required range |
| <3 personas | Insufficient coverage |
| >5 personas | May indicate overlap |

**Minimum interviews per persona**: 3 (for Score 3 - adequate)
**Recommended interviews per persona**: 5+ (for Score 4-5)

---

## Downstream Dependencies

Step 6 data flows to:

| Downstream Step | Data Required | Purpose |
|-----------------|---------------|---------|
| Step 7 | Persona segments | Matrix columns |
| Step 8-9 | Stakeholder types | Ecosystem mapping |
| Step 10 | Key findings | Executive summary |

---

## Quality Checklist

Before delivery, verify:

### Structure
- [ ] Cover page complete
- [ ] Evidence base page included
- [ ] 3-5 personas (each on new page)
- [ ] Total ≤11 pages

### Personas
- [ ] Each has validation badge
- [ ] Badge matches interview count
- [ ] First name only (no surnames)
- [ ] Age is specific number
- [ ] All sections complete

### Character Limits
- [ ] All Tasks ≤60 characters
- [ ] All Pains ≤60 characters
- [ ] All Expectations ≤60 characters
- [ ] All paragraphs 2-3 sentences

### Content Quality
- [ ] Each persona is distinct
- [ ] No solution embedded in needs
- [ ] Current solutions named specifically
- [ ] Validation gaps documented
- [ ] Could support funding decision

---

## Common Mistakes to Avoid

1. ❌ Age as range ("35-45") → ✅ Specific number ("42")
2. ❌ Full name ("Sarah Johnson") → ✅ First name only ("Sarah")
3. ❌ Bullet >60 chars → ✅ Edit to fit limit
4. ❌ Generic persona → ✅ Specific behavioral detail
5. ❌ Current solutions vague → ✅ Name specific tools
6. ❌ All personas VALIDATED → ✅ Be honest about gaps
7. ❌ Overlapping personas → ✅ Ensure distinct needs/contexts
8. ❌ Solution in needs → ✅ Problem/outcome focus only

---

**This specification ensures every Step 6 output follows consistent format for professional persona documentation.**
