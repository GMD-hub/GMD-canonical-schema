# Agent Session Handover - Country Schema v0.2

Date: 2026-09-19
Branch: feat/country-schema-v0.2
Repository: GMD-hub/GMD-canonical-schema

## 1) Executive summary

This phase moved from initial VNM-only extraction to full-country draft generation and operational hardening.

Major outcomes:
- GEO parameter contract and extraction flow implemented and scaled to all available GEO countries.
- GEO output semantics refined (dedupe by geo identity, boundary-aware effective dating, variant support for labels/variables).
- `subnatid` rule fixed to behave as `subnatid1` (level 1).
- `extract` gained incremental write behavior and `--force` support.
- JMP extraction loop hardened so a single bad workbook does not abort the whole run.
- Review/promotion operational docs were updated to reflect current workflow and counts.

## 2) Key logic decisions implemented

### 2.1 GEO variant representation

GEO rows now use plural variant fields:
- `survey_labels`
- `survey_variables`

Variants are merged and deduplicated per geo identity key.

### 2.2 GEO identity and dedupe

Row uniqueness is anchored on geo structure, not literal label text. This prevents duplicate rows caused by spelling/format variants.

### 2.3 GEO effective dating behavior

Records are segmented by boundary signature; the latest segment keeps:
- `effective_to: null`

### 2.4 Level inference rule for `subnatid`

`subnatid` is treated as level 1 (equivalent to `subnatid1`) for representative-level and `gmd_subnatid1` mapping.

### 2.5 Incremental extraction behavior

`extract` now skips rewrites when input+schema+extractor signature is unchanged.

State file:
- `extraction/20_drafts/runs/country-parameters/.incremental_state.json`

Override:
- `extract --force` forces full rewrite.

### 2.6 JMP resilience and language/identity fallback

JMP run loop now catches per-file extraction failures and continues.

Fallback behavior:
- if parser does not produce a valid ISO3, infer ISO3 from `JMP_<year>_<ISO3>_...` filename pattern.

Result payload now includes per-file JMP status details for diagnostics.

## 3) Commits made in this phase

Committed logical stages:
- `a48c33b` feat(country-inputs): add incremental extract and subnatid level-1 mapping
- `b609afc` chore(geo): add GEO crosswalk drafts for all countries

Note:
- Large pre-existing WASH/benchmark modifications were intentionally left out of those commits.

## 4) Force-run and generation status

Full-domain forced extraction was executed via:
- `.\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract --force`

GEO all-country rerun summary:
- `extraction/20_drafts/runs/geo_all_run_summary.json`
- `ok: true`, `count: 144`, `success: 144`, `failed: []`

Current draft inventory snapshot (excluding contracts):
- Total YAML: 623
- ISO3 folders: 206
- EDU drafts: 183
- WASH sanitation drafts: 146
- WASH water drafts: 150
- GEO drafts: 144

## 5) Operational documentation updated

Updated run/review/promotion docs:
- `extraction/20_drafts/runs/country-parameters/RUNBOOK_extraction_review_promotion.md`
- `extraction/20_drafts/runs/country-parameters/PROMOTION_MANIFEST_2026-09-18.md`
- `extraction/20_drafts/runs/country-parameters/PROMOTION_CHECKLIST_2026-09-18.md`

Checklist table now includes GEO column.

## 6) Known caveats and troubleshooting notes

1. Terminal execution context instability
- Some terminals intermittently parsed shell snippets as Python input, causing misleading syntax errors.
- Reliable execution path in this phase used VS Code tasks and direct Python script runners.

2. Locked workbook risk (JMP)
- Example observed: URY JMP workbook read failure when file lock existed.
- With current code, such failures are recorded and skipped per file rather than aborting entire run.

3. Output-capture inconsistencies
- Some `Out-File` captures were observed as empty despite successful execution.
- Preferred pattern is writing JSON directly from Python runner scripts.

## 7) Next steps for next agent

1. Validate JMP per-file status artifact quality
- Confirm `jmp_file_statuses` content completeness in force extract result output.

2. Add targeted rerun command for one ISO3/domain
- For faster recovery on locked files without full rerun.

3. Stabilize run output capture
- Consolidate on one canonical result-writer script for overnight runs.

4. Decide commit strategy for remaining modified benchmark/WASH files
- Many changes exist outside GEO commits and may need separate review commit(s).

## 8) Restart checklist

1. Confirm branch/state
- `git branch --show-current`
- `git status --short`

2. Inspect available source workbooks
- `.\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli inspect`

3. Force full extraction (all domains)
- `.\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli extract --force`

4. Validate drafts
- `.\\.venv\\Scripts\\python.exe -m extraction_pipeline.country_inputs.cli check`

5. GEO-only rerun if needed
- `.\\.venv\\Scripts\\python.exe extraction/20_drafts/runs/geo_all_run.py`

## 9) Governance reminder

Per AGENTS.md constraints, agent-authored artifacts should remain in staging paths unless explicitly instructed for promotion. This handover file remains under extraction-stage runtime docs.
