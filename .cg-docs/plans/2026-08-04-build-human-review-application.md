---
date: 2026-08-04
title: "Build the Human Review Application"
status: active
scope: "Deep"
brainstorm: ".cg-docs/brainstorms/2026-08-04-build-human-review-application.md"
language: "R"
estimated-effort: "large"
deviation-policy: "ask"
phases: 5
completed-phases: [1]
current-phase: 2
tags: [human-review, shiny, r, posit-connect, github, audit, markdown, governance]
---

# Plan: Build the Human Review Application

## Objective

Deliver a private, Git-backed **Shiny for R** application, deployed to Posit
Connect, that lets GPID reviewers browse CVS drafts, inspect read-only YAML
and guideline evidence, edit only the human Markdown body, and drive the
governed review state machine (`draft -> in-review -> approved`, with a
`needs-revision` loop) through role-gated actions. All review state,
versions, and audit events are durably stored on a dedicated protected
review branch as per-artifact records via a GitHub App identity, with
optimistic locking and loud partial-failure recovery.

## Context

The completed extraction milestone produces governed CVS drafts under
`extraction/20_drafts/` with YAML front matter (machine-validated identity,
values, derivation, provenance) plus a human-readable Markdown body. Per
`AGENTS.md`, `extraction/30_review/` and `extraction/40_approved/` are
human-owned; this application is the human-review tool for that stage. It
must never write to `knowledge/` or alter YAML front matter, and every write
must be traceable to an authenticated human action.

The rest of this repository (extraction pipeline, schema, validators) is
Python. This application is the one deliberately R-based component, per
explicit project-lead decision (below). `renv.lock` is already named as a
lockfile this repository commits and version-controls, so an R subproject is
anticipated infrastructure, not a deviation from repository conventions.

### Provenance and corrected conflicts

This plan supersedes two details in the source brainstorm
(`2026-08-04-build-human-review-application.md`, status `decided`), resolved
through discussion during planning rather than by editing that historical
record:

1. **Implementation language.** The brainstorm specified "Shiny for
   **Python**." The 2026-07-30 strategy session
   (`.cg-docs/strategy/2026-07-30-complete-cvs-roadmap.md`) had already
   decided "Shiny in **R**... because the project lead can build and
   maintain the reviewer interface more efficiently in Shiny." The user
   confirmed explicitly: the Shiny app is R; the rest of the project stays
   Python (and possibly R for other future components). This plan is
   R-only for the app itself.
2. **Governance/approval mechanism.** The `roadmap.json` milestone
   objective states approval is "authoritative through GitHub pull
   requests," and lists `automate-review-pull-requests` and
   `configure-codeowners-protection` as milestone features. The brainstorm
   instead scoped the MVP to **direct atomic commits** to a protected
   review branch with an **in-app approval state transition**, explicitly
   marking PR automation and CODEOWNERS/branch-protection enforcement
   out of scope for this iteration. Discussion concluded this is not a
   contradiction but an unstated two-phase design: MVP now (direct-commit,
   in-app state machine), PR + CODEOWNERS hardening later as a separate,
   still-tracked effort. This plan builds the MVP only. The two
   PR/CODEOWNERS features remain in `roadmap.json` as explicitly deferred
   `idea` items, not dropped. The milestone `objective` wording is stale
   (asserts PRs are already authoritative) but rewording an `objective` is
   outside `@cg-roadmap`'s supported operations (add/remove/status/link
   only); this is flagged as a follow-up for `/cg-strategy`, not silently
   fixed here.

### Consequence: hashing cannot be shared code

