# GMD Human Review Application - Posit Connect Operator Guide

_Production queue runbook for the Release A plan
`1787366447127-production-review-queue-plan.md`._

This guide is the operator-facing reference for deploying and operating the
private, Git-backed **Shiny for R** review application on Posit Connect. It
covers access/group configuration, Connect identity, GitHub App credentials,
branch configuration, Git-backed deployment, production queue bootstrap,
source-drift response, queue-index repair, monitoring, rollback, and recovery
from partial writes.

This runbook documents intended Release A contracts. The application code and
operator actions must create and verify production queue state; this file does
not assert that a production manifest, index, branch, bundle, or Connect GUID
already exists.

## Operating modes

- **Production:** `review/production` is the new protected production data
  branch. It uses the strict versioned queue manifest, queue index, and v2
  review records. The Git-backed Connect content item itself tracks the
  application source on `main`.
- **Legacy calibration:** `review` is preserved calibration history at
  `983d7d9503fbf5c2c911ac9d85a37b88accfe4ac`. It is read-only and may be used
  only for the legacy six-record calibration view. Do not bootstrap production
  state on this branch and do not modify or rewrite it.

Production queue visibility and approval eligibility are separate. Release A
enrolls all 267 tracked drafts, including records with governance blockers, but
`approval_mode` remains `disabled` until the Release B gates are satisfied.

It explicitly documents two design decisions from the plan:

- **R17 — Connect persistent storage is disposable cache only.** Connect's
  persistent storage must never be treated as the authoritative audit ledger.
  The authoritative ledger is the per-artifact review record
  (`extraction/30_review/*.review.yml`) and the approved artifacts
  (`extraction/40_approved/*`) committed to the protected review branch.
- **R19 — PR automation and CODEOWNERS are deferred.** Pull-request automation
  and CODEOWNERS integration remain **out of scope** for this iteration. The
  production queue plan nevertheless requires protection of
  `review/production`, including its exact required checks and governed direct
  writers. Only the deferred automation/CODEOWNERS features remain outside
  scope; do not treat their absence as a defect.

---

## 0. Architecture in one paragraph

The app (`review-app/`) is a self-contained R package served by Shiny on Posit
Connect. It authenticates users with **Connect authentication only** (R2); no
second login layer is permitted. The authenticated identity is resolved
against a repository-managed role map (`review-app/config/roles.yml`) into
`reviewer`, `approver`, or `administrator` (R3). All Git operations use the
**GitHub App identity** (R12): source drafts are read from `main` as canonical
read-only context, while review records, queue controls, and approved artifacts
are written only to the protected review branch (R13). Writes are atomic
multi-file commits with scoped optimistic locking (R11, R14, R18).

Connect persistent storage is disposable cache only. GitHub review records and
approved artifacts on the review branch are the authoritative audit ledger.

---

## 1. Private Connect access and group configuration (R1, R2)

1. Create or identify a Content view in Posit Connect (e.g. `CVS Review`) that
   only the intended GPID review team can see. The app is private: only
   authenticated Connect users in the allowed group(s) may access it.
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
  group but unmapped in the role map - they will get "no role"/no write
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
2. Commit (or open a PR) and deploy the updated file to the branch and
   subdirectory watched by the Git-backed Connect content item, then allow
   Connect to rebuild or restart the content.
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
    Connect secrets (see deployment, §5.2). Never commit them to the repository.

### 3.2 Environment variables

The app reads GitHub App credential values through `.gh_app_env` in
`github_auth.R` and then `Sys.getenv()`. Production must set the exact Connect
variables/secrets below:

