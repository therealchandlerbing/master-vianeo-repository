/**
 * ============================================================================
 * VIANEO Executive Sprint Report - JavaScript Specification (Reference)
 * ============================================================================
 *
 * PURPOSE: This file serves as the AUTHORITATIVE SPECIFICATION for the
 * Executive Sprint Report implementation. It is preserved here for:
 *
 * 1. REFERENCE: Detailed specification of document structure, formatting,
 *    and business logic
 * 2. VALIDATION: Ensuring Python implementation maintains visual fidelity
 * 3. FUTURE UPDATES: Template for modifications and enhancements
 * 4. DOCUMENTATION: Clear example of expected output structure
 *
 * STATUS: This is NOT executable code in the Vianeo framework.
 *         The actual implementation is in Python (generate_executive_sprint_report.py)
 *         using the python-docx library for architectural consistency.
 *
 * USAGE: When updating the Executive Sprint Report:
 *        1. Modify this specification first to reflect desired changes
 *        2. Update Python implementation to match
 *        3. Validate outputs match specification
 *
 * MAINTAINED BY: 360 Social Impact Studios
 * LAST UPDATED: December 8, 2025
 * VERSION: 1.0
 * ============================================================================
 */

/**
 * Vianeo Executive Sprint Report DOCX Generator
 *
 * Usage: Update the projectData object with your project's information,
 * then run: node generate_executive_sprint_report.js
 *
 * Output: [ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].docx
 */

const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, PageOrientation, LevelFormat,
  HeadingLevel, BorderStyle, WidthType, ShadingType, VerticalAlign,
  PageBreak, PageNumber
} = require('docx');

// ============================================================================
// PROJECT DATA - UPDATE THIS SECTION FOR EACH PROJECT
// ============================================================================

