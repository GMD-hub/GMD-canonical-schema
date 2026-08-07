---
date: 2026-08-07
title: "Calibrate Human Review"
status: active
scope: "Deep"
brainstorm: ".cg-docs/brainstorms/2026-08-07-calibrate-human-review.md"
language: "both"
estimated-effort: "large"
deviation-policy: "ask"
artifact-schema-version: 1
execution-report: ".cg-docs/work-reports/2026-08-07-calibrate-human-review.md"
completed-phases: [1, 2, 3]
current-phase: 4
phases: 5
tags: [human-review, calibration, shiny, review-rubric, measurement, interface, governance, r, python]
---

# Plan: Calibrate Human Review

## Objective

Make the Shiny review app live-capable, materialize a 6-variable calibration
sample with full front matter (3 real + 3 fixtures carrying seeded known
defects), execute a structured live-operator run that populates content-error,
defect, and friction logs, simplify the interface based on measured friction,
and finalize a two-layer review rubric with acceptance criteria that gates
promotion from `extraction/30_review/` to `extraction/40_approved/` at scale.

## Context

The predecessor plan (`.cg-docs/plans/2026-08-04-build-human-review-application.md`)
delivered the Shiny review app with all 5 phases "completed," but its own
Phase 5 full-mode review (execution report Run 5, Step 3.9) found unresolved
P0/P1 defects that block a real live operator run: the adapter is never wired
into the server, the production write transport cannot send payloads, the
Connect entry point calls a non-exported function, C1 front-matter immutability
is a no-op, audit/content-hash binding is broken, `authorize()` fails open,
the preview has an XSS vector, a real RSA private key leaks into the test tree,
and `DT` is undeclared. Tests pass only against an in-memory GitHub double.

This plan pays down the **live-capable subset** of those defects (Phase 1)
before any live run. The remaining P0/P1 set (exhaustive `validate_review_record`,
NAMESPACE/roxygen drift, `review-app/README.md`) is deferred to a tracked
separate effort. See the brainstorm's "Next Steps" governance escalations and
the Out of Scope section below.

The calibration sample is defined in
`.cg-docs/calibration/2026-08-06-calibration-sample.md` (6 variables: 3 real
from `knowledge/variables/dem/`, 3 fixtures). `extraction/20_drafts/` is
currently empty. The chosen approach (brainstorm Approach 1) is
instrument-first: define the measurement framework, rubric, and protocol up
front so materialized drafts conform to the rubric template and errors log in
the right schema from the first write.

### Key code findings (from source inspection)

- `app.R:8` calls `reviewapp::shiny_review_app()` but NAMESPACE exports
  `run_review_app` (line 23), not `shiny_review_app` (defined in `run.R:4`).
- `app_server.R:30` creates `adapter <- reactiveValues()` but never assigns
  `adapter$handle`; detail view (`:119-126`) fabricates placeholder front/body;
  `save_draft` (`:246`) is a no-write stub.
- `gh_adapter_http` (`github_adapter.R:78`) signature is
  `function(method, url, token)` — no `body` formal. `adapter_write_atomic`
  (`recovery.R:67,80,89,98`) passes `body = ...`, which raises "unused
  argument" in production.
- `transition` (`state_machine.R:55-56`) sets `source_blob_sha = rec$source_commit`
  and `body_sha256 = rec$current_content_sha256`; the `body_sha256` parameter
  in `perform_action` (`actions.R:54-65`) is never passed through.
- `authorize` (`authorization.R:19-21`) returns `!is.null(role)` for unknown
  actions (fail-open).
- `render_markdown_preview` (`frontmatter.R:67`) calls
  `commonmark::markdown_html(markdown, extensions = TRUE)`; `extensions = TRUE`
  enables raw-HTML passthrough, and the output is rendered via `shiny::HTML()`
  (`app_server.R:149`) — stored XSS once persistence lands.
- `app_ui.R:37` hard-codes module filter choices `c("All"="", "dem", "edu",
  "welfare")`; `index.R:26` derives `module` from the path directory name.
- `test-github-auth.R:44` writes an RSA key via
  `openssl::write_pem(key, file.path(tempdir(), "reviewapp-test-pubkey.pem"))`
  — into `tempdir()`, not the test tree. The hygiene concern (key on disk
  during test) is valid but no `pubkey` file exists in the repo to delete.

## Requirements

| ID | Requirement | Source |
|----|-------------|--------|
| R1 | `gh_adapter_http` accepts and sends a JSON `body` via `httr2::req_body_json` | Brainstorm Q1; execution report P1 |
| R2 | Connect entry point boots: `shiny_review_app` is exported or `app.R` calls an exported function | Brainstorm Q1; execution report P1 |
| R3 | Adapter is wired into the Shiny server from Connect secrets (`adapter$handle`) | Brainstorm Q1; execution report P1 |
| R4 | Detail view loads real draft + review record via the adapter, not placeholder data | Brainstorm Q1; execution report P1 |
| R5 | `save_draft` persists the edited body via the adapter and records a `saved` event | Brainstorm Q1; execution report P1 |
| R6 | `split_frontmatter` handles CRLF; `frontmatter_unchanged` is a meaningful byte-comparison; approved-path verifies front matter | Brainstorm Q2; execution report P0 |
| R7 | `transition` accepts `body_sha256`; the event's `body_sha256` and the record's `current_content_sha256` are updated; `source_blob_sha` uses the review-record blob SHA at action time | Brainstorm Q1; execution report P0 |
| R8 | `authorize()` returns `FALSE` for unknown/unlisted actions (fail-closed) | Brainstorm Q1; execution report P1 |
| R9 | `render_markdown_preview` blocks raw HTML / XSS (disable raw-HTML extension) | Brainstorm Q1; execution report P1 |
| R10 | Dashboard module filter choices are derived from unique modules in the index, not hard-coded | Brainstorm Q3/Q6 |
| R11 | `test-github-auth.R` uses `tempfile()` instead of `file.path(tempdir(), ...)` for test isolation | Plan review P2.4 |
| R12 | `DT` declared in DESCRIPTION Imports; `httr2` moved to Imports; `renv.lock` updated to restore runtime/test env | Brainstorm Q1; execution report P1 |
| R13 | Content-error taxonomy defined: 4 future agent-review dimensions + human-review content categories, with `stage` + severity | Brainstorm Q4 |
| R14 | Content-error log format + separate app-defect log format defined as structured records | Brainstorm Q4 |
| R15 | Two-layer rubric defined: Layer 1 automated structural (YAML schema + front-matter unchanged + required sections present & non-stub); Layer 2 human per-section content quality | Brainstorm Q5 |
| R16 | Live-operator protocol + friction-log format defined (paths, time-on-task, errors, 1–5 rating, free-text, severity block/slow/cosmetic) | Brainstorm Q6 |
| R17 | 3 real drafts copied from `knowledge/variables/dem/` to `extraction/20_drafts/dem/` with full front matter | Brainstorm Q2/Q3 |
| R18 | 3 fixture drafts authored with full front matter matching `knowledge/` structure + seeded known defects; directories match `module_id` | Brainstorm Q2/Q3/Q8 |
| R19 | Known-answer key kept separate under `.cg-docs/calibration/`; materialization/extraction errors logged in the content-error log | Brainstorm Q8 |
| R20 | Disposable GitHub repo + narrowly scoped GitHub App + Connect staging + `roles.yml` (reviewer + approver) provisioned; app deployed | Brainstorm Q7; execution report checklist |
| R21 | Live operator run executed: reviewer + approver walk all state-machine paths; structured friction captured per step | Brainstorm Q6/Q7 |
| R22 | Friction, content-error, and defect logs populated; both rubric layers exercised; 30→40 promotion gate tested | Brainstorm Q5 |
| R23 | Logs aggregated: error/defect rates, catch rate vs known-answer key, friction-by-step | Brainstorm Q4/Q8 |
| R24 | Interface simplified per friction decision rule (block / ≥4 by ≥2 reviewers → fix before scaling) | Brainstorm Q6 |
| R25 | Rubric acceptance criteria finalized from run evidence; ready to gate promotion at scale | Brainstorm Q5 |

