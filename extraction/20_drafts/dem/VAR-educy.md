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
  - PARAM-EDU-LEVEL-CROSSWALK
  - PARAM-EDU-MIN-EDUCATION-AGE

# --- Universe / skip gate ---
gates:
  - variable_id: VAR-age
    condition: VAR-age >= PARAM-EDU-MIN-EDUCATION-AGE

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
  notes: "PARAM-EDU-LEVEL-CROSSWALK replaces PARAM-EDU-YEARS-BY-LEVEL and the
      former fixed tertiary-year table. cum_years_schooling on each matched
      country_entry_id row now supplies years-of-schooling for any
      post-grade-12 level. Its fallback policy is block_and_escalate, so
      derived construction must stop and escalate when no valid country
      record exists for a reported national level."
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

Construction is evaluated per individual, not per survey. Skip patterns
mean the same survey can route different respondents to different
questions, so path selection depends on what data is actually present for
that record. The path used must be documented in the do-file notes.

**Gate check: enrollment status.**
Before constructing `educy`, evaluate `school` for the individual. Its value determines which
branch below applies.

**Path 1 (preferred): individual reports explicit years of education.**
Map that value directly to `educy`. Cross-check against age and education
level for plausibility before accepting it.

**Path 2: individual is enrolled (`school = 1`) with a current grade 1-12.**
  educy = current_grade - 1

**Path 3: individual is enrolled (`school = 1`) with a current year within a
post-grade-12 track (tertiary, vocational, or other post-secondary level).**
  educy = base_years + (current_track_year - 1)

**Path 4: individual is enrolled (`school = 1`) in a named post-grade-12
level/program with no current-year or progress detail.**
  educy = base_years
  Flag the record: "enrolled in [level], in-progress duration unknown;
  educy reflects last completed level only."

**Path 5: individual is not enrolled (`school = 0`) with a highest
completed grade 1-12.**
  educy = highest_completed_grade

**Path 6: individual is not enrolled (`school = 0`) and reports an ordinal
year within a post-grade-12 track (e.g., "2nd year") rather than a named
qualification.**
  educy = base_years + ordinal_year_number

**Path 7 (fallback): individual is not enrolled (`school = 0`) and reports
a national education level or qualification label beyond simple grade
numbering.**
Match the reported level text to a `country_entry_id` in
`PARAM-EDU-LEVEL-CROSSWALK` resolved from the country layer for the
survey's ISO3 code and survey ID year. The matched record supplies
`isced_level`, `gmd_educat4_target`, `gmd_educat5_target`,
`gmd_educat7_target`, and `cum_years_schooling`.
  educy = cum_years_schooling for the matched country_entry_id
Document the matched `country_entry_id` in the do-file notes.

**Shared definition: `base_years`.**
`base_years` is `cum_years_schooling` for the last completed level before
the post-grade-12 track — typically upper secondary completion (12 years
in most systems), resolved from the general-track ISCED-3 row in
`PARAM-EDU-LEVEL-CROSSWALK` when the country's value differs.

**Grade repetition.**
`educy` records completed grade levels, not years spent in school.
A grade repeated three times counts as one year, not three.

**When no usable information is available.**
Set `educy` to `.b`. Do not guestimate using age or any other variable.

## Consistency checks

- An individual with `educat7 = 1` (no education) must have `educy = 0`.
- An individual with `educat7 = 3` (primary complete) should have `educy`
  equal to `cum_years_schooling` for the matched primary-completion
  `country_entry_id` in the selected `PARAM-EDU-LEVEL-CROSSWALK` record.
- No individual below `mineducatage` should have a non-missing `educy`.
- `educy` must be non-negative for all non-missing observations.
- Cross-check the distribution against the selected country parameter values.
  Sharp departures may mean the wrong ISO3 code or survey ID year was used.

## Escalation triggers

- No `PARAM-EDU-LEVEL-CROSSWALK` record is valid for the survey's ISO3 code
  and survey ID year, or the reported national level text does not match
  any `country_entry_id`. Apply the registry's `block_and_escalate`
  fallback policy: stop and escalate without constructing the affected
  record.
- The survey's reported level does not correspond to any known national
  education structure for that country.
- The individual is enrolled in a post-grade-12 track and neither a
  current-year number nor a matchable level label is available.
- The computed distribution of `educy` is implausibly concentrated or shifted
  relative to country norms.

## Common mistakes

- Guestimating `educy` using age and education level when grade or level
  information is not available. The guidelines explicitly prohibit this.
- Using the current grade directly for enrolled individuals instead of
  subtracting one year.
- Counting repeated grades as additional years.
- Applying a country crosswalk record for the wrong ISO3 code or survey ID
  year.
- Constructing `educy` via path 7 without documenting the matched
  `country_entry_id`.
- Awarding years for an in-progress post-grade-12 track beyond
  `base_years` when progress detail is unavailable.
- Setting `educy = 0` for individuals with missing categorical education
  instead of `.b`.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |
| 2026-09-30 | 0.2     | Replaced `PARAM-EDU-YEARS-BY-LEVEL` and the fixed tertiary-year table with `PARAM-EDU-LEVEL-CROSSWALK`-based resolution; reframed construction as per-individual path selection (RULE-EDU-003 v0.2) | GPID Team |
