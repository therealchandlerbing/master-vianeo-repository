# VIANEO AI-Assisted Workflow

This guide explains how to execute each VIANEO step using an AI assistant (Claude, GPT, etc.) against the Master Vianeo Repository and the Vianeo platform.

---

## Quick Links

- [Assessment Workflow Guide](VIANEO_Assessment_Workflow_Guide.md) - Overall process and dependencies
- [Framework Overview](FRAMEWORK_OVERVIEW.md) - Complete step descriptions
- [Dependencies](../DEPENDENCIES.md) - Data flow requirements between steps

---

## 1. Standard Execution Pattern

When running any step, use this base pattern:

> **Execute the [Step Number and Title] from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called [exact prompt filename].**

### Example

> Execute the Step 11: Features-Needs Matrix Generation from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_11_features_needs_matrix.md`.

You may optionally paste the "Instructions for AI Assistant" section from the prompt file into your AI message. This is recommended for now, but its necessity is still under evaluation.

---

## 2. Step-Specific Attachments and Guardrails

Some steps must be grounded in Vianeo platform data to avoid hallucinations. Use this table as a quick reference.

| Step | Required Attachment(s) | Non-Negotiable Guardrails |
|------|------------------------|---------------------------|
| **0a** | Screenshot/export of initial Vianeo canvas | Do not alter the canvas structure, only fill or refine content |
| **0b** | Same as 0a, plus any additional venture docs | Respect character limits and section headings exactly |
| **2** | Executive Brief data, 40 questions from reference guide | Use all 40 questions exactly as written, do not add or remove questions |
| **3** | Executive Brief, Step 2 results | Score based on evidence only, use 1-5 scale exactly as defined |
| **4** | Executive Brief, Step 3 Legitimacy results | Document means with differentiation status |
| **5** | Executive Brief, customer research data | Do not introduce new needs or requesters beyond those validated |
| **6** | Screenshot of Requesters list from platform | Derive personas ONLY from these requesters. No new requester or persona names |
| **7** | Screenshot of Needs/Requesters table from platform | Only qualify existing needs and requesters. Do NOT invent new entities |
| **8** | Executive Brief, ecosystem research | Use only listed entities. Acceptability ratings must match defined scales |
| **9** | Value Network entity list + Players/Influencers from Step 8 | Only use listed entity names. Output Entities and Relationships tables explicitly |
| **10** | All prior step outputs | Synthesize only, do not introduce new findings |
| **11 (View 1)** | Screenshot of Features-Needs table from platform | Use only existing needs as columns, match Step 5 exactly |
| **11 (View 2)** | Screenshot/export of Means list from Step 4 | Use only existing means as columns, do not create new means |
| **12 Initial** | Steps 3, 7, 9 outputs | Synthesize dimension scores and signals |
| **12a** | Step 12 Initial output | Explore pathways, do not finalize recommendations |
| **12b** | Targeted requester segments from Steps 5/6 | Produce a SEPARATE business model per requester segment |
| **12 Final** | All Step 12 substep outputs | Generate summary dashboard only |

---

## 3. Entity Guardrail Reference

### Why Guardrails Matter

AI assistants excel at generating content but may inadvertently create entities (personas, needs, requesters, players) that don't exist in the validated Vianeo platform data. This causes:

- Data inconsistency across steps
- Failed validation checks
- Unusable outputs that don't match platform state

### The Cardinal Rules

1. **NEVER invent new requesters** - Use only those from Step 5 / platform screenshot
2. **NEVER invent new needs** - Use only those validated in Step 5
3. **NEVER invent new personas** - Derive only from existing requesters (Step 6)
4. **NEVER invent new players/influencers** - Use only those from Step 8
5. **NEVER invent new means** - Use only those from Step 4
6. **NEVER merge requester segments** in business models - Keep segment-specific

### When Adding New Features (Step 11 Only)

You MAY propose new features in Step 11, but:
- Mark them clearly as "NEW" or "PROPOSED"
- They must still map to existing needs, means, and requesters
- The client/evaluator must approve before platform entry

---

## 4. Step Execution Quick Reference

### Phase 1: Foundation & Screening

#### Step 0a: Canvas Extraction
```
> Execute the Step 0: Canvas Extraction from the GITHUB vianeo-platform-tools
> repository, synced to this project's files.
> Use the prompt called `prompts/step_00_canvas_extraction.md`.
```
**Attach:** Initial Vianeo canvas (if partially complete), key venture documents

#### Step 0b: Executive Brief Extraction
```
> Execute the Step 0: Executive Brief Extraction from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_00_executive_brief_extraction.md`.
```
**Attach:** Completed canvas from Step 0a, additional venture materials
**Prerequisite:** Step 0a complete

#### Step 2: 40-Question Diagnostic
```
> Execute the Step 2: 40-Question Diagnostic Assessment from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_02_diagnostic_40q.md`.
```
**Attach:** Executive Brief from Step 0b
**Note:** The 40 questions are defined in `docs/VIANEO_Comprehensive_Reference_Guide.md` and must be used verbatim.

#### Step 3: 29-Question Market Maturity
```
> Execute the Step 3: 29-Question Market Maturity Assessment from the GITHUB
> Master Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_03_market_maturity_29q.md`.
```
**Attach:** Executive Brief, Step 2 results

