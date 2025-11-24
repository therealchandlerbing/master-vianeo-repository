# Evidence Log: [Project Name]

**Project:** [Name]
**Date Range:** [Start] to [Current]
**Owner:** [Name]
**Last Updated:** [YYYY-MM-DD]

---

## Purpose

The Evidence Log provides **traceability from every claim to its source**. It ensures that assertions in assessments are grounded in external validation, not assumptions. This is the single source of truth for what is known, how it is known, and what confidence level to assign.

**Key Principle:** If it's not in the Evidence Log with a source, it's unverified.

---

## Evidence Reliability Levels

| Level | Name | Description | Examples |
|-------|------|-------------|----------|
| **L1** | Internal Assertion | Team member belief or assumption, no external source | "We think customers need X" |
| **L2** | Team Corroboration | Multiple team members agree based on experience | "Based on our 5 years in this industry" |
| **L3** | External Validated | Direct evidence from primary sources outside the team | Interview transcripts, published research, signed LOIs |

**Decision Rule:** Only use **L3 (External Validated)** evidence for Gate A decisions and scoring ≥3 in assessments.

---

## Evidence Log Entries

| ID | Claim/Insight | Source Type | Source Detail | Evidence Excerpt | Confidence | Validation Plan | Owner | Due Date |
|----|---------------|-------------|---------------|------------------|------------|-----------------|-------|----------|
| E001 | [Specific claim or insight] | [Interview / Research / Document / Survey / LOI / Pilot Data] | [Interview ID or URL or Document name] | [Verbatim quote or data point] | [L1/L2/L3] | [How to validate if L1/L2, or "Validated" if L3] | [Name] | [Date] |
| E002 | | | | | | | | |
| E003 | | | | | | | | |

---

## Example Entries

| ID | Claim/Insight | Source Type | Source Detail | Evidence Excerpt | Confidence | Validation Plan | Owner | Due Date |
|----|---------------|-------------|---------------|------------------|------------|-----------------|-------|----------|
| E001 | Rural clinic physicians lack timely specialist access | Interview | INT-045 (Dr. Sarah Chen, Rural Health Clinic) | "We wait 2-3 weeks for any specialist consultation. By then the patient's condition has often worsened." | L3 | Validated | John | ✓ |
| E002 | 35% misdiagnosis rate for complex conditions | Research | Published AMA study (2023) - Link: [URL] | "Rural facilities show 35% higher misdiagnosis rates for conditions requiring specialist input" (p. 47) | L3 | Validated | Sarah | ✓ |
| E003 | Pricing range $200-400/month acceptable | Interview | INT-051, INT-053, INT-058 (3 clinic directors) | "Between $200-400 per month would be reasonable if it reduces malpractice risk" (INT-051) | L3 | Validated | Mike | ✓ |
| E004 | Market size: 12,000 rural clinics in US | Research | HRSA Data Warehouse 2024 - Link: [URL] | "12,147 rural health clinics certified as of Q1 2024" (Table 3.2) | L3 | Validated | John | ✓ |
| E005 | Team has 15 years combined domain expertise | Team Corroboration | Founder CVs | Founder 1: 8 yrs rural health, Founder 2: 7 yrs telemedicine | L2 | Validate with external references | Sarah | 2025-02-01 |
| E006 | Competitors charge $500-1000/month | Internal Assertion | Competitor website review | Pricing pages show $500 base tier | L2 | Validate with customer interviews | Mike | 2025-01-20 |

---

## Source Type Definitions

### Primary Sources (Preferred for L3)

**Interview**
- Format: INT-### (sequential numbering)
- Metadata: Date, duration, interviewee role, organization type, location
- Storage: Transcript or detailed notes with consent documentation
- Quote Format: Always include speaker context and verbatim quote

**Survey/Questionnaire**
- Format: SURV-### with sample size and response rate
- Metadata: Distribution method, date range, demographics
- Storage: Raw data + analysis summary
- Data Format: Quantitative results with confidence intervals

**Document/Contract**
- Format: DOC-###
- Types: LOIs, MOUs, contracts, signed commitments, official reports
- Metadata: Date, parties, binding vs. non-binding status
- Storage: Scanned copy with signatures redacted for privacy

**Pilot/Test Data**
- Format: PILOT-### with test name and period
- Types: Usage data, performance metrics, user feedback, A/B test results
- Metadata: Test design, sample size, duration, controls
- Storage: Anonymized dataset + analysis

**Published Research**
- Format: RESEARCH-### with citation
- Types: Academic papers, industry reports, government statistics
- Metadata: Publication date, peer-review status, sample size
- Citation: Full citation with DOI or stable URL
- Storage: PDF + relevant excerpts highlighted

### Secondary Sources (Use with caution, typically L1-L2)

**News/Media**
- Format: NEWS-###
- Use: Market context, competitor announcements, trend signals
- Limitation: Often not verified, may be promotional
- Validation: Confirm with primary sources

**Competitor Websites/Marketing**
- Format: COMP-###
- Use: Feature comparison, pricing benchmarks, positioning
- Limitation: Self-reported, may be outdated or aspirational
- Validation: Confirm with customer interviews who use competitors

**Internal Analysis**
- Format: INTERNAL-###
- Use: Hypotheses generation, desk research synthesis
- Limitation: Team assumptions, no external validation
- Validation: Design experiments or interviews to validate

---

## Evidence Collection Workflow

