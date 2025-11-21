# Step 10: Vianeo Diagnostic DOCX Format Specification

## Overview

This template provides the exact formatting specifications for creating the professional DOCX version of the Vianeo Diagnostic Comment. The DOCX contains **identical content** to the markdown version but with professional design elevation.

**CRITICAL:** Read `/mnt/skills/public/docx/docx-js.md` completely before creating DOCX. Also review `docs/VIANEO_Diagnostic_DOCX_Formatting.md` for complete technical specifications.

---

## Content Structure

The DOCX follows this exact structure (identical to markdown):

1. **Title Section**
   - Project Name + "Vianeo Main Diagnostic Comment"
   - Date, Assessment Framework, Overall Maturity

2. **Executive Diagnostic**
   - Strengths (1-2 sentences)
   - Risks (1-2 sentences)
   - Near-term Actions (2-3 sentences)
   - Evidence Gaps (1-2 sentences)

3. **Dimension Summary**
   - Table with 5 dimensions
   - Overall status statement

4. **Critical Path Forward**
   - Immediate Priority (Weeks 1-4)
   - Short-term Priority (Months 2-3)
   - Medium-term Priority (Months 4-6)
   - Success Metrics

5. **Footer Metadata**
   - Assessment Methodology
   - Evidence Sources
   - Next Review

---

## Professional Design Specifications

### Typography Scale