## Implementation Steps

## Phase 1: Live-capable subset

### 1. Fix production write transport and Connect entry point

- **Requirements**: R1, R2, R12
- **Files**: `review-app/R/github_adapter.R`, `review-app/R/run.R`,
  `review-app/NAMESPACE`, `review-app/app.R`, `review-app/DESCRIPTION`,
  `review-app/tests/testthat/test-github-adapter.R`
- **Details**:
  - **`gh_adapter_http`**: Add a `body = NULL` parameter to the function
    signature. When `body` is not NULL, call
    `httr2::req_body_json(req, body)` before `httr2::req_perform(req)`. This
    fixes the "unused argument (body = ...)" error raised by every production
    POST/PATCH in `adapter_write_atomic` (`recovery.R:67,80,89,98`).
  - **Entry point**: Either (a) add `export(shiny_review_app)` to NAMESPACE
    alongside the existing `export(run_review_app)`, or (b) change `app.R:8`
    to call `reviewapp::run_review_app()`. Option (a) is preferred (adds one
    line; `run_review_app` already delegates to `shiny_review_app`). Ensure
    `shiny_review_app` has an `@export` roxygen tag or a manual NAMESPACE
    entry (see Out of Scope re: full roxygen drift).
  - **DESCRIPTION**: Move `httr2` from `Suggests` to `Imports` (it is on the
    production code path, not optional). Add `httr2` to the `Imports` list.
- **Test Scenarios**: production transport sends a JSON body on POST/PATCH
  (verified with a test double that captures the `body` argument and asserts
  it is non-NULL and well-formed); `app.R` loads without "object not found"
  error.
- **Tests**: `test-github-adapter.R` — add a test that `gh_adapter_http` (or
  a thin wrapper) passes `body` through to `req_body_json` by injecting a
  mock that records the request body; verify the exported entry point
  resolves via `getFromNamespace`.
- **Acceptance criteria**: `gh_adapter_http` accepts `body`; `app.R` calls
  an exported function; `httr2` in DESCRIPTION Imports.

### 2. Wire adapter into server and detail view

- **Requirements**: R3, R4, R5
- **Files**: `review-app/R/app_server.R`, `review-app/R/actions.R`,
  `review-app/R/state_machine.R`, `review-app/tests/testthat/test-app-smoke.R`,
  `review-app/tests/testthat/test-actions.R`
- **Details**:
  - **Adapter wiring**: In `app_server.R`, build the adapter from Connect
    secrets / environment variables: `REVIEW_APP_GH_OWNER`,
    `REVIEW_APP_GH_REPO`, `REVIEW_APP_GH_DEFAULT_BRANCH`,
    `REVIEW_APP_GH_REVIEW_BRANCH`, `GITHUB_APP_ID`,
    `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`. Use
    `new_github_adapter(owner, repo, default_branch, review_branch,
    get_token, http)` where `get_token` calls `installation_token()` (Phase 3
    auth). Assign the result to `adapter$handle` at session start (replace
    the empty `reactiveValues()` at `:30`). If the env vars are absent, fail
    loudly with a clear "adapter not configured" error (not an empty queue).
    For local/dev, support an injectable adapter via a package option or env
    override (preserves the R20 storage-interface abstraction and the
    existing offline tests).
  - **Detail view**: Replace the fabricated placeholder at `:119-126` with
    real adapter reads: `adapter_read_draft(adapter$handle, path)` for the
    draft (default branch) and `adapter_read_review(adapter$handle,
    record_path)` for the review record (review branch). Use
    `split_frontmatter` to separate front and body for display. Store
    `blob_sha`, `branch_head_sha`, and `body_sha256` in `detail_state` for
    optimistic locking.
  - **save_draft**: Replace the no-write stub at `:234-247` with a real
    write: verify front matter is unchanged (Step 3 fix), then call
    `perform_action(adapter$handle, rec, body_sha256=..., blob_sha=...,
    branch_head_sha=..., action="saved", ...)`. Fix `perform_action`
    (`actions.R:75`) to route `saved`/`assigned` through `record_action`
    (`state_machine.R:75`) instead of `transition` (which rejects them as
    illegal transitions). The `saved` action writes the review record (with
    the `saved` event) to the review branch; the working-copy body is
    persisted as a companion file in the same atomic commit.
  - **Authorization model update (P1.1)**: Before fixing `authorize()` to
    fail-closed (Step 4), add `saved = "reviewer"` and
    `assigned = "administrator"` to the `action_requires_role` list in
    `authorization.R:5-11`. Without this, Step 4's fail-closed change would
    reject `save_draft` because `saved` is not in the action-role map. This
    ordering dependency must be respected: Step 2 updates the map, Step 4
    makes it fail-closed.
  - **Companion-file convention (P1.2)**: The working-copy body is persisted
    as a companion file at `extraction/30_review/<artifact_id>.body.md` on
    the review branch, alongside the review record at
    `extraction/30_review/<artifact_id>.review.yml`. The adapter writes both
    files in one atomic commit via `adapter_write_with_recovery`. The detail
    view loads the body from this companion file via `adapter_read_review`
    (falling back to the source draft on the default branch if no companion
    file exists yet — first load before any save). The companion file is
    never read by the state machine or the rubric; it is a UI convenience
    for the editor.
