---
date: 2026-08-25
title: "Enable and Complete Release A Production Queue Cutover"
status: completed
completed-date: 2026-09-03
completed-phases: [1, 2, 4, 5, 6]
skipped-phases: [3]
deferred-verifications: [V9, V10]
scope: "Deep"
brainstorm: ".cg-docs/brainstorms/2026-08-04-build-human-review-application.md"
language: "both"
estimated-effort: "large"
deviation-policy: "ask"
artifact-schema-version: 1
phases: 6
execution-report: ".cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md"
tags: [release-a, review-app, production-queue, posit-connect, github, cutover]
---

# Plan: Enable and Complete Release A Production Queue Cutover

## Completion Update

This plan closed on 2026-09-03 with an approved simplification. The separate
staging repository, staging Connect item, destructive ruleset probes, synthetic
production smoke record, and duplicate evidence gates were not created. The
existing automated test coverage and completed human-review calibration were
accepted in place of the original isolated live rehearsal.

Production was migrated directly with the reviewed CLI. The migration used one
non-force GitHub App commit, preserved all 267 record blobs, and replaced only
the three queue-control paths. The migrated queue passed the exact source,
count, path-digest, bootstrap-state, and descriptor checks. Connect was then
switched to `review-production`, restarted, attested, and confirmed to display
267 rows. Approval remains disabled. The first genuine reviewer submission and
distinct approver inspection will serve as the production role smoke when
content review begins.

The durable evidence and accepted deviations are in
`.cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md`.

Human operator `acastanedaa` approved the direct production cutover on
2026-09-01 and approved replacing a synthetic production smoke record with the
first genuine distinct-role review on 2026-09-02. This decision supersedes the
original requirements V2-V4, the staging parts of V5, V6, the synthetic parts
of V9-V10, and the obsolete four-blocker representation in C6.

### Accepted Completion Contract

The accepted outcome is one protected `review-production` queue with descriptor
schema 1.1, the exact 267-record source set, unchanged record blobs, disabled
approval, an attested Connect deployment displaying all records, and unchanged
legacy `review` rollback. The following matrix records the disposition of the
original verification surface:

| IDs | Disposition | Evidence or replacement |
|---|---|---|
| V1 | Passed | Merged release code, full CI, and reviewed migration CLI |
| V2 | Replaced | Fixed application commit qualification without the original hold-branch sequence |
| V3-V4 | Skipped | Approved removal of the separate staging repository, Connect item, and telemetry repetition |
| V5 | Replaced | Active exact production ruleset plus the successful App-authored non-force migration |
| V6 | Replaced | Direct attestation of the unchanged reviewed Connect application without hold-branch restoration |
| V7-V8 | Passed | Prior rollback proof, migration atomicity, and detached queue validation |
| V9-V10 | Deferred | First genuine reviewer and distinct approver interaction; approval remains disabled |
| V11 | Passed | Final refs, queue tree, Connect state, and this execution report |

Accepted constraint deviations:

| IDs | Disposition | Evidence or replacement |
|---|---|---|
| C3 | Skipped | Separate staging was removed by the approved direct-cutover decision |
| C6 | Partially passed and replaced | Approval remains disabled; descriptor schema 1.1 replaced the obsolete four-blocker manifest representation |
| C7 | Replaced | The App performed only the format migration; future review-state writes remain human actions |
| C11 | Replaced | Human-approved direct cutover followed immutable candidate qualification without the original hold sequence |

Deferred V9-V10 work belongs to human content review and is not a Release A
cutover blocker under the approved simplification.

## Objective

Correct the release-blocking branch, source-binding, CI, and verification gaps;
qualify the resulting application in an isolated checkout and live staging;
then cut the production review application over to a protected
`review-production` data branch and bootstrap all 267 non-welfare records while
approval remains disabled. Preserve the six-record `review` calibration branch
and keep production queue state out of `main`.

## Context

The first cutover draft assumed that the existing `review` branch and a new
`review/production` branch could coexist. Git ref storage makes that impossible:
`refs/heads/review` blocks creation of any child ref. The implementation also
hard-codes `review/production`, so the production name must be changed in code,
tests, and operator documentation before cutover. This plan selects the
non-conflicting branch name `review-production`; deleting or renaming the legacy
`review` branch is forbidden.

The prior `origin/main` baseline
`8e16ee967816344e7977a0d6f00455f25cb21b47` is explicitly rejected as a release
candidate. GitHub run `32785455255` passed Python validation but failed
`Review-app R validation` while loading the `gert` binary because
`libgit2.so.1.7` was unavailable. A new candidate must include the CI repair and
all release-enabling changes, merge to `main`, and pass clean qualification.

Repository checks on 2026-08-25 established these preserved baselines:

- `origin/review` is
  `983d7d9503fbf5c2c911ac9d85a37b88accfe4ac` and contains the six calibration
  records.
- No remote `review-production` branch exists.
- `origin/main` contains `.gitkeep` under `extraction/30_review/`; bootstrap
  therefore adds exactly 269 queue paths but does not make the directory contain
  exactly 269 total paths.
- The active Connect content GUID is
  `4471d2cc-5939-4ea4-b526-caf9e88ad30c`; bundle `99172` is only a historical
  pre-cutover baseline.
- The active worktree contains this untracked plan and its roadmap registration,
  so candidate qualification must run in a separate detached worktree.

The current app already provides strict v2 records, source drift detection,
queue manifest/index contracts, server-side action gates, atomic writes, and
administrator-only enrollment. Release completion now also requires:

- one `PRODUCTION_REVIEW_BRANCH` constant set to `review-production`;
- server-side binding to an explicit expected source commit supplied through
  `REVIEW_APP_EXPECTED_SOURCE_COMMIT`;
- a green R CI setup with the required `libgit2` runtime;
- reproducible queue-validation and Connect-attestation commands;
- measurable repository-request telemetry for the index fast path; and
- a live isolated staging rehearsal before production mutation.

The plan implements the Git-backed architecture decided in
`.cg-docs/brainstorms/2026-08-04-build-human-review-application.md` and updates
the production procedure in `review-app/docs/operator-guide.md`. This plan is
self-contained; it does not depend on an absent `.kilo/plans/` seed artifact.

## Plan Review Findings Incorporated

