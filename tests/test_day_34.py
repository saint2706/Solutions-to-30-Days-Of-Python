"""Tests for the Day 34 Flask API example."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_34_Building_an_API.api_server import create_app  # noqa: E402
from Day_34_Building_an_API.data import EMPLOYEES, PRODUCTS  # noqa: E402


def _get_app_client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_home_route():
    client = _get_app_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Company Data API" in response.data


def test_get_all_products():
    client = _get_app_client()
    response = client.get("/api/v1/products")
    assert response.status_code == 200
    assert response.get_json() == PRODUCTS


def test_get_single_product():
    client = _get_app_client()
    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.get_json() == PRODUCTS[0]


def test_get_single_product_not_found():
    client = _get_app_client()
    response = client.get("/api/v1/products/999")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Product not found"}


def test_get_all_employees():
    client = _get_app_client()
    response = client.get("/api/v1/employees")
    assert response.status_code == 200
    assert response.get_json() == EMPLOYEES
