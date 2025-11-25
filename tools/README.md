# Tools Directory

**Status**: Placeholder - Utilities to be developed

This directory is reserved for automation scripts and utilities that support the VIANEO Framework evaluation workflow.

---

## Planned Structure

```
tools/
├── README.md              ← You are here
├── generators/            ← Document generation scripts (planned)
├── validators/            ← Data validation utilities (planned)
├── converters/            ← Format conversion tools (planned)
└── requirements.txt       ← Python dependencies (planned)
```

---

## Planned Tool Categories

### 1. Document Generators

Scripts to automate creation of formatted deliverables:

| Tool | Purpose | Output |
|------|---------|--------|
| `generate_executive_brief.py` | Step 0 brief from application | DOCX |
| `generate_personas.py` | Step 6 persona document | DOCX |
| `generate_value_chain.py` | Step 9 HTML visualization | HTML |
| `generate_diagnostic.py` | Step 10 assessment report | DOCX |

### 2. Data Validators

Utilities for quality assurance:

| Tool | Purpose | Checks |
|------|---------|--------|
| `validate_character_limits.py` | Enforce 60/250 char limits | Needs, bullets, statements |
| `validate_score_thresholds.py` | Check dimension minimums | ≥3.0/≥3.5 thresholds |
| `validate_data_flow.py` | Verify step dependencies | Cross-step consistency |
| `validate_evidence.py` | Check citation formats | L1/L2/L3 confidence |

### 3. Format Converters

Tools for output format conversion:

| Tool | Purpose | Conversion |
|------|---------|------------|
| `md_to_docx.py` | Markdown to DOCX | Professional formatting |
| `docx_to_md.py` | DOCX to Markdown | Version control friendly |
| `data_to_html.py` | JSON/CSV to HTML | Interactive dashboards |

---

## Integration with Prompts

Tools are designed to work with the prompt files in `/prompts/`:

```
User Input → Prompt (step_XX.md) → AI Output → Tool Processing → Final Deliverable
```

### Workflow Example

1. **Input**: Raw application materials
2. **Prompt**: `step_00_executive_brief.md` guides AI extraction
3. **AI Output**: Markdown with structured data
4. **Tool**: `generate_executive_brief.py` creates DOCX
5. **Deliverable**: Professional document for committee

---

## Requirements (Planned)

```txt
# requirements.txt (to be created)
python-docx>=0.8.11
markdown>=3.4.0
jinja2>=3.1.0
pyyaml>=6.0
```

**Python Version**: 3.8+

---

## Contributing

When adding tools:

1. Follow naming convention: `action_target.py`
2. Include docstrings with usage examples
3. Add to appropriate category above
4. Update requirements.txt if new dependencies
5. Test with example data from `/examples/`

---

## Current Status

| Category | Status | Notes |
|----------|--------|-------|
| Document Generators | 🔲 Planned | Priority for Phase 1 |
| Data Validators | 🔲 Planned | Priority for Phase 1 |
| Format Converters | 🔲 Planned | Phase 2 |
| Example Data | 🔲 Planned | Use `/examples/` for now |

---

**Note**: Until tools are developed, all deliverable generation should be done through AI prompts with manual formatting verification.