| Variable | Purpose |
|---|---|
| `GITHUB_APP_ID` | Numeric GitHub App ID, not the `Iv...` Client ID |
| `GITHUB_APP_PRIVATE_KEY` | Full PEM contents, preferably a Connect secret |
| `GITHUB_APP_INSTALLATION_ID` | App installation ID for this repo |
| `REVIEW_APP_GH_OWNER` | Repository owner (e.g. `WorldBank-...`) |
| `REVIEW_APP_GH_REPO` | Repository name |
| `REVIEW_APP_GH_DEFAULT_BRANCH` | Default branch (e.g. `main`) — source context |
| `REVIEW_APP_GH_REVIEW_BRANCH` | Dedicated protected production branch: `review/production` |
| `REVIEW_APP_ROLES` | (optional) absolute path to a role-map YAML override |
| `GOLEM_CONFIG_ACTIVE` | Production profile: `production` |
| `REVIEW_APP_USER` | Must be unset in Connect; local-development identity override only |
| `REVIEW_APP_OFFLINE` | Must be unset in Connect; `1` is CI/local offline mode only |

For production, leave `REVIEW_APP_ROLES` unset when the bundled role map is
used, or record the SHA-256 digest of the override file in the redacted A9
attestation. Do not use `REVIEW_APP_USER` or `REVIEW_APP_OFFLINE` to bypass
Connect identity or the live GitHub adapter.

For the GitHub Actions R validation job only, use
`REVIEW_APP_OFFLINE=1`, set `REVIEW_APP_ROLES` to the checked-out
`review-app/config/roles.yml`, set `NOT_CRAN=true`, and leave
`REVIEW_APP_USER` unset. These values are test controls, not production
configuration. CI supplies no GitHub App credentials and does not contact
GitHub or Connect.

### 3.3 Rotation

1. **Private key rotation**: generate a new private key in the GitHub App
   settings, replace the `GITHUB_APP_PRIVATE_KEY` Connect secret, and
    restart the Connect content. Keep the old App private key removed once the
   new one is verified (the App permits one active private key).
2. **Installation reinstalls**: if the App's installation is removed from the
   repo, reinstall it and update `GITHUB_APP_INSTALLATION_ID`.
3. **Token expiry**: installation tokens are short-lived and refreshed
   automatically by the per-session token cache (refresh lead time 60s). No
   operator action is needed for routine token expiry.
4. **Credential leak**: revoke/rotate the private key immediately, and audit
   the review-branch commit history for unexpected commits.

### 3.4 Scope and safety

- The App writes only to the **production review branch** (R13). The default
  branch's protection is untouched.
- The App's installation token must have the **minimum** repository permission
   set above. Prefer Connect secret storage over env (avoid secrets landing in
   content logs).
- `GITHUB_APP_PRIVATE_KEY` must contain the complete `.pem` file contents,
  including the `-----BEGIN ... PRIVATE KEY-----` and `-----END ... PRIVATE
  KEY-----` lines. Do not enter the filename, a path, the `Iv...` Client ID,
  or a base64-encoded copy of the file.

---

## 4. Review-branch and repository configuration (R13)

The app reads source drafts from `main` and never modifies that branch. It
writes queue controls, review records, and approved artifacts only to the
dedicated protected **data branch `review/production`**. The Connect content
item itself remains Git-backed from the application source branch; do not
confuse that source branch with `REVIEW_APP_GH_REVIEW_BRANCH`.

1. Before creating production state, assert the preserved calibration branch
   remotely rather than trusting a stale local ref:

   ```sh
   gh api \
     "repos/GMD-hub/GMD-canonical-schema/git/ref/heads/review" \
     --jq '.object.sha'
   ```

   The expected calibration SHA is
   `983d7d9503fbf5c2c911ac9d85a37b88accfe4ac`. Stop if it differs.
2. Create `review/production` from the tested app `main` commit. Never merge
   production queue state back into `main`.
3. Protect `review/production` by blocking force pushes and deletion. Permit
   governed direct writes only for the installed GitHub App and named
   administrators. Humans otherwise act through the application.
4. Require these exact successful checks for human pull requests:

   ```text
   Validate canonical schema / Python validation
   Validate canonical schema / Review-app R validation
   ```

