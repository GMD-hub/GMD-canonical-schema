---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-educy
canonical_label: "Years of education completed"
variable_name: educy
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: derived_preferred
data_type: numeric_continuous

# --- Allowed output values ---
value_codes: null
allowed_range:
  min: 0
  max: 30

# --- Missing value codes ---
missing_codes:
  - code: ".c"
    label: "Education section not applied because the individual is below mineducatage"
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because grade level is not listed and cannot be
            derived from available information"

# --- Derivation graph ---
# Listed in order of preference when direct grade-level data is unavailable.
derived_from:
  - VAR-educat7
  - VAR-educat5
  - VAR-educat4
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
# This block exists so that missing country records can be detected and
# the parameter's fallback policy applied.
country_parameters:
  - PARAM-EDU-YEARS-BY-LEVEL

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-mineducatage
    condition: "Set educy to .c for all individuals where age is below
                mineducatage."
  - variable_id: VAR-school
    condition: "Enrollment status must be evaluated before constructing
                educy. It determines whether current class or highest
                completed grade is the basis for calculation."

# --- Cross-references ---
rules:
  - RULE-EDU-001
  - RULE-EDU-003
exceptions: []
external_standards:
  - name: "UNESCO ISCED 2011 country mappings"
    url: "http://uis.unesco.org/en/isced-mappings"

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "years of education"
    - "years of schooling"
    - "grade currently attending"
    - "highest grade completed"
    - "class attending"
  typical_section_names:
    - "Education"
    - "Schooling"
    - "Human capital"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, educy"
  extraction_method: manual
  extracted_on: "2026-06-25"
  human_reviewed: false
  reviewer: null
  notes: "PARAM-EDU-YEARS-BY-LEVEL replaces the former country lookup table.
      Its fallback policy is undecided, so derived construction must stop
      and escalate when no valid country record exists."
---

## Definition

`educy` is a continuous variable recording the total number of years of formal
schooling completed by an individual. It is expressed in completed years and
does not account for grade repetition. It is constructed only when the survey
provides grade-level or years-of-education information; otherwise it is set
to missing.

## Conceptual intent

`educy` provides a cardinal measure of educational attainment that enables
quantitative comparisons within and across countries. Unlike the categorical
education variables, it captures variation within broad categories and is the
preferred input for regression-based education research and poverty analysis.

## Construction notes

Construction follows one of three paths depending on what the survey provides.
The paths are ordered from most direct to most dependent on intermediate
variables. The path used must be documented in the do-file notes.

**Prerequisite check: enrollment status.**
Before constructing `educy`, evaluate `school`. Its value determines which
grade reference point to use.

**Path 1 (preferred): survey provides explicit years of education.**
Map that value directly to `educy`. Cross-check against age and education
level for plausibility before accepting it.

**Path 2: survey provides grade level, using the country parameter.**
Resolve `PARAM-EDU-YEARS-BY-LEVEL` from the country layer matching the
survey's ISO3 code and survey ID year, then translate grades to years.

For individuals currently enrolled (`school = 1`):
  educy = years corresponding to (current grade - 1)

For individuals not currently enrolled (`school = 0`):
  educy = years corresponding to highest completed grade

**Path 3 (fallback): survey provides only categorical education levels.**
Use the highest available categorical variable plus the selected
`PARAM-EDU-YEARS-BY-LEVEL` record. Preference: educat7 first, then educat5,
then educat4.
Document which variable was used in the do-file notes.

**Tertiary education when grade or year is not explicitly recorded.**
Add the following years to completed secondary education:

| Degree | Completed | Not completed or status unclear |
|--------|-----------|----------------------------------|
| BA/BSc | +4 years  | +2 years                         |
| MA/MSc | +6 years  | +5 years                         |
| PhD    | +8 years  | +7 years                         |

**Grade repetition.**
`educy` records completed grade levels, not years spent in school.
A grade repeated three times counts as one year, not three.

**When no usable information is available.**
Set `educy` to `.b`. Do not guestimate using age or any other variable.

## Consistency checks

- An individual with `educat7 = 1` (no education) must have `educy = 0`.
- An individual with `educat7 = 3` (primary complete) should have `educy`
  equal to the primary duration in the selected
  `PARAM-EDU-YEARS-BY-LEVEL` record.
- No individual below `mineducatage` should have a non-missing `educy`.
- `educy` must be non-negative for all non-missing observations.
- Cross-check the distribution against the selected country parameter values.
  Sharp departures may mean the wrong ISO3 code or survey ID year was used.

## Escalation triggers

- No `PARAM-EDU-YEARS-BY-LEVEL` record is valid for the survey's ISO3 code and
  survey ID year. Apply its registry fallback policy. While that policy is
  `undecided`, stop and escalate without constructing the affected path.
- The survey's grade categories do not correspond to any known educational
  structure for that country.
- The tertiary degree type is not recorded and cannot be inferred.
- The computed distribution of `educy` is implausibly concentrated or shifted
  relative to country norms.

## Common mistakes

- Guestimating `educy` using age and education level when grade information
  is not available. The guidelines explicitly prohibit this.
- Using the current grade directly for enrolled individuals instead of
  subtracting one year.
- Counting repeated grades as additional years.
- Applying a record for the wrong ISO3 code or survey ID year.
- Constructing `educy` via path 3 without documenting the source variable.
- Setting `educy = 0` for individuals with missing categorical education
  instead of `.b`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
