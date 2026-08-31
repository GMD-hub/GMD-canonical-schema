---
date: 2026-08-06
title: "Windows Platform Test Failures: Line Endings, Symlinks, and Path Resolution"
category: "testing-patterns"
language: "Python"
tags: ["windows", "cross-platform", "testing", "pytest", "pathlib", "line-endings"]
root-cause: "Windows-specific behavior in write_text (line ending translation), symlink creation (requires elevated privileges), and Path.resolve() (prepends drive letter)"
severity: "P2"
---

# Windows Platform Test Failures: Line Endings, Symlinks, and Path Resolution

## Problem

Three test failures occurred on Windows that passed on Linux/macOS:

1. `test_multiline_excerpt_bounds` — Excerpt "line 2\nline 3" not found in source file
2. `test_symlink_escape` — OSError: `[WinError 1314] A required privilege is not held by the client`
3. `test_resolve_output_path` and `test_resolve_output_path_empty_filename` — Path comparison failed due to drive letter prefix

## Root Cause

### 1. Line Ending Translation
Python's `Path.write_text()` translates `\n` to `\r\n` on Windows. When a test writes `"line 1\nline 2\nline 3\nline 4\n"` with `write_text`, the file contains `line 1\r\nline 2\r\nline 3\r\nline 4\r\n`. A subsequent `find("line 2\nline 3")` fails because the search string uses Unix line endings.

### 2. Symlink Privileges
Windows requires elevated privileges (or Developer Mode enabled) to create symbolic links. Tests that create symlinks fail with `OSError: [WinError 1314]` on standard Windows environments.

### 3. Path.resolve() Drive Letter
On Windows, `Path("/workspace/...").resolve()` prepends the current drive letter (e.g., `E:/workspace/...`). Tests comparing resolved paths against hardcoded Unix-style paths fail because `E:/workspace/...` != `/workspace/...`.

## Solution

### Fix 1: Use write_bytes for Binary-Exact Content
```python
# Before (fails on Windows)
source = "line 1\nline 2\nline 3\nline 4\n"
(tmp_path / "ch.qmd").write_text(source, encoding="utf-8")

# After (works on all platforms)
source = b"line 1\nline 2\nline 3\nline 4\n"
(tmp_path / "ch.qmd").write_bytes(source)
```

### Fix 2: Skip Symlink Tests on Windows
```python
import sys
import pytest

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Windows requires elevated privileges for symlink creation",
)
def test_symlink_escape(self, tmp_path: Path) -> None:
    ...
```

### Fix 3: Compare Path Parts Instead of Full Paths
```python
# Before (fails on Windows)
expected = Path("/workspace/extraction/20_drafts/runs/exec-abc123/inventory/inventory.json")
assert path == expected

# After (works on all platforms)
expected_parts = (
    "workspace", "extraction", "20_drafts", "runs",
    "exec-abc123", "inventory", "inventory.json",
)
# On Windows, resolve() prepends drive letter; compare only path parts
assert path.parts[-len(expected_parts):] == expected_parts
```

## Prevention

1. **Use `write_bytes` when line endings matter**: If a test depends on exact byte content (e.g., excerpt matching, hash verification), use `write_bytes` to avoid platform-specific line ending translation.

2. **Skip platform-specific tests**: Use `@pytest.mark.skipif(sys.platform == "win32", reason="...")` for tests that depend on Unix-only features (symlinks, file permissions, etc.).

3. **Compare path components, not full paths**: When testing path resolution, compare `path.parts[-N:]` instead of `path == expected` to handle Windows drive letters.

4. **Use PurePosixPath for cross-platform path strings**: If you need to compare path strings, use `path.as_posix()` and normalize the expected path.

## Related

- Python documentation: [`pathlib.Path.write_text`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text)
- Python documentation: [`pathlib.Path.resolve`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve)
- pytest documentation: [`skipif`](https://docs.pytest.org/en/latest/reference/reference.html#pytest-mark-skipif)
- [Fail-closed deterministic promotion](../data-quality/2026-08-26-fail-closed-deterministic-promotion.md)