| Finding | Resolution in this plan |
|---------|-------------------------|
| P1.1 | Replace impossible `review/production` with `review-production` in one shared constant, code, tests, config examples, and docs; preserve `review`. |
| P1.2 | Reject `8e16ee...`, repair R CI, merge the enabling changes, and qualify a new `main` SHA before remote cutover. |
| P1.3 | Run Python/R qualification in an isolated detached worktree with explicit environments; set the Python test working directory to that checkout and the R working directory to its `review-app/`. |
| P1.4 | Require `REVIEW_APP_EXPECTED_SOURCE_COMMIT`, display it in the bootstrap modal, and enforce it before and after generation. |
| P1.5 | Use actual check contexts `Python validation` and `Review-app R validation`; test one parameterized ruleset only on a staging probe; apply production creation protection before creating the ref. |
| P1.6 | Provision a separate staging repository and Connect item, seed candidate `main`, legacy `review`, and production review refs, and use separate prepared artifacts for draft-save and in-review revision drift probes. |
| P1.7 | Permit only the expressly listed non-force canary, bootstrap, save, and submit commits on `review-production`; forbid all legacy `review` changes and ref rewrites. |
| P2.1 | Add a human-action matrix and require live identity-to-role checks before remote mutation; automation remains read-only for human-owned review state. |
| P2.2 | Use exact whitelisted Connect content/bundle/job endpoints, distinguish rebuild from restart, and use approved UI/manifest evidence for app subdirectory. |
| P2.3 | Require two ordered smoke commits: save, then submit. |
| P2.4 | Prove server-side approval denial with the documented namespaced Shiny input injection and unchanged branch head. |
| P2.5 | Add an exact read-only production-queue validator with `--expect-bootstrap-state`; treat successful publication as payload-preflight evidence instead of claiming an unavailable byte count. |
| P2.6 | Require exactly four repository reads, zero per-record reads, and dashboard completion within five seconds for five staging refreshes. |
| P2.7 | Rehearse data rollback before bootstrap, then restore and re-attest the production configuration. |
| P3.1 | Remove dependency on the absent Kilo seed plan from this plan and stale operator-guide references; this plan and revised guide are authoritative. |
| P3.2 | Verify 267 record files plus manifest/index added by bootstrap while allowing the inherited unchanged `.gitkeep`. |
| P1.8 | Require explicit supervised-write authorization at `/cg-work` start for exact Phase 1 code/workflow/test/doc paths; otherwise human developers perform edits and automation remains read-only. |
| P1.9 | Put production Git-backed deployment on a human-controlled hold branch before merging Phase 1; restore source branch `main` only after staging passes. |
| P2.8 | Install and verify production ruleset, including a creation rule, before the nonexistent target ref is created through an approved bypass. |
| P2.9 | Locate all force/delete probe operations in the staging repository; production repository receives only ruleset reads and removable canaries. |
| FV-P1.1 | Extend recorded GPID authorization to the exact execution-report and active-state paths required by `/cg-work`. |
| FV-P2.1 | Protect the hold ref before creation and attest Connect repository URL, tracked branch, directory, polling, last-known commit, and remote SHA at every boundary. |
| FV-P2.2 | Whitelist Connect job `tag` and require a newer successful `run_app` job for restart evidence. |
| FV-P2.3 | Keep reviewer/approver detail sessions open before staging source drift, then invoke stale-session actions after the source commit. |
| FV-P2.4 | Capture the specific denial from the action-feedback error panel, not the generic notification. |
| FV-P3.1 | Constrain the queue exclusivity invariant to Release A v2 production state, allowing preserved legacy calibration records on `review`. |
| FG-P2.1 | Deploy staging code from immutable `release-a-staging-code` while source data remains on staging `main`, so drift commits cannot restart stale sessions. |
| FG-P2.2 | Apply the equivalent ruleset to staging `review-production` and require a human-triggered App-authenticated fast-forward save before production. |
| FG-P2.3 | Run the validator script from the detached production checkout with its `review-app/` working directory and qualified renv library. |

## Human Action Matrix

| Action | Required human role | Automation boundary |
|--------|---------------------|---------------------|
| Approve/merge enabling code to `main` | Repository maintainer | Automation may prepare code/tests and report CI; it does not approve its own merge. |
| Authorize Phase 1 supervised edits | GPID Team representative | Must explicitly approve the exact path allowlist below before automation edits; otherwise edits are human-only. |
| Provision staging repository/App access/Connect item | GitHub organization and Connect administrator | Automation may provide exact configuration and read-only validation. |
| Create production ref and ruleset; run canaries | Repository administrator using approved credentials | Automation may issue read-only ref/rules queries; it must not use an agent identity for human-owned review writes. |
| Run ruleset rejection probes | Designated human test identity `<non-bypass-writer>` with repository write permission and no ruleset bypass | Organization administrator provisions/selects the identity and records its login, permission, and absence from every bypass actor before Phase 4. |
| Confirm identity mapping and bootstrap | Connect identity mapped to `administrator` (currently `acastanedaa`) | Automation observes and validates; it does not trigger bootstrap. |
| Save and submit smoke artifact | Available Connect identity mapped to `reviewer` in `roles.yml` | Automation records read-only Git evidence after each human action. |
| Perform approval-denial probe | Available Connect identity mapped to `approver` in `roles.yml` | Human performs the browser injection; automation compares refs and records evidence. |

Before any remote mutation, record the actual selected administrator, reviewer,
and approver and capture authenticated UI evidence that each `session$user`
resolves to the expected repository-managed role. Stop if any required human or
role mapping is unavailable.

## Pre-Execution Authorization Gate

Before `/cg-work` performs any plan-frontmatter, roadmap, report, active-state,
or Phase 1 mutation, it must obtain and record explicit GPID authorization for
supervised agent edits limited to:

- `review-app/R/`
- `review-app/tests/testthat/`
- `review-app/tools/`
- `review-app/README.md`
- `review-app/docs/operator-guide.md`
- `.github/workflows/validate.yml`
- `.cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md`
- `.cg-docs/active-state/current.json`
- `.cg-docs/plans/2026-08-25-complete-release-a-production-queue-cutover.md`
  limited to `/cg-work` lifecycle frontmatter fields
- `roadmap.json` limited to status changes for feature
  `complete-release-a-production-queue-cutover` through `@cg-roadmap`; direct
  edits remain forbidden