- **Test Scenarios**: adapter is built from env vars and `adapter$handle` is
  non-NULL; detail view loads real front + body from the adapter; save_draft
  persists and appends a `saved` event without a state transition; `saved`
  and `assigned` actions no longer raise "illegal transition."
- **Tests**: `test-app-smoke.R` — inject a test-double adapter and verify the
  queue populates and detail view loads real data; `test-actions.R` — add
  `saved`/`assigned` path tests through `perform_action`.
- **Acceptance criteria**: queue loads from real adapter; detail view shows
  real front matter + body; save_draft writes the body as a companion file at
  `extraction/30_review/<id>.body.md` and records a `saved` event; `saved`
  and `assigned` are in `action_requires_role`.

### 3. Fix front-matter immutability and audit binding

- **Requirements**: R6, R7
- **Files**: `review-app/R/frontmatter.R`, `review-app/R/state_machine.R`,
  `review-app/R/actions.R`, `review-app/tests/testthat/test-frontmatter.R`,
  `review-app/tests/testthat/test-state-machine.R`
- **Details**:
  - **`split_frontmatter` CRLF**: Normalize line splitting to handle both
    `\n` and `\r\n` (e.g. split on `\r?\n` or normalize `\r\n` → `\n` before
    splitting). Currently CRLF artifacts cause `split_frontmatter` to return
    `front = NULL`, which makes `frontmatter_unchanged` return `TRUE`
    (frontmatter.R:54), silently disabling C1.
  - **`frontmatter_unchanged` meaningful check**: The current implementation
    (`frontmatter.R:55`) compares `split_frontmatter(proposed)$front` to
    `original_front`. When called as
    `frontmatter_unchanged(front, join_body(front, body))` the comparison is
    always TRUE because `join_body` just re-pastes `front`. Fix: compare the
    front matter extracted from the *user's edited full artifact* against the
    *originally loaded front matter*, not a re-joined copy. The server must
    pass the actual editor output (front + body as the user sees it) — if the
    user tampered with YAML, the extracted front will differ.
  - **Approved-path verification**: On the `approved` action, verify that the
    `approved_content` front matter is byte-identical to the loaded draft's
    front matter before writing to `extraction/40_approved/`. Currently the
    approved path does no front-matter/hash verification (execution report P0).
    Note (P2.5): in the current `app_server.R:210-211` construction,
    `approved_content` is built from `detail_state$front` (the loaded front
    matter), so this check is a structural invariant — it always passes by
    construction. This is defense-in-depth; a meaningful runtime gate would
    require the `approved_content` construction to change (e.g. if the user
    can paste arbitrary content into the approval).
  - **`transition` body_sha256 and blob_sha (P2.1, P2.3)**: Add two
    parameters to `transition()` (`state_machine.R:23`):
    - `body_sha256 = rec$current_content_sha256` (default preserves backward
      compatibility with all existing ~15 test call sites, satisfying C5).
    - `blob_sha = rec$source_commit` (default preserves backward
      compatibility; replaces `source_blob_sha = rec$source_commit` at `:55`).
    Use `body_sha256` for the event's `body_sha256` field (currently
    `rec$current_content_sha256` at `:56`). Update
    `new_rec$current_content_sha256` to the passed-in `body_sha256` (currently
    unchanged). Use `blob_sha` for the event's `source_blob_sha` (currently
    `rec$source_commit` at `:55`). Pass both from `perform_action`
    (`actions.R:75`) to `transition`. Apply the same two-parameter additions
    to `record_action` (`state_machine.R:75-96`) for the `saved`/`assigned`
    event path, with the same defaults.
- **Test Scenarios**: CRLF artifact front matter is correctly extracted and
  preserved; a YAML-tampering edit is rejected; approved-path front matter
  is verified; `transition` event carries the passed-in `body_sha256` and the
  record's `current_content_sha256` is updated; `source_blob_sha` is the
  review-record blob SHA, not `source_commit`.
- **Tests**: `test-frontmatter.R` — CRLF fixture, tamper-reject, approved-path
  verification; `test-state-machine.R` — body_sha256 flows through; event
  `source_blob_sha` equals the passed blob SHA.
- **Acceptance criteria**: C1 immutability is a real check (rejects tampering
  on CRLF and normal artifacts); audit events carry the correct body hash and
  blob SHA; record's `current_content_sha256` is updated on every action;
  `transition()` and `record_action()` accept `body_sha256` and `blob_sha`
  with backward-compatible defaults (C5 satisfied).

### 4. Fix security, preview, and dashboard filter

- **Requirements**: R8, R9, R10
- **Files**: `review-app/R/authorization.R`, `review-app/R/frontmatter.R`,
  `review-app/R/app_ui.R`, `review-app/R/app_server.R`,
  `review-app/tests/testthat/test-authorization.R`,
  `review-app/tests/testthat/test-frontmatter.R`,
  `review-app/tests/testthat/test-index.R`
