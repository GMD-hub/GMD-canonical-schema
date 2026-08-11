# GMD Human Review Application — Posit Connect Operator Guide

_Step 12 of plan `2026-08-04-build-human-review-application.md` — Phase 4
(Operator documentation)._

This guide is the operator-facing reference for deploying and operating the
private, Git-backed **Shiny for R** review application on Posit Connect. It
covers access/group configuration, the Connect identity fields the app relies
on, GitHub App credential provisioning and rotation, review-branch and
repository configuration, deployment, monitoring, and the incident-recovery
procedure for partial writes.

It explicitly documents two design decisions from the plan:

- **R17 — Connect persistent storage is disposable cache only.** Connect's
  persistent storage must never be treated as the authoritative audit ledger.
  The authoritative ledger is the per-artifact review record
  (`extraction/30_review/*.review.yml`) and the approved artifacts
  (`extraction/40_approved/*`) committed to the protected review branch.
- **R19 — PR automation and CODEOWNERS are deferred.** Pull-request automation
  and CODEOWNERS/branch-protection enforcement are **out of scope** for this
  iteration. They remain tracked, deferred roadmap features
  (`automate-review-pull-requests`, `configure-codeowners-protection`). Do not
  treat their absence as a defect.

---

## 0. Architecture in one paragraph

The app (`review-app/`) is a self-contained R package served by Shiny on Posit
Connect. It authenticates users with **Connect authentication only** (R2) —
there is no second login layer. The authenticated identity is resolved against
a repository-managed role map (`review-app/config/roles.yml`) into one of
`reviewer` / `approver` / `administrator` (R3). All data operations go through a
**GitHub App identity** (R12): the app reads source drafts from the default
branch as canonical read-only context and writes review records and approved
artifacts only to a dedicated **protected review branch** (R13). Writes are
atomic multi-file commits with optimistic locking (R11, R14, R18).

---

## 1. Private Connect access and group configuration (R1, R2)

1. Create a Content view in Posit Connect (e.g. `CVS Review`) that only the
   intended GPID review team can see. The app is private: only authenticated
   Connect users in the allowed group(s) may access it.
2. Restrict access at the **content-access level** to the reviewer/approver/
   administrator group(s). Connect authentication is the single identity source
   (R2): do not add any second login layer in the app.
3. Version/notes:
   - Confirm the app's runtime R version against `review-app/renv.lock`
     (`renv::restore()` reproduces the environment).
   - Keep the `review-app/` content item separate from the Python extraction
     pipeline content on Connect — it is an independent deployment unit.

### 1.1 Group membership vs. role map

- Connect group membership controls **who can reach the app**.
- The repository role map (`config/roles.yml`) controls **what each identity
  may do inside the app**.
- These are two different layers. An identity can be in the Connect access
  group but unbumped in the role map — they will get "no role"/no write
  privileges (never a default role).

---

## 2. Required Connect identity fields

The app resolves the authenticated user from Connect's **session user**
(`session$user` on the Shiny session) via `connect_identity()` in
`review-app/R/identity.R`.

- **Confirm which real-world field Connect populates into `session$user` —
  email address or username — in your specific Connect configuration.** The
  implementation accepts whatever Connect returns, but the **role map entries
  and this decision are coupled**: `config/roles.yml` must use the exact
  strings Connect returns, or identities will not resolve.
- Document the chosen field here when you confirm it:

  > Connect `session$user` resolves to: `EMAIL` / `USERNAME` (strike one).

- For **local development only** (no Connect), the app honors the
  `REVIEW_APP_USER` environment variable as the identity. It is never used in
  production policy decisions; production must remove it or leave it unset.
- An identity absent from `config/roles.yml` gets `role = NULL` and is denied
  all write actions (R3). A missing or malformed role map fails the app loudly
  at startup rather than running without authorization.

### 2.1 Updating the role map (MVP procedure)

There is **no in-app role-management UI** in this iteration. To change roles:

1. Edit `review-app/config/roles.yml` (one `{identity, role}` entry per
   authenticated Connect identity; `role` is `reviewer`, `approver`, or
   `administrator`).
