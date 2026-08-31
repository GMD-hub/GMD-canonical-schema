---
date: 2026-08-30
depth: full
type: verification
findings:
  P0.1: fixed
  P0.2: fixed
  P1.1: fixed
  P1.2: fixed
  P1.3: fixed
  P1.4: fixed
  P1.5: fixed
  P2.1: fixed
  P2.2: fixed
---

# Review Report: Canonical Non-Welfare Inventory Ledger

## Scope

This report verifies the repaired Task C implementation on PR #18 after merging
`origin/main` commit `90eddb33425a051a287fdd48ba391f3aef69a057` into the PR branch.
The review covered the schema, compiler, generated source map and ledger, tests,
plan commands, work report, and effective PR diff.

The ledger is offline corpus evidence. It is not a review-app runtime queue,
queue initializer, enrollment contract, or production deployment input.

## Resolved Findings

- **P0.1 - Promotion trust boundary**: fixed. `promote` recompiles from the
  immutable guideline Git objects, closed source map, governed draft corpus,
  and approval evidence. Candidate bytes must equal deterministic compilation
  before atomic replacement.
- **P0.2 - Aggregate ownership**: fixed. Module totals are derived from and
  validated against canonical occurrence ownership.
- **P1.1 - Mutable claim provenance**: fixed. The obsolete UTL claim is pinned
  to canonical-schema commit `de5d6dbcc918261036073c83b46bacdba53da6e0`
  and a verified blob SHA-256.
- **P1.2 - Parser fail-closed behavior**: fixed. Unsupported constructs and
  source-row deltas stop compilation.
- **P1.3 - Source identity format**: fixed. The ledger requires a lowercase
  40-character guideline commit and seven governed lowercase SHA-256 hashes.
- **P1.4 - Closed source map**: fixed. The compiler regenerates and compares
  the complete source map. Task B workflow state is not embedded in Task C
  evidence.
- **P1.5 - Path containment**: fixed. CLI paths resolve from the canonical
  repository root. External and symlinked output paths are rejected, and
  outputs cannot overwrite the source map or obsolete-claim evidence.
- **P2.1 - Candidate test reporting**: fixed. Candidate-only tests explicitly
  skip when no candidate is configured.
- **P2.2 - Shared active-state diff**: fixed by synchronization. Main's
  `.cg-docs/active-state/current.json` was retained during the merge and has no
  effective PR #18 diff.

## Verification

- `git diff --check`: passed.
- Focused inventory tests: `52 passed, 1 skipped` without a candidate.
- Candidate-directed inventory tests: `53 passed`.
- Candidate-directed completeness tests: `19 passed`.
- Full Python tests: `337 passed, 4 skipped`.
- Final adversarial containment and evidence-integrity review: no P0/P1
  findings.
- Country-layer validation: passed with existing governance warnings recorded.
- PER bundle smoke tests for 2019 and 1995: passed.
- Review-app focused tests: passed after installing the unchanged package into
  the local renv library.
- Review-app full test suite: passed.
- `R CMD check --no-manual`: completed with the existing one documentation
  warning and two package notes; no errors.
- Two independent inventory compilations were byte-identical.
- Validation and corrected full-argument promotion passed.
- Source map SHA-256:
  `99c0ace8851f8916ab38d24e0273532cb48b4031d9fc887ca93485e7c912533b`.
- Ledger SHA-256:
  `a3da56f7c298233fea516b20b8418d5eb9cd45b6a5ec87870ee76d08bee1a35c`.
- Ledger invariants: 318 source occurrences, 267 canonical IDs, 51
  non-counting occurrences, one discrepancy, and module totals
  `9/14/24/90/61/69`.

## Remaining Gate

The generated artifacts retain `status: draft_pending_human_inventory_review`.
Human inventory review is unresolved. Task C does not approve a Task B source
lock, clear a global freeze, or alter review-app runtime behavior.