- **Details**:
  - **`authorize` fail-closed**: Change `authorization.R:19-21` to return
    `FALSE` (not `!is.null(role)`) when `required` is NULL (unknown/unlisted
    action). Unknown actions must be denied for all roles. **Prerequisite
    (P1.1)**: Step 2 must have already added `saved` and `assigned` to
    `action_requires_role`; otherwise this change breaks `save_draft`.
  - **Preview XSS (P2.2)**: In `render_markdown_preview` (`frontmatter.R:67`),
    do not pass `extensions = TRUE` (which enables raw-HTML passthrough).
    Instead, pass a specific extension list that enables useful formatting
    extensions while excluding `raw_html`:
    `extensions = c("table", "strikethrough", "autolink", "tagfilter")`.
    The `tagfilter` extension is the key safety feature — it angle-bracket
    escapes raw HTML tags. Verify that `<img onerror>`, `<svg onload>`, and
    `javascript:` hrefs are stripped or escaped. Do NOT use the blunt
    approach of omitting `extensions` entirely, as this would regress
    table and strikethrough rendering in the preview.
  - **Dashboard module filter**: In `app_ui.R:37`, replace the hard-coded
    `choices = c("All"="", "dem", "edu", "welfare")` with a
    `renderUI`/`uiOutput` that derives choices from `unique(queue_index()$module)`
    at render time. This makes `geo` appear (for `VAR-urban`) and drops dead
    `edu`/`welfare` when absent. The `module` column is already derived from
    the source-artifact-path directory name (`index.R:26`), which is correct
    given `module_id`-authoritative directories (Step 9).
- **Test Scenarios**: unknown action denied for all roles; XSS payloads are
  stripped from preview HTML; module filter shows only modules present in the
  index (including `geo`); no dead `edu`/`welfare` when absent.
- **Tests**: `test-authorization.R` — unknown-action fail-closed test;
  `test-frontmatter.R` — XSS payload test on `render_markdown_preview`;
  `test-index.R` — module filter choices derive from index.
- **Acceptance criteria**: `authorize` returns FALSE for unknown actions
  (with `saved`/`assigned` already in the action-role map per Step 2);
  preview escapes raw HTML via `tagfilter` extension; module filter is
  data-driven.

### 5. Remove leaked key and fix dependencies

- **Requirements**: R11, R12
- **Files**: `review-app/tests/testthat/test-github-auth.R`,
  `review-app/DESCRIPTION`, `review-app/renv.lock`
- **Details**:
  - **Test isolation (P2.4)**: The actual code at `test-github-auth.R:44`
    writes to `file.path(tempdir(), "reviewapp-test-pubkey.pem")`, not
    `pubkey` in the test tree. No `pubkey` file exists in the repo to delete,
    and no `.gitignore` entry is needed. The fix is to replace
    `file.path(tempdir(), ...)` with `tempfile(fileext = ".pem")` for proper
    test isolation (each test run gets a unique path). Wrap with
    `on.exit(unlink(tmp), add = TRUE)` for cleanup.
  - **DT**: Add `DT` to DESCRIPTION `Imports` (it is used in `app_server.R:52`
    and `app_ui.R:54` but not declared).
  - **renv.lock (P2.6)**: Run `renv::snapshot()` to update `renv.lock` so it
    includes `DT`, `httr2` (now in Imports), and any other runtime/test
    dependencies that were missing. **Prerequisite**: a working R environment
    with `renv` bootstrapped and all packages installed. If the environment is
    not set up, run `renv::restore()` first to bootstrap from the existing
    lockfile, then install the new/changed packages, then `renv::snapshot()`.
    Verify `renv::restore()` reproduces the environment from the updated
    lockfile. This is a manual operator step — document the bootstrap sequence
    in the operator guide.
- **Test Scenarios**: `test-github-auth.R` passes with tempfile isolation;
  `renv::restore()` succeeds; `R CMD check` does not report `DT` as an
  undeclared dependency.
- **Tests**: `test-github-auth.R` passes with tempfile; `renv` restore smoke;
  `R CMD check` clean.
- **Acceptance criteria**: test isolation via `tempfile()`; `DT` in
  DESCRIPTION; `renv.lock` restores cleanly.

## Phase 2: Instrumentation specification

### 6. Define the measurement framework

- **Requirements**: R13, R14
- **Files**: `.cg-docs/calibration/measurement-framework.md` (new)
- **Details**: Define a unified content-error taxonomy aligned to the 4
  future `independent-agent-review` dimensions plus human-review content
  categories:

  | Dimension | Agent-review category | Human-review category |
  |---|---|---|
  | Source-grounding | `source-grounding` | `content-accuracy` |
  | Schema-compliance | `schema-compliance` | `formatting` |
  | Rules-caveats | `rules-caveats` | `completeness` |
  | Consistency-derivation | `consistency-derivation` | `clarity` |

  Each content-error record has: `error_id`, `artifact_id`, `stage`
  (extraction / human-review / agent-review), `category` (one of the above),
  `severity` (block / major / minor / info), `description`, `detected_by`
  (reviewer identity, rubric layer, or automated check name), `detected_at`
  (RFC 3339 UTC), `section` (which Markdown section), `status` (open /
  resolved / escalated). The calibration populates extraction + human-review;
  agent-review categories are reserved, tagged-but-not-populated.

  Define a **separate app-defect log** with: `defect_id`, `component`
  (e.g. `github_adapter`, `frontmatter`, `preview`), `severity` (P0/P1/P2/P3),
  `description`, `source` (execution-report review or live-run observation),
  `status` (open / fixed / deferred), `fix_reference` (step or commit).
  App defects do NOT share the content-error severity scale and do NOT dilute
  content error rates (C13).
- **Test Scenarios**: taxonomy covers all 4 agent dimensions + 5 human
  categories; stage and severity fields are defined; log and defect formats
  are self-describing with examples.
- **Tests**: spec review (no automated test; the rubric in Step 7 references
  these categories).
- **Acceptance criteria**: `measurement-framework.md` exists with the
  taxonomy table, content-error record schema, and defect-log schema.

### 7. Define the two-layer review rubric

- **Requirements**: R15
- **Files**: `.cg-docs/calibration/review-rubric.md` (new, draft)
- **Details**: Define a rubric with two layers:

  **Layer 1 — automated structural gate (blocks submission)**:
  - YAML front matter parses as valid YAML (schema-valid per the Pydantic
    variable-spec model).
  - Front matter is byte-unchanged from the loaded draft (C1).
  - All required Markdown sections are present: `## Definition`, `##
    Conceptual intent`, `## Construction notes`, `## Consistency checks`, `##
    Escalation triggers`, `## Common mistakes`, `## Change log` (matching the
    structure of the 3 real `knowledge/variables/` artifacts).
  - No section is a stub: each section has non-trivial content (e.g. > 1
    sentence or > 50 characters; a precise threshold is set from the
    calibration run in Step 14).

  **Layer 2 — human content-quality gate (blocks approval)**:
  - **Definition accuracy**: the definition matches the guideline source
    evidence panel.
  - **Construction-notes path coverage**: all derivation paths are
    documented (e.g. educat4's three paths: derive from educat7, educat5,
    direct mapping).
  - **Consistency-check actionability**: checks are specific and actionable
    (not vague).
  - **Escalation-trigger presence**: triggers are present and relevant to the
    variable's risk profile.
  - **Common-mistakes relevance**: mistakes are real, instructive, and
    non-redundant.
  - Each section rated: `pass` / `revise` / `fail`.

  **Promotion gate** (30 → 40): Layer 1 passes AND Layer 2 is all-`pass` or
  `revise-with-notes` AND no open `block`/`major` extraction errors on the
  artifact. Agent-review dimensions are reserved as future gates (not active
  in this calibration).

  Include a section-template reference (the 7 required sections from the real
  artifacts) so Step 9 can conform drafts to the rubric.
