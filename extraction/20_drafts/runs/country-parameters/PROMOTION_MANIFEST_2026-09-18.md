# Promotion Manifest - Country Parameter Draft Run

Date: 2026-09-19
Branch: feat/country-schema-v0.2
Source root: extraction/20_drafts/runs/country-parameters/
Validation snapshot: extraction/20_drafts/runs/check_result.json
Force extraction snapshot: extraction/20_drafts/runs/extract_force_all_result.json
GEO rerun snapshot: extraction/20_drafts/runs/geo_all_run_summary.json

## Current Inventory Snapshot

- Total YAML draft files (excluding contracts): 623
- ISO3 folders with at least one draft file: 206

Breakdown by parameter artifact:

- PARAM-EDU-LEVEL-CROSSWALK.yaml: 183
- PARAM-WASH-SANITATION-CROSSWALK.yaml: 146
- PARAM-WASH-WATER-CROSSWALK.yaml: 150
- PARAM-GEO-GMD-CROSSWALK.yaml: 144

## Run Status Summary

- GEO all-country rerun status: ok=true, count=144, success=144, failed=[]
- Full force extraction was executed with per-file JMP fault tolerance enabled.
- JMP/ISCED/GEO outputs are now generated under one force run command:
	- .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract --force

## Promotion Scope

This manifest is for human-guided promotion from extraction drafts into canonical country parameter files.

Promotion targets:

- country-parameters/countries/<ISO3>/parameters.md
- country-parameters/countries/<ISO3>/exceptions.md when exception logic is required

## Preconditions

1. Draft check is green (ok=true) from extraction_pipeline.country_inputs.cli check.
2. Human reviewer confirms mapping quality and provenance.
3. Effective dating follows rule: EDU effective_from is null unless clear era evidence exists.
4. For missing JMP outputs, verify per-file status in extract_force_all_result.json (no_rows, unchanged, error, invalid_iso3) before concluding data absence.

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
4. chore(geo): GEO crosswalk bulk refresh (when GEO regeneration is part of run)
