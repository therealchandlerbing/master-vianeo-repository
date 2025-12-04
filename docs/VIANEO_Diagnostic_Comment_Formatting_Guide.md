# Vianeo Diagnostic Comment: Formatting Guide

**Document Type:** Single-section assessment summary
**Typical Length:** 2-4 pages
**Use Case:** Standalone diagnostic assessment for project evaluation

---

## Document Overview

The Diagnostic Comment is a concise assessment document that summarizes the Vianeo evaluation results. It provides scores, identifies strengths and gaps, and delivers actionable recommendations. This is designed as a quick-reference document that can stand alone or accompany the full Executive Report.

**When to Generate:**
- As a standalone deliverable after any evaluation step
- Before each of the 4 client reviews (as internal documentation)
- As a quick summary for stakeholders who don't need the full Executive Report
- At the end of a Vianeo Sprint as part of the deliverables package

**Relationship to Other Deliverables:**
- Can be extracted from the full Executive Report
- Based on Step 10 Diagnostic Comment methodology
- Serves as quick-reference companion to detailed analysis

---

## Color Palette

```javascript
const COLORS = {
  primary: "1B4F72",      // Deep blue - title, H1 headers, recommendations
  secondary: "2874A6",    // Medium blue - H2 headers, table headers
  accent: "27AE60",       // Green - success states, passing scores
  warning: "F39C12",      // Orange/amber - moderate scores
  danger: "E74C3C",       // Red - failing scores, critical gaps
  dark: "2C3E50",         // Dark gray - body text
  gray: "7F8C8D",         // Medium gray - metadata, dates
  white: "FFFFFF"         // White - table header text
};
```

### Color Application

| Element | Color | When to Use |
|---------|-------|-------------|
| Document title | Primary | Always |
| "Final Assessment Comment" subtitle | Secondary | Always |
| H1 section headers | Primary | Major sections |
| H2 subsection headers | Secondary | Subsections |
| Body text | Dark | All prose content |
| Dates and metadata | Gray | Timestamps, versions |
| Score >= threshold | Accent (green) | Passing dimensions |
| Score near threshold | Warning (orange) | Moderate/adequate |
| Score < threshold | Danger (red) | Failing dimensions |

---

## Typography

### Font Family
- **Primary font:** Arial
- **Consistency:** All elements use Arial explicitly

### Font Sizes

| Element | Size (half-points) | Actual Points |
|---------|-------------------|---------------|
| Document title | 48 | 24pt |
| Subtitle | 28 | 14pt |
| H1 headers | 28 | 14pt |
| H2 headers | 24 | 12pt |
| Body text | 22 | 11pt |
| Table content | 20 | 10pt |
| Large score numbers | 40 | 20pt |
| Metadata | 18-20 | 9-10pt |
| Footer/header | 18 | 9pt |

---

## Page Setup

### Margins
```javascript
page: {
  margin: {
    top: 1440,     // 1 inch
    right: 1440,   // 1 inch
    bottom: 1440,  // 1 inch
    left: 1440     // 1 inch
  }
}
```

### Orientation
- Portrait only (no landscape sections)

### Headers and Footers

**Header (right-aligned):**
```
[Project Name] Diagnostic Comment | Updated [Month Day, Year]
```
- Size: 18 (9pt)
- Color: Gray

**Footer (centered):**
```
Page [CURRENT] | [Organization Name]
```
- Size: 18 (9pt)
- Color: Gray

---

## Document Structure

### Title Block

```javascript
// Main title
new Paragraph({
  heading: HeadingLevel.TITLE,
  children: [
    new TextRun({
      text: "[Project] Vianeo Diagnostic",
      size: 48,
      bold: true,
      color: COLORS.primary,
      font: "Arial"
    })
  ]
}),

// Subtitle
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({
      text: "Final Assessment Comment",
      size: 28,
      color: COLORS.secondary,
      font: "Arial"
    })
  ]
}),

// Date line
new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 100, after: 300 },
  children: [
    new TextRun({
      text: "Updated: [Date] ([Session Reference])",
      size: 20,
      italics: true,
      color: COLORS.gray,
      font: "Arial"
    })
  ]
})
```

### Project Information Block

