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

## Run 2 — 2026-08-07 (resume)

Resumed via `/cg-work` with args `ALL phases review:auto`, explicit plan path
`.cg-docs/plans/2026-08-07-calibrate-human-review.md`, at Phase 4 (Steps 10–11),
intending to continue to Phase 5.

### Active Deviation Policy

- Stored: `ask`. Runtime override: none (no `deviate:` token in args).

### Preflight

- Artifact validation preflight passed:
  `cg-render-artifact --validate-only .cg-docs/plans/2026-08-07-calibrate-human-review.md` → exit 0 ("Validated").
- Artifact-schema-version embed: 1 (plan frontmatter). No view/body reads done.

### Phase 4 Step 10 — Provision and deploy (attempted, blocked)

Checklist review against `review-app/docs/operator-guide.md` §10:

| Sub-step | Requirement | Status in this environment |
|----------|-------------|----------------------------|
| 1 | Disposable GitHub repo + narrowly scoped GitHub App + Connect secrets | **Blocked.** `gh` token scopes are `gist, read:org, repo, workflow` — no org-owner/admin scope to create a GitHub App; GitHub App creation requires org-owner permission or an interactive app-manifest redirect. No Posit Connect instance: `rsconnect` package not installed; no `CONNECT_SERVER`/`CONNECT_API_KEY` in env or `.Renviron`; no Connect server URL anywhere in the workspace. |
| 2 | Protected `review` branch (block force-push/deletion; default untouched) | Blocked (requires the disposable repo above). |
| 3 | Stage 6 drafts on default branch `extraction/20_drafts/<module>/<id>.md` | Sources exist locally (6 files verified), but staging "on the default branch" of the disposable repo is blocked by sub-step 1. |
| 4 | `review-app/config/roles.yml` with 2 test Connect identities | **Ready** — already contains `reviewer@example.org` → reviewer and `approver@example.org` → approver (plus `admin@example.org`). No change needed. |
| 5 | `rsconnect::deployApp(review-app/)`, private group, Connect auth only | **Blocked.** No `rsconnect` package, no Connect server/API key. |
| 6 | Verify app boots + queue shows 6 artifacts, modules dem + geo | Blocked (no deployment exists). |
| 7 | Run live-operator protocol (Step 11) | Blocked (no deployed app; no human reviewers). |

**Blocked-stop condition (plan):** "The disposable repo / Connect staging cannot
be provisioned for the live run." No POSIT Connect, no GitHub App creation path,
no human reviewers. This is the same blocked boundary as Run 1; it has not been
resolved by this environment.

### Phase 4 Step 11 — Execute the live operator run (blocked)

Cannot execute: requires the deployed private app from Step 10 and two live
human operators (reviewer + approver). No live-run data exists, so neither the
run log (`live-run-2026-08-07.md`) nor the populated `defect-log.yaml` /
`friction-log.yaml` / live-run `content-error-log.yaml` entries may be
fabricated. V10 remains an accepted exception pending a genuine Connect run.

### Phase 5 Steps 12–14 (not started)

