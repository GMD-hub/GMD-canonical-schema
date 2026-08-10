# Golem 01_start.R -- run once when creating the project.
# This file documents the initial Golem setup steps that were applied.
# Do NOT re-run; it is a historical record.

# 1. golem::create_golem(".") was replaced by manual restructuring of the
#    existing reviewapp package into Golem conventions.

# 2. Set up the package metadata (DESCRIPTION) -- already present.

# 3. Add the golem config file:
#    usethis::use_golem_config()  --> inst/golem-config.yml

# 4. Add the www/ directory for static assets:
#    golem::add_css_file("custom")  --> inst/app/www/custom.css

# 5. Add the dev/ scripts:
#    golem::use_dev_routine()  --> dev/01_start.R, 02_dev.R, 03_deploy.R
