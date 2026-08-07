# Execution Report: Calibrate Human Review

- **Plan reference**: `.cg-docs/plans/2026-08-07-calibrate-human-review.md`
- **Active deviation policy**: `ask` (stored; no runtime override)
- **Branch**: `feat/calibrate-human-review`
- **Review mode**: `review:auto`

## Run 1 — 2026-08-07

Starting Phase 1 (Live-capable subset) per plan `completed-phases: []`.
Command args: `ALL phases review:auto` with explicit plan path.

### Active Deviation Policy

- Stored: `ask`. Runtime override: none.

### Evidence Table

| ID | Phase | Evidence | Status |
|----|-------|----------|--------|
| V1 | 1 | Production write transport sends JSON payloads; Connect entry point boots | passed (test-github-adapter.R transport tests + NAMESPACE export check) |
| V2 | 1 | Adapter wired; detail view loads real data; save_draft persists body + `saved` event | passed (testServer wired adapter test + test-actions.R saved/assigned) |
| V3 | 1 | C1 front-matter immutability meaningful; body_sha256 flows through transition | passed (test-frontmatter.R CRLF+tamper+approved-path; test-state-machine.R audit-binding) |
| V4 | 1 | authorize() fail-closed; preview blocks XSS; module filter derived from index | passed (test-authorization.R + XSS vectors + test-index.R filter) |
| V4 | 1 | authorize() fail-closed; preview blocks XSS; module filter derived from index | pending |
| V5 | 1 | Test isolation via tempfile(); DT declared; httr2 in Imports; renv.lock restores | passed (test-github-auth.R tempfile + DESCRIPTION + renv::restore) |
| V6 | 2 | Content-error taxonomy + log/defect formats defined | passed (measurement-framework.md, spec review) |
| V7 | 2 | Two-layer rubric defined | passed (review-rubric.md draft, spec review) |
| V8 | 2 | Live-operator protocol + friction-log format defined | passed (live-operator-protocol.md, spec review) |
| V9 | 3 | 6 drafts materialized with full front matter; fixtures carry seeded defects; known-answer key separate | passed (schema validation + file checks + integration test) |
| V10 | 4 | Live operator run completed; logs populated; rubric + 30→40 gate exercised | accepted-exception (deferred to Connect-provisioned computer; see Accepted Exceptions) |
| V6 | 2 | Content-error taxonomy + log/defect formats defined | pending |
| V7 | 2 | Two-layer rubric defined | pending |
| V8 | 2 | Live-operator protocol + friction-log format defined | pending |
| V9 | 3 | 6 drafts materialized with full front matter; fixtures carry seeded defects; known-answer key separate | pending |
| V10 | 4 | Live operator run completed; logs populated; rubric + 30→40 gate exercised | pending |
| V11 | 5 | Logs aggregated; catch rate measured; friction-by-step analyzed | pending |
| V12 | 5 | Interface simplified per friction decision rule | pending |
| V13 | 5 | Rubric acceptance criteria finalized from run evidence | pending |

### Constraints Check

| ID | Constraint | Status |
|----|-----------|--------|
| C1 | YAML front matter preserved byte-exactly; structural alterations rejected | pending (Phase 1) |
| C2 | Writes only on protected review branch | pending |
| C3 | 30/40 dirs human-owned; app writes only on authenticated action | pending |
| C4 | Phase 1 scope is live-capable subset only | in scope |
| C5 | Existing 224 tests not broken by Phase 1 | pending |
| C6 | R-native SHA-256 parity with Python maintained | pending |
| C7 | Connect auth is the only login | pending |
| C8 | Agents write only to 20_drafts/; key/logs to .cg-docs/calibration/ | pending |
| C9 | All 6 drafts carry full variable-spec front matter | pending |
| C10 | Draft dirs match module_id; filter derived from indexed modules | pending |
| C11 | Known-answer key kept separate from fixtures | pending |
| C12 | Live run uses disposable repo + Connect staging | pending |
| C13 | App defects logged separately from content errors | pending |

### Completed Steps / Phases

