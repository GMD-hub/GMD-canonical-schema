---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatid4
canonical_label: "Subnational ID - fourth highest level"
variable_name: subnatid4
module_id: MOD-GEO
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

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
  - code: ".c"
    label: "Information not available because the subnational identifier was not collected in this survey"

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
    - "village"
    - "locality"
    - "fourth administrative level"
    - "lowest administrative level"
    - "subnational"
  typical_section_names:
    - "Identification"
    - "Geography"
    - "Sampling design"
    - "Household information"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatid4"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`subnatid4` is the country-specific categorical variable that identifies the
lowest level within a country's administrative structure, in some countries
effectively a village. Each household is assigned to the fourth-level
administrative division in which it is located.

## Conceptual intent

`subnatid4` locates households at the finest administrative level available,
enabling the most granular subnational statistics the survey supports.

## Construction notes

`subnatid4` is a string variable with country-specific categorical values and no
fixed harmonized codes. The value space is defined by the national
administrative classification and depends on the country parameter layer. Load
the country parameters and exceptions valid for the survey's ID year and record
the resulting classification in the do-file notes.

`value_codes` is intentionally null because values cannot be enumerated in
advance. Select codes from the country administrative codebook or an official
shapefile. Numeric raw entries are recoded to string format using the
"code - name" naming convention.

Surveys often do not collect or are not representative at this level; when
absent, use an explicit missing code and document the reason.

## Consistency checks

- `subnatid4` must be a string variable; verify no unformatted numeric codes.
- Every fourth-level division must nest under exactly one third-level division
  (`subnatid3`).
- No household may carry a standard missing (`.`) without an explicit extended
  missing code when the level was collected.
- Verify codes match the most recent administrative classification for the
  survey.

## Escalation triggers

- The survey's fourth-level administrative classification cannot be matched to
  an official codebook or shapefile.
- A third-level division contains codes inconsistent with the official nesting.
- The country administrative boundaries changed during the survey ID year and
  the correct classification cannot be determined.

## Common mistakes

- Leaving `subnatid4` numeric instead of string.
- Fabricating value codes instead of using the country administrative
  classification.
- Assigning fourth-level codes that do not nest within the recorded
  `subnatid3`.
- Recoding numeric entries without the "code - name" string convention.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
