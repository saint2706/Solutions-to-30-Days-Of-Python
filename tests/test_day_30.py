"""Tests for Day 30 web scraping utilities."""

import importlib
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_30_Web_Scraping.web_scraping import process_book_data, scrape_books

HTML_FIXTURE = (
    (
        """
    <html>
        <body>
            <article class="product_pod">
                <h3><a title="Book One"></a></h3>
                <p class="price_color">£10.00</p>
            </article>
            <article class="product_pod">
                <h3><a title="Book Two"></a></h3>
                <p class="price_color">£12.50</p>
            </article>
            <article class="product_pod">
                <h3><a title="Book Three"></a></h3>
                <p class="price_color">£7.25</p>
            </article>
        </body>
    </html>
    """
    )
    .strip()
    .encode("utf-8")
)


class DummyResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def raise_for_status(self) -> None:  # pragma: no cover - simple stub
        return None


class DummySession:
    def __init__(self, content: bytes) -> None:
        self.content = content
        self.called_with = None

    def get(self, url, headers=None, timeout=None):  # pragma: no cover - simple stub
        self.called_with = {
            "url": url,
            "headers": headers,
            "timeout": timeout,
        }
        return DummyResponse(self.content)


def test_process_book_data_returns_clean_dataframe_and_summary():
    raw_df, clean_df, analysis = process_book_data(HTML_FIXTURE)

    assert list(raw_df.columns) == ["Title", "Price"]
    assert list(clean_df.columns) == ["Title", "Price", "Price_Float"]
    assert clean_df["Price"].tolist() == ["£10.00", "£12.50", "£7.25"]
    assert clean_df["Price_Float"].tolist() == [10.0, 12.5, 7.25]
    assert clean_df["Price_Float"].dtype.kind == "f"

    assert analysis["average_price"] == pytest.approx(9.9166, rel=1e-3)
    assert analysis["min_price"] == pytest.approx(7.25)
    assert analysis["max_price"] == pytest.approx(12.5)
    assert analysis["count"] == 3
    assert analysis["most_expensive_title"] == "Book Two"
    assert analysis["most_expensive_price"] == "£12.50"
    assert analysis["cheapest_title"] == "Book Three"
    assert analysis["cheapest_price"] == "£7.25"


def test_scrape_books_uses_injected_session():
    session = DummySession(HTML_FIXTURE)
    raw_df, clean_df, analysis = scrape_books("http://example.com", session=session)

    assert session.called_with["url"] == "http://example.com"
    assert session.called_with["timeout"] == 10
    assert "User-Agent" in session.called_with["headers"]
    assert len(raw_df) == 3
    assert analysis["count"] == 3


def test_process_book_data_with_no_books_raises_value_error():
    empty_html = "<html><body></body></html>".encode("utf-8")
    with pytest.raises(ValueError):
        process_book_data(empty_html)


def test_fetch_tables_returns_category_only_when_no_pairs(monkeypatch):
    import Day_30_Web_Scraping.web_scraping_bu as web_scraping_bu

    sample_html = (
        "<html><body>"
        '<div class="facts-wrapper"><h5>Category One</h5></div>'
        '<div class="facts-wrapper"><h5>Category Two</h5></div>'
        "</body></html>"
    ).encode("utf-8")

    class DummyResponse:
        def __init__(self, content: bytes) -> None:
            self.content = content

    def fake_get(url):  # pragma: no cover - trivial helper
        return DummyResponse(sample_html)

    monkeypatch.setattr(web_scraping_bu.requests, "get", fake_get)

    tables = web_scraping_bu.fetch_tables("http://example.com")

    assert tables == [
        {"Category": "Category One"},
        {"Category": "Category Two"},
    ]


def test_save_tables_writes_json(tmp_path):
    import Day_30_Web_Scraping.web_scraping_bu as web_scraping_bu

    data = [{"Category": "Category One", "Key": "Value"}]
    output_file = tmp_path / "output.json"

    path = web_scraping_bu.save_tables(data, output_file)

    assert path == output_file
    assert json.loads(output_file.read_text(encoding="utf-8")) == data


def test_main_orchestrates_scrape(monkeypatch, tmp_path):
    import Day_30_Web_Scraping.web_scraping_bu as web_scraping_bu

    sample_html = (
        "<html><body>"
        '<div class="facts-wrapper"><h5>Category One</h5></div>'
        '<div class="facts-wrapper"><h5>Category Two</h5></div>'
        "</body></html>"
    ).encode("utf-8")

    class DummyResponse:
        def __init__(self, content: bytes) -> None:
            self.content = content

    def fake_get(url):  # pragma: no cover - trivial helper
        return DummyResponse(sample_html)

    monkeypatch.setattr(web_scraping_bu.requests, "get", fake_get)

    output_file = tmp_path / "result.json"
    result_path = web_scraping_bu.main(
        url="http://example.com", output_path=output_file
    )

    assert result_path == output_file
    assert json.loads(output_file.read_text(encoding="utf-8")) == [
        {"Category": "Category One"},
        {"Category": "Category Two"},
    ]


def test_import_has_no_side_effects(monkeypatch):
    import requests

    module_name = "Day_30_Web_Scraping.web_scraping_bu"
    sys.modules.pop(module_name, None)

    calls = []

    def fake_get(*args, **kwargs):  # pragma: no cover - trivial helper
        calls.append((args, kwargs))
        raise AssertionError("fetch should not occur during import")

    monkeypatch.setattr(requests, "get", fake_get)

    module = importlib.import_module(module_name)

    assert module.__name__ == module_name
    assert calls == []