The report and active-state entries are limited to the execution evidence and
handoff records required by `/cg-work`. This authorization never covers `knowledge/`,
`country-parameters/`, draft/review/approved content, `AGENTS.md`, or remote
review-state writes. If authorization is denied or unavailable, human developers
must perform the Phase 1 edits and `/cg-work` remains read-only until it can
validate the resulting commit.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Preserve remote `review` at `983d7d9503fbf5c2c911ac9d85a37b88accfe4ac`; never rename, delete, rewrite, merge, or write to it. | AGENTS.md; operator guide section 4; P1.1 |
| R2 | Replace every production-only `review/production` assumption with one shared `PRODUCTION_REVIEW_BRANCH = "review-production"` contract and regression tests. | Git ref constraint; `enrollment.R`; `index.R`; P1.1 |
| R3 | Require and display `REVIEW_APP_EXPECTED_SOURCE_COMMIT`; reject bootstrap unless both pre- and post-generation `main` heads equal it. | `enrollment.R`; `mod_dashboard.R`; P1.4 |
| R4 | Repair R CI by installing the Ubuntu `libgit2` runtime/development package before R tooling installation and require both canonical checks green. | Workflow run 32785455255; `.github/workflows/validate.yml`; P1.2 |
| R5 | Add deterministic read-only commands for queue validation and Connect attestation, plus test/staging request-count instrumentation. | P2.2, P2.5, P2.6 |
| R6 | Before Phase 1 merges, move active Connect Git-backed code deployment to `release-a-production-hold`; then qualify one new `origin/main` SHA in an isolated checkout and keep production on hold until staging passes. | P1.2, P1.3, P1.9 |
| R7 | Provision a separate staging repository `GMD-hub/GMD-canonical-schema-cutover-staging`, immutable code branch `release-a-staging-code`, GitHub App access, and private Connect staging item using source-data branch `main`. | P1.6; FG-P2.1 |
| R8 | In staging, verify bootstrap, identity roles, source-drift denial, approval denial, two-commit review smoke, rollback, and measurable index performance without touching production refs. | P1.6; P2.1-P2.7 |
| R9 | Protect production `review-production` with an active GitHub ruleset that blocks deletion/non-fast-forward updates, requires both checks for human PRs, and grants explicit App/admin-team bypass. | P1.5 |
| R10 | Prove destructive rule behavior only on an equivalent disposable probe ref; use removable, non-destructive canaries on production. | P1.5 |
| R11 | Deploy the qualified candidate to the active Connect item, set the exact source/review/expected-SHA configuration, and capture whitelisted API and subdirectory evidence. | P2.2 |
| R12 | Rehearse data rollback to legacy `review` before bootstrap, verify six read-only records, restore `review-production`, and re-attest pre-bootstrap state. | P2.7 |
| R13 | Have the authenticated human administrator bootstrap exactly 267 unassigned v2 records plus manifest/index in one atomic non-force commit. | Operator guide section 6.3; `enrollment.R`; P2.5/P3.2 |
| R14 | Verify production queue counts/blockers and perform exactly two reviewer commits (save then submit), followed by adversarial server-side approval denial with no commit. | P2.3, P2.4 |
| R15 | Record exact SHAs, CI, staging, ruleset, Connect, rollback, bootstrap, smoke, guardrail, performance, and final invariant evidence in the execution report. | Goal-execution contract; all review findings |

## Implementation Steps

## Phase 1: Release-enabling implementation

### 1. Correct release contracts, CI, and evidence tooling

- **Requirements**: R1, R2, R3, R4, R5
- **Files**: `review-app/R/enrollment.R`, `review-app/R/index.R`,
  `review-app/R/mod_dashboard.R`, `review-app/R/app_server.R`,
  `review-app/R/github_adapter.R`, `review-app/tests/testthat/`,
  `review-app/tools/`, `review-app/README.md`,
  `review-app/docs/operator-guide.md`, `.github/workflows/validate.yml`
- **Details**:
  1. Define one `PRODUCTION_REVIEW_BRANCH <- "review-production"` constant and
     consume it from enrollment and index routing. Replace production-only
     strings in tests/docs/config examples, while retaining exact `review` for
     legacy read-only routing. Add a regression test that proves both refs can
     coexist and rejects `review/production`.
  2. Add required `expected_source_commit` handling. Read
     `REVIEW_APP_EXPECTED_SOURCE_COMMIT` at app startup, validate it as a SHA-1,
     display it in the bootstrap confirmation, pass it into
     `bootstrap_production_queue()`, and reject unless the source head before
     generation and after generation both equal it. Missing/malformed/mismatched
     values fail closed before publication.
  3. In R CI, install `libgit2-dev` before `renv::install(...)` and assert the
     required `libgit2.so.1.7` runtime is discoverable. Retain the current R
     version, renv restore, focused suite, full suite, and `R CMD check` gates.
  4. Add `review-app/tools/validate-production-queue.R`. It accepts a checkout
     path and expected source SHA, loads the candidate package, validates the
     manifest/index/all v2 records, verifies counts/path digest/module totals,
     allows unchanged `.gitkeep`, and exits nonzero on any mismatch. Required
     `--expect-bootstrap-state` mode additionally enforces 267 `draft` records,
     empty assignments and events, no approved output, all four blockers open,
     and `approval_mode: disabled`.
  5. Add `review-app/tools/attest-connect.R`. It queries only
     `/__api__/v1/content/<guid>`, `/bundles`, `/jobs`, and `/repository`, emits
     only whitelisted non-secret fields, and never reads or exports the
     environment endpoint.
  6. Add request-count instrumentation around the injectable repository HTTP
     adapter for tests/staging. A production index refresh must report exactly
     four repository reads (head, recursive tree, manifest blob, index blob) and
     zero per-record content reads without logging tokens or response bodies.
  7. Remove stale operator-guide references to absent `.kilo/plans/` artifacts;
     link this canonical plan and keep the revised guide self-contained.
- **Test Scenarios**: coexistence of `review`/`review-production`; legacy branch
  remains read-only; missing/malformed/mismatched expected SHA; `main` movement
  during generation; R CI dependency present/absent; validator rejects missing,
  duplicate, malformed, wrong-source, or extra queue records; Connect attestor
  redacts secrets; index path performs four reads and no record scan.
- **Tests**: focused `testthat` files for enrollment, index, source binding,
  production queue, bootstrap-state validator mode, tools, and request counts;
  full `devtools::test()`; source
  package build/check; Python suite; GitHub CI on the implementation PR.

#### Implementation checks

```sh
rg -n 'review/production|review-production' review-app .github
Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-enrollment.R")'
Rscript -e 'pkgload::load_all("review-app"); testthat::test_file("review-app/tests/testthat/test-production-queue.R")'
Rscript -e 'pkgload::load_all("review-app"); devtools::test(reporter = "summary")'
python3 -m pytest tests/ -q
```

- **Acceptance criteria**: all new and existing tests pass; no production code
  or current operator instruction expects `review/production`; bootstrap cannot
  publish against any source other than the configured expected SHA; R CI no
  longer fails loading `gert`; validator/attestor/request-counter tests are
  deterministic; no remote review ref or Connect item has been changed.

## Phase 2: Candidate qualification

### 2. Merge and qualify one immutable candidate

- **Requirements**: R1, R4, R6
- **Files**: qualified `origin/main` commit; temporary detached worktree and
  external Python/R environments only
