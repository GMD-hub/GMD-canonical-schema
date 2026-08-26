"""Supported command-line gate for extraction source identity."""

import argparse
from collections.abc import Callable, Sequence
from datetime import UTC, datetime
from pathlib import Path

from loguru import logger

from extraction_pipeline.preflight import PreflightError, run_preflight
from extraction_pipeline.source import SourceResolutionError, resolve_source


Clock = Callable[[], datetime]


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Verify extraction source identity")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--governance", type=Path, required=True)
    parser.add_argument("--checkout", type=Path, required=True)
    return parser


def run(argv: Sequence[str] | None = None, clock: Clock | None = None) -> int:
    """Run preflight before source resolution and return a process exit code."""
    args = _parser().parse_args(argv)
    try:
        manifest = run_preflight(args.manifest, args.governance)
        now = (clock or (lambda: datetime.now(UTC)))()
        resolved_at = now.astimezone(UTC).isoformat().replace("+00:00", "Z")
        resolve_source(args.checkout, manifest, resolved_at)
    except (PreflightError, SourceResolutionError) as exc:
        logger.error("Extraction source gate failed: {}", exc)
        return 1
    except Exception as exc:
        logger.error("Unexpected extraction source gate failure: {}", exc)
        return 1
    logger.info("Extraction source gate passed", checkout=str(args.checkout))
    return 0


def main() -> int:
    """CLI entry point."""
    return run()


if __name__ == "__main__":
    raise SystemExit(main())
