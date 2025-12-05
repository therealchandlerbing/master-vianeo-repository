# VIANEO End-to-End Example

A complete walkthrough of the VIANEO 13-step evaluation process using AI-assisted execution.

---

## Quick Links

- [AI-Assisted Workflow Guide](VIANEO_AI_Assisted_Workflow.md) - Standard execution patterns
- [Framework Overview](FRAMEWORK_OVERVIEW.md) - Complete step descriptions
- [Dependencies](../DEPENDENCIES.md) - Data flow requirements

---

## Prerequisites

Before starting, ensure you have:

1. **Raw venture materials** - Pitch deck, business plan, customer research
2. **Access to Vianeo platform** - For screenshots and data entry
3. **AI assistant access** - Claude, GPT, or similar
4. **This repository synced** - Master Vianeo Repository available

---

## AI-Assisted Execution Pattern

Throughout this example, we use the standard call pattern:

> **Execute the [Step Number and Title] from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called [exact prompt filename].**

See `docs/VIANEO_AI_Assisted_Workflow.md` for complete details.

---

## Phase 1: Foundation & Screening

### Step 0: Canvas and Executive Brief

Step 0 has two substeps that must be completed in order.

#### Step 0a: Canvas Extraction (Vianeo Platform Tools)

**Purpose:** Create initial Vianeo canvas aligned with platform structure

**Inputs:**
- Raw venture materials (pitch deck, business plan)
- Access to Vianeo platform for this project

**Execution (AI-assisted):**
> Execute the Step 0: Canvas Extraction from the GITHUB vianeo-platform-tools repository, synced to this project's files. Use the prompt called `prompts/step_00_canvas_extraction.md`.

Upload or paste:
- The project's initial Vianeo canvas (if partially complete)
- Key venture documents as context

**Outputs:**
- Complete, platform-aligned canvas for the venture
- Foundation for all subsequent steps

**Save output to:** `projects/[project-name]/outputs/step_00a_canvas_extraction.md`

---

#### Step 0b: Executive Brief Extraction (Master Vianeo Repo)

**Purpose:** Transform raw materials into structured 7-section Executive Brief

**Prerequisite:** Step 0a canvas extraction must be complete

**Inputs:**
- Completed canvas from Step 0a
- Additional venture documents

**Execution (AI-assisted):**
> Execute the Step 0: Executive Brief Extraction from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_00_executive_brief_extraction.md`.

**Character Limits (strictly enforced):**
- B1 (One-line description): 150 chars
- B2-B6: 300 chars each
- B7 (Team): 200 chars

**Outputs:**
- Structured Executive Brief (Markdown + DOCX)
- Evidence log with validation status

**Save output to:** `projects/[project-name]/outputs/step_00b_executive_brief.md`

---

### Step 2: 40-Question Diagnostic

**Purpose:** Rapid 4-dimension scan (Team, Technology, Management, Commercial)

**Inputs:**
- Executive Brief from Step 0b

> **CANONICAL SOURCE:** The 40 questions are defined in `docs/VIANEO_Comprehensive_Reference_Guide.md` and must be used verbatim. Do not edit wording or number of questions.

**Execution (AI-assisted):**
> Execute the Step 2: 40-Question Diagnostic Assessment from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_02_diagnostic_40q.md`.

**Outputs:**
- Assessment Results (all 40 questions scored)
- Score Summary (dimension averages)
- Questions to Ask Founders (for INSUFFICIENT DATA items)

**Save output to:** `projects/[project-name]/outputs/step_02_diagnostic_40q.md`

---

### Step 3: 29-Question Market Maturity

**Purpose:** 5-dimension VIANEO score (Legitimacy, Desirability, Acceptability, Feasibility, Viability)

**Inputs:**
- Executive Brief from Step 0b
- Step 2 results for context

**Execution (AI-assisted):**
> Execute the Step 3: 29-Question Market Maturity Assessment from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_03_market_maturity_29q.md`.

**Decision Gate:**
- Overall score ≥ 3.2: PROCEED to Phase 2
- All dimensions meet thresholds: PROCEED
- Desirability ≥ 3.5: PROCEED (highest bar)
- Otherwise: STOP/PIVOT/RE-VALIDATE

**Outputs:**
- Full 29Q assessment with dimension scores
- GO/MAYBE/NO recommendation

**Save output to:** `projects/[project-name]/outputs/step_03_market_maturity_29q.md`

---

## Phase 2: Deep Dive Validation

### Step 4: Legitimacy Worksheet

**Purpose:** Validate problem and document means inventory

**Execution (AI-assisted):**
> Execute the Step 4: Legitimacy Worksheet from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_04_legitimacy_worksheet.md`.