The brainstorm's constraint "use the repository's existing deterministic
hashing helper" (`extraction_pipeline/hashing.py`, Python) cannot be
satisfied by direct code reuse from an R application. This plan instead
requires an **R-native SHA-256 implementation** (`openssl::sha256()` or
`digest::digest(algo = "sha256")`) that produces the same lowercase-hex
digest format as `extraction_pipeline/hashing.py`, verified by a
cross-language fixture test, so hash values remain comparable across the
Python pipeline and the R app without shared code.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | Deploy a private Shiny for **R** application to Posit Connect. | Strategy decision 2026-07-30; user confirmation |
| R2 | Use Connect authentication as the only identity source; no second login layer. | Brainstorm Requirements |
| R3 | Map authenticated identities explicitly to `reviewer`, `approver`, `administrator` via a repository-managed role map; never infer roles from email conventions. | Brainstorm Requirements; Decision 2 |
| R4 | Let reviewers browse artifacts filtered by module, review state, assignment, and action required (dashboard/work queue). | Brainstorm Requirements; Decision 10 |
| R5 | Show YAML front matter and guideline evidence/citations as read-only context beside the editable Markdown body. | Brainstorm Requirements |
| R6 | Allow edits to the Markdown body only; preserve YAML front matter exactly; reject structural alterations or invalid full-artifact serialization. | Brainstorm Requirements; AGENTS.md |
| R7 | Provide a plain Markdown textarea plus rendered preview (MVP editing experience); rich-text/Quarto editing deferred. | Brainstorm Requirements |
| R8 | Support save-draft and submit-for-review actions; support approver request-revision and approve actions; support administrator assign/reopen actions. | Brainstorm Requirements; Decision 2 |
| R9 | Implement the full state machine with a revision loop: `draft -> in-review -> approved`, `in-review -> needs-revision -> in-review`; reopening `approved` is administrator-only, targets `needs-revision`, and emits an explicit audit event. | Decision 3 |
| R10 | Record reviewer identity, role, review round, timestamps, transitions, source Git SHA, body SHA-256, and optional notes as an append-only audit history per artifact. | Brainstorm Requirements; Review Record Format |
| R11 | Detect concurrent edits through optimistic locking (remote blob SHA vs. loaded SHA); never silently overwrite a newer remote revision; preserve unsaved text on rejection. | Brainstorm Requirements; Decision |
| R12 | Use a GitHub App / dedicated bot identity via Connect secrets/environment variables, not reviewer personal access tokens. | Brainstorm Requirements |
| R13 | Read source drafts from the default branch as canonical context; write all review outputs only to a dedicated protected review branch. **Protection rule**: the review branch blocks force-pushes and deletions (GitHub branch protection rule, or repository-tier equivalent); only the GitHub App's installation token and repository administrators may push directly -- humans act only through the app, never via direct `git push`. The default branch's existing protection is untouched by this plan. | Decision 6 |
| R14 | On approval, write the full approved artifact (exact YAML + approved Markdown) to `extraction/40_approved/` on the review branch, preserving the draft's relative path under that root (e.g. a draft at `extraction/20_drafts/dem/VAR-male.md` is written to `extraction/40_approved/dem/VAR-male.md`), retaining the review working copy and full event history permanently under `extraction/30_review/` (the `.review.yml` file is never deleted or archived after approval; it remains the authoritative audit ledger and its `state` may still transition to `needs-revision` via administrator reopen). | Decision 7 |
| R15 | Store state in per-artifact review records (e.g. `extraction/30_review/VAR-<id>.review.yml`), not a single mutable manifest; the dashboard derives its view by scanning/indexing these files. | Decision 5; Review Record Format |
| R16 | Use SHA-256 for content hashing, R-native, in a format compatible with the Python pipeline's digest format (no cross-language code reuse). | Brainstorm Requirements (adapted; see Provenance) |
| R17 | Use Connect persistent storage only for disposable cache/temporary operational state, never as the authoritative audit ledger. | Decision 9 |
| R18 | For any multi-file logical operation (working artifact + review record + approved artifact), the GitHub adapter creates one atomic commit; on partial/API/network failure, fail loudly, report affected paths and commit status, and do not claim a successful transition. | Decision; Brainstorm Requirements |
| R19 | Keep pull-request automation, branch-protection enforcement, outbound notifications, automatic YAML reconciliation, database provisioning, real-time collaboration, and automatic promotion to `knowledge/` out of scope for this iteration. | Brainstorm Requirements; Provenance conflict resolution |
| R20 | Provide a storage-interface abstraction so a future database migration does not require redesigning the UI/workflow. | Decision 4 |
| R21 | Validate the MVP against a representative calibration sample before scaling. | Brainstorm Next Steps 8; roadmap `calibrate-human-review` milestone |

## Data Schemas

This section is the authoritative, plan-level definition of the per-artifact
review record, audit event, and role-map schemas. It supersedes prose
references to the brainstorm's "Review Record Format" section: if the
brainstorm is later revised, this section governs implementation, not the
brainstorm (closes the self-containedness gap flagged in plan review).

### Review record (`extraction/30_review/&lt;artifact_id&gt;.review.yml`)

