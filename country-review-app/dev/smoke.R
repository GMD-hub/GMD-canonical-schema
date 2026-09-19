source(file.path("country-review-app", "R", "run.R"))
q <- build_country_queue_index(include_benchmarks = TRUE)
cat("rows=", nrow(q), "\n", sep = "")
cat("digest=", attr(q, "membership_digest"), "\n", sep = "")
