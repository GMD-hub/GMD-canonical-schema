---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-consdurables
canonical_label: "Household durables consumption component"
variable_name: consdurables
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
    label: "Cannot be harmonized — durable-use flow unavailable"

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
    - component_id: durable_user_cost
      native_unit_of_analysis: household
      roll_up_key: hhid
      value_path: estimate
      include: governed_by_switch
      governed_by: durables_treatment
    - component_id: durable_acquisition
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present
      governed_by: durables_treatment

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: durable_flow_definition
    rule: "define the service flow as a user-cost or equivalent stream, not the purchase price"
  - stage: input_recovery
    rule: "recover current value, age, depreciation, and real-interest inputs when the survey permits"
  - stage: component_assembly
    rule: "sum the durable flow to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "do not treat purchase price as current consumption"
    - "if no credible durable flow exists, omit the durable category rather than use acquisition values"

# --- Cross-references ---
rules:
  - RULE-WLF-001
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.4, pp. 48–55; durable goods should be measured as a service flow, not as the purchase price."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "durable"
    - "vehicle"
    - "appliance"
    - "furniture"
    - "user cost"
  typical_section_names:
    - "Durables"
    - "Household assets"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.4, pp. 48–55"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 recommends durable consumption as a flow of services rather than an acquisition expenditure; the practical default is user cost when data permit."
---

## Definition

`consdurables` is the household's consumption of durable goods as a flow of
services across the reference period. It is built from a user-cost or equivalent
service estimate, not from purchase prices, and is a component of `VAR-welfare`.

## Conceptual intent

The essential MV22 principle is that a durable good contributes consumption over
its lifetime, not solely at the moment of purchase. Acquisition expenditures are
misleading for welfare measurement because they reflect a stock purchase rather
than the service flow consumed during the survey period.

## Construction notes

- Prefer a user-cost estimate when asset values, age, and depreciation inputs are
  available.
- If a reliable flow cannot be estimated, omit the durable category rather than
  using acquisition prices.
- Keep border cases with semi-durables and borderline items under item-level
  classification.

## Escalation triggers

- The durable-treatment switch is unset and the household has obvious durable
  service flows or acquisitions to model.
- Purchase data are present but there is no credible service-flow estimate.