- **Test Scenarios**: rubric defines both layers with pass/revise/fail;
  promotion gate is explicit; section template is documented.
- **Tests**: spec review.
- **Acceptance criteria**: `review-rubric.md` exists with Layer 1, Layer 2,
  promotion gate, and section template.

### 8. Define the live-operator protocol and friction log

- **Requirements**: R16
- **Files**: `.cg-docs/calibration/live-operator-protocol.md` (new)
- **Details**: Define the structured protocol for the live run:

  **Roles**: reviewer (edits Markdown, saves, submits) + approver (reviews,
  requests revision or approves). Administrator reopen is covered by
  `test-integration.R` only (Q7 decision).

  **Per-artifact steps** (recorded for each):
  1. Browse: open dashboard, filter by module/state, locate the artifact.
  2. Load detail: click the row; verify YAML/evidence panels and Markdown body
     load from the adapter.
  3. Read: review the read-only YAML front matter and guideline evidence.
  4. Edit: enrich/fix the Markdown body.
  5. Preview: check the rendered preview.
  6. Save draft: save; verify persistence.
  7. Submit: submit for review; verify state → `in-review`.
  8. (Approver) Review: load the artifact; read the enriched Markdown.
  9. (Approver) Request revision OR Approve.
  10. If revision: reviewer revises, re-submits; approver approves.
  11. Verify approved artifact in `extraction/40_approved/`.

  **Friction-log record** per step: `session_id`, `reviewer_identity`, `role`,
  `artifact_id`, `step` (browse/load/read/edit/preview/save/submit/review/
  request-revision/approve), `time_on_task_seconds`, `error_count`,
  `friction_rating` (1–5), `severity` (block / slow / cosmetic), `free_text`,
  `timestamp`.

  **Decision rule**: a friction item that blocks a required path, or is
  rated ≥4 by ≥2 reviewers, triggers a simplification change before scaling.
  Cosmetic items batch for later.

  **Known-defect detection**: reviewers note which seeded defects they
  identified during review; the rubric's Layer 1 (automated) is also run
  against each draft to measure automated catch rate. The known-answer key
  (Step 9) is the scoring reference.
- **Test Scenarios**: protocol covers all paths (approve-direct,
  needs-revision loop); friction log has all fields; decision rule is stated.
- **Tests**: spec review.
- **Acceptance criteria**: `live-operator-protocol.md` exists with steps,
  friction-log schema, and decision rule.

## Phase 3: Materialize calibration drafts

### 9. Materialize the 6 calibration drafts

- **Requirements**: R17, R18, R19
- **Files**: `extraction/20_drafts/dem/VAR-male.md`,
  `extraction/20_drafts/dem/VAR-educat4.md`,
  `extraction/20_drafts/dem/VAR-educy.md`,
  `extraction/20_drafts/dem/VAR-educat7.md` (fixture),
  `extraction/20_drafts/geo/VAR-urban.md` (fixture),
  `extraction/20_drafts/dem/VAR-marital.md` (fixture),
  `.cg-docs/calibration/known-answer-key.md` (separate)
- **Details**:
  - **3 real members** (R17): Copy `VAR-male.md`, `VAR-educat4.md`,
    `VAR-educy.md` from `knowledge/variables/dem/` to
    `extraction/20_drafts/dem/`. These already carry full front matter and
    full Markdown bodies with the 7 required sections. Set `status: draft`
    and `human_reviewed: false` in provenance (they already are). These are
    the likely-clean baseline. **Note (P1.3)**: the calibration manifest
    (`.cg-docs/calibration/2026-08-06-calibration-sample.md`) and
    `test-integration.R:40-42` currently assign `module = "edu"` to
    `VAR-educat4`, `VAR-educy`, and `VAR-educat7`. Per the Q3 decision
    (`module_id` authoritative), these must use `module = "dem"` to match
    their front-matter `module_id: MOD-DEM`. The manifest and integration
    test must be updated to use `dem/` paths before materialization. The
    `edu`/`MOD-DEM` discrepancy is logged as a governance finding (see
    materialization errors below), not as a path convention.
  - **3 fixtures** (R18): Author `VAR-educat7`, `VAR-urban`, `VAR-marital`
    with full front matter mirroring the real artifacts' structure (identity,
    value_codes/allowed_range, missing_codes, derivation graph,
    country_parameters, prerequisites, rules, source_hints, provenance) and
    full Markdown bodies with all 7 required sections. Directories match
    `module_id`: `educat7` and `marital` → `dem/` (MOD-DEM), `urban` → `geo/`
    (MOD-GEO). Each fixture carries **seeded known defects** (R18/Q8):
    - `VAR-educat7`: a hallucinated rule reference (e.g. `RULE-EDU-999` that
      does not exist in `knowledge/index.md`) in the `rules` field; a missing
      escalation trigger section entry.
    - `VAR-urban`: a `module_id`/directory mismatch in front matter (e.g.
      `module_id: MOD-DEM` while the file is under `geo/`); a derivation-graph
      break (`derived_from` references a non-existent variable).
    - `VAR-marital`: a stub `Construction notes` section (< 50 chars); a
      `value_codes` entry with an invalid label.
  - **Known-answer key** (R19): Write `.cg-docs/calibration/known-answer-key.md`
    listing each seeded defect, its location, category (per the Step 6
    taxonomy), and expected severity. This file is kept separate from the
    drafts and used only for scoring in Step 12.
  - **Materialization errors** (R19): Log any real extraction/consistency
    errors discovered during materialization into the content-error log
    format from Step 6. Key finding to log: the calibration manifest and
    integration test assigned `edu` to `educat4`/`educy`/`educat7`, but the
    real artifacts carry `module_id: MOD-DEM` and live under
    `knowledge/variables/dem/`; `knowledge/variables/edu/` is empty. Record
    as a `consistency-derivation` error, stage `extraction`, severity
    `major`. The path correction (P1.3) is applied in this step.
