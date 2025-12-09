# AI-Assisted Prompts for Vianeo Report Generation

Generic prompts you can use with AI assistants (Claude, GPT-4, etc.) to generate Vianeo admin reports.

---

## Diagnostic Comment Prompts

### Generate from Project Data
```
Generate a Vianeo Diagnostic Comment for [Project Name].

Dimension Scores:
- Legitimacy: [X.X]/5.0
- Desirability: [X.X]/5.0
- Acceptability: [X.X]/5.0
- Feasibility: [X.X]/5.0
- Viability: [X.X]/5.0

Overall Score: [X.X]/5.0

Key Strengths: [List 3-5 items]
Critical Gaps: [List 3-5 items]

Create the YAML data file and generate both DOCX and Markdown outputs.
```

### Generate from Existing YAML
```
Generate a Vianeo Diagnostic Comment using the data in [file_path.yaml].

Run: python tools/generators/generate_diagnostic.py --input [file_path.yaml] --output outputs/[ProjectName]_Diagnostic

Create both DOCX and Markdown formats.
```

---

## Executive Sprint Report Prompts

### Generate from Sprint Data
```
Generate a Vianeo Executive Sprint Report for [Project Name].

Sprint: [Dates] ([X] sessions)
Principal Investigator: [Name]
Institution: [Organization]

Scores:
- Overall Vianeo: [X.X]/5.0
- Market Maturity: [X.X]/5.0
- Status: [GO/CONDITIONAL PROCEED/NO-GO]

Dimensions:
- Legitimacy (15%): [X.X] - [PASS/FAIL]
- Desirability (25%): [X.X] - [PASS/FAIL]
- Acceptability (20%): [X.X] - [PASS/FAIL]
- Feasibility (20%): [X.X] - [PASS/FAIL]
- Viability (20%): [X.X] - [PASS/FAIL]

Value Proposition: [2-3 sentences]
Revenue Model: [Model description]
Target Segments: [3-5 segments]

Create the YAML data file and generate both DOCX and Markdown outputs.
```

### Generate from Existing YAML
```
Generate a Vianeo Executive Sprint Report using [file_path.yaml].

Run: python tools/generators/generate_executive_sprint_report.py --input [file_path.yaml] --output outputs/[ProjectName]_Sprint_Report

Create both DOCX (for client delivery) and Markdown (for version control).
```

### Use Template
```
Copy examples/executive_sprint_report_irdose_sample.yaml and adapt it for [Project Name].

Update these fields:
- project_name: [Your Project]
- principal_investigator: [Name]
- institution: [Organization]
- sprint_duration: [Dates]
- All scores and findings

Then generate the report.
```

---

## Combined Workflows

### Generate Both Reports
```
Generate both Diagnostic Comment and Executive Sprint Report for [Project Name] from [data_file.yaml].

Run both generators:
1. python tools/generators/generate_diagnostic.py --input [data.yaml] --output outputs/[Project]_Diagnostic
2. python tools/generators/generate_executive_sprint_report.py --input [data.yaml] --output outputs/[Project]_Sprint_Report

Create all outputs (DOCX + Markdown for each).
```

### Batch Process Multiple Projects
```
Generate reports for these projects:
1. [Project A] - [file_a.yaml]
2. [Project B] - [file_b.yaml]
3. [Project C] - [file_c.yaml]

For each: generate both DOCX and Markdown, save to outputs/ with project name prefix.
```

---

## Quick Commands

**Diagnostic Comment:**
```bash
python tools/generators/generate_diagnostic.py --input [data.yaml] --output outputs/[Project]_Diagnostic
```

**Executive Sprint Report:**
```bash
python tools/generators/generate_executive_sprint_report.py --input [data.yaml] --output outputs/[Project]_Sprint_Report
```

**Format Options:**
- `--format docx` = DOCX only
- `--format markdown` = Markdown only
- (no flag) = Both formats (default)

---

**Sample Data Files:**
- `examples/diagnostic_sample.yaml`
- `examples/executive_sprint_report_irdose_sample.yaml`
