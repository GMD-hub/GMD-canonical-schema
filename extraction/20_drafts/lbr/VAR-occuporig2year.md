---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-occuporig2year
canonical_label: Original occupation classification, secondary job (12-month ref period)
variable_name: occup_orig_2_year
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
- VAR-occup2year
country_parameters: []
prerequisites:
- variable_id: VAR-lstatusyear
  condition: lstatus_year == 1
rules: []
exceptions: []
external_standards:
- name: ISCO-08 (International Standard Classification of Occupations)
  url: https://www.ilo.org/public/english/bureau/stat/isco/isco08/index.htm
source_hints:
  question_keywords:
  - occupation
  - second job original occupation
  - 12 months
  typical_section_names:
  - Labor
  - Secondary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 12-month reference
    period, occup_orig_2_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 12-month reference period. This section must be filled only for those individuals who responded
    to labor questions with a 12-month reference period, regardless of whether they also responded with
    a 7-day reference period. Secondary job family, 12-month reference period. Original occupation code,
    no recoding. Add external_standards ISCO where ISCO used.
---
## Definition

`occup_orig_2_year` is a categorical variable recording the original occupation code in the last 12 months for the main job, with no recoding. Labels should have spaces around hyphens and be written in full.

## Conceptual intent

occup_orig_2_year preserves the 12-month secondary job's original occupation classification.

## Construction notes

Translate labels if not ISCO; apply ISCO labeling dofiles when applicable.

## Consistency checks

- Labels must not be truncated.

## Escalation triggers



## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
