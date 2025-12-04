# Vianeo Executive Report: Formatting Guide

Comprehensive styling guidance for the 12-18 page Executive Report deliverable. Use this document when generating DOCX output from the prompts or when applying manual formatting in Word.

**Document Type:** Multi-section professional report with cover page
**Typical Length:** 12-18 pages
**Use Case:** Final deliverable for Vianeo validation sprint completion

---

## Quick Links

- [Design Tokens](VIANEO_Design_Tokens.md) - Canonical colors, typography, spacing
- [Diagnostic Comment Formatting Guide](VIANEO_Diagnostic_Comment_Formatting_Guide.md) - Companion 2-4 page assessment format
- [Step 10 Format Specification](FORMAT_SPEC_Step10_Diagnostic_Comment.md) - Data model feeding this report
- [Diagnostic DOCX Formatting](VIANEO_Diagnostic_DOCX_Formatting.md) - Layout and margin details

---

## Document Overview

The Vianeo Executive Report is a comprehensive document summarizing an entire validation sprint. It includes a cover page, executive summary, session-by-session breakdown, deliverables matrix, diagnostic comment, roadmap, metrics, and risk analysis.

**When to Generate:**
- At the end of a Vianeo Sprint (after Steps 11 and 12)
- Before each of the 4 client reviews (as internal documentation)
- As a final deliverable for committee presentations

**Relationship to Other Deliverables:**
- Incorporates the Diagnostic Comment (Step 10)
- References Features-Needs Matrix (Step 11)
- Includes Viability Assessment results (Step 12)

---

## Color Palette

> **Hex format:** Use hex values **without the `#` prefix** in DOCX code. Word APIs expect the raw 6-character string (e.g., `1B4F72`).

```javascript
// COLORS object used by generators
export const COLORS = {
  primary: "1B4F72",      // Deep blue - headers, titles, key emphasis
  secondary: "2874A6",    // Medium blue - subheaders, table headers
  accent: "27AE60",       // Green - success states, positive scores
  warning: "F39C12",      // Orange/amber - caution, moderate scores
  danger: "E74C3C",       // Red - failures, critical gaps
  dark: "2C3E50",         // Dark gray - body text
  gray: "7F8C8D",         // Medium gray - metadata, dates, captions
  lightGray: "ECF0F1",    // Light gray - subtle backgrounds
  white: "FFFFFF"         // White - table header text
};
```

### Color Usage Rules

| Element | Color | Hex Code |
|---------|-------|----------|
| Document title | Primary | 1B4F72 |
| H1 headers | Primary | 1B4F72 |
| H2 headers | Secondary | 2874A6 |
| H3 headers | Dark | 2C3E50 |
| Body text | Dark | 2C3E50 |
| Metadata/dates | Gray | 7F8C8D |
| Passing scores | Accent (green) | 27AE60 |
| Warning/moderate | Warning (orange) | F39C12 |
| Failing scores | Danger (red) | E74C3C |
| Table header backgrounds | Primary or Secondary | 1B4F72 or 2874A6 |
| Table header text | White | FFFFFF |

---

## Typography

### Font Family
- **Primary font:** Arial (universally supported, clean, professional)
- **Fallback:** System default sans-serif

### Font Sizes (in half-points)

| Element | Size Value | Actual Points |
|---------|------------|---------------|
| Document title | 56 | 28pt |
| Subtitle | 36 | 18pt |
| H1 headers | 32 | 16pt |
| H2 headers | 28 | 14pt |
| H3 headers | 24 | 12pt |
| Body text | 22 | 11pt |
| Table content | 20-22 | 10-11pt |
| Metadata/captions | 18-20 | 9-10pt |
| Large score displays | 40-48 | 20-24pt |

### Text Formatting

- **Bold:** Headers, labels, key terms, recommendations
- **Italics:** Metadata, dates, quoted material, emphasis
- **Color emphasis:** Score values use conditional coloring based on thresholds

---

## Page Setup

