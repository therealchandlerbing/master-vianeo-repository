# Vianeo Executive Sprint Report Generation Prompt

**Version:** 1.0
**Purpose:** Guide AI assistants in generating Executive Sprint Reports
**Framework:** Vianeo Business Model Evaluation System
**Output:** DOCX + Markdown (12-15 pages)

---

## Overview

Generate a professional Executive Sprint Report that synthesizes findings from a complete Vianeo Business Model Evaluation Sprint (4-6 sessions) covering all five proof-of-value dimensions.

**This report is committee-ready, investor-ready, and serves as the primary deliverable for sprint stakeholders.**

---

## Required Inputs

Before generating, collect the following data from the Vianeo platform and sprint documentation:

### 1. Project Metadata
- Project name and tagline (max 100 characters)
- Principal investigator name
- Institution/organization
- Sprint duration (dates and number of sessions)
- Report date
- Author information

### 2. Scoring Data
- Overall Vianeo score (X.X / 5.0)
- Market maturity score (X.X / 5.0)
- Overall status (GO / CONDITIONAL PROCEED / NO-GO)
- **For each dimension:**
  - Name (Legitimacy, Desirability, Acceptability, Feasibility, Viability)
  - Weight percentage
  - Score (X.X/5.0)
  - Status (PASS/FAIL)
  - Threshold value
  - One-sentence interpretation

### 3. Business Model Data
- Value proposition (2-3 sentences)
- Core differentiation points (4-6 bullets)
- Target market segments (6-10 segments with characteristics)
- Revenue model type and components
- Pricing assumptions (validated or unvalidated)

### 4. Evidence and Findings
**For each of the 5 dimensions, gather:**
- Summary paragraph (1-2 sentences)
- Key strengths (5-6 specific items with evidence/metrics)
- Key gaps (4 specific deficiencies with implications)
- Validation status (interviews conducted, evidence sources)

### 5. Stakeholder Data
- Priority personas (3-4 detailed profiles with needs and validation requirements)
- Critical ecosystem relationships (5-8 relationships with type, criticality, status)

### 6. Recommendations
- Immediate priorities (3 actions for 0-30 days with owners, timelines, items)
- Short-term validation (3 actions for 30-90 days)
- Medium-term priorities (3 actions for 90-180 days, condensed format)
- Risk mitigation strategies (5-7 risks with impact and mitigation)

### 7. Conclusion & Next Steps
- Conclusion paragraphs (4 paragraphs: strengths, gaps, path forward, final recommendation)
- Next review timing and deliverables
- Success criteria for next stage

---

## Generation Instructions

### Phase 1: Data Collection
1. Use `project_knowledge_search` or equivalent to gather all sprint data
2. Query for each dimension's scores, strengths, and gaps
3. Collect business model canvas data
4. Gather stakeholder and persona information
5. Pull recommendations from sprint documentation

### Phase 2: Document Generation
1. Load the YAML/JSON data file with all required inputs
2. Run the Python generator:
   ```bash
   python tools/generators/generate_executive_sprint_report.py \
     --input [data_file].yaml \
     --output [ProjectName]_Sprint_Report \
     --format both
   ```
3. The generator will create both DOCX and Markdown versions
4. Validate output against format specification

### Phase 3: Quality Validation
Before delivering, verify:
- [ ] All 6 sections present with correct structure
- [ ] All tables properly formatted with correct column widths
- [ ] Score colors match status (green PASS, red FAIL)
- [ ] No placeholder text ([Insert X]) remains
- [ ] All bullet points use proper Word formatting (not unicode •)
- [ ] Page breaks occur at section boundaries (11 total)
- [ ] Headers and footers consistent throughout
- [ ] Document opens correctly in Microsoft Word

---

## Document Structure

### Cover Page (Page 1)
- **Title Block:** Two-line title with project name and "Executive Sprint Report"
- **Tagline:** One-line project description
- **Metadata Table:** 6 rows (PI, Institution, Duration, Framework, Prepared By, Date)

### Section 1: Executive Summary (Pages 2-3)
- **1.1 Score Dashboard:** 3-column table (Overall, Market Maturity, Status)
- **1.2 Project Overview:** 3 paragraphs (scope, strengths, readiness)
- **1.3 Key Findings:** 5-row table (one per dimension with scores and status)
- **1.4 Primary Recommendation:** Status + summary + gaps + next steps

