"""
gmd_edu_concordance.viewer
==========================
The review app.  Three ways to get data into the same page.

**Serve a folder** -- the one to use while iterating.  A loopback HTTP server
re-reads the output directory on *every* request, so re-running the extractor
and hitting reload shows the new output.  Nothing is cached and nothing is
baked in::

    python3 -m gmd_edu_concordance viewer out/ --serve

**Pick a folder** -- the static page with no server.  Open it, choose a
country folder (or the whole ``out/`` tree) and the browser reads the
``*_view.json`` files directly.  Chromium also gets a real *reload from disk*
button, because the directory handle is kept::

    python3 -m gmd_edu_concordance viewer --picker --out review.html

When it is serving, the page can also **edit and approve**. An edit is a patch
beside the extract, never a rewrite of it; an approval names a person, pins the
fingerprint they were looking at and carries their written acknowledgement of
every warning. Both are refused unless the server is the one serving that
folder, so the frozen and folder-picked pages stay read-only by construction.

**Freeze a snapshot** -- for sending to someone who has neither Python nor the
files.  The bundles are inlined and the page needs nothing at all::

    python3 -m gmd_edu_concordance viewer out/ --embed --out review.html

The page is the same in all three cases, so what a focal point opens is what
you were looking at.
"""
from __future__ import annotations

import json
import os
import posixpath
import socket
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, List, Optional
from urllib.parse import parse_qs, urlparse

from . import review as RV

HERE = os.path.join(os.path.dirname(__file__), "data")

# Only these ever leave the machine, and only from under the served root.
READABLE = {".json", ".yaml", ".yml", ".csv", ".txt", ".md"}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
__CSS__
</style>
</head>
<body>
<div class="top">
  <div class="brand"><span class="dot"></span>GMD country concordance</div>
  <span class="tag" id="sys">—</span>
  <div class="tabs" id="countries"></div>
  <div class="tabs" id="domains"></div>
  <span class="spacer"></span>
  <div class="src" id="srcbar"></div>
  <button class="btn" id="themebtn">theme</button>
</div>
<div class="wrap">
  <div id="gate"></div>
  <div class="cols" id="cols" hidden>
    <div id="main"></div>
    <div id="side"></div>
  </div>
