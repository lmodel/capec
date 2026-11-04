#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check MITRE's CAPEC site against the version the schema renders.

The schema renders CAPEC at the version pinned below, and upstream/ holds that
version's XSD and catalogue unchanged. MITRE's last catalogue dates from January
2023 and its last news item from March 2023. No page says CAPEC has stopped, so
this watch keeps asking. Six things can change without any change in this
repository:

- the latest catalogue is another version, or another file under the same version;
- the versioned address of the catalogue stops serving the pinned file;
- the XSD at its versioned or its latest address stops being the pinned file;
- the CAPEC list page names another version;
- the Terms of Use change;
- a new news item appears, which may announce a release or a change of status.

The script reads those pages from capec.mitre.org and compares files by git object
hash and the Terms by the SHA-256 of their text.

It prints a Markdown report, and exits 1 when any of those is so, or when a check
could not finish, such as on a refused, failed or cut-off request, or an answer
larger than the script reads.

Text a server chose, such as a version or an error message, is quoted as code on
one line in the report, so the issue the workflow opens from it cannot mention
anyone. A redirect is followed only to an https address on capec.mitre.org. The
script sends no token, since the site asks for none. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import html
import http.client
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = "lmodel-capec-watch"
SITE = "https://capec.mitre.org/"
# The one host a redirect may lead to.
HOSTS = frozenset({"capec.mitre.org"})

# The most the script reads of one answer. The largest, the catalogue, is about
# 3.9 MB.
MAX_BYTES = 8_000_000

# The version the schema renders. tests/test_upstream.py holds the schema header
# and these pins equal. Move them together, with upstream/ and the header, for
# another version.
PINNED_EDITION = "3.9"
PINNED_DATE = "2023-01-24"
PINNED_XSD_VERSION = "3.5"
PINNED_XSD_NAMESPACE = "http://capec.mitre.org/capec-3"
PINNED_SOURCE = f"{SITE}data/xsd/ap_schema_v3.5.xsd"

CATALOGUE_LATEST = f"{SITE}data/xml/capec_latest.xml"
CATALOGUE_PINNED = f"{SITE}data/xml/capec_v3.9.xml"
XSD_LATEST = f"{SITE}data/xsd/ap_schema_latest.xsd"
LIST_PAGE = f"{SITE}data/index.html"
TERMS_PAGE = f"{SITE}about/termsofuse.html"
NEWS_PAGE = f"{SITE}news/index.html"

# Each file upstream/ copies, with its git object hash. tests/test_upstream.py
# holds upstream/ to this list.
PINNED_BLOBS = {
    "ap_schema_v3.5.xsd": "a3ea0d5d0f288498af57578bdd19e5a698bda055",
    "capec_v3.9.xml": "9964711df56a7dc1ab0af79e8f0a5ce3acb8874b",
}

# The SHA-256 of the licence and disclaimer as _terms_text reads them from the
# page, which leaves out the footer's year and the page's other furniture.
PINNED_TERMS_SHA256 = "1316cb31871978f32e6aaf40b30ebe86b22a01e1e670f0b314c96f2de4e5abd1"

# The date of the newest item on the news page.
PINNED_NEWS_DATE = "March 13, 2023"

_DATE = re.compile(
    r"(?:January|February|March|April|May|June|July|August|September|October"
    r"|November|December) \d{1,2}, \d{4}"
)


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on one of HOSTS."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off the expected hosts, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> bytes:
    """The body of an answer from the site, read up to the cap."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a
    person or add a link in the issue. A blank line would end the span, so
    every run of spaces and line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def blob_hash(data: bytes) -> str:
    """The git object hash of a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _root_attribute(data: bytes, name: str) -> str:
    """An attribute of the catalogue's root element, read from the file's start."""
    head = data[:2000].decode("utf-8", "replace")
    found = re.search(rf'\b{name}="([^"]*)"', head)
    if not found:
        raise ValueError(f"the catalogue's root element has no {name}")
    return found.group(1)


