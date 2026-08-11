# Human Review Application -- Shiny for R app entry point.
#
# Deployed to Posit Connect as its own content item.  All logic lives in the
# package's R/ modules so it can be unit-tested.
#
# Posit Connect does not install the local `reviewapp` package: it restores
# only the packages recorded in renv.lock, and a project-local package cannot
# be installed from the bundle.  So instead of `library(reviewapp)` we load the
# packaged source directly from the bundle with pkgload::load_all() -- golem's
# recommended entry point for Posit Connect.  This also makes
# system.file(package = "reviewapp") resolve to this bundle's inst/ directory,
# which the app relies on for golem-config.yml, the stylesheet, and the role
# map.  `pkgload` is declared in DESCRIPTION/renv.lock so Connect installs it.

options("golem.app.prod" = TRUE)

pkgload::load_all(".")

# Connect will run this file; the returned app object is served.
run_app()