5. Perform a protected-branch canary before bootstrap. Verify that force pushes
   and deletion are blocked, an unprivileged identity cannot push, and the
   app/App path can perform a governed write.

The production branch contains:

- `extraction/30_review/queue-manifest.yml` - the queue contract and Release A
  approval mode.
- `extraction/30_review/queue-index.yml` - the derived validated dashboard
  index.
- `extraction/30_review/<artifact_id>.review.yml` - v2 per-artifact records
  and append-only audit events.
- `extraction/40_approved/<module>/<artifact_id>.md` - approved artifacts only
  after the approval gates are enabled and satisfied.

The legacy `review` branch contains calibration records only and remains
read-only.

---

## 5. Git-backed Connect deployment

### 5.0 Prerequisites

- R version supported by `review-app/renv.lock` (renv-managed).
- Posit Connect with authentication enabled and the reviewer group configured.
- A GitHub App installed on the CVS repository (see §3).
- The protected `review/production` data branch created (see §4).
- A Git-backed Connect content item configured for this repository, the
  application source branch, and the `review-app/` subdirectory.

### 5.1 Configure the active content item

The active deployment model is Git-backed content deployment. Configure the
Connect content item to build `review-app/` from the repository and its
application source branch. A push to that watched branch causes Connect to
rebuild the content item. The entry point is `review-app/app.R`.

Do not use `rsconnect::deployApp()` or manual bundle upload as the active
production procedure. The checked-in Publisher and `rsconnect` records are
historical metadata for an earlier deployment path. They are retained for
audit and must not be edited because they are generated records:

- `review-app/.posit/publish/review-app-9KP9.toml`
- `review-app/.posit/publish/deployments/deployment-U42S.toml`
- `review-app/rsconnect/wbconnect/acastanedaa/.dcf`
- `review-app/rsconnect/wbconnect/acastanedaa/review-app.dcf`

Active deployment facts must come from the Connect API: content GUID, bundle
ID, deployed commit and time, repository, source branch, app subdirectory, R
runtime, and smoke result. Do not copy historical or unverified values from
the generated records into the production attestation.

### 5.2 Configure Connect secrets and environment

Set the variables in §3.2 in the Connect content configuration. Keep
`GITHUB_APP_PRIVATE_KEY` in Connect secret storage. Never commit, print, or
include credentials in logs or the attestation. After changing configuration,
restart the content item and verify the active configuration through Connect.

The server constructs the GitHub adapter automatically at session start. Do
not inject a second adapter or a reviewer personal access token.

`REVIEW_APP_GH_DEFAULT_BRANCH=main` identifies the immutable source context.
`REVIEW_APP_GH_REVIEW_BRANCH=review/production` identifies the production data
branch. `REVIEW_APP_USER` and `REVIEW_APP_OFFLINE` are local/CI controls and
must be unset in Connect.

### 5.3 Deploy and verify application code

Merge the tested application change to the branch watched by Connect. Confirm
that Connect pulled the expected commit and completed the build. `app.R` loads
the package source with `pkgload::load_all(".")`; it is the Connect entry point
and must remain in the Git-backed content item.

An application-code rollback is a deployment operation: revert the application
commit through the normal Git-backed process or restore a prior known-good
Connect bundle if the item cannot rebuild. Changing only the review data branch
does not roll back application code.

### 5.4 Redacted A9 environment attestation

Before cutover, record this exact non-secret configuration attestation. The
`REVIEW_APP_ROLES=unset` line is the default; when an override is configured,
record its SHA-256 digest instead. Never record the file contents or any secret
value.

```text
REVIEW_APP_GH_OWNER=GMD-hub
REVIEW_APP_GH_REPO=GMD-canonical-schema
REVIEW_APP_GH_DEFAULT_BRANCH=main
REVIEW_APP_GH_REVIEW_BRANCH=review/production
GOLEM_CONFIG_ACTIVE=production
REVIEW_APP_USER=unset
REVIEW_APP_OFFLINE=unset
REVIEW_APP_ROLES=unset
```

