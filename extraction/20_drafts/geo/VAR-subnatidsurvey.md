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
derived_from: []
derives_to: []

# --- Country parameter declarations ---
# Not a routing instruction. The agent always loads the country layer.
country_parameters: []

# --- Prerequisites ---
prerequisites: []

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
  notes: null
---

## Definition

`subnatidsurvey` is a country-specific, string variable that records the lowest
level of the administrative structure at which the survey is representative. In
most cases it equals `subnatid1` or `subnatid2`, but it may be a distinct
classification when the lowest level is urban/rural or another regional
categorization that cannot be mapped to the subnational identifiers.

## Conceptual intent

`subnatidsurvey` documents the effective level of subnational representativeness
of the survey regardless of how that lowest level maps to the administrative
code. It informs analysts about the geographic granularity at which survey
estimates are reliable.

## Construction notes

`subnatidsurvey` is a string variable with country-specific values and no fixed
harmonized codes. It records the lowest representative level as reported in the
survey's sampling design, whether that maps to `subnatid1`, `subnatid2`, or a
non-administrative regional classification (urban/rural or other). This depends
on the country parameter layer: load the country parameters and exceptions valid
for the survey's ID year.

`value_codes` is intentionally null because values derive from the country
survey design and cannot be enumerated in advance. Values are recorded using the
same string convention and administrative names as the subnational identifiers.

## Consistency checks

- `subnatidsurvey` must be a string variable.
- The level recorded must be consistent with the survey's documented sampling
  design and with the coarsest of `subnatid1` through `subnatid4` for which the
  survey is representative.
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
