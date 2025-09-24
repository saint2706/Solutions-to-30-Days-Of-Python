"""Business Analytics Package for Python Learning.

This package contains utility modules for common business calculations
and operations, designed specifically for MBA students learning Python.

Modules:
    - arithmetics: Basic mathematical operations for business calculations
    - greet: Business greeting and messaging functions

Example Usage:
    from mypackage.arithmetics import add_numbers, multiply
    from mypackage.greet import greet_person
    
    # Calculate quarterly revenue total
    total_revenue = add_numbers(125000, 150000, 175000, 200000)
    
    # Generate customer greeting
    welcome_message = greet_person("Jane", "Smith")
"""

__version__ = "1.0.0"
__author__ = "30 Days of Python Course"

# Import key functions for easy access
from .arithmetics import add_numbers, subtract, multiply, divide, remainder, power
from .greet import greet_person

__all__ = [
    "add_numbers", 
    "subtract", 
    "multiply", 
    "divide", 
    "remainder", 
    "power",
    "greet_person"
]