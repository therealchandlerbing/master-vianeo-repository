# VIANEO Framework Tools

**Status**: Implemented - Document generation, validation, and conversion utilities

This directory contains automation scripts and utilities that support the VIANEO Framework evaluation workflow, providing professional document outputs and quality assurance.

---

## Directory Structure

```
tools/
├── README.md              ← You are here
├── __init__.py            ← Package initialization
├── requirements.txt       ← Python dependencies
├── core/                  ← Shared utilities and constants
│   ├── __init__.py
│   ├── constants.py       ← Character limits, thresholds, styling
│   ├── utils.py           ← Helper functions, validation utilities
│   └── validators.py      ← Base validation functions
├── generators/            ← Document generation scripts
│   ├── __init__.py
│   ├── generate_executive_brief.py   ← Step 0 Executive Brief → DOCX/MD
│   ├── generate_personas.py          ← Step 6 Personas → DOCX/MD
│   ├── generate_value_chain.py       ← Step 9 Value Network → HTML/MD
│   └── generate_diagnostic.py        ← Step 10 Diagnostic → DOCX/MD
├── validators/            ← Data validation utilities
│   ├── __init__.py
│   ├── validate_character_limits.py  ← Enforce 60/250 char limits
│   ├── validate_score_thresholds.py  ← Check dimension minimums
│   ├── validate_data_flow.py         ← Verify cross-step consistency
│   └── validate_evidence.py          ← Check citation formats
└── converters/            ← Format conversion tools
    ├── __init__.py
    ├── md_to_docx.py      ← Markdown to professional DOCX
    ├── docx_to_md.py      ← DOCX to version-control Markdown
    └── data_to_html.py    ← JSON/CSV/YAML to HTML dashboards
```

---

## Quick Start

### Installation

```bash
cd tools
pip install -r requirements.txt
```

### Basic Usage

```bash
# Generate Executive Brief from data
python -m generators.generate_executive_brief --input project.yaml --output brief

# Validate character limits
python -m validators.validate_character_limits --input document.yaml

# Convert Markdown to DOCX
python -m converters.md_to_docx --input report.md --output report.docx
```

---

## Tool Categories

### 1. Document Generators

Scripts to automate creation of professional, formatted deliverables.

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `generate_executive_brief.py` | Step 0 Executive Brief | YAML/JSON | DOCX + MD |
| `generate_personas.py` | Step 6 Persona Document | YAML/JSON | DOCX + MD |
| `generate_value_chain.py` | Step 9 Value Network | YAML/JSON | HTML + MD |
| `generate_diagnostic.py` | Step 10 Diagnostic Comment | YAML/JSON | DOCX + MD |

**Features:**
- Professional DOCX formatting (Calibri font, VIANEO colors, proper spacing)
- Automatic character count validation
- Quality checklists included in output
- Markdown version for version control

### 2. Data Validators

Utilities for quality assurance across all VIANEO deliverables.

| Tool | Purpose | Checks |
|------|---------|--------|
| `validate_character_limits.py` | Enforce character limits | 60/250/300 char limits by field |
| `validate_score_thresholds.py` | Check dimension scores | ≥3.0 viable, ≥3.5 investment-ready |
| `validate_data_flow.py` | Verify step dependencies | Cross-step data consistency |
| `validate_evidence.py` | Check evidence quality | ID format, quality ratings, coverage |

**Character Limits Enforced:**
- B1 Name + Tagline: 150 characters combined
- B2-B6 Descriptions: 300 characters each
- B7 Team Overview: 200 characters
- Needs/Tasks/Pains: 60 characters each
- Strategic Notes: 250 characters

### 3. Format Converters

Tools for output format conversion.

| Tool | Purpose | Conversion |
|------|---------|------------|
| `md_to_docx.py` | Markdown to DOCX | Professional formatting applied |
| `docx_to_md.py` | DOCX to Markdown | Version control friendly output |
| `data_to_html.py` | Data to HTML | Interactive dashboards and charts |

**HTML Dashboard Types:**
- Dimension scores with color-coded cards
- Evidence quality distribution
- Needs qualification matrices
- Generic data tables

---

## Integration with Prompts

Tools are designed to work with the prompt files in `/prompts/`:

