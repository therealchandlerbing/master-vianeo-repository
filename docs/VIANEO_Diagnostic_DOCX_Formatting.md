# DOCX Professional Formatting Specifications

## Overview

This document provides exact specifications for creating professionally formatted Vianeo diagnostic comments using docx-js. These specifications must be followed precisely to ensure consistent, high-quality output.

## Prerequisites

**Before creating any DOCX:**
1. Read `/mnt/skills/public/docx/docx-js.md` COMPLETELY (no view ranges)
2. Read this document completely
3. Verify all dependencies are available

## Design System

### Color Palette

```javascript
const colors = {
  primaryBlue: "1B365D",      // Deep blue for main headers
  mediumGray: "4A4A4A",       // Section headers (H2)
  bodyGray: "2D2D2D",         // Body text (softer than pure black)
  lightGray: "757575",        // Metadata and secondary text
  tableBorder: "CCCCCC",      // Subtle table borders
  tableHeaderBg: "E8EDF2",    // Soft blue-gray for table headers
  greenHighlight: "D4EDDA",   // Scores ≥3.5 (Strong/Promising)
  yellowHighlight: "FFF3CD",  // Scores 3.0-3.4 (Developing)
  redHighlight: "F8D7DA"      // Scores <3.0 (Problematic/Non-viable)
};
```

**Design rationale:**
- Primary Blue: Trust, professionalism, authority
- Gray scale: Reading comfort, not harsh pure black
- Semantic highlights: Instant visual communication of status

### Typography Scale

```javascript
// All sizes in half-points (size: 48 = 24pt)
Title: 48 (24pt), bold, primaryBlue
Heading 1: 32 (16pt), bold, primaryBlue
Heading 2: 28 (14pt), bold, mediumGray
Body: 22 (11pt), regular, bodyGray
Metadata: 18 (9pt), regular, lightGray
```

**Design rationale:**
- Clear hierarchy with meaningful size relationships
- 11pt body optimized for comfortable reading
- Generous spacing between levels (not just 1-2pt differences)

### Spacing System

```javascript
// All values in DXA (twentieths of a point, 1440 = 1 inch)
Page margins: 1440 (1 inch) all sides

Title spacing:
  - before: 0
  - after: 240

Heading 1 spacing:
  - before: 360
  - after: 180

Heading 2 spacing:
  - before: 240
  - after: 120

Body paragraph spacing:
  - after: 240
  - line height: 360 (1.6x)

Metadata spacing:
  - after: 60

Section divider:
  - before: 360
  - after: 120
```

**Design rationale:**
- 1" margins provide professional framing
- 1.6x line height optimizes readability
- Generous spacing creates breathing room

## Document Structure

### Base Configuration

```javascript
const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: "Calibri",
          size: 22,           // 11pt body text
          color: colors.bodyGray
        }
      }
    },
    paragraphStyles: [
      // Define all paragraph styles here
    ]
  },
  numbering: {
    config: [
      // Define all list configurations here
    ]
  },
  sections: [{
    properties: {
      page: {
        margin: {
          top: 1440,
          right: 1440,
          bottom: 1440,
          left: 1440
        }
      }
    },
    children: [
      // Document content here
    ]
  }]
});
```

### Style Definitions

**CRITICAL:** Override built-in Word styles using exact IDs.

```javascript
paragraphStyles: [
  // Title style
  {
    id: "Title",
    name: "Title",
    basedOn: "Normal",
    run: {
      size: 48,              // 24pt
      bold: true,
      color: colors.primaryBlue,
      font: "Calibri"
    },
    paragraph: {
      spacing: { before: 0, after: 240 },
      alignment: AlignmentType.LEFT
    }
  },

  // Heading 1 (e.g., "Executive Diagnostic")
  {
    id: "Heading1",
    name: "Heading 1",
    basedOn: "Normal",
    next: "Normal",
    quickFormat: true,
    run: {
      size: 32,              // 16pt
      bold: true,
      color: colors.primaryBlue,
      font: "Calibri"
    },
    paragraph: {
      spacing: { before: 360, after: 180 },
      outlineLevel: 0
    }
  },

  // Heading 2 (e.g., "Strengths", "Risks")
  {
    id: "Heading2",
    name: "Heading 2",
    basedOn: "Normal",
    next: "Normal",
    quickFormat: true,
    run: {
      size: 28,              // 14pt
      bold: true,
      color: colors.mediumGray,
      font: "Calibri"
    },
    paragraph: {
      spacing: { before: 240, after: 120 },
      outlineLevel: 1
    }
  },

  // Metadata (date, framework, maturity)
  {
    id: "Metadata",
    name: "Metadata",
    basedOn: "Normal",
    run: {
      size: 18,              // 9pt
      color: colors.lightGray,
      font: "Calibri"
    },
    paragraph: {
      spacing: { after: 60 }
    }
  },

  // Body emphasis (for "Overall Status" statement)
  {
    id: "BodyEmphasis",
    name: "Body Emphasis",
    basedOn: "Normal",
    run: {
      size: 22,              // 11pt
      bold: true,
      color: colors.bodyGray,
      font: "Calibri"
    }
  }
]
```

### Numbering Configuration

**CRITICAL:** Each numbered section needs its own reference to restart numbering.

