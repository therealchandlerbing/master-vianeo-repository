# Format Specification: Committee Synthesis

**Version**: 1.0
**Purpose**: Exact format specification for Committee Synthesis outputs to ensure consistency

---

## Document Structure

### Platform Entry (Markdown)

> **Note:** The Platform Entry uses a simplified 2-column Scores table (Dimension, Score) for direct platform selection. The detailed 4-column format (with Status and Key Rationale) is used in the Committee Scores section of the full report. See "Committee Scores Table Format" section below for the detailed format.

```markdown
# [Project Name] Committee Synthesis - Vianeo Platform Entry

## Form Fields
**Title:** [Project Name]
**Date:** [Date]

## Scores (Select in Platform)
| Dimension | Score |
|-----------|:-----:|
| Team | X/5 |
| Technology | X/5 |
| Management and Business | X/5 |
| Commercial | X/5 |

## Comment
[4-paragraph diagnostic comment]

## Score Rationale
### Team: X/5
[2-3 sentence justification]

### Technology: X/5
[2-3 sentence justification]

### Management and Business: X/5
[2-3 sentence justification]

### Commercial: X/5
[2-3 sentence justification]

## Overall Assessment
| Metric | Score | Status |
|--------|:-----:|--------|
| Market Maturity Score | X.X/5.0 | [Above/Below] 3.2 threshold |
| Overall Vianeo Score | X.X/5.0 | [STRONG/PROMISING/DEVELOPING/PROBLEMATIC] |

**Recommendation:** [PROCEED/CONDITIONAL PROCEED/PAUSE/DO NOT PROCEED]
```

---

### Professional DOCX Report

**Page Setup:**
- Margins: 0.8" all sides (1152 DXA)
- Font: Arial throughout
- Default size: 11pt (22 half-points)

