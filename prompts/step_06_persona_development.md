# STEP 6: Persona Development

**Time Required:** 60-90 minutes (with interviews) or 20-30 minutes (from existing data)
**Output:** Professional DOCX persona document (3-11 pages) with validation badges
**Weight in VIANEO Score:** Supports Desirability dimension (25% of overall evaluation)

---

## Overview

The Persona Development step creates evidence-based user personas that validate the Desirability dimension by documenting:

1. **WHO** are the specific users? (3-5 distinct personas with behavioral depth)
2. **WHAT** drives their decisions? (Motivations, values, current context)
3. **WHY** do current solutions fail them? (Specific gaps and pain points)
4. **HOW VALIDATED** are these personas? (Interview counts and evidence levels)

**Philosophy:** Generic market segments aren't enough for investment decisions. Committee members need to see that you've talked to real people, understood their specific contexts, and validated that your solution addresses their actual needs. This framework transforms interview data into committee-ready persona documentation.

---

## Why Persona Development Matters

Persona development bridges the gap between:
- **Step 5 (Needs/Requesters):** Identifies WHAT needs exist and WHO has them (role-based)
- **Step 7 (Needs Qualification Matrix):** Prioritizes needs by importance and satisfaction
- **Step 8-9 (Ecosystem):** Maps stakeholders and network positioning

**Personas add the human depth:**
- Real behavioral context (not just demographics)
- Validated pain points (not just assumptions)
- Current solution analysis (why alternatives fail)
- Decision-making factors (values and constraints)

**Impact on Scoring:**
- **5 points (Exceptional):** 10+ interviews per persona, comprehensive behavioral detail
- **4 points (Strong):** 5-10 interviews per persona, solid validation
- **3 points (Adequate):** 3-5 interviews per persona (minimum acceptable)
- **2 points (Weak):** 1-2 interviews only, limited evidence
- **1 point (Insufficient):** No validation, hypothetical personas

---

## Required Inputs

**From Previous Steps:**
- **Step 5:** Requesters table (6-10 roles) - personas represent segments from this list
- **Step 4:** Legitimacy assessment - problem context and field of application
- **Step 3:** Market maturity scores - Desirability dimension baseline
- **Step 0:** Executive brief - target market and validation status

**Research Data (CRITICAL):**
- Customer discovery interview transcripts or detailed notes
- Interview count per segment (MUST document)
- Interview dates and participant roles
- Key quotes, behavioral observations, quantified impacts
- Current tools/solutions mentioned by interviewees

**Minimum Requirements:**
- 3 interviews per persona segment (adequate validation)
- 5+ interviews per persona (recommended for strong validation)
- 10+ interviews per persona (exceptional validation)

---

## Instructions for AI Assistant

Create evidence-based user personas from the provided interview data and research. For each persona:

1. **Create 3-5 distinct personas** representing key requester segments from Step 5
2. **Document validation status** with interview counts and date ranges (use colored badges)
3. **Complete all persona fields**: First name, Age, Life/Motivations, Personality/Values, Field of Application details
4. **List Activities and Challenges**: 4-6 Tasks, 4-6 Pains, 4-6 Expectations (60-char limit each)
5. **Describe Current Solutions** they use and why they fail (2-3 sentences)
6. **Apply validation badges**: Green (5+ interviews), Orange (1-4 interviews), Red (0 interviews)
7. **Generate professional DOCX** (3-11 pages) with Cover Page, Evidence Base Summary, and Individual Personas
8. **Flag personas requiring additional validation** and recommend interview targets

---

## Comprehensive Documentation System

This step uses a **three-document system** for complete guidance:

### 1. VIANEO_Persona_Development_Skill.md
**Purpose:** Master reference guide
**Location:** `docs/VIANEO_Persona_Development_Skill.md`
**Read this for:**
- Understanding purpose and when to use personas
- Output specifications (page limits, file format)
- Evidence requirements and validation levels
- Complete persona structure overview
- Quality standards and success criteria
- Integration with other VIANEO dimensions

### 2. VIANEO_Persona_Generation_Prompt.md
**Purpose:** Exact template with step-by-step formatting
**Location:** `docs/VIANEO_Persona_Generation_Prompt.md`
**Read this for:**
- Cover page template
- Evidence base page template
- Individual persona structure (exact fields)
- Character limit strategies
- Formatting guidelines
- Quality checklist

### 3. VIANEO_Persona_Reference_Guide.md
**Purpose:** Examples, scoring rubric, and best practices
**Location:** `docs/VIANEO_Persona_Reference_Guide.md`
**Read this for:**
- Complete example persona (annotated)
- Scoring rubric (1-5 scale) with examples
- Interview guidelines and question bank
- Common pitfalls with before/after examples
- Evidence documentation template
- Quality check questions

### 4. VIANEO_Persona_Complete_System_Guide.md
**Purpose:** Navigation guide for the three-document system
**Location:** `docs/VIANEO_Persona_Complete_System_Guide.md`
**Read this for:**
- How to use all three documents together
- Workflow recommendations
- Quick reference by use case
- Troubleshooting decision tree

---