const projectData = {
  // Metadata
  projectName: "IRDose",
  reportTitle: "IRDose Vianeo Validation",
  reportSubtitle: "Executive Sprint Report",
  projectTagline: "Personalized Radioiodine Dosimetry System",
  subtitle: "Business Model Evaluation & Market Readiness Assessment",
  principalInvestigator: "Daniel Alexandre Baptista Bonifacio",
  institution: "IPEN/CNEN (Instituto de Pesquisas Energéticas e Nucleares)",
  sprintDuration: "October 29 – December 8, 2025 (4 sessions)",
  evaluationFramework: "Vianeo Business Model Evaluation System",
  preparedBy: "360 Social Impact Studios",
  reportDate: "December 8, 2025",
  author: "Chandler Lewis",
  authorTitle: "Managing Director",

  // Scores
  overallVianeoScore: "4.1 / 5.0",
  marketMaturityScore: "3.1 / 5.0",
  status: "CONDITIONAL PROCEED",

  dimensions: [
    { name: "Legitimacy", weight: "15%", score: "4.7", status: "PASS", interpretation: "Validated problem, strong institutional backing" },
    { name: "Desirability", weight: "25%", score: "4.2", status: "PASS", interpretation: "Clear clinical need identified" },
    { name: "Acceptability", weight: "20%", score: "4.1", status: "PASS", interpretation: "Regulatory pathway clear" },
    { name: "Feasibility", weight: "20%", score: "4.4", status: "PASS", interpretation: "Functional prototype, costs defined" },
    { name: "Viability", weight: "20%", score: "3.7", status: "PASS", interpretation: "Business model defined but unvalidated" }
  ],

  // Section 1: Executive Summary
  projectOverview: [
    "The IRDose project represents a technically sophisticated venture developing a personalized radioiodine dosimetry system for hyperthyroidism treatment. Over four validation sessions spanning October through December 2025, 360 Social Impact Studios conducted a comprehensive Vianeo business model evaluation covering all five critical dimensions: Legitimacy, Desirability, Acceptability, Feasibility, and Viability.",
    "The project demonstrates exceptional technical legitimacy with a validated clinical problem (20-29% treatment failure rates in current fixed-dose I-131 therapy), a functional TRL 4-5 laboratory prototype featuring GAGG+SiPM crystal spectrometry achieving 7-12% energy resolution, and a world-class team of 13+ doctorate-level researchers at IPEN/CNEN. Secured FAPESP PIPE funding of R$600,000, established partnerships at HC/FMUSP for clinical validation, and operational IRDose cloud platform with INPI intellectual property registration provide strong institutional backing.",
    "However, the market maturity score of 3.1/5.0 falls below the 3.2 threshold for commercial readiness, driven primarily by critical gaps in customer validation and business model development rather than technical limitations. The project's path to commercial success requires immediate execution of a comprehensive customer discovery sprint before advancing to Series A fundraising."
  ],

  primaryRecommendation: {
    statusText: "CONDITIONAL PROCEED with mandatory customer discovery sprint",
    summary: "The IRDose project demonstrates sufficient technical legitimacy and platform readiness to warrant continued development. However, advancement to Series A fundraising or scaled clinical deployment requires immediate execution of a comprehensive customer discovery sprint to validate fundamental business model assumptions.",
    validationGaps: [
      "Zero customer discovery interviews conducted despite clear technical capabilities",
      "Pricing assumptions ($400-800/month) untested against SUS budget constraints",
      "Patient wearability acceptance and physician trust in IoT sensor data unvalidated",
      "Gaugit manufacturing partnership remains informal",
      "100% grant-dependent funding structure with no commercial team members"
    ],
    immediateNextSteps: [
      "Execute 40-60 structured customer discovery interviews across all stakeholder segments",
      "Recruit commercial co-founder or advisor with Brazilian medtech market experience",
      "Formalize Gaugit manufacturing partnership with capacity commitments and pricing tiers",
      "Restructure financial model to validate SUS reimbursement pathways and pricing acceptance",
      "Initiate HC/FMUSP pilot study with 10-patient clinical validation"
    ]
  },

  // Section 2: Business Model Overview
  valueProposition: "IRDose delivers personalized radioiodine dosimetry for hyperthyroidism treatment through a wearable gamma spectrometer combined with cloud-based Monte Carlo dosimetry platform. The system replaces current fixed-dose protocols that cause 20-29% treatment failure rates and excessive patient exposure to hospital visits.",

  coreDifferentiation: [
    "Real-time, continuous dosimetry monitoring versus periodic hospital visits",
    "Patient-specific biokinetics modeling reduces treatment failure rates",
    "Cloud-based platform enables remote monitoring and physician access",
    "Wearable form factor improves patient comfort and workflow integration",
    "Monte Carlo variance reduction algorithms enable 10-minute dosimetry calculations"
  ],

  targetSegments: [
    { segment: "Nuclear Medicine Physicians", characteristics: "Primary clinical decision-makers, frustrated with fixed-dose limitations" },
    { segment: "Medical Physicists", characteristics: "Technical gatekeepers, require dosimetry accuracy validation" },
    { segment: "Hyperthyroidism Patients", characteristics: "End-users, value reduced hospital visits and improved outcomes" },
    { segment: "Hospital Administrators", characteristics: "Budget decision-makers, focus on cost-effectiveness and SUS alignment" },
    { segment: "Public Hospitals (SUS)", characteristics: "Large addressable market (2,370 annual treatments), accessibility focus" },
    { segment: "Private Clinics", characteristics: "Premium segment, early adopter potential if efficacy proven" },
    { segment: "Research Institutions", characteristics: "Academic validation partners, evidence generation" },
    { segment: "Regulatory Bodies", characteristics: "ANVISA, CNEN approval required for market entry" }
  ],

  revenueModel: {
    type: "Proposed hybrid model (unvalidated)",
    components: [
      "Platform subscription: $400-800/month per facility (60% of revenue)",
      "Per-procedure fee: $15-25 per dosimetry analysis (25% of revenue)",
      "Hardware sales/lease: Device units at cost plus margin (15% of revenue)"
    ],
    pricingWarning: "All pricing assumptions remain untested hypotheses. Zero customer interviews conducted to validate willingness-to-pay against SUS budget constraints. Hardware COGS ranges from $513-1,499 per unit depending on volume, requiring urgent reconciliation with proposed pricing structure."
  },

  // Section 3: Dimension Details (continued in next sections due to length)
  // ... [remaining JavaScript code continues with all dimension details, stakeholder analysis, etc.]

  // Note: Full JavaScript implementation available - this is a reference specification
};

