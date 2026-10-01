---
date: 2026-09-30
title: "Replacing the fixed tertiary-year table with per-country years-of-schooling derived from the education crosswalk"
category: "data-quality"
language: "Python"
tags: [gmd, cvs, educy, educat4, isced, crosswalk, pydantic, schema-migration, pipeline-wiring, country-parameters]
root-cause: "RULE-EDU-003/VAR-educy depended on PARAM-EDU-YEARS-BY-LEVEL (an unpopulated, undecided-fallback mapping) and a flat GMD-wide tertiary-year table, neither of which reflected real per-country program length. The populated PARAM-EDU-LEVEL-CROSSWALK had the raw rows needed to derive precise years-of-schooling but no derivation logic and no schema fields to hold the result."
severity: "P2"
---

# Replacing the fixed tertiary-year table with per-country years-of-schooling derived from the education crosswalk

## Problem

`VAR-educy` (years of education) needed a precise, country-specific way to
assign years of schooling for individuals whose survey data goes beyond
simple grade 1-12 numbering (tertiary, vocational, and other post-secondary
levels). The existing design (`RULE-EDU-003` v0.1) used:

- `PARAM-EDU-YEARS-BY-LEVEL`, a generic primary/lower-secondary/upper-secondary
  duration mapping with `fallback_policy: undecided` and only placeholder,
  unverified country records (e.g. `PER`).
- A flat, GMD-wide fixed table (BA +4/+2, MA +6/+5, PhD +8/+7 years) for
  tertiary completion, which cannot reflect real variation in program length
  across countries (e.g. Vietnam's Bachelor's programs range 16-18 cumulative
  years depending on field).

Meanwhile, `PARAM-EDU-LEVEL-CROSSWALK` already had real, extracted,
per-country ISCED crosswalk rows (`country_entry_id`, `isced_level`,
`duration_years`, `national_label_en`, ...) for 183 countries, but no logic
existed to turn those rows into a cumulative years-of-schooling value, and no
schema fields existed to store one.

## Root Cause

- Two parallel parameters existed for "years by education level":
  `PARAM-EDU-YEARS-BY-LEVEL` (never populated with real data, generic
  3-bucket mapping) and `PARAM-EDU-LEVEL-CROSSWALK` (real per-country rows,
  but originally built only to support `VAR-educat4` categorical mapping).
- `schema/country_parameters.py`'s table-row validator enforces **exact** key
  equality (`set(row.keys()) != expected`) against the registry's
  `row_schema`. Extending `row_schema` with new derived fields therefore
  invalidates every existing country's committed rows **immediately** until
  they are rewritten to match — the schema change and the data migration must
  land together, not in separate steps.
- The real ISCED-source extraction pipeline
  (`extraction_pipeline/country_inputs/cli.py` `run_extract` +
  `transform.py`) is architecturally separate from the standalone
  `education_pathways.py` derivation tool that was originally built to
  compute years-of-schooling. Without wiring them together, rerunning the
  ISCED extraction would silently regress the data (drop the derived fields).

## Solution

1. **Designed the rule logic first, in plain language, before touching any
   schema** (per-individual path selection: direct years reported → enrolled
   grade 1-12 arithmetic → enrolled post-12 with/without progress detail →
   not-enrolled grade 1-12 arithmetic → not-enrolled post-12 ordinal year →
   not-enrolled named level via crosswalk lookup → `.b`). See
   `knowledge/rules/module/dem/RULE-EDU-003.md` (v0.2) for the full IF/THEN.

2. **Extended the row-level type system** (`schema/parameter.py`,
   `schema/country_parameters.py`) to add `integer_or_null` (nullable years
   value, for rows needing human review) and `array_of_string` (parent IDs,
   computation path, review flags) as valid `row_schema` value types.

3. **Extended `PARAM-EDU-LEVEL-CROSSWALK`** (`knowledge/parameters/PARAM-EDU-LEVEL-CROSSWALK.md`,
   v0.2 → v0.3) with 5 derived fields: `parent_country_entry_ids`,
   `cum_years_schooling`, `cum_years_computation_path`, `cum_years_status`
   (`computed` | `review_required`), `review_flags`. Added `VAR-educy` to
   `applies_to_variables`.

