"""
Day 14: Using Modules to Organize Code

This script demonstrates how to import and use functions from
both custom-built modules and Python's built-in modules.
"""

# --- Importing a custom module ---
# We are importing the functions we created in the 'business_logic.py' file.
# We use an alias 'bl' to keep our code clean and concise.
import business_logic as bl
import datetime
import math

print("--- Using Custom Business Logic Module ---")
# Now we can use the functions from our module using the 'bl.' prefix.
investment_amount = 50000
profit_amount = 12000
roi = bl.calculate_roi(investment_amount, profit_amount)
print(
    f"A project with an investment of {bl.format_as_currency(investment_amount)} and profit of {bl.format_as_currency(profit_amount)} has an ROI of {roi:.2f}%."
)

# Check promotion eligibility for an employee
years = 4
rating = 5
is_eligible = bl.is_eligible_for_promotion(years, rating)
print(
    f"An employee with {years} years of service and a rating of {rating} is eligible for promotion: {is_eligible}"
)
print("-" * 20)


# --- Using Python's Built-in Modules ---
print("--- Using Built-in 'datetime' and 'math' Modules ---")

# The 'datetime' module is essential for working with dates and times.
current_datetime = datetime.datetime.now()
print(f"Current Date and Time: {current_datetime}")
print(f"Current Year: {current_datetime.year}")
print(f"Current Month: {current_datetime.month}")
print(f"Current Day: {current_datetime.day}")
print()

# The 'math' module provides access to more advanced mathematical functions.
marketing_budget = 100000
# Let's say sales are proportional to the square root of the marketing budget.
growth_factor = math.sqrt(marketing_budget)
print(
    f"The growth factor for a marketing budget of {bl.format_as_currency(marketing_budget)} is {growth_factor:.2f}."
)
print("-" * 20)