---

### Phase 2: Deep Dive Validation

#### Step 4: Legitimacy Worksheet
```
> Execute the Step 4: Legitimacy Worksheet from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_04_legitimacy_worksheet.md`.
```
**Attach:** Executive Brief, Step 3 Legitimacy dimension results

#### Step 5: Needs/Requesters Analysis
```
> Execute the Step 5: Needs and Requesters Analysis from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_05_needs_requesters.md`.
```
**Attach:** Executive Brief, customer research data, interview transcripts

#### Step 6: Persona Development
```
> Execute the Step 6: Persona Development from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_06_persona_development.md`.
```
**Attach:** Screenshot of Requesters list from Vianeo platform
**Critical:** Derive personas ONLY from the attached Requesters list. Do NOT invent new personas.

#### Step 7: Needs Qualification Matrix
```
> Execute the Step 7: Needs Qualification Matrix from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_07_needs_qualification_matrix.md`.
```
**Attach:** Screenshot of Needs/Requesters table from Vianeo platform
**Critical:** Do NOT create new needs or requesters. Match the attached table exactly.

#### Step 8: Players & Influencers
```
> Execute the Step 8: Players and Influencers Analysis from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_08_players_influencers.md`.
```
**Attach:** Executive Brief, ecosystem research data

#### Step 9: Ecosystem Value Network
```
> Execute the Step 9: Ecosystem Value Network Map from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_09_ecosystem_value_network.md`.
```
**Attach:**
1. Screenshot of Value Network entity list from Vianeo platform
2. Players and Influencers output from Step 8

**Critical:** Output explicit Entities and Relationships tables. Every entity must match the attached lists exactly.

---

### Phase 3: Synthesis & Decision

#### Step 10: Diagnostic Comment
```
> Execute the Step 10: Vianeo Diagnostic Comment from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_10_vianeo_diagnostic.md`.
```
**Attach:** All prior step outputs (especially Steps 3, 7, 9)

#### Step 11: Features-Needs Matrix (View 1)
```
> Execute the Step 11: Features-Needs Matrix Generation from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_11_features_needs_matrix.md`.
> Generate View 1: Features-Needs.
```
**Attach:** Screenshot of Features-Needs table from Vianeo platform
**Critical:** Use exactly the needs shown, no more or less.

#### Step 11: Features-Means Matrix (View 2)
```
> Using the same features as in the Features-Needs matrix, generate a
> Features-Means matrix. Base it on the available means as shown in the
> attached screenshot. Do not create any new means.
```
**Attach:** Screenshot/export of Means list from Step 4
**Note:** View 2 must be EXPLICITLY requested; it is not auto-generated with View 1.

---

### Phase 4: Viability

#### Step 12 Initial: Viability Assessment
```
> Execute the Step 12 Initial: Viability Assessment from the GITHUB Master
> Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_12_initial_viability_assessment.md`.
```
**Attach:** Steps 3, 7, 9, 10, 11 outputs

#### Step 12a: Viability Pathways
```
> Execute the Step 12a: Viability Pathways from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_12a_viability_pathways.md`.
```
**Attach:** Step 12 Initial output

#### Step 12b: Viability Business Model
```
> Execute the Step 12b: Viability Business Model from the GITHUB Master Vianeo
> Repository, synced to this project's files.
> Use the prompt called `prompts/step_12b_viability_business_model.md`.
```
**Attach:** Targeted requester segments from Steps 5/6, prior viability data
**Critical:** Produce a SEPARATE business model per requester segment. Do NOT merge segments.

#### Step 12 Final: Dashboard Generation
```
> Execute the Step 12 Final: Viability Dashboard Generation from the GITHUB
> Master Vianeo Repository, synced to this project's files.
> Use the prompt called `prompts/step_12_final_dashboard_generation.md`.
```
**Attach:** All Step 12 substep outputs

---

## 5. Troubleshooting

### AI Inventing Entities

**Symptom:** Output contains names not in your Vianeo platform data

**Fix:**
1. Explicitly state: "Use ONLY the entities from the attached screenshot"
2. Paste the entity list directly into your message
3. Add: "Before generating, list all entities you will use and confirm they match the input"

### Matrix Dimensions Don't Match

**Symptom:** Step 7 or 11 matrix has different row/column counts than expected

**Fix:**
1. State exact counts: "This matrix should have exactly 10 rows and 6 columns"
2. Attach the screenshot with visible counts
3. Add: "Confirm the row and column counts before generating"

### Step 12b Merging Segments

**Symptom:** Single blended business model instead of per-segment models

**Fix:**
1. List segments explicitly: "Generate separate business models for: [Segment A], [Segment B], [Segment C]"
2. Add: "Each segment requires its own value proposition, channels, and revenue model"
3. Request: "Format output with clear section headers per segment"

---

## 6. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-05 | Initial release based on PM feedback |

---

## Related Documents

- [VIANEO Assessment Workflow Guide](VIANEO_Assessment_Workflow_Guide.md)
- [DEPENDENCIES.md](../DEPENDENCIES.md)
- [VIANEO Comprehensive Reference Guide](VIANEO_Comprehensive_Reference_Guide.md)
- [Quick Start Card](VIANEO_Quick_Start_Card.md)
