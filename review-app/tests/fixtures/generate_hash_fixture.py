#!/usr/bin/env python3
"""Generate PY_REFERENCE_SHA256 for the cross-language hash fixture.

This script hashes review-app/tests/fixtures/hash_fixture.txt using the
repository's Python SHA-256 helper (extraction_pipeline/hashing.py) and prints
the resulting lowercase-hex digest. The output is hard-coded as the constant
PY_REFERENCE_SHA256 at the top of
review-app/tests/testthat/test-hashing.R.

Regenerate procedure (when the digest format or fixture bytes change):
  1. Ensure the fixture file bytes are final.
  2. Run:  python3 review-app/tests/fixtures/generate_hash_fixture.py
  3. Copy the printed digest into PY_REFERENCE_SHA256 in test-hashing.R
     in the same commit.
  4. Update the "generated at" comment below and in test-hashing.R.

Run from the repository root.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from extraction_pipeline.hashing import hash_file


def main() -> None:
    fixture = (
        pathlib.Path(__file__).resolve().parent / "hash_fixture.txt"
    )
    digest = hash_file(fixture)
    print(digest)


if __name__ == "__main__":
    main()
