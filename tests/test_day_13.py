import sys
import os
import pytest

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_13_Higher_Order_Functions.HOF import (
    apply_bonus_to_salaries,
    filter_high_yield_projects,
    get_active_customer_names,
    sort_products_by_attribute,
)

def test_apply_bonus_to_salaries():
    """Tests applying a bonus to a list of salaries."""
    salaries = [100, 200, 1000]
    assert apply_bonus_to_salaries(salaries, 0.1) == pytest.approx([110.0, 220.0, 1100.0])

def test_filter_high_yield_projects():
    """Tests filtering projects based on an ROI threshold."""
    projects = [("A", 10), ("B", 20), ("C", 15), ("D", 25)]
    assert filter_high_yield_projects(projects, 15) == [("B", 20), ("D", 25)]

def test_get_active_customer_names():
    """Tests filtering for active customers and mapping to their names."""
    customers = [
        {"name": "InnovateCorp", "subscription_status": "active"},
        {"name": "DataDriven Inc.", "subscription_status": "inactive"},
        {"name": "Analytics LLC", "subscription_status": "active"},
    ]
    assert get_active_customer_names(customers) == ["InnovateCorp", "Analytics LLC"]

def test_sort_products_by_attribute():
    """Tests sorting a list of dictionaries by a specified key."""
    products = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25},
        {"name": "Monitor", "price": 300},
    ]

    sorted_by_price = sort_products_by_attribute(products, "price")
    assert [p["name"] for p in sorted_by_price] == ["Mouse", "Monitor", "Laptop"]

    sorted_by_name = sort_products_by_attribute(products, "name")
    assert [p["name"] for p in sorted_by_name] == ["Laptop", "Monitor", "Mouse"]