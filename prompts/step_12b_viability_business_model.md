# Step 12b: Business Model Definition

---

## AI-Assisted Execution

> To run this step with an AI assistant, see `docs/VIANEO_AI_Assisted_Workflow.md`.

**Standard Call Pattern:**
> Execute the Step 12b: Viability Business Model from the GITHUB Master Vianeo Repository, synced to this project's files. Use the prompt called `prompts/step_12b_business_model.md`.

**Required Attachments:**
- Targeted requester segments from Steps 5/6
- Product/Market Fit Sheet from Step 12a
- Prior viability data

**Segment-Specific Business Model Requirement:**

> **CRITICAL: Generate a SEPARATE business model for each targeted requester segment.**
>
> - Do NOT merge segments into a single averaged model
> - Do NOT blend value propositions across segments
> - Each segment requires its own:
>   - Value proposition (segment-specific language)
>   - Channels (segment-appropriate distribution)
>   - Revenue model (segment-appropriate pricing)
>   - Cost structure (segment-specific)
>   - Key assumptions (segment-specific)
> - If Steps 5/6 identify 3 requester segments, generate 3 distinct business models
> - Format output with clear section headers per segment

---

## Overview

Transform Product/Market Fit configurations (Step 12a) into complete Business Model Canvases. This step defines how each product creates, delivers, and captures value through four integrated components.

## Purpose

Define coherent business models that align value proposition, revenue generation, distribution approach, and cost structure. Ensure all components work together without contradictions.

---

## Instructions for AI Assistant

Using the Product/Market Fit Sheet (Step 12a) as input, define a complete Business Model Canvas for each product. Cover all four components: Value Proposition, Revenue Stream, Distribution Channel, and Cost Structure. Validate coherence across components. Generate platform-ready summaries (250 characters each). Flag assumptions and unvalidated elements.

---

## Input Requirements

### From Step 12a (PMF Sheet)

**Required**:
- Product identity (name, description, target client)
- Targeted requesters with profiles
- Primary needs addressed with validation levels
- MVP features with rationale
- Resource requirements

### From Prior Steps

**Supporting**:
- Ecosystem analysis (Steps 8-9): Distribution channels, partnerships
- Legitimacy context (Step 4): Problem statement, domain
- Feasibility data (Step 11): Resources, capabilities

---

## Four-Component Framework

### Component 1: Value Proposition

*Why clients choose this offering over alternatives*

#### Core Positioning Statement

Format: "For [client type], [product] delivers [specific outcome] without [current pain point]"

- Single sentence capturing essence
- Client-focused language (no jargon)
- Differentiating element clear

#### Competitive Advantages (3-4 items)

For each advantage:
- **Description**: Clear articulation of advantage
- **Addresses Need**: Specific fundamental/important need from PMF
- **Evidence**: Validation data supporting this claim
- **Why Better**: Comparison to existing solutions

#### Client Benefits by Requester Type

For each requester from PMF:
- **Primary Outcome**: Specific measurable result
- **Supporting Outcomes**: 2-3 additional benefits
- **Value Delivered By**: Which MVP features enable this

#### Platform Input (250 chars max)

Condensed value proposition for Vianeo platform entry.

**Quality Checks**:
- [ ] Core positioning included
- [ ] Top competitive advantage present
- [ ] Uses client language (no jargon)
- [ ] Specific, not generic
- [ ] Immediately comprehensible

---

### Component 2: Revenue Stream

*How money is earned from this offering*

#### Revenue Model Description

2-3 sentences explaining monetization in plain language:
- What is charged for (product/service/access/transaction)
- Who pays (end user/organization/third party)
- When payment occurs (upfront/recurring/usage-based)

#### Pricing Structure

**Approach**: Per unit | Subscription | Commission | License | Usage-based | Project-based | Mixed

**Revenue Type**: One-time | Recurring | Mixed

#### Pricing Mechanisms

For each mechanism:
- **Pricing Example**: Specific price with units (e.g., "$49/month per user")
- **Rationale**: Value alignment, market context, evidence basis
- **Tied To**: Which value element or need this addresses

#### Dependencies & Constraints

- **Payment Timing**: When collected vs. value delivered
- **Minimum Commitments**: Contracts, volumes, lock-in periods
- **Partner Revenue Shares**: If applicable
- **Churn Assumptions**: For recurring models

#### Platform Input (250 chars max)

Condensed revenue stream description.

**Quality Checks**:
- [ ] Pricing approach clear
- [ ] Concrete examples included
- [ ] Revenue type specified
- [ ] Key dependencies noted
- [ ] Specific, not vague ("TBD" not acceptable)

---

### Component 3: Distribution Channel

*How customers discover and purchase this offering*

#### Discovery Channels (Awareness)

**Primary Channels** (3-4 sources):
For each:
- How it works (specific approach)
- Why effective (reaches target client)
- Expected reach (estimate)

**Supporting Channels** (2-3 secondary sources)

#### Purchase Channels (Transaction)

**Primary Purchase Channel**:
- Channel type: Direct web | Sales team | Marketplace | Retail | Partner/Reseller | Hybrid
- Transaction process (step-by-step)
- Why this matches client buying behavior

**Supporting Channels**: If applicable

#### Intermediary Strategy

**Decision**: Direct to customer OR Through intermediaries

If direct:
- Rationale for direct approach

If intermediaries:
- Intermediary types with roles
- Value each provides
- Economics (revenue share, fees)

#### Geographic Strategy

- **Phase 1 ([Timeframe]):** [Initial markets]
  - **Channel Focus:** [Primary channels for this geography]
  - **Rationale:** [Why start here]
- **Phase 2 ([Timeframe]):** [Expansion markets]
  - **Channel Focus:** [Any channel variations]
  - **Rationale:** [Expansion logic]
