import sys
import os
import pytest
import requests
from unittest.mock import patch, MagicMock

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_20_Python_Package_Manager.url import (
    fetch_api_data,
    analyze_breed_metrics,
    analyze_breed_origins,
    parse_metric_range,
)


# --- Test Data Fixtures ---
@pytest.fixture
def mock_cat_breeds_data():
    """Provides a sample of cat breed data for testing."""
    return [
        {
            "name": "Abyssinian",
            "weight": {"metric": "3 - 5"},
            "life_span": "14 - 15",
            "origin": "Egypt",
        },
        {
            "name": "Aegean",
            "weight": {"metric": "3 - 4"},
            "life_span": "9 - 12",
            "origin": "Greece",
        },
        {
            "name": "American Bobtail",
            "weight": {"metric": "3 - 7"},
            "life_span": "11 - 15",
            "origin": "United States",
        },
        {
            "name": "Singapura",
            "weight": {"metric": "2 - 4"},
            "life_span": "11 - 15",
            "origin": "Singapore",
        },
        {
            "name": "Toyger",
            "weight": {"metric": "3 - 5"},
            "life_span": "10 - 15",
            "origin": "United States",
        },
    ]


# --- Test Functions ---


def test_parse_metric_range():
    """Tests parsing a string range into an average float."""
    assert parse_metric_range("3 - 5") == 4.0
    assert parse_metric_range("10 - 15") == 12.5
    assert parse_metric_range("5") == 5.0
    assert parse_metric_range("invalid") == 0.0


@patch("Day_20_Python_Package_Manager.url.requests.get")
def test_fetch_api_data_success(mock_get):
    """Tests successful API data fetching and JSON decoding."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "test"}]
    mock_get.return_value = mock_response

    data = fetch_api_data("http://fakeapi.com/data")
    assert data == [{"id": 1, "name": "test"}]
    mock_get.assert_called_once_with("http://fakeapi.com/data", timeout=15)


@patch("Day_20_Python_Package_Manager.url.requests.get")
def test_fetch_api_data_http_error(mock_get):
    """Tests the function's handling of an HTTP error."""
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    mock_get.return_value = mock_response

    assert fetch_api_data("http://fakeapi.com/data") is None


def test_analyze_breed_metrics(mock_cat_breeds_data):
    """Tests the analysis of metrics from the breed data."""
    # Test weight analysis
    weight_stats = analyze_breed_metrics(mock_cat_breeds_data, "weight", "kg")
    assert weight_stats["mean"] == pytest.approx(3.9)
    assert weight_stats["median"] == pytest.approx(4.0)

    # Test lifespan analysis
    lifespan_stats = analyze_breed_metrics(mock_cat_breeds_data, "life_span", "years")
    assert lifespan_stats["mean"] == pytest.approx(12.7)
    assert lifespan_stats["median"] == pytest.approx(13.0)


def test_analyze_breed_origins(mock_cat_breeds_data):
    """Tests the analysis of breed origins."""
    top_origins = analyze_breed_origins(mock_cat_breeds_data, top_n=2)
    assert top_origins == [("United States", 2), ("Egypt", 1)]
    # Check that the order is correct (most common first)
    assert top_origins[0][0] == "United States"
