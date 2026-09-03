---
date: 2026-09-03
plan: ".cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md"
plan-title: "Enable and Complete Release A Production Queue Cutover"
status: complete
run: 1
---

# Release A Production Queue Cutover Execution Report

## Preserved Execution History

### Run 1 - 2026-08-26

The stored deviation policy was `ask`, with no runtime override. The user
explicitly authorized the plan. Initial local implementation checks passed, but
no plan phase was marked complete because GitHub CI evidence could not exist
before the ordered commit, push, and PR operation.

Initial evidence state:

| ID | Status |
|---|---|
| V1-V11 | pending |

Constraints at that point: no remote review ref or Connect item changed; full R
tests passed from an external temporary library; Python passed 285 tests with 2
skipped; source package build succeeded; `R CMD check` tests passed with
pre-existing package-structure warnings; and `git diff --check` passed.

### Resume Attempt - 2026-08-26 07:45 EDT

The Phase 1 evidence preflight was repeated. The branch was uncommitted and had
no PR, so the required GitHub implementation-run evidence remained unavailable.
No later operation started.

### User-Directed Sequence Resolution - 2026-08-26 10:51 EDT

The user directed the supplied sequence to continue without a separate CI task.
Phase 1 was accepted on local evidence, with remote CI deferred to the ordered
PR verification. Full review found 12 issues, which were addressed through the
later release-enabling implementation and verification PRs.

## Result

The Release A review application is active on the complete non-welfare queue.
Connect reads `review-production`, displays 267 rows, and keeps approval
disabled. The six-record `review` branch remains unchanged for rollback.

## Final Identities

| Item | Final value |
|---|---|
| Application source | `GMD-hub/GMD-canonical-schema`, `main`, `review-app` |
| Deployed application commit | `f064987357fec71c67df909380ad039450f42eb4` |
| `main` at cutover evidence capture | `837ead94fc2c7eb03b9bd13762849d1889c46331` |
| Queue source snapshot | `6d6c10ee96cf3500b802b3e4aae05c70eb24ea9f` |
| Legacy rollback branch | `review@983d7d9503fbf5c2c911ac9d85a37b88accfe4ac` |
| Production queue | `review-production@1399f12fe04c33370f77fee13eff69768c90a769` |
| Queue count | 267 |
| Path digest | `8fbe8f677f7431be19d34762ee665f33169f07610e5d3abe1b8b7fbbe9da2b1c` |
| Record-set digest | `bcd1c27bed9b72fbbe99a7f722f8a524e4ce1ebdc5736a17b4fbe559a74fb718` |
| Preserved-record-blob digest | `ae2fbfdb7e3902df8a8fc377b0ee1d9d6cda9057adce360ee51567d2577771c4` |
| Descriptor | Schema 1.1; `approvals_enabled: false` |
| Production ruleset | `protect-review-production`, ID `21653500`, active |

At cutover, the later `main` commits contained only the temporary cutover
workflow and its secret-name correction. They did not change the deployed
`review-app/` source, so Connect correctly remained at the reviewed application
commit above. The closeout removes that obsolete workflow and adds only project
documentation.

## Source Delivery

The release-enabling implementation was delivered through PRs #18, #21-#27:
production branch and source pinning, simplified queue runtime, source revision
and safe reopen, browser draft recovery, minimal server-side approval,
bootstrap-state validation, and the authenticated migration CLI. PRs #28 and
#29 added the temporary one-use Actions workflow and corrected its reserved
secret names. All Python and review-app R checks passed on the merged changes;
the final `main@837ead94...` validation run also passed.

## Production Migration

Two GitHub Actions attempts, runs `33565925895` and `33620092002`, stopped in
the migration step with the CLI's generic failure message. Both attempts left
all review refs unchanged. No credential value was printed or recorded.

The temporary private key was then validated locally, and a read-only GitHub
App token exchange succeeded. A complete read-only migration preflight verified
the expected branch head, administrator role, production-v2 controls, legacy
index, immutable source snapshots, and all 267 records.

The reviewed CLI created exactly one non-force commit:

```text
1399f12fe04c33370f77fee13eff69768c90a769
```

Its only parent is
`8b5de18ae78f1dd5bb09511fd076c57e670f1db9`. GitHub records
`gmd-review-app[bot]` as author. The tree diff is exactly:

```text
A  extraction/30_review/queue-descriptor.yml
D  extraction/30_review/queue-index.yml
D  extraction/30_review/queue-manifest.yml
```

