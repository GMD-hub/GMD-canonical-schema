# Golem 02_dev.R -- development workflow helpers.
# Source this file during active development for common tasks.

# --- Load the package in development mode ------------------------------------
# pkgload::load_all() makes all R/ functions available without installing.
# Equivalent to devtools::load_all().
pkgload::load_all()

# --- Run the app locally -----------------------------------------------------
# Opens the app in a browser for interactive development.
# reviewapp::run_app()

# --- Run tests ---------------------------------------------------------------
# testthat::test_dir("tests/testthat")
# testthat::test_file("tests/testthat/test-models.R")

# --- Generate documentation --------------------------------------------------
# roxygen2::roxygenise()   -- regenerate NAMESPACE and man/ from roxygen tags

# --- Check the package -------------------------------------------------------
# devtools::check()        -- full R CMD check
# devtools::test()         -- run testthat suite

# --- Update renv lockfile after adding/changing dependencies -----------------
# renv::snapshot()         -- record current state of the library
# renv::restore()          -- restore library from renv.lock
