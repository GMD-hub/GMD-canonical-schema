---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-educat5
canonical_label: "Highest level of education completed (5 categories)"
variable_name: educat5
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
    label: "Primary incomplete"
  - value: 3
    label: "Primary complete but secondary incomplete"
  - value: 4
    label: "Secondary complete"
  - value: 5
    label: "Some tertiary/post-secondary"
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
derived_from:
  - VAR-educat7
derives_to:
  - VAR-educat4
  - VAR-educy
  - VAR-primarycomp

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-mineducatage
    condition: "Set educat5 to .c for individuals below mineducatage."
  - variable_id: VAR-educat7
    condition: "Must be defined and used as the source; educat5 is derived from
                educat7 via the stated recode."

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
    - "educational attainment"
  typical_section_names:
    - "Education"
    - "Schooling"
    - "Human capital"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, educat5"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "educat5 must be derived from educat7 if educat7 was defined, via the recode
          (3 4=3)(5=4)(6 7=5). If educat7 cannot be defined, educat5 is coded
          directly from the survey's own five categories. Do not guestimate; leave
          as missing if all five groups cannot be created."
---

## Definition

`educat5` records the highest level of education completed by an individual in
five ordered categories that balance comparability with more detail than the
four-category `educat4`:
1 = No education, 2 = Primary incomplete, 3 = Primary complete but secondary
incomplete, 4 = Secondary complete, 5 = Some tertiary/post-secondary.

## Conceptual intent

`educat5` provides an intermediate level of education detail between the coarse
four-category and the fine seven-category schemes. It is derived from `educat7`
where available so that the finer source information is not lost when
constructing the five categories.

## Construction notes

`educat5` must be derived from `educat7` if `educat7` was defined, using the
exact recode:

```stata
recode educat7 (3 4=3) (5=4) (6 7=5), gen(educat5)
```

If `educat7` cannot be defined, `educat5` is constructed directly from the
survey's own categories using the five-group definitions above.

Do not guestimate education levels. Value must be missing for individuals below
`mineducatage` (code `.c`). If the harmonizer cannot create all five groups,
leave the value missing.

## Consistency checks

- `educat5` must be internally consistent with `educat7` where both exist.
  Run a cross-tabulation (`tab educat7 educat5, m`) to confirm no contradictions.
- No individual below `mineducatage` should have a non-missing `educat5`.
- Cross-check `educat5` against age: a small child should not have secondary or
  tertiary completion.
- `educat5 = 5` (tertiary) requires a plausible age to have entered tertiary
  education.

## Escalation triggers

- Survey categories do not map cleanly to the five GMD groups.
- Incomplete primary and no education cannot be distinguished in the raw survey
  and the TTL has not resolved the ambiguity.
- Both `educat7` and direct five-category mapping are unavailable.

## Common mistakes

- Deriving `educat5` from raw survey data when `educat7` was available, silently
  losing detail.
- Applying the age restriction inconsistently across education variables.
- Guestimating education levels rather than leaving them missing.
- Using standard missing (`.`) instead of `.c` for the age restriction.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
