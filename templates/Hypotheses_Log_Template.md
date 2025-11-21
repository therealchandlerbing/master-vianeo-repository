# Hypotheses Log: [Project Name]

**Project:** [Name]
**Date Range:** [Start] to [Current]
**Owner:** [Name]
**Last Updated:** [YYYY-MM-DD]

---

## Purpose

The Hypotheses Log transforms insights and assumptions into **testable statements with explicit validation plans**. It tracks confidence evolution as evidence accumulates and governs go/pivot/stop decisions at Gate A and beyond.

**Key Principle:** Progress when hypotheses move from low to high confidence through validation, not through hope.

---

## Hypothesis Structure

Each hypothesis must have:
1. **Clear statement** - Testable claim in "If-Then" or assertion format
2. **Proof area** - Which of the 5 VIANEO dimensions it supports
3. **Current confidence** - Low/Medium/High based on evidence
4. **Validation method** - How to test this hypothesis
5. **Target evidence** - What would prove or disprove it
6. **Owner** - Who is responsible for validation
7. **Due date** - When validation is expected

---

## Confidence Levels

| Level | Definition | Criteria | Action |
|-------|------------|----------|--------|
| **Low** | Assumption or internal belief | Only L1 (internal assertion) or L2 (team corroboration) evidence | Must validate before Gate A |
| **Medium** | Some external evidence | 1-2 L3 (external validated) evidence sources | Can inform go/pivot, need more for scale |
| **High** | Strong external validation | 3+ L3 evidence sources, triangulated | Can inform investment decisions |

---

