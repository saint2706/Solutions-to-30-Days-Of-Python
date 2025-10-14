import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_03_Operators.operators import (
    accumulate_sales,
    calculate_compound_interest,
    check_bonus_eligibility,
    check_inventory_status,
    check_sales_target,
)


def test_calculate_compound_interest():
    """Tests the compound interest calculation."""
    assert round(calculate_compound_interest(10000, 0.05, 3), 2) == 11576.25
    assert calculate_compound_interest(5000, 0.1, 1) == 5500.0


def test_accumulate_sales():
    """Tests the sales accumulation logic."""
    assert accumulate_sales(0, [100, 200, 300]) == 600
    assert accumulate_sales(1000, [50, 50]) == 1100
    assert accumulate_sales(0, []) == 0


def test_check_inventory_status():
    """Tests the inventory status check."""
    assert check_inventory_status(45, 50) is True
    assert check_inventory_status(50, 50) is False
    assert check_inventory_status(55, 50) is False


def test_check_sales_target():
    """Tests the sales target check."""
    assert check_sales_target(265000, 250000) is True
    assert check_sales_target(250000, 250000) is True
    assert check_sales_target(249999, 250000) is False


def test_check_bonus_eligibility():
    """Tests the bonus eligibility logic with multiple scenarios."""
    # Scenario 1: High sales, but new employee -> Not eligible
    assert check_bonus_eligibility(12000, 1, False) is False
    # Scenario 2: Lower sales, but a top performer -> Eligible
    assert check_bonus_eligibility(8000, 3, True) is True
    # Scenario 3: Not eligible on either count -> Not eligible
    assert check_bonus_eligibility(9000, 1, False) is False
    # Scenario 4: High sales and long service -> Eligible
    assert check_bonus_eligibility(11000, 3, False) is True
    # Scenario 5: All conditions met -> Eligible
    assert check_bonus_eligibility(15000, 5, True) is True