Per Iteration Policy rule 1 ("do not start a later phase with pending `yes`
evidence from an earlier phase"), Phase 5 aggregation (V11), interface
simplification (V12), and rubric finalization (V13) all depend on Phase 4
live-run logs. They cannot be completed against fabricated or missing logs.

### Roadmap

No roadmap feature has `plan` set to this plan path; the
`calibrate-human-review` milestone features (`review-calibration-sample`,
`measure-review-errors`, `simplify-review-interface`, `finalize-review-rubric`)
have `plan: null` with status `idea`. Per Step 1.5, no roadmap active-status
dispatch applies (no matching planned feature). No roadmap write performed
(`roadmap.json` never modified directly).

### Remaining Uncertainty

- Identical to Run 1: Posit Connect instance + disposable GitHub App/repo must
  be provisioned on a Connect-capable computer; two live reviewers required.

### Accepted Exceptions (carried forward)

- **V10 (accepted, user-approved 2026-08-07)**: live operator run deferred to a
  Connect-provisioned computer; remains an accepted exception until executed.

### Final Status

- blocked (Phase 4 Steps 10–11 cannot execute without Posit Connect + GitHub App
  + human reviewers). Phases 1–3 remain complete. V10 stays accepted-exception.
- Resume command unchanged: `/cg-work phase4` on a Connect-provisioned machine.

## Run 3 — 2026-08-10 (resume)

Resumed via `/cg-work` with args `phase4-5 review:auto`, plan path
`.cg-docs/plans/2026-08-07-calibrate-human-review.md` (phases 4 and 5 in scope).
User note: the review-app has been restructured to the **{golem}** layout
(`R/mod_*.R`, `R/app_config.R`, `inst/`, `dev/`, `app.R` → `run_app()`); the
plan's Phase 4/5 file references are treated as pre-golem and adapted.

### Active Deviation Policy

- Stored: `ask`. Runtime override: none (no `deviate:` token in args).

### Preflight

- Phase argument `phase4-5` parsed as phases 4–5 (plan has 5 `## Phase`
  headers). `completed-phases: [1,2,3]`, so Phase 4 is the next incomplete
  phase; Phase 5 is in scope but depends on Phase 4 evidence (Iteration Policy
  rule 1).
- Artifact validation preflight passed:
  `cg-render-artifact --validate-only .cg-docs/plans/2026-08-07-calibrate-human-review.md`
  → exit 0 ("Validated"). `artifact-schema-version: 1`.
- No roadmap feature has `plan` set to this plan path (`calibrate-human-review`
  milestone features remain `plan: null`, status `idea`); Step 1.5 roadmap
  active-status dispatch does not apply. No roadmap write performed.
- Brain (Step 1.3): `cg-index query` → confirmed calibration plan + the
  "untested code passes review" gotcha (run real checks, not static inspection).

### Environment re-check (post-Run-2 blockers)

- Posit Connect: **partially resolved** — `CONNECT_SERVER`/`CONNECT_API_KEY`
  are set in `~/.Renviron`; Connect API returns 200 for the deployed content
  item (`review-app`, guid `88dcd5b3-91b0-47fd-97b6-b1e420c683f2`), last
  deployed 2026-08-10T17:23:01Z. `rsconnect` R package and `posit publish` CLI
  are NOT installed.
- **GitHub App backend: still not provisioned.** `GITHUB_APP_ID`,
  `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`,
  `REVIEW_APP_GH_OWNER/REPO/DEFAULT_BRANCH/REVIEW_BRANCH` are all **unset**
  locally; `gh` token scopes (`gist, read:org, repo, workflow`) still cannot
  create a GitHub App. `review_app_adapter()` in production mode will fail
  loudly.
- **Human reviewers: none available** (no real Connect identities mapped in
  `config/roles.yml`; only `reviewer@example.org` / `approver@example.org`
  placeholders).
- Deployed bundle audit: `review-app/.posit/publish/deployments/deployment-U42S.toml`
  records a deployed manifest of 18 files that **omits** the golem files
  (`R/mod_dashboard.R`, `R/mod_detail.R`, `R/app_config.R`, `inst/`, `config/`,
  `DESCRIPTION`, `NAMESPACE`). A bundle without `DESCRIPTION`/`NAMESPACE`/
  modules cannot boot — `library(reviewapp)` and `app_ui()` would fail at load.
  The publish **configuration** (`review-app/.posit/publish/review-app-9KP9.toml`)
  also omits `/DESCRIPTION`, `/NAMESPACE`, `/inst`, `/config` from its `files`.

### Deviations

- **DEV-3 (golem adaptation — user-sanctioned)**: The app is now golem-packaged;
  Phase 4 Step 10's deployment file set and "app boots" verification are
  adapted to the golem layout. The user's explicit note ("now we are using the
  {golem} structure") is the approval record for this adaptation.
- **DEV-4 (boot verification)**: "Verify the app boots on Connect" cannot be
  executed against the currently deployed content (broken/stale bundle; no
  publish toolchain installed). The local `testthat` suite against the golem
  source is used as the executable boot verification instead. Recorded; the
  deployed-bundle staleness is logged as an app defect (see defect-log entry
  below).

### Phase 4 Step 10 status (this run)

- Executable portion begun: golem deploy-bundle configuration fix + local boot
  verification (see below). Live deployment/re-run of the content item is NOT
  executed (requires publish toolchain install + user authorization to push to
  `datanalytics-int.worldbank.org`).
- Still blocked: GitHub App secrets + disposable GitHub repo provisioning and
  the protected `review` branch (sub-steps 1–3 of Step 10).

### Phase 4 Step 11 + Phase 5 status

- Still blocked: the live operator run requires a bootable deployed app, a
  working GitHub App backend, and two human reviewers walking the protocol.
  Live-run logs (content-error/defect/friction) will not be fabricated. V10
  remains an accepted exception pending a genuine run. Phase 5 Steps 12–14 are
  not started (Iteration Policy rule 1: no later phase with pending `yes`
  evidence from Phase 4).

### Executed this run (2026-08-10)

1. **Local boot / regression baseline (Phase 1→4 live-capable re-check).**
   Ran the full `reviewapp` `testthat` suite against the golem source.
   `renv::restore()` first (reinstalled `DT`, `crosstalk`, `lazyeval`; aligned
   `httr2`, `rlang`, `xml2`, `tinytex`, `xfun` to the lockfile). Result:
   **372 passed, 0 failed, 0 skipped**.
   - One golem-restructure regression was found and fixed:
     `review-app/tests/testthat/test-app-smoke.R` `dashboard module loads a
     queue from an injected adapter` called `selected_artifact()` as a bare
     local and drove un-namespaced inputs. In the golem module layout those
     live in the module's return list and a namespaced input domain. Fixed with
     a wrapper that captures `mod_dashboard_server()`'s return list and drives
     `dashboard-refresh_queue` / `dashboard-queue_table_rows_selected`
     (`test-app-smoke.R:92-118`). Red-phase confirmed before the fix: the test
     failed with `could not find function "selected_artifact"`.
   - `renv` reports out-of-sync only because the lockfile was generated under
     R 4.5.2 while this machine runs R 4.6.1; all package versions now match
     the lockfile. The lockfile was **not** rewritten (no unauthorized churn).
2. **Phase 4 Step 10 — deploy-bundle fix for the golem structure.**
   `review-app/.posit/publish/review-app-9KP9.toml` `files` now includes
   `/DESCRIPTION`, `/NAMESPACE`, `/R`, `/inst`, `/config`, `/app.R`,
   `/renv.lock`, and the `.posit/publish` self-references. TOML validated
   (`tomllib`); every referenced path exists. This is the concrete fix for
   DEF-001 (the deployed bundle previously omitted the package plumbing and
   could not boot).
3. **Phase 4 Step 10/11 — app-defect logging.**
   Created `.cg-docs/calibration/defect-log.yaml` with **DEF-001** (deployment,
   P0): the then-deployed Connect bundle `88dcd5b3` (bundle 87929 @17:23Z)
   omitted the golem package files, so the deployed app could not boot; the
   publish config was fixed. **After this run**, re-deploys executed — bundle
   88084 (2026-08-10T21:23Z), superseded by bundle 88147 (2026-08-10T22:52:40Z) —
   with the full golem file set, and DEF-001 was reconciled to `fixed`
   (boot-on-Connect smoke check still outstanding). This
   is the only defect-log entry so far; Step 11 live-run observations will
   append.
4. **Phase 4 Step 11 + Phase 5 — not executed** (blocked; see status above).
   No live-run/friction/content-error fabrication.

### Run 3 Evidence Table (delta)

| ID | Phase | Evidence | Status |
|----|-------|----------|--------|
| V1 | 1 | write transport + entry point; app boots | passed — local suite green (`app.R`/`run_app()` loads in tests); Connect boot **not yet verified** (bundle 88147 re-deployed with golem files; smoke check outstanding) |
| V2 | 1 | adapter wired; detail loads real data; save_draft persists | passed (suite green incl. wired-adapter smoke; production adapter unprovisioned) |
| V4 | 1 | authorize fail-closed; XSS; module filter | passed (suite green) |
| V10 | 4 | live operator run + populated logs + 30→40 gate | accepted-exception (still deferred; requires Connect+GitHub App+human reviewers) |
| V11-V13 | 5 | aggregation / simplification / rubric finalization | pending — not started (Phase 4 blocked) |

### Run 3 Constraints Check (delta)

- C5 (existing tests not broken): **passed** — 371 tests green after the golem
  smoke-test fix.
- C12 (live run uses disposable repo + Connect staging): **not executed** —
  connection block remains.
- Others unchanged from Runs 1–2 (C1–C4, C6–C11, C13 partially evidenced by
  suite + defect-log separation).

### Remaining Uncertainty

- Whether the re-deployed content (bundle 88147) actually boots on the Connect
  server: RECOMMEND opening the content URL / running the §5.5 smoke check and
  confirming `library(reviewapp)` install and the live queue render.
- GitHub App provisioning (org-owner scope or a pre-created App) for the write
  path; staging the 6 drafts on the disposable repo's default branch; two
  human reviewers with real Connect identities.

### Final Status

- **blocked** (Phase 4 Step 11 live operator run cannot execute: no GitHub App
  backend, no human reviewers; Step 10 deploy executed as bundle 88147 with the
  golem file set, boot smoke still outstanding). Phases 1–3 remain complete;
  Phase 4 Step 10's executable subset (local boot baseline, golem deploy-bundle
  fix, DEF-001 fixed via re-deploy) is done and uncommitted; V10 stays
  accepted-exception.
- Active-state, defect-log, and this report updated:
  `.cg-docs/active-state/current.json`, `.cg-docs/calibration/defect-log.yaml`.
- Resume: `/cg-work phase4-5` once the GitHub App + reviewers are provisioned.

