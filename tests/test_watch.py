"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads pages and files from capec.mitre.org. These
tests replace its one network call, `_get`, with a table of answers, so they run
offline. They show what the report says in each case the watch knows: another version,
another file, changed terms, a new news item, and a check that could not finish.
"""

import hashlib
import http.client
import importlib.util
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
UPSTREAM = ROOT / "upstream"

TERMS_PAGE = (
    b"<html><body><h2>Terms of Use</h2><h3>LICENSE</h3><p>A licence with "
    b"MITRE&#8217;s name.</p>\n\n<h3>DISCLAIMERS</h3>\n<p>A disclaimer.</p>\n"
    b"<div>Copyright 2007-2026</div></body></html>"
)
TERMS_TEXT = "A licence with MITRE’s name. A disclaimer."
LIST_PAGE = b"<title>CAPEC List Version 3.9</title><h1>CAPEC List Version 3.9</h1>"
NEWS_PAGE = (
    b"<!--start articles--><p>March 13, 2023 | Share</p><p>February 23, 2023</p>"
)


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.PINNED_TERMS_SHA256 = hashlib.sha256(TERMS_TEXT.encode()).hexdigest()
    return module


def _answers(watch):
    """The answers of an unchanged upstream, which a test then changes."""
    catalogue = (UPSTREAM / "capec_v3.9.xml").read_bytes()
    xsd = (UPSTREAM / "ap_schema_v3.5.xsd").read_bytes()
    return {
        watch.CATALOGUE_LATEST: catalogue,
        watch.CATALOGUE_PINNED: catalogue,
        watch.PINNED_SOURCE: xsd,
        watch.XSD_LATEST: xsd,
        watch.LIST_PAGE: LIST_PAGE,
        watch.TERMS_PAGE: TERMS_PAGE,
        watch.NEWS_PAGE: NEWS_PAGE,
    }


def _run(watch, monkeypatch, capsys, answers):
    def get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return answer

    monkeypatch.setattr(watch, "_get", get)
    code = watch.main([])
    return code, capsys.readouterr().out


def test_an_unchanged_upstream_passes(watch, monkeypatch, capsys):
    code, out = _run(watch, monkeypatch, capsys, _answers(watch))
    assert code == 0, out
    assert "**" not in out
    assert "The latest catalogue is the pinned version, 3.9 of 2023-01-24." in out


def test_another_version_asks_for_a_person(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.CATALOGUE_LATEST] = answers[watch.CATALOGUE_LATEST].replace(
        b'Version="3.9"', b'Version="4.0"', 1
    )
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "The latest catalogue is version `4.0`" in out
    assert "The latest catalogue is not the pinned file." in out


def test_another_file_under_the_same_version_asks_for_a_person(
    watch, monkeypatch, capsys
):
    answers = _answers(watch)
    answers[watch.CATALOGUE_LATEST] = answers[watch.CATALOGUE_LATEST] + b"\n"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "The latest catalogue is the pinned version" in out
    assert "The latest catalogue is not the pinned file." in out


def test_the_pinned_address_serving_another_file_asks_for_a_person(
    watch, monkeypatch, capsys
):
    answers = _answers(watch)
    answers[watch.CATALOGUE_PINNED] = b"another file"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "no longer serves the pinned file" in out


@pytest.mark.parametrize("name", ["PINNED_SOURCE", "XSD_LATEST"])
def test_another_xsd_at_either_address_asks_for_a_person(
    watch, monkeypatch, capsys, name
):
    answers = _answers(watch)
    answers[getattr(watch, name)] = b"<xs:schema/>"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert f"`{getattr(watch, name)}` is not the pinned XSD." in out


def test_the_list_page_naming_another_version_asks_for_a_person(
    watch, monkeypatch, capsys
):
    answers = _answers(watch)
    answers[watch.LIST_PAGE] = b"<h1>CAPEC List Version 4.0</h1>"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "names version `4.0`" in out


def test_a_list_page_with_no_version_asks_for_a_person(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.LIST_PAGE] = b"<h1>CAPEC has moved</h1>"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "names no version" in out


def test_changed_terms_ask_for_a_person(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.TERMS_PAGE] = TERMS_PAGE.replace(b"A licence", b"Another licence")
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "The Terms of Use changed" in out


def test_the_footers_year_is_not_a_change_of_terms(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.TERMS_PAGE] = TERMS_PAGE.replace(b"2007-2026", b"2007-2027")
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 0, out


def test_terms_that_cannot_be_found_stop_that_check(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.TERMS_PAGE] = b"<html>A new layout</html>"
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "The terms of use check could not finish" in out


def test_a_new_news_item_asks_for_a_person(watch, monkeypatch, capsys):
    answers = _answers(watch)
    answers[watch.NEWS_PAGE] = b"<p>June 1, 2027 | Share</p>" + NEWS_PAGE
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "newer item, dated `June 1, 2027`" in out


@pytest.mark.parametrize(
    "failure",
    [
        urllib.error.URLError("refused"),
        http.client.RemoteDisconnected("cut off"),
        EOFError("cut off"),
        ValueError("too large"),
    ],
)
def test_a_check_that_cannot_finish_fails_and_the_rest_still_run(
    watch, monkeypatch, capsys, failure
):
    answers = _answers(watch)
    answers[watch.LIST_PAGE] = failure
    code, out = _run(watch, monkeypatch, capsys, answers)
    assert code == 1
    assert "The list page check could not finish" in out
    assert "The text of the Terms of Use is the pinned text." in out


def test_a_servers_text_cannot_mention_anyone(watch):
    """Text a server chose goes out as code, on one line."""
    assert watch._code("@someone\n\n`tick`") == "`@someone 'tick'`"


def test_a_redirect_off_the_site_is_refused(watch):
    """A redirect is followed over https to capec.mitre.org, and nowhere else."""
    handlers = watch._open.__self__.handlers
    assert any(isinstance(h, watch._ExpectedHostRedirect) for h in handlers)
    handler = watch._ExpectedHostRedirect()
    req = watch.urllib.request.Request(watch.LIST_PAGE)
    for newurl in (
        "https://example.org/x",
        "http://capec.mitre.org/x",
        "https://capec.mitre.org.example.org/x",
    ):
        with pytest.raises(ValueError, match="off the expected hosts"):
            handler.redirect_request(req, None, 302, "", {}, newurl)
    moved = "https://capec.mitre.org/data/index.html"
    assert handler.redirect_request(req, None, 301, "", {}, moved).full_url == moved


class _Answer:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, size):
        return b"{}"


def test_no_token_travels(watch, monkeypatch):
    """The watch sends no token: the pages are public and the host is not GitHub."""
    monkeypatch.setenv("GITHUB_TOKEN", "not-to-send")
    sent = {}

    def urlopen(req, timeout):
        sent["headers"] = dict(req.header_items())
        sent["unredirected"] = dict(req.unredirected_hdrs)
        return _Answer()

    monkeypatch.setattr(watch, "_open", urlopen)
    watch._get(watch.LIST_PAGE)
    assert sent["headers"]["User-agent"] == "lmodel-capec-watch"
    assert "Authorization" not in sent["headers"]
    assert not sent["unredirected"]


def test_an_answer_over_the_cap_is_refused(watch, monkeypatch):
    class Big(_Answer):
        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch, "_open", lambda req, timeout: Big())
    with pytest.raises(ValueError, match="larger than"):
        watch._get(watch.LIST_PAGE)


def test_the_report_is_written_where_asked(watch, monkeypatch, capsys, tmp_path):
    answers = _answers(watch)
    monkeypatch.setattr(watch, "_get", answers.__getitem__)
    report = tmp_path / "report.md"
    assert watch.main(["--report", str(report)]) == 0
    assert "Pinned version: CAPEC 3.9" in report.read_text(encoding="utf-8")
    capsys.readouterr()
