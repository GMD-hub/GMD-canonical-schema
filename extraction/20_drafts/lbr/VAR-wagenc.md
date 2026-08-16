---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagenc
canonical_label: Last wage payment, primary job, excl. bonuses (7-day ref period)
variable_name: wage_nc
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
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
- VAR-wagetotal
- VAR-twagencotal
- VAR-lincnc
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat
  condition: empstat <= 2 (paid or non-paid employee)
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - wage
  - salary
  - earnings
  - last wage payment
  - income from main job
  typical_section_names:
  - Employment
  - Wages
  - Primary job
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    wage_nc
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Primary job family, 7-day reference period. Last wage payment in local currency, excluding bonuses
    and other compensation.
---
## Definition

`wage_nc` is a numeric/continuous variable recording the last wage payment in local currency of any individual (LSTATUS=1 & EMPSTAT=1 or 2) in its primary occupation. The wage comes from the main job, i.e. the job to which the person dedicated the most time in the week preceding the survey.

## Conceptual intent

wage_nc captures the regular wage of the main job, excluding tips, bonuses, and other compensation. The reference period of the wage is recorded in UNITWAGE. The non-compensation wage is the building block for annualized wage totals and labor income.

## Construction notes

For the self-employed or business owners this should be net revenues (net of all costs except taxes) or the salary taken from the business; because of the near-total lack of tax information, the wage is not net of taxes. Non-paid employees (EMPSTAT=2) should have wage_nc = 0. Use gross wages when available and net wages only when gross is unavailable.

## Consistency checks

- wage_nc should be non-missing only where lstatus == 1 and empstat == 1; non-paid employees (empstat == 2) are coded 0 by definition.
- Non-paid employees (empstat == 2) should have wage_nc == 0.
- wage_nc must be >= 0.

## Escalation triggers

- The reference period of the wage is not reported, preventing unitwage mapping.
- Gross wages are unavailable and net wages must be used (document).

## Common mistakes

- Including tips, bonuses, or in-kind compensation in wage_nc.
- Assigning wage_nc to non-paid employees instead of 0.
- Leaving wage_nc missing for paid employees.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
