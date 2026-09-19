# Country Parameter Draft Runbook

Date: 2026-09-19
Branch: feat/country-schema-v0.2
Scope: Country parameter extraction drafts under extraction/20_drafts/runs/country-parameters/

## Purpose

This runbook defines the operating steps for extraction, review, and promotion of country parameter drafts.

## Guardrails

- Draft generation happens in extraction/20_drafts/runs/country-parameters/.
- Promotion to country-parameters/countries/<ISO3>/ is human-owned and must follow review approval.
- Universal schema ownership remains in knowledge/parameters/.
- For EDU level crosswalk drafts, effective_from defaults to null unless there is explicit era evidence.
- GEO crosswalk drafts are generated only through GEO pipeline logic and must not be hand-edited in bulk.

## Step 1: Extraction

Run from repository root.

1. Optional environment activation
   - .\\.venv\\Scripts\\Activate.ps1
2. Inspect available source workbooks
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli inspect
3. Force full refresh for all domains (ISCED + JMP + GEO)
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract --force
4. Incremental rerun (only changed input/schema outputs are rewritten)
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract

Expected extraction behavior in current branch:

- Invalid root-level or non-ISO3 draft paths are cleaned/skipped.
- Empty table extractions are skipped as draft outputs.
- Stale draft files for empty extractions are removed.
- Incremental state is stored in extraction/20_drafts/runs/country-parameters/.incremental_state.json.
- JMP extraction is fault-tolerant per file: a single bad workbook is logged and skipped instead of halting the full run.
- ISO3 fallback is attempted from JMP filename pattern when workbook identity parsing is incomplete.

### Domain-specific reruns

- GEO only, one country:
  - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli geo-example --iso3 <ISO3> --limit 0 --write
- GEO only, all countries in workbook:
  - .\\.venv\\Scripts\\python.exe extraction/20_drafts/runs/geo_all_run.py

## Step 2: Draft Validation

1. Validate extraction drafts
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli check
2. Optional stable capture to file
   - $out='extraction/20_drafts/runs/check_result.json'; .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli check | Out-File -FilePath $out -Encoding utf8; Write-Output "WROTE=$out"; Write-Output "EXIT=$LASTEXITCODE"

Interpretation:

- ok=true with exit code 0 means no blocking schema errors in draft set.
- warnings may exist for empty table placeholders and are non-blocking in this draft stage.

### Status artifacts generated during force runs

- extraction/20_drafts/runs/extract_force_all_result.json
- extraction/20_drafts/runs/geo_all_run_summary.json
- extraction/20_drafts/runs/check_result.json

If a file is empty due to terminal stream behavior, rerun using a direct Python script that writes JSON from in-process results.

## Step 3: Human Review

Review target is the generated draft set under extraction/20_drafts/runs/country-parameters/<ISO3>/.

Review checks:

1. Provenance quality
   - Source path accuracy
   - human_reviewed remains false before approval
2. Mapping quality
   - Target category assignment consistency
   - obvious duplicates and spelling normalization
3. Effective dating
   - EDU crosswalk effective_from stays null unless explicit era evidence exists
4. Country exceptions separation
   - Exception logic belongs in exceptions.md flow, not parameter value tables

## Step 4: Promotion

After review approval, move approved content into canonical country files:

- country-parameters/countries/<ISO3>/parameters.md
- country-parameters/countries/<ISO3>/exceptions.md (only when needed)

Promotion rules:

1. Preserve schema structure and IDs.
2. Do not alter universal structure in knowledge/.
3. Keep provenance fields complete.

## Step 5: Post-promotion Validation

Run repository-level validation:

- .\\.venv\\Scripts\\python.exe validation/validate_country_layer.py

Exit code 0 indicates no structural failures.

## Step 6: Commit Staging

Recommended logical commit order:

1. Extractor and validation behavior changes
2. Draft output refresh under extraction/20_drafts/runs/country-parameters/
3. Canonical country promotions under country-parameters/countries/
4. Validation evidence snapshots such as extraction/20_drafts/runs/check_result.json if intentionally versioned

Recommended additional split when GEO refresh is part of run:

5. GEO draft bulk refresh under extraction/20_drafts/runs/country-parameters/*/PARAM-GEO-GMD-CROSSWALK.yaml
