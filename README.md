# VIANEO Framework - Master Repository

> **Evidence-based startup evaluation framework** | 5 Dimensions | 11-Step Process | Committee-Ready Outputs

## Table of Contents

- [Quick Start](#quick-start)
- [What is VIANEO?](#what-is-vianeo)
- [Framework at a Glance](#framework-at-a-glance)
- [Repository Structure](#repository-structure)
- [The 5 VIANEO Dimensions](#the-5-vianeo-dimensions)
- [Usage Workflows](#usage-workflows)
- [Integration with Claude](#integration-with-claude)
- [Common Questions](#common-questions)
- [Contributing](#contributing)

---

## Quick Start

**First-time users** - Get started in 5 minutes:

1. **Read** [Framework Overview](docs/FRAMEWORK_OVERVIEW.md) - Understand the 11 steps
2. **Start** with [Step 0: Executive Brief](prompts/step_00_executive_brief_extraction.md) - Transform raw materials into structured brief
3. **Assess** with [Step 2: 40Q Diagnostic](prompts/step_02_diagnostic_40q.md) - Rapid comprehensive assessment
4. **Validate** with [Step 3: Market Maturity](prompts/step_03_market_maturity_29q.md) - Score across 5 dimensions

**Experienced users** - Quick reference:
- **Prompts**: `prompts/` - All 12 evaluation prompts (Step 0-11)
- **Templates**: `templates/` - Professional output templates
- **Docs**: `docs/` - Methodology guides and checklists
- **Examples**: `examples/` - Sample assessments

---

## What is VIANEO?

The **VIANEO Business Model Evaluation Framework** is a comprehensive, evidence-based methodology for assessing startup and innovation project viability.

### Core Features

- **5 Critical Dimensions** - Legitimacy, Desirability, Acceptability, Feasibility, Viability
- **11-Step Sequential Process** - From initial screening to committee-ready packages
- **Evidence-Based Scoring** - Clear thresholds and validation requirements
- **Professional Outputs** - Markdown, DOCX, HTML, PDF formats
- **Reusable Templates** - Consistent evaluation across projects

### Framework Philosophy

> "Every sentence must add unique value. Conciseness over comprehensiveness, specificity over abstraction, actionability over analysis, evidence-based over aspirational."

## Framework at a Glance

**The 11-Step Evaluation Process:**

| Phase | Step | Name | Time | Key Output |
|-------|------|------|------|------------|
| **Phase 1: Foundation** | 0 | Executive Brief | 20-30m | Structured 7-section brief |
| | 1 | Application Forms | 15-20m | Program-specific docs |
| | 2 | 40Q Diagnostic | 30-45m | 4-dimension assessment |
| | 3 | 29Q Market Maturity | 45-60m | 5-dimension VIANEO scores |
| **Phase 2: Deep Dive** | 4 | Legitimacy Worksheet | 30-40m | Foundation validation |
| | 5 | Needs/Requesters | 45-60m | WHO/WHAT/WHY/HOW analysis |
| | 6 | Personas | 30-45m | Evidence-based personas |
| | 7 | Needs Qualification | 45-90m | Interactive matrix + report |
| | 8 | Players/Influencers | 30-40m | Ecosystem acceptability |
| | 9 | Value Network Map | 45-60m | Network visualization |
| **Phase 3: Synthesis** | 10 | Diagnostic Comment | 25-35m | Executive decision brief |
| | 11 | Features-Needs Matrix | 30-45m | MVP scope analysis |

**Core Steps**: Steps 0, 2, and 3 are required. Others are optional based on project needs.

**Detailed descriptions**: See [Framework Overview](docs/FRAMEWORK_OVERVIEW.md) for complete step details.

## Repository Structure

```
vianeo-framework/
├── prompts/              # Step 0-11 sequential evaluation prompts
├── docs/                 # Comprehensive documentation & guides
│   ├── FORMAT_SPEC_*.md       # Output format specifications
│   ├── QUICK_VALIDATION_*.md  # Quality checklists
│   └── VIANEO_*_Guide.md      # Reference guides
├── templates/            # Output templates (Markdown, DOCX, HTML)
├── examples/             # Sample assessments by maturity stage
├── tools/                # Automation scripts
└── README.md             # This file
```

**Key Directories:**
- **`prompts/`** - 12 evaluation prompts (step_00 through step_11)
- **`docs/`** - 48+ reference documents, format specs, quality checklists
- **`templates/`** - Professional output templates for all deliverables
- **`examples/`** - Real assessment examples (Early Stage, Promising, Growth)

## The 5 VIANEO Dimensions

| Dimension | Weight | Threshold | Key Question |
|-----------|--------|-----------|--------------|
| **Legitimacy** | 15% | ≥3.0 | Is there a real problem worth solving? |
| **Desirability** ⭐ | 25% | **≥3.5** | Do specific people want YOUR solution? |
| **Acceptability** | 20% | ≥3.0 | Will the ecosystem support you? |
| **Feasibility** | 20% | ≥3.0 | Can you actually deliver? |
| **Viability** | 20% | ≥3.0 | Is the business model sustainable? |

**Overall Threshold**: ≥3.2 weighted average | **Highest Bar**: Desirability ≥3.5

### Scoring Principles

- **Evidence-based** - Every claim requires documentation
- **Conservative** - Use "Don't Know" when uncertain
- **Specific** - Numbers, names, concrete examples required
- **Actionable** - Clear next steps for every gap identified

## Usage Workflows

### Individual Project Evaluation

```mermaid
graph LR
    A[Step 0: Executive Brief] --> B[Step 2: 40Q Diagnostic]
    B --> C[Step 3: Market Maturity]
    C --> D{Scores ≥ Thresholds?}
    D -->|Yes| E[Steps 4-9: Deep Dives]
    D -->|No| F[Stop or Pivot]
    E --> G[Step 10: Diagnostic]
    E --> H[Step 11: Features-Needs]
```

**Standard Path**:
1. **Step 0** (Executive Brief) - Always required, transforms raw materials
2. **Step 2** (40Q Diagnostic) - Rapid 4-dimension assessment
3. **Step 3** (29Q Market Maturity) - Comprehensive VIANEO scoring
4. **If passing**: Proceed to relevant deep dives (Steps 4-9)
5. **Step 10** (Diagnostic Comment) - Executive decision brief
6. **Step 11** (Features-Needs) - MVP scope definition

### Program/Portfolio Management

- **Cadence**: Quarterly evaluations, per-cohort assessments
- **Standardization**: Use Step 1 for consistent application formats
- **Tracking**: Monitor dimension scores over time
- **Reviews**: Use Step 10 diagnostics for portfolio decisions
- **Archive**: Maintain historical comparison data

## Integration with Claude

### Connected Repository Setup

Connect this repository to Claude to enable:
- Direct access to all prompts, templates, and documentation
- Consistent methodology across evaluations
- Version-controlled framework updates
- Seamless reference to quality standards

### Claude Projects Best Practices

For company-specific evaluations:
- Create **separate Claude Projects** per company
- Upload company materials to isolated projects
- Reference this master repository for methodology
- Maintain confidentiality and data separation

**Tip**: Use `docs/` reference guides in Claude project knowledge for consistent outputs.

---

## Common Questions

**Q: Do I need to run all 11 steps?**
No. Steps 0, 2, and 3 are core. Others (4-11) are optional based on project needs and decision requirements.

**Q: What's the minimum for a "GO" decision?**
Overall score ≥3.2 (weighted average) with all dimensions meeting thresholds. **Critical**: Desirability must score ≥3.5.

**Q: How many customer interviews are required?**
- Basic validation: 5+ interviews per segment
- Strong validation: 10+ interviews per segment
- Validated persona: Evidence from 5+ interviews

**Q: Can I modify the framework?**
Yes, but maintain core principles: evidence-based evaluation, conservative scoring, specific examples, actionable insights.

**Q: What outputs are generated?**
Professional deliverables in multiple formats: Markdown (reports), DOCX (presentations), HTML (interactive matrices), suitable for committees, boards, and investors.

---

## Contributing

This is a master reference repository. Contributions welcome via:

1. **Pull Requests** - Propose methodology improvements
2. **Documentation** - Add examples, clarify guides
3. **Templates** - Enhance output quality
4. **Issues** - Report bugs, suggest features

**Requirements**: Document rationale, ensure backward compatibility, update examples.

---

## Version & License

**Version**: 1.0 - Complete framework with all 12 steps, 48+ docs, templates, examples
**License**: [To be determined]
**Contact**: [Contact information to be added]

---

## Additional Resources

- **[Framework Overview](docs/FRAMEWORK_OVERVIEW.md)** - Detailed step descriptions
- **[Quick Reference Card](docs/VIANEO_Quick_Reference_Card.md)** - One-page cheat sheet
- **[Assessment Workflow Guide](docs/VIANEO_Assessment_Workflow_Guide.md)** - Complete process guide
- **[Evidence Checklist](docs/VIANEO_Evidence_Checklist.md)** - Validation requirements
- **[Example Assessments](examples/)** - Sample evaluations by stage

---

**Framework Philosophy**: *"Every sentence must add unique value. Conciseness over comprehensiveness, specificity over abstraction, actionability over analysis, evidence-based over aspirational."*