| Field | Type | Required | Notes |
|---|---|---|---|
| `artifact_id` | string | yes | Matches the draft's canonical ID (e.g. `VAR-male`). |
| `source_artifact_path` | string | yes | Path to the draft under `extraction/20_drafts/`. |
| `state` | enum | yes | One of `draft`, `in-review`, `needs-revision`, `approved`. |
| `review_round` | integer >= 1 | yes | Incremented each time state re-enters `in-review` from `needs-revision`. |
| `assigned_to` | list of string | yes (may be empty) | Connect identities assigned to act next. |
| `current_content_sha256` | string (64 lowercase hex) | yes | SHA-256 of the current Markdown body. |
| `source_commit` | string (Git SHA) | yes | Commit/blob SHA of the source draft this record was built from. |
| `events` | list of Event | yes (append-only) | Full ordered history; never mutated, only appended. |

### Audit event (element of `events`)

| Field | Type | Required | Notes |
|---|---|---|---|
| `event_id` | string (UUID) | yes | Unique per event. |
| `sequence` | integer >= 0 | yes | Monotonic per-record counter assigned by the adapter at write time (`len(events)` before append); authoritative ordering tie-breaker over `occurred_at`. |
| `action` | enum | yes | One of `submitted`, `request-revision`, `approved`, `assigned`, `reopened`, `saved`. |
| `from_state` / `to_state` | enum or null | yes | Null only for non-transition actions (e.g. `saved`, `assigned`). |
| `actor` | string | yes | Connect identity of the acting user. |
| `actor_role` | enum | yes | `reviewer`, `approver`, or `administrator` at the time of the action. |
| `occurred_at` | string (RFC 3339 UTC) | yes | Wall-clock time; not used for ordering (see `sequence`). |
| `source_blob_sha` | string | yes | Blob SHA read at the start of the action. |
| `body_sha256` | string | yes | SHA-256 of the Markdown body at the time of the event. |
| `note` | string or null | no | Free-text reviewer/approver note. |

### Role map (`review-app/config/roles.yml`)

```yaml
# One entry per authenticated Connect identity. Identity is the exact
# string returned by Connect's session user field (document the actual
# field used -- email vs. username -- in the operator guide, Step 12).
roles:
  - identity: reviewer@example.org
    role: reviewer
  - identity: approver@example.org
    role: approver
  - identity: admin@example.org
    role: administrator
```

- Format: top-level `roles` key holding a list of `{identity, role}`
  objects. `role` is one of `reviewer`, `approver`, `administrator`.
- **MVP update procedure**: administrators update this file only via a
  direct repository edit (commit or PR) to the branch the app reads it
  from -- there is no in-app role-management UI in this iteration. An
  in-app admin UI for role management is explicitly out of scope for the
  MVP (see Step 8).
- An identity absent from this file resolves to "no role" / no write
  privileges (R3, Step 8) -- never a default role.

### State-transition table (authoritative; mirrors brainstorm Decision 3)

| From state | Action | Actor role | To state | Notes |
|---|---|---|---|---|
| `draft` | `submitted` | reviewer | `in-review` | |
| `in-review` | `request-revision` | approver | `needs-revision` | |
| `in-review` | `approved` | approver | `approved` | Writes to `extraction/40_approved/` (R14). |
| `needs-revision` | `submitted` | reviewer | `in-review` | Increments `review_round`. |
| `approved` | `reopened` | administrator | `needs-revision` | Administrator-only; always emits an explicit audit event. |

All other `(from_state, action)` pairs are illegal and must raise an
explicit error from `transition()` (Step 3) -- no silent no-ops.

## Implementation Steps

## Phase 1: Foundations -- models and state machine

### 1. Scaffold the R application package

- **Requirements**: R1, R20
- **Files**: `review-app/` (new isolated deployable R app/package),
  `review-app/DESCRIPTION`, `review-app/renv.lock`, `review-app/app.R` or
  `review-app/R/`, `review-app/tests/testthat/`
- **Details**: Create an isolated R project using `shiny`, `bslib` (UI),
  `yaml`, `commonmark` (Markdown preview render), `openssl` or `digest`
  (hashing), `gh` or `httr2` + `jose`/`openssl` (GitHub App JWT auth and API
  calls), `testthat` (unit tests), `shinytest2` (app-level tests). Initialize
  `renv` and commit `renv.lock` per repository convention. Keep this package
  self-contained under `review-app/` so it can be deployed to Connect as its
  own content item, independent of the Python extraction pipeline.
- **Test Scenarios**: package loads; `renv::restore()` reproduces the
  environment; app skeleton launches locally.
- **Tests**: `review-app/tests/testthat/test-scaffold.R` (package
  namespace loads without error).
- **Acceptance criteria**: `renv.lock` committed; `R CMD check`-equivalent
  or `devtools::load_all()` succeeds; empty Shiny app boots locally.

### 2. Define review-record, event, assignment, and role-map models

