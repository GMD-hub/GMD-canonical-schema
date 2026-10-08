"""
Download UIS ISCED country mapping workbooks in batch.

Source:
https://www.uis.unesco.org/en/methods-and-tools/isced/mapping-and-diagrams?hub=12

Install:
    pip install requests beautifulsoup4
"""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urljoin, unquote, urlparse
import argparse
import html
import re
import time
import warnings

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import SSLError
from urllib3.exceptions import InsecureRequestWarning
from urllib3.util.retry import Retry


# ============================================================
# SETTINGS
# ============================================================

INDEX_URL = "https://www.uis.unesco.org/en/methods-and-tools/isced/mapping-and-diagrams?hub=12"

# Save into the ISCED folder where this script lives
OUTPUT_DIR = Path(__file__).resolve().parent

# Seconds between downloads
DOWNLOAD_DELAY = 0.5

# If True, existing files will not be downloaded again
SKIP_EXISTING = True

# If True, only download ISCED 2011 country mapping files
ONLY_ISCED_2011 = True

# If TLS verification fails (common behind corporate SSL interception),
# retry once with verify=False so batch download can continue.
ALLOW_INSECURE_SSL_FALLBACK = True


# ============================================================
# REQUEST SESSION
# ============================================================

session = requests.Session()

retry_strategy = Retry(
    total=5,
    connect=5,
    read=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("https://", adapter)
session.mount("http://", adapter)

session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 Chrome/131 Safari/537.36"
        )
    }
)


def _session_get(url, **kwargs):
    try:
        return session.get(url, **kwargs)
    except SSLError as exc:
        if ALLOW_INSECURE_SSL_FALLBACK and session.verify is not False:
            print(
                "[WARN] SSL verification failed. "
                "Retrying with verify=False (insecure)."
            )
            print(f"       {exc}")
            warnings.simplefilter("ignore", InsecureRequestWarning)
            session.verify = False
            return session.get(url, **kwargs)
        raise


# ============================================================
# FIND COUNTRY MAPPING LINKS
# ============================================================

def _extract_filename_from_url(url: str) -> str:
    path = urlparse(url).path
    name = Path(unquote(path)).name
    name = html.unescape(name).strip()

    # Windows-safe filename cleanup
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    return name


def _is_mapping_link(url: str) -> bool:
    lower = unquote(url).lower()
    if not lower.endswith((".xlsx", ".xls")):
        return False
    return "isced mapping" in lower


def _is_target_file(filename: str, only_2011: bool) -> bool:
    lower = filename.lower()

    if not lower.endswith((".xlsx", ".xls")):
        return False

    if only_2011:
        return lower.startswith("isced_2011_mapping_")

    return lower.startswith("isced_") and "_mapping_" in lower


def get_mapping_links(only_2011: bool = True) -> dict[str, str]:
    print(f"Reading mapping index:\n{INDEX_URL}\n")

    response = _session_get(INDEX_URL, timeout=60)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links: dict[str, str] = {}

    for a in soup.find_all("a", href=True):
        full_url = urljoin(INDEX_URL, a["href"])

        if not _is_mapping_link(full_url):
            continue

        filename = _extract_filename_from_url(full_url)

        if not _is_target_file(filename, only_2011=only_2011):
            continue

        # Keep first occurrence (page contains duplicates).
        links.setdefault(filename, full_url)

    return dict(sorted(links.items(), key=lambda kv: kv[0].lower()))


# ============================================================
# DOWNLOAD ONE FILE
# ============================================================

def download_one(filename: str, url: str):
    output_file = OUTPUT_DIR / filename

    if SKIP_EXISTING and output_file.exists():
        print(f"[SKIP] {filename}")
        return "skipped", output_file

    with _session_get(
        url,
        stream=True,
        timeout=(30, 300),
    ) as response:
        response.raise_for_status()

        temp_file = output_file.with_suffix(output_file.suffix + ".part")

        total_bytes = 0

        with open(temp_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    total_bytes += len(chunk)

    with open(temp_file, "rb") as f:
        beginning = f.read(8)

    lower_name = output_file.name.lower()

    if lower_name.endswith(".xlsx") and beginning[:2] != b"PK":
        temp_file.unlink(missing_ok=True)
        raise ValueError("Downloaded file does not appear to be a valid XLSX file.")

    if lower_name.endswith(".xls") and beginning[:4] != bytes.fromhex("D0CF11E0"):
        temp_file.unlink(missing_ok=True)
        raise ValueError("Downloaded file does not appear to be a valid XLS file.")

    temp_file.replace(output_file)

    mb = total_bytes / (1024 * 1024)
    print(f"[OK]   {filename} ({mb:.2f} MB)")
    return "downloaded", output_file


# ============================================================
# MAIN
# ============================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="Download UIS ISCED country mapping files in batch."
    )
    parser.add_argument(
        "--all-versions",
        action="store_true",
        help="Download all mapping versions found (not just ISCED 2011).",
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="List discovered files without downloading.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    only_2011 = not args.all_versions
    links = get_mapping_links(only_2011=only_2011)

    print(
        f"Found {len(links)} country mapping file(s) "
        f"({'ISCED 2011 only' if only_2011 else 'all versions'}).\n"
    )

    if args.list_only:
        for name, url in links.items():
            print(f"{name}\t{url}")
        return

    downloaded = 0
    skipped = 0
    failed = []

    items = list(links.items())

    for i, (filename, url) in enumerate(items, start=1):
        print(f"[{i}/{len(items)}] {filename}")

        try:
            status, _ = download_one(filename, url)

            if status == "downloaded":
                downloaded += 1
            elif status == "skipped":
                skipped += 1

        except Exception as exc:  # noqa: BLE001
            print(f"[FAIL] {filename}: {exc}")
            failed.append({"file": filename, "url": url, "error": str(exc)})

        time.sleep(DOWNLOAD_DELAY)

    print("\n" + "=" * 60)
    print("DOWNLOAD COMPLETE")
    print("=" * 60)
    print(f"Found:      {len(items)}")
    print(f"Downloaded: {downloaded}")
    print(f"Skipped:    {skipped}")
    print(f"Failed:     {len(failed)}")
    print(f"\nFiles saved to:\n{OUTPUT_DIR.resolve()}")

    if failed:
        failed_file = OUTPUT_DIR / "failed_isced_downloads.txt"
        with open(failed_file, "w", encoding="utf-8") as f:
            for x in failed:
                f.write(f"{x['file']}\t{x['url']}\t{x['error']}\n")

        print("\nFailed downloads written to:")
        print(failed_file)


if __name__ == "__main__":
    main()