- **Details**: Before the Phase 1 merge, a human repository administrator creates
  an active hold ruleset targeting nonexistent `release-a-production-hold`.
  The ruleset contains `creation`, `deletion`, and `non_fast_forward`, with only
  the approved administrator-team bypass. A repository maintainer creates the
  hold ref at the pre-enabling `origin/main` SHA through that bypass. The Connect
  administrator repoints the active Git-backed content source branch to the hold
  ref. The attestor's `/repository` response must match the production repository,
  branch `release-a-production-hold`, directory `review-app`, enabled polling,
  and last-known hold commit; a remote ref read must equal that commit. Only then may a human merge
  Phase 1 to `main`; production remains on the hold ref. Fetch the new
  `origin/main` and record its candidate SHA. Create a separate detached
  worktree at that SHA; do not test the dirty planning worktree. Create a Python
  3.10+ virtual
  environment outside the checkout and install `requirements.txt`. Run R from
  `review-app/` with `REVIEW_APP_OFFLINE=1`, the checkout's role map,
  `NOT_CRAN=true`, and temporary renv/cache paths. Build/check in a temporary
  output directory. Require a clean candidate worktree before and after tests.
  Confirm both canonical GitHub checks are green for the exact candidate SHA.
  Record and retain the qualified renv library path through Phase 6 so final
  queue validation uses the same candidate-qualified R dependencies.
- **Test Scenarios**: candidate passes locally and remotely; environment setup
  starts empty; build artifacts stay outside checkout; current `main` advances
  after qualification; any check belongs to a different SHA.
- **Tests**: commands below plus GitHub check-run query.

#### Hold and qualification checklist

```sh
git fetch --prune origin
gh api "repos/GMD-hub/GMD-canonical-schema/rulesets/<hold-ruleset-id>"
git push origin <pre-enabling-main-sha>:refs/heads/release-a-production-hold
git ls-remote origin refs/heads/release-a-production-hold
git rev-parse origin/main
git ls-remote origin refs/heads/review refs/heads/review-production
git worktree add --detach <qualification-worktree> <candidate-sha>
python3 -m venv <qualification-venv>
<qualification-venv>/bin/python -m pip install --requirement <qualification-worktree>/requirements.txt
gh api "repos/GMD-hub/GMD-canonical-schema/commits/<candidate-sha>/check-runs"
```

Run the Python suite with the terminal working directory set to
`<qualification-worktree>` so repository-relative fixtures resolve only inside
the candidate checkout:

```sh
<qualification-venv>/bin/python -m pytest tests/ -q
```

Run these with the terminal working directory set to
`<qualification-worktree>/review-app` and temporary `RENV_PATHS_*` values:

```sh
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript -e 'renv::install(c("devtools", "golem", "rprojroot", "shinytest2", "testthat"), prompt = FALSE)'
Rscript -e 'pkgload::load_all("."); devtools::test(reporter = "summary")'
```

Run `R CMD build` and `_R_CHECK_FORCE_SUGGESTS_=false R CMD check --no-manual`
from the temporary output directory against the candidate source. Then require
`git -C <qualification-worktree> status --short` to return no output.
- **Acceptance criteria**: the active hold ruleset predates hold-ref creation and
  blocks non-bypass creation/deletion/non-fast-forward updates; Connect
  `/repository` configuration and remote SHA are attested on the hold branch
  before merge and at the end of Phases 2, 3, and 4; one new candidate SHA has reproducible local results,
  both green GitHub checks, and clean-tree proof; `origin/review` remains at the
  preserved SHA; `review-production` still does not exist. If `main` advances,
  keep the recorded SHA but production bootstrap will fail closed until the
  operator either restores `main` to that SHA or requalifies the new head.

## Phase 3: Isolated live rehearsal

### 3. Provision staging and execute the complete cutover rehearsal

- **Requirements**: R7, R8
- **Files**: external staging repository
  `GMD-hub/GMD-canonical-schema-cutover-staging`; separate private Connect
  staging content item; staging evidence in the execution report
- **Details**: A human organization/Connect administrator provisions the named
  staging repository, grants the GitHub App contents read/write access, pushes
  the qualified candidate to staging `main` and immutable
  `release-a-staging-code`, pushes the preserved production
  repository `origin/review` commit to staging `review` to seed the six-record
  legacy rollback fixture, creates staging `review-production`, and deploys the
  candidate from `review-app/` on watched code branch
  `release-a-staging-code` to a separate private Connect item. Configure
  owner/repo, default source-data branch `main`, review `review-production`, expected source SHA,
  production profile, and the approved role map. Use real mapped
  administrator/reviewer/approver sessions. Record `<non-bypass-writer>` with
  ordinary write permission to both staging and production repositories and
  prove that login is absent from every Integration/Team bypass actor. An
  unauthenticated or read-only identity does not satisfy this gate.
- **Test Scenarios**:
  1. Human administrator bootstraps all 267 staging records.
  2. Reviewer save then submit creates two ordered commits.
  3. Approver namespaced-input probe is denied server-side while approval mode
     is disabled and leaves the ref unchanged.
  4. Prepare two distinct staging artifacts before drift: artifact A remains
     `draft`; artifact B is saved/submitted to `in-review`. Change both source
     paths only after a reviewer session is open on A with an unsaved edit and
     an approver session is open on B with Request Revision available. From
     those stale pre-drift sessions, commit both source changes to staging
     `main`, then invoke reviewer Save on A and approver Request Revision on B.
     Both server actions must fail closed and leave the review ref unchanged
     after each attempt. Connect `/repository` evidence must still show watched
     code branch `release-a-staging-code`, and `/jobs` must show no new
     `run_app` job caused by either staging `main` drift commit.
     Automated integration tests cover save, submit, assignment, revision,
     approval, and reopen denial under drift.
  5. Five consecutive dashboard refreshes each finish within five seconds and
     report exactly four repository reads with no per-record content call.
  6. Point staging to legacy `review` fixture state, verify read-only behavior,
     restore `review-production`, and verify the queue returns intact.
  7. Create `review-production-probe` in the staging repository for the Phase 4
     force/delete ruleset tests; never create that probe in production.
- **Tests**: queue validator against a temporary staging checkout; Connect
  attestor against staging; authenticated UI evidence; before/after ref reads;
  request-count trace; full guardrail integration tests.
- **Acceptance criteria**: all staging scenarios pass with no accepted
  exception; staging and production repository/GUID identities are visibly
  distinct in evidence; production `main`, `review`, and Connect configuration
  remain unchanged. Keep staging available until production completion, then
  archive it according to operator policy.

## Phase 4: Protected production data branch

### 4. Prove and apply production branch governance

- **Requirements**: R1, R9, R10
- **Files**: staging repository ruleset and
  `review-production-probe`; production repository ruleset and
  `review-production`; temporary production `extraction/30_review/.canary`
