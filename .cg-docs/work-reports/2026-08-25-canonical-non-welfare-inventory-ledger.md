# Work Report: Canonical Non-Welfare Inventory Ledger

- **Plan**: `.cg-docs/plans/2026-08-25-canonical-non-welfare-inventory-ledger.md`
- **PR**: `https://github.com/GMD-hub/GMD-canonical-schema/pull/18`
- **Repair date**: 2026-08-30
- **Status**: completed; human inventory review pending

## Synchronization

- Verified a clean existing PR #18 worktree and branch.
- PR head before synchronization:
  `4af0345a1e1eacd81bdcac409a77ff2dfd14bec4`.
- Fetched and pinned `origin/main`:
  `90eddb33425a051a287fdd48ba391f3aef69a057`.
- Merged normally without rebase, reset, force-push, or commit rewriting.
- Merge commit: `a140cd011f0fbdafc648938a0c6e4438d5137e0b`.
- Retained current main's active-state and generated Brain files during conflict
  resolution.
- Reconciled `roadmap.json` by preserving current main and adding only the Task
  C feature.

## Corrections

- Removed Task B workflow status from the Task C schema, compiler, generated
  evidence, tests, and plan.
- Derived and validated source-row, non-counting, denominator, module, and
  discrepancy cardinalities from row-level records.
- Required unique discrepancy IDs and the exact v1 discrepancy identity.
- Resolved output paths from the canonical repository root.
- Rejected external, symlinked, and governed-input overwrite targets.
- Added real temporary-Git end-to-end compile, validate, double-serialize, and
  promote coverage without mocking compiler trust boundaries.
- Added independent source-byte drift, hash mismatch, missing-row, ownership,
  ordering, candidate-tamper, aggregate-tamper, discrepancy, and path failures.
- Corrected the documented `promote` command to include all immutable compile
  inputs.
- Regenerated the source map and ledger deterministically.

## Correct Promotion Command

```bash
.venv/bin/python -m extraction_pipeline.inventory promote \
  --source-repo "$GMD_GUIDELINES_REPO" \
  --source-commit "$SOURCE_SHA" \
  --source-map "$SOURCE_MAP" \
  --draft-root extraction/20_drafts \
  --candidate "$CANDIDATE_A" \
  --output "$LEDGER"
```

Promotion recompiles from immutable evidence and requires byte equality. It
does not trust candidate structure or totals alone.

## Generated Evidence

| Artifact | SHA-256 |
|---|---|
| `extraction/20_drafts/runs/non-welfare-inventory-source-map.v1.yaml` | `99c0ace8851f8916ab38d24e0273532cb48b4031d9fc887ca93485e7c912533b` |
| `extraction/20_drafts/runs/non-welfare-inventory.v1.yaml` | `a3da56f7c298233fea516b20b8418d5eb9cd45b6a5ec87870ee76d08bee1a35c` |

The ledger contains exactly:

- 318 source occurrences;
- 267 canonical IDs;
- 51 non-counting occurrences;
- one non-source retired UTL discrepancy;
- module totals `MOD-IDN 9`, `MOD-GEO 14`, `MOD-DEM 24`, `MOD-LBR 90`,
  `MOD-UTL 61`, and `MOD-DWL 69`.

Two independent candidate compilations were byte-identical. The corrected
validation and promotion sequence reproduced the committed ledger bytes.

## Verification Evidence

| Check | Result |
|---|---|
| `git diff --check` | passed |
| Focused inventory tests | `52 passed, 1 skipped` |
| Candidate-directed inventory tests | `53 passed` |
| Candidate-directed completeness tests | `19 passed` |
| Full Python test suite | `337 passed, 4 skipped` |
| Country-layer validation | passed; existing unresolved-governance reports emitted |
| PER 2019 and PER 1995 bundle smoke tests | passed |
| Review-app focused tests | passed |
| Review-app full tests | passed |
| `R CMD check --no-manual` | completed; 0 errors, 1 existing documentation warning, 2 existing notes |
| Deterministic candidate comparison | byte-identical |
| Final immutable validation and promotion | passed |
| Final adversarial containment review | no P0/P1 findings |

The first local focused R attempt could not start the shinytest2 child process
because `reviewapp` was not installed in the new local renv library. Installing
the unchanged package with `R CMD INSTALL .` resolved the environment setup;
the rerun and all later R checks passed. No review-app source or runtime behavior
was changed.

## Scope And Remaining Gate

The ledger is offline corpus authority for the Task C non-welfare denominator.
It is not runtime review-app queue state, a queue initializer, an enrollment
contract, or a production deployment artifact.

There is no effective PR diff for `.cg-docs/active-state/current.json`,
`review-app/**`, or `.github/workflows/validate.yml`. The production `review`
and `review-production` branches, Posit Connect, and deployed behavior were not
modified.

Human inventory review remains unresolved. The ledger remains
`draft_pending_human_inventory_review`; this work does not fabricate approval,
approve a Task B source lock, or clear any global blocker.
