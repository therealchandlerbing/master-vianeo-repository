# VIANEO Design Tokens

> **Single source of truth for all visual design decisions across VIANEO outputs**

**Version**: 1.0
**Status**: Production
**Last Updated**: November 2025

---

## Purpose & Usage

This document defines the official design tokens for all VIANEO Framework outputs. Use this as your primary reference when:

- Creating Word/DOCX documents
- Generating PDF reports
- Developing automation scripts
- Ensuring brand consistency across deliverables

**Priority**: This file supersedes any conflicting values in other documentation. If you find inconsistencies, update the other file to match these tokens.

### Important: HTML Template Guidance

**Existing HTML templates** (in `/templates/*.html`) already have embedded CSS with their own design system. When working with HTML outputs:

1. **Preserve existing HTML styles** - Do not override established HTML template CSS
2. **Use this file for NEW HTML** - Only reference these tokens when creating new HTML tools
3. **DOCX/PDF are primary targets** - This design system is primarily for Word documents and PDF outputs

**This is NOT a 360 Social Impact style guide.** This is the VIANEO Framework design system. Do not apply 360 branding colors to VIANEO outputs.

---

## Color System

### Primary Palette

The VIANEO primary palette balances professionalism with clarity. These colors work across print (Word/PDF) and digital (HTML) contexts.

| Token Name | Hex | RGB | HSL | Use Case |
|------------|-----|-----|-----|----------|
| **Primary Navy** | `#1a365d` | `26, 54, 93` | `215, 56%, 23%` | Main headers, primary actions, hero elements |
| **Primary Blue** | `#2E5C8A` | `46, 92, 138` | `210, 50%, 36%` | Section headers, emphasis, Word doc headers |
| **Primary Light** | `#2c5282` | `44, 82, 130` | `213, 49%, 34%` | Secondary headers, hover states |
| **Accent Teal** | `#17A2B8` | `23, 162, 184` | `187, 78%, 41%` | Callouts, links, interactive elements |
| **Accent Cyan** | `#3182ce` | `49, 130, 206` | `209, 62%, 50%` | Info highlights, secondary actions |

**When to use which blue:**
- **Primary Navy** (`#1a365d`): HTML dashboards, digital-first outputs
- **Primary Blue** (`#2E5C8A`): Word documents, print-ready materials
- Both are "VIANEO Blue" - context determines choice

### Neutral Palette

| Token Name | Hex | RGB | Use Case |
|------------|-----|-----|----------|
| **Text Primary** | `#1a202c` | `26, 32, 44` | Main body text, headings |
| **Text Secondary** | `#4a5568` | `74, 85, 104` | Subtitles, secondary content |
| **Text Tertiary** | `#718096` | `113, 128, 150` | Captions, metadata, timestamps |
| **Dark Gray** | `#6C757D` | `108, 117, 125` | Borders, disabled states, Word doc body |
| **Border** | `#e2e8f0` | `226, 232, 240` | Table borders, dividers, cards |
| **Light Gray** | `#E9ECEF` | `233, 236, 239` | Table headers, section backgrounds |
| **Background** | `#f7fafc` | `247, 250, 252` | Page backgrounds, alternate rows |
| **Surface** | `#ffffff` | `255, 255, 255` | Cards, modals, content areas |

### Status Colors

Use consistently across all outputs for immediate recognition.

| Status | Hex | RGB | Token Name | Use Case |
|--------|-----|-----|------------|----------|
| **Success** | `#10b981` | `16, 185, 129` | `--color-success` | Validated, complete, passing, GO decisions |
| **Warning** | `#f59e0b` | `245, 158, 11` | `--color-warning` | Caution, medium priority, needs attention |
| **Danger** | `#ef4444` | `239, 68, 68` | `--color-danger` | Critical, high risk, NO-GO, blockers |
| **Info** | `#3b82f6` | `59, 130, 246` | `--color-info` | Informational, neutral highlights |

**Legacy/Print equivalents:**
| Status | Print Hex | Use in Word Docs |
|--------|-----------|------------------|
| Success | `#28A745` | Checkmarks, positive indicators |
| Warning | `#FFA726` | Medium priority items |
| Danger | `#EF5350` | Critical actions, gates |

### Validation Level Colors

For VIANEO scoring and assessment outputs:

| Level | Hex | Background | Use Case |
|-------|-----|------------|----------|
| **High Validation** | `#10b981` | `#d1fae5` | Score ≥4.0, strong evidence |
| **Medium Validation** | `#f59e0b` | `#fef3c7` | Score 3.0-3.9, partial evidence |
| **Low Validation** | `#ef4444` | `#fee2e2` | Score <3.0, weak/no evidence |

### Dimension Colors

