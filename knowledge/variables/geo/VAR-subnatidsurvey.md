---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatidsurvey
canonical_label: "Lowest level of Subnational ID"
variable_name: subnatidsurvey
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: string

# --- Allowed output values ---
value_codes: null
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

# --- Derivation graph ---
derived_from:
  - VAR-subnatid1
  - VAR-subnatid2
  - VAR-subnatid3
  - VAR-subnatid4
derives_to:
  - VAR-geocode

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "sampling level"
    - "representative level"
    - "lowest level of representation"
    - "subnational"
  typical_section_names:
    - "Sampling design"
    - "Survey methodology"
    - "Geography"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatidsurvey"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Construction is survey-derived: record the most disaggregated representative area actually observed in the survey, preserving the raw code-label spelling variants as they appear in the data."
---

## Definition

`subnatidsurvey` is a country-specific, string variable that records the lowest
administrative level at which the survey is representative, restricted to the
level that is actually present in the survey's own `subnatid1` through
`subnatid4` hierarchy. It must be a direct value drawn from one of those
variables, not an independent geography code or label invented outside the
survey-admin structure.

## Conceptual intent

`subnatidsurvey` documents the effective level of subnational representativeness
of the survey, but only for the geography that is genuinely mappable within the
survey's own administrative hierarchy. It tells analysts the deepest level of
coverage actually supported by the survey's admin variables without drifting to
an external geo layer or an unsupported raw label.

## Construction notes

`subnatidsurvey` is a string variable with country-specific values and must be
constructed only from the survey's coded administrative geography already
represented in `subnatid1`, `subnatid2`, `subnatid3`, or `subnatid4`. In other
words, the value should be the same kind of code-label string already used in
those variables, such as "6 - Gjirokaster", "6 – Gjirokaster",
"6-GJIROKASTER", or "6-Gjirokaster".

The value is not an externally matched GMD crosswalk code and not an arbitrary
raw survey label. It must be exactly the string value from one of the survey's
admin variables corresponding to the lowest representative level in the current
survey design. Across surveys and years, the numeric code may change and the
spelling/variant may differ, but it remains the same value family as the
survey's own `subnatid` hierarchy.

`value_codes` is intentionally null because values derive from the country
survey design and cannot be enumerated in advance.

## Consistency checks

- `subnatidsurvey` must be a string variable.
- The recorded value must be the same code-label family as exactly one of
  `subnatid1`, `subnatid2`, `subnatid3`, or `subnatid4`.
- The level recorded must be consistent with the survey's documented sampling
  design and with the lowest representative level actually present in the
  survey's administrative hierarchy.
- Verify the recorded value matches the survey year/round and is not carried
  over from another round.

## Escalation triggers

- The survey documentation does not state the level at which the survey is
  representative.
- The recorded representative level conflicts with the level implied by the
  completeness pattern of `subnatid1` through `subnatid4`.

## Common mistakes

- Recording a finer level than the survey is actually representative at.
- Confusing `subnatidsurvey` with the presence or absence of a particular
  subnational identifier variable.
- Fabricating a value instead of reading it from the sampling design.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
