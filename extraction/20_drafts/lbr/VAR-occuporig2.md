---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-occuporig2
canonical_label: Original occupation classification, secondary job (7-day ref period)
variable_name: occup_orig_2
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
- VAR-occup2
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards:
- name: ISCO-08 (International Standard Classification of Occupations)
  url: https://www.ilo.org/public/english/bureau/stat/isco/isco08/index.htm
source_hints:
  question_keywords:
  - occupation
  - second job occupation
  - original occupation
  typical_section_names:
  - Employment
  - Secondary job
  - Occupation
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    occup_orig_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Original occupation code, no recoding. Add external_standards
    ISCO where ISCO is used.
---
## Definition

`occup_orig_2` is a categorical variable recording the original occupation code in the last 7 days for the secondary job, with no recoding. Corresponds to whatever is in the original file with no recoding.

## Conceptual intent

occup_orig_2 preserves the survey's original occupation classification for the secondary job.

## Construction notes

Labels should be full words with spaces around hyphens. See occup_orig for how to label files.

## Consistency checks

- Labels must not be truncated.
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- The secondary job's occupation cannot be labeled.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
