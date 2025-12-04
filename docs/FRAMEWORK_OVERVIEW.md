# VIANEO Framework - Complete Overview

> Detailed descriptions of all 13 evaluation steps (Steps 0-12)

## Table of Contents

- [Overview](#overview)
- [Phase 1: Foundation & Screening (Steps 0-3)](#phase-1-foundation--screening-steps-0-3)
- [Phase 2: Deep Dive Validation (Steps 4-9)](#phase-2-deep-dive-validation-steps-4-9)
- [Phase 3: Synthesis & Decision Support (Steps 10-11)](#phase-3-synthesis--decision-support-steps-10-11)
- [Phase 4: Final Deliverables](#phase-4-final-deliverables)
- [Quick Reference Summary](#quick-reference-summary)

---

## Overview

The VIANEO Framework provides a systematic **13-step process (Steps 0-12)** for evaluating startup and innovation projects. This document provides comprehensive details on each step.

**Core Steps**: Steps 0, 2, and 3 are essential. All others are optional based on project needs.

**Total Time**:
- Minimum path (Steps 0, 2, 3): ~90-135 minutes
- Full evaluation (all 13 steps): ~6-8 hours

---

## Phase 1: Foundation & Screening (Steps 0-3)

### Step 0: Executive Brief Extraction

**Purpose**: Transform raw application materials into a structured, standardized brief

**Process**:
- Extract information into 7 standardized sections (B1-B7):
  - B1: Project Title & Tagline
  - B2: Problem & Solution
  - B3: Target Market & Customers
  - B4: Business Model & Value Proposition
  - B5: Team & Capabilities
  - B6: Current Status & Traction
  - B7: Funding & Resources
- Classify maturity stage (IDEA → PROOF → PROMISING → LAUNCH → GROWTH)
- Identify key strengths and gaps

**Outputs**:
- Executive Brief (Markdown, 2-3 pages)
- Professional DOCX version for stakeholders

**Time**: 20-30 minutes

**Prompt**: [`prompts/step_00_executive_brief_extraction.md`](../prompts/step_00_executive_brief_extraction.md)

---

### Step 1: Application Forms (Optional)

**Purpose**: Convert Executive Brief into standardized program application formats

**Two Format Options**:

1. **360 SIS** - Social Innovation & Sustainability programs
   - Focus on social impact metrics
   - Sustainability goals and SDG alignment
   - Community benefit assessment

2. **CNEN** - Research institution programs
   - Technical innovation focus
   - Research validation
   - Academic partnership opportunities

**Outputs**:
- Program-specific application document (DOCX)

**Time**: 15-20 minutes

**Prompt**: [`prompts/step_01_application_forms.md`](../prompts/step_01_application_forms.md)

---

### Step 2: 40-Question Diagnostic Assessment

**Purpose**: Rapid comprehensive assessment across 4 critical dimensions

**Assessment Structure**:
- **Team (T1-T9)**: 9 questions
  - Completeness, experience, commitment
  - Domain expertise
  - Advisory network

- **Technology (Tech1-Tech11)**: 11 questions
  - Innovation level
  - Development stage
  - IP protection
  - Technical risks

- **Management (M1-M12)**: 12 questions
  - Business model validation
  - Market understanding
  - Operational readiness
  - Financial planning

- **Commercial (C1-C8)**: 8 questions
  - Market opportunity
  - Competition analysis
  - Go-to-market strategy
  - Revenue potential

**Scoring**: 1-5 scale with evidence requirements
- **5**: Excellent - Strong evidence across multiple sources
- **4**: Good - Solid evidence, minor gaps
- **3**: Adequate - Basic evidence, some gaps
- **2**: Weak - Limited or questionable evidence
- **1**: Very Weak - Little to no evidence

**Outputs**:
- Assessment Results with all 40 questions scored
- Score Summary with dimension averages
- Gap analysis and recommendations

**Time**: 30-45 minutes

**Prompt**: [`prompts/step_02_diagnostic_40q.md`](../prompts/step_02_diagnostic_40q.md)

---

### Step 3: 29-Question Market Maturity Assessment

**Purpose**: Comprehensive market readiness evaluation across 5 VIANEO dimensions

**Assessment Structure** (29 questions total):

1. **Legitimacy** (6 questions, 15% weight, threshold ≥3.0)
   - Problem validation
   - Market identification
   - Solution feasibility

2. **Desirability** (6 questions, 25% weight, threshold ≥3.5) ⭐ **HIGHEST BAR**
   - Customer discovery
   - Needs validation
   - Solution preference

3. **Acceptability** (5 questions, 20% weight, threshold ≥3.0)
   - Stakeholder alignment
   - Regulatory compliance
   - Ecosystem readiness

4. **Feasibility** (6 questions, 20% weight, threshold ≥3.0)
   - Technical capability
   - Resource availability
   - Execution competence

5. **Viability** (6 questions, 20% weight, threshold ≥3.0)
   - Revenue model
   - Unit economics
   - Profitability path

**Decision Thresholds**:
- **GO**: Overall ≥3.2 AND all dimensions ≥ thresholds (especially Desirability ≥3.5)
- **MAYBE**: Near thresholds, addressable gaps identified
- **NO**: Below thresholds with fundamental issues

**Outputs**:
1. Markdown Assessment Report (comprehensive)
2. DOCX Analysis Part 1: Dimension Scores & Summary
3. DOCX Analysis Part 2: Detailed Results by Question

**Time**: 45-60 minutes

**Prompt**: [`prompts/step_03_market_maturity_29q.md`](../prompts/step_03_market_maturity_29q.md)

---

## Phase 2: Deep Dive Validation (Steps 4-9)

These steps provide detailed validation of specific dimensions. Run selectively based on project needs and Phase 1 results.

### Step 4: Legitimacy Deep Dive Worksheet

**Purpose**: Validate foundational justification and problem-solution fit

**Assessment Areas**:
1. **Problem Definition** - Clear, specific, validated problem statement
2. **Application Domain** - Market context, dynamics, trends
3. **Team & Approach** - Capability to address the problem
4. **Available Resources** - Access to necessary assets

**Methodology**:
- Evidence collection (studies, interviews, data)
- Stakeholder validation
- Market trend analysis
- Resource audit

**Outputs**:
- Legitimacy Worksheet (Markdown)
- Professional DOCX summary

**Time**: 30-40 minutes

**Prompt**: [`prompts/step_04_legitimacy_worksheet.md`](../prompts/step_04_legitimacy_worksheet.md)

---

### Step 5: Needs/Requesters Analysis (Desirability Deep Dive)

**Purpose**: Comprehensive WHO/WHAT/WHY/HOW analysis of customer needs

**Framework Components**:

1. **WHO - Requesters** (6-10 roles)
   - Role name and description
   - % of target market
   - Interview count
   - Reliability rating (A/B/C)

2. **WHAT - Needs** (10 needs)
   - Tasks to accomplish
   - Pains to avoid
   - Expectations to meet
   - 60-character limit per need

3. **WHY - Importance Scoring** (10 ratings)
   - Fundamental / Important / Nice-to-Have
   - For each of the 10 needs

4. **HOW - Current Alternatives** (5-6 competitors)
   - How customers solve the problem today
   - Satisfaction levels
   - Switching barriers

**Outputs**:
1. Markdown Summary Report
2. DOCX Part 1: Requester Profiles
3. DOCX Part 2: Needs Analysis
4. DOCX Part 3: Competitive Alternatives

**Weight**: 25% of overall VIANEO evaluation (highest)

**Time**: 45-60 minutes

**Prompt**: [`prompts/step_05_needs_requesters.md`](../prompts/step_05_needs_requesters.md)

---

### Step 6: Persona Development

**Purpose**: Create evidence-based user personas with validation tracking

**Components**:
- Demographics & psychographics
- Goals, motivations, pain points
- Behavior patterns
- Decision-making process
- Validation badge system

**Validation Levels**:
- ✓ **VALIDATED** - 5+ interviews, strong evidence
- ⚠ **PARTIAL** - 2-4 interviews, some evidence
- ✗ **NEEDS VALIDATION** - <2 interviews, assumptions only

**Outputs**:
- Professional Persona Document (DOCX, 3-11 pages)
- Multiple personas if serving different segments

**Time**: 30-45 minutes per persona

**Prompt**: [`prompts/step_06_persona_development.md`](../prompts/step_06_persona_development.md)

---

### Step 7: Needs Qualification Matrix & Analysis Report

**Purpose**: Visual dashboard showing Importance vs. Satisfaction for all needs

**Matrix Structure**:
- **X-axis**: Importance (Fundamental → Important → Nice-to-Have)
- **Y-axis**: Satisfaction (Not At All → Somewhat → Very Well)
- **Hot Zones**: Fundamental + Not At All = highest priority opportunities

**Analysis Includes**:
- Opportunity identification
- Competitive gaps
- Priority ranking
- Strategic recommendations

**Outputs**:
1. Interactive HTML Matrix (landscape, visual dashboard)
2. Comprehensive HTML/PDF Report (portrait, 9-12 pages)

**Time**: 45-90 minutes

**Prompt**: [`prompts/step_07_needs_qualification_matrix.md`](../prompts/step_07_needs_qualification_matrix.md)

---

### Step 8: Players & Influencers (Acceptability Deep Dive)

**Purpose**: Map ecosystem stakeholders and their acceptance levels

**Analysis Components**:
- **Players & Influencers**: 8-10 critical entities
  - Regulators, partners, channels, associations
  - Industry leaders, media, investors

- **Acceptability Ratings**:
  - 🟢 Favorable - Actively supportive
  - 🟡 Neutral - Neither for nor against
  - 🔴 Unfavorable - Resistant or opposing
  - ⚪ Don't Know - Insufficient information

- **Strategic Notes**: 250-character max per stakeholder
- **Action Plans**: How to secure/maintain support

**Outputs**:
- Professional 2-page DOCX report
- Markdown analysis

**Weight**: 20% of overall VIANEO acceptability dimension

**Time**: 30-40 minutes

**Prompt**: [`prompts/step_08_players_influencers.md`](../prompts/step_08_players_influencers.md)

---

### Step 9: Ecosystem Value Network Map

**Purpose**: Visual mapping of value flows in the ecosystem

**Components**:
1. **Network Diagram**
   - Project at center
   - Stakeholders positioned around
   - Value flows (arrows with labels)
   - Relationship types (transactional/collaborative)

2. **Analysis**
   - Network density
   - Key dependencies
   - Vulnerability points
   - Positioning opportunities

3. **Strategic Recommendations**
   - Network strengthening
   - Gap filling
   - Partnership priorities

**Outputs**:
1. Interactive HTML Value Network Visualization
2. Network Analysis (DOCX)
3. Priority Targets List (DOCX)
4. Strategic Recommendations (Markdown)

**Time**: 45-60 minutes

**Prompt**: [`prompts/step_09_ecosystem_value_network.md`](../prompts/step_09_ecosystem_value_network.md)

---

## Phase 3: Synthesis & Decision Support (Steps 10-11)

### Step 10: VIANEO Diagnostic Comment

**Purpose**: Executive-ready synthesis for decision-makers

**Structure** (4 paragraphs, 6-8 sentences total):

1. **Strengths** (1-2 sentences)
   - Key competitive advantages
   - Validated capabilities

2. **Risks** (1-2 sentences)
   - Primary concerns
   - Potential blockers

3. **Near-term Actions** (2-3 sentences)
   - Specific next steps with owners
   - Timeline expectations
   - Resource requirements

4. **Evidence Gaps** (1-2 sentences)
   - Critical unknowns
   - Validation needed

**Additional Components**:
- Dimension Summary Table (5 VIANEO scores)
- GO/MAYBE/NO recommendation
- Critical Path Forward (3-5 key milestones)

**Outputs**:
- Markdown Report
- Professional 1-page DOCX for committees

**Time**: 25-35 minutes

**Prompt**: [`prompts/step_10_vianeo_diagnostic.md`](../prompts/step_10_vianeo_diagnostic.md)

---

### Step 11: Features-Needs Matrix

**Purpose**: Map solution features against validated customer needs

**Matrix Structure**:
- **Columns**: Product/service features
- **Rows**: Validated customer needs (from Step 5)
- **Cells**: Coverage indicators
  - ✓✓ Strongly addresses
  - ✓ Partially addresses
  - ∅ Does not address

**Analysis Includes**:
- Coverage gaps (needs not addressed)
- Feature redundancy (multiple features per need)
- MVP scope recommendations
- Development priorities

**Outputs**:
1. Interactive HTML Matrix
2. Strategic Analysis (Markdown)
   - Gap analysis
   - Feature priorities
   - MVP definition
   - Roadmap recommendations

**Time**: 30-45 minutes

**Prompt**: [`prompts/step_11_features_needs_matrix.md`](../prompts/step_11_features_needs_matrix.md)

---

## Phase 4: Final Deliverables

After completing the evaluation steps, two primary deliverables can be generated to summarize the validation sprint findings.

### Executive Report

**Purpose**: Comprehensive multi-section report summarizing the entire validation sprint

**When to Generate**:
- At the end of a Vianeo Sprint (after Steps 11 and 12)
- Before each of the 4 client reviews (as internal documentation)
- As final deliverable for committee presentations

**Contents**:
- Cover page with project metadata
- Executive summary with score overview
- Dimension breakdown table
- Session-by-session sprint overview
- Deliverables completed matrix
- Final diagnostic comment (strengths and gaps)
- Post-Vianeo roadmap
- Key metrics to track
- Risk factors assessment
- Final assessment and attribution

**Outputs**:
- Professional DOCX (12-18 pages)

**Format Guide**: [`docs/VIANEO_Executive_Report_Formatting_Guide.md`](VIANEO_Executive_Report_Formatting_Guide.md)

---

### Diagnostic Comment (Standalone)

**Purpose**: Concise assessment document for quick-reference evaluation summary

**When to Generate**:
- As a standalone deliverable after any evaluation step
- Before client reviews as internal documentation
- As a companion to the full Executive Report
- For stakeholders who need quick summary

**Contents**:
- Score summary table (Market Maturity and Overall VIANEO)
- Dimension breakdown (5 dimensions with scores and status)
- Strengths confirmed through validation
- Critical gaps requiring action
- Summary assessment callout
- Recommendations and next steps

**Outputs**:
- Professional DOCX (2-4 pages)

**Format Guide**: [`docs/VIANEO_Diagnostic_Comment_Formatting_Guide.md`](VIANEO_Diagnostic_Comment_Formatting_Guide.md)

**Note**: This standalone Diagnostic Comment complements the Step 10 Diagnostic Comment but is formatted as a final deliverable rather than a step output.

---

## Quick Reference Summary

### Minimum Evaluation Path
**Steps 0 + 2 + 3** = ~90-135 minutes
- Step 0: Executive Brief (20-30m)
- Step 2: 40Q Diagnostic (30-45m)
- Step 3: 29Q Market Maturity (45-60m)

### Comprehensive Evaluation Path
**All 13 steps (0-12)** = ~6-8 hours
- Phase 1 (0-3): 90-135 minutes
- Phase 2 (4-9): 4-6 hours
- Phase 3 (10-11): 55-80 minutes

### Decision Criteria

**GO Decision Requires**:
- Overall VIANEO score ≥3.2 (weighted average)
- All dimension thresholds met:
  - Legitimacy ≥3.0
  - **Desirability ≥3.5** (highest bar)
  - Acceptability ≥3.0
  - Feasibility ≥3.0
  - Viability ≥3.0
- Clear evidence for all claims
- Addressable risks identified

**MAYBE Decision**:
- Near thresholds (within 0.3 points)
- Specific gaps with clear remediation path
- Additional validation needed but feasible

**NO Decision**:
- Below thresholds by >0.3 points
- Fundamental flaws in business model
- Unaddressable market or team issues
- Insufficient evidence despite attempts

---

## Related Resources

- **[Main README](../README.md)** - Repository overview
- **[Quick Reference Card](VIANEO_Quick_Reference_Card.md)** - One-page cheat sheet
- **[Assessment Workflow Guide](VIANEO_Assessment_Workflow_Guide.md)** - Process details
- **[Evidence Checklist](VIANEO_Evidence_Checklist.md)** - Validation standards
- **[All Prompts](../prompts/)** - Step-by-step instructions
- **[Templates](../templates/)** - Output formats
- **[Examples](../examples/)** - Sample assessments

---

**Last Updated**: November 2025
**Framework Version**: 2.0
