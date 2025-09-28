import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_11_Functions.functions import (
    get_net_profit,
    calculate_commission,
    is_eligible_for_bonus,
    format_currency,
)

def test_get_net_profit():
    """Tests the net profit calculation."""
    assert get_net_profit(1000, 800) == 200
    assert get_net_profit(500, 500) == 0
    assert get_net_profit(200, 300) == -100

def test_calculate_commission():
    """Tests the sales commission calculation."""
    assert calculate_commission(10000) == 1500
    assert calculate_commission(0) == 0

def test_is_eligible_for_bonus():
    """Tests the bonus eligibility logic."""
    # Eligible scenario
    assert is_eligible_for_bonus(performance_rating=5, years_of_service=3) is True
    assert is_eligible_for_bonus(performance_rating=4, years_of_service=5) is True
    # Not eligible due to rating
    assert is_eligible_for_bonus(performance_rating=3, years_of_service=5) is False
    # Not eligible due to service years
    assert is_eligible_for_bonus(performance_rating=5, years_of_service=2) is False
    # Not eligible on both counts
    assert is_eligible_for_bonus(performance_rating=2, years_of_service=1) is False

def test_format_currency():
    """Tests the currency formatting function."""
    assert format_currency(1234.56) == "$1,234.56"
    assert format_currency(100) == "$100.00"
    assert format_currency(9999999.99) == "$9,999,999.99"