// ============================================================================
// STYLING CONSTANTS
// ============================================================================

const colors = {
  primaryBlue: "1E3A5F",
  secondaryBlue: "2E5A7F",
  lightBlue: "E8F4F8",
  successGreen: "28A745",
  warningYellow: "FFC107",
  dangerRed: "DC3545",
  gray: "6C757D",
  lightGray: "F8F9FA",
  white: "FFFFFF",
  black: "000000"
};

const tableBorder = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const cellBorders = { top: tableBorder, bottom: tableBorder, left: tableBorder, right: tableBorder };

// ============================================================================
// DOCUMENT STRUCTURE SPECIFICATION
// ============================================================================

/**
 * EXECUTIVE SPRINT REPORT DOCUMENT STRUCTURE
 *
 * Page Count: 12-15 pages
 * Orientation: Portrait
 * Margins: 1 inch all sides (1440 DXA)
 * Font: Arial (universal compatibility)
 *
 * SECTIONS:
 *
 * 1. Cover Page (Page 1)
 *    - Title block (2 lines, 28pt + 22pt, centered, primary blue)
 *    - Tagline (14pt, italic, gray)
 *    - Assessment type (12pt, secondary blue)
 *    - Metadata table (6 rows × 2 columns)
 *
 * 2. Executive Summary (Pages 2-3)
 *    - Score Dashboard (3-column table)
 *    - Project Overview (3 paragraphs)
 *    - Key Findings (5-row table with color-coded status)
 *    - Primary Recommendation (status + gaps + next steps)
 *
 * 3. Business Model Overview (Pages 4-5)
 *    - Value Proposition
 *    - Core Differentiation (bullet list)
 *    - Target Segments (8-row table)
 *    - Revenue Model (with pricing warning callout)
 *
 * 4. Evaluation Results (Pages 6-10)
 *    - Introduction paragraph
 *    - 5 dimension sections (each on new page):
 *      * Legitimacy (15% weight)
 *      * Desirability (25% weight)
 *      * Acceptability (20% weight)
 *      * Feasibility (20% weight)
 *      * Viability (20% weight)
 *    - Each dimension has:
 *      * Score header with status indicator
 *      * Summary paragraph
 *      * Strengths (3-7 bullets)
 *      * Gaps (3-5 bullets)
 *
 * 5. Stakeholder Analysis (Pages 11-12)
 *    - Priority Personas (4 detailed profiles)
 *    - Ecosystem Relationships (5-row table)
 *
 * 6. Recommendations (Pages 13-14)
 *    - Immediate Priorities (0-30 days, 3 actions)
 *    - Short-Term Validation (30-90 days, 3 actions)
 *    - Medium-Term Priorities (90-180 days, 3 actions, condensed)
 *    - Risk Mitigation (6-row table)
 *
 * 7. Conclusion (Page 15)
 *    - Summary (4 paragraphs)
 *    - Next Review Checkpoint
 *    - Footer with attribution
 *
 * PAGE BREAKS:
 * - After Cover Page
 * - Before Section 2 (Business Model)
 * - Before Section 3 (Evaluation Results)
 * - Before each dimension (3.1, 3.2, 3.3, 3.4, 3.5)
 * - Before Section 4 (Stakeholder Analysis)
 * - Before Section 5 (Recommendations)
 * - Before Medium-Term Priorities subsection
 * - Before Section 6 (Conclusion)
 *
 * TYPOGRAPHY:
 * - Title: 28pt, bold, primary blue (#1E3A5F)
 * - Heading 1: 16pt, bold, deep blue
 * - Heading 2: 14pt, bold, dark gray
 * - Heading 3: 12pt, bold, black
 * - Body: 11pt, regular, black
 * - Metadata: 9pt, light gray
 *
 * TABLES:
 * - Header: Deep blue (#1E3A5F) background, white text, bold 11pt
 * - Alternating rows: White and light blue (#E8F4F8)
 * - Borders: Light gray (#CCCCCC), 1pt
 * - Cell padding: 100 DXA top/bottom, 180 DXA left/right
 *
 * STATUS COLORS:
 * - PASS: Green (#28A745)
 * - FAIL: Red (#DC3545)
 * - CONDITIONAL: Yellow (#FFC107)
 * - Critical: Red
 * - High: Yellow
 * - Medium: Green
 * - Low: Gray
 *
 * VALIDATION REQUIREMENTS:
 * - All score tables must use color-coded cells
 * - All bullet lists use proper Word formatting (not unicode)
 * - No em dashes anywhere in document
 * - Page breaks occur at specified boundaries
 * - Headers/footers consistent throughout
 * - Document opens correctly in Microsoft Word
 */

