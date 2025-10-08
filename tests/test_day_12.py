import os
import sys

import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_12_List_Comprehension.list_comprehension import (
    apply_price_increase,
    filter_large_sales,
    get_top_sales_performers,
)


def test_apply_price_increase():
    """Tests applying a price increase to a list of prices."""
    prices = [100, 200, 1000]
    new_prices = apply_price_increase(prices, 0.1)  # 10% increase
    assert new_prices == pytest.approx([110.0, 220.0, 1100.0])


def test_filter_large_sales():
    """Tests filtering a list for sales above a threshold."""
    sales = [50, 150, 100, 200, 250]
    assert filter_large_sales(sales, 100) == [150, 200, 250]
    assert filter_large_sales(sales, 300) == []


def test_get_top_sales_performers():
    """Tests filtering and transforming a list of dictionaries."""
    employees = [
        {"name": "Alice", "department": "Sales", "quarterly_sales": 12000},
        {"name": "Bob", "department": "Engineering", "quarterly_sales": 9000},
        {"name": "Charlie", "department": "Sales", "quarterly_sales": 8000},
        {"name": "David", "department": "Sales", "quarterly_sales": 15000},
        {"name": "Eve", "department": "Sales", "quarterly_sales": 10000},  # Not > 10000
    ]
    target = 10000

    top_performers = get_top_sales_performers(employees, target)

    assert top_performers == ["Alice", "David"]
    assert "Charlie" not in top_performers
    assert "Bob" not in top_performers
    assert "Eve" not in top_performers


def test_get_top_sales_performers_empty():
    """Tests the top performers function with an empty list."""
    assert get_top_sales_performers([], 10000) == []