For the 5 VIANEO dimensions (use in charts, headers, badges):

| Dimension | Primary Hex | Light Hex | Weight |
|-----------|-------------|-----------|--------|
| **Legitimacy** | `#8b5cf6` | `#ede9fe` | 15% |
| **Desirability** | `#10b981` | `#d1fae5` | 25% |
| **Acceptability** | `#3b82f6` | `#dbeafe` | 20% |
| **Feasibility** | `#f59e0b` | `#fef3c7` | 20% |
| **Viability** | `#ec4899` | `#fce7f3` | 20% |

### Product/Progress Status Colors

For Step 12 dashboards and project tracking:

| Status | Hex | Use Case |
|--------|-----|----------|
| **MVP Ready** | `#10b981` | Product ready for launch |
| **In Progress** | `#3b82f6` | Active development |
| **Planning** | `#8b5cf6` | In planning phase |
| **Blocked** | `#ef4444` | Blocked, needs intervention |

---

## Typography System

### Font Stack

```css
/* Primary font stack - use for all VIANEO outputs */
--font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Monospace - for code, data, technical content */
--font-mono: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', monospace;
```

**Word Document Fonts:**
- **Primary**: Calibri (preferred), Arial (fallback)
- **Acceptable**: Segoe UI, Helvetica Neue, Open Sans
- **Never use**: Times New Roman, Comic Sans, decorative fonts

### Type Scale

| Element | HTML (px/rem) | Word (pt) | Weight | Line Height |
|---------|---------------|-----------|--------|-------------|
| **Display** | 36px / 2.25rem | - | 700 | 1.2 |
| **H1 / Doc Title** | 30px / 1.875rem | 20pt | 700 | 1.2 |
| **H2 / Section** | 24px / 1.5rem | 16pt | 600 | 1.3 |
| **H3 / Subsection** | 20px / 1.25rem | 14pt | 600 | 1.4 |
| **H4 / Sub-subsection** | 18px / 1.125rem | 12pt | 600 | 1.4 |
| **Body** | 16px / 1rem | 11pt | 400 | 1.6 |
| **Body Small** | 14px / 0.875rem | 10pt | 400 | 1.5 |
| **Caption** | 12px / 0.75rem | 9pt | 400 | 1.4 |
| **Overline** | 11px / 0.6875rem | 8pt | 500 | 1.3 |

### Font Weights

| Weight Name | Value | Use Case |
|-------------|-------|----------|
| **Regular** | 400 | Body text, descriptions |
| **Medium** | 500 | Subtle emphasis, overlines |
| **Semibold** | 600 | Subheadings, labels |
| **Bold** | 700 | Headings, strong emphasis |

---

## Spacing System

### Base Unit

All spacing derives from a 4px base unit.

| Token | Value | Use Case |
|-------|-------|----------|
| `--space-1` | 4px | Tight spacing, inline elements |
| `--space-2` | 8px | Related elements, icon gaps |
| `--space-3` | 12px | Form fields, small cards |
| `--space-4` | 16px | Standard padding, card content |
| `--space-5` | 20px | Section padding |
| `--space-6` | 24px | Large gaps, section breaks |
| `--space-8` | 32px | Major sections |
| `--space-10` | 40px | Page sections |
| `--space-12` | 48px | Hero spacing |
| `--space-16` | 64px | Major page breaks |

### Word Document Spacing

| Element | Space Before | Space After |
|---------|--------------|-------------|
| H1 / Section Header | 12pt | 6pt |
| H2 / Subsection | 10pt | 4pt |
| H3 / Sub-subsection | 8pt | 3pt |
| Body Paragraph | 0pt | 6pt |
| List Item | 0pt | 3pt |
| Table | 6pt | 6pt |

---

## Border & Shadow System

### Border Radius

| Token | Value | Use Case |
|-------|-------|----------|
| `--radius-none` | 0 | Tables, formal documents |
| `--radius-sm` | 4px | Buttons, inputs |
| `--radius-md` | 8px | Cards, modals |
| `--radius-lg` | 12px | Large cards, panels |
| `--radius-xl` | 16px | Hero sections |
| `--radius-full` | 9999px | Pills, avatars |

### Border Widths

| Token | Value | Use Case |
|-------|-------|----------|
| `--border-thin` | 1px | Standard borders |
| `--border-medium` | 2px | Emphasis borders, callouts |
| `--border-thick` | 4px | Strong emphasis, active states |

### Shadows

```css
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
```

---

## Component Tokens

### Tables