- **Requirements**: R3, R9, R10, R15, R16
- **Files**: `review-app/R/models.R`, `review-app/R/hashing.R`,
  `review-app/tests/testthat/test-models.R`,
  `review-app/tests/fixtures/hash_fixture.txt`,
  `review-app/tests/fixtures/generate_hash_fixture.py`,
  `review-app/tests/testthat/test-hashing.R`
- **Details**: Implement validated R list-based (or S7/R6) structures for
  exactly the fields specified in this plan's **Data Schemas** section
  above: the per-artifact review record, the audit event (including the
  `sequence` field), and the role map. Implement `hash_body(text)` in R
  using `openssl::sha256()` (or `digest::digest(algo = "sha256")`)
  returning a lowercase-hex digest.
  - **Fixture maintenance process**: commit a fixed fixture input file,
    `review-app/tests/fixtures/hash_fixture.txt` (exact bytes, no
    trailing-newline ambiguity). Commit a small, standalone script,
    `review-app/tests/fixtures/generate_hash_fixture.py`, that imports
    `extraction_pipeline/hashing.py`'s hashing function, hashes
    `hash_fixture.txt`, and prints the resulting lowercase-hex digest. Run
    this script once and hard-code its output as a constant,
    `PY_REFERENCE_SHA256`, at the top of `test-hashing.R`, with a comment
    stating the exact command used to generate it and the date/commit it
    was generated against. `test-hashing.R` computes `hash_body()` over
    the same fixture file's bytes in R and asserts equality against
    `PY_REFERENCE_SHA256`. If `extraction_pipeline/hashing.py`'s digest
    format ever changes, `generate_hash_fixture.py` must be re-run and
    `PY_REFERENCE_SHA256` manually updated in the same commit -- add a
    one-line comment to `extraction_pipeline/hashing.py` pointing back to
    this fixture/constant so a future editor is warned to update it.
- **Test Scenarios**: valid record parses; missing required field rejected;
  R-computed hash over the committed fixture bytes matches the hard-coded
  `PY_REFERENCE_SHA256` constant.
- **Tests**: `test-models.R`, `test-hashing.R`.
- **Acceptance criteria**: models validate/reject exactly per the Data
  Schemas section; hash format parity test passes against
  `PY_REFERENCE_SHA256`.

### 3. Implement the state-transition and authorization engine

- **Requirements**: R8, R9, R3
- **Files**: `review-app/R/state_machine.R`, `review-app/R/authorization.R`,
  `review-app/tests/testthat/test-state-machine.R`,
  `review-app/tests/testthat/test-authorization.R`
- **Details**: Implement a pure function `transition(record, action, actor,
  role)` enforcing exactly the state-transition table defined in this
  plan's **Data Schemas** section above (`draft -> in-review`,
  `in-review -> needs-revision`, `in-review -> approved`,
  `needs-revision -> in-review`, `approved -> needs-revision`). Every
  applied transition appends an event with a `sequence` value equal to the
  current length of `events` before the append (Data Schemas section). All
  other `(from_state, action)` pairs raise an explicit error (fail loudly,
  no silent no-ops). Implement `authorize(role, action)` as a single source
  of truth consulted both by the engine and by UI action-availability logic
  (UI hiding is not a security boundary).
- **Test Scenarios**: every legal transition succeeds and appends one
  event with a correctly incrementing `sequence`; every illegal transition
  (wrong role, wrong from-state, skipped state) is rejected with a
  descriptive error; reopen path requires administrator role and produces
  an event.
- **Tests**: `test-state-machine.R`, `test-authorization.R`.
- **Acceptance criteria**: 100% of the state-transition table in this
  plan's Data Schemas section is covered by passing/failing test cases
  (one test per row, plus at least one illegal-transition test per state).

## Phase 2: GitHub adapter

### 4. Implement GitHub App authentication

- **Requirements**: R12
- **Files**: `review-app/R/github_auth.R`,
  `review-app/tests/testthat/test-github-auth.R`
- **Details**: Sign a GitHub App JWT from a Connect-secret private key,
  exchange it for an installation access token scoped to this repository,
  and cache/refresh the token per its expiry. Credentials come only from
  Connect environment variables/secrets, never from reviewer PATs.
- **Test Scenarios**: valid key produces a usable installation token;
  expired/invalid key fails loudly with a clear error; token refresh occurs
  before expiry.
- **Tests**: `test-github-auth.R` (mocked JWT/HTTP layer); manual
  integration check against a disposable test GitHub App installation.
- **Acceptance criteria**: token retrieval succeeds against a real
  disposable test repository in at least one integration run.

