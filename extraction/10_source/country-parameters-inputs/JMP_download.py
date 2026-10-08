"""
Download all JMP/WASH household Excel files for all countries.

Source:
https://washdata.org/data/downloads

Install:
    pip install requests beautifulsoup4
"""

from pathlib import Path
from urllib.parse import urljoin
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

INDEX_URL = "https://washdata.org/data/downloads"

# Change this to wherever you want the files
OUTPUT_DIR = Path(r"c:\Users\wb327173\OneDrive - WBG\Downloads\ECA\DEC\AI harmonization\Concordance\JMP")

# Seconds between downloads -- polite to the server
DOWNLOAD_DELAY = 0.5

# If True, existing files will not be downloaded again
SKIP_EXISTING = True

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
# FIND ALL HOUSEHOLD COUNTRY LINKS
# ============================================================

def get_household_links():

    print(f"Reading download index:\n{INDEX_URL}\n")

    response = _session_get(INDEX_URL, timeout=60)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Example:
    # /data/country/BGD/household/download
    pattern = re.compile(
        r"/data/country/([A-Za-z0-9]{3})/household/download/?$",
        re.IGNORECASE,
    )

    countries = {}

    for link in soup.find_all("a", href=True):

        full_url = urljoin(INDEX_URL, link["href"])

        match = pattern.search(full_url)

        if match:
            iso3 = match.group(1).upper()

            countries[iso3] = full_url

    return dict(sorted(countries.items()))


# ============================================================
# GET SERVER FILE NAME
# ============================================================

def get_filename(response, iso3):

    content_disposition = response.headers.get(
        "Content-Disposition", ""
    )

    # Try filename*=UTF-8''...
    match = re.search(
        r"filename\*=UTF-8''([^;]+)",
        content_disposition,
        re.IGNORECASE,
    )

    if match:
        from urllib.parse import unquote
        return unquote(match.group(1)).strip("\"'")

    # Try normal filename=
    match = re.search(
        r'filename="?([^";]+)"?',
        content_disposition,
        re.IGNORECASE,
    )

    if match:
        return match.group(1).strip()

    # Safe fallback
    return f"{iso3}_household.xlsx"


# ============================================================
# DOWNLOAD ONE COUNTRY
# ============================================================

def download_country(iso3, url):

    with _session_get(
        url,
        stream=True,
        timeout=(30, 300),
    ) as response:

        response.raise_for_status()

        filename = get_filename(response, iso3)

        # Make sure it has an Excel extension
        if not filename.lower().endswith((".xlsx", ".xls")):
            filename += ".xlsx"

        # Prefix with ISO3 if the server filename does not contain it
        if iso3.lower() not in filename.lower():
            filename = f"{iso3}_{filename}"

        output_file = OUTPUT_DIR / filename

        if SKIP_EXISTING and output_file.exists():
            print(
                f"[SKIP] {iso3}: "
                f"{output_file.name}"
            )
            return "skipped", output_file

        # Download first to temporary file
        temp_file = output_file.with_suffix(
            output_file.suffix + ".part"
        )

        total_bytes = 0

        with open(temp_file, "wb") as f:

            for chunk in response.iter_content(
                chunk_size=1024 * 1024
            ):
                if chunk:
                    f.write(chunk)
                    total_bytes += len(chunk)

        # Basic check for accidental HTML/error pages
        with open(temp_file, "rb") as f:
            beginning = f.read(4)

        # XLSX files are ZIP containers and normally start with PK
        if output_file.suffix.lower() == ".xlsx":
            if beginning[:2] != b"PK":
                temp_file.unlink(missing_ok=True)
                raise ValueError(
                    "Downloaded file does not appear "
                    "to be a valid XLSX file."
                )

        temp_file.replace(output_file)

        mb = total_bytes / (1024 * 1024)

        print(
            f"[OK]   {iso3}: "
            f"{output_file.name} "
            f"({mb:.2f} MB)"
        )

        return "downloaded", output_file


# ============================================================
# MAIN
# ============================================================

def main():

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    countries = get_household_links()

    print(
        f"Found {len(countries)} "
        "country household files.\n"
    )

    downloaded = 0
    skipped = 0
    failed = []

    for i, (iso3, url) in enumerate(
        countries.items(),
        start=1,
    ):

        print(
            f"[{i}/{len(countries)}] "
            f"{iso3}"
        )

        try:

            status, _ = download_country(
                iso3,
                url,
            )

            if status == "downloaded":
                downloaded += 1

            elif status == "skipped":
                skipped += 1

        except Exception as e:

            print(
                f"[FAIL] {iso3}: {e}"
            )

            failed.append(
                {
                    "iso3": iso3,
                    "url": url,
                    "error": str(e),
                }
            )

        time.sleep(DOWNLOAD_DELAY)

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print("\n" + "=" * 60)

    print("DOWNLOAD COMPLETE")

    print("=" * 60)

    print(f"Found:      {len(countries)}")
    print(f"Downloaded: {downloaded}")
    print(f"Skipped:    {skipped}")
    print(f"Failed:     {len(failed)}")

    print(
        f"\nFiles saved to:\n"
        f"{OUTPUT_DIR.resolve()}"
    )

    if failed:

        failed_file = (
            OUTPUT_DIR /
            "failed_downloads.txt"
        )

        with open(
            failed_file,
            "w",
            encoding="utf-8",
        ) as f:

            for x in failed:

                f.write(
                    f"{x['iso3']}\t"
                    f"{x['url']}\t"
                    f"{x['error']}\n"
                )

        print(
            "\nFailed downloads written to:"
        )

        print(failed_file)


if __name__ == "__main__":
    main()