4. **Retired `PARAM-EDU-YEARS-BY-LEVEL` entirely**: deleted
   `knowledge/parameters/PARAM-EDU-YEARS-BY-LEVEL.md`, removed its two
   placeholder records from `country-parameters/countries/PER/parameters.md`,
   removed its `knowledge/index.md` row. Repointed the 4 tests that used it
   purely as a generic fixture parameter (not for its specific identity) to
   `PARAM-DEM-MIN-MARRIAGE-AGE` instead: `tests/test_effective_dating.py`,
   `tests/test_overlap_detection.py`, `tests/test_table_parameter_values.py`,
   `tests/test_bundle_integrity.py`.

5. **Built the derivation algorithm** in
   `extraction_pipeline/country_inputs/education_pathways.py`:
   - `enrich_rows(rows)` — given a flat list of crosswalk rows (each with
     `country_entry_id`, `isced_level`, `duration_years`, `national_label_en`),
     infers `parent_country_entry_ids` per row (by ISCED level adjacency and
     general-vs-vocational/adult-track label heuristics), then computes
     `cum_years_schooling` via memoized recursion over the parent graph.
     ISCED level `'0'` rows are excluded from totals. Rows with multiple
     candidate parents select the **minimum**-years path and are flagged
     `review_flags: ["minimum parent path selected from: ..."]` (visible,
     not hidden — "fail loud" per `AGENTS.md`).
   - `infer_period`/`infer_country`/`run_sweep` — a standalone sweep over
     **committed** country data, for ad-hoc review of the derivation logic
     without needing real ISCED source files. Writes to
     `extraction/20_drafts/runs/country-parameters/education-pathways/<ISO3>.yaml`
     plus a summary at `extraction/25_agent_review/education-pathways-summary.yaml`.
   - `promote_country`/`promote_all` — rewrites a country's committed
     `PARAM-EDU-LEVEL-CROSSWALK` rows with the enriched rows from whichever
     draft is available (see `_load_periods_for_promotion`, which **prefers
     the real `cli.py extract` draft** and falls back to the standalone sweep
     draft).

6. **Closed the real extraction-pipeline gap**: wired `enrich_rows()` directly
   into `extraction_pipeline/country_inputs/cli.py`'s `run_extract()`, right
   after `country_entry_id` assignment, for the education (ISCED) path. Before
   this, rerunning the real extraction (`cli.py extract`) would have produced
   rows **without** the derived fields and immediately failed the registry's
   row-key validation. Verified against a real source file
   (`ISCED_2011_Mapping_Viet_Nam.xlsx`) that a fresh extraction now produces
   all 16 row keys including `cum_years_schooling`, matching the committed
   values exactly.

7. **Ran the full promotion across all 183 countries** that have
   `PARAM-EDU-LEVEL-CROSSWALK`, then verified with three independent checks:
   `validate_country_layer.py` (`EXIT=0`), `cli.py check` (`ok: true`,
   623 drafts, 0 errors), and a programmatic row-by-row diff between every
   committed file and a freshly re-extracted draft (182/183 countries
   identical; `VNM` differs only because its committed data has 2
   effective-dated periods — a historical system split added by manual
   research — vs. 1 period from a single-snapshot ISCED file, which is
   expected, not a defect).

8. **Cleaned up one-off artifacts**: deleted the standalone sweep's
   per-country YAML drafts (`extraction/20_drafts/runs/country-parameters/education-pathways/*.yaml`,
   206 files — superseded once promoted into `country-parameters/`) and the
   verification-run drafts under
   `extraction/20_drafts/runs/country-parameters/<ISO3>/` (183+ files from the
   `cli.py extract --force` proof run), replacing both with `.gitkeep`.

## How to run this for next time