### 5. Implement authenticated reads and hash verification

- **Requirements**: R13, R16
- **Files**: `review-app/R/github_adapter.R`,
  `review-app/tests/testthat/test-github-adapter.R`
- **Details**: Read draft artifacts from the default branch (source
  context) and review records/approved artifacts from the review branch.
  Every read returns content plus its blob SHA. Provide
  `verify_body_hash(content, expected_sha256)` using the Phase 1 hashing
  helper.
- **Test Scenarios**: read returns correct content + blob SHA from a
  disposable test repo/branch; hash verification succeeds/fails correctly.
- **Tests**: `test-github-adapter.R` against a disposable test repository.
- **Acceptance criteria**: V3 evidence passes.

### 6. Implement atomic multi-file commit writes with optimistic locking

- **Requirements**: R11, R14, R18
- **Files**: `review-app/R/github_adapter.R` (extended),
  `review-app/tests/testthat/test-github-adapter.R` (extended)
- **Details**: Build a Git tree from the changed files for one logical
  operation (working artifact + review record, and additionally the
  approved artifact on approval), create one commit, and update the review
  branch ref -- all atomic from the caller's perspective. Before writing,
  re-fetch the branch ref's current commit SHA and, from its tree, the
  current blob SHA for each touched path; reject the write if either (a)
  any touched-path blob SHA differs from the SHA loaded at read time, or
  (b) the branch ref's commit SHA has moved at all since load, even if the
  specific touched blobs are unchanged (a moved ref means the write's tree
  base is stale and must be rebuilt against current HEAD). On rejection,
  return a clear "stale, please reload" error and never force-push or
  overwrite a newer remote revision. **Unsaved-text preservation**: on
  rejection, keep the user's in-progress Markdown body in the current
  Shiny session's server-side reactive state and re-render the editor
  pre-filled with that text plus a banner prompting the user to review the
  newer remote version before reapplying edits; this is session-lifetime
  only (not persisted to Connect storage, per R17) and is lost if the
  session ends first. If rejection is because the artifact's `state`
  itself changed (e.g. an approver already moved it out of `in-review`),
  the banner states that explicitly rather than showing a generic
  SHA-mismatch message.
- **Test Scenarios**: happy-path atomic commit with multiple files; stale
  write (touched blob SHA changed since load) is rejected without
  overwriting; stale write where only the branch ref moved (an unrelated
  file changed) is also rejected; concurrent-writer simulation confirms no
  lost update; unsaved text is retained in reactive session state after a
  rejected save.
- **Tests**: `test-github-adapter.R` stale-save and atomic-commit
  scenarios, run against a disposable test repository/branch.
- **Acceptance criteria**: V4 evidence passes.

### 7. Implement partial-failure detection and operator recovery path

- **Requirements**: R18
- **Files**: `review-app/R/github_adapter.R` (extended),
  `review-app/R/recovery.R`, `review-app/tests/testthat/test-recovery.R`
- **Details**: If a multi-step Git operation (tree creation, commit
  creation, ref update) fails partway, surface exactly which paths/commit
  steps succeeded or failed, and never mark the review-record transition as
  applied unless the full atomic operation completed. Provide an operator
  utility/report to inspect and reconcile an interrupted operation.
- **Test Scenarios**: simulated failure after tree creation but before ref
  update is detected and reported; no transition is recorded as successful
  when the underlying commit did not complete.
- **Tests**: `test-recovery.R` using injected/mocked API failures.
- **Acceptance criteria**: V5 evidence passes.

## Phase 3: Shiny application

### 8. Resolve Connect identity to role

- **Requirements**: R2, R3
- **Files**: `review-app/R/identity.R`,
  `review-app/tests/testthat/test-authorization.R` (extended)
- **Details**: Read the Connect-provided authenticated user identity
  (`session$user` or equivalent Connect header/environment mechanism) and
  resolve it against the repository-managed role map (a version-controlled
  file, e.g. `review-app/config/roles.yml`, editable only by an
  administrator through the app or direct repo edit). No second
  authentication layer; missing/unmapped identities get no write
  privileges and a clear "not authorized" state, not a silent default role.
- **Test Scenarios**: mapped identity resolves to correct role; unmapped
  identity is denied all write actions; role map load failure fails loudly.
- **Tests**: `test-authorization.R` (extended with identity-resolution
  cases).
- **Acceptance criteria**: V6 evidence passes.

### 9. Build the dashboard / work queue

