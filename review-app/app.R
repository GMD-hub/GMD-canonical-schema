# Human Review Application -- Shiny for R app entry point.
#
# Deployed to Posit Connect as its own content item. All logic lives in the
# package's R/ modules so it can be unit-tested.

library(reviewapp)

# Connect will run this file; the returned app object is served.
reviewapp::shiny_review_app()