### 1. Pre-Interview/Research
- Assign Evidence ID (E###)
- Define claim or question to investigate
- Select source type and identify specific sources
- Prepare interview guide or research query

### 2. During Interview/Research
- Record consent (verbal or written)
- Capture verbatim quotes with context
- Note body language, tone, emphasis
- Ask for examples, specifics, numbers
- Request documentation or references

### 3. Post-Interview/Research
- Transcribe or summarize within 24 hours
- Extract key claims with Evidence IDs
- Assign confidence level (L1/L2/L3)
- Link to related Evidence IDs
- Update Evidence Log

### 4. Validation Planning
- For L1/L2 evidence: Design validation method
- Set due date and owner
- Track status in Evidence Log
- Update confidence as validation progresses

---

## Traceability Requirements

**For Every Assessment Score:**
- Scores 1-2: Note what evidence is missing
- Scores 3: Cite at least 1 L3 evidence ID
- Scores 4: Cite 2-3 L3 evidence IDs
- Scores 5: Cite 3+ L3 evidence IDs from multiple sources

**For Executive Brief (Step 0):**
- B2 Problem Statement: Minimum 2 L3 evidence IDs
- B4 Market Size: Minimum 1 L3 evidence ID (research or data)
- B6 Traction: All metrics must have L3 evidence IDs
- B7 Team: L2 acceptable (CVs, LinkedIn) unless external references available

**For Gate A Decision:**
- Every hypothesis must cite evidence
- Confidence score must match evidence level
- Validation plan required for all L1/L2 evidence used

---

## Ethics and Privacy

**Interview Consent:**
- [ ] Verbal or written consent obtained before recording
- [ ] Purpose of interview explained
- [ ] Confidentiality terms stated
- [ ] Right to withdraw explained
- [ ] Recording/notes permission granted

**Data Protection:**
- Store transcripts with access controls
- Redact personally identifiable information in shared reports
- Use role-based anonymization (e.g., "Clinic Director A" instead of name)
- Keep signed consent forms separate from transcripts
- Set retention period and deletion policy

**Quote Usage:**
- Always provide context (role, not name)
- Check if quote can be attributed or must be anonymized
- Avoid quotes that could identify speaker by circumstance
- Get approval for external publication of quotes

---

## Quality Checks

**Weekly Evidence Review:**
- [ ] All evidence IDs have complete entries
- [ ] Sources are specific and retrievable
- [ ] Verbatim quotes are accurate
- [ ] Confidence levels match evidence quality
- [ ] Validation plans have owners and due dates
- [ ] No orphaned claims (claims without evidence IDs)

**Before Gate A Decision:**
- [ ] All critical hypotheses have L3 evidence
- [ ] Evidence triangulation (multiple sources for key claims)
- [ ] No invented or assumed data points
- [ ] All interview consents documented
- [ ] Privacy requirements met

---

## Common Pitfalls

**❌ Pitfall: "We believe customers need X"**
- Problem: Internal assertion (L1) presented as fact
- Fix: Add Evidence ID with "L1 - Internal Assertion" and validation plan

**❌ Pitfall: Citing competitor websites as proof of market size**
- Problem: Marketing claims are not validated market data
- Fix: Find published research or conduct primary interviews

**❌ Pitfall: Invented statistics**
- Problem: "Studies show 80% of users..." without citation
- Fix: Remove claim or find actual study with Evidence ID

**❌ Pitfall: Stale evidence**
- Problem: Interview from 18 months ago used for current decision
- Fix: Note date and validate if still current

**❌ Pitfall: No validation plan for L1/L2 evidence**
- Problem: Assumptions remain unvalidated
- Fix: Design experiments or interviews with due dates

---

## Integration with VIANEO Steps

**Step 0 (Executive Brief):**
- Evidence Log IDs cited in B2, B4, B6
- Maturity stage justified with evidence

**Step 2 (40-Question Diagnostic):**
- Every score ≥3 requires Evidence Log citations
- INSUFFICIENT DATA triggers new Evidence Log entry with validation plan

**Step 3 (Market Maturity 29Q):**
- Each question scored with confidence based on evidence level
- Low confidence scores trigger validation requirements

**Step 4 (Legitimacy Deep Dive):**
- Problem validation requires multiple Evidence IDs
- Counterfactual analysis requires evidence

**Step 5 (Desirability):**
- Interview notes become Evidence Log entries
- Needs validation requires Evidence IDs

**Gate A Decision:**
- All hypotheses reference Evidence Log
- Decision brief shows evidence completeness

---

## Reporting

**Evidence Summary for Committee:**

| Proof Area | L3 Evidence Count | L2 Evidence Count | L1 Evidence Count | Validation Gap |
|------------|-------------------|-------------------|-------------------|----------------|
| Legitimacy | [#] | [#] | [#] | [Critical gaps] |
| Desirability | [#] | [#] | [#] | [Critical gaps] |
| Acceptability | [#] | [#] | [#] | [Critical gaps] |
| Feasibility | [#] | [#] | [#] | [Critical gaps] |
| Viability | [#] | [#] | [#] | [Critical gaps] |

**Evidence Quality Score:** [L3 count / Total entries] × 100 = [%]

**Target:** ≥70% L3 evidence before Gate A decision

---

## File Naming Convention

**Evidence Log:**
- `[ProjectName]_[Date]_Evidence_Log.md`
- `[ProjectName]_[Date]_Evidence_Log.xlsx` (for large projects)

**Interview Transcripts:**
- `INT-###_[Role]_[Date]_Transcript.md`
- Example: `INT-045_ClinicDirector_2025-01-15_Transcript.md`

**Supporting Documents:**
- `DOC-###_[Type]_[Date].pdf`
- Example: `DOC-012_LOI_2025-01-10.pdf`

---

**Template Version:** 1.0
**Last Updated:** 2025-01-15
**Compatible with:** VIANEO 13-Step Evaluation System
**Purpose:** Ensure traceability from every claim to validated sources