### Margins
```javascript
page: {
  margin: {
    top: 1440,    // 1 inch (1440 DXA = 1 inch)
    right: 1440,  // 1 inch
    bottom: 1440, // 1 inch
    left: 1440    // 1 inch
  }
}
```

### Orientation
- Cover page: Portrait
- Main content: Portrait
- (Landscape available for wide tables if needed)

---

## Document Structure

### Section 1: Cover Page (Separate Section)

**Elements (top to bottom):**
1. Vertical space (2400 DXA before content)
2. Project title (56pt, bold, primary color, centered)
3. Subtitle line 1 (36pt, secondary color, centered)
4. Subtitle line 2 (36pt, bold, secondary color, centered)
5. Decorative divider (accent color)
6. Principal Investigator name
7. Institution name
8. Sprint duration
9. Sessions completed
10. Prepared by section
11. Organization name
12. Team member names
13. Date
14. Page break

**Spacing Pattern:**
```javascript
// Example of large top margin
new Paragraph({ spacing: { before: 2400 }, children: [] });

// Example of spacing between major elements
// Use a value between 400 and 800 depending on importance
new Paragraph({ spacing: { before: 600 }, children: [] });

// Example of spacing between related items
// Use a value between 100 and 200
new Paragraph({ spacing: { before: 150 }, children: [] });
```

### Section 2: Main Content (Separate Section with Headers/Footers)

**Header:**
- Right-aligned
- Format: "[Project Name] [Document Type] | [Month Year]"
- Size: 18 (9pt), gray color

**Footer:**
- Centered
- Format: "Page [CURRENT] of [TOTAL] | [Organization Name]"
- Size: 18 (9pt), gray color

---

## Component Patterns

### Score Summary Box (2-Column Table)

```javascript
new Table({
  columnWidths: [4680, 4680],  // Equal halves of usable width
  rows: [
    // Header row
    new TableRow({
      children: [
        new TableCell({
          shading: { fill: COLORS.primary, type: ShadingType.CLEAR },
          children: [/* Header text, white, bold */]
        }),
        // ... second cell
      ]
    }),
    // Score row with conditional coloring
    new TableRow({
      children: [
        new TableCell({
          shading: { fill: "FADBD8", type: ShadingType.CLEAR },  // Light red for below threshold
          children: [
            new Paragraph({ /* Large score number */ }),
            new Paragraph({ /* Status text */ })
          ]
        }),
        new TableCell({
          shading: { fill: "D5F5E3", type: ShadingType.CLEAR },  // Light green for passing
          children: [/* ... */]
        })
      ]
    })
  ]
});
```

**Conditional Background Colors:**
- Passing/Strong: `"D5F5E3"` (light green)
- Warning/Moderate: `"FCF3CF"` (light yellow)
- Failing/Critical: `"FADBD8"` (light red)

### Dimension Breakdown Table (4-Column)

| Column | Width (DXA) | Content |
|--------|-------------|---------|
| Dimension | 2800 | Dimension name (bold) |
| Score | 1400 | Score value with conditional cell color |
| Status | 1400 | Status text with conditional cell color |
| Interpretation | 3760 | Brief description |

