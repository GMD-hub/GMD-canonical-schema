---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-elecacc
canonical_label: "Access to electricity"
variable_name: elec_acc
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: categorical

# --- Allowed output values ---
value_codes:
  - value: 1
    label: "Yes, public/quasi-public"
  - value: 2
    label: "Yes, private"
  - value: 3
    label: "Yes, source unstated"
  - value: 4
    label: "No"
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
  source_section: "Utilities (UTL), Access to Services, Access to Energy, elec_acc"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`elec_acc` is a categorical variable that identifies the type of connection to electricity, distinguishing the source of supply.

## Conceptual intent

It captures both the fact of electricity access and whether it is public/quasi-public (mains), private (generator, solar, private company), or source unstated.

## Construction notes

Public/quasi-public refers to mains electricity supply from power stations; private refers to generator, solar, or private company supply. Use 3 when access exists but the source is unstated, 4 for no access. Having a connection says nothing about the actual service quality.

## Consistency checks

- `electricity` equals 1 when `elec_acc` is 1, 2, or 3.
- Cross-check against `lightsource` where electricity is the main light source.
- Cross-check quality against `elechracc` where available.

## Escalation triggers

- The survey records access but not the source of electricity.

## Common mistakes

- Treating generator or solar access as public mains electricity.
- Coding access with unstated source as missing instead of 3.
- Confusing connection type with the quality of the electrical service delivered.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
