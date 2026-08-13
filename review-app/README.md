# GMD Human Review Application

A private, Git-backed Shiny for R application for the GPID team's human review
workflow. Built with the [Golem](https://thinkr-open.github.io/golem/) framework
for production-grade Shiny applications and deployed on Posit Connect.

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
│   └── testthat/            # 14 test files covering all modules
├── docs/
│   └── operator-guide.md    # Posit Connect deployment runbook
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
| `REVIEW_APP_GH_REVIEW_BRANCH` | Yes | Protected review branch (e.g. `review`) |
| `GITHUB_APP_ID` | Yes | Numeric GitHub App ID (not the `Iv...` Client ID) |
| `GITHUB_APP_INSTALLATION_ID` | Yes | GitHub App installation ID |
| `GITHUB_APP_PRIVATE_KEY` | Yes | Full GitHub App PEM private-key contents (Connect secret) |
| `REVIEW_APP_ROLES` | No | Absolute path to role-map YAML override |
| `REVIEW_APP_USER` | No | Identity override for local dev (no Connect) |
| `REVIEW_APP_OFFLINE` | No | Set to `1` to run without GitHub adapter |
| `GOLEM_CONFIG_ACTIVE` | No | Golem config profile (`default` / `production`) |

## Posit Connect Deployment

### Prerequisites

- R version matching `renv.lock` (currently 4.5.2)
- Posit Connect with authentication enabled
- A GitHub App installed on the CVS repository
- A protected review branch created

### Step 1: Build the Content Bundle

```bash
cd review-app
Rscript -e 'renv::restore()'
```

Exclude `renv/` local library, `.posit/`, and `dev/` from the bundle (already
listed in `.Rbuildignore`).

### Step 2: Publish to Connect

```r
rsconnect::deployApp(
  appDir = ".",
  appName = "gmd-human-review",
  account = "<connect-account>",
  server = "<connect-server>"
)
```

Or use the Posit Connect UI to upload the bundle with entry point `app.R`.

### Step 3: Configure Connect Secrets

Set the environment variables from the table above as Connect environment
variables or Vault secrets. The `GITHUB_APP_PRIVATE_KEY` should use Connect's
secret storage (not plain environment variables) to avoid leaking in logs.

### Step 4: Verify

1. Log in as a mapped `reviewer` -- dashboard loads with the live queue.
2. Open an artifact -- YAML renders read-only; Markdown body is editable.
3. Save-draft, then submit -- write succeeds, record visible on review branch.
4. Log in as unmapped identity -- "not authorized" message, no action buttons.

See `docs/operator-guide.md` for the complete deployment runbook, including
GitHub App provisioning, branch protection, monitoring, and incident recovery.

## Testing

```r
# Run all tests
testthat::test_dir("tests/testthat")

# Run a specific test file
testthat::test_file("tests/testthat/test-models.R")

# Full R CMD check
devtools::check()
```

The test suite (14 files) covers:
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

## License

MIT
