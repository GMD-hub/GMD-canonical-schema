# GMD Human Review Application

A private, Git-backed Shiny for R application for the GPID team's human review
workflow. Built with the [Golem](https://thinkr-open.github.io/golem/) framework
for production-grade Shiny applications and deployed on Posit Connect.

## Queue Modes and Release A

The intended production review queue uses `review-production`. The preserved
`review` branch is the legacy calibration queue and remains historical,
read-only review data. These branches have different contracts:

- `review-production` requires the strict production queue manifest, queue
  index, and versioned review records.
- `review` supports legacy calibration records only as read-only content. It
  must not be used as the production queue or as a source for a bootstrap.

Release A makes all 267 non-welfare drafts visible while approval remains
disabled. The tracked denominator and module counts are:

| Module | Count |
|---|---:|
| IDN | 9 |
| GEO | 14 |
| DEM | 24 |
| LBR | 90 |
| UTL | 61 |
| DWL | 69 |
| **Total** | **267** |

An authenticated administrator performs the initial bootstrap. Records start
unassigned. Governance-blocked records may be opened, edited, saved, submitted,
and returned for revision, but no record may be approved while the global
approval gate is disabled.

The manifest, index, and production review records are operator-produced Git
state; they are not generated or asserted by this README. Until bootstrap and
the A9 smoke checks are complete, production commit, blob, bundle, and Connect
GUID values are intentionally not recorded here.

Production operators must run the fail-closed queue validator and redacted
Connect attestor documented in
[`docs/operator-guide.md`](docs/operator-guide.md#63-production-bootstrap).
The tools are `tools/validate-production-queue.R` and
`tools/attest-connect.R`; neither changes repository or remote state.

## Project Structure

```
review-app/
├── R/
│   ├── app_config.R         # Golem config: app_sys(), golem_add_external_resources()
│   ├── app_ui.R             # Top-level UI composing module UIs
│   ├── app_server.R         # Top-level server wiring modules + navigation
│   ├── run.R                # Entry point: run_app(), backward-compat aliases
│   ├── mod_dashboard.R      # Work-queue module (filters, DT table, refresh)
│   ├── mod_detail.R         # Artifact detail module (editor, preview, actions)
│   ├── models.R             # Review-record, event, and role-map data models
│   ├── state_machine.R      # Pure state-transition engine
│   ├── authorization.R      # Role-gated authorization gate
│   ├── github_adapter.R     # GitHub REST API adapter (reads/writes)
│   ├── github_auth.R        # GitHub App JWT signing + token exchange
│   ├── hashing.R            # SHA-256 hashing (cross-language compatible)
│   ├── identity.R           # Connect identity resolution
│   ├── index.R              # Dashboard work-queue index builder
│   ├── queue_manifest.R     # Production queue and index contracts
│   ├── source_binding.R     # Immutable source and drift checks
│   ├── enrollment.R         # Administrator production bootstrap
│   ├── recovery.R           # Atomic multi-file commit + partial-failure recovery
│   ├── actions.R            # Role-gated action orchestration
│   └── frontmatter.R        # YAML front-matter handling + Markdown preview
├── inst/
│   ├── golem-config.yml     # Golem environment-aware configuration
│   └── app/www/
│       └── custom.css       # Custom styles for the review UI
├── dev/
│   ├── 01_start.R           # Golem setup history (do not re-run)
│   ├── 02_dev.R             # Development workflow helpers
│   ├── 03_deploy.R          # Deployment helpers
│   └── run_dev.R            # Quick-launch script for development
├── config/
│   └── roles.yml            # Role map: identity -> role (reviewer/approver/admin)
├── tests/
│   └── testthat/            # Test files covering all modules
├── docs/
│   └── operator-guide.md    # Git-backed Posit Connect operator runbook
├── DESCRIPTION              # Package metadata + dependencies
├── NAMESPACE                # Exported functions
├── app.R                    # Posit Connect entry point
├── renv.lock                # Pinned dependency versions (R 4.5.2)
└── .Rprofile                # renv bootstrap
```

### Module Architecture

The application follows the Golem `mod_*` convention with two primary modules:

| Module | File | Responsibility |
|--------|------|----------------|
| `dashboard` | `mod_dashboard.R` | Work-queue table, filters (module/state/assignment), refresh |
| `detail` | `mod_detail.R` | Artifact editor, live preview, role-gated action buttons |

Modules communicate through shared reactive state managed by `app_server`:
- A shared `refresh_counter` reactiveVal allows the detail module to trigger
  queue reloads after successful actions without tight coupling.
- The dashboard exposes `selected_artifact` (reactive) consumed by detail.
- Navigation between panels is handled at the app level since it references
  the top-level `navset_hidden`.

### Performance Optimizations

- **Debounced preview**: The Markdown live preview uses `shiny::debounce()`
  with a 300ms delay, preventing re-renders on every keystroke.
- **Token caching**: GitHub installation tokens are cached per-session with
  automatic refresh 60 seconds before expiry.
- **On-demand queue loading**: The work queue loads only on explicit Refresh
  button click or after a successful action, not on every reactive invalidation.
- **Minimal DT options**: The DataTable uses `dom = "t"` (table only) for
  faster rendering.

## Quick Start (Development)

```r
# 1. Restore the renv environment
renv::restore()

# 2. Load the package in development mode
pkgload::load_all()

# 3. Run the app locally (offline mode -- no GitHub connection)
Sys.setenv(REVIEW_APP_OFFLINE = "1")
reviewapp::run_app()

# 4. Run the test suite
testthat::test_dir("tests/testthat")
```

Or source the dev runner:

```r
source("dev/run_dev.R")
```

## Dependencies

All dependencies are CRAN-installable. No GitHub-only or local packages are
required.

### Runtime (Imports)

| Package | Purpose |
|---------|---------|
| `shiny` | Web application framework |
| `bslib` | Bootstrap-based UI components |
| `DT` | Interactive DataTables |
| `httr2` | HTTP requests (GitHub API) |
| `jsonlite` | JSON parsing |
| `yaml` | YAML parsing/writing |
| `commonmark` | Markdown rendering |
| `xml2` | HTML sanitization for preview |
| `openssl` | JWT signing, SHA-256 hashing |
| `base64enc` | Base64 encoding (Git blobs, JWT) |
| `digest` | Hash utilities |
| `uuid` | Event ID generation |

### Development (Suggests)

| Package | Purpose |
|---------|---------|
| `golem` | Golem framework scaffolding |
| `testthat` | Unit testing |
| `shinytest2` | App-level smoke testing |
| `withr` | Test-scoped environment management |
| `rprojroot` | Project root discovery |
| `renv` | Dependency management |

### Dependency Management with renv

```r
# Restore the library from the lockfile
renv::restore()

# After adding/changing dependencies in DESCRIPTION:
renv::snapshot()
```

The `renv.lock` pins exact versions for reproducible deployment. The lockfile
targets R 4.5.2 with CRAN as the sole repository.

## Environment Variables

| Variable | Required | Purpose |
|----------|----------|---------|
| `REVIEW_APP_GH_OWNER` | Yes | GitHub repository owner |
| `REVIEW_APP_GH_REPO` | Yes | GitHub repository name |
| `REVIEW_APP_GH_DEFAULT_BRANCH` | Yes | Source branch (e.g. `main`) |
| `REVIEW_APP_GH_REVIEW_BRANCH` | Yes | Protected production data branch (`review-production`) |
| `REVIEW_APP_EXPECTED_SOURCE_COMMIT` | Yes | Qualified lowercase 40-character `main` commit required for bootstrap |
| `GITHUB_APP_ID` | Yes | Numeric GitHub App ID (not the `Iv...` Client ID) |
| `GITHUB_APP_INSTALLATION_ID` | Yes | GitHub App installation ID |
| `GITHUB_APP_PRIVATE_KEY` | Yes | Full GitHub App PEM private-key contents (Connect secret) |
| `REVIEW_APP_ROLES` | No | Absolute path to role-map YAML override |
| `REVIEW_APP_USER` | No | Identity override for local dev (no Connect) |
| `REVIEW_APP_OFFLINE` | No | Set to `1` to run without GitHub adapter |
| `GOLEM_CONFIG_ACTIVE` | No | Golem config profile (`default` / `production`) |

For CI, use only test-safe values: `REVIEW_APP_OFFLINE=1`,
`REVIEW_APP_ROLES` set to the checked-out `review-app/config/roles.yml`,
`NOT_CRAN=true`, and `GOLEM_CONFIG_ACTIVE=production` if the production
configuration profile is being exercised. Leave `REVIEW_APP_USER` unset in
CI. These settings do not represent production configuration and must not be
copied to Connect.

## Git-Backed Posit Connect Deployment

The active deployment model is Git-backed content deployment. Connect builds
the `review-app/` content item from the configured repository and branch; a
push to the configured app source branch triggers the Connect redeploy. Do not
use `rsconnect::deployApp()` or a manual bundle upload as the active production
procedure. The checked-in Publisher and `rsconnect` files are historical
metadata for an earlier manual deployment and are retained without editing:

- `review-app/.posit/publish/review-app-9KP9.toml`
- `review-app/.posit/publish/deployments/deployment-U42S.toml`
- `review-app/rsconnect/wbconnect/acastanedaa/.dcf`
- `review-app/rsconnect/wbconnect/acastanedaa/review-app.dcf`

### Prerequisites

- R version matching `renv.lock` (currently 4.5.2)
- Posit Connect with authentication enabled
- A GitHub App installed on the CVS repository
- A protected `review-production` branch created from the tested app commit
- Git-backed Connect content configured to the repository's `main` branch and
  the `review-app/` subdirectory

### Step 1: Configure Git-Backed Content

Configure or verify the Connect content item using the Connect administration
interface and record the active repository, source branch, subdirectory,
runtime, content GUID, and deployed commit in the operator attestation. The
application entry point is `review-app/app.R`. The active deployment facts must
come from Connect's API, not from historical Publisher metadata.

### Step 2: Configure Connect Secrets

Set the runtime variables and secrets in the Connect content configuration.
Keep the GitHub App private key in Connect secret storage. Never commit or
print credentials, and never expose them in an issue, workflow log, or
attestation.

### Step 3: Deploy from Git

Merge the tested app change to `main`, the branch watched by the Git-backed
Connect item. Confirm that Connect pulled the expected commit and completed the
build.
An app-code rollback is a deployment operation: restore the prior known-good
app commit through the Git-backed deployment process, or use the prior Connect
bundle if the item cannot rebuild. Changing only the review data branch does
not roll back application code.

### Step 4: Verify the Active Deployment

Use the A9 smoke procedure in the operator guide. Do not call the deployment
successful until Connect reports the active commit and the application boots
with the expected branch configuration.

## Queue Bootstrap and Recovery

An administrator starts bootstrap from the application only after
`review-production` exists and has no queue manifest. The app must show the
source commit and the expected 267 total before confirmation. Bootstrap
enumerates only `extraction/20_drafts/<module>/VAR-*.md`, validates the exact
Release A path set and counts (`9/14/24/90/61/69`), creates 267 unassigned
version-2 records, and writes the manifest and index in one protected Git
commit. A repeated bootstrap, a source-head move, a path/count mismatch, or an
incomplete payload fails without moving the production ref.

The queue dashboard reads the derived
`extraction/30_review/queue-index.yml` rather than scanning all records. Each
row identifies the artifact, source path, module, state, round, assignments,
record path/blob identity, and governance/source-drift indicators. Per-artifact
records remain the authoritative audit records. The manifest does not embed a
mutable index digest; each action locks the current queue-index blob identity.

If the index is missing or invalid, stop review writes and use the administrator
repair procedure defined in `docs/operator-guide.md`. Rebuild the index from
the authoritative v2 records and current manifest, validate the exact total,
module counts, path set, and row identities, and verify that the serialized
bytes are identical to the deterministic rebuild before publishing one
non-force repair commit. Never hand-edit a row, repair an index without a
manifest, or silently re-enroll records.

## Source Binding and Fail-Closed Writes

Every production record is bound to the enrolled source commit, Git blob SHA,
and source-content SHA-256. The app displays the enrolled snapshot while also
checking the current `main` artifact. A changed, deleted, unreadable, or
unverifiable source is drift. The app rechecks source binding and the current
queue manifest immediately before every state-changing action. Drift, API
failure, invalid queue controls, or uncertain blocker state prevents every
write, including save, submit, assignment, revision, and approval.

An unrelated `main` commit is not drift when the enrolled artifact blob and
content hash are unchanged. Approval, when enabled in Release B, uses the
enrolled immutable front matter and persisted reviewed body only.

For a data-cutover rollback, set the configured review branch back to `review`
and restart the Git-backed Connect item. Legacy calibration records remain
read-only. Leave `review-production` intact for diagnosis and never rewrite
either branch. This is separate from an application-code rollback.

## A9 Redacted Attestation

Before production cutover, record the following non-secret values exactly and
obtain deployment facts from the Connect API. Do not include GitHub App IDs,
installation IDs, private keys, or role-map contents in the attestation.

```text
REVIEW_APP_GH_OWNER=GMD-hub
REVIEW_APP_GH_REPO=GMD-canonical-schema
REVIEW_APP_GH_DEFAULT_BRANCH=main
REVIEW_APP_GH_REVIEW_BRANCH=review-production
REVIEW_APP_EXPECTED_SOURCE_COMMIT=<qualified-main-sha>
GOLEM_CONFIG_ACTIVE=production
REVIEW_APP_USER=unset
REVIEW_APP_OFFLINE=unset
REVIEW_APP_ROLES=unset
```

If a role-map override is configured, replace the final line in the redacted
operator record with `REVIEW_APP_ROLES=sha256:<roles-file-sha256>`. Never
record the override path or contents in a public issue or CI log.

See `docs/operator-guide.md` for the complete deployment runbook, including
GitHub App provisioning, branch protection, monitoring, and incident recovery.

## Testing

```r
# Run all tests
testthat::test_dir("tests/testthat")

# Run a specific test file
testthat::test_file("tests/testthat/test-models.R")

# Full package test suite
devtools::test(reporter = "summary")

# Full R CMD check (from the repository root)
R CMD check --no-manual review-app
```

The test suite covers:
- Data models and validation (V1)
- State transitions (V2)
- Authorization logic
- SHA-256 hashing with cross-language fixtures
- Front-matter immutability and preview sanitization
- Dashboard index building and filtering
- GitHub adapter reads/writes with in-memory doubles
- Atomic writes, optimistic locking, and recovery
- End-to-end action orchestration
- Full lifecycle integration test (approve, revise, reopen paths)
- App scaffold and smoke tests
- Module-level testServer tests

CI keeps the Python validation job and adds a separate `Review-app R
validation` job. The required protected-branch check names are:

- `Validate canonical schema / Python validation`
- `Validate canonical schema / Review-app R validation`

The R job restores the locked environment, runs focused queue/source-binding
tests when those files are present, runs `devtools::test()`, and runs
`R CMD check --no-manual`. It is an offline validation job; it does not connect
to GitHub or Posit Connect.

## License

MIT
