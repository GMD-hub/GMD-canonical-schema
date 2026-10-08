# Country input review app entry point.

run_candidates <- c(
	file.path("R", "run.R"),
	file.path("country-review-app", "R", "run.R")
)
run_path <- run_candidates[file.exists(run_candidates)][1]
if (is.na(run_path)) {
	stop(sprintf("Unable to locate run.R from working directory: %s", getwd()))
}

source(run_path)
run_app()