- **Test Scenarios**: all 6 drafts exist with full front matter; schema
  validation passes on the 3 real members; the 3 fixtures have the 7 required
  sections; known-answer key lists all seeded defects; materialization error
  logged.
- **Tests**: Pydantic schema validation (`python3 -m schema.validate` or
  equivalent) on each draft; file-existence check; known-answer key content
  check.
- **Acceptance criteria**: 6 drafts in `extraction/20_drafts/` with full
  front matter and `module_id`-authoritative directories; known-answer key
  separate; materialization error logged.

## Phase 4: Live operator run

### 10. Provision and deploy

- **Requirements**: R20
- **Files**: disposable GitHub repo (external); `review-app/config/roles.yml`
  (update with 2 test identities); Connect content item (external)
- **Details**: Follow the execution report's deployment checklist (Run 5):
  1. Provision a disposable GitHub repo + narrowly scoped GitHub App
     (contents read/write on default + `review` branches only); register
     Connect secrets `GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`,
     `GITHUB_APP_PRIVATE_KEY`, `REVIEW_APP_GH_OWNER`, `REVIEW_APP_GH_REPO`,
     `REVIEW_APP_GH_DEFAULT_BRANCH`, `REVIEW_APP_GH_REVIEW_BRANCH`.
  2. Create the protected `review` branch; block force-push/deletion; confirm
     default-branch protection is untouched.
  3. Stage the 6 calibration drafts from Step 9 as drafts under
     `extraction/20_drafts/<module>/<id>.md` on the default branch.
  4. Configure `review-app/config/roles.yml` with 2 test Connect identities
     (reviewer + approver).
  5. Deploy the content item (`rsconnect::deployApp` on `review-app/`),
     private group access, Connect auth confirmed as the only login (C7).
  6. Verify the app boots (Phase 1 Step 1 entry-point fix) and the queue
     populates from the adapter (Phase 1 Step 2 wiring fix).
- **Test Scenarios**: app boots on Connect; queue shows 6 artifacts; module
  filter includes `dem` and `geo`.
- **Tests**: manual deployment verification.
- **Acceptance criteria**: deployed app is reachable, private, and shows the
  6-artifact queue with correct modules.

### 11. Execute the live operator run

- **Requirements**: R21, R22
- **Files**: `.cg-docs/calibration/live-run-2026-08-07.md` (run log),
  `.cg-docs/calibration/content-error-log.yaml` (populated),
  `.cg-docs/calibration/defect-log.yaml` (populated),
  `.cg-docs/calibration/friction-log.yaml` (populated)
- **Details**: The reviewer and approver each walk the protocol from Step 8
  against the deployed app:
  - **Reviewer** walks: browse → load → read → edit → preview → save → submit
    for each artifact they are assigned.
  - **Approver** walks: browse → load → review → request-revision or approve.
  - At least one artifact exercises each state-machine path: approve-direct
    (VAR-male or VAR-educat4), needs-revision loop (VAR-educy or VAR-educat7),
    (admin reopen is covered by `test-integration.R` only).
  - Each reviewer records a friction-log entry per step (time-on-task,
    errors, 1–5 rating, severity, free-text).
  - Reviewers note which seeded defects they identified (for catch-rate
    scoring in Step 12).
  - The rubric's Layer 1 (automated structural) is run against each draft at
    submission; results recorded.
  - The rubric's Layer 2 (human content) is applied by the approver at the
    review step; results recorded.
  - The 30→40 promotion gate is exercised: at least one artifact is promoted
    to `extraction/40_approved/` and verified on the review branch.
  - Any app defects encountered during the run are logged in the defect log.
  - Any content errors found are logged in the content-error log.
- **Test Scenarios**: all state-machine paths complete; logs are populated
  with all required fields; promotion gate exercised; at least one artifact
  reaches `extraction/40_approved/`.
- **Tests**: manual run + log completeness check.
- **Acceptance criteria**: run log + all 3 logs populated; both rubric layers
  exercised; 30→40 gate tested; all paths completed.

## Phase 5: Measure, simplify, finalize

### 12. Aggregate logs and measure

- **Requirements**: R23
- **Files**: `.cg-docs/calibration/calibration-report.md` (new)
- **Details**: Aggregate the live-run logs:
  - **Content-error rate**: count of content errors by category and severity,
    per artifact. Compare reviewer-detected errors against the known-answer
    key to compute **catch rate** (detected / total seeded) and **false
    negatives** (missed defects). Also compute Layer 1 (automated) catch rate
    separately.
  - **Defect rate**: count of app defects by severity; note which were Phase 1
    fixes vs. newly discovered during the live run.
  - **Friction-by-step**: average friction rating and time-on-task per step;
    identify steps with block-severity friction or ≥4 rating by ≥2 reviewers.
  - Surface the `edu`/`MOD-DEM` materialization finding and any other
    extraction errors discovered.
- **Test Scenarios**: report includes catch rate, false negatives, error
  rates, defect counts, friction-by-step.
- **Tests**: report completeness check.
- **Acceptance criteria**: `calibration-report.md` exists with catch rate,
  false negatives, error/defect rates, and friction analysis.

### 13. Simplify the interface

- **Requirements**: R24
- **Files**: `review-app/R/app_ui.R`, `review-app/R/app_server.R`,
  `.cg-docs/calibration/calibration-report.md` (updated with simplification
  decisions)
- **Details**: Apply the friction decision rule from Step 8:
  - For each friction item with `block` severity OR rated ≥4 by ≥2 reviewers:
    implement a simplification change (reduce steps per path, remove
    dead/ambiguous controls, clarify labels, surface guideline evidence
    beside the editor).
  - For `cosmetic` items: batch for a later iteration (record in the report).
  - Known-issue fixes already in Phase 1 (module filter derivation) are
    confirmed; any additional simplification discovered during the live run
    is applied here.
  - Re-test the simplified interface against the in-memory double and a
    short smoke check on Connect staging.
- **Test Scenarios**: simplified interface passes the existing test suite;
  friction items triggering the rule are resolved; cosmetic items are
  batched.