```
User Input → Prompt (step_XX.md) → AI Output → Tool Processing → Final Deliverable
```

### Workflow Example

1. **Input**: Raw application materials
2. **Prompt**: `step_00_executive_brief.md` guides AI extraction
3. **AI Output**: Structured YAML/JSON data
4. **Tool**: `generate_executive_brief.py` creates DOCX
5. **Validate**: `validate_character_limits.py` checks compliance
6. **Deliverable**: Professional document for committee

---

## Core Module

The `core/` module provides shared functionality:

### constants.py
- `CharacterLimits` - All VIANEO character limit values
- `ScoreThresholds` - Dimension scoring thresholds
- `DocxStyles` - Professional styling constants
- `VIANEO_DIMENSIONS` - Dimension definitions and weights
- `STEP_DEPENDENCIES` - Cross-step data flow requirements

### utils.py
- Character counting and validation
- Text cleaning (em dash removal, whitespace normalization)
- Date formatting (ISO 8601)
- Score formatting and parsing
- Markdown parsing utilities
- File naming conventions
- `ValidationReport` and `ValidationResult` classes

### validators.py
- Base validation functions
- Pattern matching validators
- Score range validators
- Content quality validators (solution neutrality, quantification)

---

## Requirements

```txt
# Document Generation
python-docx>=0.8.11          # DOCX creation
markdown>=3.4.0              # Markdown parsing
jinja2>=3.1.0                # Templating

# Data Processing
pyyaml>=6.0                  # YAML configuration
jsonschema>=4.17.0           # JSON validation
pydantic>=2.0.0              # Data validation

# HTML Generation
beautifulsoup4>=4.12.0       # HTML processing
lxml>=4.9.0                  # XML/HTML backend

# Utilities
python-dateutil>=2.8.0       # Date handling
click>=8.1.0                 # CLI interface
rich>=13.0.0                 # Terminal output
```

**Python Version**: 3.8+

---

## Contributing

When adding tools:

1. Follow naming convention: `action_target.py`
2. Include docstrings with usage examples
3. Add CLI with argparse
4. Use core utilities for common functions
5. Update requirements.txt if new dependencies
6. Test with example data from `/examples/`
7. Add to appropriate `__init__.py`

---

## Current Status

| Category | Status | Count | Notes |
|----------|--------|-------|-------|
| Document Generators | Implemented | 4 | All Phase 1 tools complete |
| Data Validators | Implemented | 4 | All Phase 1 tools complete |
| Format Converters | Implemented | 3 | Phase 2 tools complete |
| Core Utilities | Implemented | 3 | Constants, utils, validators |

**Total**: 14 Python modules providing comprehensive VIANEO automation

---

## Example Usage

### Generate Executive Brief

```python
from tools.generators import generate_executive_brief
from tools.generators.generate_executive_brief import ExecutiveBriefData

data = ExecutiveBriefData(
    project_name="MediTrack",
    tagline="AI-powered medication adherence for elderly patients",
    problem_description="Elderly patients forget 40% of medication doses...",
    # ... more fields
)

outputs = generate_executive_brief(data=data, output_format="both")
print(f"Generated: {outputs}")
```

### Validate Document

```python
from tools.validators import validate_character_limits

report = validate_character_limits(
    input_path="my_brief.yaml",
    doc_type="executive_brief"
)

if report.is_valid:
    print("All character limits valid!")
else:
    print(f"Found {report.error_count} violations")
    for result in report.results:
        if not result.is_valid:
            print(f"  - {result}")
```

### Convert Formats

```python
from tools.converters import convert_md_to_docx, convert_data_to_html

# Markdown to DOCX
convert_md_to_docx("report.md", "report.docx")

# Data to HTML dashboard
convert_data_to_html("scores.yaml", "dashboard.html", visualization_type="scores")
```

---

## Related Documentation

- `/docs/FORMAT_SPEC_*.md` - Output format specifications for each step
- `/docs/QUICK_VALIDATION_*.md` - Quality checklists
- `/DEPENDENCIES.md` - Cross-step data flow requirements
- `/templates/` - Output templates in various formats
- `/examples/` - Sample assessment data for testing

---

**Version**: 1.0.0
**Last Updated**: November 2025
**Compatible With**: VIANEO Framework v2.0 (13-Step Evaluation System)
