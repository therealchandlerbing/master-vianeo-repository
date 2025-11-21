# VIANEO STEP 8 QUICK REFERENCE
## Ecosystem Value Network Map

**Print this page for quick reference during Step 8 execution**

---

## AT A GLANCE

**Time:** 60-90 min standalone | 15-20 min if importing from Step 7
**Outputs:** 3 files (Data Matrix + HTML Visualization + Priority Targets Summary)
**Core Concept:** Organizations don't have needs—people do. Focus where favorable organizations contain requesters with urgent needs.

---

## THREE DELIVERABLES

| Deliverable | Format | Purpose | Use For |
|-------------|--------|---------|---------|
| **Ecosystem Data Matrix** | Markdown → DOCX | Complete structured data table | Working document, team reference, data updates |
| **HTML Visualization** | HTML | Interactive visual network map | Presentations, stakeholder communication, strategic planning |
| **Priority Targets Summary** | Markdown → DOCX | Strategic engagement plan | Sales/BD execution, resource allocation, quarterly planning |

---

## FIVE VALUE CHAIN POSITIONS

```
ENABLERS → CORE PRODUCT → CHANNELS → BUYERS → END USERS
```

| Position | Definition | Examples |
|----------|------------|----------|
| **Enablers & Influencers** | Provide infrastructure, funding, regulation, standards, expertise | Government agencies, standards bodies, industry associations, research institutions |
| **Core Product/Service** | Your offering (center of network) | Your product/service name, tagline, 6 key features |
| **Channels & Partners** | Facilitate distribution, adoption, implementation | Distribution networks, implementation consultants, resellers, integrators |
| **Buyers & Clients** | Purchasing power and budget authority | Enterprise clients, government procurement, purchasing consortia, prime contractors |
| **End Users (Downstream)** | Where innovation is actually used day-to-day | Facilities, institutions employing users, production sites, service delivery locations |

---

## ACCEPTABILITY CLASSIFICATIONS

| Level | Definition | Indicators | Actions |
|-------|------------|------------|---------|
| **Favorable** | Expressed interest, aligns with goals, actively seeking solutions | Signed MOUs, attended demos, requested pilots, allocated budget | Prioritize for engagement |
| **Neutral** | Unknown position, waiting for proof, cautiously interested | Attending presentations, asking questions, no commitment yet | Nurture relationship, provide validation |
| **Unfavorable** | Has concerns, competing priorities, sees as threat | Declined meetings, cited barriers, expressed skepticism | Understand objections, address barriers, consider if worth pursuing |

**Critical Rule:** Be evidence-based, not wishful. One positive conversation ≠ Favorable.

---

## NEED LEVEL CLASSIFICATIONS

| Level | Definition | Evidence | Urgency |
|-------|------------|----------|---------|
| **Critical** | Urgent pain NOW, actively seeking solutions, budget allocated | "We're losing $X/month", "This is my #1 priority", "Need solution by [date]" | Immediate |
| **Important** | Significant problem, measurable impact if solved, timeline flexible | "This would save X hours/week", "Meaningful KPI improvement" | Near-term |
| **Secondary** | Nice-to-have, incremental improvement, convenience | "Interesting idea", "Might be useful", "We'll consider it" | Low priority |
| **None** | No identified need for this requester | Supportive but no personal pain point | Not applicable |

**Critical Rule:** Distinguish between validated needs (evidence from conversations) and assumed needs (you think they should need it).

---

## PRIORITY TARGET LOGIC

**Priority Target = BOTH criteria met:**

```
IF (Acceptability = Favorable) AND (Need Level = Critical OR Important)
THEN Priority Target = TRUE
```

**Why Both Matter:**

| Acceptability | Need Level | Result | Conversion Probability |
|---------------|------------|--------|------------------------|
| Favorable | Critical/Important | ✅ **PRIORITY TARGET** | **HIGH** - Sweet spot! |
| Favorable | None/Secondary | ⚠️ Nice relationship | **LOW** - No action driver |
| Neutral/Unfavorable | Critical/Important | ⚠️ Need exists | **LOW** - Organizational barriers |
| Neutral/Unfavorable | None/Secondary | ❌ Skip | **VERY LOW** - No alignment |

**Expected:** 5-15 priority targets across all value chain positions

---

## HTML VISUAL ENCODING

### CSS Class Decision Logic

```
FOR EACH ORGANIZATION:

IF (Acceptability = Favorable) AND (Need = Critical OR Important):
    CSS Class = "player-box priority-target"
    Background = Light green gradient
    Border = Thick green
    Need Badge = Critical (red) OR Important (orange)
    Dot = Green

ELSE IF (Acceptability = Favorable) AND (Need = None OR Secondary):
    CSS Class = "player-box box-favorable"
    Background = White
    Border = Green
    Need Badge = None (or Secondary if applicable)
    Dot = Green

ELSE IF (Acceptability = Neutral):
    CSS Class = "player-box box-neutral"
    Background = Light orange gradient
    Border = Orange
    Need Badge = Any or None
    Dot = Orange

ELSE IF (Acceptability = Unfavorable):
    CSS Class = "player-box box-unfavorable"
    Background = Light red gradient
    Border = Red
    Need Badge = Any or None
    Dot = Red
```

