---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-educat4
canonical_label: "Highest education level completed, 4 categories"
variable_name: educat4
module_id: MOD-DEM
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: individual
mapping_role: derived_preferred
data_type: categorical_ordered

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "No education"
  - value: 2
    label: "Primary (complete or incomplete)"
  - value: 3
    label: "Secondary (complete or incomplete)"
  - value: 4
    label: "Tertiary (complete or incomplete)"
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
# Listed in order of preference. educat7 must be attempted before educat5.
# Direct mapping from raw survey data is the last resort only when
# neither educat7 nor educat5 can be defined.
derived_from:
  - VAR-educat7
  - VAR-educat5
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites:
  - variable_id: VAR-mineducatage
    condition: "Must be evaluated first. Set educat4 to .c for all
                individuals where age is below mineducatage."

# --- Cross-references ---
rules:
  - RULE-EDU-001
  - RULE-EDU-002
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
    - "Demographics"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Demography (DEM), Mapping and Description of Variables, educat4"
  extraction_method: manual
  extracted_on: "2026-06-25"
  human_reviewed: false
  reviewer: null
  notes: "Guidelines state: at the bare minimum, this variable must be generated.
          CSV shows basic=0 for educat4, which likely means it is in a separate output
          file rather than the basic file. Tier=1 retained per guidelines language.
          Needs team clarification."
---
## Definition

`educat4` records the highest level of education completed by an individual,
collapsed into four broad groups that are comparable across countries. It is
the minimum required education variable in the GMD: every harmonized survey
must contain it.

## Conceptual intent

`educat4` provides the broadest and most internationally comparable education
grouping in the GMD. Its four categories are designed to be achievable even in
surveys where finer distinctions, such as primary complete versus incomplete,
cannot be reliably drawn. It is the fallback anchor for all education analysis.

## Construction notes

Follow this order of preference strictly. Do not skip to a lower-preference
path if a higher-preference path is possible.

**Path 1 (preferred): derive from `educat7`.**

If `educat7` has been defined for this survey, apply the following recode
exactly as stated in the GMD guidelines:

```stata
recode educat7 (1=1) (2 3=2) (4 5=3) (6 7=4), gen(educat4)
```

**Path 2 (fallback): derive from `educat5`.**

If `educat7` cannot be defined but `educat5` has been defined, apply the
following recode. Note: this recode is a derived convention not explicitly
stated in the GMD guidelines. Flag its use in the do-file notes.

```stata
recode educat5 (1=1) (2=2) (3 4=3) (5=4), gen(educat4)
```

**Path 3 (last resort): map directly from raw survey data.**

Only when neither `educat7` nor `educat5` can be defined, map the raw survey
categories directly to the four-group scheme. When this path is used, `educat4`
is behaving as an atomic variable for this survey. Document this explicitly in
the do-file notes and the Harmonization Specification, and escalate to the reviewer.

**Age restriction (applies to all paths).**

Set `educat4` to `.c` for all individuals whose age is below `mineducatage`.
Do not guestimate education levels for these individuals under any circumstances.

## Consistency checks

- `educat4` must be internally consistent with `educat7` and `educat5` wherever
  those variables exist. Run a cross-tabulation to verify no individual has
  contradictory values across the three variables.
- No individual below `mineducatage` should have a non-missing value for
  `educat4`.
- In ECA region surveys, it is expected and correct for individuals under 15 or
  16 to have missing education values due to compulsory education systems.
- If `educat4 = 4` (tertiary), the individual should be old enough to have
  plausibly started tertiary education. Flag cases below age 18 for review.

## Escalation triggers

- Cannot distinguish "no education" from "incomplete primary" in the raw survey
  and the survey documentation does not resolve the ambiguity.
- Survey categories do not map cleanly to the four GMD groups under any
  reasonable interpretation.
- Neither `educat7` nor `educat5` can be defined and direct raw mapping is
  also not possible.
- More than 5 percent of adults at or above `mineducatage` have missing
  `educat4` for reasons other than the age restriction.

## Common mistakes

- Generating `educat4` directly from raw data when `educat7` or `educat5`
  could have been defined first. This creates silent inconsistencies between
  the education variables.
- Applying the age restriction inconsistently across education variables within
  the same survey.
- Guestimating education levels when the survey is ambiguous, rather than
  leaving as missing and consulting the TTL.
- In ECA surveys, attempting to fill in education for individuals below the
  compulsory schooling age cutoff.
- Using standard Stata missing (`.`) for the age restriction instead of `.c`.

This is just a test. This has more explanation.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-06-25 | 0.1     | Initial draft | GPID Team  |