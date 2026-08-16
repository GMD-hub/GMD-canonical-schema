---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-minlaborage
canonical_label: Labor module application age (country-specific)
variable_name: minlaborage
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
  max: 20
missing_codes:
- code: .a
  label: Variable not harmonized
- code: .b
  label: Cannot be harmonized because data does not meet harmonization definition
- code: .c
  label: Information not available because the item was not collected in this survey
derived_from: []
derives_to: []
country_parameters: []
prerequisites: []
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - minimum working age
  - labor module application age
  - age cutoff
  - working age
  typical_section_names:
  - Labor module
  - Employment
  - Individual characteristics
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Labor status, 7-day reference period, minlaborage
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: Chapter source file is chapter5-LMR.qmd, where 'LMR' is the module-code alias for LBR; references
    resolve to MOD-LBR (Labor). Labor module is applied only to individuals at or above MINLABORAGE.
---
## Definition

`minlaborage` is a numeric/continuous variable recording the lowest age for which the labor module is implemented in the survey, i.e. the minimum working age in the country. The lower age cutoff at which labor information is collected varies from country to country.

## Conceptual intent

minlaborage defines the population to which the labor module applies. All labor outcomes are harmonized only for individuals aged greater than or equal to this country-specific minimum working age.

## Construction notes

Record the minimum legal working age applied by the survey. According to the module's consistency checks, minlaborage must be an integer and should not be higher than 20.

## Consistency checks

- MINLABORAGE must be an integer: flag records where `round(minlaborage) != minlaborage`.
- MINLABORAGE should not be higher than 20: flag `minlaborage > 20 & !mi(minlaborage)`.

## Escalation triggers

- The source documentation does not state the minimum working age.
- The recorded minimum working age exceeds the guidance threshold of 20.

## Common mistakes

- Recording a continuous age range instead of a single integer minimum.
- Applying labor variables to individuals below the minimum working age.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