## Output Specification: Professional DOCX

### Document Structure (Maximum 11 Pages)

**Page 1: Cover Page**
```
[Company Name]
Vianeo Business Model Evaluation
User Persona Analysis

[Subtitle describing project or domain]

Prepared: [Month Year]
Validation Status: [X personas based on Y total interviews]
Evaluation Phase: Desirability Assessment
```

**Page 2: Evidence Base Summary**
- Introductory paragraph (research approach, total interviews, methodology)
- Validation breakdown table (persona, interview count, date range, status)
- Critical gaps and next steps paragraph

**Pages 3-7+ (up to page 11): Individual Personas**
Each persona on a new page with:
1. Validation status badge (colored table: Green/Orange/Red)
2. Requester section (First name, Age, Life/Motivations, Personality/Values)
3. Field of Application (Thinks/Feels, Observes, Does, Others Say)
4. Activities and Challenges (Tasks, Pains, Expectations - all 4-6 bullets, max 60 chars each)
5. Current Solutions (2-3 sentences naming specific tools and gaps)

### Validation Badge Colors

**✓ VALIDATED (Green)**
- Background: #E8F4EA, Text: #2D7A3E
- Criteria: 5+ formal interviews
- Example: "✓ VALIDATED (8 interviews conducted October-November 2024)"

**⚠ PARTIALLY VALIDATED (Orange)**
- Background: #FFF4E6, Text: #CC7A00
- Criteria: 1-4 interviews OR beta user engagement
- Example: "⚠ PARTIALLY VALIDATED (3 interviews, 2-3 additional recommended)"

**✗ NEEDS VALIDATION (Red)**
- Background: #FFEBEE, Text: #C62828
- Criteria: 0 formal interviews
- Example: "✗ NEEDS VALIDATION (0 interviews, 10-15 needed for B2B segment)"

---

## Critical Requirements

### Character Limits (STRICTLY ENFORCED)

| Field | Limit | Notes |
|-------|-------|-------|
| All bullet points | 60 chars | Tasks, Pains, Expectations |
| First name | Single name | No middle initials |
| Age | Specific number | Not a range (e.g., "42" not "40-45") |
| Text paragraphs | 2-3 sentences | Each section's paragraph content |

**Validation Tip:** Use character count tool. If over 60 characters:
1. Remove adjectives first
2. Use numbers instead of words ("12-15 hours" vs. "significant time")
3. Abbreviate universally understood terms ("RFPs" vs. "requests for proposals")
4. Front-load key information

### Evidence Quality Standards

**For Score of 3 (Minimum Acceptable):**
- 3-5 interviews per persona
- Basic behavioral information
- Personas somewhat distinct
- Current solutions mentioned
- Pain points identified

**For Score of 4 (Strong):**
- 5-10 interviews per persona
- Good behavioral detail
- Clear distinction between personas
- Current solutions with gap analysis
- Pain points specific and measurable

**For Score of 5 (Exceptional):**
- 10+ interviews per persona
- Direct quotes and behavioral observations
- Each persona completely unique
- Detailed current solution analysis with pricing
- All pain points quantified (time, cost, frequency)

---

## Workflow

### Phase 1: Preparation (15 minutes)
1. Read `docs/VIANEO_Persona_Development_Skill.md` completely
2. Review `docs/VIANEO_Persona_Generation_Prompt.md` for template
3. Skim `docs/VIANEO_Persona_Reference_Guide.md` for examples
4. Gather interview data and evidence

### Phase 2: Evidence Review (15-20 minutes)
1. Document interview metadata (dates, roles, organizations)
2. Extract key quotes, behaviors, pain points
3. Identify patterns across interviews
4. Map distinct user segments (aim for 3-5 personas)
5. Assign validation levels based on interview counts

### Phase 3: Persona Creation (30-40 minutes)
1. Use `VIANEO_Persona_Generation_Prompt.md` as working template
2. Draft each persona following exact structure
3. Validate character counts for all bullets (max 60 chars)
4. Verify 2-3 sentence requirements for paragraphs
5. Name specific current solutions with gaps
6. Assign appropriate validation badge

### Phase 4: Document Generation (10-15 minutes)
1. Create cover page with company name
2. Build evidence base page with interview breakdown
3. Generate each persona on new page with badge
4. Apply consistent styling and spacing
5. Export to DOCX with proper formatting

### Phase 5: Quality Assurance (10-15 minutes)
1. Use quality checklist from Generation Prompt
2. Apply scoring rubric from Reference Guide
3. Answer quality check questions
4. Make final refinements
5. Verify maximum 11 pages

---

## Integration with VIANEO Framework

### Connection to Other Steps

**Legitimacy (Step 4):**
- Personas validate that problem statement addresses real user needs
- Evidence from personas confirms problem significance
- User quotes support problem discovery narrative

**Needs/Requesters (Step 5):**
- Personas represent specific segments from Requesters table
- Persona needs align with 10 needs identified in Step 5
- Personas add behavioral depth to role-based analysis

**Needs Qualification Matrix (Step 7):**
- Personas inform importance ratings (how critical each need is)
- Persona segments become columns in matrix
- Current solution gaps drive satisfaction ratings