- **Tests**: full `testthat` suite + `shinytest2` smoke.
- **Acceptance criteria**: all block/≥4-by-≥2 friction items resolved;
  existing tests pass; changes documented in the calibration report.

### 14. Finalize the rubric

- **Requirements**: R25
- **Files**: `.cg-docs/calibration/review-rubric.md` (finalized)
- **Details**: Finalize the rubric from the live-run evidence:
  - Set the stub-detection threshold from the calibration data (e.g. if the
    run shows the 50-char threshold is too lenient or strict, adjust).
  - Confirm or adjust the promotion gate criteria based on whether any
    artifact was incorrectly promoted or incorrectly blocked.
  - Add a "calibration evidence" section referencing the catch rate, false
    negatives, and friction analysis from Step 12.
  - Document the known limitations (N=6 artifacts, 2 reviewers, no agent
    review) and the conditions under which the rubric should be re-calibrated
    (e.g. when the `independent-agent-review` milestone adds agent-review
    gates, or when the sample grows beyond the calibration scale).
  - Note that promotion to `knowledge/rubrics/` is a human step (per AGENTS.md,
    agents may not write to `knowledge/`); the finalized rubric draft in
    `.cg-docs/calibration/` is the handoff for human promotion.
- **Test Scenarios**: rubric acceptance criteria are concrete, evidence-
  backed, and ready to gate promotion at scale.
- **Tests**: rubric review.
- **Acceptance criteria**: `review-rubric.md` finalized with evidence-backed
  thresholds, promotion gate, calibration evidence, and known limitations.

## Testing Strategy

- **Phase 1**: `testthat` unit tests for each fix (adapter wiring, transport,
  front-matter immutability, audit binding, authorize fail-closed, XSS,
  module filter). The existing 224 tests must still pass (C5). The full suite
  is re-run after each step.
- **Phase 1→3**: `shinytest2` app smoke tests with an injected adapter double
  verify the server loads real data and actions persist. The live Connect run
  (Phase 4) is the production verification.
- **Phase 3**: Pydantic schema validation on each materialized draft (Python);
  the 3 real members must validate identically to their `knowledge/`
  originals.
- **Phase 2/3/4**: instrumentation specs and logs are reviewed manually (no
  automated test); the rubric is validated by exercising it in the live run.
- **Cross-language**: the SHA-256 parity test (`test-hashing.R`) must continue
  to pass after Phase 1 changes (C6).
- **No test may claim a successful state transition unless the underlying Git
  write actually completed** (mirrors R18 / production behavior).

## Documentation Checklist

- [ ] `.cg-docs/calibration/measurement-framework.md` (Step 6)
- [ ] `.cg-docs/calibration/review-rubric.md` (Step 7 draft → Step 14 finalized)
- [ ] `.cg-docs/calibration/live-operator-protocol.md` (Step 8)
- [ ] `.cg-docs/calibration/known-answer-key.md` (Step 9)
- [ ] `.cg-docs/calibration/live-run-2026-08-07.md` (Step 11)
- [ ] `.cg-docs/calibration/calibration-report.md` (Step 12 → updated Step 13)
- [ ] `review-app/docs/operator-guide.md` updated with Connect secret names
      (REVIEW_APP_GH_*) and the disposable-repo deployment checklist (Step 10)
- [ ] Phase 1 fix summary in the execution report

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Phase 1 scope creeps into deferred hardening (exhaustive validate_review_record, NAMESPACE/roxygen, README) | C4 boundary; deviation policy `ask` pauses for approval; deferred items tracked as a separate roadmap effort |
| Existing 224 tests break during Phase 1 fixes | C5; re-run full suite after each step; fix tests that asserted the old (buggy) behavior |
| No Posit Connect instance or disposable GitHub repo available for the live run | Blocked-stop condition; Phase 4 cannot execute without provisioning; the in-memory double + structured walkthrough is a fallback (but does not satisfy V10) |
| Seeded defects in fixtures are too obvious or too subtle, making catch rate uninformative | Step 12 reports catch rate AND false negatives; if all/none are caught, the report notes the calibration is uninformative and recommends a re-run with adjusted defects |
| The `edu`/`MOD-DEM` module ambiguity blocks materialization | Q3 decision: `module_id` is authoritative; the discrepancy is logged as a governance finding, not a blocker; escalate to `/cg-strategy` for the MOD-EDU question |
| `save_draft` body-persistence design resolved (P1.2) | Step 2 defines the companion-file convention: body → `extraction/30_review/<id>.body.md` on the review branch, written atomically with the review record |
| Reviewer availability (2 reviewers, specific roles) delays the live run | Step 10 provisioning is done first; the run can be scheduled when reviewers are available; the instrumentation (Phase 2) and materialization (Phase 3) proceed independently |

## Out of Scope

- **Deferred P0/P1** (tracked as a separate roadmap effort under
  `human-review-application`): exhaustive `validate_review_record` (event
  schema, `artifact_id`/`source_artifact_path`/`source_commit` validation,
  path-poisoning prevention); NAMESPACE/roxygen `@export` drift (54/55 exports
  lack `@export` tags); `review-app/README.md` missing; `rprojroot` in wrong
  DESCRIPTION section; `assigned_to` NULL normalization; `sub()` module
  extraction silent pass-through; `new_event` unknown-action/sequence bounds.
- PR automation, CODEOWNERS/branch-protection enforcement (roadmap features
  `automate-review-pull-requests`, `configure-codeowners-protection` remain
  tracked, deferred).
- The `independent-agent-review` milestone's agent-review implementation
  (content-error taxonomy reserves agent-review categories only).
- Automatic YAML reconciliation from approved Markdown (separate milestone
  `complete-universal-records`).
- Automatic promotion to `knowledge/` (human step).
- Real-time multi-user collaborative editing.
- Database provisioning / PostgreSQL migration.
- Rewording `roadmap.json`'s stale milestone `objective` text (flagged as a
  `/cg-strategy` follow-up).

## Completion Contract

### Outcome

The Shiny review app is live-capable (boots on Connect, browses/edits/persists
real data with correct front-matter immutability and audit binding); 6
calibration drafts are materialized with full front matter (3 real + 3 fixtures
with seeded known defects and a separate known-answer key); a reviewer and
approver complete a structured live-operator run that populates content-error,
defect, and friction logs; the interface is simplified based on measured
friction; and a two-layer review rubric with evidence-backed acceptance
criteria is finalized to gate promotion from `extraction/30_review/` to
`extraction/40_approved/` at scale.

