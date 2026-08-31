# GMD Human Review Application

A private, Git-backed Shiny for R application for the GPID team's human review
workflow. Built with the [Golem](https://thinkr-open.github.io/golem/) framework
for production-grade Shiny applications and deployed on Posit Connect.

## Queue Contract

Versioned queues use authoritative v2 review records and one immutable
`queue-descriptor.yml`. The descriptor records the queue ID, source revision,
creation actor/time, expected record count, and digest of the immutable record
identities. Dashboard state is derived from batched record reads. No mutable
global queue index participates in a review action.

The preserved `review` calibration branch remains read-only. Existing
production-v2 queues that still contain `queue-manifest.yml` and
`queue-index.yml` are supported through a temporary read adapter. The old index
is not authoritative and is not changed by review actions.

Queue initialization and migration are authenticated operator functions, not
Shiny controls. Both operations publish one non-force atomic Git commit.
Initialization rejects any non-placeholder file in the review or approved
namespace. Migration validates every source and record identity and leaves all
record blobs unchanged.

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
│   ├── queue_manifest.R     # Queue descriptor and compatibility contracts
│   ├── source_binding.R     # Immutable source and drift checks
│   ├── enrollment.R         # Operator-only initialization and migration
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
| `REVIEW_APP_GH_REVIEW_BRANCH` | Yes | Protected review data branch |
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

## Queue Initialization and Migration

`initialize_review_queue()` requires an authenticated administrator, an
explicit immutable source revision, a queue ID, and an empty review/approved
namespace. It also requires an independent expected record count and source
path-set digest. It discovers generic `VAR-*.md` draft paths, creates
source-bound v2 records, creates the minimal descriptor, and publishes one
atomic commit.

`migrate_review_queue()` accepts an existing production-v2 queue. It validates
the old immutable manifest fields, legacy index consistency, all v2 records,
and the record set. It then adds the descriptor and removes the old manifest
and index in one forward-only commit. Tests use only in-memory adapters and
temporary repositories. Operators must never use production as a test target.

Production-v2 compatibility is read-only until migration. Approval and v2
reopen remain unavailable until the sequential Task D and Task E changes
install their complete server-side gates.

## Source Binding and Fail-Closed Writes

Every production record is bound to the enrolled source commit, Git blob SHA,
and source-content SHA-256. The app displays the enrolled snapshot while also
checking the current source artifact. A changed, deleted, unreadable, or
unverifiable source is structured drift. The app rechecks source binding and
the current queue descriptor immediately before every state-changing action.
Drift, API failure, or invalid queue controls prevents every
write, including save, submit, assignment, revision, and approval.

An unrelated source-branch commit is not drift when the enrolled artifact blob
and content hash are unchanged. Approval uses the enrolled immutable front
matter and persisted reviewed body only, and remains blocked when drift is not
resolved.

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
REVIEW_APP_GH_REVIEW_BRANCH=<protected-review-branch>
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