```javascript
numbering: {
  config: [
    // Immediate Priority list
    {
      reference: "immediate-list",
      levels: [{
        level: 0,
        format: LevelFormat.DECIMAL,
        text: "%1.",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }
          }
        }
      }]
    },

    // Short-term Priority list (separate reference = restarts at 1)
    {
      reference: "short-term-list",
      levels: [{
        level: 0,
        format: LevelFormat.DECIMAL,
        text: "%1.",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }
          }
        }
      }]
    },

    // Medium-term Priority list (separate reference = restarts at 1)
    {
      reference: "medium-term-list",
      levels: [{
        level: 0,
        format: LevelFormat.DECIMAL,
        text: "%1.",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }
          }
        }
      }]
    },

    // Success Metrics bullet list
    {
      reference: "success-metrics-list",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "•",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }
          }
        }
      }]
    }
  ]
}
```

## Content Elements

### Dimension Summary Table

**CRITICAL:** Set columnWidths array AND individual cell widths.

```javascript
const tableBorder = {
  style: BorderStyle.SINGLE,
  size: 1,
  color: colors.tableBorder
};

const cellBorders = {
  top: tableBorder,
  bottom: tableBorder,
  left: tableBorder,
  right: tableBorder
};

new Table({
  columnWidths: [3120, 1560, 4680],  // Total = 9360 (letter width with 1" margins)
  margins: { top: 100, bottom: 100, left: 180, right: 180 },
  rows: [
    // Header row
    new TableRow({
      tableHeader: true,
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 3120, type: WidthType.DXA },
          shading: { fill: colors.tableHeaderBg, type: ShadingType.CLEAR },
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "Dimension", bold: true, size: 22 })]
          })]
        }),
        // ... other header cells
      ]
    }),

    // Data rows - color code based on score
    new TableRow({
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 3120, type: WidthType.DXA },
          children: [new Paragraph({
            children: [new TextRun({ text: "Legitimacy", bold: true })]
          })]
        }),
        new TableCell({
          borders: cellBorders,
          width: { size: 1560, type: WidthType.DXA },
          // Color based on score:
          // ≥3.5 = greenHighlight
          // 3.0-3.4 = yellowHighlight
          // <3.0 = redHighlight
          shading: { fill: getScoreColor(score), type: ShadingType.CLEAR },
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: "3.5/5", bold: true })]
          })]
        }),
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA },
          children: [new Paragraph({
            children: [new TextRun("Above Average - Real problem, genuine advantages")]
          })]
        })
      ]
    })
    // ... repeat for all 5 dimensions
  ]
})

// Helper function
function getScoreColor(score) {
  if (score >= 3.5) return colors.greenHighlight;
  if (score >= 3.0) return colors.yellowHighlight;
  return colors.redHighlight;
}
```

## Quality Validation

Before delivering, verify:

**Typography:**
- [ ] All headings use correct sizes (24pt/16pt/14pt)
- [ ] Body text is 11pt with 1.6x line height
- [ ] Metadata is 9pt gray
- [ ] Font is Calibri throughout

**Colors:**
- [ ] Headers use primaryBlue (#1B365D)
- [ ] H2 headers use mediumGray (#4A4A4A)
- [ ] Body text uses bodyGray (#2D2D2D)
- [ ] Metadata uses lightGray (#757575)
- [ ] Table scores color-coded correctly

**Spacing:**
- [ ] 1" margins all sides
- [ ] Proper spacing before/after all headings
- [ ] 1.6x line height on body paragraphs
- [ ] Generous whitespace throughout

**Tables:**
- [ ] Borders present and subtle
- [ ] Column widths set correctly
- [ ] Header row has background color
- [ ] Scores have semantic color coding
- [ ] Cell margins consistent

**Lists:**
- [ ] Each numbered section uses unique reference
- [ ] Numbering restarts at 1 for each section
- [ ] Indentation consistent (720/360)
- [ ] No unicode bullets (real Word lists only)

## Common Mistakes to Avoid

**CRITICAL ERRORS:**
- ❌ Using string "bullet" instead of LevelFormat.BULLET constant
- ❌ Using ShadingType.SOLID (causes black backgrounds)
- ❌ Not setting BOTH columnWidths array AND individual cell widths
- ❌ Using same numbering reference across sections (won't restart at 1)
- ❌ Adding custom style to heading paragraphs (breaks TOC if ever added)
- ❌ Using \n for line breaks (always use separate Paragraphs)
- ❌ Using unicode bullets (• symbol) instead of proper lists

**FORMATTING ERRORS:**
- ❌ Inconsistent spacing between sections
- ❌ Wrong color codes (typos in hex values)
- ❌ Missing cell borders
- ❌ Incorrect DXA calculations for measurements
- ❌ Forgetting to set type: ShadingType.CLEAR

**STYLE ERRORS:**
- ❌ Not overriding built-in styles (using wrong IDs)
- ❌ Missing outlineLevel on heading styles
- ❌ Not setting default font in styles.default
- ❌ Inconsistent font across document

## Design Principles Applied

This formatting follows professional design elevation principles:

1. **Typography Scale** - Clear hierarchy with meaningful size relationships
2. **Strategic Color** - Restrained palette with semantic meaning
3. **Generous White Space** - Professional margins, breathing room, 1.6x line height
4. **Hand-crafted Appearance** - Deliberate choices at every level
5. **Borrowed Excellence** - References Apple (typography), Swiss design (systematic), Stripe (data presentation)

---

**Remember:** Every formatting choice should serve readability and professional credibility. When in doubt, choose clarity and restraint over decoration.