| Property | Value | Notes |
|----------|-------|-------|
| Header Background | `#E9ECEF` (Light Gray) | Or Primary Blue for emphasis |
| Header Text | `#2E5C8A` (Primary Blue) | White if on blue background |
| Cell Border | `#e2e8f0` | 1px solid |
| Header Border Bottom | `#2E5C8A` | 2px solid for emphasis |
| Row Hover | `#f7fafc` | Subtle highlight |
| Alternate Row | `#f8f9fa` | Optional zebra striping |
| Cell Padding | 8px 12px | Comfortable reading |

### Cards

| Property | Value |
|----------|-------|
| Background | `#ffffff` |
| Border | `1px solid #e2e8f0` |
| Border Radius | 8px |
| Padding | 16px - 24px |
| Shadow | `--shadow-sm` or `--shadow-md` |

### Buttons

| Variant | Background | Text | Border |
|---------|------------|------|--------|
| **Primary** | `#1a365d` | `#ffffff` | none |
| **Secondary** | `#ffffff` | `#1a365d` | `1px solid #1a365d` |
| **Success** | `#10b981` | `#ffffff` | none |
| **Danger** | `#ef4444` | `#ffffff` | none |
| **Ghost** | transparent | `#1a365d` | none |

### Callout Boxes

| Type | Border Color | Background | Icon |
|------|--------------|------------|------|
| **Info** | `#3b82f6` | `#dbeafe` | i |
| **Success** | `#10b981` | `#d1fae5` | check |
| **Warning** | `#f59e0b` | `#fef3c7` | alert |
| **Critical** | `#ef4444` | `#fee2e2` | x |

---

## Ready-to-Use Code

### CSS Variables

Copy this block into any HTML template:

```css
:root {
    /* Primary Colors */
    --color-primary: #1a365d;
    --color-primary-light: #2c5282;
    --color-primary-lighter: #4a5d7f;
    --color-primary-word: #2E5C8A;
    --color-accent: #17A2B8;
    --color-accent-light: #3182ce;

    /* Surface Colors */
    --color-surface: #ffffff;
    --color-background: #f7fafc;
    --color-border: #e2e8f0;
    --color-border-light: #E9ECEF;

    /* Text Colors */
    --color-text-primary: #1a202c;
    --color-text-secondary: #4a5568;
    --color-text-tertiary: #718096;
    --color-text-muted: #6C757D;

    /* Status Colors */
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    --color-info: #3b82f6;

    /* Status Backgrounds */
    --bg-success: #d1fae5;
    --bg-warning: #fef3c7;
    --bg-danger: #fee2e2;
    --bg-info: #dbeafe;

    /* Validation Colors */
    --color-validation-high: #10b981;
    --color-validation-medium: #f59e0b;
    --color-validation-low: #ef4444;

    /* Dimension Colors */
    --color-legitimacy: #8b5cf6;
    --color-desirability: #10b981;
    --color-acceptability: #3b82f6;
    --color-feasibility: #f59e0b;
    --color-viability: #ec4899;

    /* Typography */
    --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Roboto, sans-serif;
    --font-mono: 'SF Mono', Monaco, monospace;

    /* Spacing */
    --space-1: 4px;
    --space-2: 8px;
    --space-3: 12px;
    --space-4: 16px;
    --space-6: 24px;
    --space-8: 32px;

    /* Borders */
    --radius-sm: 4px;
    --radius-md: 8px;
    --radius-lg: 12px;

    /* Shadows */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
```

### Python Dictionary

For automation scripts and data processing:

```python
VIANEO_COLORS = {
    # Primary
    "primary": "#1a365d",
    "primary_light": "#2c5282",
    "primary_word": "#2E5C8A",
    "accent": "#17A2B8",

    # Neutrals
    "text_primary": "#1a202c",
    "text_secondary": "#4a5568",
    "text_tertiary": "#718096",
    "border": "#e2e8f0",
    "background": "#f7fafc",
    "surface": "#ffffff",

    # Status
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "info": "#3b82f6",

    # Validation
    "validation_high": "#10b981",
    "validation_medium": "#f59e0b",
    "validation_low": "#ef4444",

    # Dimensions
    "legitimacy": "#8b5cf6",
    "desirability": "#10b981",
    "acceptability": "#3b82f6",
    "feasibility": "#f59e0b",
    "viability": "#ec4899",
}

VIANEO_TYPOGRAPHY = {
    "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
    "font_word": "Calibri, Arial, sans-serif",
    "sizes": {
        "h1": "20pt",
        "h2": "16pt",
        "h3": "14pt",
        "h4": "12pt",
        "body": "11pt",
        "small": "10pt",
        "caption": "9pt",
    }
}
```

### JavaScript Object

For web applications and interactive tools:

