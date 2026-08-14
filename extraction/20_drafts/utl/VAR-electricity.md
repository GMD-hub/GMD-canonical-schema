---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-electricity
canonical_label: "Access to electricity in dwelling"
variable_name: electricity
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: binary

# --- Allowed output values ---
value_codes:
  - value: 0
    label: "No"
  - value: 1
    label: "Yes"
allowed_range: null
# --- Missing value codes ---
missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized because data does not meet harmonization definition"
  - code: ".c"
    label: "Information not available because the item was not collected in this survey"
  - code: ".o"
    label: "Other value not covered by harmonized codes"
# --- Derivation graph ---
derived_from:
  []
derives_to: []
# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  []
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Access to Energy, electricity"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`electricity` is a dummy variable that specifies access to electricity in the household irrespective of source.

## Conceptual intent

It is the binary electricity access indicator, capturing whether the household has electricity from any source (mains, generator, solar, private company).

## Construction notes

Set to 1 if the household has electricity access from any source, 0 if not. This is independent of the source type captured in `elec_acc`.

## Consistency checks

- `electricity` equals 1 when `elec_acc` is 1, 2, or 3.
- Cross-check with `lightsource` (electricity category) where available.

## Escalation triggers

- The survey records electricity but the source or access status is ambiguous.

## Common mistakes

- Setting 1 for a household with a connection but no actual service.
- Treating a dwelling with no electrical service as having electricity access.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
