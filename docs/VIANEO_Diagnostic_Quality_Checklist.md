# Vianeo Diagnostic Quality Checklist

## Pre-Delivery Validation

Use this checklist before delivering any Vianeo diagnostic comment. All items must be checked before presenting to user.

## Content Quality

### Executive Diagnostic Section

#### Length & Structure
- [ ] Total is 6-8 sentences across 4 paragraphs
- [ ] Strengths: 1-2 sentences
- [ ] Risks: 1-2 sentences
- [ ] Near-term Actions: 2-3 sentences
- [ ] Evidence Gaps: 1-2 sentences

#### Strengths Paragraph
- [ ] Leads with strongest validation
- [ ] Includes specific numbers (not "some" or "several")
- [ ] Names people, partners, or technologies
- [ ] Every claim backed by assessment data
- [ ] Uses evidence hierarchy (external > internal > self-reported)
- [ ] No generic statements ("team seems capable", "promising")

#### Risks Paragraph
- [ ] Identifies systemic issues (not minor gaps)
- [ ] Quantifies risks where possible
- [ ] Uses direct language (no "may", "might", "possibly")
- [ ] Prioritizes by impact (highest severity first)
- [ ] Connects to specific dimension scores
- [ ] No downplaying or hedging

#### Near-term Actions Paragraph
- [ ] Contains 3-4 specific actions
- [ ] Each action has responsible owner in parentheses
- [ ] Actions are measurable and time-bound (30-60 days)
- [ ] Uses delegation-ready language
- [ ] Addresses critical risks or capitalizes on strengths
- [ ] Owners use actual names from team data

#### Evidence Gaps Paragraph
- [ ] Gaps are material (affect decision-making)
- [ ] Specific about what's missing (not "more research needed")
- [ ] Grouped logically by category
- [ ] Clear why each gap matters
- [ ] Different from information in Risks section
- [ ] No nitpicking or minor documentation issues

### Dimension Summary

#### Table Structure
- [ ] All 5 dimensions included (Legitimacy, Desirability, Acceptability, Feasibility, Viability)
- [ ] Scores use X.X/5 format
- [ ] Each dimension has status keyword + explanation
- [ ] Overall status statement below table

#### Score Accuracy
- [ ] Scores match source assessment data exactly
- [ ] Status keywords match score ranges:
  - 4.5-5.0 = Strong
  - 3.5-4.4 = Promising
  - 3.0-3.4 = Developing
  - 2.0-2.9 = Problematic
  - <2.0 = Non-viable

#### Interpretation Quality
- [ ] Explanations specific to this venture (not generic)
- [ ] Connected to key findings from assessment
- [ ] Brief but informative (5-10 words)
- [ ] Overall status balances strengths and weaknesses

### Critical Path Forward

#### Structure
- [ ] Immediate Priority (Weeks 1-4) - max 3 actions
- [ ] Short-term Priority (Months 2-3) - max 4 actions
- [ ] Medium-term Priority (Months 4-6) - max 4 actions
- [ ] Success Metrics - max 6 metrics

#### Action Quality
- [ ] Each action is specific and measurable
- [ ] Realistic timeframes
- [ ] Clear outcomes defined
- [ ] Addresses identified gaps or risks
- [ ] Builds on proven strengths
- [ ] Proper progression (immediate → short → medium)

#### Metrics Quality
- [ ] Specific thresholds (not "improve X")
- [ ] Measurable (can verify objectively)
- [ ] Timeframes included where applicable
- [ ] Mix of input and output metrics
- [ ] Aligned with actions in critical path

### Footer Metadata

- [ ] Assessment Methodology lists all frameworks used
- [ ] Evidence Sources lists all primary documents
- [ ] Next Review includes date and trigger event
- [ ] All three sections complete and specific

## Format Quality

### Markdown Output

#### File & Structure
- [ ] Filename: `[ProjectName]_Vianeo_Diagnostic_Comment.md`
- [ ] Saved to `/mnt/user-data/outputs/`
- [ ] Follows template structure exactly
- [ ] All required sections present in correct order

