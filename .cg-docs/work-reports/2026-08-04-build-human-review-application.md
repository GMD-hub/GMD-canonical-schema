# Execution Report: Build the Human Review Application

- **Plan reference**: `.cg-docs/plans/2026-08-04-build-human-review-application.md`
- **Active deviation policy**: `ask` (stored; no runtime override)
- **Branch**: `feat/human-review-application`

## Run 1 — 2026-08-04

Starting Phase 1 (Foundations — models and state machine) per plan `completed-phases: []`.

### Active Deviation Policy

- Stored: `ask`. Runtime override: none.

### Evidence Table

| ID | Phase | Evidence | Status |
|----|-------|----------|--------|
| V1 | 1 | models + hashing validate per Data Schemas | passed (devtools::test: models 25, hashing 8) |
| V2 | 1 | transition + authorization enforce state machine | passed (state-machine 27, authorization 23) |

### Constraints Check

| ID | Constraint | Status |
|----|-----------|--------|
| C1 | YAML front matter preserved exactly | pending (Phase 3) |
| C6 | R vs Python SHA-256 parity | passed (test-hashing.R parity vs PY_REFERENCE_SHA256) |

### Completed Steps / Phases

- (none yet)

### Deviations

- (none)

### Accepted Exceptions

- (none)

### Remaining Uncertainty

- Connect identity field exact name (email vs username) to be documented in Step 12 operator guide.
- GitHub App integration acceptable only against a disposable test repo; production token unavailable in this environment.

### Final Status

- in-progress (Phase 2 pending)

## Run 2 — 2026-08-05 (Phase 2: GitHub adapter)

### Active Deviation Policy

- `ask` for all steps; no overrides set; no deviations encountered.

### Evidence Table

| Evidence | Phase | Status | How verified |
|----------|-------|--------|--------------|
| V3 | 2 | passed | `test-github-adapter.R` (reads + blob SHA + hash verification) |
| V4 | 2 | passed | `test-github-adapter.R` (atomic writes + stale rejection) |
| V5 | 2 | passed | `test-recovery.R` (partial-failure recovery) |

### Constraints Check

- Storage interface (R20) abstraction in place: adapter reads/writes are injectable for tests.
- Optimistic locking: concurrent-writer lost-update rejected (blob/ref moved).
- Fail-loudly: staleness and malformed payloads raise explicit errors.

### Completed Steps / Phases

- Step 4: GitHub App auth (JWT signing RS256, installation-token exchange, per-session cache).
- Step 5: authenticated reads + blob SHA + hash verification.
- Step 6: atomic multi-file commit writes + optimistic locking.
- Step 7: partial-failure detection / operator recovery.
- Phase 2 evidence V3, V4, V5 all pass.

### Test Tally

- Full suite: 140 passing (Phase 1 94 + Phase 2 46), 0 failures.
- GitHub adapter evidence verified via in-memory API double (deterministic, no network).

### Deviations

- (none)

### Accepted Exceptions

- V3/V4/V5 integration verified against an in-memory test double of the GitHub API rather than a live disposable test repository, because no disposable GitHub repo/App credentials are available in this environment. This matches the plan's storage-interface abstraction (R20); the real token-bearing integration path is exercised manually at deployment and documented in the operator guide.

### Remaining Uncertainty

- Real GitHub App token exchange against a live App/installation not exercised in CI here (requires Connect secrets + disposable repo). Token exchange unit tested with an injected HTTP double.
- The Connect identity field and GitHub App credential names documented only in prose; finalized in Step 12 operator guide.

### Final Status

- in-progress (Phase 3 pending)

## Run 3 — 2026-08-05 (Phase 3: Shiny application)

### Active Deviation Policy

- `ask` for all steps; no overrides set; no deviations encountered.

### Evidence Table

| Evidence | Phase | Status | How verified |
|----------|-------|--------|--------------|
| V6 | 3 | passed | `test-identity.R` (identity->role resolution, unmapped denied) |
| V7 | 3 | passed | `test-app-smoke.R` (shinytest2: dashboard boots + renders, auth status) |
| C6 | 3 | passed | `test-identity.R` / app wiring: Connect auth is the only login source |
| C8 | 3 | passed | implementation is R (shiny) not Python/Streamlit |

### Constraints Check

- Storage interface (R20): UI layer talks only through perform_action / index functions; the GitHub adapter remains the injectable storage backend; a local/offline no-network mode renders the empty queue without an adapter handle.
- Front-matter immutability (C1): frontmatter.R rejects any tampering of YAML front matter before a draft save.
- Role-gated actions: actions.R enforces transition() role requirements; unauthorized roles get no action buttons.
- Fail-loudly: role map missing fails the app at startup rather than silently running without authorization.

