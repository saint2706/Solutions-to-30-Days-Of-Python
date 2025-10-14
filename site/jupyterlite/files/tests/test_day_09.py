import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_09_Conditionals.conditionals import (
    calculate_discount_percent,
    calculate_employee_bonus,
    calculate_shipping_cost,
)


def test_calculate_discount_percent():
    """Tests the discount calculation logic for various amounts."""
    assert calculate_discount_percent(125.50) == 0.10
    assert calculate_discount_percent(100.00) == 0.05
    assert calculate_discount_percent(75.00) == 0.05
    assert calculate_discount_percent(50.00) == 0.00
    assert calculate_discount_percent(25.00) == 0.00
    assert calculate_discount_percent(-10.00) == 0.00  # Test invalid input
    assert calculate_discount_percent("abc") == 0.00  # Test invalid input type


def test_calculate_shipping_cost():
    """Tests the shipping cost calculation for different countries and weights."""
    # USA
    assert calculate_shipping_cost("USA", 40) == 50
    assert calculate_shipping_cost("USA", 60) == 75
    # Canada
    assert calculate_shipping_cost("Canada", 40) == 65
    assert calculate_shipping_cost("Canada", 60) == 100
    # Other
    assert calculate_shipping_cost("Mexico", 40) == -1


def test_calculate_employee_bonus():
    """Tests the employee bonus calculation with different scenarios."""
    salary = 100000
    # Excellent performance in Sales
    assert calculate_employee_bonus(5, "Sales", salary) == 15000
    # Excellent performance in another department
    assert calculate_employee_bonus(4, "Marketing", salary) == 10000
    # Met expectations
    assert calculate_employee_bonus(3, "Engineering", salary) == 5000
    # Needs improvement
    assert calculate_employee_bonus(2, "Sales", salary) == 0
    assert calculate_employee_bonus(1, "HR", salary) == 0
