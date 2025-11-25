# Vianeo Document Formatting Guide
## Professional Styling for Desirability Analysis Documents

---

> **Design System Reference**: For the authoritative color values, typography scales, and ready-to-use code snippets, see **[VIANEO_Design_Tokens.md](VIANEO_Design_Tokens.md)**. This guide provides Word-specific formatting instructions; the Design Tokens file is the single source of truth for all visual design decisions.

---

## PURPOSE

This guide provides step-by-step instructions for formatting the three Word documents in the Vianeo Desirability: Needs/Requesters analysis package. Use this to ensure consistent, professional appearance across all deliverables.

**Who should use this:**
- Team members formatting Word documents
- External contractors/VAs handling document production
- Anyone converting markdown to Word format
- Automated systems (Zapier workflows) applying styling

---

## TABLE OF CONTENTS

1. [Brand Color Palette](#brand-colors)
2. [Typography Standards](#typography)
3. [Document Setup](#document-setup)
4. [Component Formatting Guide](#component-formatting)
5. [Document-Specific Instructions](#document-specific)
6. [Quick Reference Tables](#quick-reference)
7. [Common Mistakes to Avoid](#common-mistakes)

---

## BRAND COLORS

### Primary Color Palette

Use these exact colors for all Vianeo documents:

| Color Name | Hex Code | RGB Values | Use Case |
|------------|----------|------------|----------|
| **Primary Blue** | `#2E5C8A` | R:46 G:92 B:138 | Main headers, primary emphasis |
| **Teal Accent** | `#17A2B8` | R:23 G:162 B:184 | Secondary headers, callouts |
| **Dark Gray** | `#6C757D` | R:108 G:117 B:125 | Body text, subtitles |
| **Light Gray** | `#E9ECEF` | R:233 G:236 B:239 | Table headers, section dividers |
| **Success Green** | `#28A745` | R:40 G:167 B:69 | Positive indicators, checkmarks |
| **Warning Orange** | `#FFA726` | R:255 G:167 B:38 | Medium priority, cautions |
| **Alert Red** | `#EF5350` | R:239 G:83 B:80 | High priority, critical actions |

### How to Apply Colors in Word

**Method 1: Using Hex Codes**
1. Select text
2. Home tab → Font Color dropdown
3. Click "More Colors"
4. Select "Custom" tab
5. Change "Color model" to RGB
6. Enter RGB values from table above

**Method 2: Using Theme Colors**
1. Design tab → Colors dropdown
2. Click "Customize Colors"
3. Set theme colors to values above
4. Save as "Vianeo Palette"
5. Apply throughout document

---

## TYPOGRAPHY

### Font Selection

**Primary Font:** Calibri (preferred) or Arial
- Professional sans-serif
- High readability
- Standard on Microsoft Office

**Acceptable Alternatives:**
- Segoe UI
- Helvetica Neue
- Open Sans (if available)

**Do NOT use:**
- Times New Roman (too formal, dated)
- Comic Sans (unprofessional)
- Decorative or script fonts

### Font Size Hierarchy

| Element | Size | Weight | Color | Notes |
|---------|------|--------|-------|-------|
| **Document Title** | 20pt | Bold | Primary Blue (#2E5C8A) | Main title only |
| **Document Subtitle** | 16pt | Bold | Dark Gray (#6C757D) | Project name |
| **Secondary Line** | 14pt | Regular | Dark Gray (#6C757D) | "Core Analysis", etc. |
| **Section Headers (H1)** | 16pt | Bold | Primary Blue (#2E5C8A) | ALL CAPS optional |
| **Subsection Headers (H2)** | 14pt | Bold | Teal Accent (#17A2B8) | Title Case |
| **Sub-subsection (H3)** | 12pt | Bold | Dark Gray (#6C757D) | Title Case |
| **Body Text** | 11pt | Regular | Black (#000000) | Standard paragraphs |
| **Table Text** | 10pt | Regular | Black (#000000) | Cell content |
| **Table Headers** | 11pt | Bold | White (#FFFFFF) | On colored background |
| **Footer Text** | 9pt | Italic | Dark Gray (#6C757D) | Page footer content |
| **Emphasis** | 11pt | Bold | Black (#000000) | Bold within body text |
| **Notes/Caveats** | 10pt | Italic | Dark Gray (#6C757D) | Explanatory notes |

### Line Spacing and Paragraph Settings

**Body Text:**
- Line spacing: 1.15 or 1.5
- Space before paragraph: 0pt
- Space after paragraph: 6pt

**Headers:**
- Space before: 12pt (H1), 10pt (H2), 8pt (H3)
- Space after: 6pt (H1), 4pt (H2), 3pt (H3)

**Lists:**
- Bullet/number spacing: 1.0
- Hanging indent: 0.25"

---

## DOCUMENT SETUP

### Page Setup (All Documents)

**Orientation:** Portrait

**Margins:**
- Top: 1.0"
- Bottom: 1.0"
- Left: 1.0"
- Right: 1.0"

**Paper Size:** Letter (8.5" × 11")

### Headers and Footers

**Header (First Page):**
- Document title (20pt Bold, Primary Blue)
- Project name (16pt Bold, Dark Gray)
- Secondary line (14pt Regular, Dark Gray)
- Horizontal line separator (Light Gray, 1pt)

**Header (Subsequent Pages):**
- Project name (10pt Regular, Dark Gray)
- Aligned left
- Light gray horizontal line below

**Footer (All Pages):**
- Left-aligned: *Analysis Completed: [Date]*
- Center: Page X of Y
- Right-aligned: Framework citation
- Font: 9pt Italic, Dark Gray
- Light gray horizontal line above

### How to Create Headers/Footers in Word

1. Insert tab → Header → Edit Header
2. Different First Page: Check this box (Design tab)
3. Format first page header per specs above
4. Navigate to page 2 header (different format)
5. Repeat for footers

---

## COMPONENT FORMATTING

### Tables

#### Basic Table Style

**Table Properties:**
- Border: All cells, 0.5pt, Dark Gray (#6C757D)
- Cell padding: 0.05" on all sides
- Alignment: Top-left for text, top-center for headers

**Header Row:**
- Fill: Light Gray (#E9ECEF)
- Text: 11pt Bold, Primary Blue (#2E5C8A)
- Alignment: Center
- Border bottom: 1pt, Primary Blue

**Data Rows:**
- Alternating fill (optional): None or very light gray (#F8F9FA)
- Text: 10pt Regular, Black
- Alignment: Top-left (wrap text enabled)

**Column Widths:**
- Distribute evenly unless specified otherwise
- Requesters table: 25% | 55% | 20%
- Solutions table: 25% | 35% | 40%

#### How to Format Tables in Word

**Step 1: Insert Table**
1. Insert tab → Table → Insert Table
2. Specify columns and rows
3. Click OK

**Step 2: Apply Header Style**
1. Select header row
2. Table Design tab → Shading → Light Gray (#E9ECEF)
3. Home tab → Font Color → Primary Blue (#2E5C8A)
4. Home tab → Bold
5. Home tab → Center alignment

**Step 3: Format Borders**
1. Select entire table
2. Table Design tab → Borders dropdown
3. Select "Borders and Shading"
4. Set all borders to 0.5pt, Dark Gray
5. Select header row
6. Set bottom border to 1pt, Primary Blue

**Step 4: Set Column Widths**
1. Hover over column border
2. Drag to adjust width
3. Or: Table Layout tab → Cell Size → specify width

**Step 5: Enable Text Wrapping**
1. Select all data cells (not headers)
2. Table Layout tab → Alignment → Align Top Left
3. Table Properties → Cell tab → Options → "Wrap text" checked

### Bullet Lists

**Standard Bullets:**
- Symbol: • (solid circle)
- Indent: 0.25" hanging
- Spacing: Single line spacing within items
- Color: Black text, same as body

**Bold Emphasis in Bullets:**
- Bold the first phrase or key term
- Rest of bullet in regular weight

**Example:**
• **Source customized NdFeB powders domestically** for supply chain security
• **Validate magnetic properties** for specific applications before production
• **Scale production with consistent quality standards** across batches

**How to Format in Word:**
1. Select list
2. Home tab → Bullets dropdown
3. Select solid circle bullet
4. Home tab → Paragraph → Increase Indent (if needed)
5. Bold key phrases using Ctrl+B

### Numbered Lists

**Use for:**
- Sequential steps
- Prioritized recommendations
- Ordered actions

**Format:**
- Style: 1., 2., 3. (period after number)
- Indent: 0.25" hanging
- Bold the number, regular text

**Example:**
**1.** Complete 20+ customer discovery interviews
**2.** Secure 3+ pilot testing agreements
**3.** Validate pricing framework

### Callout Boxes

**Use for:**
- Critical recommendations
- Important warnings
- Key takeaways
- Strategic decisions

**Format:**
- Border: 2pt, Teal Accent (#17A2B8) or Alert Red (#EF5350)
- Fill: Light tint of border color (10% opacity)
- Padding: 0.15" all sides
- Text: 11pt Regular, Black
- Optional: Icon or bold header

**How to Create in Word:**
1. Insert tab → Text Box → Draw Text Box
2. Format Shape → Fill → Light tint
3. Format Shape → Line → 2pt, colored border
4. Right-click → Format Shape → Layout & Properties → Text Box
5. Set margins: 0.15" all sides

**Example Callout:**
```
┌─────────────────────────────────────────────────┐
│ CRITICAL ACTION                                  │
│                                                  │
│ Schedule customer discovery kickoff within       │
│ 30 days. Do not proceed to pilot plant          │
│ investment without customer validation.          │
└─────────────────────────────────────────────────┘
```

### Horizontal Rules (Section Dividers)

**Use between major sections**

**Format:**
- Width: 100% of page width
- Thickness: 1pt
- Color: Light Gray (#E9ECEF)
- Space before: 12pt
- Space after: 12pt

**How to Insert:**
1. Home tab → Borders dropdown
2. "Horizontal Line"
3. Right-click line → Format Horizontal Line
4. Set color, width, height

### Emphasis and Highlighting

**Bold Text:**
- Use for: Key terms, headers within text, critical actions
- Don't overuse: Should be <10% of text

**Italic Text:**
- Use for: Notes, caveats, citations, sources
- Example: *(Heard from 12/15 manufacturers interviewed)*

**UPPERCASE:**
- Use sparingly: Section headers only (optional)
- Don't use for: Body text or emphasis

**Color Emphasis:**
- Success (Green): Validated items, positive indicators
- Warning (Orange): Medium priority, caution items
- Alert (Red): High priority, critical actions, gates

**Example:**
***CRITICAL:*** Do not proceed to pilot plant investment until customer discovery complete.

---

## DOCUMENT-SPECIFIC INSTRUCTIONS

### Part 1: Core Analysis

**Purpose:** Clean stakeholder summary

**Formatting priorities:**
- Maximum scannability
- Professional tables
- Minimal color (only headers)
- Print-friendly

**Specific instructions:**

**Title Page:**
- Title: 20pt Bold, Primary Blue
- Subtitle: 16pt Bold, Dark Gray
- "Core Analysis": 14pt Regular, Dark Gray
- Metadata block: 11pt Regular, formatted as table (no borders)

**Content Sections:**
- Section headers (H1): 16pt Bold, Primary Blue, ALL CAPS optional
- Subsection headers (H2): 14pt Bold, Teal Accent
- Use horizontal rules between major sections

**Tables:**
- Requesters: 3 columns, formatted per table specs
- Solutions: 3 columns, formatted per table specs
- Keep tables together (don't break across pages)

**Page Target:** 4-6 pages

**Special Notes:**
- No callout boxes (keep clean)
- No color in body text
- Emphasize white space and clarity

---

### Part 2: Strategic Analysis & Recommendations

**Purpose:** Internal planning and decision-making

**Formatting priorities:**
- Emphasis on actionable recommendations
- Callout boxes for critical items
- Color coding for priorities
- Clear risk indicators

**Specific instructions:**

**Title Page:**
- Title: 20pt Bold, Primary Blue
- Subtitle: 16pt Bold, Dark Gray
- "Strategic Analysis & Recommendations": 14pt Regular, Dark Gray

**Content Sections:**
- Generous use of subsections (H2, H3)
- Bold emphasis on critical terms

**Priority Recommendations:**
- Format each as callout box with colored left border
- Priority 1: Teal border (#17A2B8)
- Priority 2: Teal border (#17A2B8)
- Priority 3: Teal border (#17A2B8)
- Or use color coding if priorities differ in urgency

**Critical Actions:**
- Red callout box (#EF5350)
- Bold text
- Triple asterisks: ***ACTION REQUIRED***

**Validation Checklist:**
- Use checkbox bullets: ☐
- Or standard bullets with [ ] at start
- Format as: - [ ] Checklist item

**Conclusion Section:**
- "Path Forward" in larger header (18pt)
- Strategic Recommendation in callout box
- Bottom Line in bold

**Page Target:** 8-12 pages

**Special Notes:**
- Use color strategically for emphasis
- Callout boxes for 3 recommendations minimum
- Bold all success metrics

---

### Part 3: Customer Discovery Interview Guide

**Purpose:** Field-usable interview tool

**Formatting priorities:**
- Easy scanning during interviews
- Clear timing markers
- Question formatting for reference
- Portable/printable design

**Specific instructions:**
**Title Page:**
- Title: 20pt Bold, Primary Blue
- Subtitle: 16pt Bold, Dark Gray
- "Appendix to Vianeo Desirability Analysis": 12pt Italic, Dark Gray

**Interview Structure:**
- Phase headers: 14pt Bold, Teal Accent
- Timing in parentheses: (5 minutes)
- Italic context above questions: *Explore their current situation:*
- Questions: 11pt Regular, bullet list, hanging indent

**Question Formatting:**
```
Current State (15 minutes)

Explore their current situation and practices:

• Tell me about your use of [relevant context]
• Walk me through your current [process/approach]
• Who are your current [suppliers/partners]?
• What's working well with your current approach?
• What challenges or frustrations do you face?
```

**Best Practices Section:**
- Numbered list (1-7)
- Bold the practice title
- Regular text for explanation

**Example:**
```
1. Listen More, Talk Less
Let the interviewee speak 80% of the time. Your role is to
understand their world, not pitch your solution.
```

**Pitfalls Section:**
- Bullet list with bold headers
- Brief explanation

**Target Segments:**
- Format as simple bullet list
- Bold the segment name
- Number of interviews in parentheses

**Page Target:** 5-7 pages

**Special Notes:**
- Single-column layout (no tables)
- Generous line spacing (1.5)
- Print in easy-to-read format
- Consider including blank "Notes" sections

---

## QUICK REFERENCE

### Color Quick Codes

Copy these into your document for quick access:

**Primary Blue:** #2E5C8A (RGB: 46, 92, 138)
**Teal Accent:** #17A2B8 (RGB: 23, 162, 184)
**Dark Gray:** #6C757D (RGB: 108, 117, 125)
**Light Gray:** #E9ECEF (RGB: 233, 236, 239)

### Font Size Cheat Sheet

| Element | Size |
|---------|------|
| Document Title | 20pt |
| Section Header (H1) | 16pt |
| Subsection (H2) | 14pt |
| Sub-subsection (H3) | 12pt |
| Body Text | 11pt |
| Table Content | 10pt |
| Footer | 9pt |

### Keyboard Shortcuts

**Formatting:**
- Bold: Ctrl+B (Cmd+B on Mac)
- Italic: Ctrl+I (Cmd+I on Mac)
- Underline: Ctrl+U (Cmd+U on Mac)
- Font color: Alt+H, FC (Windows)

**Navigation:**
- Find/Replace: Ctrl+H
- Select all: Ctrl+A
- Undo: Ctrl+Z
- Redo: Ctrl+Y

**Lists:**
- Bullet list: Ctrl+Shift+L
- Numbered list: Ctrl+Alt+L (Windows)
- Increase indent: Ctrl+M
- Decrease indent: Ctrl+Shift+M

---

## COMMON MISTAKES TO AVOID

### Formatting Mistakes

**1. Inconsistent header sizes**
❌ Using random font sizes for headers
✓ Follow the hierarchy: 20pt → 16pt → 14pt → 12pt

**2. Overusing color**
❌ Rainbow text with multiple colors throughout
✓ Use brand colors for headers and strategic emphasis only

**3. Cramped spacing**
❌ Single-spacing with no paragraph breaks
✓ Use 1.15-1.5 line spacing and 6pt after paragraphs

**4. Tables breaking across pages**
❌ Header on one page, data on next
✓ Right-click table → Table Properties → Row tab → "Allow row to break across pages" (unchecked)

**5. Inconsistent table formatting**
❌ Different border styles, colors, or alignment per table
✓ Format first table, then copy formatting to others

**6. Poor font choices**
❌ Mixing multiple font families or using decorative fonts
✓ Stick to one sans-serif font throughout

**7. Ignoring page breaks**
❌ Headers orphaned at bottom of page
✓ Insert page breaks before major sections (Ctrl+Enter)

### Content Mistakes

**1. Missing page numbers**
❌ Forgetting to add footer with page numbers
✓ Insert → Page Number → Bottom of Page

**2. Generic document title**
❌ "Vianeo Desirability Analysis" (no project name)
✓ "Vianeo Desirability Analysis: [Project Name]"

**3. Incorrect date format**
❌ "11/7/25" (ambiguous)
✓ "November 7, 2025" (clear)

**4. Missing framework citation**
❌ No reference to Vianeo framework
✓ Footer includes "Vianeo Business Model Evaluation Playbook"

**5. Inconsistent terminology**
❌ "Customers" in one section, "Requesters" in another
✓ Use consistent terminology throughout (Requesters)

---

## FINAL QUALITY CHECK

Before delivering documents:

**Visual Quality:**
- [ ] All headers use correct colors (Primary Blue, Teal Accent)
- [ ] All headers use correct sizes (20pt, 16pt, 14pt, 12pt)
- [ ] Tables have borders and formatted headers
- [ ] Column widths are appropriate (text doesn't overflow)
- [ ] Generous white space between sections
- [ ] No orphaned headers (header at bottom of page, content on next)
- [ ] Page breaks used appropriately before major sections

**Consistency:**
- [ ] Same font used throughout (Calibri or Arial)
- [ ] Consistent bullet style across all lists
- [ ] Consistent table formatting across all tables
- [ ] Project name correct in all three documents
- [ ] Date consistent across all three documents

**Completeness:**
- [ ] Headers on all pages (different first page)
- [ ] Footers with page numbers on all pages
- [ ] Framework citation in footer
- [ ] All required sections present per document type

**Professionalism:**
- [ ] No spelling or grammar errors
- [ ] Professional terminology (not casual language)
- [ ] Clean, scannable layout
- [ ] Print-ready (looks good on paper, not just screen)

---

## TIPS FOR EFFICIENCY

### Creating a Template

Save time on future documents:

1. Format one document perfectly
2. Delete all content (keep headers, footers, styles)
3. Save as template (.dotx)
4. Use for all future Vianeo documents

### Using Styles

**Why use Word Styles:**
- Apply consistent formatting with one click
- Easy to update formatting across entire document
- Automatic table of contents generation

**How to create custom styles:**
1. Format text exactly how you want (e.g., Section Header)
2. Home tab → Styles pane → Create a Style
3. Name it (e.g., "Vianeo H1")
4. Save in template

**Recommended custom styles:**
- Vianeo H1 (Section Header)
- Vianeo H2 (Subsection)
- Vianeo H3 (Sub-subsection)
- Vianeo Body (Body text)
- Vianeo Table Header
- Vianeo Critical (Callout text)

### Batch Formatting

**For multiple tables:**
1. Format first table perfectly
2. Right-click table → Copy
3. Select next table → Right-click → Paste
4. Replaces content but keeps formatting
5. Or: Table Design tab → Copy formatting

**For multiple text sections:**
1. Format first section
2. Double-click Format Painter (Home tab)
3. Click each section to apply formatting
4. Press Esc when done

---

## AUTOMATION NOTES

For Zapier workflows and automated document generation:

### API-Friendly Specifications

**Color codes (hex for APIs):**
- Primary Blue: `#2E5C8A`
- Teal Accent: `#17A2B8`
- Dark Gray: `#6C757D`

**Font specifications:**
- Family: `Calibri` or `Arial`
- Sizes: `20, 16, 14, 12, 11, 10, 9` (points)
- Weights: `bold`, `regular`, `italic`

**Spacing (CSS-style):**
- Line height: `1.15` or `1.5`
- Margin after paragraph: `6pt`
- Table cell padding: `0.05in`

**Table border styles:**
- Width: `0.5pt` (data cells), `1pt` (header bottom)
- Color: `#6C757D` (Dark Gray)
- Style: `solid`

---

*This formatting guide supports the Vianeo Business Model Evaluation Playbook.*

*Companion documents:*
*- **Design Tokens: `VIANEO_Design_Tokens.md`** (single source of truth for colors, typography, code)*
*- Quick Start: `VIANEO_Desirability_Quick_Start.md`*
*- Complete Reference: `VIANEO_Desirability_Complete_Reference.md`*
*- Execution Guide: `prompts/step_5_needs_requesters.md`*

*Version: 2.1 | Updated: November 2025*
