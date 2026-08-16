---
date: 2026-08-14
depth: data-risk
type: standard
plan: .cg-docs/plans/2026-08-13-complete-non-welfare-extraction.md
findings:
  P1.1: fixed
  P1.2: fixed
  P1.3: skipped
  P2.1: fixed
  P2.2: fixed
  P2.3: skipped
  P2.4: fixed
  P2.5: fixed
  P2.6: fixed
  P2.7: fixed
  P3.1: fixed
  P3.2: fixed
  P3.3: skipped
  P3.4: skipped
  P3.5: skipped
  P3.6: fixed
  P3.7: skipped
  P3.8: skipped
---

## Review Report

**Review mode**: data-risk (auto-routed from /cg-work review:auto)
**Files reviewed**: 267 variable drafts + 3 run reports + plan/active-state
**Findings**: 18 (P0: 0, P1: 3, P2: 7, P3: 8)

### P1 — CRITICAL (fix before merge)
- **[P1.1]** [cg-data-quality] `extraction/20_drafts/dwl/VAR-*.md` (25 files) — Consistency checks boilerplate says "Values must be 0 or 1" on non-binary variables (categorical 1-6, numeric, string). Wrong validation guidance that can silently corrupt non-binary values. **Fix**: Replace boilerplate with actual domain (e.g. integer in [1,4]; area non-negative hectares); only true binary vars retain 0/1 check.
- **[P1.2]** [cg-data-quality] `extraction/20_drafts/lbr/VAR-wagenc.md` — three-way contradiction on non-paid employee wage_nc: Construction says EMPSTAT=2 -> wage_nc=0; Consistency says non-missing only where empstat==1; prerequisite requires empstat==1. **Fix**: decide one rule (define wage_nc for EMPSTAT 1&2 with prerequisite empstat<=2, or 0-only for empstat==1); align all three sections.
- **[P1.3]** [cg-code-quality / cg-testing] `schema/variable.py:95` + plan — `data_type` is unconstrained `str` with 7 inconsistent labels across corpus (numeric vs numeric_continuous vs integer; categorical vs categorical_ordered), invisible to schema/tests. Also the plan's V5 snippet (`VariableDefinition(**data, context=...)`) is non-executable under extra="forbid" — correct API is `model_validate(d, context=...)`. **Fix**: constrain data_type to a `Literal` set, reconcile corpus; correct the plan snippet.

### P2 — IMPORTANT (should fix)
- **[P2.1]** [cg-testing] No committed/repeatable test exercises the 267 drafts (V5/V5b/C4/acyclicity only one-off harness). **Fix**: add `tests/extraction/test_drafts.py` globbing drafts, validating with `model_validate(..., context=...)`, asserting 7 headers, no dup ids, acyclic graph.
- **[P2.2]** [cg-reproducibility] `extraction/20_drafts/runs/source-acquisition-2026-08-13.md` evidence artifact doesn't exist but `current.json` V0 claims it passed. **Fix**: create it or relabel V0 to point to source-lock report.
- **[P2.3]** [cg-code-quality] Missing-code sets inconsistent across modules (LBR no `.o`, UTL all `.o`; DEM order differs) with no documented rationale. **Fix**: standardize per data_type/category, document rule, enforce with test.
- **[P2.4]** [cg-reproducibility] Absolute machine-specific source path embedded in source-lock report; source not vendored. **Fix**: record portable clone command + note sha256-integrity reliance.
- **[P2.5]** [cg-data-quality] `extraction/20_drafts/lbr/*.md` (46 files) — Definition says "is a categorical variable" but data_type numeric_continuous. **Fix**: rewrite Definition openings to "continuous/numeric" for numeric_continuous LBR drafts.
- **[P2.6]** [cg-data-quality] `extraction/20_drafts/dwl/*.md` (69 files) — verbatim appliance-specific boilerplate (Common-mistakes/Escalation) irrelevant to land/area/material vars. **Fix**: remove appliance boilerplate from non-asset vars; add area/material-specific mistakes.
- **[P2.7]** [cg-testing] V6 welfare-leakage grep is not a committed test and misses prose references. **Fix**: record limitation, add content scan test; keep human sign-off gate.

### P3 — MINOR (nice to have)
- **[P3.1]** [cg-data-quality] DEM 6 disability domains typed `categorical` instead of `categorical_ordered`. **Fix**: reclassify for consistency with education family.
- **[P3.2]** [cg-data-quality] `extraction/20_drafts/lbr/VAR-minlaborage.md` allowed_range 0-120 conflicts with "should not be higher than 20". **Fix**: narrow range or convert to PARAM declaration.
- **[P3.3]** [cg-reproducibility] Per-draft provenance doesn't record source commit. **Fix**: add source_commit or notes pointer to source-lock.
- **[P3.4]** [cg-reproducibility] source_document serialization inconsistent (LBR unquoted, others quoted). **Fix**: standardize (always quoted).
- **[P3.5]** [cg-reproducibility] source_section citation format non-uniform (file vs human-readable title). **Fix**: adopt uniform scheme referencing locked source file.
- **[P3.6]** [cg-version-control] work-report frontmatter status `active` vs current.json `complete`; and current.json updatedAt precedes completeness report. **Fix**: align status and refresh updatedAt.
- **[P3.7]** [cg-version-control] run-report filenames use plan date (2026-08-13) but frontmatter date 2026-08-14. **Fix**: document or standardize convention.
- **[P3.8]** [cg-code-quality] Drafter style divergence (LBR single-quoted/no banners; UTL nested null) cosmetic only. **Fix**: standardize formatting or codify LBR as valid variant.

### ✅ Passed
- cg-data-quality: value-code completeness/overlaps, missing-code discipline, missing-evidence handling — no issues
- cg-reproducibility: no randomness/seeds, commit hygiene, gitignore — no issues
- cg-testing: corpus structurally sound, 212 tests pass, V5b 7-section order, no dup ids, acyclic graph — no issues in clean categories
