---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatid1
canonical_label: "Subnational ID - highest level"
variable_name: subnatid1
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
  - code: ".c"
    label: "Information not available because the subnational identifier was not collected in this survey"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-subnatidsurvey

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
    - "province"
    - "state"
    - "region"
    - "administrative division"
    - "first administrative level"
    - "subnational"
  typical_section_names:
    - "Identification"
    - "Geography"
    - "Sampling design"
    - "Household information"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatid1"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Construction is survey-derived: the encoded value and label are taken directly from the raw survey's administrative variable text and code, with spelling and punctuation variants preserved as they occur in the data."
---

## Definition

`subnatid1` is the country-specific categorical variable that identifies the
highest-level administrative subdivision within a country's administrative
structure, typically a province or state. Each household is assigned to the
first-level administrative division in which it is located.

## Conceptual intent

`subnatid1` provides the first-level subnational geographic context for every
household and underpins regional disaggregation across the GMD. Along with the
related subnational identifiers it supports analysis of regional inequities and
the construction of subnational statistics that are uniquely identifiable in a
global context.

## Construction notes

`subnatid1` is a string variable that holds country-specific categorical values
as they appear in the source survey. The value is constructed from the actual
survey data, not from the GMD geo crosswalk: it is a single text token made from
the survey's encoded code and the corresponding area label, for example
"6 - Gjirokaster", "6 – Gjirokaster", "6-GJIROKASTER", or "6-Gjirokaster".

The numeric part comes from the survey's own code for the first administrative
level; the text part comes from the label or area name recorded in the raw data.
The number can differ across surveys or years, and spelling/variant differences
must be preserved as they occur in the source data rather than normalized to a
single canonical case. The construction is therefore data-driven and survey-
anchored, with no requirement to retrieve a GMD crosswalk record for the value.

Because the value space is country-specific, `value_codes` is intentionally
left null and must not be fabricated. The agent should build the string from the
observed survey code and label combination and record any variant spelling or
punctuation differences in the do-file notes.

## Consistency checks

- `subnatid1` must be a string variable, not a numeric categorical; verify no
  numeric placeholder codes remain unformatted.
- No household may carry a standard missing (`.`) for `subnatid1`; every case
  must receive a valid country code or an explicit extended missing code.
- Cross-check against `subnatid2`: every second-level division must map to
  exactly one first-level division.
- Verify the codes used match the most recent administrative classification
  pertaining to that survey and that the mapping to the official shapefile is
  consistent.

## Escalation triggers

- The survey's first-level administrative classification cannot be located or
  matched to any official administrative codebook or shapefile.
- A household cannot be assigned to any first-level division.
- The country administrative boundaries changed during the survey ID year and
  the correct classification cannot be determined.

## Common mistakes

- Leaving `subnatid1` as a numeric categorical instead of a string variable.
- Fabricating value codes instead of using the country-specific administrative
  classification.
- Mixing administrative levels (e.g., assigning a second-level code to a
  household) within the same variable.
- Recoding numeric entries without the "code - name" string convention.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