2. Commit (or open a PR) and deploy the updated file to the branch/artifact the
   app reads the role map from, then restart/republish the Connect content item.
3. Note: an in-app admin UI for role management is explicitly out of scope for
   the MVP.

---

## 3. GitHub App credential provisioning and rotation (R12)

The app authenticates to GitHub as a **GitHub App** — it never uses reviewer
personal access tokens. It signs a short-lived JWT with the App's private key,
exchanges it for an installation access token scoped to this repository, and
caches the token per session with refresh before expiry
(`review-app/R/github_auth.R`).

### 3.1 Provisioning

1. **Create a GitHub App** (org-level for the CVS repository org) with
   repository permissions scoped to the minimum needed:
   - Contents: read/write (blobs, trees, commits, refs for the review branch).
   - Metadata: read.
   - Do **not** grant org-admin or broad repo scope.
2. **Install the App** on the CVS repository and record the **installation ID**.
3. **Fetch the App credentials**:
   - **App ID** (client ID number shown on the App's general page).
   - **Private key** (`.pem` file generated under *Generate a private key*).
   - **Installation ID** (from the install URL / API).
4. **Store the credentials only in Connect**, as environment variables or
   Connect secrets (see deployment, §5.3). Never commit them to the repository.

### 3.2 Environment variables (recommended naming)

The app reads GitHub App credential values through a small env/config helper
(`.gh_app_env` in `github_auth.R`) that checks an optional injected `cfg` list
first and then `Sys.getenv()`. Production should set these Connect
variables/secrets (the exact names below are the recommended convention; wire
them to the adapter factory at deploy time):

| Variable | Purpose |
|---|---|
| `REVIEW_APP_GH_APP_ID` | GitHub App ID |
| `REVIEW_APP_GH_PRIVATE_KEY` | PEM private key (connect secret) |
| `REVIEW_APP_GH_INSTALLATION_ID` | App installation ID for this repo |
| `REVIEW_APP_GH_OWNER` | Repository owner (e.g. `WorldBank-...`) |
| `REVIEW_APP_GH_REPO` | Repository name |
| `REVIEW_APP_GH_DEFAULT_BRANCH` | Default branch (e.g. `main`) — source context |
| `REVIEW_APP_GH_REVIEW_BRANCH` | Dedicated protected review branch (e.g. `review/...`) |
| `REVIEW_APP_ROLES` | (optional) absolute path to a role-map YAML override |

### 3.3 Rotation

1. **Private key rotation**: generate a new private key in the GitHub App
   settings, replace the `REVIEW_APP_GH_PRIVATE_KEY` Connect secret, and
   republish/restart the content. Keep the old App private key removed once the
   new one is verified (the App permits one active private key).
2. **Installation reinstalls**: if the App's installation is removed from the
   repo, reinstall it and update `REVIEW_APP_GH_INSTALLATION_ID`.
3. **Token expiry**: installation tokens are short-lived and refreshed
   automatically by the per-session token cache (refresh lead time 60s). No
   operator action is needed for routine token expiry.
4. **Credential leak**: revoke/rotate the private key immediately, and audit
   the review-branch commit history for unexpected commits.

### 3.4 Scope and safety

- The App writes only to the **review branch** (R13). The default branch's
  protection is untouched.
- The App's installation token must have the **minimum** repository permission
  set above. Prefer Connect secret storage over env (avoid secrets landing in
  content logs).

---

## 4. Review-branch and repository configuration (R13)

The app writes all review outputs (review records and approved artifacts) only
to a dedicated **protected review branch**. Source drafts are read from the
default branch and are never modified.

1. **Create the review branch** once (e.g. `review/human-review`), rooted at the
   current default-branch tip so the app's reads and the record paths exist.
2. **Configure GitHub branch protection** on the review branch:
   - Block **force pushes** (protect the branch from force-push).
   - Block **branch deletions**.
   - Only the **GitHub App's installation token** and **repository
     administrators** may push directly.
3. **Humans act only through the app** — never via direct `git push` to the
   review branch.
4. The review branch holds:
   - `extraction/30_review/<artifact_id>.review.yml` — per-artifact review
     records (authoritative audit ledger, append-only `events`).
   - `extraction/40_approved/<module>/<artifact_id>.md` — approved artifacts,
     one per approval, at the path mirroring the draft's location under
     `extraction/20_drafts/`.
5. Verify the branch protection rule once with a test push attempt (should be
   rejected for a non-admin identity without the App).

---

## 5. Deployment steps

### 5.0 Prerequisites

- R version supported by `review-app/renv.lock` (renv-managed).
- A Posit Connect server with **Connect identity provider** enabled
  (authentication is required; there is no anonymous mode).
- A GitHub App installed on the CVS repository (see §3).
- The protected review branch created (see §4).

### 5.1 Prepare the content bundle

From `review-app/`:

1. Restore the R environment: `renv::restore()` (committed lockfile).
2. (Optional) run a local pre-flight: `devtools::load_all(); run_review_app()`
   to confirm the app skeleton boots.
3. Build a bundle **excluding** the `renv/` local library and any local
   secrets. The repo's `.gitignore` already excludes `compound-gpid.local.md`,
   `.kilo/`, `.agents/`, `.claude/`, `.opencode/`, and generated build output —
   keep those out of the deployable bundle.

### 5.2 Publish to Connect

1. In the Connect UI (or `rsconnect`/`vetiver` deploy tooling), create the
   content item from `review-app/` and set the R runtime per `renv.lock`.
2. Set the app entry point to `app.R` (`shiny_review_app()`).
3. Restrict content access to the reviewer group(s) (§1).
4. Go live and open the app to confirm the dashboard loads for an authorized
   identity.

> **Entry point note:** `app.R` loads the package from the bundled source with
> `pkgload::load_all(".")` rather than `library(reviewapp)`. Posit Connect
> installs only the packages recorded in `renv.lock`, and the project-local
> `reviewapp` package cannot be installed from the bundle — so `app.R` must
> keep using `load_all` and `renv.lock` must keep `pkgload` in `Imports`
> (`renv::record("pkgload", lockfile = "renv.lock")` if it drifts out). Keep
> the empty `R/_disable_autoload.R` guard in place: it stops Shiny from
> auto-sourcing `R/` before `app.R` (which would duplicate the `load_all`
> definitions and log the "appears to contain an R package" warning).

### 5.3 Configure Connect secrets / environment variables

Set the variables from §3.2 as **Connect environment variables or Vault
secrets** (prefer secrets for `REVIEW_APP_GH_PRIVATE_KEY`). The app reads them
at session start; after any change, republish or restart the content.

### 5.4 Deploy-time wiring of the GitHub adapter

The Shiny server expects an injected GitHub adapter handle (the storage
interface, R20). At deploy time, construct it from the Connect secrets, e.g.:

```r
adapter <- reviewapp::new_github_adapter(
  owner          = Sys.getenv("REVIEW_APP_GH_OWNER"),
  repo           = Sys.getenv("REVIEW_APP_GH_REPO"),
  default_branch = Sys.getenv("REVIEW_APP_GH_DEFAULT_BRANCH"),
  review_branch  = Sys.getenv("REVIEW_APP_GH_REVIEW_BRANCH"),
  get_token      = function() {
    reviewapp::installation_token(
      get_token = function() reviewapp::gh_exchange_installation_token(
        app_id          = Sys.getenv("REVIEW_APP_GH_APP_ID"),
        private_key_pem = Sys.getenv("REVIEW_APP_GH_PRIVATE_KEY"),
        installation_id = Sys.getenv("REVIEW_APP_GH_INSTALLATION_ID")
      ),
      cache = reviewapp::new_token_cache()
    )
  }
)
# then inject `adapter` into the app server (replaces the local/dev handle)
```

This wiring is what Phase 5 calibration (V9) exercises end-to-end against a
disposable test branch if production branch protection is not yet configured.

### 5.5 First-run smoke check

1. Log in as a mapped `reviewer` — dashboard loads with the live queue.
2. Open an artifact — YAML/evidence panels render read-only; the Markdown body
   is editable; a preview renders.
3. Perform a **save-draft**, then a **submit** — the write must report success
   and the record must be visible on the review branch.
4. Confirm an unmapped identity sees "not authorized" and **no** action buttons.

---

## 6. Monitoring

- **Connect logs**: watch the content's runtime logs for errors. Expected
  signals:
  - `stale, please reload: ...` — optimistic-lock rejection (normal, user
    re-loads and reapplies).
  - `PARTIAL FAILURE: transition NOT applied. Completed steps: [...]` —
    requires the incident-recovery procedure (§7).
  - GitHub API 4xx/5xx errors — check App permissions (§3.4) and that the
    token exchange is current.
- **Branch health**: periodically confirm the review branch's protection is
  still active and that only App/administrator pushes appear in history.
- **Role map**: after role changes, confirm the expected identities resolve
  (see §2.1).
- **Freshness**: the dashboard re-scans on user "Refresh" and page load; there
  are **no push/websocket updates** in the MVP. A stale dashboard only ever
  produces a rejected save (never a silent overwrite), so this is a UX
  convenience, not a correctness mechanism.

---

## 7. Incident recovery — partial GitHub writes (R18, Step 7)

The app wraps every multi-file logical write in `adapter_write_with_recovery()`
(`review-app/R/recovery.R`). A write only ever reports
`transition_applied = TRUE` when the **entire** atomic operation (staleness
check → blob(s) → tree → commit → ref update) completed. A partial
API/network failure surfaces exactly which steps completed and which did not,
and **never claims a transition succeeded** (R18).

### 7.1 Recovery report fields

| Field | Meaning |
|---|---|
| `ok` | overall success boolean |
| `transition_applied` | TRUE **only** when the full atomic write completed |
| `commit_sha` | commit created on success (NULL otherwise) |
| `steps_completed` | which of the 5 write steps completed |
| `error$kind` | `stale` (optimistic lock), `partial` (mid-write API failure), or `other` |

### 7.2 Response by error kind

**`stale` (optimistic-lock rejection) — no write occurred.**
- Operator/user action: reload the artifact and reapply the edits. The app
  preserves unsaved text in the server-side session so the user can review the
  newer remote version before reapplying. If a concurrent approver already
  moved the artifact's `state`, the app says so explicitly.
- This is expected under concurrency; not a data-loss incident.

**`partial` (mid-write failure).**
1. The transition was **not** applied; do **not** treat the review state as
   changed.
2. Inspect the generated report: `steps_completed` tells you how far the write
   got (e.g. blobs created but ref update failed, or a commit was created but
   the branch ref did not move).
3. Use `recovery_report_text(report)` (in `recovery.R`) for a one-line
   operator-facing description.
4. Reconciliation:
   - If the ref update failed after a commit was created, the commit may exist
     on the API side without the branch pointing at it. Re-run the write: the
     staleness pre-check re-reads the current ref; a moved ref is handled
     before any new write. Do **not** force-push.
   - Inspect the review-branch history to confirm which paths were actually
     updated; the affected paths and commit status are in the report.
   - Re-apply the logical operation once the failure cause is resolved.
5. Escalate to repository administrators only if a ref cannot be reconciled
   through the app and manual repair is required on the review branch (as
   permitted by its protection rule).

**`other` (generic write failure).**
- Check Connect secrets (§3.2), App permissions (§3.4), and the GitHub API
  status before retrying.

### 7.3 Operator utility

`recovery.R` provides the inspection/report surface. There is no separate
CLI/DB in the MVP; the recovery report returned to the UI (rendered as a
notification) is the operator's primary signal. The dashboard's per-record
state and the review-branch history are the cross-checks.

---

## 8. Storage semantics (R17) and deferred scope (R19)

- **R17 — Connect persistent storage is disposable.** Do not store review
  state, audit events, or approved artifacts in Connect persistent storage.
  The authoritative ledger is the review-branch records + approved artifacts.
  Temporary/operational state (e.g. an in-flight draft in session memory) lives
  only for the session and is lost when the session ends.
- **R19 — Deferred and separately tracked.** Pull-request automation and
  CODEOWNERS/branch-protection enforcement are collective, tracked roadmap
  items, **not features of this MVP**. The MVP commits directly to the review
  branch (R13) and drives approval through the in-app state machine.

---

## 9. Related documentation

- Plan: `.cg-docs/plans/2026-08-04-build-human-review-application.md` (Data
  Schemas, state-transition table, Verification Surface V1–V9).
- Role map format/procedure: `review-app/config/roles.yml`.
- App source: `review-app/` (R modules, tests, `renv.lock`).
- Local dev: run `renv::restore()` then `devtools::load_all(); run_review_app()`
  (see `review-app/README.md`).
- Phase 5 calibration (V9): validate the workflow against the planned sample of
  5–10 variables using a disposable test branch/repo if production protection
  is not yet configured.

## 10. Calibration live-run deployment checklist (plan `2026-08-07-calibrate-human-review.md`, Step 10)

This is the operator checklist for provisioning the disposable environment the
calibration live operator run (Step 11) executes against. The Shiny server
builds its GitHub adapter at session start via `review_app_adapter()` in
`review-app/R/github_adapter.R`, which reads these exact Connect
variables/secrets:

| Variable | Purpose |
|---|---|
| `REVIEW_APP_GH_OWNER` | Disposable repo owner |
| `REVIEW_APP_GH_REPO` | Disposable repo name |
| `REVIEW_APP_GH_DEFAULT_BRANCH` | Source branch (e.g. `main`) |
| `REVIEW_APP_GH_REVIEW_BRANCH` | Protected review branch (e.g. `review`) |
| `GITHUB_APP_ID` | GitHub App ID |
| `GITHUB_APP_INSTALLATION_ID` | GitHub App installation ID for the repo |
| `GITHUB_APP_PRIVATE_KEY` | GitHub App private key (Connect secret) |
| `REVIEW_APP_ROLES` | (optional) absolute path to a role-map YAML override |

> Naming note: the adapter factory in this plan reads `GITHUB_APP_ID`,
> `GITHUB_APP_INSTALLATION_ID`, and `GITHUB_APP_PRIVATE_KEY` for the App
> identity (matching `github_auth.R`'s `.gh_app_env` helper). Earlier drafts of
> the operator guide proposed a `REVIEW_APP_GH_*` variant for the App fields;
> the connected secrets must use the names the deployed code reads.

Sequence:

1. **Provision a disposable GitHub repo** (e.g. `gmd-calibration-<date>`), plus
   a **narrowly scoped GitHub App** with contents read/write on the default and
   review branches only. Register Connect secrets: `GITHUB_APP_ID`,
   `GITHUB_APP_INSTALLATION_ID`, `GITHUB_APP_PRIVATE_KEY`,
   `REVIEW_APP_GH_OWNER`, `REVIEW_APP_GH_REPO`,
   `REVIEW_APP_GH_DEFAULT_BRANCH`, `REVIEW_APP_GH_REVIEW_BRANCH`.
2. **Create the protected `review` branch**; block force-push and deletion;
   leave default-branch protection untouched.
3. **Stage the 6 calibration drafts** (Step 9) as drafts under
   `extraction/20_drafts/<module>/<id>.md` on the default branch:
   `dem/VAR-male`, `dem/VAR-educat4`, `dem/VAR-educy`, `dem/VAR-educat7`,
   `geo/VAR-urban`, `dem/VAR-marital`.
4. **Configure `review-app/config/roles.yml`** with 2 test Connect identities
   (one reviewer, one approver).
5. **Deploy** the content item (`rsconnect::deployApp` on `review-app/`), private
   group access, Connect auth confirmed as the only login (C7).
6. **Verify** the app boots (Phase 1 Step 1 entry-point fix) and the queue
   populates from the adapter (Phase 1 Step 2 wiring fix): 6 artifacts, module
   filter includes `dem` and `geo`.
7. Run the live operator protocol from
   `.cg-docs/calibration/live-operator-protocol.md` (Step 11), populating
   `content-error-log.yaml`, `defect-log.yaml`, and `friction-log.yaml`, then
   aggregate in Step 12 (`calibration-report.md`).
