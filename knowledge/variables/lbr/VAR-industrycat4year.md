---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================
variable_id: VAR-industrycat4year
canonical_label: 4-category industry classification, primary job (12-month ref period)
variable_name: industrycat4_year
module_id: MOD-LBR
gmd_version: '3.0'
schema_version: '0.1'
status: draft
tier: 1
unit_of_analysis: individual
mapping_role: derived_preferred
data_type: categorical
value_codes:
- value: 1
  label: Agriculture
- value: 2
  label: Industry
- value: 3
  label: Services
- value: 4
  label: Other
allowed_range: null
missing_codes:
  - MISS-OTHER-CATEGORY
derived_from:
- VAR-industrycat10year
derives_to: []
correspondence_output:
  method: recode
  from: VAR-industrycat10year
  map: {"1": 1, "2/5": 2, "6/9": 3, "10": 4}
country_parameters:
- PARAM-LBR-INDUSTRY-CROSSWALK
gates:
- variable_id: VAR-lstatusyear
  condition: VAR-lstatusyear == 1
rules: []
exceptions: []
external_standards: []
source_hints:
  question_keywords:
  - industry
  - broad economic activity
  - 12 months
  typical_section_names:
  - Labor
  - Primary job
  - 12-month
provenance:
  source_document: GMD_household_survey_harmonization.md
  source_section: Labor (LBR) [Chapter 5, chapter5-LMR.qmd], Primary Employment, 12-month reference period,
    industrycat4_year
  extraction_method: manual
  extracted_on: '2026-08-14'
  human_reviewed: false
  reviewer: null
  notes: >-
    12-month reference period. This section must be filled only for those individuals who responded to
    labor questions with a 12-month reference period, regardless of whether they also responded with a
    7-day reference period. Primary job family, 12-month reference period. Broad Economic Activities.
    Draft, proposed, pending GPID Team review: derived_from VAR-industrycat10year and the recode 1 ->
    1, 2-5 -> 2, 6-9 -> 3, 10 -> 4 added; mapping_role atomic -> derived_preferred, since the
    construction notes create the variable from the ten categories, else directly from the data. The
    recode is not written out in the GMD guideline text nor in the GLD manual text read; it follows
    the category labels and is the recode observed in a legacy ECA GMD file. To confirm.
---
## Definition

`industrycat4_year` is a categorical variable recording the 1-digit industry classification for Broad Economic Activities for the main job in the last 12 months. Four categories after harmonization.

## Conceptual intent

industrycat4_year aggregates 12-month primary industry into four broad categories.

## Construction notes

Created directly from data or from industrycat10_year.

The recode from `VAR-industrycat10year` is the `correspondence_output` recipe of this record. Where the survey's classification is coarser than the ten categories (a group of ISIC sections), the variable takes the value every category of the group recodes to, and has none when they differ.

## Consistency checks

- industrycat4_year must be an integer in [1,4] where non-missing.
- Must not conflict with industrycat10_year.

## Escalation triggers

- Aggregating industrycat10_year into industrycat4_year incorrectly.

## Common mistakes



## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1 | Initial draft | GPID Team  |
| 2026-11-23 | 0.1 | Draft: add derived_from VAR-industrycat10year, correspondence_output (recode) and PARAM-LBR-INDUSTRY-CROSSWALK; mapping_role derived_preferred | GPID Team (proposed) |
