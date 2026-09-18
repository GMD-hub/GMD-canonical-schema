# Country Parameter Draft Runbook

Date: 2026-09-18
Branch: feat/country-schema-v0.2
Scope: Country parameter extraction drafts under extraction/20_drafts/runs/country-parameters/

## Purpose

This runbook defines the operating steps for extraction, review, and promotion of country parameter drafts.

## Guardrails

- Draft generation happens in extraction/20_drafts/runs/country-parameters/.
- Promotion to country-parameters/countries/<ISO3>/ is human-owned and must follow review approval.
- Universal schema ownership remains in knowledge/parameters/.
- For EDU level crosswalk drafts, effective_from defaults to null unless there is explicit era evidence.

## Step 1: Extraction

Run from repository root.

1. Optional environment activation
   - .\\.venv\\Scripts\\Activate.ps1
2. Inspect available source workbooks
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli inspect
3. Extract drafts for all discovered inputs
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract

Expected extraction behavior in current branch:

- Invalid root-level or non-ISO3 draft paths are cleaned/skipped.
- Empty table extractions are skipped as draft outputs.
- Stale draft files for empty extractions are removed.

## Step 2: Draft Validation

1. Validate extraction drafts
   - .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli check
2. Optional stable capture to file
   - $out='extraction/20_drafts/runs/check_result.json'; .\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli check | Out-File -FilePath $out -Encoding utf8; Write-Output "WROTE=$out"; Write-Output "EXIT=$LASTEXITCODE"

Interpretation:

- ok=true with exit code 0 means no blocking schema errors in draft set.
- warnings may exist for empty table placeholders and are non-blocking in this draft stage.

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
