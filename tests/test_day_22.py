import sys
import os
import pytest
import numpy as np

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_22_NumPy.numpy_examples import (
    calculate_revenue_vectorized,
    analyze_sales_data,
    filter_above_average,
)


def test_calculate_revenue_vectorized():
    """Tests vectorized revenue calculation."""
    prices = [10, 20, 30]
    units = [5, 2, 3]
    revenue = calculate_revenue_vectorized(prices, units)
    assert isinstance(revenue, np.ndarray)
    np.testing.assert_array_equal(revenue, np.array([50, 40, 90]))


def test_analyze_sales_data():
    """Tests the sales data analysis function."""
    sales = [100, 200, 300, 400, 500]
    stats = analyze_sales_data(sales)
    assert stats["total"] == 1500
    assert stats["mean"] == 300
    assert stats["max"] == 500
    assert stats["min"] == 100
    assert stats["std_dev"] == pytest.approx(141.42, rel=1e-2)


def test_analyze_sales_data_empty():
    """Tests the sales analysis function with empty data."""
    stats = analyze_sales_data([])
    assert stats == {}


def test_filter_above_average():
    """Tests filtering an array for values above the mean."""
    data = np.array([1, 2, 3, 4, 5, 10])  # Mean is 4.16
    result = filter_above_average(data)
    np.testing.assert_array_equal(result, np.array([5, 10]))

    # Test with empty array
    empty_result = filter_above_average(np.array([]))
    assert empty_result.size == 0