### Verification Surface

| ID | Phase | Evidence Required | Command/Artifact | Required |
|----|-------|-------------------|------------------|----------|
| V1 | 1 | Production write transport sends JSON payloads; Connect entry point boots | `test-github-adapter.R` transport test; `app.R` loads on Connect | yes |
| V2 | 1 | Adapter wired into server; detail view loads real draft + review record; save_draft persists body as companion file + records `saved` event | `shinytest2` with injected adapter + `test-actions.R` save path | yes |
| V3 | 1 | C1 front-matter immutability meaningful (CRLF + tamper reject); body_sha256 flows through transition to event + record | `test-frontmatter.R` + `test-state-machine.R` audit-binding | yes |
| V4 | 1 | authorize() fail-closed for unknown actions; preview blocks XSS; module filter derived from index | `test-authorization.R` + XSS test + `test-index.R` filter | yes |
| V5 | 1 | Test isolation via tempfile(); DT declared; httr2 in Imports; renv.lock restores | `test-github-auth.R` + `R CMD check` / `renv::restore()` | yes |
| V6 | 2 | Content-error taxonomy (4 agent dimensions + human-review categories + stage + severity) + log/defect formats defined | `.cg-docs/calibration/measurement-framework.md` | yes |
| V7 | 2 | Two-layer rubric (Layer 1 structural template + Layer 2 per-section content) defined | `.cg-docs/calibration/review-rubric.md` (draft) | yes |
| V8 | 2 | Live-operator protocol (paths, time-on-task, errors, friction rating, free-text) + friction-log format defined | `.cg-docs/calibration/live-operator-protocol.md` | yes |
| V9 | 3 | 6 drafts materialized in extraction/20_drafts/ with full front matter, module_id-authoritative dirs; 3 fixtures carry seeded defects; known-answer key separate | schema validation + file existence + known-answer key check | yes |
| V10 | 4 | Live operator run completed (reviewer + approver, all paths); friction, content-error, defect logs populated; rubric layers + 30→40 gate exercised | `.cg-docs/calibration/live-run-2026-08-07.md` + populated logs | yes |
| V11 | 5 | Logs aggregated; catch rate measured vs known-answer key; friction-by-step analyzed | `.cg-docs/calibration/calibration-report.md` | yes |
| V12 | 5 | Interface simplified per friction decision rule (block/≥4-by-≥2-reviewer items resolved) | `app_ui.R` diff + re-test | yes |
| V13 | 5 | Rubric acceptance criteria finalized from run evidence; ready to gate promotion at scale | `.cg-docs/calibration/review-rubric.md` (finalized) | yes |

### Constraints

| ID | Phase | Constraint | Check |
|----|-------|------------|-------|
| C1 | 1 | YAML front matter preserved byte-exactly; structural alterations rejected | `test-frontmatter.R` meaningful immutability (CRLF + tamper + approved-path) |
| C2 | 1 | Writes only on the protected review branch; default branch remains canonical source | adapter target-branch assertions |
| C3 | 1 | `extraction/30_review/` and `extraction/40_approved/` human-owned; app writes only on authenticated human action | authorization/audit tests |
| C4 | 1 | Phase 1 scope is the live-capable subset only; remaining P0/P1 deferred to a tracked separate effort | scope review against the fix-triage boundary |
| C5 | 1 | Existing 224 passing tests are not broken by Phase 1 fixes | full `testthat` suite re-run |
| C6 | 1 | R-native SHA-256 parity with Python pipeline maintained | `test-hashing.R` |
| C7 | 1 | Connect auth is the only login; no second auth layer | app wiring test |
| C8 | 3 | Agents write only to `extraction/20_drafts/`; known-answer key and logs go to `.cg-docs/calibration/` | path audit |
| C9 | 3 | All 6 drafts carry full variable-spec front matter mirroring `knowledge/` structure | schema validation |
| C10 | 3 | Draft directories match front-matter `module_id`; dashboard filter derived from indexed modules | file-path + index test |
| C11 | 3 | Known-answer key kept separate from fixtures; used only for scoring | file separation check |
| C12 | 4 | Live run uses a disposable repo + Connect staging, never the production CVS repository | deployment config audit |
| C13 | 4 | App defects logged separately from content errors; do not dilute content error rates | log schema check |

### Boundaries

- **Allowed**: Phase 1 fixes (adapter wiring, production transport, entry
  point, front-matter immutability, audit binding, authorize fail-closed,
  preview XSS, module filter, leaked key removal, dependency fixes);
  instrumentation specs under `.cg-docs/calibration/`; 6 draft files under
  `extraction/20_drafts/`; known-answer key under `.cg-docs/calibration/`;
  live run against a disposable repo + Connect staging; interface
  simplification based on measured friction; rubric finalization.
- **Out of scope**: exhaustive `validate_review_record` + path-poisoning
  hardening; NAMESPACE/roxygen `@export` drift; `review-app/README.md`;
  remaining P0/P1 from the predecessor review (deferred to a tracked separate
  effort); PR automation, CODEOWNERS/branch-protection enforcement; the
  `independent-agent-review` milestone's agent-review implementation
  (categories reserved only); automatic YAML reconciliation; automatic
  promotion to `knowledge/`; real-time collaboration; database provisioning.

### Iteration Policy

1. Work front-to-back in phases; do not start a later phase with pending `yes`
   evidence from an earlier phase.
2. A deviation under policy `ask` pauses for approval; under `autonomous` is
   justified and recorded; under `strict` is a blocked-stop.
3. Phase 1 fixes must not break the existing 224 passing tests; re-run the
   full suite after each fix.
4. The live run uses a disposable repo + Connect staging; never the
   production CVS repository's protected review branch.
5. Any new public function added gets at least one `testthat` test.

### Blocked-Stop Conditions

- Required verification cannot be executed (no Connect instance or disposable
  repo available).
- Any required evidence fails after allowed recovery attempts.
- A protected boundary (write to `knowledge/`, the default branch) must be
  crossed.
- Front-matter immutability or optimistic-locking guarantees cannot be
  demonstrated after Phase 1.
- The disposable repo / Connect staging cannot be provisioned for the live
  run.
- Phase 1 scope creeps beyond the live-capable subset into deferred hardening
  without approval.
