---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industryorig
canonical_label: Original industry code, primary job (7-day ref period)
variable_name: industry_orig
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: string
value_codes: null
allowed_range: null
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-industrycat10
- VAR-industrycat4
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards:
- name: ISIC Rev. 3.1/4.0 (International Standard Industrial Classification)
  url: https://unstats.un.org/unsd/classifications/Econ/ISIC
source_hints:
  question_keywords:
  - industry
  - economic activity
  - original industry code
  - type of business
  - sector of work
  typical_section_names:
  - Employment
  - Primary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    industry_orig
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Original (country-specific) industry code, no recoding.
    External standard ISIC applies where the survey uses ISIC/NACE; add external_standards ISIC.
---
## Definition

`industry_orig` is a categorical variable recording the original industry codes in the last 7 days for the main job, as provided in the survey with no recoding. The variable is constructed for all persons administered this module and is missing otherwise.

## Conceptual intent

industry_orig preserves the survey's original industry classification (e.g. ISIC or NACE) for the main job so that details are not lost during harmonization to the 1-digit categories.

## Construction notes

Code and name format, e.g. '1 - Agriculture'. Do not recode. If the classification is not ISIC, labels must be translated to English by a language expert. If the survey uses ISIC/NACE, the standard labeling dofiles may be applied.

## Consistency checks

- Labels should use full words; truncated labels such as 'pharm.' are not allowed.
- The classification revision (ISIC Rev 3.1/4.0, NACE Rev 1/2) should be documented.

## Escalation triggers

- The survey's classification system is unknown and cannot be labeled.
- Translation of a non-English classification cannot be verified.

## Common mistakes

- Recoding the original industry codes.
- Leaving industry_orig missing for employed individuals.
- Using abbreviations or truncated labels.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
