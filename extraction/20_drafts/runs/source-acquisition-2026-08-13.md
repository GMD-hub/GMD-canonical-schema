---
date: 2026-08-14
plan: 2026-08-13-complete-non-welfare-extraction
source-commit: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
---

# Source Acquisition Report

## Resolved source path

`~/Documents/projects_WBG/GMD/GMD-guidelines/` (local sibling repo, used read-only).

Portable acquisition path (independent of the originating machine):
```
git clone https://github.com/GMD-hub/GMD-guidelines.git
cd GMD-guidelines
git checkout d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
```

## Verification

- Commit on `main`: `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` (matches pinned approved revision).
- Chapters present: chapter1-INTRO ... chapter8-CONS, plus docs/GMD_household_survey_harmonization.md.
- Chapters 2-7 confirmed for extraction; chapter 8 (CONS) is welfare-excluded.
- Per-chapter sha256 recorded in `source-lock-2026-08-13.md`.

## Outcome

Source used read-only at sibling repo path. No clone/copy executed (not needed).
Chapter-file existence verified; no missing chapters.
