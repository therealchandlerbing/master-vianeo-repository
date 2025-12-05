# VIANEO Framework: PM Feedback Implementation Plan

**Date Created:** 2025-12-05
**Status:** In Progress
**Priority:** Critical - Production Readiness

---

## Executive Summary

This plan addresses critical PM feedback to make the VIANEO framework fully operational for AI-assisted evaluation workflows. The changes focus on:

1. **Preventing AI hallucination** through strict entity guardrails
2. **Standardizing execution patterns** for consistent AI interactions
3. **Cross-repository integration** (vianeo-platform-tools)
4. **Canonical data sources** for questions and entities
5. **Restructuring complex steps** (12) for clarity

---

## Implementation Priority Matrix

| Priority | Change | Impact | Effort | Files Affected |
|----------|--------|--------|--------|----------------|
| **1** | AI-Assisted Workflow Guide | High | Medium | 1 new + 16 prompts |
| **2** | Step 0 Canvas + Brief split | High | Low | 3 docs |
| **3** | 40Q Canonical Source | High | Medium | 2 files + test |
| **4** | Step 6 Personas guardrails | High | Low | 2 files |
| **5** | Steps 7/9 entity hardening | High | Medium | 4 files |
| **6** | Step 11 two-view structure | Medium | Medium | 2 files |
| **7** | Step 12 substep restructure | High | High | 6 files |
| **8** | End-to-End Example updates | Medium | High | 1 new file |
| **9** | Data schema + validators | Medium | High | 3 files |
| **10** | Onboarding/testing | Medium | Medium | 3 files |

---

## Detailed Implementation Tasks

### Priority 1: AI-Assisted Workflow Guide

**Goal:** Create standard execution pattern for AI assistants

**New File:** `docs/VIANEO_AI_Assisted_Workflow.md`

**Content Structure:**
1. Standard execution pattern:
   > "Execute the [Step Number and Title] from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called [exact prompt filename]."

2. Step-specific attachments table (0a-12)

3. Non-negotiable guardrails per step

**Prompt Updates (16 files):**
Add to each `prompts/step_XX_*.md`:
```markdown
---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the [Step X: Title] from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_XX_[name].md`.

**Required Attachments:**
- [List specific attachments]

**Guardrails:**
- [List step-specific constraints]

---
```

---

### Priority 2: Step 0 Canvas + Executive Brief Split

**Goal:** Acknowledge cross-repo dependency and dual substeps

**Files to Update:**
1. `docs/FRAMEWORK_OVERVIEW.md` - Add Step 0a/0b structure
2. `docs/VIANEO_Assessment_Workflow_Guide.md` - Add substep guidance
3. `docs/VIANEO_AI_Assisted_Workflow.md` - Include Step 0a row

**Step 0 Structure:**
- **Step 0a:** Canvas Extraction (external repo: `vianeo-platform-tools/prompts/step_00_canvas_extraction.md`)
- **Step 0b:** Executive Brief Extraction (this repo: `prompts/step_00_executive_brief_extraction.md`)

---

### Priority 3: Centralize 40Q Diagnostic Questions

**Goal:** Make `VIANEO_Comprehensive_Reference_Guide.md` the single source of truth

**Files to Update:**
1. `docs/VIANEO_Comprehensive_Reference_Guide.md` - Ensure complete 40Q list
2. `prompts/step_02_diagnostic_40q.md` - Add canonical source note

**Add to Step 2 Prompt Header:**
```markdown
> **CANONICAL SOURCE:** The 40 questions below must match `docs/VIANEO_Comprehensive_Reference_Guide.md` exactly. Do not edit wording or number of questions without updating that guide first.
```

**New Validator:** `tools/validators/validate_40q_parity.py`
- Asserts questions in prompt match reference guide line-by-line

---

### Priority 4: Step 6 Personas Guardrails

**Goal:** Prevent AI from inventing new personas/requesters

**File to Update:** `prompts/step_06_persona_development.md`

**Add Prerequisites Block:**
```markdown
## Prerequisites

