---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagenc2
canonical_label: Last wage payment, secondary job, excl. bonuses (7-day ref period)
variable_name: wage_nc_2
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 2
unit_of_analysis: individual
mapping_role: atomic
data_type: numeric_continuous
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
- VAR-wagetotal2
- VAR-twagencotal
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat2
  condition: empstat_2 == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - second job wage
  - salary
  - earnings secondary job
  typical_section_names:
  - Employment
  - Secondary job
  - Wages
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Secondary Employment, 7-day reference period,
    wage_nc_2
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Secondary job family, 7-day reference period. Last wage payment in local currency, excluding
    bonuses.
---
## Definition

`wage_nc_2` is a numeric/continuous variable recording the last wage payment in local currency of any individual (LSTATUS=1 & EMPSTAT=1) in its secondary occupation. The wage comes from the second job, i.e. the job to which the person dedicated the second most time in the week preceding the survey.

## Conceptual intent

wage_nc_2 captures the regular wage of the secondary job, excluding tips, bonuses, and other compensation. The reference period is recorded in unitwage_2.

## Construction notes

For the self-employed this is net revenues (net of all costs except taxes) or salary taken from the business. Non-paid employees (EMPSTAT_2=2) should have wage = 0. Use gross wages when available, net only when gross is unavailable.

## Consistency checks

- wage_nc_2 should be non-missing only where lstatus == 1 and empstat_2 == 1.
- Non-paid employees of the secondary job should have wage_nc_2 == 0.

## Escalation triggers

- The secondary-job wage reference period is not reported.

## Common mistakes

- Including tips/bonuses in wage_nc_2.
- Assigning a wage to non-paid secondary workers.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
