"""SHA-256 hashing for source files — Phase 2 Step 3."""

import hashlib
from pathlib import Path


def hash_file(path: Path, chunk_size: int = 65536) -> str:
    """Return the SHA-256 hex digest of a file's contents."""
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def hash_bytes(data: bytes) -> str:
    """Return the SHA-256 hex digest of byte content."""
    return hashlib.sha256(data).hexdigest()


def verify_file_hash(path: Path, expected_sha256: str) -> bool:
    """Verify a file matches its expected SHA-256 hash."""
    if not path.exists():
        return False
    actual = hash_file(path)
    return actual == expected_sha256