- **Requirements**: R4, R15
- **Files**: `review-app/R/app_ui.R`, `review-app/R/app_server.R`,
  `review-app/R/index.R` (scan/index review records)
- **Details**: Scan `extraction/30_review/*.review.yml` records (via the
  GitHub adapter) to build a filterable dashboard by module, state,
  assignment, and action-required. This scan is a derived view, not a
  source of truth (per Decision 5); no separate manifest is authoritative.
  Use the GitHub Trees API (single recursive tree call for
  `extraction/30_review/`) rather than the paginated Contents API, so the
  MVP scan is a single request regardless of artifact count up to the
  Trees API's 100,000-entry/7MB response ceiling -- acceptable for the
  calibration-scale (5-10 artifact) and near-term (tens to low hundreds of
  artifacts) volumes anticipated; revisit if the corpus approaches that
  ceiling. **Refresh strategy**: no push/websocket updates in the MVP; the
  dashboard re-scans on an explicit user-triggered "Refresh" action and on
  fresh page load/session start. Reviewers are not automatically notified
  of other reviewers' changes mid-session; the optimistic-locking check in
  Step 6 is the authoritative concurrency guard, and a stale dashboard view
  only ever produces a rejected save (never a silent overwrite), so the
  refresh strategy is a UX convenience, not a correctness mechanism.
- **Test Scenarios**: dashboard reflects current states across a set of
  fixture review records; filters narrow results correctly; a record with
  malformed YAML surfaces an explicit error rather than being silently
  skipped; manual refresh reflects a state change made by a concurrent
  simulated actor since initial load.
- **Tests**: `review-app/tests/testthat/test-index.R`; `shinytest2` smoke
  test of dashboard rendering.
- **Acceptance criteria**: dashboard loads and filters correctly against
  fixture data.

### 10. Build the artifact detail view (read-only context + Markdown editor)

- **Requirements**: R5, R6, R7, R11
- **Files**: `review-app/R/app_ui.R` (extended),
  `review-app/R/app_server.R` (extended), `review-app/R/frontmatter.R`
- **Details**: Render YAML front matter and guideline evidence/citations as
  read-only panels; render the Markdown body in a textarea with a
  `commonmark`-rendered live preview, calling
  `commonmark::markdown_html(text, extensions = TRUE)` with its default
  safe rendering (raw HTML/script tags in the source Markdown are not
  passed through; do not enable any `smart`/raw-HTML-passthrough option
  that would defeat this). On load, capture and retain the blob SHA and
  body SHA-256 for later optimistic-lock comparison (Step 6). Reject any
  attempt to alter YAML on save; validate the full artifact reserializes
  with front matter byte-identical to what was loaded.
- **Test Scenarios**: front matter round-trips unchanged after a Markdown
  edit and save; an edit that would alter YAML is rejected; preview
  renders Markdown correctly.
- **Tests**: `review-app/tests/testthat/test-frontmatter.R`
  (front-matter immutability); `shinytest2` UI test.
- **Acceptance criteria**: C1 (front-matter immutability) and V7 evidence
  pass.

### 11. Wire role-gated actions and the audit timeline

- **Requirements**: R8, R9, R10, R14
- **Files**: `review-app/R/app_server.R` (extended),
  `review-app/R/actions.R`
- **Details**: Wire save-draft, submit, request-revision, approve, assign,
  and reopen buttons to the Phase 1 state machine and Phase 2 adapter,
  gated by `authorize(role, action)`. Render the append-only event history
  as an audit timeline. On approve, write the approved artifact to
  `extraction/40_approved/` per R14 in the same atomic commit as the review
  record update.
- **Test Scenarios**: each role sees only its authorized actions; each
  action produces the correct transition, event, and (for approve) the
  correct file write to `extraction/40_approved/`; audit timeline reflects
  full history in order.
- **Tests**: `shinytest2` end-to-end scenarios per role; extends
  `test-state-machine.R` integration coverage.
- **Acceptance criteria**: V7 evidence passes; C3 (human-owned,
  traceable writes) holds for every action.

## Phase 4: Operator documentation

### 12. Write the Posit Connect operator guide

- **Requirements**: R1, R2, R12, R17, R19, R20
- **Files**: `review-app/docs/operator-guide.md`
- **Details**: Document private Connect access/group configuration,
  required Connect identity fields, GitHub App credential provisioning and
  rotation, review-branch and repository configuration, deployment steps,
  monitoring, and the Step 7 incident-recovery procedure for partial
  writes. Explicitly document that Connect storage is disposable cache
  only (R17) and that pull-request/CODEOWNERS hardening is a deferred,
  separately tracked roadmap effort (R19).
