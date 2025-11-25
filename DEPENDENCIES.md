# Vianeo Sprint Step Dependencies

This document defines critical data flow requirements between sprint steps.

## Quick Reference

| Downstream | Upstream | Data That Must Match |
|------------|----------|---------------------|
| Step 7 | Step 5 | Requesters (columns), Needs (rows) |
| Step 9 | Step 5 | Requesters (inside org boxes in Buyers/End Users) |
| Step 9 | Step 8 | Players (value chain nodes), Influencers (top nodes), Acceptability |
| Step 11 (Needs) | Step 5 | Needs (columns) |
| Step 11 (Needs) | Step 7 | Importance/Satisfaction (column colors, requester dropdowns) |
| Step 11 (Means) | Step 4 | Means (columns), Differentiation status |

## Visual Flow

```
LEGITIMACY              DESIRABILITY                 ACCEPTABILITY
    |                        |                            |
Step 4                   Step 5                       Step 8
(Problem/Means)      (Needs/Requesters)         (Players/Influencers)
    |                        |                            |
    |               +--------+--------+                   |
    |               |        |        |                   |
    |               v        |        |                   |
    |           Step 7       |        |                   |
    |    (Needs Qualification)|       |                   |
    |               |        |        |                   |
    |               |        |        |                   |
    v               v        v        v                   v
Step 11         Step 11    Step 9    Step 9            Step 9
(Means view)   (Needs view) (Requesters) (Players)  (Influencers)
```

## Detailed Data Flow

### Step 4 -> Step 11 (Means View)

**What flows:**
- Human Means (with differentiation status)
- Physical/Intellectual Means (with differentiation status)
- Financial Means

**Format requirement:**
```
[Description] | Differentiating: Yes/No
```

**Example:**
- 30+ years of sales relationship to manufacturing plants | Differentiating: Yes
- Beta software for log sheets and log books | Differentiating: Yes
- 1 developer | Differentiating: No

### Step 5 -> Step 7 (Needs Qualification Matrix)

**What flows:**
- Individual Requester names (become column headers)
- Need statements (become row labels)
- Interview counts (shown in column headers)

**Exact matching required:**
- Requester names must match verbatim
- Need statements must match verbatim (60-char limit)
- No paraphrasing or combining

### Step 5 -> Step 9 (Value Network)

**What flows:**
- Individual Requesters (positioned inside organization boxes)
- Organizational Context (becomes box labels)

**Example transformation:**
```
Step 5 Output:
| Individual Requester | Organizational Context |
|---------------------|----------------------|
| Field operator      | Industrial Operational Staff |
| maintenance staff   | Industrial Operational Staff |
| plant manager       | Industrial manufacturer (management) |

Step 9 Result:
Box: "Industrial Operational Staff"
  - Contains: Field operator, maintenance staff

Box: "Industrial manufacturer (management)"
  - Contains: plant manager
```

### Step 5 -> Step 11 (Needs View)

**What flows:**
- Need statements (become column headers)
- Need types (Job-to-be-done, Pain, Expectation)

**Format requirement:**
- 60-character limit preserved
- Exact wording maintained

### Step 7 -> Step 11 (Needs View)

**What flows:**
- Importance ratings per need/requester
- Satisfaction ratings per need/requester
- Opportunity classification (determines column color)

**Column color logic:**
- High Opportunity (Fundamental + Not At All) = Green
- Expected (satisfied needs) = Gray

### Step 8 -> Step 9 (Value Network)

**What flows:**
- Player names (exact)
- Player types (Supplier, Channel, Partner, etc.)
- Influencer names (exact)
- Acceptability ratings (Favorable/Neutral/Unfavorable)

**Positioning logic:**
| Step 8 Category | Step 9 Position |
|-----------------|-----------------|
| Players (suppliers) | Left side of network |
| Players (channels) | Channels & Partners column |
| Players (customers) | Buyers & Clients column |
| Influencers | Enablers & Influencers column (top) |