```javascript
new Paragraph({
  spacing: { before: 200 },
  children: [
    new TextRun({ text: "Project: ", bold: true, size: 22, font: "Arial" }),
    new TextRun({ text: "[Project Name]", size: 22, font: "Arial" })
  ]
}),
new Paragraph({
  children: [
    new TextRun({ text: "Principal Investigator: ", bold: true, size: 22, font: "Arial" }),
    new TextRun({ text: "[Name, Institution]", size: 22, font: "Arial" })
  ]
})
```

---

## Score Summary Table

### Layout (2-Column Equal Width)

```javascript
new Table({
  columnWidths: [4680, 4680],  // Equal halves
  rows: [
    // Header row
    new TableRow({
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA },
          shading: { fill: COLORS.primary, type: ShadingType.CLEAR },
          children: [
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 80, after: 80 },
              children: [
                new TextRun({
                  text: "Market Maturity Score",
                  bold: true,
                  size: 22,
                  color: COLORS.white,
                  font: "Arial"
                })
              ]
            })
          ]
        }),
        // Second header cell (Overall Vianeo Score)
      ]
    }),
    // Score display row
    new TableRow({
      children: [
        new TableCell({
          borders: cellBorders,
          width: { size: 4680, type: WidthType.DXA },
          children: [
            // Large score number
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { before: 150 },
              children: [
                new TextRun({
                  text: "3.1 / 5.0",  // Example
                  bold: true,
                  size: 40,
                  color: COLORS.warning,  // Conditional
                  font: "Arial"
                })
              ]
            }),
            // Status text
            new Paragraph({
              alignment: AlignmentType.CENTER,
              spacing: { after: 150 },
              children: [
                new TextRun({
                  text: "Below 3.2 threshold",
                  size: 18,
                  color: COLORS.danger,
                  font: "Arial"
                })
              ]
            })
          ]
        }),
        // Second score cell
      ]
    })
  ]
});
```

### Score Color Logic

```javascript
// For Market Maturity (threshold 3.2)
const marketColor = score >= 3.2 ? COLORS.accent : COLORS.warning;
const marketStatus = score >= 3.2 ? "Meets threshold" : "Below 3.2 threshold";

// For Overall Score
const overallColor = score >= 4.0 ? COLORS.accent :
                     score >= 3.0 ? COLORS.warning : COLORS.danger;
const overallStatus = score >= 4.0 ? "PROMISING" :
                      score >= 3.0 ? "DEVELOPING" : "AT RISK";
```

---

## Dimension Breakdown Table

### Layout (3-Column)

| Column | Width (DXA) | Purpose |
|--------|-------------|---------|
| Dimension | 2500 | Dimension name |
| Score | 1500 | Numeric score |
| Status | 5360 | Status label with conditional coloring |

**Total width:** 9360 DXA

### Conditional Cell Backgrounds

| Status | Background Color |
|--------|-----------------|
| Strong | `"D5F5E3"` (light green) |
| Adequate | `"FCF3CF"` (light yellow) |
| Needs Work | `"FCF3CF"` (light yellow) |
| Critical | `"FADBD8"` (light red) |

### Row Pattern

```javascript
new TableRow({
  children: [
    // Dimension name
    new TableCell({
      borders: cellBorders,
      width: { size: 2500, type: WidthType.DXA },
      children: [
        new Paragraph({
          children: [
            new TextRun({
              text: "Legitimacy",
              bold: true,
              size: 20,
              font: "Arial"
            })
          ]
        })
      ]
    }),
    // Score
    new TableCell({
      borders: cellBorders,
      width: { size: 1500, type: WidthType.DXA },
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "4.7 / 5.0",
              bold: true,
              size: 20,
              font: "Arial"
            })
          ]
        })
      ]
    }),
    // Status with conditional background
    new TableCell({
      borders: cellBorders,
      width: { size: 5360, type: WidthType.DXA },
      shading: { fill: "D5F5E3", type: ShadingType.CLEAR },
      children: [
        new Paragraph({
          children: [
            new TextRun({
              text: "Strong",
              bold: true,
              size: 20,
              font: "Arial"
            })
          ]
        })
      ]
    })
  ]
})
```

---

## Content Sections

### Strengths Section