- Phase 1 Step 1 (Fix production write transport and Connect entry point) — done 2026-08-07.
  - `gh_adapter_http` accepts `body = NULL` and sends via `httr2::req_body_json`; `app.R` resolves exported `shiny_review_app`; `httr2` moved to DESCRIPTION Imports.
  - Red-phase: new `test-github-adapter.R` tests failed with "unused argument (body = ...)" before the fix.
  - Tests: `test-github-adapter.R` passing after fix.
  - Also fixed pre-existing C6 drift: added `.gitattributes` `-text` for the hash fixture so git `core.autocrlf` no longer converts to CRLF at checkout (committed LF blob = `PY_REFERENCE_SHA256`).
- Phase 1 Step 2 (Wire adapter into server and detail view) — done 2026-08-07.
  - `review_app_adapter()` factory reads Connect secrets / injected option / offline flag; `app_server.R` builds `adapter$handle` from it (fails loudly when unconfigured).
  - Detail view loads real draft + review record + companion body via adapter; stores blob_sha, branch_head_sha, body_sha256 for optimistic locking.
  - `save_draft` persists edited body as companion file `extraction/30_review/<id>.body.md` + records `saved` event via `perform_action`; `perform_action` routes `saved`/`assigned` through `record_action` (P1.2, P1.1).
  - `saved = "reviewer"` added to `action_requires_role` (P1.1); existing `test-authorization.R` saved-model assertion updated (was fail-open).
  - Tests: `test-actions.R` saved/assigned paths, `test-app-smoke.R` in-process testServer wiring (queue + detail), `test-github-adapter.R` adapter-factory tests.
- Phase 1 Step 3 (Fix front-matter immutability and audit binding) — done 2026-08-07.
  - `split_frontmatter` normalizes CRLF→LF (R6); `frontmatter_unchanged` compares the front extracted from the user's edited artifact against the loaded reference, returning FALSE when front matter is absent; approved-path structural gate added (P2.5).
  - `transition()`/`record_action()` accept `body_sha256`/`blob_sha` (defaults preserve C5); event carries the passed body hash; record `current_content_sha256` updated on every action; event `source_blob_sha` = passed review-record blob SHA (R7/P2.1/P2.3).
  - Tests: `test-frontmatter.R` CRLF/tamper/approved-path; `test-state-machine.R` body_sha256/blob_sha flow + backward-compat defaults.
- Phase 1 Step 4 (Fix security, preview, and dashboard filter) — done 2026-08-07.
  - `authorize()` fails closed for unknown/unlisted/NULL actions (R8); `saved`/`assigned` already in the action-role map (P1.1 ordering respected).
  - Preview: `render_markdown_preview` now uses `tagfilter` AND a post-render `sanitize_preview_html()` pass (xml2) that removes executable elements and `on*`/`javascript:` attributes (R9/P2.2). `xml2` added to DESCRIPTION Imports.
  - Dashboard module filter is data-driven via `module_filter_choices()` + `uiOutput("filter_module_ui")` (R10).
  - Tests: `test-authorization.R` fail-closed; `test-frontmatter.R` XSS vectors; `test-index.R` module-filter derivation.
- Phase 1 Step 5 (Remove leaked key and fix dependencies) — done 2026-08-07.
  - `test-github-auth.R` JWT-verify test writes the temporary public key via `tempfile(fileext = ".pem")` + `on.exit(unlink(...))` (P2.4/R11). No stray `pubkey` file exists in the test tree.
  - `DT` added to DESCRIPTION Imports; `httr2` already moved to Imports (Step 1); `xml2` added in Step 4.
  - renv bootstrapped + `renv::restore()` succeeded (35 packages); `DT`/`httr2`/`xml2` installed; `renv::snapshot()` updated `renv.lock` (50 packages; R recorded 4.5.2).
  - Full testthat suite green after all Phase 1 steps.
- Phase 2 Steps 6–8 (Instrumentation specification) — done 2026-08-07.
  - `.cg-docs/calibration/measurement-framework.md` — R13, R14: content-error taxonomy (4 agent-review + human-review categories, stage + severity), content-error record schema, separate app-defect log schema (C13).
  - `.cg-docs/calibration/review-rubric.md` — R15: Layer 1 (automated structural: YAML schema, front-matter unchanged, 7 required sections, non-stub) + Layer 2 (human per-section pass/revise/fail) + promotion gate 30→40 + section template.
  - `.cg-docs/calibration/live-operator-protocol.md` — R16: roles, 11-step per-artifact flow, friction-log schema, decision rule, known-defect detection.
  - Spec review only (no automated test per plan).
