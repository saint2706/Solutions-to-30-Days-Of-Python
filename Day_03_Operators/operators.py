"""
Day 3: Operators in Action for Business Analysis

This script demonstrates how different Python operators can be used
to perform business calculations and logical checks.
"""

# --- Arithmetic Operators for Financial Calculations ---
print("--- Financial Calculations ---")

# Example: Calculating compound interest
# Formula: A = P(1 + r/n)^(nt)
# For simplicity, we'll do annual compounding (n=1)
principal = 10000  # Initial investment
rate = 0.05        # Annual interest rate (5%)
time = 3           # Number of years

# The ** operator is used for exponents
final_amount = principal * (1 + rate) ** time

print(f"Investment of ${principal} after {time} years at {rate*100}% interest will be: ${final_amount:.2f}")
print("-" * 20)


# --- Assignment Operators for Accumulating Data ---
print("--- Accumulating Daily Sales ---")
total_sales = 0
daily_sale_day1 = 1500
daily_sale_day2 = 2200
daily_sale_day3 = 1850

# The += operator is a shorthand to add a value to a variable
total_sales += daily_sale_day1
total_sales += daily_sale_day2
total_sales += daily_sale_day3

print(f"Total sales after 3 days: ${total_sales}")
print("-" * 20)


# --- Comparison Operators for Business Rules ---
print("--- Inventory and Sales Target Checks ---")
inventory_count = 45
low_stock_threshold = 50

# The < operator checks if a value is less than another
is_low_stock = inventory_count < low_stock_threshold
print(f"Is inventory low? {is_low_stock}")

sales_target = 250000
current_sales = 265000

# The >= operator checks for "greater than or equal to"
target_met = current_sales >= sales_target
print(f"Has the sales target been met? {target_met}")
print("-" * 20)


# --- Logical Operators for Complex Eligibility Rules ---
print("--- Sales Bonus Eligibility Test ---")

# Scenario 1: High sales, but new employee
sales = 12000
years_of_service = 1
top_performer_last_quarter = False

# The 'and' requires both conditions to be true
# The 'or' allows either condition to be true
is_eligible = (sales > 10000 and years_of_service > 2) or top_performer_last_quarter
print(f"Scenario 1 (High Sales, New Employee): Eligible? {is_eligible}")

# Scenario 2: Lower sales, but a top performer
sales = 8000
years_of_service = 3
top_performer_last_quarter = True
is_eligible = (sales > 10000 and years_of_service > 2) or top_performer_last_quarter
print(f"Scenario 2 (Top Performer): Eligible? {is_eligible}")

# Scenario 3: Not eligible on either count
sales = 9000
years_of_service = 1
top_performer_last_quarter = False
is_eligible = (sales > 10000 and years_of_service > 2) or top_performer_last_quarter
print(f"Scenario 3 (Not Eligible): Eligible? {is_eligible}")