</div>
<script>
window.__MODE__ = "__VIEWMODE__";
window.__BUNDLES__ = __DATA__;
</script>
<script>
__JS__
</script>
</body>
</html>
"""


def _assets():
    with open(os.path.join(HERE, "viewer.css"), encoding="utf-8") as fh:
        css = fh.read()
    with open(os.path.join(HERE, "viewer.js"), encoding="utf-8") as fh:
        js = fh.read()
    return css, js


def _page(mode: str, bundles: Optional[List[dict]], title: str) -> str:
    css, js = _assets()
    data = json.dumps(bundles or [], ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")     # never close the tag early
    return (PAGE.replace("__CSS__", css)
                .replace("__JS__", js)
                .replace("__TITLE__", title)
                .replace("__VIEWMODE__", mode)
                .replace("__DATA__", data))


# --------------------------------------------------------------------------
# reading a folder
# --------------------------------------------------------------------------
def find_bundles(target: str) -> List[str]:
    """Every ``*_view.json`` under a directory, or the file itself."""
    if os.path.isfile(target):
        return [target]
    out = []
    for root, _dirs, files in os.walk(target):
        for f in files:
            if f.endswith("_view.json"):
                out.append(os.path.join(root, f))
    return sorted(out)


def read_bundles(target: str, with_review: bool = False,
                 root: Optional[str] = None) -> List[dict]:
    """Read every bundle under ``target``.

    ``root`` is the folder the *server* is serving, and the one every path the
    page sends back is relative to. Without it a bundle read from ``out/IND``
    reports its folder as "" and the page then asks the server to write into
    ``out`` -- which is how the first version of the edit endpoint returned 400
    for every edit.
    """
    base = os.path.abspath(root if root is not None else target)
    out = []
    for p in find_bundles(target):
        try:
            with open(p, encoding="utf-8") as fh:
                b = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"{p} could not be read: {exc}") from exc
        b["_file"] = os.path.basename(p)
        b["_stem"] = os.path.basename(p)[: -len("_view.json")]
        rel = os.path.relpath(os.path.dirname(p), base)
        b["_dir"] = "" if rel == "." else rel.replace(os.sep, "/")
        if with_review:
            d = os.path.dirname(p)
            patches = RV.load_patches(d, b["_stem"]).get("patches", [])
            b["_review"] = {"patches": patches,
                            "approval": RV.load_approval(d, b["_stem"])}
            if patches:
                b = RV.apply_patches(b, patches)
        out.append(b)
    out.sort(key=lambda b: (b.get("country", {}).get("iso3", ""),
                            b.get("domain", "")))
    return out


def scan(root: str) -> Dict[str, Any]:
    """What is on disk right now, grouped by country folder.

    A *country* is a folder holding at least one view bundle.  Pointing at
    ``out/`` finds them all; pointing at ``out/IND`` finds the one.
    """
    root = os.path.abspath(root)
    folders: List[Dict[str, Any]] = []
    for dirpath, _dirs, files in os.walk(root):
        views = [f for f in files if f.endswith("_view.json")]
        if not views:
            continue
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir.replace(os.sep, "/")
        iso3 = ""
        doms = []
        for v in sorted(views):
            try:
                with open(os.path.join(dirpath, v), encoding="utf-8") as fh:
                    b = json.load(fh)
            except (OSError, json.JSONDecodeError):
                continue
            iso3 = iso3 or b.get("country", {}).get("iso3", "")
            doms.append({"domain": b.get("domain"), "file": v,
                         "verdict": b.get("verdict"),
                         "counts": b.get("counts"),
                         "name": b.get("country", {}).get("name", "")})
        entry = {
            "dir": rel_dir,
            "iso3": iso3 or (rel_dir or os.path.basename(root)),
            "name": (doms[0]["name"] if doms else ""),
            "domains": doms,
            "files": sorted(
                ({"name": f,
                  "rel": (f"{rel_dir}/{f}" if rel_dir else f),
                  "size": os.path.getsize(os.path.join(dirpath, f))}
                 for f in files
                 if os.path.splitext(f)[1].lower() in READABLE),
                key=lambda x: x["name"]),
        }
        folders.append(entry)
    folders.sort(key=lambda c: (c["iso3"], c["dir"]))
    return {"root": root, "countries": folders}


def _safe_join(root: str, rel: str) -> Optional[str]:
    """Resolve ``rel`` under ``root``, or None if it escapes.

    Traversal is refused outright rather than normalised away: ``../..`` that
    happens to land back inside the root is still a caller asking for
    something it should not be asking for, and a quietly-corrected path is how
    the next version of this function stops being safe.
    """
    rel = (rel or "").replace("\\", "/")
    if rel.startswith("/") or ".." in rel.split("/"):
        return None
    if posixpath.normpath(rel) != posixpath.normpath(rel).lstrip("/"):
        return None
    full = os.path.abspath(os.path.join(root, rel.replace("/", os.sep)))
    if full != root and not full.startswith(root + os.sep):
        return None
    return full


# --------------------------------------------------------------------------
# the review server
# --------------------------------------------------------------------------
class _Handler(BaseHTTPRequestHandler):
    root = "."
    title = "GMD country concordance"
    server_version = "gmd-concordance-viewer"

    def log_message(self, fmt, *args):        # quiet; this is a review tool
        pass

    def _send(self, code, body: bytes, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(body)
        except BrokenPipeError:
            pass

    def _json(self, obj, code=200):
        self._send(code, json.dumps(obj, ensure_ascii=False,
                                    default=str).encode("utf-8"))

    def _body(self) -> Dict[str, Any]:
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > (1 << 20):
            return {}
        try:
            return json.loads(self.rfile.read(n).decode("utf-8")) or {}
        except (ValueError, UnicodeDecodeError):
            return {}

    def _stem_dir(self, q) -> Optional[tuple]:
        """(folder on disk, stem) for a bundle the caller names."""
        d = _safe_join(self.root, (q.get("dir") or [""])[0])
        stem = (q.get("stem") or [""])[0]
        if d is None or not os.path.isdir(d) or not stem:
            return None
        if "/" in stem or "\\" in stem or ".." in stem:
            return None
        return d, stem

    def do_POST(self):                         # noqa: N802
        u = urlparse(self.path)
        q = parse_qs(u.query)
        body = self._body()
        q.setdefault("dir", [body.get("dir", "")])
        q.setdefault("stem", [body.get("stem", "")])
        try:
            where = self._stem_dir(q)
            if where is None:
                return self._json({"error": "unknown bundle"}, 404)
            d, stem = where
            if u.path == "/api/patch":
                return self._json(RV.add_patch(d, stem, body.get("patch") or {}))
            if u.path == "/api/unpatch":
                ok = RV.undo_patch(d, stem, int(body.get("seq") or 0))
                return self._json({"undone": ok}, 200 if ok else 404)
            if u.path == "/api/approve":
                return self._json(RV.approve(
                    d, stem, by=body.get("by", ""),
                    fingerprint=body.get("fingerprint", ""),
                    version=body.get("version", ""),
                    verdict=body.get("verdict", ""),
                    counts=body.get("counts") or {},
                    acknowledged=body.get("acknowledged") or [],
                    note=body.get("note", ""),
                    patches=int(body.get("patches") or 0)))
            if u.path == "/api/revoke":
                return self._json(RV.revoke(d, stem, body.get("by", ""),
                                            body.get("reason", "")))
            return self._json({"error": "not found"}, 404)
        except ValueError as exc:
            # a refusal, not a crash: the message is meant for the reviewer
            return self._json({"error": str(exc)}, 400)
        except Exception as exc:               # noqa: BLE001
            return self._json({"error": str(exc)}, 500)

    def do_GET(self):                          # noqa: N802
        u = urlparse(self.path)
        q = parse_qs(u.query)
        path = u.path
        try:
            if path in ("/", "/index.html"):
                html = _page("server", None, self.title)
                return self._send(200, html.encode("utf-8"),
                                  "text/html; charset=utf-8")
            if path == "/api/scan":
                # re-read on every request: that is the whole point
                return self._json(scan(self.root))
            if path == "/api/bundles":
                d = _safe_join(self.root, (q.get("dir") or [""])[0])
                if d is None or not os.path.isdir(d):
                    return self._json({"error": "no such folder"}, 404)
                return self._json(read_bundles(d, with_review=True,
                                               root=self.root))
            if path == "/api/review":
                where = self._stem_dir(q)
                if where is None:
                    return self._json({"error": "unknown bundle"}, 404)
                d, stem = where
                return self._json({
                    "patches": RV.load_patches(d, stem).get("patches", []),
                    "approval": RV.load_approval(d, stem)})
            if path == "/api/raw":
                rel = (q.get("rel") or [""])[0]
                f = _safe_join(self.root, rel)
                if (f is None or not os.path.isfile(f)
                        or os.path.splitext(f)[1].lower() not in READABLE):
                    return self._json({"error": "not readable"}, 404)
                if os.path.getsize(f) > 4 << 20:
                    return self._json({"error": "file too large to display"}, 413)
                with open(f, encoding="utf-8", errors="replace") as fh:
                    return self._json({"rel": rel, "text": fh.read()})
            return self._json({"error": "not found"}, 404)
        except Exception as exc:               # noqa: BLE001
            return self._json({"error": str(exc)}, 500)


def _free_port(preferred: int) -> int:
    for p in [preferred] + list(range(preferred + 1, preferred + 40)):
        with socket.socket() as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    return 0


def serve(root: str, port: int = 8765, open_browser: bool = False,
          title: str = "GMD country concordance", block: bool = True):
    """Serve ``root`` on loopback.  Every request re-reads the folder."""
    root = os.path.abspath(root)
    if not os.path.isdir(root):
        raise ValueError(f"{root} is not a directory")
    handler = type("Handler", (_Handler,), {"root": root, "title": title})
    port = _free_port(port)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{httpd.server_address[1]}/"
    if open_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    if not block:
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()
        return httpd, url
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
    return httpd, url


# --------------------------------------------------------------------------
# writing the page
# --------------------------------------------------------------------------
def build(target: Optional[str] = None, out_path: Optional[str] = None,
          title: str = "GMD country concordance", embed: bool = False) -> str:
    """Write the page.

    ``embed=False`` (default) writes the folder-picker page: it carries no
    data and reads whatever folder is chosen, so it never goes stale.
    ``embed=True`` freezes the bundles under ``target`` into it.
    """
    bundles = read_bundles(target) if (embed and target) else None
    html = _page("embed" if bundles else "picker", bundles, title)
    if out_path is None:
        base = target if (target and os.path.isdir(target)) else "."
        out_path = os.path.join(base, "concordance_viewer.html")
    d = os.path.dirname(os.path.abspath(out_path))
    if d:
        os.makedirs(d, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return out_path