### Visual Encoding Summary Table

| Condition | Box Class | Border | Background | Badge | Dot |
|-----------|-----------|--------|------------|-------|-----|
| Favorable + Critical/Important need | `priority-target` | Green (thick) | Light green gradient | Critical/Important | Green |
| Favorable only | `box-favorable` | Green | White | None | Green |
| Neutral | `box-neutral` | Orange | Light orange gradient | Any or none | Orange |
| Unfavorable | `box-unfavorable` | Red | Light red gradient | Any or none | Red |

---

## DECISION TREES

### Decision Tree 1: Acceptability Classification

```
START: Classify organization's stance

Has organizational leadership expressed interest and aligned with goals?
├─ YES: Have they taken concrete actions?
│   ├─ YES: Meetings, demos, pilots, budget allocated
│   │   → FAVORABLE
│   └─ NO: Just words, no actions yet
│       → NEUTRAL
└─ NO: Unknown or expressed concerns?
    ├─ Declined meetings, cited barriers, skeptical
    │   → UNFAVORABLE
    └─ Unknown, waiting for proof, cautious
        → NEUTRAL
```

### Decision Tree 2: Need Level Classification

```
START: Classify requester's need urgency

Is this causing urgent pain or significant loss NOW?
├─ YES: Actively seeking solutions, budget allocated?
│   ├─ YES: "We're losing $X", "This is #1 priority"
│   │   → CRITICAL
│   └─ NO: Want it eventually but no urgency
│       → IMPORTANT
└─ NO: Would it significantly improve operations?
    ├─ YES: Measurable impact, willing to invest
    │   → IMPORTANT
    └─ NO: Nice-to-have, incremental
        → SECONDARY
```

### Decision Tree 3: Which Deliverable Do I Need?

```
START: What's your use case?

Need to collect/organize ecosystem data?
    → Use: ECOSYSTEM DATA MATRIX

Need to present to stakeholders/investors?
    → Use: HTML VISUALIZATION

Need to plan sales/BD engagement?
    → Use: PRIORITY TARGETS SUMMARY

Quarterly strategy review?
    → Use: ALL THREE DELIVERABLES

Investor/board presentation?
    → Use: HTML + PRIORITY TARGETS SUMMARY

New team member onboarding?
    → Use: ALL THREE DELIVERABLES
```

---

## CHARACTER LIMITS (ENFORCED)

| Field | Limit | Purpose |
|-------|-------|---------|
| Organization Name | 60 chars | Concise entity name |
| Role/Description | 120 chars | Brief functional description |
| Requester Name/Title | 60 chars | Specific role within org |
| Need Description | 250 chars | Specific problem/pain point |
| Notes | 250 chars | Context, relationship history |
| Product Name | 60 chars | Your offering name |
| Tagline | 120 chars | Value proposition |
| Features | 60 chars each | 6 distinct capabilities |

**Why limits matter:** Forces clarity, ensures HTML visualization remains readable, maintains consistency.

---

## COMMON PITFALLS & FIXES

### Pitfall 1: Organizations vs. Individuals
❌ **Wrong:** "Dr. Sarah Johnson" as organization
✅ **Right:** Organization = "Memorial Hospital" | Requester = "Chief Medical Officers"

### Pitfall 2: Generic Categories vs. Specific Entities
❌ **Wrong:** "School Districts" as single organization
✅ **Right:** "Austin ISD", "Houston ISD", "Dallas ISD" as separate entities

### Pitfall 3: Optimistic Acceptability
❌ **Wrong:** Everyone "Favorable" based on polite conversation
✅ **Right:** "Neutral" until organizational support demonstrated through actions

### Pitfall 4: Treating All Favorable Equally
❌ **Wrong:** Engage all 20 favorable organizations simultaneously
✅ **Right:** Focus 80% effort on 5-8 priority targets (Favorable + Critical/Important needs)

### Pitfall 5: Missing the Requester
❌ **Wrong:** Organization has need, but no specific person identified
✅ **Right:** "IT Directors" or "Procurement Managers" named as requesters

### Pitfall 6: Confusing Need Levels
❌ **Wrong:** Everything is "Critical" because you want urgency
✅ **Right:** Critical = actively seeking NOW, budget allocated, timeline pressure

### Pitfall 7: HTML Without Quality Check
❌ **Wrong:** Copy-paste HTML, don't test in browser
✅ **Right:** Open in browser, verify priority targets visually distinct, check legend

### Pitfall 8: Priority Targets Without Strategy
❌ **Wrong:** List 12 targets with generic "reach out"
✅ **Right:** Each target has specific approach, timeline, metrics, barriers addressed

