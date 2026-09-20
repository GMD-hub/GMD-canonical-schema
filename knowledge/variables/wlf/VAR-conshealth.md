---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-conshealth
canonical_label: "Household health expenditure component"
variable_name: conshealth
module_id: MOD-WLF
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: household
mapping_role: aggregate
data_type: numeric_continuous

value_codes: null
allowed_range:
  min: 0
  max: null

missing_codes:
  - code: ".a"
    label: "Variable not harmonized"
  - code: ".b"
    label: "Cannot be harmonized — no usable health expenditure module"

# --- Derivation graph ---
derived_from: []
derives_to:
  - VAR-welfare

country_parameters: []
prerequisites: []

# --- Aggregate: component structure ---
component_structure:
  operation: sum
  output_unit_of_analysis: household
  components:
    - component_id: health_medicines
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: health_services
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: health_lumpy_events
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: direct_value
      include: governed_by_switch
      governed_by: health_lumpy

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "collect all user-paid health expenditures and map them to the reference period"
  - stage: lumpy_treatment
    governed_by: health_lumpy
    rule: "apply the survey-specific health-lumpiness rule before assembly"
  - stage: component_assembly
    rule: "sum to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "health items are not automatically double-counted with other expenditure categories"
    - "where catastrophic spending is treated separately, preserve a clear audit trail"

# --- Cross-references ---
rules:
  - RULE-WLF-001
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3.1, pp. 42–46; health expenditures are typically included but the lumpy-shock treatment is survey-specific."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "health"
    - "medical"
    - "hospital"
    - "medicine"
    - "doctor"
  typical_section_names:
    - "Health"
    - "Medical expenses"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3.1, pp. 42–46"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 recommends inclusion of health expenditures in the aggregate, with the choice of how to treat lumpy episodes left to survey-specific implementation."
---

## Definition

`conshealth` is the household's health-related consumption component, covering
out-of-pocket medical and health-service expenditures in the reference period,
with any survey-specific treatment of lumpy or catastrophic episodes applied
according to the selected switch. It is a component of `VAR-welfare`.

## Conceptual intent

MV22 treats health as a legitimate welfare component in principle, but recognizes
that large episodic spending can be lumpy and noisy. The aggregate should include
health care when it reflects consumption of a welfare-enhancing service, while
the precise treatment of catastrophic episodes is a survey-specific decision.

## Construction notes

- Include routine health expenditures, medicines, and health services.
- Carry forward the survey's chosen treatment for large, infrequent spending.
- Do not assume that all health spending is equally represented in a common
  annual reference period.

## Escalation triggers

- The health-lumpiness rule is unset while the health module contains large or
  shock-driven claims.
- The module is present but the reported spending cannot be mapped to a usable
  welfare flow.