- **Test Scenarios**: n/a (documentation artifact).
- **Tests**: none (manual review).
- **Acceptance criteria**: V8 evidence passes -- document exists and covers
  all listed topics.

## Phase 5: Calibration

### 13. Validate the MVP against a calibration sample

- **Requirements**: R21
- **Files**: none new (validation run); optional
  `review-app/tests/testthat/test-integration.R`
- **Details**: Deploy to Connect (or a staging equivalent) and run the full
  workflow -- browse, edit, submit, revise, approve -- against the
  roadmap's planned calibration sample of five to ten variables across
  complexity levels (`calibrate-human-review` milestone), using a
  disposable test repository/branch for the write path if production
  branch protection is not yet configured.
- **Test Scenarios**: full lifecycle completes for at least one artifact of
  each state-machine path (approve directly; needs-revision loop; admin
  reopen).
- **Tests**: `test-integration.R` end-to-end scenario, plus manual sign-off
  notes.
- **Acceptance criteria**: V9 evidence passes.

## Testing Strategy

- Unit tests (`testthat`) for models, hashing, state machine, and
  authorization: fast, no network.
- Integration tests for the GitHub adapter (auth, read, atomic write, stale
  write, partial failure) run against a **disposable test repository or
  dedicated test branch** -- never against the production CVS repository's
  protected review branch.
- App-level tests (`shinytest2`) for dashboard rendering, artifact detail
  round-trip, and role-gated action visibility/behavior.
- Cross-language fixture test proving R and Python SHA-256 digests match
  for identical byte content (C6).
- No test may claim a successful state transition unless the underlying
  Git write actually completed (mirrors R18/production behavior in test
  doubles).

## Documentation Checklist

- [ ] `review-app/docs/operator-guide.md` (Step 12)
- [ ] `review-app/README.md` covering local dev setup (`renv::restore()`,
      running the app locally against a test repo)
- [ ] Role map file (`review-app/config/roles.yml`) documented with format
      and administrator-update procedure
- [ ] Cross-reference from `compound-gpid.context.md` or `AGENTS.md`-adjacent
      docs noting the app exists and where it writes (human approval
      required for any such doc edit, per file permissions)

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| GitHub API partial failures leave inconsistent state | Step 7's explicit recovery path; never claim success without full atomic completion (R18) |
| Optimistic locking race between two reviewers | Step 6's SHA-comparison-before-write; reject stale writes, preserve unsaved text |
| R and Python hash digests silently diverge in format (e.g. case, encoding) | Step 2's cross-language fixture test (C6) run in CI |
| Role map misconfiguration silently grants/denies wrong access | Step 8 fails loudly on unmapped identities; `authorize()` is the single gate consulted everywhere, not just in UI |
| Dashboard scan-based indexing becomes slow as artifact count grows | Explicitly out of scope for MVP optimization (Decision 5); flagged as a future roadmap item, not solved here |
| Mixed Python/R repository increases CI and dependency-maintenance surface | `review-app/` is isolated with its own `renv.lock`; does not touch Python CI workflows in this plan |
| GitHub App credential leakage or overly broad scope | Step 4 restricts to Connect secrets only; App should be scoped to minimum required repo permissions (documented in operator guide) |

## Out of Scope

- Pull-request automation and CODEOWNERS/branch-protection enforcement
  (roadmap features `automate-review-pull-requests`,
  `configure-codeowners-protection` remain tracked, deferred).
- Outbound notifications (email/Slack/etc.).
- Automatic YAML reconciliation from approved Markdown (separate milestone:
  `complete-universal-records`).
- Database provisioning / PostgreSQL migration (Approach 3 in the
  brainstorm; deferred).
- Real-time multi-user collaborative editing.
- Automatic promotion to `knowledge/`.
- Rich-text or Quarto-based editing (plain Markdown + preview only).
- Rewording `roadmap.json`'s stale milestone `objective` text (flagged as a
  `/cg-strategy` follow-up, not performed by this plan).

## Completion Contract

### Outcome