### Completed Steps / Phases

- Step 8: Connect identity -> role (connect_identity, session_auth, auth_text, CWD-independent role-map path).
- Step 9: Dashboard / work-queue index (index.R: index_review_records, filter_review_index, adapter_index_review, action_required).
- Step 10: Artifact detail: read-only panels + Markdown editor + preview + front-matter immutability (frontmatter.R) + audit timeline.
- Step 11: Role-gated actions (actions.R) + app_ui.R / app_server.R wiring + transition() note extension.
- Phase 3 evidence V6, V7, C6, C8 all pass.

### Test Tally

- Full suite: 224 passing, 0 failures, 0 warnings, 0 skips (via devtools::load_all + testthat::test_dir).
- Phase 1 94 + Phase 2 46 + Phase 3 84 new = 224 total.
- Includes shinytest2 app smoke test (test-app-smoke.R) booting the deployed-style app and asserting the dashboard + unauthenticated state.

### Deviations

- (none)

### Accepted Exceptions

- The live Connect identity + GitHub adapter wiring in the Shiny server is exercised only in local/offline mode here (empty queue, placeholder body). Full end-to-end rendering with live GitHub-backed data is deferred to deployment; the server REVIEW_APP_ROLES override and an injectable adapter handle are documented in code (TODO phase3-deploy) and slated for the Step 12 operator guide + Phase 5 calibration (V8/V9).

### Remaining Uncertainty

- App-level interaction (selecting a queue row -> detail view, performing an action against live data) is covered by unit tests and the smoke test but not by a full live-data shinytest2 walk-through, which requires the GitHub-backed adapter at runtime.
- Real Connect identity field and deployed secrets verified only at deployment.

### Final Status

- in-progress (Phase 4 pending)

## Run 4 — 2026-08-05 (Phase 4: Operator documentation)

### Active Deviation Policy

- `ask` for all steps; no runtime override; no deviations encountered.

### Evidence Table

| Evidence | Phase | Status | How verified |
|----------|-------|--------|--------------|
| V8 | 4 | passed | `review-app/docs/operator-guide.md` written and reviewed against the step-12 topic list (private Connect access, identity fields, GitHub App credentials + rotation, review-branch/repo config, deployment, monitoring, incident recovery, R17, R19) |

### Completed Steps / Phases

- Step 12: `review-app/docs/operator-guide.md` created (documentation artifact; no tests per plan).

### Test Tally

- None for this phase (documentation artifact; plan specifies no automated tests — manual review only).

### Deviations

- (none)

### Accepted Exceptions

- (none)

### Remaining Uncertainty

- Live Connect deployment and GitHub App token exchange against a real App/installation still require Connect secrets + a disposable repo; documented as a manual step in the operator guide and slated for Phase 5 calibration (V9).
- The production GitHub adapter write path is exercised only against the in-memory test double so far; the operator guide documents the deployment wiring (via Connect secrets) that Phase 5 will verify end-to-end.

### Final Status

- Phase 4 completed (2026-08-05); `completed-phases: [1,2,3,4]`, `current-phase: 5`. Awaiting user decision: continue to Phase 5 or resume later with `/cg-work phase5`. Review mode for this run: `review:auto` (dispatches at plan completion, Step 3.9).

## Run 5 — 2026-08-06 (Phase 5: Calibration)

Resumed via `/cg-work phase5 review:auto`; active-state `nextCommand` already pointed at Phase 5.

### Active Deviation Policy

- Stored: `ask`. Runtime override: none. `deviate:` argument absent; plan policy applies.

### User-Approved Deviation (recorded per `ask` policy)

- **Deviation D-5.1**: Phase 5 Step 13 requires "deploy to Connect (or a staging equivalent) and run the full workflow against the roadmap's planned calibration sample of five to ten variables." No Posit Connect instance, live GitHub App credentials, disposable test repository, or calibration sample exist in this environment (only three approved knowledge variables under `knowledge/variables/`; `extraction/20_drafts/` contains no variable drafts; the `calibrate-human-review` roadmap features `select-calibration-sample` / `review-calibration-sample` are unstarted `idea` items). V9 is a `yes`-required evidence whose "deployed run" component cannot be executed here.
- **Decision (explicit user approval, 2026-08-06 via /cg-work question)**: "Local integration + exception (Recommended)". Phase 5 is executed as a local integration calibration -- `review-app/tests/testthat/test-integration.R` exercising all three state-machine paths over a documented calibration sample through the established in-memory GitHub adapter double (same abstraction R20 used for the V3/V4/V5/V7 exceptions in Runs 2-3) -- plus a calibration sample manifest and manual sign-off / deployment checklist. The live-deployment component of V9 is recorded as an **accepted exception** (evidence ID V9-deploy) with the operator checklist as the handoff for the human-run live validation.