## Grouping Logic

### Requesters (Step 5 -> Step 9)

Step 5 captures individual requesters AND their organizational context:
```
Individual Requester    ->    Organizational Context (Step 9 box)
------------------------------------------------------------------
Field operator          ->    Industrial Operational Staff
maintenance staff       ->    Industrial Operational Staff
plant manager           ->    Industrial manufacturer (management)
board directors         ->    Industrial manufacturer (management)
```

In Step 9, the organizational context becomes the box label, with individual requesters listed inside.

### Players vs Influencers (Step 8 -> Step 9)

| Step 8 Category | Step 9 Position |
|-----------------|-----------------|
| Players (suppliers) | Left side of network |
| Players (channels) | Channels & Partners column |
| Players (customers) | Buyers & Clients column |
| Influencers | Enablers & Influencers column (top) |

## Why Exact Matching Matters

Without enforced dependencies:
1. Requester names may differ between matrices (Step 7) and network (Step 9)
2. Need statements may be paraphrased differently across Steps 5, 7, 11
3. Means may not match between Step 4 definition and Step 11 matrix
4. Acceptability ratings may be inconsistent between Step 8 and Step 9

These inconsistencies undermine evaluation integrity and confuse committee presentations.

## Validation Protocol

Before generating any downstream step:
1. Retrieve the upstream step output for the project
2. Extract exact data (do not paraphrase)
3. Run validation checklist before finalizing output
4. Flag any mismatches for review

### Step 7 Validation Checklist
- [ ] All requester names match Step 5 exactly
- [ ] All need statements match Step 5 exactly
- [ ] Interview counts match Step 5
- [ ] Number of columns = number of requesters in Step 5
- [ ] Number of rows = number of needs in Step 5

### Step 9 Validation Checklist
- [ ] All requesters from Step 5 appear in Buyers/Clients or End Users columns
- [ ] Requesters are grouped by organizational context from Step 5
- [ ] All players from Step 8 appear in appropriate columns
- [ ] All influencers from Step 8 appear in Enablers & Influencers column
- [ ] Acceptability ratings match Step 8 exactly

### Step 11 Validation Checklist

For Features/Needs:
- [ ] All need statements match Step 5 exactly
- [ ] Column count matches need count from Step 5
- [ ] Importance-based coloring matches Step 7
- [ ] Requester dropdowns match Step 7 data

For Features/Means:
- [ ] All means match Step 4 exactly
- [ ] Differentiation status matches Step 4
- [ ] Column count matches total means from Step 4

## Testing Protocol

After updates, validate with a test project:

1. Run Steps 4, 5, 8 sequentially
2. Run Step 7 and verify:
   - Requester columns match Step 5 names exactly
   - Need rows match Step 5 statements exactly
3. Run Step 9 and verify:
   - Requesters appear inside organizational grouping boxes
   - All players from Step 8 appear in network
   - All influencers from Step 8 appear at top
   - Acceptability colors match Step 8
4. Run Step 11 and verify:
   - Features/Needs columns match Step 5 needs exactly
   - Features/Means columns match Step 4 means exactly
   - Differentiation icons match Step 4

## Summary of Changes

| File | Action | Key Addition |
|------|--------|--------------|
| `step_04_legitimacy_worksheet.md` | Update | Structured means output with differentiation |
| `step_05_needs_requesters.md` | Update | Organizational grouping for requesters |
| `step_07_needs_qualification_matrix.md` | Update | Explicit Step 5 dependency, validation checklist |
| `step_08_players_influencers.md` | Update | Clear player vs influencer structure |
| `step_09_ecosystem_value_network.md` | Update | Positioning logic, requester grouping |
| `step_11_features_needs_matrix.md` | Update | Dual-view dependencies (Needs + Means) |
| `DEPENDENCIES.md` | Create | Master reference document |

---

**Document Version:** 2.0
**Last Updated:** November 2025
**Compatible With:** VIANEO 13-Step Evaluation System (Steps 0-12)
