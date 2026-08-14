---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-wagetotal
canonical_label: Annualized total wage, primary job (7-day ref period)
variable_name: wage_total
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: derived
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
derived_from:
- VAR-wagenc
- VAR-unitwage
- VAR-wmonths
- VAR-whours
derives_to:
- VAR-twageothers
- VAR-twagencotal
- VAR-twagetotal
- VAR-lincnc
- VAR-laborincome
country_parameters: []
prerequisites:
- variable_id: VAR-lstatus
  condition: lstatus == 1
- variable_id: VAR-empstat
  condition: empstat == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - annualized wage
  - total wage
  - wage total
  - annual wage
  typical_section_names:
  - Employment
  - Wages
  - Primary job
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 7-day reference period,
    wage_total
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: 'Primary job family, 7-day reference period. Derived: annualized wage including bonuses, in-kind
    and other compensation.'
---
## Definition

`wage_total` is a numeric/continuous variable recording the annualized wage payment (regular wage plus bonuses, in-kind, compensation, etc.) for the primary occupation in local currency. The wage comes from the main job and includes tips, compensations such as bonuses, dwellings or clothes, and other payments.

## Conceptual intent

wage_total annualizes the total wage of the main job, including non-regular compensation, over the months actually worked. It is a key building block for total employment earnings and labor income.

## Construction notes

wage_total is derived from wage_nc, unitwage, whours, and wmonths using the annualization formula in the chapter. wage_total equals wage_nc when there are no bonuses/tips. Annualization must use the actual months worked; do not assume full-year work. Use gross wages when available, net only when gross is unavailable.

## Consistency checks

- wage_total must be >= 0.
- If no bonuses/tips exist, wage_total should equal the annualized wage_nc.
- wage_total should only be non-missing for lstatus == 1 and empstat == 1.

## Escalation triggers

- The unitwage period or months worked is unavailable, so annualization cannot be computed reliably.

## Common mistakes

- Annualizing assuming the person worked the whole year.
- Including wage_nc for non-paid employees in wage_total.
- Applying the wrong unitwage conversion factor.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
