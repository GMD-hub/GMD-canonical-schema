# Golem 03_deploy.R -- deployment helpers for Posit Connect.

# --- Pre-deployment checks ---------------------------------------------------

# 1. Ensure renv is restored:
#    renv::restore()

# 2. Run the test suite:
#    devtools::test()

# 3. Run R CMD check:
#    devtools::check()

# --- Deploy to Posit Connect -------------------------------------------------
#
# Option A: rsconnect CLI (recommended for CI/CD)
#
#   rsconnect::deployApp(
#     appDir   = ".",
#     appName  = "gmd-human-review",
#     account  = "<connect-account>",
#     server   = "<connect-server>",
#     forceUpdate = TRUE
#   )
#
# Option B: Posit Connect CLI (rsconnect-python / rsconnect-rs)
#
#   rsconnect deploy shiny . --name gmd-human-review --server <url>
#
# See docs/operator-guide.md for the full deployment runbook including
# GitHub App credential provisioning, Connect secrets, and branch protection.

# --- Post-deployment verification --------------------------------------------
#
# 1. Log in as a mapped reviewer -- dashboard should load with live queue.
# 2. Open an artifact -- YAML/evidence panels render; Markdown editor works.
# 3. Save-draft then submit -- write succeeds, record visible on review branch.
# 4. Log in as unmapped identity -- "not authorized" message, no action buttons.