**Typography Scale:**
- Title: 24pt bold, deep blue (#1B365D)
- Heading 1: 14pt bold, deep blue
- Heading 2: 12pt bold, deep blue
- Body: 11pt, dark gray (#1F2937)
- Caption/Footer: 9pt, medium gray (#4B5563)

**Color Palette:**
- Primary (headers): #1B365D (deep blue)
- Success (>=4/5): #059669 (green)
- Warning (3/5): #D97706 (amber)
- Danger (<=2/5): #DC2626 (red)
- Background light: #F9FAFB
- Border: #E5E7EB

**Score Table Formatting:**
- Header row: Deep blue background, white text
- Score cells: Color-coded background based on value
  - >=4/5: Light green (#DCFCE7)
  - 3/5: Light amber (#FEF3C7)
  - <=2/5: Light red (#FEE2E2)
- Column widths: Dimension 3500 DXA, Score 1200 DXA, Rationale 4300 DXA

**Section Structure:**
1. Title and project metadata table
2. Committee Scores table
3. Diagnostic Comment (4 subsections)
4. Overall Assessment summary box
5. Methodology footer

---

## Character Limits

For Vianeo platform compatibility:

| Field | Limit | Guidance |
|-------|-------|----------|
| Title | 100 chars | Project name only |
| Comment | 2000 chars | Full 4-paragraph diagnostic |
| Per-dimension rationale | 500 chars | 2-3 sentences |

---

## Diagnostic Comment Constraints

| Paragraph | Sentences | Focus |
|-----------|-----------|-------|
| Strengths | 1-2 | Validated capabilities, metrics |
| Risks | 1-2 | Critical gaps, quantified |
| Actions | 2-3 | Numbered, with owners and timelines |
| Evidence Gaps | 1-2 | Missing validation, blocking decisions |

**Total:** 6-8 sentences across 4 paragraphs

---

## Document Header Format

### Platform Entry Header

```markdown
# [Project Name] Committee Synthesis - Vianeo Platform Entry

**Project:** [Full project name]
**Principal Investigator:** [Name, Organization]
**Date:** YYYY-MM-DD
**Assessment Framework:** Vianeo Business Model Evaluation (Post-Sprint)
**Maturity Stage:** [Stage]

---
```

**Critical Rules:**
- First line: "# [Project Name] Committee Synthesis - Vianeo Platform Entry"
- Bold all metadata labels
- Date format: YYYY-MM-DD
- Three dashes for section separator

### DOCX Header Table

| Field | Value |
|-------|-------|
| Project | [Project Name] |
| Principal Investigator | [Name, Organization] |
| Date | YYYY-MM-DD |
| Assessment Framework | Vianeo Business Model Evaluation (Post-Sprint) |
| Maturity Stage | [Stage] |

---

## Committee Scores Table Format

### Markdown Version

```markdown
## Committee Scores

| Dimension | Score | Status | Key Rationale |
|-----------|:-----:|--------|---------------|
| **Team** | X/5 | [Strong/Adequate/Below] | [2-3 sentence justification] |
| **Technology** | X/5 | [Strong/Adequate/Below] | [2-3 sentence justification] |
| **Management and Business** | X/5 | [Strong/Adequate/Below] | [2-3 sentence justification] |
| **Commercial** | X/5 | [Strong/Adequate/Below] | [2-3 sentence justification] |
```

### Column Specifications

1. **Dimension** (bold, left-aligned)
   - Exact names: Team, Technology, Management and Business, Commercial

2. **Score** (center-aligned)
   - Format: X/5 (integer, not decimal)
   - Range: 1-5

3. **Status** (left-aligned)
   - Strong: Score 4-5
   - Adequate: Score 3
   - Below: Score 1-2

4. **Key Rationale** (left-aligned, 500 characters max)
   - 2-3 sentences with specific evidence
   - Include metrics where available

---

## Diagnostic Comment Format

### Structure

```markdown
## Diagnostic Comment

**STRENGTHS:** [1-2 sentences on validated capabilities with specific metrics]

**RISKS:** [1-2 sentences on critical gaps, quantified]

**NEAR-TERM ACTIONS:** (1) [Action with owner and timeline]. (2) [Action with owner and timeline]. (3) [Action with owner and timeline].

**EVIDENCE GAPS:** [1-2 sentences on missing validation and blocking decisions]
```

### Action Item Format

Each action must include:
1. Specific action (verb + noun)
2. Owner (named person or role)
3. Timeline (specific days or date)

**Correct Format:**
```
(1) Launch customer discovery sprint across 8 stakeholder segments. Owner: Daniel Bonifacio. Timeline: 60 days.
```

**Incorrect Format:**
```
(1) Do customer research soon.
```

---

## Overall Assessment Section

```markdown
## Overall Assessment

| Metric | Score | Status |
|--------|:-----:|--------|
| Market Maturity Score | X.X/5.0 | [Above/Below] 3.2 threshold |
| Overall Vianeo Score | X.X/5.0 | [STRONG/PROMISING/DEVELOPING/PROBLEMATIC] |

**Recommendation:** [PROCEED/CONDITIONAL PROCEED/PAUSE/DO NOT PROCEED]

[1-2 sentence justification for recommendation]
```

### Status Definitions

| Overall Score | Status Label |
|---------------|--------------|
| >=4.0 | STRONG |
| 3.2-3.9 | PROMISING |
| 2.5-3.1 | DEVELOPING |
| <2.5 | PROBLEMATIC |

---

## Vianeo to Committee Score Reference

### Quick Reference Table

```markdown
## Quick Reference

| Vianeo Dimension | Score | Committee Mapping |
|------------------|:-----:|-------------------|
| Legitimacy | X.X/5 | -> Team, Technology |
| Desirability | X.X/5 | -> Commercial |
| Acceptability | X.X/5 | -> Management and Business |
| Feasibility | X.X/5 | -> Team, Technology |
| Viability | X.X/5 | -> Management and Business, Commercial |
```

---

## Formatting Rules

1. **Never use em dashes** (use commas, periods, or parentheses)
2. **Always include specific metrics** (not "strong team" but "13+ doctorate team")
3. **Always include timelines** for actions (not "soon" but "60 days")
4. **Always name owners** for actions (not "team" but "Daniel Bonifacio")
5. **State gaps directly** (not "could improve" but "zero interviews conducted")
6. **Use arrows** for mapping indicators (->)
7. **Use parentheses** for numbered actions: (1), (2), (3)

---

## Validation Checklist

Before delivering Committee Synthesis:

### Structure Completeness
- [ ] Document header with all metadata fields
- [ ] Committee Scores table (all 4 dimensions)
- [ ] Diagnostic Comment (all 4 paragraphs)
- [ ] Overall Assessment section
- [ ] Vianeo to Committee score reference
- [ ] Methodology footer

### Format Accuracy
- [ ] Score table uses exact 4-column format
- [ ] All dimension names match specification exactly
- [ ] Scores are integers (X/5, not decimals)
- [ ] Status labels match score ranges
- [ ] Rationale <=500 characters per dimension
- [ ] Total diagnostic comment 6-8 sentences

### Content Quality
- [ ] All scores justified with specific evidence
- [ ] All actions have owners and timelines
- [ ] All metrics are specific numbers
- [ ] Gaps stated directly without softening
- [ ] Recommendation matches score pattern
- [ ] No em dashes used anywhere

---

## File Naming Convention

**Platform Entry (Markdown):** `[ProjectName]_[Date]_Committee_Synthesis_Platform.md`
**Professional Report (DOCX):** `[ProjectName]_[Date]_Committee_Synthesis_Report.docx`

**Examples:**
- `IRDose_2025-12-08_Committee_Synthesis_Platform.md`
- `IRDose_2025-12-08_Committee_Synthesis_Report.docx`

**Rules:**
- The date format is YYYY-MM-DD, using dashes as internal separators
- Underscore separators between filename elements
- CamelCase for project name

---

## Common Mistakes to Avoid

1. Using em dashes instead of commas/periods
2. Vague metrics ("strong team" instead of "13 PhD team members")
3. Actions without owners or timelines
4. Softening language for gaps ("could improve" instead of "zero interviews")
5. Decimal scores in committee table (use 4/5, not 4.2/5)
6. Missing status labels in score table
7. Exceeding character limits
8. Wrong recommendation for score pattern
9. Missing methodology footer
10. Inconsistent date formats

---

**This specification ensures every Committee Synthesis output follows the exact same format for professional consistency and platform compatibility.**