**A. Regenerate crosswalk drafts from source (ISCED/JMP/GEO workbooks), including years-of-schooling automatically:**
```powershell
python -m extraction_pipeline.country_inputs.cli extract --force
```
`--force` reprocesses every source file regardless of the incremental cache;
omit it for incremental (changed-files-only) runs. Output lands under
`extraction/20_drafts/runs/country-parameters/<ISO3>/PARAM-EDU-LEVEL-CROSSWALK.yaml`
(and the WASH/GEO equivalents), already containing `cum_years_schooling` etc.
for the education parameter.

> Redirect stderr separately or run with `-W ignore` — `openpyxl` emits many
> harmless "unsupported extension" warnings per file, and capturing them via
> PowerShell's `*>` formats each as a pseudo-error record, which is slow
> (added ~10 minutes to a 180-file run that should take under a minute of
> actual compute).

**B. Validate the regenerated drafts against the registry:**
```powershell
python -m extraction_pipeline.country_inputs.cli check
```

**C. Promote (overwrite) committed `country-parameters/countries/<ISO3>/parameters.md`
with the enriched draft rows:**
```powershell
python -m extraction_pipeline.country_inputs.education_pathways --promote
```
This reads from the step-A draft locations (preferred) or, if absent, from a
standalone sweep (`--all`, see below). It only replaces the `value` list of
existing `PARAM-EDU-LEVEL-CROSSWALK` records — it does not add/remove periods
or touch any other parameter in the file. It raises (does not silently guess)
if committed vs. draft period counts/windows disagree for a country.

**D. (Optional) Ad-hoc review of the derivation logic without real source files:**
```powershell
python -m extraction_pipeline.country_inputs.education_pathways --all
```
Sweeps every country's **already-committed** crosswalk rows through
`enrich_rows()` for review (e.g., to see which countries are flagged
`ambiguous`/`review_required` before deciding whether to promote). Writes to
`extraction/20_drafts/runs/country-parameters/education-pathways/<ISO3>.yaml`
and a summary to `extraction/25_agent_review/education-pathways-summary.yaml`.

**E. Final repo-wide validation:**
```powershell
python validation/validate_country_layer.py
pytest tests/ -q
```

## Prevention

- When extending a `row_schema` (or any strict-equality validated structure),
  land the schema change and the full data migration in the same unit of
  work — never let the registry get ahead of the committed data it validates.
- When two pipelines independently produce the "same" artifact shape (here:
  the real `cli.py extract` vs. the standalone `education_pathways --all`
  sweep), make the promotion step read from whichever is authoritative first,
  with an explicit fallback — don't let a one-off tool's output silently
  become the only source of truth.
- Prefer deleting one-off verification artifacts (temp output files, proof-run
  drafts) over leaving them to be mistaken for authoritative data later.
- `temp_repository` in `tests/conftest.py` does a full `shutil.copytree` +
  `git init`/`commit` of `country-parameters/` **per test function** — as
  committed data grows, tests using it get slower; this is fixture overhead,
  not a hang. Budget real wall-clock time for test runs touching this
  fixture.

## Related

- Rule: `knowledge/rules/module/dem/RULE-EDU-003.md` (v0.2)
- Variable: `knowledge/variables/dem/VAR-educy.md`
- Parameter: `knowledge/parameters/PARAM-EDU-LEVEL-CROSSWALK.md` (v0.3)
- Derivation + promotion: `extraction_pipeline/country_inputs/education_pathways.py`
- Extraction pipeline wiring: `extraction_pipeline/country_inputs/cli.py` (`run_extract`)
- Schema: `schema/parameter.py`, `schema/country_parameters.py`
- Tests: `tests/extraction/test_education_pathways.py`, `tests/extraction/test_drafts.py`,
  `tests/test_effective_dating.py`, `tests/test_overlap_detection.py`,
  `tests/test_table_parameter_values.py`, `tests/test_bundle_integrity.py`
- Hand-drafting CVS variable specs at scale (same corpus-gate pattern):
  `.cg-docs/solutions/data-quality/2026-08-14-hand-draft-cvs-variable-specs.md`