**Ecosystem Mapping (Steps 8-9):**
- Personas map to requester segments in ecosystem
- Persona decision factors inform stakeholder influence
- Persona needs drive value network positioning

### Dimension Scoring Impact

**Desirability (25% of total):** Direct impact
- Exceptional personas (10+ interviews): 5 points
- Strong personas (5-10 interviews): 4 points
- Adequate personas (3-5 interviews): 3 points
- Weak personas (1-2 interviews): 2 points
- No validation: 1 point

**Legitimacy (15%):** Indirect support
- Personas validate problem significance
- User quotes confirm problem existence

**Acceptability (20%):** Indirect support
- Personas identify stakeholder segments
- Decision factors inform ecosystem strategy

**Feasibility (20%):** Indirect support
- Persona needs drive functionality requirements
- Current workflows shape implementation priorities

**Viability (20%):** Indirect support
- Persona pain points validate value proposition
- Current solution costs inform pricing strategy
- Evidence of willingness to pay

---

## Common Pitfalls (See Reference Guide for Details)

### Pitfall 1: Generic Personas
**Problem:** "John is a 25-45 year old professional who wants better tools"
**Solution:** Specific age, role, context, quantified behaviors

### Pitfall 2: Solution-First Thinking
**Problem:** "Sarah needs our AI-powered analytics dashboard"
**Solution:** Document actual problem, current workarounds, gaps

### Pitfall 3: Overlapping Personas
**Problem:** Multiple personas with same needs, different titles
**Solution:** Find what makes them distinct or combine them

### Pitfall 4: Character Limit Violations
**Problem:** Bullets over 60 characters break platform requirements
**Solution:** See character limit strategies in Generation Prompt

### Pitfall 5: Missing Current Solutions
**Problem:** "Uses various tools that don't work well"
**Solution:** Name 2-4 specific tools with pricing and gap analysis

---

## Success Criteria

A successful persona document:
- ✓ Based on documented interviews (minimum 3 per persona)
- ✓ Each persona is distinct with unique needs
- ✓ All bullets under 60 characters (verified)
- ✓ All paragraphs are 2-3 sentences
- ✓ Current solutions specifically named with gaps identified
- ✓ Validation badge matches evidence level
- ✓ Professional formatting ready for committee presentation
- ✓ Maximum 11 pages including cover and evidence base

---

## Output File Naming

Save completed personas to:
```
/mnt/user-data/outputs/[CompanyName]_Vianeo_Personas_Professional.docx
```

Example: `/mnt/user-data/outputs/Thinkie_Vianeo_Personas_Professional.docx`

---

## AI Execution Instructions

When executing this step with AI assistance:

```
"Execute VIANEO Step 6: Persona Development

Use interview data from [source] covering [X] interviews across [Y] segments.

Create professional DOCX with:
- 3-5 evidence-based personas
- Validation badges matching interview counts
- All bullets under 60 characters
- Current solutions specifically named

Follow complete documentation in:
- docs/VIANEO_Persona_Development_Skill.md
- docs/VIANEO_Persona_Generation_Prompt.md
- docs/VIANEO_Persona_Reference_Guide.md"
```

---

## Next Steps After Completion

**Immediate:**
1. Review personas with project team for accuracy
2. Identify validation gaps requiring additional interviews
3. Use personas to inform Step 7 (Needs Qualification Matrix)

**Within 30 Days:**
4. Conduct additional interviews to strengthen weak personas
5. Update personas with new evidence
6. Validate persona accuracy with actual user behavior

**Ongoing:**
7. Reference personas in feature prioritization decisions
8. Update personas as market evolves
9. Use personas in marketing messaging and positioning

---

## Quality Gates

Before proceeding to Step 7, verify:

- [ ] Minimum 3 personas created (maximum 5)
- [ ] At least 3 interviews per persona (9-15 total minimum)
- [ ] All bullets verified under 60 characters
- [ ] All paragraphs are 2-3 sentences
- [ ] Current solutions named with specific gaps
- [ ] Validation badges match evidence levels
- [ ] Professional DOCX generated
- [ ] Total page count ≤ 11 pages
- [ ] Each persona is distinct (no significant overlap)
- [ ] Could support funding decision if presented to committee

---

## References

**Complete Documentation:**
- Master Guide: `docs/VIANEO_Persona_Development_Skill.md`
- Template & Format: `docs/VIANEO_Persona_Generation_Prompt.md`
- Examples & Best Practices: `docs/VIANEO_Persona_Reference_Guide.md`
- System Navigation: `docs/VIANEO_Persona_Complete_System_Guide.md`

**Related Steps:**
- Previous: `prompts/step_05_needs_requesters.md`
- Next: `prompts/step_07_needs_qualification_matrix.md`

**Templates:**
- Persona templates are embedded in Generation Prompt document
- DOCX formatting specifications included in all guides

---

**Version:** 1.0
**Framework:** VIANEO Business Model Evaluation Methodology
**Last Updated:** November 2025
**Part of:** Complete 9-Step Evaluation System
