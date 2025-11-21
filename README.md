# VIANEO Framework - Master Repository

## Overview

The **VIANEO Business Model Evaluation Framework** is a comprehensive, evidence-based methodology for assessing startup and innovation project viability. This repository serves as the master reference for all VIANEO skills, prompts, templates, and documentation.

## Purpose

This framework provides:
- **Systematic evaluation** across 5 critical dimensions (Legitimacy, Desirability, Acceptability, Feasibility, Viability)
- **11-step sequential process** from initial screening to committee-ready packages
- **Evidence-based scoring** with clear thresholds and validation requirements
- **Professional outputs** in multiple formats (Markdown, DOCX, HTML, PDF)
- **Reusable templates** for consistent evaluation across projects

## Framework Structure

### The 11 Steps

#### Phase 1: Foundation & Screening (Steps 0-3)

**Step 0: Executive Brief Extraction**
- Transform raw application materials into structured 7-section brief (B1-B7)
- Classify maturity stage (IDEA → GROWTH)
- Output: Markdown + Professional DOCX (2-3 pages)
- **Time**: 20-30 minutes

**Step 1: Application Forms** *(Optional)*
- Convert Executive Brief into standardized formats
- Two formats: 360 SIS (social impact) or CNEN (research institutions)
- Output: Program-specific application documents
- **Time**: 15-20 minutes

**Step 2: 40-Question Diagnostic Assessment**
- Rapid comprehensive assessment across 4 dimensions
  - Team (T1-T9): 9 questions
  - Technology (Tech1-Tech11): 11 questions
  - Management (M1-M12): 12 questions
  - Commercial (C1-C8): 8 questions
- 1-5 scoring scale with evidence requirements
- Output: Assessment Results + Score Summary
- **Time**: 30-45 minutes

**Step 3: 29-Question Market Maturity Assessment**
- Comprehensive market readiness evaluation across 5 VIANEO dimensions
  - Legitimacy (15% weight, threshold ≥3.0)
  - **Desirability (25% weight, threshold ≥3.5)** - HIGHEST BAR
  - Acceptability (20% weight, threshold ≥3.0)
  - Feasibility (20% weight, threshold ≥3.0)
  - Viability (20% weight, threshold ≥3.0)
- Overall threshold: ≥3.2 (weighted average)
- Output: 3 documents (Markdown report + 2 DOCX analyses)
- **Time**: 45-60 minutes

#### Phase 2: Deep Dive Validation (Steps 4-9)

**Step 4: Legitimacy Deep Dive Worksheet**
- Validates foundational justification
- 4 assessment areas: Problem Definition, Application Domain, Team & Approach, Available Resources
- Output: Markdown + DOCX
- **Time**: 30-40 minutes

**Step 5: Needs/Requesters Analysis** (Desirability)
- WHO/WHAT/WHY/HOW framework
- 6-10 requester roles with reliability ratings
- 10 needs across Tasks/Pains/Expectations (60-char max)
- 5-6 competitive alternatives analysis
- Output: 4-file package (Markdown + 3 DOCX)
- **Weight**: 25% of overall VIANEO evaluation (highest)
- **Time**: 45-60 minutes

**Step 6: Persona Development**
- Evidence-based user personas
- Validation badge system (✓ VALIDATED / ⚠ PARTIAL / ✗ NEEDS VALIDATION)
- Based on interview counts (5+ = validated)
- Output: Professional DOCX (3-11 pages)
- **Time**: 30-45 minutes

**Step 7: Needs Qualification Matrix & Analysis Report**
- Visual dashboard: Importance vs. Satisfaction
- Two outputs: Landscape HTML Matrix + Portrait HTML/PDF Report (9-12 pages)
- Identifies hot opportunity zones (Fundamental + Not At All = priority)
- Output: 2 HTML files + PDFs
- **Time**: 45-90 minutes