A private, Git-backed **Shiny for R** application is deployed to Posit
Connect that lets reviewers browse CVS drafts, view read-only YAML and
guideline evidence, edit only the human Markdown body, and drive the
governed review state machine (`draft -> in-review -> approved`, with a
`needs-revision` loop) through role-gated actions. All review state,
versions, and audit events are durably stored on a dedicated protected
review branch as per-artifact records via a GitHub App identity, with
optimistic locking and loud partial-failure recovery. PR automation and
CODEOWNERS enforcement remain explicitly deferred, tracked roadmap features.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|--------------------|------------------|----------|
| V1 | 1 | Review-record, event, assignment, and role-map models validate against this plan's Data Schemas section | `review-app/tests/testthat/test-models.R` via `testthat::test_dir()` | yes |
| V2 | 1 | Transition and authorization functions enforce the state machine and role gates; illegal transitions rejected | `test-state-machine.R`, `test-authorization.R` | yes |
| V3 | 2 | GitHub adapter performs authenticated reads, returns blob SHA + SHA-256, and hash verification matches | `test-github-adapter.R` against a disposable test repo | yes |
| V4 | 2 | Atomic multi-file commit writes succeed; a stale write (SHA mismatch) is rejected without overwrite | `test-github-adapter.R` stale-save scenario | yes |
| V5 | 2 | Partial write failure surfaces affected paths and commit status; does not claim a transition | `test-recovery.R` | yes |
| V6 | 3 | App resolves Connect identity to role via the repository role map; writes denied for unauthorized roles | `test-authorization.R` (identity cases) | yes |
| V7 | 3 | Artifact detail UI: read-only YAML + evidence panels, Markdown-only editor, preview, audit timeline, state-appropriate actions | deployed Connect smoke check + `shinytest2` app tests | yes |
| V8 | 4 | Operator guide documents private access/groups, identity fields, GitHub App credentials, review-branch config, deployment, monitoring, incident recovery | `review-app/docs/operator-guide.md` | yes |
| V9 | 5 | MVP validated on a representative calibration sample before scaling | deployed run against sample + `test-integration.R` | yes |

### Constraints

| ID | Constraint | Check |
|----|------------|-------|
| C1 | YAML front matter preserved exactly; structural alterations or invalid full-artifact serialization rejected | `test-frontmatter.R` immutability test |
| C2 | Writes only on the protected review branch; default branch remains canonical source context | adapter target-branch assertion tests |
| C3 | `extraction/30_review/` and `extraction/40_approved/` remain human-owned; app writes only on authenticated human action, traceable to that person | authorization/audit tests |
| C4 | Connect persistent storage used only for disposable cache, never as authoritative audit ledger | design review + tests |
| C5 | No PR automation, no CODEOWNERS/branch-protection enforcement, no outbound notifications, no automated promotion to `knowledge/`, no database, no real-time collaboration in this iteration (deferred to a separate, later, roadmap-tracked effort) | scope review |
| C6 | R-native SHA-256 (`openssl`/`digest`) produces lowercase-hex digests matching the Python pipeline's format; no cross-language code reuse | cross-language fixture test comparing R digest to a known Python-hashed value |
| C7 | Connect auth is the only login; no second authentication layer | app wiring test |
| C8 | App is implemented in R (`shiny`), not Python/Streamlit -- corrects the brainstorm's Python framing to match the 2026-07-30 strategy decision and explicit user confirmation | plan provenance note |

### Boundaries

- **Allowed**: Shiny for R app under `review-app/`; Connect auth + role map;
  dashboard/work queue; read-only YAML/evidence panels; Markdown-only
  editing + preview; save-draft; submit/revision/approve/reopen
  transitions; per-artifact review records with append-only event history;
  GitHub App adapter (R, e.g. `gh`/`httr2`/`gert`) with atomic commits +
  optimistic locking + recovery; `testthat`/`shinytest2` tests; operator
  guide; calibration validation.
- **Out of scope**: pull-request automation, CODEOWNERS/branch-protection
  enforcement, outbound notifications, automatic YAML reconciliation,
  database provisioning, real-time collaboration, automatic promotion to
  `knowledge/`, rich-text/Quarto editing. (PR automation and CODEOWNERS are
  tracked as deferred `roadmap.json` features, not dropped.)

### Iteration Policy

1. Work front-to-back in phases; do not start a later phase with pending
   `yes` evidence from an earlier phase.
2. A deviation under policy `ask` pauses for approval; under `autonomous`
   is justified and recorded; under `strict` is a blocked-stop.
3. Integration behaviors must be proven against a disposable test
   repository/branch, not only static inspection.
4. Any new public function added gets at least one `testthat` test (per
   project context convention).

### Blocked-Stop Conditions

- Required verification cannot be executed (safe runner unavailable).
- Any required evidence fails after allowed recovery attempts.
- A required deviation is found under `ask` without user approval, or
  under `strict` at all.
- A protected boundary (e.g., write to `knowledge/` or the default branch)
  must be crossed.
- Front-matter immutability or optimistic-locking guarantees cannot be
  demonstrated.
