---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industryorig2
canonical_label: Original industry code, secondary job (7-day ref period)
variable_name: industry_orig_2
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
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
- VAR-industrycat102
- VAR-industrycat42
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
  - second job industry
  - original industry
  - economic activity
  typical_section_names:
  - Employment
  - Secondary job
  - Industry
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    industry_orig_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Original industry code, no recoding. Add external_standards
    ISIC where ISIC/NACE is used.
---
## Definition

`industry_orig_2` is a categorical variable recording the original industry codes for the second job with reference period of the last 7 days, with no recoding. Corresponds to whatever is in the original file with no recoding.

## Conceptual intent

industry_orig_2 preserves the survey's original industry classification for the secondary job.

## Construction notes

Do not put missing values for people below the working age. See industry_orig for how to label files.

## Consistency checks

- Labels should be full words; no truncated labels.
- Document the classification revision used.

## Escalation triggers

- The secondary job's classification cannot be labeled.

## Common mistakes

- Recoding the original secondary-job industry codes.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