```javascript
const VIANEO_TOKENS = {
  colors: {
    primary: {
      DEFAULT: '#1a365d',
      light: '#2c5282',
      word: '#2E5C8A',
    },
    accent: {
      DEFAULT: '#17A2B8',
      light: '#3182ce',
    },
    text: {
      primary: '#1a202c',
      secondary: '#4a5568',
      tertiary: '#718096',
    },
    status: {
      success: '#10b981',
      warning: '#f59e0b',
      danger: '#ef4444',
      info: '#3b82f6',
    },
    validation: {
      high: '#10b981',
      medium: '#f59e0b',
      low: '#ef4444',
    },
    dimensions: {
      legitimacy: '#8b5cf6',
      desirability: '#10b981',
      acceptability: '#3b82f6',
      feasibility: '#f59e0b',
      viability: '#ec4899',
    },
  },
  spacing: {
    1: '4px',
    2: '8px',
    3: '12px',
    4: '16px',
    6: '24px',
    8: '32px',
  },
  borderRadius: {
    sm: '4px',
    md: '8px',
    lg: '12px',
  },
};
```

---

## Accessibility Requirements

### Color Contrast

All text must meet WCAG AA standards:

| Text Type | Minimum Ratio | Notes |
|-----------|---------------|-------|
| Normal text (<18px) | 4.5:1 | Body copy, labels |
| Large text (≥18px bold, ≥24px) | 3:1 | Headings, buttons |
| UI components | 3:1 | Icons, borders |

**Pre-validated combinations:**
| Background | Text Color | Ratio | Status |
|------------|------------|-------|--------|
| `#ffffff` | `#1a202c` | 15.5:1 | Pass |
| `#ffffff` | `#4a5568` | 7.0:1 | Pass |
| `#1a365d` | `#ffffff` | 12.6:1 | Pass |
| `#f7fafc` | `#1a202c` | 14.8:1 | Pass |
| `#d1fae5` | `#1a202c` | 13.2:1 | Pass |

**Avoid these combinations:**
- Yellow (`#f59e0b`) text on white background
- Light gray text on light backgrounds
- Accent teal (`#17A2B8`) for small body text on white

### Focus States

All interactive elements must have visible focus indicators:

```css
:focus {
    outline: 2px solid var(--color-accent);
    outline-offset: 2px;
}

:focus:not(:focus-visible) {
    outline: none;
}

:focus-visible {
    outline: 2px solid var(--color-accent);
    outline-offset: 2px;
}
```

---

## Quick Reference Tables

### Color Cheat Sheet (Copy-Paste)

```
PRIMARY NAVY:    #1a365d | rgb(26, 54, 93)
PRIMARY BLUE:    #2E5C8A | rgb(46, 92, 138)
ACCENT TEAL:     #17A2B8 | rgb(23, 162, 184)

SUCCESS:         #10b981 | rgb(16, 185, 129)
WARNING:         #f59e0b | rgb(245, 158, 11)
DANGER:          #ef4444 | rgb(239, 68, 68)
INFO:            #3b82f6 | rgb(59, 130, 246)

TEXT PRIMARY:    #1a202c | rgb(26, 32, 44)
TEXT SECONDARY:  #4a5568 | rgb(74, 85, 104)
BORDER:          #e2e8f0 | rgb(226, 232, 240)
BACKGROUND:      #f7fafc | rgb(247, 250, 252)
```

### Typography Cheat Sheet

```
DOCUMENT TITLE:  20pt Bold, Primary Blue
SECTION (H1):    16pt Bold, Primary Blue
SUBSECTION (H2): 14pt Bold, Teal Accent
SUB-SUB (H3):    12pt Bold, Dark Gray
BODY:            11pt Regular, Black
TABLE CONTENT:   10pt Regular, Black
CAPTION/FOOTER:  9pt Italic, Dark Gray
```

### VIANEO Dimension Thresholds

```
Legitimacy:    ≥3.0 (15% weight) | #8b5cf6
Desirability:  ≥3.5 (25% weight) | #10b981  ← HIGHEST BAR
Acceptability: ≥3.0 (20% weight) | #3b82f6
Feasibility:   ≥3.0 (20% weight) | #f59e0b
Viability:     ≥3.0 (20% weight) | #ec4899

OVERALL:       ≥3.2 weighted average for GO
```

---

## Document Reference

This design tokens file is referenced by:

- `docs/FORMATTING_STRATEGY.md` - Overall formatting approach
- `docs/VIANEO_Document_Formatting_Guide.md` - Word document formatting
- `docs/FORMAT_SPEC_*.md` - Step-specific format specifications
- `templates/*.html` - Interactive HTML tools

When creating new outputs, always reference this file for color and typography values.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | November 2025 | Initial release - unified design system |

---

**Document Status**: Active - Single Source of Truth
**Maintainer**: VIANEO Framework Team
**Review Cycle**: Update when adding new output types or dimensions
