# Vianeo Persona Development Skill

## Purpose

This skill guides the creation of evidence-based user personas for Vianeo Business Model Evaluation, specifically validating the **Desirability dimension (25% of total score)**. The skill produces professional DOCX persona documents that demonstrate validated user needs, behaviors, and pain points required for committee evaluation.

## When to Use This Skill

Use this skill when:
- Evaluating innovation projects through the Vianeo framework
- Documenting user research for Desirability assessment
- Creating personas based on actual interviews (minimum 3 per segment)
- Producing committee-ready documentation for funding decisions
- Supporting startup accelerators, research institutions, or innovation programs

## Output Specifications

**Document Structure:**
- **Page 1:** Cover page with company name and validation metadata
- **Page 2:** Evidence base summary with interview breakdown
- **Pages 3-7+:** Individual personas (1 per page, 3-5 personas recommended)
- **Maximum:** 11 pages total including cover

**File Format:**
- Professional DOCX with custom styles
- Color-coded validation badges
- Consistent typography and spacing
- Ready for committee presentation

## Evidence Requirements

### Validation Levels

**✓ VALIDATED (Green Badge)**
- **Criteria:** 5+ formal interviews conducted per persona
- **Badge Color:** Background #E8F4EA, Text #2D7A3E
- **Use When:** Strong evidence base with documented research

**⚠ PARTIALLY VALIDATED (Orange Badge)**
- **Criteria:** 1-4 interviews OR beta user engagement without formal interviews
- **Badge Color:** Background #FFF4E6, Text #CC7A00
- **Use When:** Preliminary validation with gaps identified

**✗ NEEDS VALIDATION (Red Badge)**
- **Criteria:** 0 interviews, hypothesis only
- **Badge Color:** Background #FFEBEE, Text #C62828
- **Use When:** Documenting gaps and research needs

### Interview Guidelines

**Minimum Standards:**
- 3-5 interviews per persona segment (bare minimum)
- 5+ interviews per persona (recommended for strong validation)
- 10-15 interviews for complex B2B personas
- Document interview dates, participant roles, key quotes

**What Counts as an Interview:**
- One-on-one structured conversations (30+ minutes)
- User observation sessions with follow-up questions
- Focus groups with detailed notes per participant
- Beta user feedback sessions with documented responses

**What Does NOT Count:**
- Survey responses without follow-up
- Casual conversations without structure
- Secondary research or market reports
- Internal team assumptions

## Persona Structure Requirements

Each persona MUST include all sections with exact formatting:

### Section 1: Requester
- **First name:** Single first name only (e.g., "Marcus", not "Marcus J.")
- **Age:** Specific age number (e.g., 42, not "40-45")
- **Life/Motivations:** 2-3 sentences about daily life, career, what drives them
- **Personality/Values:** 2-3 sentences about character, values, decision-making

### Section 2: Field of Application
- **Thinks/Feels:** 2-3 sentences about worries, hopes, emotional state
- **Observes:** 2-3 sentences about what they see, trends, patterns
- **Does:** 2-3 sentences about actual behaviors, habits, actions
- **Others Say:** 2-3 sentences about feedback, reputation, how others view them

### Section 3: Activities and Challenges
- **Tasks/Activities:** 4-6 bullets, each under 60 characters
- **Pains/Lacks:** 4-6 bullets, each under 60 characters
- **Expectations/Hopes:** 4-6 bullets, each under 60 characters

### Section 4: Current Solutions
- **Paragraph:** 2-3 sentences describing actual tools used, why inadequate, gaps

## Character Limits

**CRITICAL:** These limits match Vianeo platform requirements:

| Field | Limit | Notes |
|-------|-------|-------|
| All bullet points | 60 chars | For Tasks, Pains, Expectations |
| First name | Single name | No middle initials |
| Age | Specific number | Not a range |
| Text paragraphs | 2-3 sentences | Each section's paragraph content |

**Validation Tip:** Each bullet should be concise, specific, and measurable. If over 60 characters, remove adjectives first, then use abbreviations if universally understood.

## Quality Standards

### Evidence-Based Content
- Every claim supported by interview data
- Direct quotes available (even if not shown in final doc)
- Behavioral specifics, not demographics only
- Actual tools and workarounds named specifically

### Persona Distinctiveness
- Each persona addresses different needs or contexts
- No significant overlap between personas
- Clear segmentation criteria
- Test: Could you satisfy one persona's needs without satisfying another's?

### Behavioral Depth
- Specific actions described (not generic behaviors)
- Current workflows documented with tools named
- Pain points quantified where possible (hours, dollars, frequency)
- Realistic and relatable to actual people

## Workflow

### Phase 1: Research & Evidence Gathering
1. Conduct minimum 3-5 interviews per planned persona
2. Document interview metadata (dates, roles, organizations)
3. Extract key quotes, behaviors, pain points
4. Identify patterns across interviews
5. Map distinct user segments

### Phase 2: Persona Development
1. Read this SKILL.md completely
2. Read PERSONA_GENERATION_PROMPT.md for detailed format
3. Read PERSONA_REFERENCE_GUIDE.md for examples and guidance
4. Draft personas following exact structure
5. Validate character counts for all bullets
6. Verify 2-3 sentence requirements for paragraphs