- **Details**: A human repository administrator records the GitHub App
  integration ID and the approved administrator-team ID. Build one parameterized
  ruleset payload with active enforcement, explicit Integration and Team bypass
  actors, exact ref condition, deletion/non-fast-forward rules, and both required
  status checks. First target the disposable probe ref. Prove force-push and
  deletion are rejected for a non-bypass actor and allowed only for the intended
  bypass used to clean up the disposable probe. The probe and its ruleset exist
  only in `GMD-hub/GMD-canonical-schema-cutover-staging`. Never run destructive
  tests in the production repository. After the probe passes, apply the
  equivalent ruleset to staging `review-production`. A human staging reviewer
  saves one fresh, non-drifted draft through the app; require an
  App-authenticated fast-forward commit and unchanged ruleset JSON. This proves
  the Integration bypass on the actual protected writer path. Then create and verify
  the production-target ruleset while `review-production` does not yet exist.
  Its creation rule allows only the approved bypass actors to create the ref.
  The human administrator then creates `review-production` from the qualified
  candidate through the approved bypass, without force.
  All rejection probes authenticate as the previously recorded
  `<non-bypass-writer>`; stop if its write permission or non-bypass status cannot
  be reverified immediately before the probe.

#### Ruleset payload contract

```json
{
  "name": "protect-review-production",
  "target": "branch",
  "enforcement": "active",
  "bypass_actors": [
    {
      "actor_id": "<github-app-integration-id>",
      "actor_type": "Integration",
      "bypass_mode": "always"
    },
    {
      "actor_id": "<approved-admin-team-id>",
      "actor_type": "Team",
      "bypass_mode": "always"
    }
  ],
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/<target-ref>"],
      "exclude": []
    }
  },
  "rules": [
    {"type": "creation"},
    {"type": "deletion"},
    {"type": "non_fast_forward"},
    {
      "type": "required_status_checks",
      "parameters": {
        "strict_required_status_checks_policy": true,
        "do_not_enforce_on_create": true,
        "required_status_checks": [
          {"context": "Python validation"},
          {"context": "Review-app R validation"}
        ]
      }
    }
  ]
}
```

The human administrator must resolve the two actor IDs through organization
administration and record them in the execution report; they are identifiers,
not secrets. Stop rather than broadening bypass to all writers.
- **Test Scenarios**: staging probe force-push/delete rejection; intended bypass cleanup;
  App-authenticated reviewer save through protected staging `review-production`;
  production creation by non-bypass rejected before the real creation;
  unprivileged production canary rejected or, if it
  unexpectedly succeeds, immediately removed by the administrator and execution
  stops; administrator canary create/remove; no legacy branch change.
- **Tests**: create/update/read/delete ruleset with `gh api`; remote ref reads;
  staging-probe-only destructive commands under the designated test credential;
  production tree and canary reads.

#### Production read-only checks

```sh
gh api "repos/GMD-hub/GMD-canonical-schema/git/ref/heads/review" --jq '.object.sha'
git ls-remote origin refs/heads/review-production
gh api "repos/GMD-hub/GMD-canonical-schema/rulesets/<production-ruleset-id>"
```

#### Human administrator mutation

The approved repository administrator, not automation, creates the protected
ref through the recorded bypass:

```sh
git push origin <candidate-sha>:refs/heads/review-production
```

#### Post-creation read-only checks

```sh
git ls-remote origin refs/heads/review refs/heads/review-production
git ls-tree -r --name-only origin/review-production extraction/30_review
```

- **Acceptance criteria**: staging probe evidence proves destructive controls without
  risking production; a protected staging save proves the configured Integration
  actor can fast-forward through the same rules and leaves rule configuration
  unchanged; production ruleset JSON exactly matches the payload and
  recorded actors and was active before ref creation; a non-bypass creation is
  rejected; administrator canary is created and removed in two non-force
  commits; no canary remains; `review-production` descends from the candidate;
  `review` retains the preserved SHA.

## Phase 5: Connect cutover and rollback rehearsal

### 5. Deploy, attest, rehearse rollback, and restore

- **Requirements**: R1, R11, R12
- **Files**: Posit Connect content configuration for GUID
  `4471d2cc-5939-4ea4-b526-caf9e88ad30c`; no repository secrets or generated
  deployment metadata files
- **Details**: Confirm production Git-backed source still points to
  `release-a-production-hold` and the exact candidate passed staging. A human
  Connect administrator then restores the watched source branch to `main`,
  triggering the first production rebuild of the enabling code. Require a new
  successful bundle because application code changed. Set owner/repo, source branch `main`, review branch `review-production`,
  expected source commit equal to the qualified SHA, and production profile.
  Unset local/offline controls. Use the repository-managed role map unless an
  approved override already exists; record only the override SHA-256.

  Run `review-app/tools/attest-connect.R` against exact read-only endpoints:

  - `GET /__api__/v1/content/<guid>`: whitelist GUID, name, bundle ID,
    `last_deployed_time`, R version, application mode, and status-relevant
    non-secret fields.
  - `GET /__api__/v1/content/<guid>/bundles`: whitelist active bundle ID,
    creation time, R version, active flag, and metadata keys `source`,
    `source_branch`, `source_commit`, `source_repo`.
  - `GET /__api__/v1/content/<guid>/jobs`: whitelist job ID, bundle ID,
    `tag`, start/end times, status, exit code, and error presence.
  - `GET /__api__/v1/content/<guid>/repository`: whitelist repository URL,
    tracked branch, directory, polling state, last error presence,
    last-known commit, and last-fetched time.

  Do not call or export the environment endpoint. Capture `review-app/` source
  subdirectory through a redacted Connect admin-UI screenshot or approved bundle
  manifest, because it is not a direct field in the content/bundle response.
- **Test Scenarios**:
  1. New bundle uses the qualified source commit and boots to the expected
     `bootstrap required` state on `review-production`.
  2. Authenticated selected administrator/reviewer/approver identities resolve
     to their expected roles before any queue write.
  3. Pre-bootstrap rollback rehearsal: change only the review-branch setting to
     `review`, restart the same bundle, require a newer successful job record,
     and verify six legacy records are read-only.
  4. Restore `review-production`, restart, require another successful job, and
     verify bootstrap-required state. A restart may retain the same bundle; job
     evidence, not a new bundle, proves the restart. Each restart record must
     have `tag == "run_app"`, use the same active bundle, start after the
     operator action, finish successfully with zero exit code, and contain no
     error.
- **Tests**: Connect attestor outputs; redacted configuration/subdirectory
  evidence; authenticated UI role and queue-state evidence; remote ref reads
  before/after each restart.

#### Configuration and evidence checklist

Apply and attest these non-secret values in the active content item:

```text
REVIEW_APP_GH_OWNER=GMD-hub
REVIEW_APP_GH_REPO=GMD-canonical-schema
REVIEW_APP_GH_DEFAULT_BRANCH=main
REVIEW_APP_GH_REVIEW_BRANCH=review-production
REVIEW_APP_EXPECTED_SOURCE_COMMIT=<candidate-sha>
GOLEM_CONFIG_ACTIVE=production
REVIEW_APP_USER=unset
REVIEW_APP_OFFLINE=unset
REVIEW_APP_ROLES=unset
```