**Required Attachments:**
- Screenshot of Requesters list from Vianeo platform

**Entity Constraints:**
⚠️ CRITICAL: You must derive personas EXCLUSIVELY from the attached Requesters list.
- Do NOT invent new personas
- Do NOT introduce new requester names
- Use requester names EXACTLY as they appear in the screenshot
- Each persona must map to one or more requesters from the list
```

**Update DEPENDENCIES.md:**
Add formal Step 6 → Step 5 dependency

---

### Priority 5: Steps 7/9 Entity Hardening

**Goal:** Prevent AI from inventing needs, requesters, or entities

#### Step 7 Updates (`prompts/step_07_needs_qualification_matrix.md`):

**Add to Prerequisites:**
```markdown
**Required Attachments:**
- Screenshot of the Needs/Requesters table from Vianeo platform

**Entity Constraints:**
⚠️ CRITICAL GUARDRAILS:
- Do NOT create any new needs or requesters
- Every row must correspond to a requester in the attached table
- Every need must come from the attached table, written EXACTLY as shown
- If the screenshot shows 10 needs and 6 requesters, your matrix has exactly 10 rows and 6 columns
```

#### Step 9 Updates (`prompts/step_09_ecosystem_value_network.md`):

**Add Required Attachments:**
```markdown
**Required Attachments:**
1. Screenshot of Value Network entity list from Vianeo platform (right-hand entities)
2. Screenshot/export of Players and Influencers from Step 8

**Output Structure:**
Generate TWO explicit tables:

**Table 1: Entities**
| Entity Name | Entity Type | Source Step | Notes |
|-------------|-------------|-------------|-------|
| [exact name] | Player/Influencer/Requester | Step 5/8 | [context] |

**Table 2: Relationships**
| From Entity | To Entity | Flow Type | Strength | Notes |
|-------------|-----------|-----------|----------|-------|
| [exact name] | [exact name] | [type] | [rating] | [context] |

⚠️ CRITICAL: Every From/To Entity MUST match an entity from Table 1. Do NOT invent new entities.
```

---

### Priority 6: Step 11 Two-View Structure

**Goal:** Make Features-Needs and Features-Means views explicit

**File to Update:** `prompts/step_11_features_needs_matrix.md`

**Restructure Content:**

```markdown
## View 1: Features-Needs Matrix

**Purpose:** Validate that features address validated customer needs

**Required Attachment:**
- Screenshot of Features-Needs table from Vianeo platform

**Axis Constraints:**
- Horizontal axis: Use EXACTLY these N needs from the screenshot, no more or less
- Vertical axis: Use the N features shown; you may propose additional features marked as 'New'

**Guardrails:**
- Need names must match Step 5 exactly
- Do not paraphrase or abbreviate needs

---

## View 2: Features-Means Matrix

**Purpose:** Validate ability to implement features with available resources

**Trigger:** This view must be EXPLICITLY requested (not auto-generated with View 1)

**Required Attachment:**
- Screenshot/export of Means list from Step 4

**Axis Constraints:**
- Horizontal axis: Use ONLY the means shown in the screenshot
- Vertical axis: Same features as View 1

**Guardrails:**
- Do NOT create new means
- All means names must match the attached list EXACTLY
- Preserve differentiation status from Step 4
```

---

### Priority 7: Step 12 Substep Restructure

**Goal:** Break Step 12 into clear substeps with segment-specific business models

**Current Files:**
- `prompts/step_12_viability.md`
- `prompts/step_12a_product_market_fit.md`
- `prompts/step_12b_business_model.md`
- `prompts/step_12_dashboard_generation.md`

**New Structure:**
1. `prompts/step_12_initial_viability_assessment.md` - Synthesis of scores
2. `prompts/step_12a_viability_pathways.md` - Options, scenarios, assumptions
3. `prompts/step_12b_viability_business_model.md` - Per-segment business models
4. `prompts/step_12_final_dashboard_generation.md` - Summary dashboard

**Step 12b Critical Addition:**
```markdown
## Segment-Specific Business Models