- Phase 3 Step 9 (Materialize the 6 calibration drafts) — done 2026-08-07.
  - P1.3 correction: calibration manifest (`2026-08-06-calibration-sample.md`) and `test-integration.R` updated to `dem/` for educat4/educy/educat7 (module_id authoritative = MOD-DEM; `edu/` empty). Integration test module-count assertions updated (dem=5, geo=1).
  - 3 real drafts copied from `knowledge/variables/dem/` → `extraction/20_drafts/dem/` (VAR-male, VAR-educat4, VAR-educy) with full front matter; Pydantic schema validation passes for all 3 (identical to knowledge originals).
  - 3 fixtures authored with full front matter + all 7 required sections: VAR-educat7 (dem/, MOD-DEM; seeded RULE-EDU-999 + stub escalation triggers), VAR-urban (geo/; seeded module_id MOD-DEM mismatch + derived_from VAR-rurality break), VAR-marital (dem/; seeded stub Construction notes `TODO.` + invalid `value: 5` label).
  - Known-answer key written separately at `.cg-docs/calibration/known-answer-key.md` (6 seeded defects, categories/severities, scoring reference).
  - Materialization error logged in content-error-log.yaml (ERR-EDU-MOD-001..003, consistency-derivation, major, resolved).
  - Full testthat suite green after the path corrections.
- Phase 4 Steps 10–11 (Provision + Live operator run) — **blocked** 2026-08-07 (deferred to another computer).
  - Blocked-stop condition: this environment has no Posit Connect (no `rsconnect` package, no `CONNECT_SERVER`/`CONNECT_API_KEY`), no disposable GitHub repo/App provisioning path, and no live human reviewers. Per plan Blocked-Stop Conditions: "The disposable repo / Connect staging cannot be provisioned for the live run."
  - Completed: `review-app/docs/operator-guide.md` §10 calibration deployment checklist written (exact Connect secret names, 7-step sequence); Layer-1 structural checks executed over all 6 drafts (see below).
  - Layer-1 executed results (in-memory double, no network): all 6 drafts parse YAML, have front matter, and all 7 required sections present. Stub detection flags: `VAR-educat7` `## Escalation triggers` (stub) and `VAR-marital` `## Construction notes` (`TODO.`). Schema validation flags `VAR-educat7` `RULE-EDU-999` (seeded defect).
  - Not executed (requires Connect/disposable repo on another computer): Step 10 provisioning+deploy, Step 11 live reviewer+approver run, `live-run-2026-08-07.md`, populated friction/defect logs.

### Deviations

- **D1 (recorded)**: Plan P2.2 prescribed only the commonmark `tagfilter` extension to block XSS. In this commonmark build, `tagfilter` escapes a small tag list only and leaves `<img onerror>`, `<svg onload>`, and `javascript:` hrefs intact — failing V4's acceptance criteria (XSS vectors must be stripped). Added `sanitize_preview_html()` (xml2 post-render pass) in addition to `tagfilter`, preserving benign markdown (tables, em) while meeting the plan's stated XSS requirement. Rationale: the plan's outcome (V4 "preview blocks XSS") requires the sanitizer; recorded as a deviation with impact (extra dependency `xml2`, now in Imports).

### Accepted Exceptions

- **V10 (accepted, user-approved 2026-08-07)**: The live operator run on a
  deployed Posit Connect app cannot be executed from this environment (no
  Connect instance/repo/App/reviewers). Per the user's decision, V10 is
  deferred to another computer via `/cg-work phase4`. The in-memory Layer-1
  structural results are recorded above as design evidence only and do NOT
  satisfy V10. Rationale recorded: provisioning requires external
  resources unavailable in this session.

- **Phase 4 Steps 10–11 (deferred)**: provisioning/deploy + live operator run
  are handed off to another computer; resume command below.

### Remaining Uncertainty

- Posit Connect instance / disposable GitHub repo availability for Phase 4 (potentially blocked-stop).
- R environment with renv bootstrap for Phase 1 Step 5 `renv::snapshot()`/`restore()`.
- Two live human reviewers for the Phase 4 run.

### Final Status

- blocked (Phase 4 deferred for Connect provisioning on another computer).
- Resume: `/cg-work phase4` with the run script/report present;
  `.cg-docs/active-state/current.json` points to this report.
- Phases 1–3 complete and committed; Phase 5 depends on Phase 4 live-run logs.