Use only the whitelisting attestor plus redacted manual configuration evidence.
Do not copy Publisher/rsconnect metadata or any secret value into the report.
- **Acceptance criteria**: production remained on the hold branch through the
  staging gate; the active new bundle is built from the qualified
  SHA; all three human identities resolve correctly; API, subdirectory, and
  redacted configuration evidence agree; rollback to six-record legacy
  read-only mode and restoration to bootstrap-required mode both succeed without
  changing either review ref; no production queue has been written.

## Phase 6: Production bootstrap and evidence

### 6. Bootstrap, smoke-test, and reconcile production

- **Requirements**: R1, R3, R13, R14, R15
- **Files**: remote `review-production` paths
  `extraction/30_review/*.review.yml`,
  `extraction/30_review/queue-manifest.yml`, and
  `extraction/30_review/queue-index.yml`
- **Details**: The authenticated human administrator verifies the modal displays
  the qualified expected source SHA, total, module counts, and
  `review-production`, then triggers bootstrap exactly once. Automation observes
  and validates but does not trigger the human-owned write. Successful
  publication proves the payload-size preflight passed; no unavailable exact
  byte count is required. If UI success is uncertain, inspect remote state and
  never replay when a manifest or index exists.
- **Test Scenarios**: happy path - one atomic commit enrolls the complete set;
  edge case - the UI reloads after a successful commit but before displaying
  success, requiring remote-state verification instead of replay; error path -
  expected/current source mismatch, source movement, count/path mismatch,
  payload overflow, partial/uncertain publication, or orphan index.
- **Tests**: remote head/tree reads; exact validator command against a detached
  checkout; bootstrap commit diff; actor and expected-source audit comparison.

#### Bootstrap command and evidence checklist

After the authenticated human administrator confirms and triggers bootstrap,
run the read-only verification commands:

```sh
git fetch origin review-production
git rev-parse origin/review-production
git ls-tree -r --name-only origin/review-production extraction/30_review
git ls-tree -r --name-only origin/review-production extraction/30_review | rg '[.]review[.]yml$' | wc -l
git show origin/review-production:extraction/30_review/queue-manifest.yml
git show origin/review-production:extraction/30_review/queue-index.yml
git worktree add --detach <queue-validation-worktree> origin/review-production
```

Set the terminal working directory to
`<queue-validation-worktree>/review-app`, set
`RENV_PATHS_LIBRARY=<qualified-renv-library>` from Phase 2, and execute the
validator shipped by that detached candidate checkout:

```sh
REVIEW_APP_OFFLINE=1 Rscript tools/validate-production-queue.R --repo <queue-validation-worktree> --expected-source <candidate-sha> --expect-bootstrap-state
```

Require 267 record files. Compare the bootstrap commit to its first parent and
require exactly 269 added queue paths: 267 records, manifest, and index. The
inherited `.gitkeep` may remain unchanged and is excluded from that count.
- **Acceptance criteria**: validator exits zero; all records are v2, `draft`,
  and unassigned; totals are `267` and `9/14/24/90/61/69`; expected source SHA,
  all four Release A blockers, `approval_mode: disabled`, bootstrap actor, and
  bootstrap commit are recorded; `review` remains unchanged.

#### Authenticated smoke and guardrail checklist

- **Requirements**: R14, R15
- **Files**: one designated smoke artifact record and
  `extraction/30_review/queue-index.yml` on `review-production`
- **Details**: Verify the dashboard shows 267 unassigned rows and zero
  approvals through the compact index path. Select and record one smoke artifact
  at run time. The human reviewer saves and then submits. These are exactly two
  ordered non-force commits, not one combined operation. With the artifact now
  `in-review`, the human approver uses the adversarial Shiny input sequence below
  because the ordinary Approve button is correctly hidden. Compare the branch
  head before/after and require no approval commit.
- **Test Scenarios**: save commit has body + record + index and `saved` event;
  submit commit has record + index and `submitted` event; final state is
  `in-review`; approval injection returns `approval_mode is disabled`; malformed
  injection or wrong role cannot write; dashboard telemetry remains four reads.
- **Tests**: authenticated UI evidence; resulting Git diffs/audit events;
  before/after ref comparison; Connect request-count telemetry.

Execute and record this sequence:

1. Confirm 267 dashboard rows, all unassigned, and zero approvals.
2. Select and record one smoke artifact; do not hard-code it before the run.
3. Record head H0. As reviewer, edit and click Save Draft. Record H1 and require
   one commit changing body, record, and index with a `saved` event.
4. Click Submit for review. Record H2 and require one later commit changing only
   record and index with a `submitted` event and final `in-review` state.
5. As approver on that artifact, record H2 and execute in the browser console:

   ```js
   Shiny.setInputValue("detail-act_approve", Date.now(), {priority: "event"})
   Shiny.setInputValue("detail-confirm_approve", Date.now(), {priority: "event"})
   ```

   Capture the action-feedback error panel containing
   `approval_mode is disabled`; the generic notification is not sufficient.
   Re-read the branch head and require it still equals H2.
6. Confirm production telemetry reports exactly four repository reads for a
   dashboard refresh and zero per-record reads. Live drift evidence comes only
   from the completed staging gate; production `main` is not mutated.

- **Acceptance criteria**: H1 and H2 prove exactly two ordered atomic commits;
  selected artifact reaches `in-review`; index/record identities agree;
  adversarial approval is denied server-side with no ref movement; production
  telemetry matches the four-read index contract; staging drift evidence remains
  linked in the execution report.

#### Final reconciliation command checklist

- **Requirements**: R1, R15
- **Files**:
  `.cg-docs/work-reports/2026-08-26-complete-release-a-production-queue-cutover.md`
- **Details**: Re-read remote refs and trees after smoke testing. Prove the
  legacy `review` branch remains at the preserved SHA and contains only its six
  calibration records. Prove `main` has no production queue files and
  `review-production` retains the bootstrap and smoke history. Record baseline
  and final SHAs, test counts, CI URLs/statuses, branch rule evidence, redacted
  Connect configuration, API deployment facts, bootstrap commit/counts,
  selected smoke artifact, approval/drift evidence, residual warnings, and the
  tested rollback procedure. Do not copy secrets or stale Publisher metadata.
- **Test Scenarios**: happy path - all invariants and evidence reconcile; edge
  case - a non-secret deployment fact changed during the run and is reconciled
  to the latest API state; error path - legacy branch drift, queue files on
  `main`, missing evidence, or an unexplained production commit.
- **Tests**: remote ref/tree comparisons; parsed final manifest/index; Connect
  API re-query; secret scan of the report; completion-contract evidence audit.

```sh
git fetch --prune origin
git ls-remote origin refs/heads/main refs/heads/review refs/heads/review-production
git ls-tree -r --name-only origin/main extraction/30_review
git ls-tree -r --name-only origin/review extraction/30_review
git ls-tree -r --name-only origin/review-production extraction/30_review
git log --oneline --decorate origin/review-production -- extraction/30_review
```

