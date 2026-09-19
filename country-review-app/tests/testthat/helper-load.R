find_existing_path <- function(candidates) {
  hits <- candidates[file.exists(candidates)]
  if (!length(hits)) return(NULL)
  hits[[1L]]
}

find_helper_path <- function() {
  candidates <- c(
    file.path("country-review-app", "tests", "testthat", "helper-load.R"),
    file.path("tests", "testthat", "helper-load.R"),
    "helper-load.R"
  )
  path <- find_existing_path(candidates)
  if (is.null(path)) {
    stop(sprintf(
      "Unable to locate helper-load.R from current directory: %s",
      getwd()
    ))
  }
  path
}

app_root <- function() {
  cwd <- normalizePath(getwd(), winslash = "/", mustWork = TRUE)
  candidates <- c(
    file.path(cwd, "country-review-app"),
    cwd,
    dirname(cwd),
    dirname(dirname(cwd)),
    dirname(dirname(dirname(cwd)))
  )
  candidates <- unique(candidates)
  for (root in candidates) {
    if (file.exists(file.path(root, "R", "models.R")) &&
        file.exists(file.path(root, "tests", "testthat", "helper-load.R"))) {
      return(root)
    }
    if (file.exists(file.path(root, "country-review-app", "R", "models.R")) &&
        file.exists(file.path(root, "country-review-app", "tests", "testthat", "helper-load.R"))) {
      return(file.path(root, "country-review-app"))
    }
  }
  stop(sprintf(
    "Unable to locate country-review-app root from current directory: %s",
    cwd
  ))
}

app_source <- function(relative_path) {
  source(file.path(app_root(), relative_path), local = parent.frame())
}