**Header:**
```javascript
new Paragraph({
  heading: HeadingLevel.HEADING_2,
  children: [
    new TextRun({
      text: "Strengths Confirmed Through Validation Sprint",
      bold: true,
      size: 24,
      color: COLORS.secondary,
      font: "Arial"
    })
  ]
})
```

**Strength Item Pattern:**
```javascript
new Paragraph({
  spacing: { before: 150 },
  children: [
    new TextRun({
      text: "Strength Title: ",
      bold: true,
      size: 22,
      font: "Arial"
    }),
    new TextRun({
      text: "Description of the strength with supporting evidence.",
      size: 22,
      font: "Arial"
    })
  ]
})
```

### Critical Gaps Section

**Header:**
```javascript
new Paragraph({
  heading: HeadingLevel.HEADING_2,
  children: [
    new TextRun({
      text: "Critical Gaps Requiring Post-Vianeo Action",
      bold: true,
      size: 24,
      color: COLORS.secondary,
      font: "Arial"
    })
  ]
})
```

**Gap Item Pattern:**
```javascript
// Gap title with score
new Paragraph({
  spacing: { before: 150 },
  children: [
    new TextRun({
      text: "1. Gap Name (Score: X/5)",
      bold: true,
      size: 22,
      font: "Arial"
    })
  ]
}),

// Gap description with recommendation
new Paragraph({
  children: [
    new TextRun({
      text: "Description of the gap. ",
      size: 22,
      font: "Arial"
    }),
    new TextRun({
      text: "Recommendation: Specific action to address the gap.",
      bold: true,
      size: 22,
      color: COLORS.primary,
      font: "Arial"
    })
  ]
})
```

---

## Callout Boxes

### Final Assessment Box

```javascript
new Paragraph({
  shading: { fill: "EBF5FB", type: ShadingType.CLEAR },  // Light blue
  spacing: { before: 200, after: 200 },
  indent: { left: 360, right: 360 },
  children: [
    new TextRun({
      text: "Summary assessment text with key insights...",
      size: 22,
      italics: true,
      font: "Arial",
      color: COLORS.dark
    })
  ]
})
```

### Recommendation Box

```javascript
new Paragraph({
  shading: { fill: "E8F8F5", type: ShadingType.CLEAR },  // Light green
  spacing: { before: 200, after: 200 },
  indent: { left: 360, right: 360 },
  children: [
    new TextRun({
      text: "Recommended next step: Specific action recommendation...",
      size: 22,
      bold: true,
      font: "Arial",
      color: COLORS.primary
    })
  ]
})
```

### Box Background Colors

| Purpose | Background Color |
|---------|-----------------|
| Informational/Summary | `"EBF5FB"` (light blue) |
| Warning/Caution | `"FEF9E7"` (light yellow) |
| Action/Recommendation | `"E8F8F5"` (light green) |

---

## Closing Section

### Decorative Divider

```javascript
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({
      text: "\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",
      size: 24,
      color: COLORS.accent,
      font: "Arial"
    })
  ]
})
```

### Attribution Block

```javascript
new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 100 },
  children: [
    new TextRun({
      text: "Assessment prepared by [Organization] / [Program Name]",
      size: 18,
      color: COLORS.gray,
      font: "Arial"
    })
  ]
}),
new Paragraph({
  alignment: AlignmentType.CENTER,
  children: [
    new TextRun({
      text: "[Date]",
      size: 18,
      color: COLORS.gray,
      font: "Arial"
    })
  ]
}),
new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 100 },
  children: [
    new TextRun({
      text: "Next Review: [Milestone] (Target: [Date])",
      size: 16,
      italics: true,
      color: COLORS.gray,
      font: "Arial"
    })
  ]
})
```

---

## Table Styling

### Border Configuration

```javascript
const tableBorder = {
  style: BorderStyle.SINGLE,
  size: 1,
  color: "CCCCCC"
};
const cellBorders = {
  top: tableBorder,
  bottom: tableBorder,
  left: tableBorder,
  right: tableBorder
};
```

### Header Row