When a role-map override is configured, record
`REVIEW_APP_ROLES=sha256:<roles-file-sha256>` instead of `unset`.

The attestation is a redacted operator record, not a substitute for the
Connect API deployment facts. Do not claim it is complete until Connect's
active repository, source branch, subdirectory, runtime, GUID, bundle, and
deployed commit/time have also been captured.

### 5.5 Connect cutover and smoke check

1. Repoint or restart the active Git-backed Connect item with the production
   runtime configuration above.
2. Log in as the mapped administrator and run the explicit 267-record
   bootstrap described in §6.
3. Verify the queue total and module counts: `267`, `9/14/24/90/61/69`.
4. Verify every record is unassigned and approval-blocked.
5. As a reviewer, open, edit, save, and submit one designated smoke artifact.
   Record the selected artifact ID in the cutover evidence; do not invent one
   in advance.
6. As an approver, verify that server-side approval is rejected while the
   global gate is disabled.
7. In staging or a disposable branch, trigger source drift and verify that all
   state-changing writes fail closed.
8. Capture the Connect API deployment facts listed in §5.1 and the smoke
   results.

---

## 6. Production queue contract and bootstrap

### 6.1 Queue manifest

The production manifest is
`extraction/30_review/queue-manifest.yml`. It must contain the schema version,
queue ID, creation identity/time, source commit, expected total and module
counts, expected path-set identity, queue-index path, source-manifest,
inventory, and agent-review identities/digests, `approval_mode`, global
blockers, and artifact blockers. Pending source-manifest, inventory, or
agent-review identities must be recorded explicitly as `pending`, not guessed.

The initial global blockers are:

- `SOURCE_LOCK_PENDING`
- `SOURCE_INVENTORY_FREEZE_PENDING`
- `RUBRIC_GATE_PENDING`
- `PRODUCTION_CALIBRATION_PENDING`

`approval_mode` must remain `disabled` for Release A even if an individual
blocker is edited. Enabling approval is a later Release B administrator action
that requires the readiness command and an audit event.

### 6.2 Queue index

The derived index is
`extraction/30_review/queue-index.yml`. It contains one compact row for each
of the 267 artifacts: artifact ID, source path, module, lifecycle state,
review round, assignments, record path and blob identity, current content
hash, and governance-blocked/source-drift indicators. The dashboard reads this
single index rather than fetching 267 records. Per-artifact records remain the
authoritative audit records. The manifest never stores a digest of this
mutable index; each action uses the current index Git blob SHA as its control
dependency.

### 6.3 Administrator bootstrap

Bootstrap is available only when the configured branch is exactly
`review/production` and the branch has no queue manifest. It requires an
authenticated Connect identity mapped to `administrator` and explicit
confirmation of the source commit, total `267`, and module counts:

```text
IDN=9 GEO=14 DEM=24 LBR=90 UTL=61 DWL=69 TOTAL=267
```

The administrator procedure is:

1. Resolve one `main` head and enumerate only
   `extraction/20_drafts/<module>/VAR-*.md` for the six reviewed modules.
2. Reject any missing, extra, duplicate, malformed, or wrongly owned path.
3. Fetch the source tree once and retrieve draft contents in bounded GitHub
   GraphQL batches of at most 50 blobs per request. Compute source, full-body,
   and body digests in memory and show progress.
4. Generate 267 unassigned v2 records, the manifest, and the queue index.
5. Re-read the `main` head. Abort if it moved. Validate the complete payload
   and enforce the configured payload-size limit before writing.
6. Submit the generated records, index, and manifest as inline tree entries,
   create one commit, and perform one non-force ref update. No partial
   production ref is acceptable.
7. Record the administrator in the manifest and commit message. A repeated
   bootstrap is rejected after the manifest exists; it never implicitly repairs
   or re-enrolls the queue.

