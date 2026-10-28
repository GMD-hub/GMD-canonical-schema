---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-watersource
canonical_label: "Main source of drinking water"
variable_name: water_source
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
    label: "Piped water into dwelling"
  - value: 2
    label: "Piped water to yard/plot"
  - value: 3
    label: "Public tap or standpipe"
  - value: 4
    label: "Tubewell or borehole"
  - value: 5
    label: "Protected dug well"
  - value: 6
    label: "Protected spring"
  - value: 7
    label: "Bottled water"
  - value: 8
    label: "Rainwater"
  - value: 9
    label: "Unprotected spring"
  - value: 10
    label: "Unprotected dug well"
  - value: 11
    label: "Cart with small tank/drum"
  - value: 12
    label: "Tanker-truck"
  - value: 13
    label: "Surface water"
  - value: 14
    label: "Other"
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
derives_to:
  - VAR-impwatrec
# --- Country parameter declarations ---
country_parameters:
  - PARAM-WASH-WATER-CROSSWALK

# --- Correspondence output (machine-readable construction recipe) ---
correspondence_output:
  method: external_standard
  standard: "JMP-2025"
  level: water_source
  map:
    "tap_water": [1, 2, 3]
    "tap_water.piped_on_premises": [1, 2]
    "tap_water.piped_on_premises.piped_water_into_dwelling": 1
    "tap_water.piped_on_premises.piped_water_to_yard_plot": 2
    "tap_water.public_tap_standpipe": 3
    "ground_water": [4, 5, 6, 9, 10]
    "ground_water.protected_ground_water": [4, 5, 6]
    "ground_water.unprotected_ground_water": [9, 10]
    "ground_water.protected_wells_or_springs": [5, 6]
    "ground_water.protected_wells_or_springs.private": [5, 6]
    "ground_water.protected_wells_or_springs.public": [5, 6]
    "ground_water.protected_wells_or_springs.other": [5, 6]
    "ground_water.unprotected_wells_or_springs": [9, 10]
    "ground_water.unprotected_wells_or_springs.private": [9, 10]
    "ground_water.unprotected_wells_or_springs.public": [9, 10]
    "ground_water.unprotected_wells_or_springs.other": [9, 10]
    "ground_water.all_wells": [4, 5, 10]
    "ground_water.all_wells.private": [4, 5, 10]
    "ground_water.all_wells.public": [4, 5, 10]
    "ground_water.all_wells.other": [4, 5, 10]
    "ground_water.tubewell_borehole": 4
    "ground_water.tubewell_borehole.private": 4
    "ground_water.tubewell_borehole.public": 4
    "ground_water.tubewell_borehole.other": 4
    "ground_water.traditional_wells": [5, 10]
    "ground_water.traditional_wells.private": [5, 10]
    "ground_water.traditional_wells.public": [5, 10]
    "ground_water.traditional_wells.other": [5, 10]
    "ground_water.protected_well": 5
    "ground_water.protected_well.private": 5
    "ground_water.protected_well.public": 5
    "ground_water.protected_well.other": 5
    "ground_water.unprotected_well": 10
    "ground_water.unprotected_well.private": 10
    "ground_water.unprotected_well.public": 10
    "ground_water.unprotected_well.other": 10
    "ground_water.all_springs": [6, 9]
    "ground_water.all_springs.private": [6, 9]
    "ground_water.all_springs.public": [6, 9]
    "ground_water.all_springs.other": [6, 9]
    "ground_water.protected_spring": 6
    "ground_water.protected_spring.private": 6
    "ground_water.protected_spring.public": 6
    "ground_water.protected_spring.other": 6
    "ground_water.unprotected_spring": 9
    "ground_water.unprotected_spring.private": 9
    "ground_water.unprotected_spring.public": 9
    "ground_water.unprotected_spring.other": 9
    "rainwater": 8
    "rainwater.covered_cistern_tank": 8
    "rainwater.uncovered_cistern_tank": 8
    "packaged_water": 7
    "packaged_water.bottled_water": 7
    "packaged_water.sachet_water": 7
    "surface_water": 13
    "surface_water.river": 13
    "surface_water.lake": 13
    "surface_water.dam": 13
    "surface_water.pond": 13
    "surface_water.stream": 13
    "surface_water.irrigation_channel": 13
    "surface_water.other": 13
    "other_improved_sources": [11, 12, 14]
    "other_improved_sources.cart_with_small_tank_drum": 11
    "other_improved_sources.tanker_truck_provided": 12
    "other_improved_sources.other": 14
    "other_improved_sources.other#2": 14
    "other_non_improved": 14
    "other_non_improved.other": 14
    "other_non_improved.other#2": 14

# --- Universe / skip gate ---
gates: []

# --- Cross-references ---
rules:
  - RULE-WASH-001
exceptions: []
external_standards:
  - name: "WHO/UNICEF JMP"
    url: https://washdata.org
# --- Discovery hints ---
source_hints:
  question_keywords: []
  typical_section_names: []

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "Utilities (UTL), Access to Services, Water, Sanitation and Hygiene (WASH), water_source"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "2026-10-27 (proposed, pending GPID Team approval): added derives_to VAR-impwatrec (the
          guidelines: water_source feeds imp_wat_rec), PARAM-WASH-WATER-CROSSWALK (the
          national route), RULE-WASH-001, and correspondence_output (until now kept
          only in the survey-harmonization vendored copy).
          2026-10-28 (proposed): correspondence_output is the JMP-2025 anchor: each node of
          the JMP country-file water tree (jmp_id, which the national categories carry) ->
          its water_source code, transcribed from the gmd and spans fields of the JMP
          master tree (extraction/10_source/country-parameters-inputs, gmd_wash_concordance).
          A coarse node maps to the list of codes it spans. Tap water > Other has no
          water_source code (imp_wat_rec is set for it directly, VAR-impwatrec). The cart node
          takes code 11 (Cart with small tank/drum); the tree's gmd token placed it with tanker
          trucks (12). It replaces the category_keyword placeholder."
---

## Definition

`water_source` is a categorical variable that indicates the main source of drinking water for the household, harmonized into fourteen standardized categories.

## Conceptual intent

It is the core WASH water access indicator, distinguishing improved from unimproved sources and feeding the `piped`, `piped_to_prem`, and `imp_wat_rec` variables.

## Construction notes

Code from `water_original` unless otherwise justified, referring to the survey questionnaire for the best match. If several water types are used, record only the main source. If the source differs between wet and dry season, use the dry-season source. Apply the detailed category definitions (e.g. piped into dwelling means a service pipe with in-house plumbing).

## Consistency checks

- `piped` equals 1 if `water_source` is 1, 2, or 3.
- `piped_to_prem` equals 1 only if `water_source` is 1 or 2.
- `imp_wat_rec` equals 1 for codes 1 through 8.

## Escalation triggers

- The survey uses a water category that does not map cleanly to any standardized code.
- Water source differs by season and the dry-season source cannot be determined.

## Common mistakes

- Coding bottled water (7) as if it were a protected source.
- Treating a borehole with a reticulated piped system as tubewell instead of piped water.
- Not consulting the questionnaire and guessing the correspondence.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
| 2026-10-27 | 0.2     | Add derives_to VAR-impwatrec, PARAM-WASH-WATER-CROSSWALK, RULE-WASH-001 and correspondence_output | GPID Team (proposed) |
| 2026-10-28 | 0.3     | correspondence_output: JMP-2025 anchor (jmp_id -> water_source code or span), replacing category_keyword; external_standards JMP | GPID Team (proposed) |