// ============================================================================
// PYTHON IMPLEMENTATION MAPPING
// ============================================================================

/**
 * TRANSLATION GUIDE: JavaScript → Python (python-docx)
 *
 * Document Setup:
 * JS: new Document()
 * PY: Document()
 *
 * Paragraphs:
 * JS: new Paragraph({ children: [new TextRun({ text: "...", bold: true })] })
 * PY: para = doc.add_paragraph()
 *     run = para.add_run("...")
 *     run.bold = True
 *
 * Headings:
 * JS: new Paragraph({ heading: HeadingLevel.HEADING_1 })
 * PY: doc.add_heading("...", level=1)
 *
 * Tables:
 * JS: new Table({ rows: [...] })
 * PY: table = doc.add_table(rows=X, cols=Y)
 *
 * Column Widths:
 * JS: width: { size: 3500, type: WidthType.DXA }
 * PY: table.columns[i].width = Inches(2.4)  # 3500 DXA ≈ 2.4 inches
 *
 * Cell Shading:
 * JS: shading: { fill: "E8F4F8", type: ShadingType.CLEAR }
 * PY: shading = OxmlElement('w:shd')
 *     shading.set(qn('w:fill'), "E8F4F8")
 *     cell._tc.get_or_add_tcPr().append(shading)
 *
 * Text Color:
 * JS: color: "1E3A5F"
 * PY: run.font.color.rgb = RGBColor.from_string("1E3A5F")
 *
 * Page Breaks:
 * JS: new PageBreak()
 * PY: doc.add_page_break()
 *
 * Alignment:
 * JS: alignment: AlignmentType.CENTER
 * PY: para.alignment = WD_ALIGN_PARAGRAPH.CENTER
 *
 * Font Size:
 * JS: size: 28 (half-points)
 * PY: run.font.size = Pt(14)  # 28 half-points = 14 points
 *
 * Note: DXA (twentieths of a point) conversions:
 * - 1440 DXA = 1 inch
 * - 720 DXA = 0.5 inch
 * - To convert: inches = DXA / 1440
 */

// ============================================================================
// END OF SPECIFICATION
// ============================================================================

/**
 * IMPLEMENTATION NOTES:
 *
 * 1. The Python implementation (generate_executive_sprint_report.py) follows
 *    this specification exactly but uses python-docx library instead of docx-js.
 *
 * 2. All visual elements (colors, fonts, spacing) are preserved in Python using
 *    equivalent python-docx APIs.
 *
 * 3. Table structures use the same column widths converted from DXA to Inches.
 *
 * 4. Business logic (status colors, score thresholds) is implemented in Python
 *    using the same conditional logic.
 *
 * 5. For any discrepancies between outputs, THIS SPECIFICATION is authoritative.
 *    Update the Python implementation to match this document.
 *
 * MAINTAINERS: When updating the Executive Sprint Report:
 * 1. Update this specification first
 * 2. Modify Python implementation to match
 * 3. Test with sample data
 * 4. Validate output matches specification
 * 5. Update version number and date
 */