- **Regional Considerations:** [Any differences in distribution approach by geography]

#### Platform Input (250 chars max)

Condensed distribution description.

**Quality Checks**:
- [ ] Separates awareness from purchase
- [ ] Specific channels named
- [ ] Intermediary status clear
- [ ] Matches client buying behavior
- [ ] Actionable, not vague

---

### Component 4: Cost Structure

*Major costs to develop, produce, market, and deliver*

#### Cost Categories

**Development**:
- List major items (product development, infrastructure, R&D)

**Operations**:
- List major items (hosting, support, content, processing fees)

**Marketing/Sales**:
- List major items (digital marketing, sales team, partnerships)

**Human Resources**:
- Core team composition
- Part-time/contractors

**General/Administrative** (if significant):
- Overhead items

#### Fixed vs. Variable Classification

**Fixed Costs** (don't scale with volume):
- List with rationale

**Variable Costs** (scale with customers/usage):
- List with rationale

#### Cost Drivers

For each major driver (3-4 total):
- **Impact**: Which categories increase
- **Scaling Pattern**: Linear, sub-linear, step-function

#### Cost Structure Insights

**Business Model Pattern**:
- Software/SaaS: High fixed + low variable = good scaling
- Marketplace: Moderate fixed + low variable = network effects
- Hardware + Software: High fixed + high variable = volume-dependent
- Services: Low fixed + high variable = linear scaling

**This Product**: Pattern identification and implications

**Scaling Implications**: How costs change as business grows

**Break-Even Considerations**: High-level scale requirements

#### Platform Input (250 chars max)

Condensed cost structure summary.

**Quality Checks**:
- [ ] Major categories included
- [ ] Fixed/variable distinction clear
- [ ] Cost drivers identified
- [ ] Realistic and comprehensive
- [ ] Matches product requirements

---

## Coherence Validation

### Alignment Checks

Verify each pair aligns without contradictions:

| Check | Question | Validation |
|-------|----------|------------|
| Value-Features | Can MVP features deliver value proposition claims? | Aligned / Gap |
| Value-Revenue | Does pricing reflect value delivered? | Aligned / Gap |
| Revenue-Distribution | Does channel match payment complexity? | Aligned / Gap |
| Distribution-Costs | Are CAC costs included for chosen channels? | Aligned / Gap |
| Costs-Revenue | Can revenue model support costs at scale? | Aligned / Gap |

### Red Flag Assessment

Check for common contradictions:
- Premium value proposition + self-serve low-touch channel
- High CAC channel + low-margin revenue model
- Enterprise value prop + consumer pricing
- Complex product + no support costs
- Geographic distribution + no local costs
- Recurring revenue + no retention costs

### Coherence Summary

**Overall Assessment**: Coherent | Minor Issues | Major Issues

**Narrative** (2-3 sentences): Explain alignment, strongest points, any concerns.

---

## Quality Standards

### Character Limits (Enforced)

All platform inputs: max 250 characters

Verify character counts for all four components.

### Validation Requirements

- Value advantages must tie to validated needs from PMF
- Pricing must be specific (not "TBD" or "competitive")
- Distribution must match client buying behavior (from personas)
- Costs must cover all activities implied by other components

### Completeness Checks

- [ ] All four components complete
- [ ] Platform inputs within 250 chars
- [ ] Coherence validation performed
- [ ] Red flag assessment completed
- [ ] Evidence basis documented

---

## Common Pitfalls to Avoid

1. **Vague Value Props**: Must be specific and differentiating
2. **Undefined Pricing**: "TBD" is not acceptable
3. **Channel Mismatch**: Distribution must match client buying behavior
4. **Incomplete Costs**: Account for all implied activities
5. **Incoherent Model**: Components must work together
6. **Missing Validation**: Flag what's tested vs. assumed

---

## Timeline Expectations

**Per Product**:
- Business Model Canvas: 45-60 minutes
- Coherence validation: 15-20 minutes

---

## Output Structure

```markdown
# Business Model Canvas: [Product Name]

**Project**: [Name]
**Date**: [YYYY-MM-DD]
**Product**: [Product Name]
**Target Client**: [Segment]

## 1. VALUE PROPOSITION
[Core positioning, advantages, benefits, platform input]

## 2. REVENUE STREAM
[Model, pricing, dependencies, platform input]

## 3. DISTRIBUTION CHANNEL
[Discovery, purchase, intermediaries, platform input]

## 4. COST STRUCTURE
[Categories, fixed/variable, drivers, platform input]

## 5. COHERENCE VALIDATION
[Alignment checks, red flags, summary]

## Evidence Basis Summary
[Sources for each component]

## Next Steps
[Validation activities needed]

---

## Document Metadata
**Based On**: Step 12a (PMF Sheet), Steps 5-11
**Feeds Into**: Step 13 (Financial Modeling)
**Status**: [Draft | Review | Final]
**Date**: [YYYY-MM-DD]
```

---

## Output Files

Generate:
- `[ProductName]_Business_Model.md` - Primary deliverable
- `[ProductName]_Business_Model.docx` - If professional formatting requested

Use template: `templates/Step12_Business_Model_Template.md`

---

## Position in Workflow

**Inputs From**:
- Step 12a: Product/Market Fit Sheet
- Steps 8-9: Ecosystem and distribution insights
- Step 11: Resource and partnership data

**Feeds Into**:
- Step 12 Dashboard: Portfolio visualization
- Step 13: Financial Modeling (revenue projections, cost budgets)
- Go-to-Market Strategy: Distribution execution

---

*This prompt focuses on Business Model definition. Ensure Step 12a PMF Sheet is complete before proceeding. Use Step 12 Dashboard prompt for visualization generation.*
