---
# ================================================================
# VARIABLE SPECIFICATION — GMD Canonical Variable Schema v0.1
# mapping_role: aggregate
# ================================================================

# --- Identity ---
variable_id: VAR-conscommunications
canonical_label: "Household communications and information services consumption component"
variable_name: conscommunications
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
    label: "Cannot be harmonized — communication module unusable"

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
    - component_id: communication_services
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: telecom_usage
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: always
    - component_id: communication_equipment
      native_unit_of_analysis: item
      roll_up_key: hhid
      value_path: direct_value
      include: when_present

# --- Aggregate: construction pipeline ---
construction_pipeline:
  - stage: value_normalization
    rule: "sum direct communication expenditures and map them to the household reference period; do not assume quantity × unit price is the standard reporting format"
  - stage: recall_annualization
    scope: all rows
    rule: "value * (365 / recall_days)"
  - stage: component_assembly
    rule: "sum item rows to household via hhid"

# --- Aggregate: reconciliation ---
reconciliation:
  internal:
    - "exclude communication equipment that is a durable acquisition if treated separately"
    - "sum of included rows equals the communications subtotal"

# --- Cross-references ---
rules:
  - RULE-WLF-004
  - RULE-WLF-005
  - RULE-WLF-007
exceptions: []
external_standards:
  - name: "MV22, §4.3, pp. 35–40; communication services and related non-durable information expenditures are included."
    url: "http://documents.worldbank.org/curated/en/099225003092220001"

source_hints:
  question_keywords:
    - "telephone"
    - "internet"
    - "communication"
    - "mobile"
    - "data"
  typical_section_names:
    - "Communications"
    - "Telephone and internet"

provenance:
  source_document: "extraction/sources/mancini-vecchi-2022.txt"
  source_section: "§4.3, pp. 35–40"
  extraction_method: manual
  extracted_on: "2026-08-27"
  human_reviewed: false
  reviewer: null
  notes: "MV22 includes communication services and related information-service expenditures as ordinary nondurable consumption."
---

## Definition

`conscommunications` is the household's communication and information
services expenditure, including telecom service fees and similar services that
reflect current consumption. It is a component of `VAR-welfare`.

## Conceptual intent

Communication services are standard current-use items. Durable equipment such as
phones or modems is treated with the durable boundary rule and should not be
mixed into the current-flow component unless the survey explicitly maps them as
service expenditure.

## Construction notes

- Include recurring communication services and internet-related charges.
- Exclude durable communication equipment when it is capital-like.
- Annualize where the recall period differs from the common reference period.

## Escalation triggers

- The communication module is reported but cannot be classified into service
  consumption versus durable acquisition.
- There are no usable communication charges but the survey appears to contain a
  mixed service/equipment file.