### Section 2: Business Model Overview (Pages 4-5)
- **2.1 Value Proposition:** Summary + core differentiation bullets
- **2.2 Target Segments:** Table with 6-10 segments
- **2.3 Revenue Model:** Model type + components + pricing warning (if applicable)

### Section 3: Evaluation Results (Pages 6-10)
- **Introduction:** Brief overview of five dimensions
- **3.1 Legitimacy (15%):** Score, status, summary, strengths, gaps
- **3.2 Desirability (25%):** Score, status, summary, strengths, gaps
- **3.3 Acceptability (20%):** Score, status, summary, strengths, gaps
- **3.4 Feasibility (20%):** Score, status, summary, strengths, gaps
- **3.5 Viability (20%):** Score, status, summary, strengths, gaps

**Each dimension gets its own page for committee review.**

### Section 4: Stakeholder Analysis (Pages 11-12)
- **4.1 Priority Personas:** 3-4 detailed persona profiles
- **4.2 Ecosystem Relationships:** Table with critical partnerships

### Section 5: Recommendations (Pages 13-14)
- **5.1 Immediate Priorities (0-30 days):** 3 detailed actions
- **5.2 Short-Term Validation (30-90 days):** 3 detailed actions
- **5.3 Medium-Term Priorities (90-180 days):** 3 condensed actions
- **5.4 Risk Mitigation:** Table with 5-7 risks

### Section 6: Conclusion (Page 15)
- **Summary:** 4 paragraphs (strengths → gaps → path → recommendation)
- **6.1 Next Review Checkpoint:** Timing, deliverables, success criteria
- **Footer:** Attribution and date

---

## Writing Quality Standards

### Tone & Style

**Professional but not academic:**
- ✅ "Zero customer interviews conducted"
- ❌ "It is observed that customer validation activities have not yet been initiated"

**Evidence-based, not opinion:**
- ✅ "20-29% treatment failure rates documented in peer-reviewed literature"
- ❌ "We believe the market need is strong"

**Action-oriented, not passive:**
- ✅ "Execute 40-60 customer interviews within 60 days"
- ❌ "Customer interviews should be considered"

**Specific, not vague:**
- ✅ "R$600,000 FAPESP PIPE funding secured"
- ❌ "Significant funding obtained"

### Balance Requirement

Every dimension assessment should include BOTH strengths AND gaps:
- ✅ "Exceptional technical legitimacy with 13+ researchers, but entirely academic structure with zero commercial team members"
- ❌ Listing only strengths or only weaknesses

### Score Interpretation

| Overall Vianeo Score | Status | Typical Recommendation |
|---------------------|--------|------------------------|
| 4.5-5.0 | GO | Exceptional readiness for commercialization |
| 4.0-4.4 | GO | Strong readiness with minor conditions |
| 3.5-3.9 | CONDITIONAL PROCEED | Validation required before scaling |
| 3.0-3.4 | CONDITIONAL PROCEED | Significant work needed |
| Below 3.0 | NO-GO | Fundamental issues require addressing |

### Market Maturity Threshold

- **3.2+:** Commercial readiness achieved
- **Below 3.2:** Additional validation required before market entry

### Dimension Thresholds

| Dimension | Minimum Threshold | Reason for Threshold |
|-----------|-------------------|---------------------|
| Legitimacy | 3.0 | Problem must be real, team capable |
| Desirability | 3.5 | **Higher bar** - most important dimension |
| Acceptability | 3.0 | Key stakeholders must support |
| Feasibility | 3.0 | Team must be able to build |
| Viability | 3.0 | Business model must be sustainable |

---

## Common Mistakes to Avoid

### Content Mistakes

❌ **Using aspirational language for unvalidated assumptions**
✅ **Clearly labeling hypotheses as "(unvalidated)" or "(hypothesized)"**

❌ **Generic, vague strengths ("strong team")**
✅ **Specific, evidence-backed strengths ("13+ doctorate-level researchers with detector physics expertise")**

❌ **Missing interview counts**
✅ **Explicit validation status ("Zero customer discovery interviews conducted" or "20 physician interviews completed")**