⚠️ CRITICAL REQUIREMENT: Generate a SEPARATE business model for each targeted requester segment.

**Required Input:**
- List of targeted requester segments from Steps 5/6

**Output Format:**
For EACH segment, produce:
1. Segment name and description
2. Value proposition (segment-specific)
3. Channels (segment-specific)
4. Revenue model (segment-specific)
5. Cost structure (segment-specific)
6. Key assumptions (segment-specific)

**Guardrails:**
- Do NOT merge segments into a single averaged model
- Do NOT blend value propositions across segments
- Each segment's business model must stand alone
```

**Docs to Update:**
- `docs/FRAMEWORK_OVERVIEW.md` - Add substep structure
- `docs/VIANEO_Assessment_Workflow_Guide.md` - Add substep guidance

---

### Priority 8: End-to-End Example Document

**Goal:** Create runnable example with AI-assisted workflow

**New File:** `docs/VIANEO_End_to_End_Example.md`

**Structure:**
1. Prerequisites and setup
2. AI-assisted execution pattern (link to workflow guide)
3. Step 0: Canvas and Executive Brief (0a/0b)
4. Step 2: 40Q with canonical questions note
5. Step 3: 29Q Market Maturity
6. Phase 2 Deep Dives (Steps 4-9 with guardrails)
7. Step 11: Two-view execution
8. Step 12: Substep execution
9. Final deliverables generation

**Sample Project:** Include reference to existing `examples/` folder

---

### Priority 9: Data Schema and Validators

**New File:** `docs/DATA_SCHEMA.md`

**Content:**
- YAML/JSON schemas for each step output
- Required fields per step
- Entity naming conventions
- Cross-step field mappings

**Validator Extensions (`tools/validators/`):**

1. `validate_40q_parity.py` - Questions match reference guide
2. `validate_entity_consistency.py` - No new entities in Steps 6, 7, 9, 11
3. `validate_step12b_segments.py` - One business model per segment

---

### Priority 10: Onboarding and Testing

**README.md Updates:**
- Add minimal "run this sample project" sequence
- Link to AI-Assisted Workflow guide
- Python requirements (explicit version)

**New Test Script:** `tools/scripts/run_sample_project.sh`
- Validates example project against all schemas
- Runs all relevant validators

**Formatting Guide Updates:**
- Add Step 12 substeps to Executive Report structure
- Create `docs/Formatting_Guide_Parity_Checklist.md`

---

## Implementation Sequence

```
Phase 1 (Foundation):
├── Priority 1: AI-Assisted Workflow Guide [NEW]
├── Priority 2: Step 0 Canvas split [UPDATE]
└── Priority 3: 40Q Canonical source [UPDATE]

Phase 2 (Entity Guardrails):
├── Priority 4: Step 6 Personas [UPDATE]
└── Priority 5: Steps 7/9 hardening [UPDATE]

Phase 3 (Structure):
├── Priority 6: Step 11 two-view [UPDATE]
└── Priority 7: Step 12 substeps [RESTRUCTURE]

Phase 4 (Documentation):
├── Priority 8: End-to-End Example [NEW]
├── Priority 9: Data schema + validators [NEW]
└── Priority 10: Onboarding/testing [UPDATE]
```

---

## Success Criteria

- [ ] AI assistant can execute any step using standard pattern
- [ ] No entity hallucination possible (guardrails in place)
- [ ] 40Q questions verifiably canonical
- [ ] Step 12 produces segment-specific business models
- [ ] New user can run full evaluation using End-to-End Example
- [ ] All validators pass on example project

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Breaking existing workflows | All changes are additive; existing prompts still work |
| External repo dependency (Step 0a) | Clear documentation with fallback instructions |
| Over-constraining AI | Guardrails focus on entities, not content generation |

---

**Document Version:** 1.0
**Last Updated:** 2025-12-05
