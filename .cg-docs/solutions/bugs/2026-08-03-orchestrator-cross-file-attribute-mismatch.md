---
date: 2026-08-03
title: "Orchestrator cross-file attribute mismatch — untested code passes review"
category: "bugs"
language: "Python"
tags: [orchestrator, cross-file-breakage, untested-code, attribute-mismatch, verify-pass, extraction-pipeline]
root-cause: "New module referenced an attribute name from a different model; no test exercised the path"
severity: "P0"
---

# Orchestrator Cross-File Attribute Mismatch

## Problem

The extraction orchestrator (`extraction_pipeline/orchestrator.py`) was added as
a fix for P2.23 ("Missing orchestrator module"). It was the declared "single
entry point that ties the 6 phases together." However, it was never exercised by
any test. The orchestrator read `item.blocking_issue_ids` to decide canonical vs.
blocked state, but `ItemState` in `extraction_pipeline/state.py` defines the
field as `issue_ids` — not `blocking_issue_ids`. The name `blocking_issue_ids`
exists only on `ExtractionCandidate` (`schema/extraction/candidate.py`), a
different model.

At runtime, any real extraction run would crash with:
```
AttributeError: 'ItemState' object has no attribute 'blocking_issue_ids'
```

The 214 passing tests gave false confidence because none of them called
`run_item_pipeline`. The bug was only caught during a `/cg-review mode:verify`
pass, not during the original standard review or the fix-triage sessions that
created the orchestrator.

## Root Cause

Three factors combined:

1. **Field name drift across models**: `ExtractionCandidate.blocking_issue_ids`
   and `ItemState.issue_ids` serve related purposes but use different names. The
   orchestrator author (an AI agent) naturally used the more descriptive
   `blocking_issue_ids` without checking `ItemState`'s actual field name.

2. **No test for the new module**: The orchestrator was added as a thin sequencer
   with the expectation that its individual phase modules were already tested.
   But the wiring between modules — the attribute access, the gate calls, the
   state transitions — was itself untested.

3. **Green CI masks untested paths**: 214 tests passed, but the orchestrator's
   code path had zero coverage. The test suite tested each phase module in
   isolation but never drove an item through the full pipeline.

## Solution

1. **Fixed the attribute name**: Changed `item.blocking_issue_ids` → `item.issue_ids`
   (2 occurrences in `orchestrator.py`).

2. **Added orchestrator tests**: Created `tests/extraction/test_orchestrator.py`
   with 7 tests covering:
   - Canonical path (all gates pass, no blocking issues)
   - Blocked path: critic rejection
   - Blocked path: blocking issues present
   - Blocked path: gate failure
   - Blocked path: welfare leakage (G9 fail)
   - Initialization (all items queued)
   - Empty inventory

3. **Wired all 7 per-item gates**: The verify pass also found that the orchestrator
   only checked G3, G5, G7 — silently dropping G4 (citation), G6 (sections),
   G8 (graph), and G9 (welfare leakage). Fixed by wiring all gates into the
   `all_gates_passed` check.

## Prevention

### Anti-pattern: "Thin sequencer" without integration tests

When adding a new module that wires together existing tested modules, always
write at least one integration test that drives a full path through the new
module. "Each piece is tested" does not mean "the wiring is correct."

### Pattern: Verify attribute names across model boundaries

When code in module A accesses attributes on a model defined in module B, the
attribute name must be verified against the model definition — not inferred from
a related model with a similar field. AI agents are especially prone to this
because they carry field names across model boundaries from context.

### Pattern: Verify pass catches what standard review misses

The original standard review (8 agents, 50 findings) did not catch this bug
because the orchestrator was added during fix-triage, not during the original
implementation. The verify pass (2 agents, light depth) caught it because it
specifically checked whether fixes introduced cross-file breakage. Always run
`/cg-review mode:verify` after fix-triage, especially when new modules are added.

### Rule: Every new public function needs at least one test

If a function is the declared "single entry point" for a package, it must have
at least one test that exercises it end-to-end. Zero-tested public functions are
a P0 testing gap, regardless of how thin the function is.

## Related

- Review report: `.cg-docs/reviews/2026-08-03-extract-universal-non-welfare-schema-review.md` (P2.23 — missing orchestrator)
- `extraction_pipeline/orchestrator.py` — the fixed orchestrator
- `extraction_pipeline/state.py` — `ItemState.issue_ids` field definition
- `schema/extraction/candidate.py` — `ExtractionCandidate.blocking_issue_ids` field definition
