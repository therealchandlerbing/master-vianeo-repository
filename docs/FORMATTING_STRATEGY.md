# VIANEO Framework: Formatting Strategy for Consistent Outputs

**Version**: 1.0
**Purpose**: Memory-efficient approach to ensure consistent, professional outputs across all VIANEO steps

---

## The Problem

Without explicit format specifications, AI-generated outputs can vary in:
- Structural organization (headers, sections, tables)
- Naming conventions (file names, metadata fields)
- Data presentation (table columns, calculation display)
- Visual consistency (bold text, emoji usage, separators)
- Content quality (justification length, evidence specificity)

**Result**: Outputs look unprofessional, automated processing fails, users must manually reformat.

---

## The Solution: Centralized Format Specifications

Instead of embedding all formatting details in every prompt (memory bloat), we:

1. **Create separate format spec files** (one per step with visual outputs)
2. **Prompts reference the specs** ("Follow FORMAT_SPEC_StepX.md exactly")
3. **Validation checklists** ensure compliance before delivery
4. **Examples demonstrate** the format in practice

### Design Tokens: Single Source of Truth

**All visual design decisions are centralized in `docs/VIANEO_Design_Tokens.md`**

This file defines:
- **Color system** - Primary, status, validation, and dimension colors
- **Typography** - Font stacks, sizes, weights for HTML and Word
- **Spacing** - Consistent spacing scale
- **Components** - Tables, cards, buttons, callouts
- **Code snippets** - Ready-to-use CSS, Python, and JavaScript

**Priority**: When colors or typography values conflict between documents, `VIANEO_Design_Tokens.md` is the authoritative source. Update other files to match.

### Memory Efficiency

**Old Approach** (duplicated in every prompt):
```
Total per step: ~2,000 words of formatting instructions
× 11 steps = ~22,000 words
Result: Prompts become bloated, hard to maintain
```

**New Approach** (centralized specs):
```
Format spec file: ~2,500 words (comprehensive with examples)
Prompt reference: ~50 words ("Follow FORMAT_SPEC_StepX.md")
× 11 steps = ~550 words in prompts + 11 standalone specs
Result: Prompts stay focused, specs are reusable and updatable
```

**Memory Savings**: ~95% reduction in formatting instructions within prompts

---

## Format Specification Files Created

### Design System Foundation

✅ **VIANEO_Design_Tokens.md** - Single source of truth for all visual design
- Unified color palette (primary, status, validation, dimensions)
- Typography system (fonts, sizes, weights)
- Spacing and layout tokens
- Ready-to-use CSS, Python, and JavaScript code
- Accessibility requirements and validated color combinations

### High-Priority Steps (Completed)

✅ **FORMAT_SPEC_Step3_Market_Maturity.md** - Most critical
- Assessment table format (29 questions)
- Dimension score calculations
- Overall weighted score
- Category classification
- Key findings structure

✅ **FORMAT_SPEC_Step9_Ecosystem_Value_Network.md** - Complex tables
- 5 value chain table structures
- Executive summary format
- Priority target analysis
- Emoji and character limit rules

### Remaining Steps (To Create)

📋 **FORMAT_SPEC_Step0_Executive_Brief.md** - Foundation document
📋 **FORMAT_SPEC_Step2_40Q_Diagnostic.md** - Rapid assessment
📋 **FORMAT_SPEC_Step5_Needs_Requesters.md** - Desirability analysis
📋 **FORMAT_SPEC_Step6_Persona_Development.md** - Persona documents
📋 **FORMAT_SPEC_Step7_Needs_Matrix.md** - HTML matrix + report
📋 **FORMAT_SPEC_Step10_Diagnostic_Comment.md** - Executive diagnostic
📋 **FORMAT_SPEC_Step11_Features_Needs_Matrix.md** - Interactive matrix

---

## How It Works: Three-Layer System

### Layer 1: Format Specification (Reference Document)

**Location**: `/docs/FORMAT_SPEC_StepX.md`
**Purpose**: Complete visual specification with examples
**Content**:
- Exact header structure
- Required sections with templates
- Table formats with column specs
- Calculation formulas
- Naming conventions
- Character/length limits
- Visual examples (good vs. bad)
- Common mistakes to avoid

**Used by**: AI when generating outputs, humans when reviewing quality

### Layer 2: Prompt Integration (Execution)

**Location**: `/prompts/stepXX_[name].md`
**Updated section**:
```markdown
## Output Format

**CRITICAL**: Follow the format specification exactly.

**Format Reference**: `docs/FORMAT_SPEC_StepX.md`

Before delivering output:
1. Generate content following methodology in this prompt
2. Format output according to FORMAT_SPEC_StepX.md
3. Validate against checklist in format spec
4. Only deliver if all checks pass

Key formatting requirements:
- [3-5 most critical rules highlighted]
- See format spec for complete details
```

**Memory impact**: ~100 words added to prompt

### Layer 3: Validation Checklist (Quality Control)

**Location**: Within each FORMAT_SPEC file
**Purpose**: Pre-delivery verification
**Format**:
```markdown
## Validation Checklist

Before delivering output, verify:

### Structure Completeness
- [ ] All required sections present
- [ ] Headers at correct levels
- [ ] Separators in correct positions

### Format Accuracy
- [ ] Naming conventions followed
- [ ] Bold/italic applied correctly
- [ ] Tables formatted exactly
- [ ] Calculations shown with formulas

### Content Quality
- [ ] Evidence cited for all claims
- [ ] Character limits respected
- [ ] No vague language ("some", "many")
- [ ] Specific numbers and dates used
```