Require `review` to retain the preserved SHA, which is the definitive invariant.
At that SHA it contains exactly six `*.review.yml` records plus the existing
`extraction/30_review/.gitkeep` and
`extraction/30_review/VAR-educat4.body.md`. The
`main` tree must contain no production manifest, queue index, or v2 review
records. Re-query Connect deployment facts, scan the work report for accidental
secret values, and reconcile every V/C row before completion.
- **Acceptance criteria**: all required verification rows and constraints have
  executed evidence in the work report; final branch/data invariants pass;
  rollback remains available; the plan is ready for completion without an
  accepted exception.

## Testing Strategy

- **Code layer**: focused tests cover branch constants, ref coexistence,
  expected-source enforcement, queue validator, Connect field whitelisting,
  request counts, exact action commit sets, and all fail-closed actions.
- **Package layer**: full `devtools::test()`, source build, installed-package
  `R CMD check`, and the repository Python suite run in the isolated candidate
  checkout. Golem module tests capture module returns and namespaced inputs.
- **CI layer**: both required checks must be green for the exact candidate. The
  prior failed run cannot satisfy any evidence row.
- **Staging layer**: full GitHub App/Connect/identity/write path is exercised in
  a separate repository and content item, including live drift, adversarial
  approval, rollback, and five measured dashboard refreshes.
- **Governance layer**: force/delete tests run only on an equivalent disposable
  probe ref. Production gets non-destructive canaries plus read-only ruleset
  inspection.
- **Deployment layer**: the whitelisting attestor proves active content, bundle,
  source commit, and jobs; approved UI/manifest evidence proves app subdirectory.
  A rebuild requires a new bundle; a restart requires a new successful job.
- **Data layer**: the queue validator proves exact records, path set, source
  identity, blockers, and deterministic index from a detached checkout. UI row
  count alone is insufficient.
- **Production layer**: bootstrap is one commit; reviewer smoke is two commits;
  approval denial is an adversarial server request with unchanged branch head.

## Documentation Checklist

- [ ] Operator guide and README consistently use `review-production` and expected-source pinning.
- [ ] Work report records Phase 1 changes, candidate SHA, test counts, CI URLs, and clean-checkout evidence.
- [ ] Staging repository/GUID, identities, drift probes, request counts, latency, rollback, and teardown policy are recorded without secrets.
- [ ] Ruleset payload, actor IDs, probe results, production canaries, and final ruleset ID are recorded.
- [ ] Connect rebuild and restart evidence is whitelisted; subdirectory evidence is redacted.
- [ ] Bootstrap commit/actor/source/counts/blockers/manifest/index and successful payload preflight are recorded.
- [ ] Save H1, submit H2, exact path diffs/events, approval denial, and unchanged post-denial head are recorded.
- [ ] Legacy `review`, `main`, and `review-production` final invariants are recorded.
- [ ] Data rollback and application-code rollback remain distinct.

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Ref-name collision recurs in code or docs. | Production branch creation is impossible. | One shared constant, global search, ref-coexistence regression test, and `review` preservation check. |
| R CI repair is runner-specific or incomplete. | Candidate remains unqualified. | Install/assert `libgit2-dev` on the actual runner and require the entire R job green before merge/cutover. |
| Dirty ambient files contaminate qualification. | Evidence does not apply to candidate. | Detached worktree, external environments/build output, before/after clean-tree assertions. |
| Merge to `main` auto-deploys un-rehearsed code. | Production changes before staging gate. | Repoint watched source to `release-a-production-hold` before merge; restore `main` only after staging passes. |
| `main` differs from the qualified source during bootstrap. | Untested drafts are enrolled. | Required expected SHA in Connect and server-side pre/post equality checks. |
| Staging cannot be provisioned or lacks real identities. | Live guardrails remain unverified. | Staging is a hard gate; stop before production rather than accept an exception. |
| Ruleset bypass actors are wrong or too broad. | App writes fail or governance is bypassed. | Record exact Integration/Team IDs, probe equivalent rules first, compare final JSON, never broaden to all writers. |
| Destructive rule test touches production. | Production ref can be deleted/rewritten. | Force/delete tests are confined to disposable probe; production tests are removable canaries and reads. |
| Connect restart is mistaken for rebuild. | Deployment evidence is false. | New bundle for code rebuild; newer successful job for same-bundle restart. |
| Environment/API output leaks secrets. | Credential compromise. | Whitelist four read-only endpoint responses; never query/export environment; scan report. |
| Bootstrap result is ambiguous and replayed. | Divergent queue state. | Inspect remote manifest/index/head; never replay on uncertainty or existing control file. |
| Smoke evidence expects one commit. | Correct app behavior falsely fails. | Require ordered save H1 and submit H2 commits with exact path/event sets. |
| Hidden approval UI is mistaken for server authorization. | Server-side regression goes undetected. | Namespaced adversarial input, exact denial message, unchanged branch-head proof. |
| Performance claim is subjective. | Slow 267-row queue ships. | Five staging refreshes, each <=5 seconds, exactly four repository reads, zero per-record reads. |
| `.gitkeep` causes false file-count failure. | Valid bootstrap is rejected. | Count exactly 269 added queue paths and allow unchanged inherited `.gitkeep`. |

## Out of Scope

- Release B source-lock, inventory-freeze, rubric, or calibration gate work.
- Enabling `approval_mode` or removing Release A blockers.
- Any changes to protected semantics, `knowledge/`, `country-parameters/`,
  draft bodies, or artifact YAML.
- Any write, rename, delete, merge, or ref rewrite of legacy `review`.
- Deleting, force-pushing, or merging `review-production`; only the listed
  administrator canaries, human bootstrap, human reviewer save, and human
  reviewer submit commits are permitted.
- Manual bundle upload with `rsconnect::deployApp()`.
- Hand-editing, implicit repair, or re-enrollment of manifest, index, or review
  records.
- Merging production queue state to `main` or automatically promoting content
  to `knowledge/`.
- Reusing the production repository or Connect item for destructive drift or
  force/delete tests.
- Capturing exact bootstrap payload bytes; successful publication is the durable
  evidence that the enforced preflight limit passed.

## Original Completion Contract (Superseded)

The accepted completion contract and verification dispositions at the start of
this plan supersede the original strict contract below. This section remains as
historical rationale and must not be read as executed evidence.

### Outcome