**Key Output:** Means with differentiation status (used in Step 11 View 2)

---

### Step 5: Needs/Requesters Analysis

**Purpose:** Identify WHO has needs and WHAT those needs are

**Execution (AI-assisted):**
> Execute the Step 5: Needs and Requesters Analysis from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_05_needs_requesters.md`.

**Critical Outputs (used downstream):**
- 6-10 Requesters with organizational context
- 10 Needs (60-char each, exact wording required for Steps 6, 7, 9, 11)

> **WARNING:** Requester names and need statements must be used EXACTLY in all downstream steps. Any paraphrasing breaks data consistency.

---

### Step 6: Persona Development

**Purpose:** Create evidence-based personas from requesters

**Inputs:**
- Screenshot of Requesters list from Vianeo platform

**Execution (AI-assisted):**
> Execute the Step 6: Persona Development from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_06_persona_development.md`.

Attach the Requesters screenshot and instruct the AI:
- Derive personas EXCLUSIVELY from the attached Requesters list
- Do NOT invent new requester names or personas
- Each persona maps to one or more requesters from Step 5

**Outputs:**
- Professional DOCX with 3-5 personas
- Validation badges based on interview counts

---

### Step 7: Needs Qualification Matrix

**Purpose:** Rate importance and satisfaction for each need/requester combination

**Inputs:**
- Screenshot of Needs/Requesters table from Vianeo platform

**Execution (AI-assisted):**
> Execute the Step 7: Needs Qualification Matrix from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_07_needs_qualification_matrix.md`.

Attach the Needs/Requesters screenshot and instruct the AI:
- Do NOT create any new needs or requesters
- Match the attached table structure exactly
- If screenshot shows 10 needs and 6 requesters, matrix has exactly 10 rows and 6 columns

**Outputs:**
- Interactive HTML matrix (landscape)
- Analysis report (9-12 pages)

---

### Step 8: Players & Influencers

**Purpose:** Map ecosystem stakeholders with acceptability ratings

**Execution (AI-assisted):**
> Execute the Step 8: Players and Influencers Analysis from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_08_players_influencers.md`.

**Critical Outputs (used in Step 9):**
- 8-10 ecosystem entities
- Acceptability ratings (🟢🟡🔴)

---

### Step 9: Ecosystem Value Network

**Purpose:** Visualize value network with explicit relationship mapping

**Inputs:**
1. Screenshot of Value Network entity list from Vianeo platform
2. Players and Influencers output from Step 8

**Execution (AI-assisted):**
> Execute the Step 9: Ecosystem Value Network Map from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_09_ecosystem_value_network.md`.

Attach both screenshots and instruct the AI:
- Output explicit Entities table and Relationships table
- Only use entity names from attachments
- Every From/To entity must exist in Entities table
- Acceptability ratings must match Step 8 exactly

**Output Format (for easy platform transfer):**

**Table 1: Entities**
| Entity Name | Entity Type | Source Step | Value Chain Position | Acceptability |
|-------------|-------------|-------------|---------------------|---------------|

**Table 2: Relationships**
| From Entity | To Entity | Flow Type | Strength | Notes |
|-------------|-----------|-----------|----------|-------|

**Outputs:**
- Interactive HTML visualization
- Entities and Relationships tables (for platform import)

---

## Phase 3: Synthesis & Decision

### Step 10: Diagnostic Comment

**Purpose:** Executive summary synthesizing all findings

**Execution (AI-assisted):**
> Execute the Step 10: Vianeo Diagnostic Comment from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_10_vianeo_diagnostic.md`.

**Outputs:**
- 4-paragraph executive brief (6-8 sentences)
- GO/MAYBE/NO recommendation

---

### Step 11: Features-Needs Matrix (Two Views)

Step 11 produces TWO linked matrices sharing the same feature rows.

#### View 1: Features-Needs

**Purpose:** Validate that features address validated customer needs

