# Step 8: Players & Influencers - Output Format Specification

**Version**: 2.0
**Purpose**: Exact format specification for Step 8 outputs (Ecosystem mapping)
**Dimension**: Acceptability (20% of VIANEO score)

---

## Required Output Structure

### Primary Output: Markdown Analysis

Comprehensive analysis with:
- Players table (value chain actors)
- Influencers table (non-transactional actors)
- Acceptability ratings
- Strategic implications

### Secondary Output: Professional DOCX

2-page formatted document for committee presentation

---

## Document Header

```markdown
# Players & Influencers Analysis - [Project Name]

**Date**: YYYY-MM-DD
**Project/Business Name**: [Full official name]
**Evaluator**: [Name or "Assessment Team"]
**Source**: Step 0 Executive Brief + Market Research
**Players Identified**: [X]
**Influencers Identified**: [Y]

---
```

---

## Section 1: Players (Value Chain Actors)

### Format

```markdown
## PLAYERS (Value Chain)

### Suppliers (Upstream)

| Player Name | Type | Acceptability | Validation | Rationale |
|-------------|------|---------------|------------|-----------|
| [Specific name] | Raw Material/Tech/Service/Data | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [Brief reason] |

### Channels (Distribution)

| Player Name | Type | Acceptability | Validation | Rationale |
|-------------|------|---------------|------------|-----------|
| [Specific name] | Direct/Reseller/Marketplace/Retail | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [Brief reason] |

### Partners (Complementary)

| Player Name | Type | Acceptability | Validation | Rationale |
|-------------|------|---------------|------------|-----------|
| [Specific name] | Integration/Co-marketing/Strategic | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [Brief reason] |

### Competitors

| Player Name | Type | Acceptability | Validation | Rationale |
|-------------|------|---------------|------------|-----------|
| [Specific name] | Direct/Indirect/Substitute | Unfavorable | (researched) | [Competitive position] |
| Do Nothing | Status Quo | Neutral | — | [Why customers stay with current state] |
```

### Player Count Requirements

| Category | Minimum | Typical |
|----------|---------|---------|
| Suppliers | 2 | 3-5 |
| Channels | 2 | 3-5 |
| Partners | 2 | 3-5 |
| Competitors | 3 | 4-6 |
| **Total Players** | **8** | **12-20** |

---

## Section 2: Influencers (Non-Transactional Actors)

### Format

```markdown
## INFLUENCERS (Non-Transactional)

### Regulators

| Influencer Name | Type | Acceptability | Validation | Impact |
|-----------------|------|---------------|------------|--------|
| [Specific name/body] | Government/Industry/Compliance | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [How they impact market] |

### Associations & Standards

| Influencer Name | Type | Acceptability | Validation | Impact |
|-----------------|------|---------------|------------|--------|
| [Specific name] | Association/Standards/Certification | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [How they impact market] |

### Opinion Leaders

| Influencer Name | Type | Acceptability | Validation | Impact |
|-----------------|------|---------------|------------|--------|
| [Specific name] | Analyst/Expert/Media | Favorable/Neutral/Unfavorable | (validated)/(researched)/[validate] | [How they shape opinions] |
```

### Influencer Count Requirements

| Category | Minimum | Typical |
|----------|---------|---------|
| Regulators | 1 | 2-3 |
| Associations | 1 | 2-3 |
| Opinion Leaders | 1 | 2-3 |
| **Total Influencers** | **3** | **5-10** |

---

## Acceptability Ratings

### Definition