Release-blocking code and CI defects are corrected and qualified at one immutable
source SHA; the same candidate passes a complete isolated live rehearsal; and
the protected `review-production` branch contains one atomically bootstrapped
queue of 267 v2 records. The active Git-backed Connect app displays the queue,
review save/submit works as two auditable commits, approval remains denied
server-side, legacy `review` is unchanged, and all evidence is durable.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Branch constant, source-SHA pin, CI dependency repair, queue validator, Connect attestor, and request telemetry are implemented and covered | Focused/full R tests, Python tests, CI implementation run | yes |
| V2 | 2 | Production code deployment is held at the pre-enabling SHA; new candidate passes isolated Python/R tests, source build/check, clean-tree proof, and both GitHub checks | Hold-branch attestation, detached qualification outputs, check-run API | yes |
| V3 | 3 | Separate staging repo/Connect item watches immutable `release-a-staging-code`, has seeded source `main`, legacy `review`, and `review-production`, and completes bootstrap, stale-session two-artifact drift denial without restart, adversarial approval denial, rollback, and identity checks | Staging refs, repository/job attestation, validator, authenticated UI evidence | yes |
| V4 | 3 | Five staging dashboard refreshes each complete within five seconds with exactly four repository reads and zero per-record reads | Instrumented request trace and timings | yes |
| V5 | 4 | Staging probe rejects destructive changes; equivalent protected staging review ref accepts one App-authenticated fast-forward save; active production ruleset includes creation protection before ref creation, exact checks/bypass actors, removed canary, and preserved `review` | Ruleset JSON/API, staging App commit, probe evidence, production refs/trees | yes |
| V6 | 5 | Production remained on hold through staging; restoring watched source to `main` produces a new active bundle from candidate SHA with exact redacted config and whitelisted API/subdirectory evidence | Hold/main source evidence, `attest-connect.R`, redacted UI/manifest evidence | yes |
| V7 | 5 | Pre-bootstrap rollback to six-record legacy read-only mode and restoration to bootstrap-required production mode both succeed without ref changes | Two restart job records, UI evidence, remote refs | yes |
| V8 | 6 | Human bootstrap adds exactly 267 records plus manifest/index in one non-force commit; validator passes source/count/blocker/state checks | Remote commit/tree and `validate-production-queue.R` | yes |
| V9 | 6 | Reviewer save H1 and submit H2 are exactly two ordered atomic commits with correct paths/events and final `in-review` state | Commit diffs, record history, index evidence | yes |
| V10 | 6 | Namespaced approval probe shows action-feedback `approval_mode is disabled`, creates no commit, and production dashboard reports four-read index path | Before/after head, action-feedback capture, request telemetry | yes |
| V11 | final | `review` is unchanged, `main` has no queue state, `review-production` retains history, and every required artifact is recorded | Final refs/API checks and execution report | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | final | Do not alter protected semantics, `knowledge/`, `country-parameters/`, draft bodies, or artifact YAML | Candidate-to-final tree comparison |
| C2 | final | Never rename, write, merge, delete, or rewrite legacy `review` | Preserved remote SHA before/after every remote phase |
| C3 | 3 | Staging repo/GUID are distinct from production and contain all destructive/drift tests | Staging/production identity attestation |
| C4 | 4 | Production destructive rule tests never occur; production branch never receives force/delete operations | Probe log and production audit |
| C5 | 5 | Secrets never enter Git, logs, attestation, screenshots, or report | Whitelist checks and secret scan |
| C6 | 6 | `approval_mode` stays disabled and all four Release A blockers remain | Queue validator and denial probe |
| C7 | 6 | Human actors perform all remote review-state writes; automation is read-only | Session identities, manifest/events/commits |
| C8 | final | Release A v2 production queue state exists only on `review-production` and never enters `main`; preserved legacy calibration state remains on `review` | Remote tree comparison |
| C9 | final | `review-production` is never force-pushed, deleted, or merged; only listed non-force commits are allowed | Ruleset and commit audit |
| C10 | 6 | Bootstrap source commit equals the Phase 2 candidate before and after generation | Modal/config/manifest and server checks |
| C11 | 2 | Production Git-backed source remains on `release-a-production-hold` from before Phase 1 merge until the Phase 3 staging gate passes | Connect source/bundle attestation at phase boundaries |

### Boundaries

- Allowed: scoped review-app/workflow/tests/docs/tooling fixes in Phase 1;
  isolated qualification; human-provisioned staging; ruleset/probe operations;
  Connect rebuild/restarts; listed human canary/bootstrap/save/submit writes;
  read-only validation and evidence reporting.
- Out of scope: Release B gates or approval enablement; protected semantic or
  canonical artifact changes; any legacy `review` write; force/delete/merge of
  production data; manual bundle upload; queue hand-edit/repair/re-enrollment;
  queue merge to `main`; automatic promotion to `knowledge/`.

### Iteration Policy

1. Treat each phase as a hard gate; do not begin the next phase until all
   required evidence for the current phase passes.
2. Human approval/availability gates are mandatory for merge, staging
   provisioning, ruleset/ref changes, Connect configuration, and every
   human-owned review-state write.
3. Record exact SHAs, identities, and API/ref evidence immediately after every
   state change.
4. Retry a transient operation at most once only after proving no remote
   mutation occurred; never replay bootstrap on ambiguity or existing controls.
5. Pause under `deviation-policy: ask` before changing a command, branch,
   repository, GUID, expected SHA, ruleset actor, evidence item, or boundary.
6. If staging fails, stop before production. If production fails before
   bootstrap, restore Connect to `review`. After bootstrap, preserve
   `review-production` intact for diagnosis and do not rewrite data.
7. Required evidence must be executed; no static inspection or accepted
   exception may substitute for staging or production gates in this release.

### Blocked-Stop Conditions

- Any `review/production` production assumption remains after Phase 1, or legacy
  `review` differs from its preserved SHA.
- R CI dependency repair fails, candidate checkout is dirty, local/build/check
  fails, or either candidate check is not green for the exact SHA.
- Required staging repo/App/Connect item or mapped human identity is unavailable;
  any staging guardrail, rollback, latency, or request-budget test fails.
- Production Git-backed source cannot be moved to the hold ref before merge,
  changes from the hold unexpectedly, or is restored to `main` before staging
  evidence passes.
- Ruleset actor IDs cannot be verified, probe controls fail, bypass is broader
  than approved, production canary remains, or production destructive testing
  would be required.
- Connect attestation disagrees on GUID/repository/source/subdirectory/commit,
  a code rebuild lacks a new successful bundle, or a restart lacks a newer
  successful job.
- `review-production` contains unexpected manifest/index state before bootstrap.
- Expected source SHA is missing/malformed/mismatched, source moves during
  generation, inventory/path/count validation fails, or publication is partial
  or uncertain.
- Bootstrap is not one atomic non-force commit, validator fails, `.gitkeep` is
  modified unexpectedly, approval/blocker state is wrong, reviewer commits do
  not match H1/H2 semantics, denial creates a commit, or telemetry exceeds four
  repository reads.
- Required evidence/report cannot be persisted, secrets appear in evidence, or
  continuing would cross `AGENTS.md`, charter, protected-artifact, or plan boundaries.