**Inputs:**
- Screenshot of Features-Needs table from Vianeo platform

**Execution (AI-assisted):**
> Execute the Step 11: Features-Needs Matrix Generation from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_11_features_needs_matrix.md`. Generate View 1: Features-Needs.

Attach the Features-Needs screenshot and instruct the AI:
- Horizontal axis: Use EXACTLY the needs shown, no more or less
- Vertical axis: Use the features shown; mark any new proposals as "NEW"
- Need statements must match Step 5 exactly

---

#### View 2: Features-Means

**Purpose:** Validate ability to implement features with available resources

> **NOTE:** View 2 must be EXPLICITLY requested. It is NOT auto-generated with View 1.

**Inputs:**
- Screenshot/export of Means list from Step 4

**Execution (AI-assisted):**
> Using the same features as in the Features-Needs matrix, generate a Features-Means matrix. Base it on the available means as shown in the attached screenshot. Do not create any new means.

Attach the Means screenshot and instruct the AI:
- Columns correspond exactly to means from screenshot
- Means names are not altered
- Preserve differentiation status from Step 4

**Outputs:**
- `step_11_features_needs_matrix.html` (View 1)
- `step_11_features_means_matrix.html` (View 2)

---

## Phase 4: Viability

Step 12 is split into four substeps for clarity.

### Step 12 Initial: Viability Assessment

**Purpose:** Synthesize key scores and signals (desirability, feasibility, viability)

**Execution (AI-assisted):**
> Execute the Step 12 Initial: Viability Assessment from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12_viability.md`.

**Inputs:** Steps 3, 7, 9, 10, 11 outputs

---

### Step 12a: Viability Pathways

**Purpose:** Explore alternative trajectories, assumptions, and strategic options

**Execution (AI-assisted):**
> Execute the Step 12a: Viability Pathways from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12a_product_market_fit.md`.

---

### Step 12b: Viability Business Model (Per Segment)

**Purpose:** Generate distinct business models for each requester segment

**Inputs:**
- Targeted requester segments from Steps 5/6
- Prior viability data

**Execution (AI-assisted):**
> Execute the Step 12b: Viability Business Model from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12b_business_model.md`.

**CRITICAL REQUIREMENT:**
> Generate a SEPARATE business model for each targeted requester segment. Do NOT merge segments into a single averaged model.

For each segment, produce:
1. Segment name and description
2. Value proposition (segment-specific)
3. Channels (segment-specific)
4. Revenue model (segment-specific)
5. Cost structure (segment-specific)
6. Key assumptions (segment-specific)

---

### Step 12 Final: Dashboard Generation

**Purpose:** Generate summary viability dashboard for decision makers

**Execution (AI-assisted):**
> Execute the Step 12 Final: Viability Dashboard Generation from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12_dashboard_generation.md`.

**Inputs:** All Step 12 substep outputs

**Outputs:**
- Summary dashboard (HTML)
- Input for Executive Report

---

## Final Deliverables

After completing all steps, generate:

1. **Executive Report (12-18 pages)** - See `docs/VIANEO_Executive_Report_Formatting_Guide.md`
2. **Diagnostic Comment (2-4 pages)** - See `docs/VIANEO_Diagnostic_Comment_Formatting_Guide.md`
3. **Interactive Dashboards** - HTML files from Steps 7, 9, 11, 12

---

## Entity Guardrail Summary

| Step | Entity Type | Rule |
|------|-------------|------|
| 6 | Personas | Derive ONLY from Step 5 Requesters |
| 7 | Needs/Requesters | Match Step 5 EXACTLY, no new entities |
| 9 | Players/Influencers | Match Step 8 EXACTLY, no new entities |
| 11 View 1 | Needs | Match Step 5 EXACTLY |
| 11 View 2 | Means | Match Step 4 EXACTLY |
| 12b | Segments | Separate model per segment, no merging |

---

## Troubleshooting

### AI Inventing Entities
**Fix:** Explicitly state "Use ONLY the entities from the attached screenshot"

### Matrix Dimensions Wrong
**Fix:** State exact counts: "This matrix should have exactly 10 rows and 6 columns"

### Step 12b Merging Segments
**Fix:** List segments explicitly: "Generate separate business models for: [Segment A], [Segment B], [Segment C]"

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-05 | Initial release based on PM feedback |
