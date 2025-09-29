import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_10_Loops.loops import (
    calculate_total_from_list,
    filter_high_value_customers,
    check_inventory_levels,
    simulate_investment_growth,
)


def test_calculate_total_from_list():
    """Tests the summation of a list of numbers."""
    assert calculate_total_from_list([10, 20, 30]) == 60
    assert calculate_total_from_list([1.5, 2.5]) == 4.0
    assert calculate_total_from_list([]) == 0


def test_filter_high_value_customers():
    """Tests the filtering of high-value customers."""
    customers = [
        {"name": "A", "total_spent": 2500},
        {"name": "B", "total_spent": 1500},
        {"name": "C", "total_spent": 2001},
        {"name": "D", "total_spent": 2000},
    ]
    high_value = filter_high_value_customers(customers, threshold=2000)
    assert high_value == ["A", "C"]

    # Test with no high-value customers
    assert filter_high_value_customers(customers, threshold=3000) == []


def test_check_inventory_levels():
    """Tests the inventory level checking logic."""
    inventory = {"Laptops": 15, "Mice": 100, "Keyboards": 45}
    low_stock = check_inventory_levels(inventory, threshold=50)
    assert "Laptops" in low_stock
    assert "Keyboards" in low_stock
    assert "Mice" not in low_stock
    assert len(low_stock) == 2


def test_simulate_investment_growth():
    """Tests the investment growth simulation."""
    # Test doubling money at 7%
    assert simulate_investment_growth(10000, 20000, 0.07) == 11
    # Test with a higher rate
    assert simulate_investment_growth(10000, 20000, 0.10) == 8
    # Test invalid input
    assert simulate_investment_growth(0, 1000, 0.05) == -1
    assert simulate_investment_growth(1000, 2000, 0) == -1
