---
# ================================================================
# VARIABLE SPECIFICATION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
variable_id: VAR-countrycode
canonical_label: "ISO3 country code"
variable_name: countrycode
module_id: MOD-IDN
gmd_version: "3.0"
schema_version: "0.1"
status: draft
tier: 1

# --- Nature of the variable ---
unit_of_analysis: survey
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
    label: "Cannot be harmonized because country code is not available or does not meet harmonization definition"

# --- Derivation graph ---
derived_from: []
derives_to: []

# --- Country parameter declarations ---
country_parameters: []

# --- Prerequisites ---
prerequisites: []

# --- Cross-references ---
rules: []
exceptions: []
external_standards:
  - name: "ISO 3166-1 alpha-3 country codes (World Bank survey catalogue Appendix A)"
    url: "https://microdata.worldbank.org/index.php/home"

# --- Discovery hints ---
source_hints:
  question_keywords:
    - "country"
    - "country code"
    - "ISO3"
    - "ISO"
  typical_section_names:
    - "Identification"
    - "Survey metadata"
    - "Sample design"

# --- Provenance ---
provenance:
  source_document: "GMD_household_survey_harmonization.md"
  source_section: "ID Module (IDN), Mapping and Description of Variables, countrycode"
  extraction_method: manual
  extracted_on: "2026-08-14"
  human_reviewed: false
  reviewer: null
  notes: "Country code must be the 3-character ISO3 code used by the World Bank. Common legacy adjustments are documented in Lessons Learned and Challenges (KSV->XKX, TMP->TLS, WBG->PSE, ZAR->COD)."
---

## Definition

`countrycode` is a string variable that specifies the 3-character ISO3 country
code used by the World Bank to identify each country.

## Conceptual intent

`countrycode` labels each survey record with its country of origin so that
data can be correctly attributed across countries. Together with `year`, it
forms the core survey-level keys needed for cross-national comparison and
metadata linkage in the World Bank survey catalogue.

## Construction notes

Map the raw country identifier to the 3-character ISO3 code specified by the
World Bank. Although different naming conventions exist in raw data, the
harmonized value must use the ISO3 code to ensure data is appropriately
labeled.

Country codes must be updated to current ISO 3166-1 alpha-3 codes. Common
adjustments documented in the guidelines:

```
cap replace countrycode="XKX" if countrycode=="KSV"
cap replace countrycode="TLS" if countrycode=="TMP"
cap replace countrycode="PSE" if countrycode=="WBG"
cap replace countrycode="COD" if countrycode=="ZAR"
```

Ensure the variable is a three-letter string. Use
`cap confirm str3 var country` and throw an error otherwise.

## Consistency checks

- Every record must carry a valid three-letter ISO3 country code.
- The country code must match the known ISO3 code for the survey's country.
- No record should retain legacy or deprecated codes listed in the construction
  notes (KSV, TMP, WBG, ZAR).

## Escalation triggers

- The survey's country does not map cleanly to a single ISO3 code.
- The raw data uses a code not listed in ISO 3166-1 alpha-3 and no documented
  adjustment is available.

## Common mistakes

- Using a legacy, two-letter, or non-standard code instead of the ISO3 code.
- Forgetting to apply documented legacy-code conversions.
- Storing the code with trailing whitespace or mixed casing.

## Change log

| Date       | Version | Change        | Authority  |
|------------|---------|---------------|------------|
| 2026-08-14 | 0.1     | Initial draft | GPID Team  |
