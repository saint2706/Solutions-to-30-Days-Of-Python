"""Tests for Day 35 Flask text analyser."""
from __future__ import annotations

import html
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from Day_35_Flask_Web_Framework.app import create_app
from Day_35_Flask_Web_Framework.app.text_utils import (
    clean_text,
    lex_div_calc,
    most_common_word,
)


@pytest.fixture()
def app():
    return create_app({"TESTING": True, "SECRET_KEY": "test"})


@pytest.fixture()
def client(app):
    return app.test_client()


def test_clean_text_strips_noise() -> None:
    noisy = "Hello, MBA world! Visit https://example.com for more info [ref]."
    assert (
        clean_text(noisy)
        == "hello mba world visit for more info"
    )


def test_most_common_word_counts_sorted() -> None:
    counts = most_common_word("flask flask python data")
    assert counts == [("flask", 2), ("python", 1), ("data", 1)]


def test_lex_div_calc_handles_empty() -> None:
    assert lex_div_calc("") == "0.0"


@pytest.mark.parametrize(
    "payload",
    [
        "Hello world! Hello, <b>Flask</b> 123\nNew line.",
    ],
)
def test_full_text_analysis_flow(client, payload: str) -> None:
    response = client.post("/post", data={"content": payload}, follow_redirects=True)
    assert response.status_code == 200

    cleaned = clean_text(payload)
    word_counts = most_common_word(cleaned)

    page = response.get_data(as_text=True)
    assert f"Total Number of Words: {len(cleaned.split())}" in page
    assert f"Number of characters: {len(cleaned)}" in page
    if word_counts:
        assert f"Most Frequent Word: {word_counts[0][0]}" in page
    assert f"Word Variety: {lex_div_calc(cleaned)} %" in page

    unescaped = html.unescape(page)
    for count in word_counts[:3]:
        assert str(count) in unescaped
