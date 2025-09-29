"""Unit tests for the Day 33 API helpers."""

from __future__ import annotations

import os
import sys

import pandas as pd
import pytest
import requests
import responses

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_33_API.api import fetch_post, fetch_posts_by_user, fetch_users

BASE_URL = "https://jsonplaceholder.typicode.com"


@responses.activate
def test_fetch_users_success() -> None:
    responses.add(
        responses.GET,
        f"{BASE_URL}/users",
        json=[{"id": 1, "name": "Ada", "username": "ada"}],
        status=200,
    )

    df = fetch_users()

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 3)
    assert df.iloc[0]["name"] == "Ada"


@responses.activate
def test_fetch_post_success() -> None:
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts/10",
        json={"id": 10, "userId": 99, "title": "Example", "body": "text"},
        status=200,
    )

    post = fetch_post(10)

    assert post["id"] == 10
    assert post["userId"] == 99


@responses.activate
def test_fetch_posts_by_user_success() -> None:
    payload = [
        {"id": 1, "userId": 3, "title": "First"},
        {"id": 2, "userId": 3, "title": "Second"},
    ]
    responses.add(
        responses.GET,
        f"{BASE_URL}/posts",
        json=payload,
        match=[responses.matchers.query_param_matcher({"userId": "3"})],
        status=200,
    )

    df = fetch_posts_by_user(3)

    assert df.shape[0] == 2
    assert sorted(df["title"]) == ["First", "Second"]


@responses.activate
@pytest.mark.parametrize(
    "func, url",
    [
        (lambda: fetch_users(), f"{BASE_URL}/users"),
        (lambda: fetch_post(42), f"{BASE_URL}/posts/42"),
        (lambda: fetch_posts_by_user(8), f"{BASE_URL}/posts"),
    ],
)
def test_http_error_paths(func, url) -> None:
    responses.add(responses.GET, url, status=500)

    with pytest.raises(requests.HTTPError):
        func()
