---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wmonths
canonical_label: Months worked in the last 12 months, primary job (7-day ref period)
variable_name: wmonths
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
value_codes: null
allowed_range:
  min: 0
  max: 12
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to:
- VAR-wagetotal
- VAR-twageothers
- VAR-thoursannual
- VAR-lincnc
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - months worked
  - months in last year
  - months employed
  - months of work
  typical_section_names:
  - Employment
  - Primary job
  - Months
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    wmonths
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Number of months worked in the last 12 months for
    the main job.
---
## Definition

`wmonths` is a numeric/continuous variable recording the number of months worked in the last 12 months for the main job of any individual with a job (LSTATUS=1). The main job is the occupation to which the person dedicated the most time over the past week.

## Conceptual intent

wmonths captures the months of work in the main job over the past year, which is essential for annualizing wages without assuming full-year work.

## Construction notes

Record the number of months the person worked in the main job during the last 12 months. Used to annualize wage_total; the harmonizer should not assume the person worked the whole year.

## Consistency checks

- wmonths must lie in [0,12].
- Should be non-missing only where lstatus == 1.

## Escalation triggers

- wmonths is missing while wage payments are reported, preventing annualization.

## Common mistakes

- Assuming full-year work when wmonths is missing (do not default to 12).
- Recording wmonths outside the [0,12] range.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
