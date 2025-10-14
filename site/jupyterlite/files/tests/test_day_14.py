import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the functions from the business_logic module to be tested
from Day_14_Modules import business_logic as bl


def test_calculate_roi():
    """Tests the Return on Investment calculation."""
    assert bl.calculate_roi(investment=50000, profit=10000) == 20.0
    assert bl.calculate_roi(investment=1000, profit=0) == 0.0
    # Test edge case where investment is zero
    assert bl.calculate_roi(investment=0, profit=1000) == 0


def test_calculate_future_value():
    """Tests the future value calculation."""
    # FV = P(1+r)^n
    assert bl.calculate_future_value(principal=1000, rate=0.05, years=1) == 1050.0
    assert bl.calculate_future_value(principal=1000, rate=0.05, years=2) == 1102.5


def test_is_eligible_for_promotion():
    """Tests the employee promotion eligibility logic."""
    # Eligible: years > 3 and rating >= 4
    assert (
        bl.is_eligible_for_promotion(years_of_service=4, performance_rating=4) is True
    )
    assert (
        bl.is_eligible_for_promotion(years_of_service=5, performance_rating=5) is True
    )
    # Not eligible due to years
    assert (
        bl.is_eligible_for_promotion(years_of_service=3, performance_rating=5) is False
    )
    # Not eligible due to rating
    assert (
        bl.is_eligible_for_promotion(years_of_service=4, performance_rating=3) is False
    )


def test_format_as_currency():
    """Tests the currency formatting."""
    assert bl.format_as_currency(5000.75) == "$5,000.75"
    assert bl.format_as_currency(123) == "$123.00"
