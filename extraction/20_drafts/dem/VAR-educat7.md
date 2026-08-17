---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-educat7
canonical_label: "Highest education level completed, 7 categories"
variable_name: educat7
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: derived
data_type: categorical_ordered

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "No education"
  - value: 2
    label: "Incomplete primary"
  - value: 3
    label: "Primary complete"
  - value: 4
    label: "Incomplete secondary"
  - value: 5
    label: "Secondary complete"
  - value: 6
    label: "Post-secondary non-tertiary"
  - value: 7
    label: "Tertiary"
allowed_range: null

# --- Missing value codes ---
missing_codes:
  - code: ".c"
    label: "Education section not applied because the individual is below mineducatage"
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-educat4
  - VAR-educy
  - VAR-educat5
  - VAR-primarycomp

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-mineducatage
    condition: "Must be evaluated first. Set educat7 to .c for all
                individuals where age is below mineducatage."

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "highest level of education"
    - "highest grade completed"
    - "level of schooling"
  typical_section_names:
    - "Education"
    - "Schooling"
    - "Human capital"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, educat7 (calibration fixture)"
  extraction_method: manual
  extracted_on: "2026-08-07"
  human_reviewed: false
  reviewer: null
  notes: "Calibration fixture (not from the extraction pipeline). Carries seeded
          known defects for the calibration run; see known-answer-key.md.
          FIX: original rules list referenced RULE-EDU-999, which is unregistered and
          fails strict validation. The reference was dropped (rules: []). Remains a
          blocking issue until RULE-EDU-999 is registered or confirmed obsolete."
---

## Definition

`educat7` records the highest level of education completed by an individual in
seven ordered categories that preserve more detail than the four-category
`educat4`. It is the preferred source for deriving `educat4` and `educy` where
the survey supports seven-level coding.

## Conceptual intent

`educat7` is the finest-grained categorical education variable in the GMD. It
exists so that results requiring finer education distinctions (primary complete
vs incomplete, post-secondary) remain possible while still providing the four
broad groups through the derived `educat4`.

## Construction notes

Construct `educat7` by mapping the raw survey's education categories directly
to the seven GMD codes. When the raw survey does not distinguish the level of
detail required for all seven categories, collapse to the nearest available
level and document the mapping in the do-file notes.

Apply the age restriction (`mineducatage`) before coding, setting `educat7` to
`.c` below the cutoff. Do not guestimate an education level for any individual.

## Consistency checks

- `educat7` must be internally consistent with `educat4` where both exist: a
  cross-tabulation must show no contradictory values.
- No individual below `mineducatage` should have a non-missing `educat7`.
- Tertiary code (7) requires a plausible age for having entered tertiary
  education; flag cases below age 18.

## Escalation triggers

(TODO: escalate when mapping is ambiguous.)

## Common mistakes

- Mapping raw categories directly to `educat4` when `educat7` could have been
  constructed first, silently losing detail.
- Applying the age restriction inconsistently across education variables.
- Guestimating education levels when the survey is ambiguous instead of leaving
  the value missing and consulting the TTL.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-07 | 0.1     | Initial fixture | Calibration |