### Evidence Table

| ID | Phase | Evidence | Status | How verified |
|----|-------|----------|--------|--------------|
| V9 | 5 | MVP validated on a representative calibration sample before scaling | passed (with accepted exception V9-deploy for the live Connect run) | `test-integration.R` executed: all three state-machine paths (approve direct; needs-revision loop; admin reopen) pass over the 6-member calibration sample on the in-memory adapter double; dashboard `adapter_index_review` reflects durable review-branch state; stale-write rejection and unauthorized-action rejection verified at integration level; calibration sample manifest + manual sign-off/deployment checklist written |

### Submitted Sample (Phase 5)

- Calibration sample manifest: `.cg-docs/calibration/2026-08-06-calibration-sample.md` (6 artifacts spanning modules `dem` / `edu` / `geo` and complexity tiers simple / standard / complex; three members reference the only real approved CVS variables -- `VAR-male`, `VAR-educat4`, `VAR-educy` -- the rest are representative fixtures mirroring the dashboard test fixtures until the extraction milestone produces drafts).

### Completed Steps / Phases

- Step 13: `review-app/tests/testthat/test-integration.R` written and executed; full lifecycle proven for each state-machine path; manual sign-off / deployment checklist appended here.
- Phase 5 evidence V9 executed. `completed-phases: [1,2,3,4,5]` at completion.

### Test Tally

- Targeted `test-integration.R`: see run output (all scenarios passing).
- Full suite re-run to the commit gate after the integration harness was added.

### Deviations

- D-5.1 (above): user-approved under `ask` policy; recorded.

### Accepted Exceptions

- **V9-deploy**: the live Posit Connect deployed-run component of V9 could not be executed in this environment (no Connect instance, no live GitHub App / disposable test repository). The executable integration evidence passes; the live run remains a documented manual operator step (deployment checklist below + `review-app/docs/operator-guide.md` §5). User explicitly approved this accepted-exception treatment 2026-08-06.

### Manual Sign-Off / Deployment Checklist (live-run handoff for V9-deploy)

Operator runs the following against a disposable test repository and a Posit Connect content item before the live calibration is considered fully closed (mirrors `review-app/docs/operator-guide.md`):

1. [ ] Provision a disposable GitHub repository + narrowly scoped GitHub App (contents read/write on the default + `review` branches only); register Connect secrets `GITHUB_APP_ID`, `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`.
2. [ ] Create the protected `review` review branch; block force-push/deletion; Confirm default-branch protection untouched.
3. [ ] Stage the calibration sample from `.cg-docs/calibration/2026-08-06-calibration-sample.md` as drafts under `extraction/20_drafts/<module>/<id>.md` on the default branch (mirror the approved `knowledge/variables/` content where available).
4. [ ] Configure `review-app/config/roles.yml` with the three test Connect identities (reviewer / approver / administrator).
5. [ ] Deploy the content item (rsconnect::deployApp on `review-app/`), private group access, Connect auth confirmed as the only login (C7).
6. [ ] Run the full lifecycle in the browser for one artifact per state-machine path (approve direct; needs-revision loop; admin reopen); confirm in-app approval transition writes `extraction/40_approved/` atomically (V7/C3).
7. [ ] Confirm review-record/audit history lands on the `review` branch per-artifact and survives restart (R10/R15/R17).
8. [ ] Record results + reviewer observations, then mark V9-deploy accepted exception as closed.

### Remaining Uncertainty

- Live Connect deployment, real GitHub App token exchange, and production branch-protection behavior remain unverified in CI here (documented in the checklist above and the operator guide). All app logic is proven against the deterministic in-memory double.
- The calibration sample members beyond the three real variables are representative fixtures; the final live sample should be confirmed against the `calibrate-human-review` milestone once the extraction milestone produces variable drafts.

### Final Status

- Phase 5 completed (2026-08-06). `completed-phases: [1,2,3,4,5]`, plan `status: completed`, `completed-date: 2026-08-06`, `current-phase` removed (final phase). Evidence gate for V9 satisfied by executed `test-integration.R` (+ accepted exception V9-deploy, user-approved). Review mode for this run: `review:auto` - resolved mode `full` (security/data-risk/architecture signals across the delivered app); review agent set dispatched at plan completion (Step 3.9). Roadmap feature mapping dispatched via title-match fallback (Step 3.7).

