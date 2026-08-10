---
name: golem-skill-app-builder
description: "Composite skill for building golem Shiny applications. Handles creating golem apps, adding modules, adding functions, checking apps, running tests, and fixing missing namespaces. Triggers on: - \"build a golem app\" - \"create a shiny app with golem\" - \"develop a golem application\" - any golem-related task"
---

# Golem App Builder

Composite skill for golem Shiny application development. This skill bundles
all golem-specific workflows following R package best practices and golem
conventions from ThinkR.

## Workflows

| Task | Reference |
|------|-----------|
| Create App | [Create Golem](references/create-golem.md) |
| Add Module | [Add Module](references/add-module.md) |
| Add Function | [Add Function](references/add-function.md) |
| Check App | [Check App](references/check-app.md) |
| Run Tests | [Run Tests](references/run-tests.md) |
| Fix Missing ns() | [Check Namespaces](references/check-ns.md) |

## Key Commands

```r
# Launch the app
Rscript -e "golem::run_dev()"

# Run tests
Rscript -e "devtools::test()"

# Check package
Rscript -e "devtools::check()"

# Regenerate documentation
Rscript -e "devtools::document()"

# Format code
air format .
```

## Requirements

- R 4.0+
- `{golem}` package
- `{devtools}` package
- `{shiny}` package