## Hypotheses Log Entries

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H001 | [Testable statement] | [L/D/A/F/V] | [L/M/H] | [E###, E###] | [Method] | [What would prove/disprove] | [Name] | [Date] | [Open/In Progress/Validated/Invalidated] |
| H002 | | | | | | | | | |
| H003 | | | | | | | | | |

**Proof Area Codes:**
- **L** = Legitimacy
- **D** = Desirability
- **A** = Acceptability
- **F** = Feasibility
- **V** = Viability

**Status Values:**
- **Open** - Not yet started validation
- **In Progress** - Validation underway
- **Validated** - Evidence supports hypothesis (upgrade confidence)
- **Invalidated** - Evidence disproves hypothesis (pivot required)
- **On Hold** - Waiting for dependencies

---

## Example Hypotheses

### Legitimacy (L)

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H001 | Rural primary care physicians experience significant delays (2+ weeks) accessing specialist consultations for complex diagnoses | L | High | E001, E002, E007, E009 | Discovery interviews with 10+ rural clinic MDs | 8+ of 10 interviewees confirm 2+ week delays | John | 2025-01-20 | Validated |
| H002 | This delay contributes to measurable patient harm (missed diagnoses, treatment delays, adverse outcomes) | L | Medium | E002, E011 | Medical record review + specialist validation | Documentation of 20+ cases where delay caused measurable harm | Sarah | 2025-02-05 | In Progress |
| H003 | The problem is specific to rural settings, not urban/suburban clinics | L | Low | - | Comparative interviews: rural vs urban clinics | Urban clinics report <3 day specialist access | John | 2025-02-10 | Open |

### Desirability (D)

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H004 | Rural clinic physicians rank "faster specialist access" as a top-3 operational priority | D | Medium | E001, E003, E005 | Needs prioritization exercise with 15+ physicians | 10+ of 15 rank this in top 3 of 10-12 needs | Mike | 2025-01-25 | In Progress |
| H005 | Current telemedicine solutions are inadequate due to long wait times (satisfaction score ≤2 on 1-5 scale) | D | High | E003, E006, E008, E010 | Interview 20+ clinics currently using telemedicine | 15+ of 20 rate satisfaction ≤2 for wait times | Mike | 2025-01-22 | Validated |
| H006 | AI-assisted triage can reduce wait time from weeks to minutes while maintaining diagnostic accuracy | D | Low | - | Pilot test with 50 cases, compare to specialist gold standard | ≥85% diagnostic accuracy, <15 min response time | Sarah | 2025-03-01 | Open |

### Acceptability (A)

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H007 | Rural health system administrators will support adoption if malpractice risk is reduced | A | Medium | E012, E015 | Interviews with 10 health system administrators | 7+ of 10 express willingness to pilot with evidence of risk reduction | Lisa | 2025-02-15 | In Progress |
| H008 | State medical boards will not object to AI-assisted diagnostic recommendations if licensed physicians review all outputs | A | Low | - | Policy review + 3 interviews with medical board members | Written confirmation or published guidance allowing AI-assistance with physician oversight | Lisa | 2025-02-28 | Open |
| H009 | Existing telemedicine vendors will be neutral to resistant (not supportive partners) | A | Medium | E018 | Competitor analysis + 5 partnership outreach attempts | Response patterns and partnership discussions | John | 2025-02-20 | In Progress |

### Feasibility (F)

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H010 | A functional MVP can be built in 8 weeks with existing AI models and EHR integration APIs | F | Medium | E020, INTERNAL-003 | Technical proof-of-concept sprint | Working prototype handling 10 test cases end-to-end | Sarah | 2025-02-10 | In Progress |
| H011 | Team has sufficient ML expertise to train and validate diagnostic models | F | High | E021, E022 (team CVs + external references) | External validation of team capabilities | 2 external ML experts confirm team has necessary skills | Sarah | 2025-01-18 | Validated |
| H012 | Epic EHR API integration is technically feasible within compliance requirements | F | Low | - | Epic developer program registration + API documentation review | Successful test integration with sandbox environment | Mark | 2025-02-25 | Open |

### Viability (V)

| H# | Hypothesis Statement | Proof Area | Confidence | Evidence IDs | Validation Method | Target Evidence | Owner | Due Date | Status |
|----|---------------------|------------|------------|--------------|-------------------|-----------------|-------|----------|--------|
| H013 | Rural clinics will pay $200-400/month for faster specialist access with demonstrated quality | V | Medium | E003, E014, E016 | Pricing interviews with 15 clinic directors | 10+ of 15 express willingness to pay in this range | Mike | 2025-01-28 | In Progress |
| H014 | CAC can be kept under $4K through direct sales to health systems (not individual clinics) | V | Low | INTERNAL-005 | Sales process modeling + 5 pilot health system engagements | Signed pilots with ≤$4K acquisition cost per clinic | Mike | 2025-03-15 | Open |
| H015 | Unit economics achieve 5:1 LTV:CAC ratio at scale (500+ clinics) | V | Low | INTERNAL-006 | Financial model with sensitivity analysis | Model shows profitability path with conservative assumptions | Lisa | 2025-02-05 | Open |
| H016 | Gross margin can reach 75% with cloud-based delivery model | V | Low | INTERNAL-007 | Cost structure analysis + cloud pricing | Detailed cost model validates 75% margin at scale | Lisa | 2025-02-05 | Open |

---

## Hypothesis Development Process

### Phase 1: Generation (After Steps 0-2)
1. Review Executive Brief, 40Q Diagnostic, Evidence Log
2. Identify assumptions embedded in assessment
3. Convert assumptions into testable hypotheses
4. Assign to proof areas (L, D, A, F, V)
5. Note current confidence (likely Low at this stage)
6. Draft initial validation methods

### Phase 2: Prioritization (Before Step 3-5)
1. Identify **critical hypotheses** - if wrong, project fails
2. Identify **enabling hypotheses** - needed to proceed but not fatal if wrong
3. Identify **optimization hypotheses** - improve outcomes but not required for viability
4. Focus validation efforts on critical hypotheses first

### Phase 3: Validation (Steps 3-8)
1. Execute validation methods
2. Collect evidence, assign Evidence IDs
3. Update confidence levels as evidence accumulates
4. Document validated or invalidated status
5. Trigger pivots if critical hypotheses are invalidated

### Phase 4: Gate A Review
1. All critical hypotheses must be at Medium or High confidence
2. Enabling hypotheses should have validation plans in progress
3. Optimization hypotheses can remain Low confidence
4. Decision: Go if critical hypotheses validated, Pivot if invalidated, Stop if unvalidatable

---

## Validation Methods Reference

### Discovery Interviews
- **When:** Hypotheses about user needs, pain points, workflows
- **Target:** 10-20 interviews per segment for saturation
- **Evidence:** Interview transcripts with verbatim quotes
- **Confidence Upgrade:** Low → Medium with 10+ interviews, Medium → High with 20+ triangulated

### Surveys/Questionnaires
- **When:** Quantify prevalence of needs or behaviors
- **Target:** 50-100+ responses for statistical confidence
- **Evidence:** Survey data with response rates and demographics
- **Confidence Upgrade:** Low → Medium with 50+ responses, Medium → High with 100+ and >50% response rate

### Prototype Testing
- **When:** Hypotheses about solution desirability or technical feasibility
- **Target:** 10-20 users for qualitative, 50+ for quantitative
- **Evidence:** Usage data, feedback forms, observation notes
- **Confidence Upgrade:** Low → Medium with 10+ users, Medium → High with 50+ and positive metrics

### Pilot Deployments
- **When:** Hypotheses about real-world feasibility and willingness to pay
- **Target:** 5-10 pilot customers for initial validation
- **Evidence:** Pilot metrics, retention data, payment conversion
- **Confidence Upgrade:** Low → High if pilots convert to paying customers

### Published Research
- **When:** Hypotheses about market size, problem prevalence, industry trends
- **Target:** 2-3 credible studies supporting claim
- **Evidence:** Citations with page numbers and direct quotes
- **Confidence Upgrade:** Low → Medium with 1 study, Medium → High with 3+ studies from different sources

### Expert Interviews
- **When:** Hypotheses about technical feasibility, regulatory environment, industry practices
- **Target:** 3-5 recognized experts
- **Evidence:** Interview transcripts, written opinions
- **Confidence Upgrade:** Low → Medium with 2 experts, Medium → High with 5+ experts consensus

### Competitive Analysis
- **When:** Hypotheses about positioning, pricing, feature gaps
- **Target:** 3-5 direct competitors analyzed
- **Evidence:** Product analysis, pricing data, customer reviews
- **Confidence Upgrade:** Low → Medium with direct analysis, validate further with customer interviews

### LOIs/MOUs
- **When:** Hypotheses about acceptability and willingness to pay
- **Target:** 3-5 signed letters of intent
- **Evidence:** Signed documents with specific commitments
- **Confidence Upgrade:** Low → High (LOIs are strong validation)

---

## Pivot Triggers

### Critical Hypothesis Invalidated
**Trigger:** Evidence strongly disproves a critical hypothesis
**Action:** Stop current direction, analyze root cause, explore pivot options
**Example:** "Rural clinics will pay $200-400/month" → 15 interviews show max willingness is $50/month → Pivot to different business model or customer segment

### Enabling Hypothesis Invalidated
**Trigger:** Evidence shows necessary condition is not met
**Action:** Redesign approach to work around constraint
**Example:** "Epic EHR integration is feasible" → Epic denies API access → Pivot to manual data entry or partner with Epic-certified vendor

### Multiple Low Confidence After Validation Attempts
**Trigger:** After reasonable validation effort, confidence remains Low
**Action:** Reassess hypothesis quality or validation method
**Example:** Cannot get access to interview rural physicians → Pivot to secondary research or find alternative validation path

---

## Reporting for Gate A

### Hypothesis Summary by Proof Area

| Proof Area | Critical Hyp (High Conf) | Critical Hyp (Med Conf) | Critical Hyp (Low Conf) | Enabling Hyp (Any Conf) | Optimization Hyp |
|------------|--------------------------|-------------------------|-------------------------|-------------------------|------------------|
| Legitimacy | [#] | [#] | [#] | [#] | [#] |
| Desirability | [#] | [#] | [#] | [#] | [#] |
| Acceptability | [#] | [#] | [#] | [#] | [#] |
| Feasibility | [#] | [#] | [#] | [#] | [#] |
| Viability | [#] | [#] | [#] | [#] | [#] |

### Validation Progress

| Status | Count | % of Total |
|--------|-------|------------|
| Validated | [#] | [%] |
| In Progress | [#] | [%] |
| Open | [#] | [%] |
| Invalidated | [#] | [%] |

**Readiness Score:** [# High Confidence Critical Hypotheses / Total Critical Hypotheses] × 100 = [%]

**Gate A Recommendation:**
- **GO:** ≥80% of critical hypotheses at High or Medium confidence
- **PIVOT:** ≥1 critical hypothesis invalidated
- **STOP:** <50% of critical hypotheses at Medium+ confidence after reasonable validation effort

---

## Integration with VIANEO Steps

**After Step 0 (Executive Brief):**
- Generate initial hypotheses from B1-B7 sections
- Flag assumptions in maturity stage classification
- All claims without evidence become hypotheses

**After Step 2 (40Q Diagnostic):**
- Scores 1-2 with INSUFFICIENT DATA become hypotheses
- Claims in "Questions to Ask Founders" become validation targets
- Red flags become critical hypotheses to validate or invalidate

**During Steps 3-5 (Market Maturity + Deep Dives):**
- Each question is a hypothesis test
- Evidence collected upgrades confidence
- Low scores trigger new hypotheses or pivots

**At Gate A:**
- Review all hypotheses
- Check critical hypothesis confidence levels
- Decide go/pivot/stop
- Update validation plans for remaining Low confidence hypotheses

**Post-Gate A (if Go):**
- Continue validating enabling and optimization hypotheses
- Track during build and pilot phases
- Update Evidence Log with pilot results
- Use for scale/no-scale decision at next gate

---

## Quality Checks

**Weekly Hypothesis Review:**
- [ ] All critical hypotheses identified
- [ ] Validation methods are specific and executable
- [ ] Target evidence is clear and measurable
- [ ] Owners and due dates assigned
- [ ] Status is current (updated within 7 days)
- [ ] Evidence IDs linked where validation occurred

**Before Gate A:**
- [ ] All critical hypotheses at Medium or High confidence, OR
- [ ] Low confidence critical hypotheses have near-term validation plans with budget
- [ ] No invalidated critical hypotheses without pivot plan
- [ ] Hypothesis log reviewed with full team
- [ ] Decision brief references hypothesis log

---

## Common Pitfalls

**❌ Pitfall: Vague hypothesis**
- Bad: "Customers will like the product"
- Good: "Rural clinic physicians will rate satisfaction ≥4/5 after using product for 30 days"

**❌ Pitfall: No validation method**
- Bad: Hypothesis listed but no way to test it
- Good: Specific method (interviews, prototype, pilot) with target evidence defined

**❌ Pitfall: Validation method is too slow/expensive**
- Bad: "Build full product and launch to market" as validation for desirability hypothesis
- Good: "Prototype test with 10 users" before building full product

**❌ Pitfall: Not updating confidence as evidence accumulates**
- Bad: Hypothesis stays "Low confidence" even after 20 validating interviews
- Good: Upgrade to "Medium" after 10, "High" after 20 with triangulation

**❌ Pitfall: Treating invalidated hypotheses as failures**
- Bad: Hide or ignore evidence that disproves hypothesis
- Good: Pivot quickly when hypothesis invalidated - it's a learning, not a failure

---

## File Naming Convention

**Hypotheses Log:**
- `[ProjectName]_[Date]_Hypotheses_Log.md`
- `[ProjectName]_[Date]_Hypotheses_Log.xlsx` (for large projects with many hypotheses)

**Example:**
- `RuralHealthAI_2025-01-15_Hypotheses_Log.md`

---

**Template Version:** 1.0
**Last Updated:** 2025-01-15
**Compatible with:** VIANEO 8-Step Evaluation System, Evidence Log Template
**Purpose:** Transform assumptions into testable hypotheses with explicit validation plans