def check_catalogue() -> tuple[list[str], bool]:
    """Report whether the latest catalogue is the pinned version and file, and
    whether the versioned address still serves that file."""
    report, attention = [], False
    latest = _get(CATALOGUE_LATEST)
    version, date = _root_attribute(latest, "Version"), _root_attribute(latest, "Date")
    if (version, date) != (PINNED_EDITION, PINNED_DATE):
        attention = True
        report.append(
            f"- **The latest catalogue is version {_code(version)} of {_code(date)}; "
            f"the schema renders {PINNED_EDITION} of {PINNED_DATE}.** Read what "
            "changed, decide whether the schema moves to it, and move upstream/, the "
            "pins here and the schema headers together."
        )
    else:
        report.append(
            f"- The latest catalogue is the pinned version, {PINNED_EDITION} of "
            f"{PINNED_DATE}."
        )
    if blob_hash(latest) != PINNED_BLOBS["capec_v3.9.xml"]:
        attention = True
        report.append(
            "- **The latest catalogue is not the pinned file.** Find out what changed "
            "before trusting the copy in upstream/."
        )
    else:
        report.append("- The latest catalogue is the pinned file.")
    if blob_hash(_get(CATALOGUE_PINNED)) != PINNED_BLOBS["capec_v3.9.xml"]:
        attention = True
        report.append(
            f"- **`{CATALOGUE_PINNED}` no longer serves the pinned file.** Find out "
            "what happened before trusting the copy in upstream/."
        )
    else:
        report.append(f"- `{CATALOGUE_PINNED}` serves the pinned file.")
    return report, attention


def check_schema() -> tuple[list[str], bool]:
    """Report whether the XSD at each address is the pinned file."""
    report, attention = [], False
    for url in (PINNED_SOURCE, XSD_LATEST):
        if blob_hash(_get(url)) != PINNED_BLOBS["ap_schema_v3.5.xsd"]:
            attention = True
            report.append(
                f"- **`{url}` is not the pinned XSD.** Read what changed, decide "
                "whether the schema moves to it, and move upstream/ with it."
            )
        else:
            report.append(f"- `{url}` is the pinned XSD.")
    return report, attention


def check_list_page() -> tuple[list[str], bool]:
    """Report whether the CAPEC list page names the pinned version."""
    text = _get(LIST_PAGE).decode("utf-8", "replace")
    found = re.search(r"CAPEC List Version ([0-9][0-9.]*)", text)
    if not found:
        return ["- **The CAPEC list page names no version.** Read the page."], True
    if found.group(1) != PINNED_EDITION:
        return [
            f"- **The CAPEC list page names version {_code(found.group(1))}, not "
            f"{PINNED_EDITION}.** Read what changed and decide whether the schema "
            "moves to it."
        ], True
    return [f"- The CAPEC list page names version {PINNED_EDITION}."], False


def _terms_text(page: bytes) -> str:
    """The licence and the disclaimer from the Terms of Use page, as plain text.
    The rest of the page holds the menus, and a footer whose year moves."""
    text = page.decode("utf-8", "replace")
    found = re.search(
        r"<h3>LICENSE</h3>(.*?)<h3>DISCLAIMERS</h3>\s*<p>(.*?)</p>", text, re.S
    )
    if not found:
        raise ValueError("the Terms of Use page has no licence and disclaimer")
    plain = re.sub(r"<[^>]+>", " ", found.group(1) + " " + found.group(2))
    return " ".join(html.unescape(plain).split())


def check_terms() -> tuple[list[str], bool]:
    """Report whether the text of the Terms of Use is the pinned text."""
    digest = hashlib.sha256(_terms_text(_get(TERMS_PAGE)).encode("utf-8")).hexdigest()
    if digest != PINNED_TERMS_SHA256:
        return [
            f"- **The Terms of Use changed, at {TERMS_PAGE}.** Read what changed, "
            "update NOTICE and upstream/TERMS.txt if the licence moved, and move "
            "the pin."
        ], True
    return ["- The text of the Terms of Use is the pinned text."], False


def check_news() -> tuple[list[str], bool]:
    """Report whether the newest news item is the pinned one."""
    text = _get(NEWS_PAGE).decode("utf-8", "replace")
    found = _DATE.search(text)
    if not found:
        return ["- **The news page shows no dated item.** Read the page."], True
    if found.group(0) != PINNED_NEWS_DATE:
        return [
            f"- **The news page has a newer item, dated {_code(found.group(0))}.** "
            f"Read {NEWS_PAGE}, since it may announce a release or a change of status, "
            "and move the pin."
        ], True
    return [f"- The newest news item is the pinned one, of {PINNED_NEWS_DATE}."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("catalogue", check_catalogue),
    ("schema", check_schema),
    ("list page", check_list_page),
    ("terms of use", check_terms),
    ("news", check_news),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned version: CAPEC {PINNED_EDITION} of {PINNED_DATE}, under XSD "
        f"{PINNED_XSD_VERSION}, {PINNED_SOURCE}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer, and
        # ValueError an answer of another shape or one that is too large.
        except (OSError, http.client.HTTPException, EOFError, ValueError) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