**Used by**: AI before delivery, reviewers during quality checks

---

## Benefits of This Approach

### 1. Consistency Across Evaluations
- Same project evaluated twice → identical format
- Different evaluators → identical format
- Different AI models → identical format

### 2. Professional Quality
- Board-ready presentation
- Automated processing compatible
- Print-friendly formatting
- Client-facing professional

### 3. Easy Maintenance
- Format change needed? Update ONE file
- All future outputs automatically consistent
- No need to update 11 different prompts

### 4. Training & Onboarding
- New evaluators learn format from specs
- Clear examples of good vs. bad
- Common mistakes documented

### 5. Automated Validation
- Checklists can be automated (future)
- Format compliance can be tested
- Quality gates before delivery

---

## Implementation Guidelines

### For Prompt Writers

When creating/updating prompts:

1. **Focus prompts on methodology**, not formatting
2. **Add format reference** in "Output Format" section:
   ```markdown
   **Format Reference**: `docs/FORMAT_SPEC_StepX.md`
   ```
3. **Highlight 3-5 critical rules** most commonly violated
4. **Reference validation checklist** before delivery

### For AI Assistants Generating Outputs

When executing a VIANEO step:

1. **Read the methodology** from prompt
2. **Generate content** based on provided data
3. **Read the format spec** for this step
4. **Reformat output** to match spec exactly
5. **Run validation checklist** from spec
6. **Only deliver if all checks pass**

### For Quality Reviewers

When reviewing outputs:

1. **Open format spec** for the step
2. **Follow validation checklist** item by item
3. **Check common mistakes section**
4. **Flag any deviations** for correction
5. **Approve only if 100% compliant**

---

## Example: Step 3 Format Enforcement

### Before Format Spec

**Problems**:
- Inconsistent headers ("Vianeo Assessment" vs. "Market Maturity Evaluation")
- Missing metadata fields
- Justifications 2-3 sentences (should be 1)
- Calculations without formulas shown
- Thresholds incorrect (3.0 for Desirability instead of 3.5)
- Category names vary ("Good" vs. "Promising")

### After Format Spec

**Improvements**:
- Exact header: "Vianeo Market Maturity Assessment - [Name]"
- All 5 metadata fields present and formatted correctly
- Every justification exactly 1 sentence
- Calculations show full arithmetic
- All thresholds correct (3.5 for Desirability)
- Category names standardized with exact score ranges

**Result**: Outputs indistinguishable from each other, professional quality

---

## Metrics for Success

Track these metrics to measure format consistency:

### Compliance Rate
- **Target**: 100% of outputs pass validation checklist
- **Measure**: % of checklist items marked ✓ before delivery
- **Action**: If <100%, identify recurring mistakes and update spec

### Revision Rate
- **Target**: <5% of outputs require reformatting
- **Measure**: % of delivered outputs sent back for format fixes
- **Action**: If >5%, enhance format spec with more examples

### Time to Deliver
- **Target**: No increase despite format enforcement
- **Measure**: Average time from start to delivery
- **Action**: If increase, streamline checklist or add automation

---

## Next Steps

### Immediate (This Commit)

1. ✅ Create FORMAT_SPEC_Step3_Market_Maturity.md
2. ✅ Create FORMAT_SPEC_Step9_Ecosystem_Value_Network.md
3. ✅ Create this FORMATTING_STRATEGY.md
4. 🔄 Update Step 3 prompt to reference format spec
5. 🔄 Update Step 9 prompt to reference format spec

### Short-term (Next 1-2 weeks)

1. Create format specs for Steps 0, 2, 5, 6, 7, 10, 11
2. Update all prompts to reference their format specs
3. Add format spec references to README.md
4. Create "Quick Format Guide" (1-page summary per step)

### Long-term (Future)

1. Develop automated validation tools
2. Create format compliance dashboard
3. Build templates that auto-populate with format
4. Add format checking to CI/CD pipeline

---

## FAQ

**Q: Why not just include examples in prompts?**
A: Examples are good but insufficient. Format specs provide:
- Exhaustive rules (not just examples)
- Validation checklists
- Common mistakes to avoid
- Centralized maintenance

**Q: Won't this make prompts harder to use?**
A: No. Prompts become *easier* because they focus on methodology. Format specs are separate reference documents.

**Q: What if I need to customize the format?**
A: Format specs are guidelines. For special cases:
- Note deviation in output
- Explain why deviation was needed
- Document custom format for future reference

**Q: How do I know if my output is compliant?**
A: Run the validation checklist in the format spec. If all boxes check, you're compliant.

**Q: What if the format spec conflicts with the prompt?**
A: Format spec always wins for formatting questions. Prompt wins for methodology/content questions. If conflict, update prompt or spec to align.

---

## Conclusion

**The formatting strategy achieves:**
- ✅ **Consistency**: Identical format across all outputs
- ✅ **Quality**: Professional, board-ready deliverables
- ✅ **Efficiency**: 95% reduction in prompt formatting bloat
- ✅ **Maintainability**: Update once, apply everywhere
- ✅ **Scalability**: Easy to add new steps or modify existing

**Without adding significant memory overhead**, we ensure every VIANEO output meets the highest professional standards.

---

**Document Status**: Active
**Last Updated**: 2025-01-21
**Next Review**: After completing all format specs
