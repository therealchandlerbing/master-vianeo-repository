# Templates Directory

This directory contains reusable output templates for all VIANEO framework deliverables.

## Structure

All templates are organized at the root level of this directory, organized by file type and step number.

### Template Naming Convention

```
[StepNumber]_[OutputType]_[Format]_Template.[ext]
```

Examples:
- `Step3_MarketMaturity_Markdown_Template.md`
- `Step7_Needs_Matrix_Template.html`
- `Step10_Diagnostic_DOCX_Template.md`

## Templates by Format

### Markdown Templates (.md)
| File | Purpose |
|------|---------|
| `Executive_Brief_Template.md` | Step 0 executive brief output |
| `Assessment_Template.md` | General assessment structure |
| `Step3_MarketMaturity_Markdown_Template.md` | 29Q assessment report |
| `Step3_Assessment_Results_Template.md` | Assessment results format |
| `Step3_Dimension_Analysis_Template.md` | Dimension-by-dimension analysis |
| `Step4_Legitimacy_Markdown_Template.md` | Legitimacy worksheet |
| `Step5_NeedsRequesters_Markdown_Template.md` | WHO/WHAT/WHY/HOW analysis |
| `Step7_Analysis_Report_Template.md` | Needs qualification report |
| `Step8_EcosystemAnalysis_Markdown_Template.md` | Players/Influencers analysis |
| `Step9_Analysis_Markdown_Template.md` | Value network analysis |
| `Step10_Diagnostic_Markdown_Template.md` | Executive diagnostic |
| `Step11_FeaturesNeeds_Analysis_Template.md` | Features-Needs analysis |
| `Step12_PMF_Template.md` | Product/Market Fit sheet |
| `Step12_Business_Model_Template.md` | Business Model Canvas |
| `Step12_Dashboard_Template.md` | Viability dashboard |
| `Committee_Synthesis_Template.md` | Post-sprint committee synthesis report |
| `Committee_Synthesis_PlatformEntry.md` | Platform copy/paste entry guide |

### DOCX Format Specifications (.md describing Word format)
| File | Purpose |
|------|---------|
| `40Q_Assessment_Results_Template.md` | 40Q diagnostic Word format |
| `40Q_Score_Summary_Template.md` | Score summary format |
| `360SIS_Application_Template.md` | 360 SIS application format |
| `CNEN_Application_Template.md` | CNEN application format |
| `Step4_Legitimacy_DOCX_Template.md` | Legitimacy Word format |
| `Step5_NeedsRequesters_DOCX_Part1_Template.md` | Requesters Word format |
| `Step5_NeedsRequesters_DOCX_Part2_Template.md` | Needs Word format |
| `Step5_NeedsRequesters_DOCX_Part3_Template.md` | Alternatives Word format |
| `Step8_PlayersInfluencers_DOCX_Format_Spec.md` | Players/Influencers Word format |
| `Step9_Ecosystem_Data_DOCX_Template.md` | Ecosystem data Word format |
| `Step9_Priority_Targets_DOCX_Template.md` | Priority targets Word format |
| `Step10_Diagnostic_DOCX_Template.md` | Diagnostic Word format |

### HTML Interactive Templates (.html)
| File | Purpose |
|------|---------|
| `Step7_Needs_Matrix_Template.html` | Interactive needs qualification matrix |
| `Step9_Value_Network_Visualization.html` | Interactive value network diagram |
| `Step11_FeaturesNeeds_Matrix_Template.html` | Interactive features-needs matrix |
| `Step11_FeaturesNeeds_DualView_Template.html` | Dual-view matrix (Needs + Means) |
| `Step12_Viability_Dashboard.html` | Interactive viability dashboard |

### Utility Templates
| File | Purpose |
|------|---------|
| `Evidence_Log_Template.md` | Track evidence sources |
| `Hypotheses_Log_Template.md` | Track hypotheses and validation |
| `Interview_Guide_Template.md` | Customer interview structure |
| `Gate_A_Decision_Brief_Template.md` | Gate decision format |
| `Step7_Quick_Start_Guide.md` | Quick start for Step 7 |

## Templates by Step

| Step | Templates Available |
|------|---------------------|
| **Step 0** | Executive Brief (MD) |
| **Step 1** | 360SIS Application, CNEN Application |
| **Step 2** | 40Q Assessment Results, 40Q Score Summary |
| **Step 3** | Market Maturity MD, Assessment Results, Dimension Analysis |
| **Step 4** | Legitimacy MD, Legitimacy DOCX |
| **Step 5** | Needs/Requesters MD, DOCX Parts 1-3 |
| **Step 6** | *(See note below)* |
| **Step 7** | Needs Matrix HTML, Analysis Report MD, Quick Start |
| **Step 8** | Ecosystem Analysis MD, Players/Influencers DOCX |
| **Step 9** | Value Network HTML, Analysis MD, Data DOCX, Priority Targets DOCX |
| **Step 10** | Diagnostic MD, Diagnostic DOCX |
| **Step 11** | Features-Needs HTML, Dual-View HTML, Analysis MD |
| **Step 12** | PMF MD, Business Model MD, Dashboard MD, Viability Dashboard HTML |
| **Post-Sprint** | Committee Synthesis MD, Platform Entry MD |

> **Note**: Step 6 (Persona Development) templates follow the detailed specifications in the `prompts/step_06_persona_development.md` prompt file.
>
> **Note**: Committee Synthesis is a post-sprint administrative step that translates the 5-dimension Vianeo assessment into the 4-dimension committee evaluation format for platform submission.

## Usage

All templates follow consistent formatting standards defined in `docs/VIANEO_Design_Tokens.md`:
- Professional typography (Calibri/Arial for Word, system fonts for HTML)
- Semantic color coding (dimension colors, status colors, validation levels)
- Clear section hierarchy
- Quality checklists embedded
- Evidence citation requirements