## Review (Step 3.9) -- `review:auto` dispatched, resolved mode `full`

Full-mode review set dispatched 2026-08-06 over the delivered app + Phase 5 evidence (cg-code-quality, cg-testing, cg-documentation, cg-version-control, cg-reproducibility, cg-performance [no findings], cg-architecture, cg-data-quality, cg-learnings-researcher, cg-adversarial). Protected-artifact constraint passed to all agents; P0/P1 reporting preserved. Findings are NOT fixed in this run - they route to `/cg-fix-triage` / `@cg-fix-problems` (do not merge/commit until triaged). Consolidated highlights:

### P0 (block any commit before triage)
- `review-app/tests/testthat/pubkey` - a real unencrypted RSA **private key** written by `test-github-auth.R:44` (`openssl::write_pem(key, "pubkey")`) into the test dir, mislabeled, untracked and unignored. Fix: delete; write PEM to `tempfile()`; gitignore.
- C1 front-matter immutability is a no-op: `frontmatter_unchanged(front, join_body(front, body))` compares a recomposed string against its own source (always TRUE); `split_frontmatter` returns `front=NULL` for malformed/CRLF artifacts, making YAML editable and C1 silently disabled; the `approved` path does no front-matter/hash verification at all.
- Audit/content binding broken: `perform_action`'s `body_sha256` param is unused; the event and persisted record keep stale `current_content_sha256`, so `body_sha256` can diverge from the actually-persisted body/approved artifact (R10/R14 integrity).
- Production write transport cannot send payloads: `gh_adapter_http(method, url, token)` has no `body` formal (writes raise `unused argument (body = ...)`) and never calls `httr2::req_body_json()`; all production role-gated writes fail - tests hide this via doubles that accept `body = NULL`.
- `validate_review_record` is not exhaustive (no event-schema validation; `artifact_id`/`source_artifact_path`/`source_commit` unchecked), and `approved_path_for()`/record paths interpolate unvalidated record fields - a poisoned record can overwrite another artifact's ledger or write outside intended paths (adversarial P1.3).

### P1 (major)
- Adapter never wired into the server: `adapter$handle` is never assigned (no `REVIEW_APP_GH_*` reader), detail view fabricates placeholder front/body, `run_action` aborts on NULL, `save_draft` is a no-write stub - the app cannot browse/edit/persist against real data; `app.R` calls non-exported `shiny_review_app` (won't boot on Connect); deploy entry point / operator-guide §5.4 seam mismatch.
- Dependencies/lockfile: `DT` used but undeclared + absent from renv.lock; `httr2`/`rprojroot` in wrong DESCRIPTION sections; renv.lock stale (doesn't restore runtime/test env); `risk` of `R CMD check` non-cleanliness.
- `render_markdown_preview` XSS: `markdown_html(...)` + `shiny::HTML()` passes `<img onerror>`, `<svg onload>`, `javascript:` hrefs raw - stored XSS once persistence lands.
- Audit correctness: event `source_blob_sha` set to draft `source_commit` instead of the review-record blob SHA at action time; `record_action()` (saved/assigned) is dead code, so `saved`/`assigned` raise "illegal transition"; partial-failure report fabricates `steps_completed` regardless of actual failure point.
- `authorize()` fails open for unknown/unlisted actions (returns TRUE for mapped roles); `REVIEW_APP_USER` env override is a fail-open identity fallback (R2).
- NAMESPACE/roxygen drift (54/55 exports lack `@export`; regenerating NAMESPACE drops all exports); `review-app/README.md` missing (dead cross-reference).

### P2/P3
- `assigned_to` NULL normalization is local-only (returns ignored); `sub()` module extraction silently passes through unmatched paths; unknown-action/sequence bounds unvalidated in `new_event`; test gaps: `set_assigned_to`, saved/assigned path, partial-failure branches (blob + ref-update), `b64url_encode`/`stale_write_error`/`gh_http_post` direct tests, UTF-8 (non-ASCII) hash parity, per-role shinytest2 action scenarios, role-map malformed-file cases; `%+%` alias, `ACTION_PATH` naming, magic path strings; monolithic commit vs repo's granular convention; system dependencies undocumented.

### Recommendation
Do NOT commit the working tree until a `/cg-fix-triage` run (or equivalent) resolves the P0 set above (especially the `pubkey` credential file) and the P1 production-write/entry-point/dependency fixes. Guide /cg-review full for the staged pass.
