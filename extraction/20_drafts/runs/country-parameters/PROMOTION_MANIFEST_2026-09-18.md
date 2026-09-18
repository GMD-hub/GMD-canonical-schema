# Promotion Manifest - Country Parameter Draft Run

Date: 2026-09-18
Branch: feat/country-schema-v0.2
Source root: extraction/20_drafts/runs/country-parameters/
Validation snapshot: extraction/20_drafts/runs/check_result.json

## Current Inventory Snapshot

- Total YAML draft files (excluding contracts): 400
- ISO3 folders with at least one draft file: 197

Breakdown by parameter artifact:

- PARAM-EDU-LEVEL-CROSSWALK.yaml: 183
- PARAM-WASH-SANITATION-CROSSWALK.yaml: 107
- PARAM-WASH-WATER-CROSSWALK.yaml: 110

## Promotion Scope

This manifest is for human-guided promotion from extraction drafts into canonical country parameter files.

Promotion targets:

- country-parameters/countries/<ISO3>/parameters.md
- country-parameters/countries/<ISO3>/exceptions.md when exception logic is required

## Preconditions

1. Draft check is green (ok=true) from extraction_pipeline.country_inputs.cli check.
2. Human reviewer confirms mapping quality and provenance.
3. Effective dating follows rule: EDU effective_from is null unless clear era evidence exists.

## Promotion Procedure (Per Country)

1. Open each source draft in extraction/20_drafts/runs/country-parameters/<ISO3>/.
2. Merge approved records into country-parameters/countries/<ISO3>/parameters.md.
3. Keep schema_version, IDs, and provenance shape aligned with canonical schema.
4. Add or update exceptions only in exceptions.md where needed.

## Post-Promotion Verification

Run:

- .\\.venv\\Scripts\\python.exe validation/validate_country_layer.py

If exit code is non-zero, resolve structural failures before commit.

## Commit Recommendation

1. chore(country-inputs): extraction and check behavior updates
2. chore(country-inputs): refresh extraction draft outputs
3. feat(country-parameters): promote reviewed country parameter records