**Column widths total:** 9360 DXA (full usable width with 1" margins)

### Deliverables Matrix (3-Column)

| Column | Width (DXA) | Content |
|--------|-------------|---------|
| Deliverable | 4200 | Deliverable name |
| Status | 2000 | "Complete" with green background |
| Session | 3160 | Session reference |

### Metrics Tracking Table (3-Column)

| Column | Width (DXA) | Content |
|--------|-------------|---------|
| Metric | 4000 | Metric description |
| Current | 2680 | Current value (red/yellow background) |
| Target | 2680 | Target value (green background) |

### Risk Matrix (4-Column)

| Column | Width (DXA) | Content |
|--------|-------------|---------|
| Risk | 3000 | Risk description |
| Likelihood | 1500 | High/Medium/Low with conditional color |
| Impact | 1500 | Critical/High/Medium/Low with conditional color |
| Mitigation | 3360 | Mitigation strategy |

---

## Table Styling

### Border Configuration
```javascript
const tableBorder = {
  style: BorderStyle.SINGLE,
  size: 1,
  color: "CCCCCC"  // Light gray borders
};
const cellBorders = {
  top: tableBorder,
  bottom: tableBorder,
  left: tableBorder,
  right: tableBorder
};
```

### Header Row Pattern
```javascript
new TableRow({
  tableHeader: true,
  children: [
    new TableCell({
      borders: cellBorders,
      width: { size: 4680, type: WidthType.DXA }, // Example width
      shading: { fill: COLORS.primary, type: ShadingType.CLEAR },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "Header Text",
              bold: true,
              size: 22,
              color: COLORS.white,
              font: "Arial"
            })
          ]
        })
      ]
    })
  ]
});
```

### Data Row Pattern
```javascript
new TableRow({
  children: [
    new TableCell({
      borders: cellBorders,
      width: { size: 4680, type: WidthType.DXA }, // Example width
      shading: { fill: "D5F5E3", type: ShadingType.CLEAR }, // Example: light green for passing
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,  // or LEFT for text
          children: [
            new TextRun({
              text: "Cell content",
              size: 20,
              font: "Arial"
            })
          ]
        })
      ]
    })
  ]
});
```

---

## Bullet and Numbered Lists

### Numbering Configuration
```javascript
const numberingConfig = {
  config: [
    {
      reference: "bullet-main",  // Unique reference name
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }  // Standard indent
          }
        }
      }]
    },
    {
      reference: "numbered-phase1",  // Each numbered list needs unique reference
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
    }
    // Add more references for each separate numbered list
  ]
};
```

### List Item Pattern
```javascript
new Paragraph({
  numbering: { reference: "bullet-main", level: 0 },
  children: [
    new TextRun({
      text: "List item text",
      size: 22,
      font: "Arial"
    })
  ]
});
```

**Critical Rule:** Each separate numbered list must have its own unique reference name, or numbers will continue from previous lists.

---

## Special Elements

### Callout/Quote Box
```javascript
new Paragraph({
  shading: { fill: "EBF5FB", type: ShadingType.CLEAR },  // Light blue
  spacing: { before: 200, after: 200 },
  indent: { left: 360, right: 360 },
  children: [
    new TextRun({
      text: "Key insight or recommendation text...",
      size: 22,
      italics: true,
      font: "Arial",
      color: COLORS.dark
    })
  ]
});
```

**Callout Background Colors:**
- Informational: `"EBF5FB"` (light blue)
- Warning/Caution: `"FEF9E7"` (light yellow)
- Success/Action: `"E8F8F5"` (light green)

### Decorative Divider
```javascript
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({
      text: "\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",
      size: 28,
      color: COLORS.accent,
      font: "Arial"
    })
  ]
});
```

### Page Break
```javascript
new Paragraph({ children: [new PageBreak()] });
```

---

## Spacing Guidelines

### Between Major Sections
```javascript
spacing: { before: 400 }  // H1 headers
```

### Between Subsections
```javascript
spacing: { before: 300 }  // H2 headers
spacing: { before: 200 }  // H3 headers
```

### Between Paragraphs
```javascript
spacing: { before: 120, after: 120 }  // Standard body paragraphs
spacing: { before: 150 }  // After headers, before content
```

### Empty Spacer Paragraph
```javascript
new Paragraph({ spacing: { before: 300 }, children: [] });
```

---

## Content Organization

### Recommended Section Order

1. **Cover Page**
2. **Executive Summary** (1 page)
   - Score summary table
   - 2-3 overview paragraphs
3. **Dimension Breakdown** (1 page)
   - Full dimension table
4. **Sprint Overview** (2-3 pages)
   - Session-by-session breakdown with bullet lists
5. **Deliverables Completed** (1 page)
   - Matrix table
6. **Final Diagnostic Comment** (2-3 pages)
   - Strengths section with H3 headers
   - Critical Gaps section with H3 headers
7. **Post-Vianeo Roadmap** (1 page)
   - Phased action items
8. **Key Metrics to Track** (1 page)
   - Multiple tracking tables
9. **Risk Factors** (1 page)
   - Risk matrix table
10. **Final Assessment** (1 page)
    - Callout boxes
    - Closing attribution

---

## Helper Functions

### Create Header
```javascript
function createHeader(text, level = 1) {
  const sizes = { 1: 32, 2: 28, 3: 24 };
  const headingLevels = {
    1: HeadingLevel.HEADING_1,
    2: HeadingLevel.HEADING_2,
    3: HeadingLevel.HEADING_3
  };
  return new Paragraph({
    heading: headingLevels[level],
    spacing: { before: level === 1 ? 400 : 300, after: 200 },
    children: [
      new TextRun({
        text: text,
        bold: true,
        size: sizes[level],
        color: COLORS.primary,
        font: "Arial"
      })
    ]
  });
}
```

### Create Paragraph
```javascript
function createParagraph(text, options = {}) {
  return new Paragraph({
    spacing: { before: 120, after: 120 },
    alignment: options.align || AlignmentType.LEFT,
    children: [
      new TextRun({
        text: text,
        size: options.size || 22,
        font: "Arial",
        color: options.color || COLORS.dark,
        bold: options.bold || false,
        italics: options.italics || false
      })
    ]
  });
}
```

### Create Score Cell with Conditional Coloring
```javascript
function createScoreCell(score, threshold = 3.0) {
  const passed = score >= threshold;
  return new TableCell({
    borders: cellBorders,
    width: { size: 1200, type: WidthType.DXA },
    shading: {
      fill: passed ? "D5F5E3" : "FADBD8",
      type: ShadingType.CLEAR
    },
    children: [
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({
            text: score.toFixed(1),
            bold: true,
            size: 22,
            color: passed ? COLORS.accent : COLORS.danger,
            font: "Arial"
          })
        ]
      })
    ]
  });
}
```

---

## Required Imports

```javascript
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  Header,
  Footer,
  AlignmentType,
  PageOrientation,
  LevelFormat,
  HeadingLevel,
  BorderStyle,
  WidthType,
  PageNumber,
  PageBreak,
  ShadingType
} = require('docx');
const fs = require('fs');
```

---

## Output Generation

```javascript
const doc = new Document({
  numbering: numberingConfig,
  styles: { /* style definitions */ },
  sections: [
    { /* Cover page section */ },
    { /* Main content section with headers/footers */ }
  ]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("output.docx", buffer);
});
```

---

## Quality Checklist

Before generating the document:

- [ ] All colors use hex codes without # prefix
- [ ] All fonts explicitly set to "Arial"
- [ ] Table columnWidths array matches number of columns
- [ ] Each cell has width property matching columnWidths
- [ ] All shading uses `ShadingType.CLEAR` (never SOLID)
- [ ] Each numbered list has unique reference name
- [ ] PageBreak wrapped in Paragraph
- [ ] Headers use HeadingLevel constants
- [ ] All text uses TextRun objects (never text property on Paragraph)
- [ ] Spacing values are in DXA (1440 = 1 inch)

---

## Resource Cross-References

- **[Diagnostic Comment Formatting Guide](VIANEO_Diagnostic_Comment_Formatting_Guide.md)** - Standalone 2-4 page assessment format
- **[Design Tokens](VIANEO_Design_Tokens.md)** - Canonical colors, typography, spacing values
- **[Diagnostic DOCX Formatting](VIANEO_Diagnostic_DOCX_Formatting.md)** - Step 10 DOCX specifications
- **[Quality Control](QUICK_VALIDATION_Step10.md)** - Validation checklist
- **[Template Snippets](../tools/generators)** - Code references using these values

Use these resources alongside the palette and spacing guidance above to keep Executive Report exports consistent and error-free.

---

**Version:** 1.0
**Last Updated:** December 2025
**Created by:** 360 Social Impact Studios
