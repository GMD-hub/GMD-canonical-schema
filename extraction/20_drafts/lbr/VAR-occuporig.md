---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-occuporig
canonical_label: Original occupation classification, primary job (7-day ref period)
variable_name: occup_orig
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
- VAR-occup
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
  - original occupation
  - job title
  - occupation code
  typical_section_names:
  - Employment
  - Primary job
  - Occupation
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    occup_orig
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Original (country-specific) occupation code, no recoding.
    Add external_standards ISCO where the survey uses ISCO.
---
## Definition

`occup_orig` is a categorical variable recording the original occupation code in the last 7 days for the main job, with no recoding. For each value label there must be a space between the hyphens, and truncated labels must be written in full.

## Conceptual intent

occup_orig preserves the survey's original occupation classification for the main job.

## Construction notes

Code and name format, e.g. '1 - Pharmacist'; 'pharm.' and 'law.' are not allowed. If not ISCO, translate labels to English by a language expert. If ISCO is used, the standard labeling dofiles may be applied.

## Consistency checks

- Labels must not be truncated; use full occupation names.
- The ISCO digit level (1-4) used should be documented.

## Escalation triggers

- The occupation classification cannot be labeled reliably.

## Common mistakes

- Truncating occupation labels.
- Recoding the original occupation codes.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