The implementation must stay within the bounded GitHub request budget and
leave the branch unchanged if any pre-publication step fails. The 267-record
fixture target is no more than 15 GitHub requests, with the payload-size limit
checked before publication. The human administrator, not an implementation
agent, performs this production action.

### 6.4 Source drift and fail-closed behavior

Each v2 record binds an artifact to its immutable enrolled source blob SHA,
source content SHA-256, source commit, and enrolled body digest. On detail
load, the app displays the enrolled source snapshot and separately resolves
the current `main` path. A changed or deleted artifact, unreadable source, or
failed hash/blob verification is source drift.

Each production record must declare `record_schema_version: "2.0"`, its queue
ID, artifact and source-path identity, lifecycle state, round, assignments,
enrollment identity/time, structured assessment placeholder, blocker
references, and append-only events. Version 2 events use
`review_record_blob_sha_before` for optimistic-lock audit; do not reuse the
ambiguous legacy `source_blob_sha` field for that purpose.

Immediately before every state-changing action, the app must re-fetch and
verify the current source and queue manifest. On drift, API failure, an
unverifiable blob, an invalid manifest/index, or uncertain blocker state, the
app fails closed: it may display the enrolled snapshot but must not save,
submit, request revision, assign, approve, or otherwise write. An unrelated
`main` commit is not drift when the enrolled artifact blob and content hash are
unchanged. Approval, when eventually enabled, uses the enrolled immutable
front matter and persisted reviewed body only.

### 6.5 Queue-index repair

If `queue-index.yml` is missing, malformed, or inconsistent, stop all review
writes and keep the production branch intact while diagnosing. An
administrator must rebuild it from the current queue manifest and authoritative
v2 records, then validate:

- exactly 267 rows with no duplicate artifact IDs;
- module counts `9/14/24/90/61/69` and the manifest path-set identity;
- safe artifact IDs, source paths, record paths, record blob SHAs, state/round
  values, and scalar blocker/drift flags;
- queue ID and manifest compatibility; and
- byte-identical deterministic serialization from the same records and
  manifest.

Publish a repair only as one non-force protected-branch commit after all checks
pass. Do not hand-edit a row, repair an index without its manifest, alter an
artifact record as part of an index repair, or use repair to bypass source
drift or approval blockers. If the manifest is missing, the correct state is
administrator bootstrap/error, not implicit repair.

### 6.6 Data-cutover rollback

If the production queue or production branch must be taken out of service:

1. Change the configured review branch back to `review` and restart the
   Git-backed Connect content item.
2. Confirm that the legacy calibration queue is visible read-only.
3. Leave `review/production` intact for diagnosis and preserve its history.
4. Never force-push, rewrite, delete, or merge either review branch as part of
   the rollback.

This data rollback is distinct from application-code rollback in §5.3. If the
application code itself is defective, restore the prior known-good app commit
through the Git-backed deployment process or use a prior Connect bundle; do not
change only the review branch and call that an app rollback.

---

## 7. Monitoring

- **Connect logs**: watch the content's runtime logs for errors. Expected
  signals:
  - `stale, please reload: ...` - optimistic-lock rejection (normal, user
    re-loads and reapplies).
  - `PARTIAL FAILURE: transition NOT applied. Completed steps: [...]` -
    requires the incident-recovery procedure (§8).
  - GitHub API 4xx/5xx errors - check App permissions (§3.4) and that the
    token exchange is current.
- **Branch health**: periodically confirm `review/production` protection is
  still active and that only App/administrator pushes appear in its history.
- **Role map**: after role changes, confirm the expected identities resolve
   (see §2.1).
- **Freshness**: the dashboard refreshes its queue index on page load and user
  refresh. A stale dashboard must produce a rejected action, never a silent
  overwrite.

---

## 8. Incident recovery - partial GitHub writes (R18)