An independent tree comparison proved all 267 review-record path/blob pairs
unchanged. No body, event-history, blocker, assignment, reviewed-output, or
approved-output path changed.

## Validation And Deployment

A fresh detached checkout of the exact migration commit passed
`validate-production-queue.R` with the fixed source SHA, expected count 267,
fixed path digest, and bootstrap-state checks. The checkout remained clean and
was removed. Descriptor schema 1.1 and disabled approval were checked
independently.

Connect retained repository `GMD-hub/GMD-canonical-schema`, application branch
`main`, directory `review-app`, and application commit `f064987...`. Only
`REVIEW_APP_GH_REVIEW_BRANCH` changed from `review` to `review-production`.
Connect accepted the environment update, redeployed the active bundle, passed
attestation, and displayed 267 rows.

## Accepted Simplifications

- No staging data branch, staging repository, or staging Connect item was
  created.
- Destructive ruleset probes and duplicate canaries were omitted.
- The direct migration replaced staging migration plus promotion.
- Existing automated lifecycle coverage and the completed human-review
  calibration were accepted instead of repeating the full live staging matrix.
- No synthetic production record was changed. The first genuine review will
  serve as the production role smoke.
- Approval enablement moves to the start of real content review and requires one
  governed descriptor-only commit before the first approval.

These simplifications preserve exact source identity, the proven 267-record
denominator, immutable queue records, fail-closed drift, server-side approval
gates, safe reopen/re-enrollment, and real distinct-role review.

## Completion Verification

| ID | Final status | Evidence or approved disposition |
|---|---|---|
| V1 | passed | Release fixes and tests merged; final Python and R CI passed |
| V2 | replaced | Reviewed application commit qualified without the original hold-branch sequence |
| V3 | skipped | Human-approved removal of separate staging repository and Connect item |
| V4 | skipped | Human-approved removal of duplicate staging telemetry run |
| V5 | replaced | Active exact production ruleset and App-authored non-force migration |
| V6 | replaced | Direct application attestation replaced hold-branch restoration evidence |
| V7 | passed | Legacy `review` rollback was proven before direct cutover and remains intact |
| V8 | replaced and passed | Atomic format migration plus detached 267-record validation |
| V9 | deferred | First genuine reviewer save/submit is tracked as content-review launch work |
| V10 | deferred | Distinct approver inspection and disabled-approval confirmation move with V9 |
| V11 | passed | Final refs, tree identities, ruleset, Connect state, and report reconciled |

| Constraint | Final status | Check |
|---|---|---|
| C1 | passed | No protected semantic, canonical, country, or draft artifact changed |
| C2 | passed | Legacy `review` stayed at its preserved SHA |
| C3 | skipped | Separate staging was removed by approved simplification |
| C4 | passed | No destructive production rule test or ref operation occurred |
| C5 | passed | No secret entered Git or evidence; temporary copies were removed and revoked |
| C6 | partially passed and replaced | Descriptor and server gate keep approval disabled; the obsolete manifest blocker representation was removed by migration |
| C7 | replaced | App wrote only the migration; future review-state writes remain human actions |
| C8 | passed | Queue state exists only on `review-production`, not `main` |
| C9 | passed | Production history is a non-force single-parent App commit |
| C10 | passed | Every record remains bound to source snapshot `6d6c10ee...` |
| C11 | replaced | Direct cutover was human-approved after immutable candidate qualification |

## Accepted Exceptions

Human operator `acastanedaa` approved direct production cutover on 2026-09-01
and approved using the first genuine distinct-role review instead of synthetic
production smoke on 2026-09-02. The decisions affected V2-V6, V9-V10, C3, C6,
C7, and C11. No exception permits source drift, record mutation, force
operations, approval enablement, or deletion of rollback history.

## Rollback

Set `REVIEW_APP_GH_REVIEW_BRANCH=review`, restart Connect, and confirm the six
legacy records return read-only. Do not delete or rewrite `review-production`.

## Remaining Work

- A mapped reviewer and a distinct mapped approver perform the first genuine
  review interaction; do not create artificial smoke content.
- Enable approval with one governed descriptor-only commit before the first
  approval decision.
- Complete human review of all 267 records.
- Reconcile approved Markdown and YAML, promote governed records, validate final
  counts and provenance, and freeze Version 1.

The temporary Actions environment and its three secrets were deleted on
2026-09-03. The local temporary PEM file was deleted, and the GitHub App owner
revoked the temporary key on the same date.

## Final Status

`complete` with the accepted simplifications above. Content review and Version
1 reconciliation remain separate roadmap work.