- **Title:** 24pt, bold, deep blue (#1B365D), left-aligned
- **Heading 1:** 16pt, bold, deep blue (#1B365D)
- **Heading 2:** 14pt, bold, medium gray (#4A4A4A)
- **Body Text:** 11pt, regular, body gray (#2D2D2D)
- **Metadata:** 9pt, regular, light gray (#757575)
- **Font:** Calibri throughout

### Color Palette

```javascript
primaryBlue: "1B365D"      // Headers - conveys authority and trust
mediumGray: "4A4A4A"       // Subheadings - professional hierarchy
bodyGray: "2D2D2D"         // Body text - reading comfort
lightGray: "757575"        // Metadata - secondary information
tableBorder: "CCCCCC"      // Subtle borders
tableHeaderBg: "E8EDF2"    // Soft blue-gray for table headers
greenHighlight: "D4EDDA"   // Scores ≥3.5 (Strong/Promising)
yellowHighlight: "FFF3CD"  // Scores 3.0-3.4 (Developing)
redHighlight: "F8D7DA"     // Scores <3.0 (Problematic/Non-viable)
```

### Spacing System (DXA units, 1440 = 1 inch)

**Page Setup:**
- Margins: 1" all sides (1440 DXA)

**Paragraph Spacing:**
- Title: 0pt before, 240pt after
- H1: 360pt before, 180pt after
- H2: 240pt before, 120pt after
- Body: 240pt after, line height 360 (1.6x)
- Metadata: 60pt after each line

---

## Table Formatting (Dimension Summary)

### Table Structure

**Column Widths (DXA):**
- Dimension: 3120
- Score: 1560
- Interpretation: 4680
- **Total: 9360** (fits letter width with 1" margins)

**CRITICAL:** Set BOTH `columnWidths` array AND individual cell widths.

### Table Cell Specifications

**All Cells:**
- Borders: Light gray (#CCCCCC), 1pt, all sides
- Cell margins: 100pt top/bottom, 180pt left/right

**Header Row:**
- Background: Soft blue-gray (#E8EDF2)
- Text: Bold, 11pt, centered
- Example: "Dimension", "Score", "Interpretation"

**Data Rows:**
- Dimension column: Bold text, left-aligned
- Score column: Bold text, centered, **color-coded background**
- Interpretation column: Regular text, left-aligned

### Score Cell Color Coding

**Apply semantic colors based on score:**
- Score ≥3.5: Green background (#D4EDDA)
- Score 3.0-3.4: Yellow background (#FFF3CD)
- Score <3.0: Red background (#F8D7DA)

**Helper function:**
```javascript
function getScoreColor(score) {
  if (score >= 3.5) return "D4EDDA";
  if (score >= 3.0) return "FFF3CD";
  return "F8D7DA";
}
```

---

## List Formatting

### Numbered Lists (Critical Path Sections)

**CRITICAL:** Each section needs its own numbering reference to restart at 1.

**Configuration:**
```javascript
// Immediate Priority
{ reference: "immediate-list", level: 0, format: LevelFormat.DECIMAL, text: "%1." }

// Short-term Priority (different reference = restarts numbering)
{ reference: "short-term-list", level: 0, format: LevelFormat.DECIMAL, text: "%1." }

// Medium-term Priority (different reference = restarts numbering)
{ reference: "medium-term-list", level: 0, format: LevelFormat.DECIMAL, text: "%1." }
```

**Indentation:**
- Left indent: 720pt
- Hanging indent: 360pt

### Bullet Lists (Success Metrics)

**Configuration:**
```javascript
{ reference: "success-metrics-list", level: 0, format: LevelFormat.BULLET, text: "•" }
```

**CRITICAL:** Use `LevelFormat.BULLET` constant, NOT the string "bullet".

---

## Footer Section

### Horizontal Rule

- Border: Top only, light gray (#CCCCCC), 1pt
- Spacing: 360pt before, 120pt after

### Metadata Lines

**Format each line:**
```javascript
new Paragraph({
  style: "Metadata",
  children: [
    new TextRun({ text: "Assessment Methodology: ", bold: true }),
    new TextRun("Vianeo 40-Question Diagnostic Framework...")
  ]
})
```

**Three required lines:**
1. Assessment Methodology: [frameworks list]
2. Evidence Sources: [documents list]
3. Next Review: [date and trigger]

---

## File Generation

### Save Location
Save to: `/mnt/user-data/outputs/[ProjectName]_Vianeo_Diagnostic_Comment.docx`

### Generation Code Structure

```javascript
const fs = require('fs');
const { Document, Packer } = require('docx');

// Create document with all specifications
const doc = new Document({ /* configuration */ });

// Generate and save
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(
    "/mnt/user-data/outputs/[ProjectName]_Vianeo_Diagnostic_Comment.docx",
    buffer
  );
});
```

---

## Quality Validation Checklist

Before delivering, verify:

**Typography:**
- [ ] Title is 24pt bold deep blue
- [ ] H1 headers are 16pt bold deep blue
- [ ] H2 headers are 14pt bold medium gray
- [ ] Body text is 11pt body gray with 1.6x line height
- [ ] Metadata is 9pt light gray
- [ ] Font is Calibri throughout

**Colors:**
- [ ] All header colors match specification
- [ ] Table header background is soft blue-gray
- [ ] Score cells color-coded by range
- [ ] Body text uses softer gray (not pure black)

**Spacing:**
- [ ] 1" margins on all sides
- [ ] Title, H1, H2 spacing matches specification
- [ ] Body paragraphs have 1.6x line height
- [ ] Generous whitespace between sections

**Tables:**
- [ ] Column widths set correctly (both array AND individual cells)
- [ ] All borders present and subtle
- [ ] Header row has background color
- [ ] Score cells color-coded correctly
- [ ] Cell margins consistent

**Lists:**
- [ ] Each numbered section uses unique reference
- [ ] Numbering restarts at 1 for each section
- [ ] Indentation consistent (720/360)
- [ ] Bullets use LevelFormat.BULLET constant
- [ ] No unicode symbols used

**Content:**
- [ ] IDENTICAL to markdown version
- [ ] No content added or removed
- [ ] All sections present and complete

---

## Common Mistakes to Avoid

**CRITICAL ERRORS:**
- ❌ Using string "bullet" instead of LevelFormat.BULLET constant
- ❌ Using ShadingType.SOLID (causes black backgrounds)
- ❌ Not setting BOTH columnWidths array AND individual cell widths
- ❌ Using same numbering reference across sections
- ❌ Using \n for line breaks (always use separate Paragraphs)
- ❌ Using unicode bullets instead of proper Word lists

**FORMATTING ERRORS:**
- ❌ Inconsistent spacing between sections
- ❌ Wrong color codes (typos in hex values)
- ❌ Missing cell borders in tables
- ❌ Incorrect DXA measurements
- ❌ Forgetting type: ShadingType.CLEAR

**CONTENT ERRORS:**
- ❌ Content differs from markdown version
- ❌ Missing sections
- ❌ Adding extra content not in markdown

---

## Design Principles

This formatting applies professional design elevation:

1. **Typography Scale** - Clear hierarchy, meaningful size relationships
2. **Strategic Color** - Restrained palette with semantic meaning
3. **Generous White Space** - Professional margins, breathing room
4. **Systematic Approach** - Consistent application across document
5. **Borrowed Excellence** - Apple typography, Swiss design, Stripe data presentation

---

## Reference Files

**Complete technical specifications:**
`docs/VIANEO_Diagnostic_DOCX_Formatting.md`

**docx-js documentation:**
`/mnt/skills/public/docx/docx-js.md`

**Content template:**
`templates/Step10_Diagnostic_Markdown_Template.md`

---

**Remember:** The DOCX should be visually professional while containing IDENTICAL content to the markdown version. Every formatting choice serves readability and credibility.
