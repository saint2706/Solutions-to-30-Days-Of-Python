import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_15_Exception_Handling.exception import (
    unpack_country_list,
    calculate_profit_margin,
)


def test_unpack_country_list():
    """Tests the unpacking of a list of countries."""
    countries = [
        "Finland",
        "Sweden",
        "Norway",
        "Denmark",
        "Iceland",
        "Estonia",
        "Russia",
    ]
    nordic, estonia, russia = unpack_country_list(countries)
    assert nordic == ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
    assert estonia == "Estonia"
    assert russia == "Russia"


def test_unpack_country_list_insufficient_items():
    """Tests the country unpacking function with a list that is too short."""
    countries = ["Estonia", "Russia"]
    nordic, estonia, russia = unpack_country_list(countries)
    assert nordic is None
    assert estonia is None
    assert russia is None


def test_calculate_profit_margin():
    """Tests the profit margin calculation, including the zero division case."""
    assert calculate_profit_margin(revenue=1000, profit=200) == 20.0
    # Test the ZeroDivisionError case
    assert calculate_profit_margin(revenue=0, profit=100) == 0.0
    # Test the TypeError case
    assert calculate_profit_margin(revenue="abc", profit=100) is None