| Rating | Definition | Indicator Color |
|--------|------------|-----------------|
| **Favorable** | Likely to support, aligned interests | Green (#10b981) |
| **Neutral** | No strong position, persuadable | Yellow (#f59e0b) |
| **Unfavorable** | Likely to resist, conflicting interests | Red (#ef4444) |

### Evidence Requirements

| Rating | Evidence Needed |
|--------|-----------------|
| Favorable | Direct contact confirming interest OR clear strategic alignment |
| Neutral | No engagement yet OR mixed signals |
| Unfavorable | Direct rejection OR competitive conflict OR regulatory barrier |

---

## Validation Status Tags

### Format

| Tag | Meaning | When to Use |
|-----|---------|-------------|
| `(validated)` | Direct contact made | Interview, meeting, or response received |
| `(researched)` | Secondary research | Website, press, reports reviewed |
| `[validate]` | Assumption | No direct evidence, needs confirmation |

**Example:**
```markdown
| Amazon Web Services | Cloud Provider | Favorable | (validated) | Active partnership discussion |
| Local Distributor | Regional | Neutral | [validate] | Potential interest assumed |
```

---

## Section 3: Strategic Analysis

### Format

```markdown
## STRATEGIC ANALYSIS

### Acceptability Summary

| Category | Favorable | Neutral | Unfavorable |
|----------|-----------|---------|-------------|
| Suppliers | [X] | [X] | [X] |
| Channels | [X] | [X] | [X] |
| Partners | [X] | [X] | [X] |
| Competitors | [X] | [X] | [X] |
| Influencers | [X] | [X] | [X] |
| **Total** | **[X]** | **[X]** | **[X]** |

### Key Relationships to Develop

1. **[Player/Influencer name]**: [Why important, suggested approach]
2. **[Player/Influencer name]**: [Why important, suggested approach]

### Potential Blockers

1. **[Player/Influencer name]**: [Risk and mitigation strategy]
2. **[Player/Influencer name]**: [Risk and mitigation strategy]

### Validation Priorities

- [ ] [Player/Influencer requiring validation] - [Suggested action]
- [ ] [Player/Influencer requiring validation] - [Suggested action]
```

---

## Section 4: Acceptability Score

### Format

```markdown
## ACCEPTABILITY SCORE

### Score Calculation

**Acceptability** = (Q3 + Q10 + Q17 + Q20 + Q23 + Q24) / 6

- Q3 (Ecosystem mapping): [1-5]
- Q10 (Stakeholder analysis): [1-5]
- Q17 (Barriers identified): [1-5]
- Q20 (Market dynamics): [1-5]
- Q23 (Regulatory/legal): [1-5]
- Q24 (Partnerships): [1-5]

**Acceptability Score**: **[X.X]** / 5.0

### Threshold Check

- **Required**: ≥3.0
- **Status**: ✓ PASS / ✗ FAIL

### Score Justification

[2-3 sentences explaining the score based on ecosystem analysis]
```

---

## Output Files

### Required Deliverables

1. **Markdown Analysis**
   - File: `[ProjectName]_Ecosystem_Analysis.md`
   - Content: Full analysis with all sections

2. **Professional DOCX** (2 pages)
   - File: `[ProjectName]_Players_Influencers.docx`
   - Page 1: Players table
   - Page 2: Influencers table + strategic summary

### File Naming Convention

```
[ProjectName]_Ecosystem_Analysis_YYYYMMDD.md
[ProjectName]_Players_Influencers_YYYYMMDD.docx
```

---

## Downstream Dependencies

Step 8 feeds into:

| Downstream Step | Data Required | Purpose |
|-----------------|---------------|---------|
| **Step 9** | Player names (exact) | Value chain nodes |
| **Step 9** | Player types | Positioning logic |
| **Step 9** | Influencer names (exact) | Enablers column |
| **Step 9** | Acceptability ratings | Node colors |
| **Step 10** | Key findings | Executive summary |

---

## Quality Checklist

Before delivery, verify:

### Players
- [ ] 8-15 players identified
- [ ] All categories covered (Suppliers, Channels, Partners, Competitors)
- [ ] Specific names (not generic categories)
- [ ] "Do Nothing" included as competitor
- [ ] Acceptability ratings for all

### Influencers
- [ ] 3-8 influencers identified
- [ ] Categories covered (Regulators, Associations, Opinion Leaders)
- [ ] Specific names/bodies
- [ ] Acceptability ratings for all

### Validation
- [ ] At least 3 players validated (direct contact)
- [ ] Validation tags used correctly
- [ ] "[validate]" used for assumptions
- [ ] Not all marked "Favorable" (unrealistic)

### Analysis
- [ ] Strategic implications documented
- [ ] Key relationships identified
- [ ] Blockers and mitigations noted
- [ ] Validation priorities listed

---

## Common Mistakes to Avoid

1. ❌ Generic categories ("suppliers") → ✅ Specific names ("AWS", "Acme Corp")
2. ❌ All rated Favorable → ✅ Realistic mix including Unfavorable
3. ❌ Missing competitors → ✅ Always include 3+ competitors + "Do Nothing"
4. ❌ Players confused with Influencers → ✅ Players transact, Influencers shape
5. ❌ No validation tags → ✅ Every rating needs (validated)/(researched)/[validate]
6. ❌ Missing rationale → ✅ Brief reason for each rating
7. ❌ Too few players/influencers → ✅ Meet minimums (8 players, 3 influencers)

---

**This specification ensures every Step 8 output follows consistent format for ecosystem analysis.**
