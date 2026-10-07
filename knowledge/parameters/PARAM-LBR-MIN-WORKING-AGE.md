---
# ================================================================
# PARAMETER DEFINITION - GMD Canonical Variable Schema v0.1
# ================================================================

# --- Identity ---
parameter_id: PARAM-LBR-MIN-WORKING-AGE
parameter_name: "Minimum legal working age"
module_id: MOD-LBR
schema_version: "0.1"
status: draft
authority: "GPID Team"

# --- Nature of the parameter ---
kind: validation
value_type: integer
value_schema: null

# --- Where it is used ---
applies_to_variables: []

# --- Behavior when no country record exists ---
fallback_policy: undecided
global_default: null

# --- Provenance ---
provenance:
  source_document: "min_labor_age_panel_1990_2026.xlsx"
  extraction_method: manual
  extracted_on: "2026-10-04"
  human_reviewed: false
  reviewer: null
  notes: "Approved 2026-10-07. Source panel carries ILO Convention 138
          (C138) national minimum working age by country-year, with an
          optional ratification year per country. No labor variable spec is
          promoted to knowledge/ yet (all still in extraction/20_drafts/lbr/),
          so applies_to_variables is empty until a labor module variable
          (e.g. VAR-empstat, VAR-lstatus) is approved and updated to declare
          this parameter."
---

## Definition

Defines an integer threshold recording a country's legal minimum working age
over time, distinct from `VAR-minlaborage` (the survey's own age cutoff for
applying the labor module, which is a harmonized variable, not a legal fact).

## Why this is country specific

Minimum working age legislation differs across countries and periods (ILO
Convention 138 allows national variation, e.g. general minimum age, "light
work" age, and transitional provisions for developing countries). The
parameter is a validation input only and does not define or change harmonized
value codes.

## How the agent uses it

Once a variable spec declares this parameter, the agent selects the country
record whose validity window (`effective_from`/`effective_to`) contains the
survey ID year, and uses it to flag harmonized labor outcomes (e.g. employed
status) reported below the legal minimum age. No current variable spec
declares it.

## Fallback behavior

The fallback policy is undecided. The validator flags this parameter, and no
harmonization may rely on it until the GPID Team approves a policy.

## Data sources for populating values

Values are extracted from
`extraction/10_source/country-parameters-inputs/Labor/min_labor_age_panel_1990_2026.xlsx`
(sheet `panel_long`, columns `country`, `year`, `MINLABORAGE_C138`,
`ratified_by_year`), which carries ILO C138-based national minimum working age
by country-year. Country records were promoted to
`country-parameters/countries/<ISO3>/parameters.md` on 2026-10-07 via
`extraction_pipeline/country_inputs/cli.py promote --param-input labor-min-working-age`.

## Change log

| Date       | Version | Change                              | Authority |
|------------|---------|--------------------------------------|-----------|
| 2026-10-04 | 0.1     | Initial draft                        | GPID Team |
| 2026-10-07 | 0.1     | Approved; promoted to knowledge/     | GPID Team |