**Step 8: Players & Influencers** (Acceptability)
- Ecosystem analysis: 8-10 critical players and influencers
- Acceptability ratings (🟢 Favorable / 🟡 Neutral / 🔴 Unfavorable / ⚪ Don't Know)
- Strategic notes (250-char max)
- Output: Professional 2-page DOCX + Markdown
- **Weight**: 20% of overall VIANEO acceptability
- **Time**: 30-40 minutes

**Step 9: Ecosystem Value Network Map**
- Visual ecosystem maps with value flows
- Network analysis and positioning strategies
- Output: 4 deliverables (visualization + analysis)
- **Time**: 45-60 minutes

#### Phase 3: Synthesis & Decision Support (Steps 10-11)

**Step 10: VIANEO Diagnostic Comment**
- Executive-ready diagnostic synthesis
- 4-paragraph structure (6-8 sentences total):
  1. Strengths (1-2 sentences)
  2. Risks (1-2 sentences)
  3. Near-term Actions (2-3 sentences with owners)
  4. Evidence Gaps (1-2 sentences)
- Dimension Summary Table + Critical Path Forward
- Output: Markdown + Professional DOCX
- **Time**: 25-35 minutes

**Step 11: Features-Needs Matrix**
- Interactive visual matrix: Features (columns) × Needs (rows)
- Maps solution features against validated customer needs
- Identifies coverage gaps and MVP scope
- Output: Interactive HTML + Strategic Analysis MD
- **Time**: 30-45 minutes

## Repository Structure

```
vianeo-framework/
├── prompts/              # Step 0-11 sequential prompts
│   ├── step_00_executive_brief_extraction.md
│   ├── step_01_application_forms.md
│   ├── step_02_diagnostic_40q.md
│   ├── step_03_market_maturity_29q.md
│   ├── step_04_legitimacy_worksheet.md
│   ├── step_05_needs_requesters.md
│   ├── step_06_persona_development.md
│   ├── step_07_needs_qualification_matrix.md
│   ├── step_08_players_influencers.md
│   ├── step_09_ecosystem_value_network.md
│   ├── step_10_vianeo_diagnostic.md
│   └── step_11_features_needs_matrix.md
│
├── docs/                 # Comprehensive documentation
│   ├── skill_files/      # Individual skill documentation
│   ├── guides/           # Complete reference guides
│   └── quick_reference/  # Quick reference cards
│
├── templates/            # Output templates
│   ├── markdown/         # Markdown templates
│   ├── docx/             # DOCX format templates
│   └── html/             # HTML templates (matrices, reports)
│
├── tools/                # Automation scripts
│   └── python/           # Python DOCX generators
│
├── examples/             # Sample assessments
│   └── by_stage/         # Organized by maturity stage
│
└── README.md             # This file
```

## Key Concepts

### VIANEO Dimensions

The framework evaluates 5 core dimensions:

1. **Legitimacy (15%)** - Is there a real problem worth solving?
   - Problem validation
   - Market identification
   - Foundation assessment

2. **Desirability (25%)** - Do specific people want YOUR solution? ⭐ HIGHEST BAR
   - Customer validation through interviews
   - Product-market fit
   - Needs qualification
   - Minimum: 3.5/5.0 score threshold

3. **Acceptability (20%)** - Will the ecosystem support you?
   - Stakeholder alignment
   - Regulatory environment
   - Partner readiness

4. **Feasibility (20%)** - Can you actually deliver?
   - Technical capability
   - Resource availability
   - Team competence

5. **Viability (20%)** - Is the business model sustainable?
   - Revenue model validation
   - Unit economics
   - Path to profitability

### Scoring Philosophy

- **Evidence-based**: Every claim requires documentation
- **Conservative**: Use "Don't Know" when uncertain
- **Specific**: Numbers, names, concrete examples required
- **Actionable**: Gaps identified with clear next steps

### Quality Standards

All outputs aim for professional quality suitable for:
- Investment committee presentations
- Board meetings
- Stakeholder communications
- Fundraising materials

## Usage Workflow

### For Individual Evaluations

1. Start with **Step 0** (Executive Brief) - always required
2. Run **Step 2** (40Q Diagnostic) for rapid assessment
3. Run **Step 3** (29Q Market Maturity) for comprehensive evaluation
4. If scores ≥ thresholds, proceed to deep dives (Steps 4-9) as needed
5. Generate **Step 10** (Diagnostic Comment) for decision-makers
6. Create **Step 11** (Features-Needs Matrix) when defining MVP

### For Program Management

1. Set up evaluation cadence (quarterly, per cohort, etc.)
2. Standardize on application format (Step 1) if using formal programs
3. Track dimension scores over time
4. Use diagnostics (Step 10) for portfolio reviews
5. Archive all outputs for historical comparison

## Integration with Claude

### As Connected Repository

When this repository is connected to Claude:
- Claude can access all prompts, templates, and documentation
- Reference materials available for all evaluation steps
- Consistent methodology across all assessments
- Version-controlled framework updates

### In Claude Projects

For individual evaluations, create separate Claude Projects:
- Upload company-specific materials
- Reference this master repository for methodology
- Keep evaluation data isolated per company
- Maintain confidentiality

## Contributing

This is a master reference repository. To contribute:

1. Propose changes via pull request
2. Document rationale for methodology updates
3. Ensure backward compatibility
4. Update examples to reflect changes

## Version History

- **v1.0** (Current) - Initial repository setup with complete framework structure

## License

[License to be determined]

## Contact

For questions about the VIANEO framework or this repository, contact [contact information to be added].

---

## Quick Start Guide

### First-Time Users

1. **Read this README** - Understand the framework structure
2. **Review Step 0 prompt** - This is your entry point
3. **Check templates** - Familiarize yourself with output formats
4. **Run a sample evaluation** - Use examples to learn the process

### Experienced Users

1. **Reference prompts/** - Jump to specific evaluation steps
2. **Use templates/** - Speed up output generation
3. **Consult docs/** - Deep dive on methodology
4. **Contribute examples/** - Share successful assessments

## Common Questions

**Q: Do I have to run all 11 steps?**
A: No. Steps 0, 2, and 3 are core. Others are optional based on needs.

**Q: What's the minimum for a "GO" decision?**
A: Overall score ≥3.2 with all dimensions meeting thresholds, especially Desirability ≥3.5.

**Q: How many customer interviews are required?**
A: Minimum 5 per segment for basic validation, 10+ for strong validation.

**Q: Can I modify the framework?**
A: Yes, but maintain core principles of evidence-based evaluation.

## Next Steps

1. ✅ **Repository structure created**
2. ✅ **Prompts for all 11 steps added**
3. 🔄 **Documentation to be populated** (in progress)
4. 🔄 **Templates to be added** (in progress)
5. ⏳ **Examples to be created** (pending)

---

**Framework Philosophy**: "Every sentence must add unique value. Conciseness over comprehensiveness, specificity over abstraction, actionability over analysis, evidence-based over aspirational."
