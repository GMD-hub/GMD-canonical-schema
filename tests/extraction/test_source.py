"""Tests for source resolution and hashing — Phase 2 Step 3."""

import copy
from pathlib import Path
import shutil
import subprocess
from unittest.mock import Mock

import pytest

import extraction_pipeline.source as source_module
from extraction_pipeline.hashing import hash_bytes, hash_file, verify_file_hash
from extraction_pipeline.source import (
    SourceResolutionError,
    resolve_source,
    resolve_source_directory,
    verify_source_hashes,
)


class TestHashing:
    def test_hash_bytes_deterministic(self) -> None:
        assert hash_bytes(b"abc") == (
            "ba7816bf8f01cfea414140de5dae2223"
            "b00361a396177a9cb410ff61f20015ad"
        )

    def test_hash_bytes_empty_and_binary_vectors(self) -> None:
        assert hash_bytes(b"") == (
            "e3b0c44298fc1c149afbf4c8996fb924"
            "27ae41e4649b934ca495991b7852b855"
        )
        assert hash_bytes(bytes(range(256))) == (
            "40aff2e9d2d8922e47afd4648e696749"
            "7158785fbd1da870e7110266bf944880"
        )

    def test_hash_file_deterministic(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("hello", encoding="utf-8")
        h1 = hash_file(f)
        h2 = hash_file(f)
        assert h1 == h2 == (
            "2cf24dba5fb0a30e26e83b2ac5b9e29"
            "e1b161e5c1fa7425e73043362938b9824"
        )

    def test_hash_file_multi_chunk_vector(self, tmp_path: Path) -> None:
        path = tmp_path / "million-a.bin"
        path.write_bytes(b"a" * 1_000_000)
        assert hash_file(path) == (
            "cdc76e5c9914fb9281a1c7e284d73e67"
            "f1809a48a497200e046d39ccc7112cd0"
        )

    def test_different_content_different_hash(self, tmp_path: Path) -> None:
        f1 = tmp_path / "a.txt"
        f2 = tmp_path / "b.txt"
        f1.write_text("alpha", encoding="utf-8")
        f2.write_text("beta", encoding="utf-8")
        assert hash_file(f1) != hash_file(f2)

    def test_verify_file_hash_match(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("abc", encoding="utf-8")
        assert verify_file_hash(
            f,
            "ba7816bf8f01cfea414140de5dae2223"
            "b00361a396177a9cb410ff61f20015ad",
        )

    def test_verify_file_hash_mismatch(self, tmp_path: Path) -> None:
        f = tmp_path / "test.txt"
        f.write_text("original", encoding="utf-8")
        assert not verify_file_hash(f, "a" * 64)

    def test_verify_file_hash_missing(self, tmp_path: Path) -> None:
        assert not verify_file_hash(tmp_path / "nonexistent.txt", "a" * 64)


class TestSourceResolution:
    def test_resolve_directory(self, source_repository: dict[str, object]) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        result = resolve_source_directory(root, manifest)
        assert result == root.resolve()

    @pytest.mark.parametrize("kind", ["missing", "file"])
    def test_invalid_repository_root(
        self,
        tmp_path: Path,
        source_repository: dict[str, object],
        kind: str,
    ) -> None:
        manifest = source_repository["manifest"]
        assert isinstance(manifest, dict)
        root = tmp_path / kind
        if kind == "file":
            root.write_text("not a repository", encoding="utf-8")
        message = "does not exist" if kind == "missing" else "not a directory"
        with pytest.raises(SourceResolutionError, match=message):
            resolve_source_directory(root, manifest)

    def test_verify_hashes_reads_all_selected_git_blobs(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        verified, all_verified = verify_source_hashes(root, manifest)
        assert [entry.path for entry in verified] == [
            "docs/source.md",
            "references/context.txt",
        ]
        assert all_verified is True

    def test_reads_explicit_commit_not_head_or_worktree(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        contents = source_repository["contents"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        assert isinstance(contents, dict)

        (root / "docs/source.md").write_bytes(b"new committed bytes\n")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(
            ["git", "commit", "--quiet", "-m", "new head"],
            cwd=root,
            check=True,
        )
        (root / "docs/source.md").write_bytes(b"uncommitted bytes\n")

        proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        assert proof.get_bytes("docs/source.md") == contents["docs/source.md"]
        assert proof.repository.commit_sha == source_repository["commit"]

    def test_changed_source_after_verification_cannot_change_proof(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        contents = source_repository["contents"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        assert isinstance(contents, dict)

        proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        (root / "docs/source.md").write_bytes(b"changed after verification\n")
        assert proof.get_bytes("docs/source.md") == contents["docs/source.md"]

    def test_hash_mismatch_raises(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        manifest["source_files"][0]["sha256"] = "a" * 64
        with pytest.raises(SourceResolutionError, match="SHA-256 mismatch"):
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")

    def test_invalid_proof_metadata_fails_as_source_resolution_error(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        with pytest.raises(SourceResolutionError, match="proof validation"):
            resolve_source(root, manifest, " ")

    def test_repository_identity_mismatch_raises(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        manifest["repository"]["url"] = "https://example.com/other/repository"
        with pytest.raises(SourceResolutionError, match="Origin repository identity"):
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")

    def test_repository_mismatch_does_not_disclose_origin_credentials(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        subprocess.run(
            [
                "git",
                "remote",
                "set-url",
                "origin",
                "https://user:SECRET@example.com/acme/source-fixture",
            ],
            cwd=root,
            check=True,
        )
        with pytest.raises(SourceResolutionError) as error:
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        assert "SECRET" not in str(error.value)

    def test_missing_path_at_commit_raises(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        manifest["source_files"][0] = {
            "path": "docs/missing.md",
            "scope": "primary",
            "sha256": "a" * 64,
        }
        with pytest.raises(SourceResolutionError, match="missing or ambiguous"):
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")

    def test_symlink_blob_is_rejected(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)

        outside = root.parent / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        link = root / "docs/link.md"
        link.symlink_to("../../outside.md")
        subprocess.run(["git", "add", "docs/link.md"], cwd=root, check=True)
        subprocess.run(
            ["git", "commit", "--quiet", "-m", "add source symlink"],
            cwd=root,
            check=True,
        )
        commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        manifest["repository"]["commit_sha"] = commit
        manifest["source_files"][0] = {
            "path": "docs/link.md",
            "scope": "primary",
            "sha256": hash_bytes(b"../../outside.md"),
        }
        with pytest.raises(SourceResolutionError, match="symlink or tree"):
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")

    def test_worktree_parent_symlink_cannot_redirect_git_object_read(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        contents = source_repository["contents"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        assert isinstance(contents, dict)

        outside = root.parent / "outside-directory"
        outside.mkdir()
        (outside / "source.md").write_bytes(b"outside bytes\n")
        shutil.rmtree(root / "docs")
        (root / "docs").symlink_to(outside, target_is_directory=True)

        proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        assert proof.get_bytes("docs/source.md") == contents["docs/source.md"]

    def test_git_replacement_refs_are_ignored(
        self,
        source_repository: dict[str, object],
    ) -> None:
        root = source_repository["root"]
        manifest = source_repository["manifest"]
        contents = source_repository["contents"]
        old_commit = source_repository["commit"]
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        assert isinstance(contents, dict)
        assert isinstance(old_commit, str)

        (root / "docs/source.md").write_bytes(b"replacement bytes\n")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(
            ["git", "commit", "--quiet", "-m", "replacement target"],
            cwd=root,
            check=True,
        )
        new_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        subprocess.run(
            ["git", "replace", old_commit, new_commit],
            cwd=root,
            check=True,
        )

        proof = resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        assert proof.get_bytes("docs/source.md") == contents["docs/source.md"]

    def test_malformed_manifest_fails_before_git_read(
        self,
        source_repository: dict[str, object],
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        root = source_repository["root"]
        manifest = copy.deepcopy(source_repository["manifest"])
        assert isinstance(root, Path)
        assert isinstance(manifest, dict)
        manifest["source_files"][0]["path"] = "../outside.md"
        git_run = Mock(side_effect=AssertionError("Git must not run"))
        monkeypatch.setattr(source_module, "_run_git", git_run)
        with pytest.raises(SourceResolutionError, match="manifest validation"):
            resolve_source(root, manifest, "2026-08-30T12:00:00Z")
        git_run.assert_not_called()
