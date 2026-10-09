---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-subnatid2
canonical_label: "Subnational ID - second highest level"
variable_name: subnatid2
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

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards: []

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "district"
    - "second administrative level"
    - "subnational"
    - "administrative division"
  typical_section_names:
    - "Identification"
    - "Geography"
    - "Sampling design"
    - "Household information"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Geography (GEO), Mapping and Description of Variables, subnatid2"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Construction is survey-derived: the encoded value and label are taken directly from the raw survey's administrative variable text and code, with spelling and punctuation variants preserved as they occur in the data."
---

## Definition

`subnatid2` is the country-specific categorical variable that identifies the
second-highest level within a country's administrative structure, typically a
district. Each household is assigned to the second-level administrative
division in which it is located.

## Conceptual intent

`subnatid2` locates households at the second administrative level, enabling
finer regional disaggregation than `subnatid1`. It supports subnational
statistics and policy analysis at a more localized geographic granularity.

## Construction notes

`subnatid2` is a string variable with country-specific categorical values as
they appear in the source survey. The value is constructed from the actual
survey data, not from the GMD geo crosswalk: it is a single text token made from
the survey's encoded code and the corresponding area label, for example
"6 - Gjirokaster", "6 – Gjirokaster", "6-GJIROKASTER", or "6-Gjirokaster".

The numeric part comes from the survey's own code for the second administrative
level; the text part comes from the label or area name recorded in the raw data.
The number can differ across surveys or years, and spelling/variant differences
must be preserved as they occur in the source data rather than normalized to a
single canonical case. The construction is therefore data-driven and survey-
anchored, with no requirement to retrieve a GMD crosswalk record for the value.

Households for which the survey only records the first administrative level
may have `subnatid2` missing; use an explicit missing code and document the
reason.

## Consistency checks

- `subnatid2` must be a string variable. Verify no unformatted numeric
  placeholder codes remain.
- Every second-level division must nest under exactly one first-level division
  (`subnatid1`).
- No household may carry a standard missing (`.`) without an explicit extended
  missing code when the level was collected.
- Verify codes match the most recent administrative classification pertaining to
  that survey.

## Escalation triggers

- The survey's second-level administrative classification cannot be matched to
  an official codebook or shapefile.
- A first-level division contains second-level codes that are inconsistent with
  the official nesting.
- The country administrative boundaries changed during the survey ID year and
  the correct classification cannot be determined.

## Common mistakes

- Leaving `subnatid2` numeric instead of string.
- Fabricating value codes instead of using the country administrative
  classification.
- Assigning second-level codes that do not nest within the recorded
  `subnatid1`.
- Recoding numeric entries without the "code - name" string convention.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