### Phase 3: Document Generation
1. Create cover page with company name and subtitle
2. Build evidence base page with interview breakdown
3. Generate each persona on new page with status badge
4. Apply consistent styling and spacing
5. Export to DOCX with proper formatting

### Phase 4: Quality Check
1. Verify all personas start on new pages
2. Check validation badges match evidence level
3. Confirm all bullets under 60 characters
4. Validate 2-3 sentences in all paragraph sections
5. Ensure distinct, non-overlapping personas
6. Review against scoring rubric (see PERSONA_REFERENCE_GUIDE.md)

## DOCX Styling Specifications

### Typography
- **Headers:** Calibri or Arial, 18pt bold for section headers
- **Field Labels:** 12pt bold for "First name:", "Age:", etc.
- **Body Text:** 11pt regular for paragraph content
- **Bullets:** 11pt with standard bullet formatting

### Spacing
- **Between Sections:** 1 blank line (12pt spacing)
- **After Field Labels:** 6pt spacing before content
- **After Paragraphs:** 12pt spacing after
- **Page Breaks:** Before each new persona

### Status Badge Table
```javascript
// Full-width table, single cell, centered text
columnWidths: [9360] // Full page width
margins: { top: 180, bottom: 180, left: 240, right: 240 }
alignment: CENTER
bold: true
size: 24pt
```

**Badge Colors by Validation Level:**
- Validated: Fill #E8F4EA, Text #2D7A3E, Symbol ✓
- Partial: Fill #FFF4E6, Text #CC7A00, Symbol ⚠
- Needs: Fill #FFEBEE, Text #C62828, Symbol ✗

## Integration with Vianeo Framework

### Scoring Impact
Personas directly impact Desirability scoring (25% of total evaluation):
- **5 points:** Exceptional personas with 10+ interviews each, comprehensive validation
- **4 points:** Strong personas with 5-10 interviews each, good behavioral detail
- **3 points:** Adequate personas with 3-5 interviews each, basic validation
- **2 points:** Weak personas with 1-2 interviews, limited evidence
- **1 point:** No validation, hypothetical personas only

### Connection to Other Dimensions
- **Legitimacy:** Personas validate that problem statement addresses real user needs
- **Acceptability:** Personas inform ecosystem player identification and requester segments
- **Feasibility:** Personas drive functionality requirements from actual user needs
- **Viability:** Personas validate value proposition and willingness to pay

## Common Pitfalls

### Pitfall 1: Generic Personas
**Problem:** "John is a 25-45 year old professional who wants better tools"
**Solution:** "Marcus, 42, runs a solo grant writing consultancy serving 8-12 nonprofits..."

### Pitfall 2: Solution-First Thinking
**Problem:** "Sarah needs our AI-powered analytics dashboard"
**Solution:** "Sarah needs real-time project profitability visibility, currently impossible with her fragmented spreadsheet system"

### Pitfall 3: Overlapping Personas
**Problem:** Persona A and B both need "project management tools" with same context
**Solution:** Combine them or find what makes them truly distinct (different workflows, different constraints)

### Pitfall 4: Character Limit Violations
**Problem:** "● Spending significant time on repetitive proposal sections" (94 chars)
**Solution:** "● 12-15 hours per proposal on repetitive sections" (51 chars)

### Pitfall 5: Missing Current Solutions
**Problem:** "Uses various tools but they don't work well"
**Solution:** "Uses Microsoft Word with manual template library, Asana for tracking, and Google Sheets for status, requiring constant context-switching without AI assistance"

## Files in This Skill

1. **SKILL.md** (this file): Master reference for skill usage
2. **PERSONA_GENERATION_PROMPT.md**: Detailed prompt for persona creation
3. **PERSONA_REFERENCE_GUIDE.md**: Comprehensive guide with examples and scoring

## Output Location

Save completed personas to:
```
/mnt/user-data/outputs/[CompanyName]_Vianeo_Personas_Professional.docx
```

Example: `/mnt/user-data/outputs/Thinkie_Vianeo_Personas_Professional.docx`

## Success Criteria

A successful persona document:
- ✓ Based on documented interviews (minimum 3 per persona)
- ✓ Each persona is distinct with unique needs
- ✓ All bullets under 60 characters
- ✓ All paragraphs are 2-3 sentences
- ✓ Current solutions specifically named with gaps identified
- ✓ Validation badge matches evidence level
- ✓ Professional formatting ready for committee presentation
- ✓ Maximum 11 pages including cover and evidence base

## Next Steps

1. **Read PERSONA_GENERATION_PROMPT.md** for exact template and format instructions
2. **Read PERSONA_REFERENCE_GUIDE.md** for detailed examples and best practices
3. Gather interview data and evidence
4. Draft personas following the template precisely
5. Generate professional DOCX with correct styling
6. Validate against quality checklist

---

**Version:** 1.0
**Last Updated:** November 2025
**Part of:** Vianeo Business Model Evaluation Playbook
**Dimension:** Desirability Assessment (25% of total score)
