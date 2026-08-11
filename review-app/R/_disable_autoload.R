# Shiny autoload guard (golem convention).
#
# With `app.R` at the package root, Shiny's `loadSupport()` would otherwise
# source every file in this R/ directory BEFORE evaluating app.R, duplicating
# the package definitions that app.R loads via pkgload::load_all() (see
# `?loadSupport` -- a file named `_disable_autoload.R` here disables R/
# auto-sourcing and its "appears to contain an R package" warning). This file
# is intentionally empty; it must not be removed.
