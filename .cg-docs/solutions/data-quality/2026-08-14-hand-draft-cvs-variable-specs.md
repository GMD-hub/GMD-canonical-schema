---
date: 2026-08-14
title: "Hand-drafting GMD CVS variable specs at scale and validating them"
category: "data-quality"
language: "Python"
tags: [gmd, cvs, extraction, variable-drafts, pydantic, validation, pydantic-v2, corpus-gate, naming-normalization, module-inventory]
root-cause: "Bulk hand-drafting of 267 non-welfare CVS variable specs from GMD-guidelines chapters 2-7 required a deterministic naming convention, authoritative per-chapter inventories, and committed, repeatable validation gates."
severity: "P2"
---

# Hand-drafting GMD CVS variable specs at scale and validating them

## Problem

The GMD Canonical Variable Schema (CVS) needed `VariableDefinition`-valid draft
specs for every non-welfare variable across six modules (IDN, GEO, DEM, LBR,
UTL, DWL) grounded in `GMD-guidelines` (commit `d46dc03`). Naive drafting
produced schema failures, duplicate IDs, and unverifiable claims. The pipeline
orchestrator is a thin sequencer that does not draft, and preflight is blocked
by the supervised source-manifest lock.

## Root Cause

- The Pydantic schema is strict (`extra="forbid"`) and rejects unknown
  RULE-/PARAM- IDs with no draft exemption for rules (only variable refs honor
  `allow_unresolved_draft`).
- The `variable_id` pattern `^VAR-[a-z][a-z0-9]*$` rejects underscores, yet GMD
  uses snake_case names (e.g. `relationship_to_head`).
- The chapter summary tables list far more variables than the module skills
  suggest (GEO: 14 vars vs skill's 2).
- Validation context in pydantic v2 must use `Model.model_validate(data,
  context={...})`, not the constructor.

## Solution

1. **Deterministic naming rule**: map every GMD snake_case name to
   `VAR-<underscore-drop>` (e.g. `relationship_to_head`→`VAR-relationshiptohead`),
   with one grandfathered exception (`VAR-marital`, not `VAR-maritalstatus`).
   Keep the original snake_case as `variable_name`.
2. **Authoritative inventory**: build the per-module inventory from the chapter
   summary tables (the skill is only a hint). Record each name→id mapping before
   drafting.
3. **Decide ownership**: DEM owns core person demographics; IDN owns household
   identifiers and weights. This prevents duplicate `variable_id` across
   modules.
4. **Registered-reference discipline**: reference only registered RULE/PARAM
   ids (RULE-EDU-001/002/003, RULE-SEX-001; PARAM-DEM-MIN-MARRIAGE-AGE,
   PARAM-EDU-YEARS-BY-LEVEL) or leave `rules: []`; document governance concepts
   (e.g. Non-Null Weight Invariant) in `provenance.notes`, never in `rules:`.
5. **Pydantic v2 context validation** (the key gotcha):
   ```python
   VariableDefinition.model_validate(data, context={
       "allow_unresolved_draft": True,
       "variable_ids": all_ids, "parameter_ids": param_ids, "rule_ids": rule_ids,
   })
   ```
   NOT `VariableDefinition(**data, context=...)` — under `extra="forbid"` the
   constructor rejects `context` as an extra kwarg.
6. **Committed corpus gate**: add a test that globs `extraction/20_drafts/**/*.md`,
   validates frontmatter, asserts the 7 required `## ` body sections, asserts no
   duplicate `variable_id`, checks derivation-graph acyclicity, and runs the
   grep-based welfare-leakage scan. This makes the V5/V5b/C4/V6 gates repeatable
   under `pytest`, not a one-shot harness.

## Prevention

- Always use `model_validate(data, context=...)` (pydantic v2) when validating
  with cross-referencing context; never pass `context` to the constructor.
- Re-run the corpus gate after any draft edit or new draft to catch drift.
- Normalize names once in the inventory and keep the mapping table.
- Cite chapter subsections in `provenance.source_section`; record the source
  commit and per-chapter sha256 in a supervised source-lock report rather than
  editing `extraction/config/`.

## Related

- Source: `GMD-hub/GMD-guidelines` commit `d46dc03`.
- Schema: `schema/variable.py`, `schema/frontmatter.py`.
- Gate tests: `tests/extraction/test_drafts.py`.
- Welfare boundary detection:
  `.cg-docs/solutions/testing-patterns/2026-08-03-welfare-boundary-content-based-detection.md`.
- Orchestrator cross-file attribute mismatch:
  `.cg-docs/solutions/bugs/2026-08-03-orchestrator-cross-file-attribute-mismatch.md`.
- Fail-closed promotion from immutable evidence:
  `.cg-docs/solutions/data-quality/2026-08-26-fail-closed-deterministic-promotion.md`.