❌ **Weak recommendations ("consider exploring")**
✅ **Directive recommendations with owners and timelines ("Execute 40-60 interviews within 60 days - Owner: Daniel Bonifacio")**

### Formatting Mistakes

❌ **Using em dashes (—) anywhere in the document**
✅ **Using commas, periods, or parentheses instead**

❌ **Unicode bullet points (•, -, *)**
✅ **Proper Word numbering configuration with built-in bullet formatting**

❌ **Missing table column widths**
✅ **Specified widths that sum to 6.5 inches**

❌ **Inconsistent color coding**
✅ **Systematic color application matching status indicators (green=PASS, red=FAIL)**

---

## Output Files

The generator produces two files:

### 1. DOCX (Primary)
**Filename:** `[ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].docx`

**Purpose:** Professional, print-ready format for:
- Committee presentations
- Investor pitches
- Board reviews
- Stakeholder handoffs

**Features:**
- Full formatting (colors, fonts, tables)
- Page breaks at section boundaries
- Headers and footers with page numbers
- Professional appearance in Microsoft Word, Google Docs, LibreOffice

### 2. Markdown (Secondary)
**Filename:** `[ProjectName]_Vianeo_Sprint_Executive_Report_[YYYYMMDD].md`

**Purpose:** Version-controllable format for:
- Git tracking
- Collaborative editing
- Web publishing
- Plain-text review

**Features:**
- Identical content to DOCX
- GitHub-flavored Markdown
- Tables rendered with pipes (|)
- Links and references preserved

---

## Integration with Vianeo Framework

This report synthesizes outputs from:
- **Step 0:** Executive Brief (project metadata)
- **Step 3:** Market Maturity 29Q Assessment (market maturity score)
- **Step 4:** Legitimacy Deep Dive (legitimacy dimension)
- **Step 5:** Needs/Requesters Analysis (desirability dimension)
- **Step 6:** Persona Development (personas and needs)
- **Step 7:** Needs Qualification Matrix (needs validation status)
- **Step 8:** Ecosystem Mapping (acceptability dimension)
- **Step 9:** Value Network Analysis (ecosystem relationships)
- **Step 10:** Diagnostic Comment (overall assessment synthesis)
- **Step 11:** Features-Needs Analysis (feasibility dimension)
- **Step 12:** Viability Dashboard (viability dimension, revenue model)

**The Executive Sprint Report is the culminating deliverable presenting all findings in a committee-ready format.**

---

## Example Data Structure (YAML)

See `examples/executive_sprint_report_irdose_sample.yaml` for a complete, real-world example.

**Key sections:**
```yaml
project_name: "IRDose"
overall_vianeo_score: "4.1 / 5.0"
market_maturity_score: "3.1 / 5.0"
status: "CONDITIONAL PROCEED"

key_findings:
  - dimension: "Legitimacy"
    weight: "15%"
    score: "4.7"
    status: "PASS"
    interpretation: "Validated problem, strong institutional backing"
  # ... 4 more dimensions

legitimacy:
  name: "Legitimacy"
  weight: "15%"
  score: "4.7/5.0"
  threshold: "3.0"
  status: "PASS"
  summary: "IRDose demonstrates exceptional technical legitimacy..."
  strengths:
    - "Clinical problem validated: 20-29% treatment failure rates..."
    - "13+ doctorate-level researchers with detector physics expertise..."
    # ... 5-6 total strengths
  gaps:
    - "Zero commercial team members despite exceptional technical depth..."
    # ... 3-4 total gaps

# ... repeat for all 5 dimensions
# ... personas, ecosystem relationships, priorities, etc.
```

---

## Support & Resources

### Documentation
- **Format Specification:** `docs/FORMAT_SPEC_Executive_Sprint_Report.md`
- **Quality Checklist:** `docs/VIANEO_ExecutiveSprintReport_Quality_Checklist.md`
- **JavaScript Reference:** `docs/reference/executive_sprint_report_specification.js`

### Examples
- **IRDose Sample Data:** `examples/executive_sprint_report_irdose_sample.yaml`

### Code
- **Python Generator:** `tools/generators/generate_executive_sprint_report.py`
- **Data Models:** See `ExecutiveSprintReportData` dataclass in generator file

### Contact
**360 Social Impact Studios**
For questions or support with Executive Sprint Report generation.

---

**End of Prompt**