---

## EXECUTION CHECKLIST

### Phase 1: Data Collection ✓
- [ ] Gather data for all 5 value chain positions
- [ ] Minimum 2 organizations per position
- [ ] Organizations are specific entities (not categories)
- [ ] Requesters identified within each organization
- [ ] Acceptability evidence-based (cite conversations/actions)
- [ ] Need levels validated (not assumed)

### Phase 2: Priority Targets ✓
- [ ] Identify organizations meeting both criteria
- [ ] Count: Critical needs | Important needs
- [ ] Verify each has specific requester with validated need
- [ ] Expected: 5-15 priority targets total

### Phase 3: Ecosystem Data Matrix ✓
- [ ] All 5 value chain positions completed
- [ ] Character limits respected throughout
- [ ] Priority Targets Quick Reference section accurate
- [ ] Tables properly formatted
- [ ] Ready for DOCX conversion

### Phase 4: HTML Visualization ✓
- [ ] Project name and date updated in header
- [ ] Core product section complete (name, tagline, 6 features)
- [ ] All organizations added to correct columns
- [ ] CSS classes correctly applied (priority-target, box-favorable, box-neutral, box-unfavorable)
- [ ] Need badges only on Critical/Important/Secondary (not None)
- [ ] Acceptability dots match classifications
- [ ] Opens in browser without errors
- [ ] Priority targets visually distinct (green gradient)
- [ ] Legend displays correctly

### Phase 5: Priority Targets Summary ✓
- [ ] Only includes true priority targets (Favorable + Critical/Important)
- [ ] Each target has complete profile (all sections)
- [ ] Engagement strategies specific (not generic)
- [ ] Success metrics measurable
- [ ] Timeline realistic
- [ ] Resources honestly estimated
- [ ] Risks with mitigation strategies
- [ ] Aligns with data matrix

---

## MAINTENANCE SCHEDULE

### Monthly (15 min)
- Add new organizations/requesters discovered
- Update acceptability for engaged organizations
- Adjust need urgency based on conversations
- Add notes about developments

**Do NOT regenerate HTML or Priority Targets** (save for quarterly)

### Quarterly (30-45 min)
- Review entire data matrix for accuracy
- Validate all classifications
- Identify new priority targets
- **Regenerate HTML visualization**
- **Update Priority Targets Summary**
- Archive previous versions
- Share with team

### Annual (90-120 min)
- Complete ecosystem reassessment
- Remove irrelevant organizations
- Add all new players
- Comprehensively reassess classifications
- Update core product positioning
- **Regenerate all 3 deliverables from scratch**
- Present to leadership

---

## INTEGRATION WITH OTHER VIANEO STEPS

```
Step 5 (Desirability) → Requesters + Needs
    ↓
Step 7 (Ecosystem Mapping) → Stakeholders + Acceptability
    ↓
Step 8 (Value Network) → Complete Visualization + Priority Targets
    ↓
Committee Report / Executive Package
```

**Can Step 8 work standalone?** YES - but best results with Step 5/7 foundation.

---

## SUCCESS CRITERIA

You've successfully completed Step 8 when:

✅ **Data Matrix** contains 15-40 organizations across all 5 positions
✅ **Priority Targets** identified (5-15 organizations meeting both criteria)
✅ **HTML Visualization** renders perfectly, priority targets clearly highlighted
✅ **Strategic Plan** specific and actionable (not generic)
✅ **Team Alignment** everyone understands visual encoding and priority logic
✅ **Action-Oriented** engagement activities planned for 30/60/90 days
✅ **Evidence-Based** classifications justified with conversations/actions

---

## FILE NAMING

**Format:** `[ProjectName]_[Date]_08_[Deliverable].[ext]`

**Examples:**
- `TechEd_2025-01-15_08_Ecosystem_Data.md`
- `TechEd_2025-01-15_08_Value_Network.html`
- `TechEd_2025-01-15_08_Priority_Targets.md`

---

## QUICK HELP

**Question:** How many organizations should I include?
**Answer:** 15-40 total across all 5 positions. Minimum 2 per position.

**Question:** What if I have 30 favorable organizations?
**Answer:** That's great! But focus 80% effort on the 5-10 that have Critical/Important needs.

**Question:** Can a buyer also be an end user?
**Answer:** Sometimes, but usually different (e.g., School District buys, Elementary Schools use).

**Question:** What if I'm not sure about acceptability?
**Answer:** Default to Neutral until you have evidence of Favorable or Unfavorable.

**Question:** Do I need evidence citations (E### format)?
**Answer:** Recommended if using full VIANEO scoring, but not required for Step 8.

**Question:** How often should I update the HTML?
**Answer:** Quarterly. Monthly updates go in data matrix only.

---

**Document Version:** 1.0
**Last Updated:** 2025-01-13
**Maintained by:** VIANEO Framework Team

**Print this page and keep it handy during Step 8 execution!**