#### Formatting
- [ ] Heading levels correct (# for H1, ## for H2, ### for H3)
- [ ] Table formatted with proper markdown syntax
- [ ] Lists use correct syntax (numbered: `1.` / bullet: `-`)
- [ ] No em dashes used anywhere (use commas or parentheses)
- [ ] Bold formatting used appropriately (dimension names, emphasis)
- [ ] Line breaks and spacing consistent

### DOCX Output

#### File & Generation
- [ ] Filename: `[ProjectName]_Vianeo_Diagnostic_Comment.docx`
- [ ] Saved to `/mnt/user-data/outputs/`
- [ ] Generated using docx-js (not other methods)
- [ ] No errors during generation

#### Typography
- [ ] Title: 24pt, bold, deep blue (#1B365D)
- [ ] Heading 1: 16pt, bold, deep blue (#1B365D)
- [ ] Heading 2: 14pt, bold, medium gray (#4A4A4A)
- [ ] Body: 11pt, body gray (#2D2D2D)
- [ ] Metadata: 9pt, light gray (#757575)
- [ ] Font is Calibri throughout

#### Spacing
- [ ] 1" margins on all sides
- [ ] Title spacing: 0pt before, 240pt after
- [ ] H1 spacing: 360pt before, 180pt after
- [ ] H2 spacing: 240pt before, 120pt after
- [ ] Body paragraphs: 240pt after, 1.6x line height
- [ ] Metadata: 60pt after each line

#### Colors
- [ ] Headers use primaryBlue (#1B365D)
- [ ] H2 headers use mediumGray (#4A4A4A)
- [ ] Body text uses bodyGray (#2D2D2D)
- [ ] Metadata uses lightGray (#757575)
- [ ] Table borders use tableBorder (#CCCCCC)
- [ ] Table header background: #E8EDF2

#### Table Formatting
- [ ] Column widths set correctly (3120, 1560, 4680 DXA)
- [ ] BOTH columnWidths array AND individual cell widths set
- [ ] All cells have borders
- [ ] Header row has background color (#E8EDF2)
- [ ] Score cells color-coded by range:
  - ≥3.5: green (#D4EDDA)
  - 3.0-3.4: yellow (#FFF3CD)
  - <3.0: red (#F8D7DA)
- [ ] Cell margins: 100pt top/bottom, 180pt left/right
- [ ] Text aligned appropriately (center for scores/headers, left for content)

#### Lists
- [ ] Each numbered section uses unique reference
- [ ] Numbering restarts at 1 for each section
- [ ] Indentation: 720pt left, 360pt hanging
- [ ] Bullets use LevelFormat.BULLET constant (not string)
- [ ] No unicode symbols (• character) used
- [ ] Proper Word list formatting (not fake lists)

#### Footer
- [ ] Horizontal rule present (gray border)
- [ ] Spacing: 360pt before rule, 120pt after
- [ ] Metadata labels in bold
- [ ] All three sections complete

## Accuracy & Evidence

### Data Verification
- [ ] All dimension scores match source assessments
- [ ] Numbers cited are accurate (not approximated)
- [ ] Names spelled correctly
- [ ] Dates are current and accurate
- [ ] Evidence sources exist and are cited correctly

### Claims Validation
- [ ] Every claim in Strengths backed by assessment data
- [ ] Every risk identified in source materials
- [ ] All actions address documented gaps or risks
- [ ] Evidence gaps verified in source assessments
- [ ] No hallucinated information or assumptions

### Team & Ownership
- [ ] Owner names match team roster from assessments
- [ ] Team structure accurately represented
- [ ] Roles and responsibilities correctly attributed
- [ ] No invented team members or capabilities

## Consistency

### Content Consistency
- [ ] Markdown and DOCX contain identical content
- [ ] No contradictions between sections
- [ ] Dimension scores consistent with interpretations
- [ ] Actions aligned with identified risks
- [ ] Metrics support stated goals

### Terminology Consistency
- [ ] Project name consistent throughout
- [ ] Person names consistent throughout
- [ ] Company/organization names consistent
- [ ] Technical terms used consistently
- [ ] Dimension names match Vianeo framework

## Writing Quality

### Conciseness
- [ ] Every sentence adds unique value
- [ ] No redundancy between sections
- [ ] No unnecessary adjectives or qualifiers
- [ ] Can't remove any sentence without losing meaning
- [ ] Total length appropriate (not bloated)

### Specificity
- [ ] Uses concrete examples (not abstractions)
- [ ] Includes real numbers (not "some" or "many")
- [ ] Names actual people and things
- [ ] Avoids generic business speak
- [ ] Could not apply to a different business

### Actionability
- [ ] Reader knows exactly what to do next
- [ ] Clear ownership and accountability
- [ ] Measurable outcomes defined
- [ ] Realistic timeframes provided
- [ ] No vague recommendations

### Evidence-Based
- [ ] Every claim supported by data
- [ ] Sources clearly documented
- [ ] Gaps acknowledged honestly
- [ ] No speculation or assumption
- [ ] Validated vs. assumed clearly distinguished

## Red Flags

If ANY of these are present, revise immediately:

### Content Red Flags
- [ ] Generic praise ("team seems capable", "promising opportunity")
- [ ] Hedging language ("may", "might", "possibly", "could")
- [ ] Actions without owners
- [ ] Vague risks ("some concerns", "needs work")
- [ ] Evidence gaps that are actually risks
- [ ] Mixing aspirations with validated strengths

### Format Red Flags
- [ ] Em dashes used (— character)
- [ ] Inconsistent formatting between outputs
- [ ] Missing table borders or colors
- [ ] Incorrect heading hierarchy
- [ ] Unicode bullets instead of proper lists
- [ ] Poor paragraph spacing

### Quality Red Flags
- [ ] Longer than 8 sentences in Executive Diagnostic
- [ ] Generic statements that apply to any business
- [ ] Missing specific numbers in Strengths
- [ ] Downplayed or buried risks
- [ ] Unverified claims or data
- [ ] Contradictions between sections

## Final Validation

Before delivering, confirm:

**The Five Essential Questions:**
1. **Actionable?** Can someone read this and know exactly what to do?
2. **Specific?** Is this clearly about THIS business, not any business?
3. **Balanced?** Does it acknowledge both strengths AND real problems?
4. **Evidence-based?** Is every claim supported by assessment data?
5. **Concise?** Could any sentence be cut without losing meaning?

**If "no" to any question, revise before delivering.**

## Delivery Checklist

- [ ] Both files created (markdown and DOCX)
- [ ] Both files saved to /mnt/user-data/outputs/
- [ ] File names follow convention
- [ ] Files tested and can be opened
- [ ] Quality validation complete
- [ ] Ready to present to user

## Post-Delivery

After delivering, be prepared to:
- [ ] Explain any specific findings if asked
- [ ] Clarify methodology if requested
- [ ] Provide additional context on gaps
- [ ] Discuss prioritization rationale
- [ ] Iterate based on feedback

---

**Remember:** This document often makes the first impression on investors or stakeholders. Quality matters. Take the time to validate thoroughly before delivery.

**Time Budget:**
- Content creation: 10-15 minutes
- Quality validation: 5-10 minutes
- Format verification: 5 minutes
- Final review: 3-5 minutes
- **Total: 25-35 minutes for complete diagnostic**

**If validation fails or questions arise, pause and address before delivery. Never deliver a diagnostic that doesn't pass this checklist.**
