# AI-Assisted Prompts for Vianeo Report Generation

**Purpose**: Ready-to-use prompts and commands for generating Vianeo admin reports using AI assistants (Claude, GPT-4, etc.) or command-line tools.

**Last Updated**: December 9, 2025

---

## Table of Contents

1. [Quick Start Commands](#quick-start-commands)
2. [Diagnostic Comment Prompts](#diagnostic-comment-prompts)
3. [Executive Sprint Report Prompts](#executive-sprint-report-prompts)
4. [Combined Workflow Prompts](#combined-workflow-prompts)
5. [Advanced Usage](#advanced-usage)

---

## Quick Start Commands

### Generate Diagnostic Comment (Command Line)

```bash
# From repository root
cd /home/user/master-vianeo-repository

# Generate both DOCX and Markdown
python tools/generators/generate_diagnostic.py \
  --input examples/diagnostic_sample.yaml \
  --output outputs/MyProject_Diagnostic_Comment

# Generate only DOCX
python tools/generators/generate_diagnostic.py \
  --input examples/diagnostic_sample.yaml \
  --output outputs/MyProject_Diagnostic_Comment \
  --format docx

# Generate only Markdown
python tools/generators/generate_diagnostic.py \
  --input examples/diagnostic_sample.yaml \
  --output outputs/MyProject_Diagnostic_Comment \
  --format markdown
```

### Generate Executive Sprint Report (Command Line)

```bash
# From repository root
cd /home/user/master-vianeo-repository

# Generate both DOCX and Markdown
python tools/generators/generate_executive_sprint_report.py \
  --input examples/executive_sprint_report_irdose_sample.yaml \
  --output outputs/IRDose_Sprint_Report

# Generate only DOCX
python tools/generators/generate_executive_sprint_report.py \
  --input examples/executive_sprint_report_irdose_sample.yaml \
  --output outputs/IRDose_Sprint_Report \
  --format docx

# Generate only Markdown
python tools/generators/generate_executive_sprint_report.py \
  --input examples/executive_sprint_report_irdose_sample.yaml \
  --output outputs/IRDose_Sprint_Report \
  --format markdown
```

---

## Diagnostic Comment Prompts

### Prompt 1: Generate Diagnostic Comment from Scratch

**Use Case**: You have project data and want to create a Diagnostic Comment

**AI Assistant Prompt**:
```
I need to generate a Vianeo Diagnostic Comment for my project. Here's the project information:

Project Name: [Your Project Name]
Company: [Company Name]
Brief ID: EB-2025-001
Evaluation Date: December 9, 2025

Dimension Scores:
- Legitimacy: 4.2/5.0
- Desirability: 3.8/5.0
- Acceptability: 3.5/5.0
- Feasibility: 4.0/5.0
- Viability: 3.3/5.0

Overall Vianeo Score: 3.8/5.0

Key Strengths:
- [List 3-5 strengths]

Critical Gaps:
- [List 3-5 gaps]

Please create a YAML data file following the structure in examples/diagnostic_sample.yaml, then generate the Diagnostic Comment using the generate_diagnostic.py tool.
```

### Prompt 2: Generate from Existing YAML

**Use Case**: You already have a YAML file with project data

**AI Assistant Prompt**:
```
Please generate a Vianeo Diagnostic Comment using the data in [path/to/your/file.yaml].

Use the command:
python tools/generators/generate_diagnostic.py --input [path/to/your/file.yaml] --output outputs/MyProject_Diagnostic

Generate both DOCX and Markdown formats.
```

### Prompt 3: Quick Diagnostic with Minimal Data

**Use Case**: You want a quick diagnostic with just scores and basic info

**AI Assistant Prompt**:
```
Generate a minimal Vianeo Diagnostic Comment with:

Project: QuickTest
Overall Score: 3.5/5.0
Status: Promising but needs validation

Dimensions:
- Legitimacy: 3.8 (PASS)
- Desirability: 3.2 (PASS)
- Acceptability: 3.0 (PASS)
- Feasibility: 3.6 (PASS)
- Viability: 2.9 (FAIL)

Primary concern: Viability score below threshold (3.0)

Create a minimal YAML file and generate the report.
```

---

## Executive Sprint Report Prompts

### Prompt 1: Generate Executive Sprint Report from Scratch

**Use Case**: You completed a 4-6 session sprint and want to create the comprehensive report

**AI Assistant Prompt**:
```
I need to generate a Vianeo Executive Sprint Report for a completed sprint. Here's the project information:

Project Name: [Your Project]
Sprint Duration: [Dates and session count]
Principal Investigator: [Name]
Institution: [Organization]

Overall Scores:
- Vianeo Score: 4.1/5.0
- Market Maturity: 3.1/5.0
- Status: CONDITIONAL PROCEED

Dimension Scores:
- Legitimacy (15%): 4.7 - PASS
- Desirability (25%): 4.2 - PASS
- Acceptability (20%): 4.1 - PASS
- Feasibility (20%): 4.4 - PASS
- Viability (20%): 3.7 - PASS

Business Model:
- Value Proposition: [2-3 sentences]
- Revenue Model: [Subscription/usage/hybrid]
- Target Segments: [List 3-5 key segments]

Key Findings:
[Provide 3-5 paragraphs of sprint insights]

Please create a complete YAML data file following examples/executive_sprint_report_irdose_sample.yaml, then generate the Executive Sprint Report using generate_executive_sprint_report.py.
```

### Prompt 2: Generate from Existing Sprint Data

**Use Case**: You have sprint data in YAML format

**AI Assistant Prompt**:
```
Please generate a Vianeo Executive Sprint Report using the sprint data in [path/to/sprint_data.yaml].

Use the command:
python tools/generators/generate_executive_sprint_report.py --input [path/to/sprint_data.yaml] --output outputs/MyProject_Sprint_Report

Generate both DOCX (for client delivery) and Markdown (for version control).

Ensure the output includes:
- Complete 12-15 page report
- Color-coded status indicators
- All 6 sections (Cover, Executive Summary, Business Model, Evaluation Results, Stakeholder Analysis, Recommendations, Conclusion)
- Professional formatting per FORMAT_SPEC
```

### Prompt 3: Generate Sprint Report with IRDose Template

**Use Case**: You want to use the IRDose example as a starting point

**AI Assistant Prompt**:
```
Generate an Executive Sprint Report using the IRDose sample as a template.

Steps:
1. Copy examples/executive_sprint_report_irdose_sample.yaml to a new file
2. Update the following fields with my project data:
   - project_name: [Your Project]
   - principal_investigator: [Your Name]
   - institution: [Your Org]
   - sprint_duration: [Your Dates]
   - [scores, findings, recommendations...]
3. Generate the report using:
   python tools/generators/generate_executive_sprint_report.py --input [new_file.yaml] --output outputs/[YourProject]_Sprint_Report

Please help me adapt the IRDose template to my project.
```

### Prompt 4: Post-Sprint Synthesis

**Use Case**: You have raw session notes and want AI to help structure the sprint report data

**AI Assistant Prompt**:
```
I completed a 4-session Vianeo sprint for [Project Name]. I have session notes covering all 5 dimensions (Legitimacy, Desirability, Acceptability, Feasibility, Viability).

Please help me:
1. Analyze my session notes to extract:
   - Dimension scores (1-5 scale)
   - Key strengths for each dimension (3-5 bullets)
   - Critical gaps for each dimension (3-5 bullets)
   - Stakeholder personas (4 priority personas)
   - Recommendations (immediate, short-term, medium-term)

2. Structure this into a YAML file following examples/executive_sprint_report_irdose_sample.yaml

3. Generate the Executive Sprint Report

Here are my session notes:
[Paste session notes or attach files]
```

---

## Combined Workflow Prompts

### Workflow 1: End-to-End Sprint Process

**Use Case**: Complete sprint workflow from initial brief to final report

**AI Assistant Prompt**:
```
I'm conducting a complete Vianeo evaluation sprint. Please help me through this workflow:

**Phase 1: Initial Assessment** (Session 1)
- Generate Executive Brief
- Establish baseline scores

**Phase 2: Deep Dive** (Sessions 2-4)
- Validate scores across 5 dimensions
- Conduct stakeholder interviews
- Identify strengths and gaps

**Phase 3: Synthesis** (Session 4-5)
- Generate Diagnostic Comment with:
  python tools/generators/generate_diagnostic.py --input [sprint_data.yaml] --output outputs/[Project]_Diagnostic

**Phase 4: Final Report** (Post-sprint)
- Generate Executive Sprint Report with:
  python tools/generators/generate_executive_sprint_report.py --input [sprint_data.yaml] --output outputs/[Project]_Sprint_Report

Project: [Your Project Name]
Current Phase: [1/2/3/4]

Please guide me through the current phase and prepare the necessary files.
```

### Workflow 2: Generate Both Reports Sequentially

**Use Case**: You want both Diagnostic Comment and Sprint Report from the same data

**AI Assistant Prompt**:
```
Generate both the Diagnostic Comment and Executive Sprint Report for [Project Name] using the same source data.

Data file: [path/to/project_data.yaml]

Commands to run:
1. Diagnostic Comment:
   python tools/generators/generate_diagnostic.py --input [data.yaml] --output outputs/[Project]_Diagnostic

2. Executive Sprint Report:
   python tools/generators/generate_executive_sprint_report.py --input [data.yaml] --output outputs/[Project]_Sprint_Report

Expected outputs:
- [Project]_Diagnostic.docx
- [Project]_Diagnostic.md
- [Project]_Vianeo_Sprint_Executive_Report_[Date].docx
- [Project]_Vianeo_Sprint_Executive_Report_[Date].md

Please execute both generators and verify all outputs are created.
```

### Workflow 3: Update Existing Report

**Use Case**: You need to regenerate a report with updated data

**AI Assistant Prompt**:
```
I need to update an existing Vianeo report with new data.

Original report: outputs/[Project]_Sprint_Report_20251208.docx
Updated data: [List what changed - scores, recommendations, etc.]

Steps:
1. Read the original YAML data file
2. Update the following fields: [list fields]
3. Regenerate the report with new date stamp
4. Compare old vs new outputs

Please help me update the data file and regenerate the report.
```

---

## Advanced Usage

### Batch Generation

**Prompt**:
```
I have multiple projects that need reports generated. Please process them in batch:

Projects:
1. Project A - diagnostic_project_a.yaml
2. Project B - diagnostic_project_b.yaml
3. Project C - sprint_report_project_c.yaml

For each project:
- Generate both DOCX and Markdown
- Save to outputs/ with project name prefix
- Log any errors or warnings

Batch process all three projects.
```

### Custom Output Locations

**Prompt**:
```
Generate reports with custom output locations:

Diagnostic Comment:
- Input: data/client_projects/acme/diagnostic_data.yaml
- Output: deliverables/acme/2025Q4/ACME_Diagnostic_Comment
- Formats: DOCX only (client delivery)

Executive Sprint Report:
- Input: data/client_projects/acme/sprint_data.yaml
- Output: deliverables/acme/2025Q4/ACME_Sprint_Report
- Formats: Both DOCX and Markdown

Use custom output paths and ensure directories exist.
```

### Quality Validation

**Prompt**:
```
Generate the Executive Sprint Report and validate against the quality checklist:

1. Generate report:
   python tools/generators/generate_executive_sprint_report.py --input [data.yaml] --output outputs/[Project]_Sprint_Report

2. Validate against docs/VIANEO_ExecutiveSprintReport_Quality_Checklist.md:
   - Content completeness (80+ items)
   - Formatting accuracy
   - Data consistency
   - Professional presentation

3. Report any validation failures

Please generate and validate the report.
```

### Integration with Version Control

**Prompt**:
```
Generate reports and commit to git:

1. Generate both reports:
   - Diagnostic Comment (Markdown only for version control)
   - Executive Sprint Report (both formats)

2. Add files to git:
   git add outputs/[Project]_Diagnostic.md
   git add outputs/[Project]_Sprint_Report.md
   git add outputs/[Project]_Sprint_Report.docx

3. Commit with message:
   git commit -m "Add Vianeo reports for [Project] - Sprint completed [Date]"

4. Push to branch: vianeo-reports/[project-name]

Please execute this workflow and confirm successful push.
```

---

## Sample Conversation Starters

### For Diagnostic Comment:

1. **"Generate a Vianeo Diagnostic Comment for my project [Name] with overall score 3.8/5.0"**
2. **"I have diagnostic data in YAML format at [path]. Please generate the Diagnostic Comment."**
3. **"Help me create a diagnostic report showing that Viability (2.9) is the primary concern."**
4. **"Generate a minimal diagnostic with just scores and status - I'll add details later."**

### For Executive Sprint Report:

1. **"Generate a comprehensive Executive Sprint Report for our completed 4-session sprint."**
2. **"Use the IRDose example as a template and adapt it for my project [Name]."**
3. **"I have raw session notes from our sprint. Help me structure them into a Sprint Report."**
4. **"Generate the Executive Sprint Report from [yaml_file] and validate against the quality checklist."**

### For Combined Workflows:

1. **"Generate both Diagnostic Comment and Executive Sprint Report for [Project]."**
2. **"Walk me through the complete Vianeo sprint workflow from initial brief to final report."**
3. **"Update my existing Sprint Report with new scores and regenerate all outputs."**
4. **"Batch generate reports for 5 projects and commit all outputs to git."**

---

## Tips for Effective AI-Assisted Generation

### 1. Provide Context
Always include:
- Project name and domain
- Sprint duration and session count
- Key stakeholders
- Primary objectives

### 2. Specify Output Requirements
Clearly state:
- Desired formats (DOCX, Markdown, or both)
- Output location
- Any custom naming conventions

### 3. Include Data Quality Indicators
Mention:
- Evidence quality level (Gold Standard, Strong, Moderate, Weak)
- Validation status (validated vs. hypothesized)
- Data sources (customer interviews, market research, etc.)

### 4. Request Validation
Ask AI to:
- Check character limits
- Validate score thresholds
- Verify formatting compliance
- Compare against quality checklist

### 5. Iterate Incrementally
For complex reports:
- Start with minimal data
- Generate initial output
- Review and refine
- Add details iteratively

---

## Troubleshooting

### Issue: "File not found" error
**Prompt**: "The generator can't find my input file. Please check the path and create the directory structure if needed."

### Issue: Missing dependencies
**Prompt**: "I'm getting a python-docx import error. Please verify dependencies are installed: pip install python-docx pyyaml"

### Issue: Formatting doesn't match specification
**Prompt**: "The generated DOCX doesn't match the FORMAT_SPEC. Please validate against docs/FORMAT_SPEC_Executive_Sprint_Report.md and regenerate."

### Issue: Character limit violations
**Prompt**: "Some fields exceed character limits. Please validate against tools/core/constants.py and truncate or revise as needed."

---

## Quick Reference Card

```
╔════════════════════════════════════════════════════════════════╗
║               VIANEO REPORT GENERATION - QUICK REFERENCE        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  DIAGNOSTIC COMMENT                                            ║
║  ─────────────────────────────────────────────────────────────  ║
║  Command:                                                       ║
║    python tools/generators/generate_diagnostic.py \            ║
║      --input [data.yaml] --output [path]                       ║
║                                                                 ║
║  Sample Data: examples/diagnostic_sample.yaml                  ║
║  Output: 3-4 page summary with scores and recommendations     ║
║                                                                 ║
╠════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  EXECUTIVE SPRINT REPORT                                       ║
║  ─────────────────────────────────────────────────────────────  ║
║  Command:                                                       ║
║    python tools/generators/generate_executive_sprint_report.py\║
║      --input [data.yaml] --output [path]                       ║
║                                                                 ║
║  Sample Data: examples/executive_sprint_report_irdose_sample.yaml║
║  Output: 12-15 page comprehensive report                       ║
║                                                                 ║
╠════════════════════════════════════════════════════════════════╣
║                                                                 ║
║  FORMAT OPTIONS                                                ║
║  ─────────────────────────────────────────────────────────────  ║
║  --format docx      → DOCX only (client delivery)              ║
║  --format markdown  → Markdown only (version control)          ║
║  (no flag)          → Both formats (default)                   ║
║                                                                 ║
╚════════════════════════════════════════════════════════════════╝
```

---

**Document Version**: 1.0
**Maintained By**: 360 Social Impact Studios
**Last Updated**: December 9, 2025
**Questions?**: Contact contact@360socialimpact.com
