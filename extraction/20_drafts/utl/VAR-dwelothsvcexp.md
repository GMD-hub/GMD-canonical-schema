---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-dwelothsvcexp
canonical_label: "Total annual consumption of other services relating to the dwelling"
variable_name: dwelothsvc_exp
module_id: MOD-UTL
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 2

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: atomic
data_type: numeric_continuous

# --- Allowed output values ---
value_codes:
  null
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
  - name: "COICOP 4.4.4 Other services relating to the dwelling"
    url: https://unstats.un.org/unsd/classifications/Econ
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Affordability, Essential variables - Water, Sanitation and Hygiene (WASH), dwelothsvc_exp"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: null
---

## Definition

`dwelothsvc_exp` is a continuous variable that refers to total annual household expenditures on other services relating to the dwelling.

## Conceptual intent

It captures miscellaneous dwelling services such as co-proprietor charges, security services, caretaking, and other services, following COICOP 4.4.4.

## Construction notes

Include co-proprietor charges in multi-occupied buildings and other miscellaneous dwelling services. Exclude household services (window cleaning, disinfecting, COICOP 5.6.2), bodyguards (12.7.0), and maintenance/repair of the dwelling (captured in `dwelmatexp`/`dwelsvcexp`, COICOP 4.3).

## Consistency checks

- Should not include maintenance and repair of the dwelling.
- Cross-check exclusions against household services and bodyguard expenditures.

## Escalation triggers

- The survey bundles other dwelling services with maintenance/repair.

## Common mistakes

- Including household services, bodyguards, or maintenance/repair.
- Treating co-proprietor charges as maintenance rather than other dwelling services.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
