#!/usr/bin/env bash
# End-to-end demo. Point WORKBOOKS at a folder of source files.
set -e
WORKBOOKS="${1:-.}"
python3 -m gmd_wash_concordance bulk "$WORKBOOKS" --out out/
echo
echo "artefacts under out/"
find out -type f | sort
