import os
import sys

# Add the parent directory to the Python path to allow for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_01_Introduction.helloworld import (
    calculate_gross_profit,
    calculate_gross_profit_margin,
)


def test_calculate_gross_profit():
    """Test the calculate_gross_profit function."""
    assert calculate_gross_profit(500000, 350000) == 150000
    assert calculate_gross_profit(1000, 1000) == 0
    assert calculate_gross_profit(0, 0) == 0
    assert calculate_gross_profit(100, 150) == -50


def test_calculate_gross_profit_margin():
    """Test the calculate_gross_profit_margin function."""
    assert calculate_gross_profit_margin(150000, 500000) == 30.0
    assert calculate_gross_profit_margin(0, 1000) == 0.0
    assert calculate_gross_profit_margin(500, 1000) == 50.0
    assert calculate_gross_profit_margin(1000, 1000) == 100.0


def test_calculate_gross_profit_margin_zero_revenue():
    """Test the edge case where revenue is zero to avoid division by zero."""
    assert calculate_gross_profit_margin(0, 0) == 0
    assert calculate_gross_profit_margin(100, 0) == 0
