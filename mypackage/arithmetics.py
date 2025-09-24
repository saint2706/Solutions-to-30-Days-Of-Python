"""Business arithmetic operations module.

This module provides essential mathematical functions commonly used
in business calculations, such as financial analysis, inventory management,
and performance metrics calculations.
"""
from typing import Union

# Type alias for numeric types commonly used in business calculations
Number = Union[int, float]

def add_numbers(*args: Number) -> Number:
    """Calculate the sum of multiple numbers.
    
    Useful for calculating total revenue, total expenses, or aggregating
    multiple financial metrics across different business units.
    
    Args:
        *args: Variable number of numeric values to sum
        
    Returns:
        Number: The sum of all input numbers
        
    Example:
        >>> add_numbers(1000, 2500, 750)  # Q1, Q2, Q3 revenue
        4250
    """
    total = 0
    for num in args:
        total += num
    return total


def subtract(a: Number, b: Number) -> Number:
    """Subtract one number from another.
    
    Commonly used for calculating profit (revenue - costs),
    variance analysis, or determining changes between periods.
    
    Args:
        a (Number): The minuend (number to subtract from)
        b (Number): The subtrahend (number to subtract)
        
    Returns:
        Number: The difference (a - b)
        
    Example:
        >>> subtract(50000, 35000)  # Revenue - Costs
        15000
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.
    
    Essential for calculating total costs (quantity × unit_price),
    compound growth, or scaling business metrics.
    
    Args:
        a (Number): First multiplicand
        b (Number): Second multiplicand
        
    Returns:
        Number: The product of a and b
        
    Example:
        >>> multiply(100, 25.50)  # 100 units at $25.50 each
        2550.0
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide one number by another.
    
    Used for calculating ratios, averages, unit costs, or percentage
    calculations in business analysis.
    
    Args:
        a (Number): The dividend (number to be divided)
        b (Number): The divisor (number to divide by)
        
    Returns:
        float: The quotient (a / b)
        
    Raises:
        ZeroDivisionError: If b is zero
        
    Example:
        >>> divide(1000, 4)  # Total budget across 4 quarters
        250.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero in business calculations")
    return a / b


def remainder(a: Number, b: Number) -> Number:
    """Calculate the remainder after division.
    
    Useful for inventory management (remaining stock after packaging),
    shift scheduling, or resource allocation calculations.
    
    Args:
        a (Number): The dividend
        b (Number): The divisor
        
    Returns:
        Number: The remainder of a divided by b
        
    Raises:
        ZeroDivisionError: If b is zero
        
    Example:
        >>> remainder(100, 12)  # Items remaining after packing in dozens
        4
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate remainder with zero divisor")
    return a % b


def power(base: Number, exponent: Number) -> Number:
    """Raise a number to a given power.
    
    Used for compound interest calculations, exponential growth modeling,
    and advanced financial projections.
    
    Args:
        base (Number): The base number
        exponent (Number): The power to raise the base to
        
    Returns:
        Number: The result of base raised to the power of exponent
        
    Example:
        >>> power(1.05, 10)  # 5% annual growth over 10 years
        1.6288946267584238
    """
    return base ** exponent
