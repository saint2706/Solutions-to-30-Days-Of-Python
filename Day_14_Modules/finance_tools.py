"""
Day 12: Exercise 1 Module

This file is the 'finance_tools' module required by Exercise 1.
It contains functions for calculating ROI and future value.
"""


def calculate_roi(investment: float, profit: float) -> float:
    """Calculates the Return on Investment (ROI) as a percentage."""
    if investment == 0:
        return 0
    return (profit / investment) * 100


def calculate_future_value(principal: float, rate: float, years: int) -> float:
    """Calculates the future value of an investment with annual compounding."""
    return principal * ((1 + rate) ** years)
