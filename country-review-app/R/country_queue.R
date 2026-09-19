# Queue discovery and indexing for country-input artifacts.

COUNTRY_DRAFT_ROOT <- file.path(
  "extraction", "20_drafts", "runs", "country-parameters"
)
BENCHMARK_ROOT <- file.path("governance", "benchmarks")

raw_to_hex <- function(raw_value) {
  paste(sprintf("%02x", as.integer(raw_value)), collapse = "")
}

queue_membership_digest <- function(index_df) {
  if (!nrow(index_df)) return(raw_to_hex(openssl::sha256(charToRaw(""))))
  keys <- paste(index_df$artifact_id, index_df$source_artifact_path, sep = "|")
  payload <- paste(sort(keys), collapse = "\n")
  raw_to_hex(openssl::sha256(charToRaw(payload)))
}

read_yaml_safe <- function(path) {
  tryCatch(
    yaml::read_yaml(path),
    error = function(error) {
      list(`_parse_error` = conditionMessage(error))
    }
  )
}

index_country_artifact <- function(path, include_benchmarks = TRUE) {
  parsed <- read_yaml_safe(path)
  artifact_type <- detect_artifact_type_from_path(path, parsed)
  if (is.null(artifact_type)) return(NULL)
  if (!include_benchmarks && identical(artifact_type, "benchmark")) return(NULL)

  iso3 <- extract_iso3_from_path(path, parsed)
  artifact_id <- build_artifact_id(path, artifact_type, iso3)

  status <- parsed$status %||% if (identical(artifact_type, "benchmark")) "reference" else "draft"
  provenance_flag <- NA
  if (identical(artifact_type, "parameter") && is.list(parsed$parameters) && length(parsed$parameters)) {
    first <- parsed$parameters[[1L]]
    provenance_flag <- isTRUE(first$provenance$human_reviewed %||% FALSE)
  }

  data.frame(
    artifact_id = artifact_id,
    artifact_type = artifact_type,
    iso3 = iso3,
    status = as.character(status),
    source_artifact_path = gsub("\\\\", "/", path),
    read_only = identical(artifact_type, "benchmark"),
    parse_error = parsed$`_parse_error` %||% NA_character_,
    human_reviewed = provenance_flag,
    stringsAsFactors = FALSE
  )
}

country_draft_paths <- function(root = COUNTRY_DRAFT_ROOT) {
  if (!dir.exists(root)) return(character(0))
  list.files(root, pattern = "[.]yaml$", recursive = TRUE, full.names = TRUE)
}

benchmark_paths <- function(root = BENCHMARK_ROOT) {
  if (!dir.exists(root)) return(character(0))
  list.files(root, pattern = "_benchmark_draft[.]yaml$", recursive = FALSE, full.names = TRUE)
}

build_country_queue_index <- function(include_benchmarks = TRUE) {
  paths <- country_draft_paths()
  if (include_benchmarks) {
    paths <- c(paths, benchmark_paths())
  }
  rows <- Filter(Negate(is.null), lapply(paths, index_country_artifact, include_benchmarks = include_benchmarks))
  if (!length(rows)) {
    empty <- data.frame(
      artifact_id = character(0),
      artifact_type = character(0),
      iso3 = character(0),
      status = character(0),
      source_artifact_path = character(0),
      read_only = logical(0),
      parse_error = character(0),
      human_reviewed = logical(0),
      stringsAsFactors = FALSE
    )
    attr(empty, "membership_digest") <- queue_membership_digest(empty)
    return(empty)
  }
  output <- do.call(rbind, rows)
  row.names(output) <- NULL
  attr(output, "membership_digest") <- queue_membership_digest(output)
  output
}
