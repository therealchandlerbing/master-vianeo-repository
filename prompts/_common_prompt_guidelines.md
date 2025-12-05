# VIANEO Common Prompt Guidelines

> **Shared standards for all evaluation prompts** | Reduces duplication | Ensures consistency

This file contains reusable blocks, standards, and conventions that apply across all VIANEO evaluation prompts (Steps 0-12). Reference this file when creating or updating prompts to ensure consistency.

---

## Table of Contents

- [Standard Prompt Header](#standard-prompt-header)
- [AI-Assisted Execution Block](#ai-assisted-execution-block)
- [Skip Criteria](#skip-criteria)
- [File Naming Convention](#file-naming-convention)
- [Character Limits Reference](#character-limits-reference)
- [Quality Check Standards](#quality-check-standards)
- [Evidence Requirements](#evidence-requirements)
- [Output Format Standards](#output-format-standards)
- [Cross-Step Data Flow](#cross-step-data-flow)

---

## Standard Prompt Header

Every prompt file should begin with this structure:

```markdown
# STEP [N]: [Step Title]

**Time Required:** [X-Y] minutes
**Output:** [Number] document(s) - [List of deliverables]
**Weight in VIANEO Score:** [X]% (if applicable)
**Prerequisites:** [Required prior steps]

---
```

### Time Estimates by Complexity

| Complexity | Time Range | Examples |
|------------|-----------|----------|
| Quick | 15-25 min | Application forms, Canvas extraction |
| Standard | 30-45 min | Diagnostic assessments, Persona development |
| Comprehensive | 45-90 min | Needs analysis, Value network mapping |
| Extended | 2-4 hours | Full viability assessment suite |

---

## AI-Assisted Execution Block

Include this standardized block in every prompt:

```markdown
## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the [Step N: Step Title] from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/[filename].md`.

**Required Attachments:**
- [List required inputs from previous steps]
- [Additional materials if applicable]

**Canonical Source:**
> **IMPORTANT:** [Reference to authoritative source if applicable]
```

### Attachment Guidelines by Step

| Step | Minimum Required Inputs |
|------|------------------------|
| 0 | Raw venture materials, pitch deck, or canvas |
| 1 | Step 0 Executive Brief |
| 2 | Step 0 Executive Brief |
| 3 | Steps 0, 2 outputs |
| 4 | Steps 0, 2, 3 outputs |
| 5 | Steps 0-4 outputs, interview data |
| 6 | Step 5 Requesters (MUST derive from Step 5 only) |
| 7 | Steps 5, 6 outputs |
| 8 | Steps 0-5 outputs, ecosystem research |
| 9 | Steps 5, 8 outputs |
| 10 | Steps 2-5 minimum; Steps 6-9 enhance |
| 11 | Steps 4, 5, 7 outputs |
| 12 | Steps 5, 6, & 11 outputs (mandatory); all other prior step outputs (recommended) |

---

## Skip Criteria

Some steps may be skipped when conditions apply. Use these standardized skip criteria:

### When to Mark a Step as OPTIONAL

```markdown
**Status:** OPTIONAL

**Skip Conditions:**
- Team is working ad-hoc without formal program structure
- No standardized format or downstream process requires this deliverable
- Next phase begins immediately with different requirements
```

### Steps That Should NOT Be Skipped

| Step | Reason | Exception |
|------|--------|-----------|
| 0 | Foundation for all analysis | Never skip |
| 2 | Core diagnostic scores | Never skip |
| 3 | VIANEO dimension scores | Never skip |
| 5 | Desirability is 25% of score | Skip only if no customer data |

### Skip Documentation

When skipping a step, document:
1. Which step was skipped
2. Reason for skipping
3. How downstream steps will handle missing data

---

## File Naming Convention

Use this consistent naming pattern for all outputs:

```
[ProjectName]_[YYYY-MM-DD]_[StepNumber]_[DeliverableName].[ext]
```

### Examples

| Step | Example Filename |
|------|-----------------|
| 0 | `HealthTech_2025-01-15_00_Executive_Brief.md` |
| 2 | `HealthTech_2025-01-15_02_Diagnostic_Results.docx` |
| 5 | `HealthTech_2025-01-15_05_Needs_Analysis_Part1.docx` |
| 12 | `HealthTech_2025-01-15_12_Viability_Dashboard.html` |

### Naming Rules

1. **ProjectName**: Use PascalCase (e.g., `HealthTech`), with acronyms fully capitalized (e.g., `RaylAI`)
2. **Date**: ISO format YYYY-MM-DD
3. **StepNumber**: Two digits with leading zero (00-12)
4. **DeliverableName**: Descriptive, underscores for spaces
5. **Extension**: Match output format (.md, .docx, .html)

---

## Character Limits Reference

Enforce these limits across all prompts for professional outputs:

### Executive Brief (Step 0)

| Section | Limit | Purpose |
|---------|-------|---------|
| B1: Project Name + Tagline | 150 chars | Memorable identifier |
| B2: Problem Statement | 300 chars | Solution-neutral problem |
| B3: Solution Overview | 300 chars | Clear value proposition |
| B4: Market Description | 300 chars | Target market definition |
| B5: Revenue Model | 300 chars | Business model summary |
| B6: Traction Status | 300 chars | Validation evidence |
| B7: Team Overview | 200 chars | Team composition |

### General Field Limits

| Field Type | Limit | Examples |
|------------|-------|----------|
| Need statement | 60 chars | Tasks, Pains, Expectations |
| Means statement | 60 chars | Differentiating capabilities |
| Organization name | 60 chars | Players, Influencers |
| Role description | 100 chars | Requester roles |
| Strategic notes | 250 chars | Analysis notes, rationale |
| Feature name | 80 chars | MVP features |

### Character Counting Block

Include this in prompts with character limits:

```markdown
[Character count: X/[LIMIT]]
```

Example:
```markdown
**Problem Statement:**
Patients with chronic conditions struggle to track medications across multiple providers, leading to dangerous drug interactions and missed doses.

[Character count: 156/300]
```

---

## Quality Check Standards

Include appropriate quality checks at the end of each prompt:

### Standard Quality Checklist Format

```markdown
## Quality Checklist

Before finalizing, verify:

### Content Quality
- [ ] All required sections completed
- [ ] Character limits respected
- [ ] Evidence cited for all claims
- [ ] No invented data or entities

### Format Quality
- [ ] File naming convention followed
- [ ] Both Markdown and DOCX generated (if applicable)
- [ ] Tables formatted correctly
- [ ] Headings hierarchy consistent

### Data Consistency
- [ ] Entity names match previous steps exactly
- [ ] Scores use correct scale (1-5)
- [ ] No contradictions with prior outputs
```

### Step-Specific Checks

Add these based on step type:

**For Assessment Steps (2, 3):**
- [ ] All questions scored or marked with special response
- [ ] Dimension averages calculated correctly
- [ ] Red flags identified

**For Analysis Steps (5, 6, 7, 8, 9):**
- [ ] Entities derived from prior steps only
- [ ] No new personas beyond validated requesters
- [ ] Cross-references accurate

**For Synthesis Steps (10, 11, 12):**
- [ ] Metrics match source documents
- [ ] Recommendations evidence-based
- [ ] Gate recommendation justified

---

## Evidence Requirements

### Evidence Quality Scale

Use this standard 5-level scale across all steps:

| Level | Name | Description | Examples |
|-------|------|-------------|----------|
| 5 | Gold Standard | External validation, multiple sources | Published research, audited financials, signed contracts |
| 4 | Strong | Some external validation | Multiple testimonials, verified metrics |
| 3 | Moderate | Internal validation only | Single-source testimonials, founder-reported |
| 2 | Weak | Anecdotal evidence | Unverified claims, assumptions |
| 1 | Very Weak | No supporting evidence | Speculation, wishful thinking |

### Evidence ID Format

When tracking evidence, use this format:
```
E[Step#][Sequential] - e.g., E501, E502 (Step 5, evidence 1 and 2)
```

### Confidence Level Labels

| Label | Meaning | Use When |
|-------|---------|----------|
| L1 | Internal assertion | Team claims without corroboration |
| L2 | Team corroboration | Multiple team members confirm |
| L3 | Externally validated | Third-party verification exists |

**Rule:** Only L3 evidence supports scores of 4+.

---

## Output Format Standards

### Dual-Output Requirement

Most steps require both formats:

1. **Markdown (.md)** - For version control, AI processing, internal review
2. **DOCX (.docx)** - For stakeholder presentations, committee review

### DOCX Styling Standards

```
Font: Calibri (preferred) or Arial
Title: 24pt, Bold, Primary Blue (#1B365D)
Heading 1: 16pt, Bold, Primary Blue
Heading 2: 14pt, Bold, Primary Blue
Body: 11pt, Regular, Body Gray (#4A5568)
Line Height: 1.6
Margins: 1 inch all sides
```

### HTML Output Standards (Steps 7, 9, 11, 12)

```css
/* Primary Color Palette */
--color-primary: #1B365D;
--color-primary-light: #2c5282;
--color-surface: #ffffff;
--color-background: #f7fafc;

/* Status Colors */
--color-success: #10b981;
--color-warning: #f59e0b;
--color-danger: #ef4444;
```

### Table Format Standards

| Column Type | Alignment | Width |
|-------------|-----------|-------|
| ID/Number | Center | Auto |
| Name/Title | Left | 20-30% |
| Description | Left | 40-50% |
| Score | Center | 10% |
| Status | Center | 15% |

---

## Cross-Step Data Flow

### Entity Guardrails

These rules prevent data inconsistency:

| Rule | Description | Enforcing Steps |
|------|-------------|-----------------|
| Requesters Source | Personas MUST derive from Step 5 Requesters only | Steps 6, 7, 12b |
| Entity Names | Use exact names from source step (no paraphrasing) | All steps |
| No Invention | Do NOT create new requesters, personas, or players | Steps 6-12 |
| Needs Consistency | Maintain exact need wording for cross-reference | Steps 5, 7, 11 |

### Data Flow Diagram

- **Step 0 (Brief):** Input to all other steps.
- **Step 2 (40Q):** Input to Steps 3, 10, 12.
- **Step 3 (29Q):** Input to Steps 4-12.
- **Step 4 (Legitimacy):** Input to Steps 5, 11.
- **Step 5 (Requesters):** Input to Steps 6, 7, 9, 11, 12b.
- **Step 6 (Personas):** Input to Steps 7, 12b.
- **Step 7 (Needs Matrix):** Input to Steps 11, 12.
- **Step 8 (Players):** Input to Step 9.
- **Step 9 (Value Network):** Input to Steps 10, 12.
- **Steps 10-12:** Synthesis steps that consume outputs from multiple prior steps.

### Dependency Validation

Before running a step, verify inputs exist:

```markdown
**Dependency Check:**
- [ ] [Dependency 1] available
- [ ] [Dependency 2] available
- [ ] Entity names verified against source
```

---

## Special Response Types

For assessment questions, allow these special responses:

| Response | When to Use | Format |
|----------|------------|--------|
| INSUFFICIENT DATA | Materials don't provide enough info | Add to "Questions for Founders" |
| CONTEXTUAL NOTE | Score needs qualification | [Score] + CONTEXTUAL NOTE: [Explanation] |
| YES/NO | Binary question where score doesn't apply | YES or NO + brief explanation |
| N/A | Question not relevant to venture | N/A + brief justification |

**Important:** Use special responses sparingly. Most questions should receive standard 1-5 scores.

---

## Framework Philosophy

Embed this principle in all outputs:

> **"Every sentence must add unique value. Conciseness over comprehensiveness, specificity over abstraction, actionability over analysis, evidence-based over aspirational."**

### Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|-----------|
| Generic language that fits any startup | Specific claims with evidence |
| Hedging with "may" or "could" | Clear statements with confidence level |
| Burying insights in lengthy text | Front-load key findings |
| Speculating beyond evidence | Mark gaps explicitly |
| Inventing data to fill gaps | Document as INSUFFICIENT DATA |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-05 | Initial release - extracted from cross-prompt analysis |

---

*This guidelines file is the canonical reference for prompt standards. Update this file before modifying individual prompts to ensure framework-wide consistency.*
