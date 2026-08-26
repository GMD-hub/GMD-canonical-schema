# Verification Review: Lock Extraction Source Resolution

## Scope

Uncommitted implementation for
`.cg-docs/plans/2026-08-25-lock-extraction-source-resolution.md`.

## Verification

- Focused extraction review suite: 89 passed.
- Full repository suite before review: 315 passed, 1 skipped.
- `git diff --check`: passed.

## Findings

### P1: Orchestrator bypasses the mandatory gate contract

`extraction_pipeline/orchestrator.py:67-97` reconstructs a partial manifest from
caller-supplied data and invokes source resolution without proving governance or
parser preflight. The CLI gate also discards its resolved result, leaving no
supported contract between gate output and orchestration input.

### P1: Committed-manifest test is tied to temporary protected state

`tests/extraction/test_preflight.py:61-63` requires the committed protected
manifest to remain invalid, which would fail after approved Phase 2 activation.
Use a synthetic pre-approval manifest fixture instead.

### P1: Parser contract test combines independent invalid mutations

`tests/extraction/test_manifest_models.py:79-84` changes the parser tool and
removes the installation method in one assertion. Test each field independently
with field-specific error locations.

### P2: Preflight does not run before the injected clock

`extraction_pipeline/source_gate.py:29-32` invokes the clock before preflight,
contrary to the required gate sequence.

### P2: Initial filesystem inspection can escape domain errors

`extraction_pipeline/preflight.py:38-41` and
`extraction_pipeline/source.py:23-26` perform stat operations outside the error
translation boundary.

### P2: Required deterministic coverage is incomplete

Governance read/decode failures and checkout revision timeout behavior lack
focused tests with stable messages and chained causes.

### P2: Orchestrator repeats full source verification per item

`extraction_pipeline/orchestrator.py:75-94` repeats Git and hash work for each
item and exceeds the plan's documentation-only boundary.

### P3: Active-state verification counts are stale

`.cg-docs/active-state/current.json` records older focused test counts than the
execution report.

## Adversarial Risk

The standalone gate verifies a mutable checkout, so bytes can change between a
successful gate and later extraction. This is best addressed by an in-process
verified-source contract or immutable snapshot. Triage must align any fix with
the plan's explicit gate and orchestration boundaries rather than adding an
unplanned persistence format.

## Result

Verification review findings were triaged and resolved. The orchestrator was
returned to the plan's documentation-only precondition; gate ordering and
stable filesystem error translation were corrected; state-dependent and
combined tests were replaced; and governance I/O plus Git timeout coverage was
added. The mutable-checkout TOCTOU scenario remains a documented design risk
requiring a future immutable-snapshot contract. No protected configuration,
governance decision, or workflow changes were observed.