```javascript
new TableRow({
  tableHeader: true,
  children: [
    new TableCell({
      borders: cellBorders,
      width: { size: WIDTH, type: WidthType.DXA },
      shading: { fill: COLORS.secondary, type: ShadingType.CLEAR },
      children: [
        new Paragraph({
          children: [
            new TextRun({
              text: "Header Text",
              bold: true,
              size: 20,
              color: COLORS.white,
              font: "Arial"
            })
          ]
        })
      ]
    })
  ]
})
```

---

## Numbering Configuration

```javascript
const numberingConfig = {
  config: [
    {
      reference: "bullet-list",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: {
          paragraph: {
            indent: { left: 720, hanging: 360 }
          }
        }
      }]
    },
    {
      reference: "numbered-list",
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
  ]
};
```

---

## Spacing Guidelines

| Context | Spacing Value |
|---------|--------------|
| After title block | 300 DXA |
| Before H1 headers | 300-400 DXA |
| After H1 headers | 150 DXA |
| Before H2 headers | 200-300 DXA |
| After H2 headers | 100 DXA |
| Between strength/gap items | 150 DXA |
| Before callout boxes | 200 DXA |
| After callout boxes | 200 DXA |
| Before closing divider | 400 DXA |

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
  LevelFormat,
  HeadingLevel,
  BorderStyle,
  WidthType,
  PageNumber,
  ShadingType
} = require('docx');
const fs = require('fs');
```

---

## Style Configuration

```javascript
const doc = new Document({
  numbering: numberingConfig,
  styles: {
    default: {
      document: {
        run: { font: "Arial", size: 22 }
      }
    },
    paragraphStyles: [
      {
        id: "Title",
        name: "Title",
        basedOn: "Normal",
        run: { size: 48, bold: true, color: COLORS.primary, font: "Arial" },
        paragraph: {
          spacing: { before: 0, after: 200 },
          alignment: AlignmentType.CENTER
        }
      },
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 28, bold: true, color: COLORS.primary, font: "Arial" },
        paragraph: {
          spacing: { before: 300, after: 150 },
          outlineLevel: 0
        }
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 24, bold: true, color: COLORS.secondary, font: "Arial" },
        paragraph: {
          spacing: { before: 200, after: 100 },
          outlineLevel: 1
        }
      }
    ]
  },
  sections: [{ /* content */ }]
});
```

---

## Content Checklist

A complete Diagnostic Comment should include:

- [ ] Title and subtitle block
- [ ] Update date with session reference
- [ ] Project and PI information
- [ ] Score summary table (2 scores)
- [ ] Dimension breakdown table (5 dimensions)
- [ ] Strengths section (3-5 strengths)
- [ ] Critical Gaps section (3-5 gaps with recommendations)
- [ ] Summary callout box
- [ ] Recommendation callout box
- [ ] Decorative divider
- [ ] Attribution and date
- [ ] Next review milestone

---

## Output Generation

```javascript
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("Diagnostic_Comment.docx", buffer);
  console.log("Document created successfully!");
});
```

---

## Differences from Executive Report

| Aspect | Diagnostic Comment | Executive Report |
|--------|-------------------|------------------|
| Length | 2-4 pages | 12-18 pages |
| Sections | Single section | Multiple sections |
| Cover page | No | Yes |
| Session breakdown | No | Yes (detailed) |
| Deliverables matrix | No | Yes |
| Roadmap phases | No | Yes |
| Metrics tables | No | Yes |
| Risk matrix | No | Yes |
| Purpose | Quick reference | Comprehensive record |

---

## Related Documents

- **[VIANEO_Executive_Report_Formatting_Guide.md](VIANEO_Executive_Report_Formatting_Guide.md)** - Full executive report format
- **[VIANEO_Design_Tokens.md](VIANEO_Design_Tokens.md)** - Design system reference
- **[VIANEO_Document_Formatting_Guide.md](VIANEO_Document_Formatting_Guide.md)** - General document formatting
- **[VIANEO_Diagnostic_DOCX_Formatting.md](VIANEO_Diagnostic_DOCX_Formatting.md)** - Step 10 DOCX specifications
- **[FORMAT_SPEC_Step10_Diagnostic_Comment.md](FORMAT_SPEC_Step10_Diagnostic_Comment.md)** - Step 10 format specification

---

**Version:** 1.0
**Last Updated:** December 2025
**Created by:** 360 Social Impact Studios
