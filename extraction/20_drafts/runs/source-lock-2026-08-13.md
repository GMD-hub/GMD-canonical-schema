---
date: 2026-08-14
plan: 2026-08-13-complete-non-welfare-extraction
source-commit: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1
---

# Source Lock Report

Resolved source: `/Users/acastanedaa/Documents/projects_WBG/GMD/GMD-guidelines/`
(resolved from AGENTS.md source-of-truth GMD-hub/GMD-guidelines).

Portable acquisition path (machine-independent):
`git clone https://github.com/GMD-hub/GMD-guidelines.git && cd GMD-guidelines && git checkout d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`. The per-chapter sha256 below ensures integrity once obtained.

- Commit: `d46dc03d253764ad7bdef53f625d54fd2a0a9ea1` on `main` (verified against pinned revision).
- Used read-only at sibling repo path; no clone/copy required.

## Chapter sha256 (chapters 2-8)

| Chapter | sha256 |
|---------|--------|
| chapter2-IDN.qmd | 5e25f7bc25031e102f8152feab8236c6384f1a3a438fcfb4e9d7b85f16da3e39 |
| chapter3-GEO.qmd | 850d635bb2cb36703e756d307e24cf33c94101e95c6ba5b9027fb44f1044e32e |
| chapter4-DEM.qmd | f091a0c110d931b911799618005a31dab9375794f68aca270653f9dc5d07acd0 |
| chapter5-LMR.qmd | c46796103d86412daf8d38bd56fbe118e669aa319d7948822a3476239c6d0d40 |
| chapter6-UTL.qmd | e8cb9818dd8c69317e7bb752d7afab9d6d3bc60c22526a72f751fe449bea1ba0 |
| chapter7-DWL.qmd | 3d881952d4ec0f21c88fd31101a0b0224681a19a7a1a7ec822f8bdab9d700743 |
| chapter8-CONS.qmd | 1fc00a05f15422d7217c41147df24dc76f82417f8fc3c725889ef97354946b31 (WELFARE - excluded) |

## Manifest lock (SUPERVISED - agent did not write to extraction/config/)

The values above are proposed for `extraction/config/source-manifest.v1.yaml`:
- `commit_sha: d46dc03d253764ad7bdef53f625d54fd2a0a9ea1`
- per-file sha256 for chapters 2-7 as in the table above.
- chapter 8 recorded in the welfare exclusion ledger.

A human/GPID team member must apply this lock. Agent did not modify `extraction/config/`.