The app wraps every multi-file logical write in `adapter_write_with_recovery()`
(`review-app/R/recovery.R`). A write only ever reports
`transition_applied = TRUE` when the **entire** atomic operation (staleness
check → blob(s) → tree → commit → ref update) completed. A partial
API/network failure surfaces exactly which steps completed and which did not,
and **never claims a transition succeeded** (R18).

### 8.1 Recovery report fields

| Field | Meaning |
|---|---|
| `ok` | overall success boolean |
| `transition_applied` | TRUE **only** when the full atomic write completed |
| `commit_sha` | commit created on success (NULL otherwise) |
| `steps_completed` | which of the 5 write steps completed |
| `error$kind` | `stale` (optimistic lock), `partial` (mid-write API failure), or `other` |

### 8.2 Response by error kind

**`stale` (optimistic-lock rejection) - no write occurred.**
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

### 8.3 Operator utility

`recovery.R` provides the inspection/report surface. There is no separate
CLI/DB in the MVP; the recovery report returned to the UI (rendered as a
notification) is the operator's primary signal. The dashboard's per-record
state and the review-branch history are the cross-checks.

---

## 9. Storage semantics (R17) and deferred scope (R19)

- **R17 — Connect persistent storage is disposable.** Do not store review
  state, audit events, or approved artifacts in Connect persistent storage.
  The authoritative ledger is the review-branch records + approved artifacts.
  Temporary/operational state (e.g. an in-flight draft in session memory) lives
  only for the session and is lost when the session ends.
- **R19 — Deferred and separately tracked.** Pull-request automation and
  CODEOWNERS integration are tracked roadmap items, **not features of this
  MVP**. Protection of `review/production` and its required checks are part of
  the Release A operator setup. Release A commits governed queue state directly
  to `review/production` (R13) and drives review through the in-app state
  machine.

---

## 10. Related documentation

- Production queue plan: `.kilo/plans/1787366447127-production-review-queue-plan.md`.
- Historical app plan: `.cg-docs/plans/2026-08-04-build-human-review-application.md`
  (Data Schemas, state-transition table, Verification Surface V1–V9).
- Role map format/procedure: `review-app/config/roles.yml`.
- App source: `review-app/` (R modules, tests, `renv.lock`).
- Local dev: run `renv::restore()` then `pkgload::load_all(".");
  reviewapp::run_app()` (see `review-app/README.md`).
- Phase 5 calibration (V9): validate the workflow against the planned sample of
  5–10 variables using a disposable test branch/repo if production protection
  is not yet configured.

## 11. Historical calibration checklist (not production)

The following checklist is retained as historical calibration material from
plan `2026-08-07-calibrate-human-review.md`, Step 10. It is not the production
deployment procedure and must not be used to configure the production queue.
It provisions a disposable repository and legacy `review` branch for the
six-record calibration run. The active production procedure is §5-§6.

The Shiny server builds its GitHub adapter at session start via
`review_app_adapter()` in `review-app/R/github_adapter.R`, which reads these
exact Connect variables/secrets:

| Variable | Purpose |
|---|---|
| `REVIEW_APP_GH_OWNER` | Disposable repo owner |
| `REVIEW_APP_GH_REPO` | Disposable repo name |
| `REVIEW_APP_GH_DEFAULT_BRANCH` | Source branch (e.g. `main`) |
| `REVIEW_APP_GH_REVIEW_BRANCH` | Protected legacy calibration branch (`review`) |
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
5. **Deploy** the disposable calibration content item through the deployment
   mechanism available for that historical run; do not use this step for the
   Git-backed production content item.
6. **Verify** the app boots (Phase 1 Step 1 entry-point fix) and the queue
   populates from the adapter (Phase 1 Step 2 wiring fix): 6 artifacts, module
   filter includes `dem` and `geo`.
7. Run the live operator protocol from
   `.cg-docs/calibration/live-operator-protocol.md` (Step 11), populating
   `content-error-log.yaml`, `defect-log.yaml`, and `friction-log.yaml`, then
   aggregate in Step 12 (`calibration-report.md`).
