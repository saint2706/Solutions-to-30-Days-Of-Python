"""
Day 13: Elegant Data Manipulation with List Comprehensions

This script demonstrates how to use list comprehensions to
efficiently transform and filter lists of business data.
"""

# --- Example 1: Transforming Data (Applying a Price Increase) ---
print("--- Applying a Price Increase ---")
prices = [100.00, 150.50, 200.00, 80.25]
print(f"Original prices: {prices}")

# The 'for' loop way (for comparison)
new_prices_loop = []
for price in prices:
    new_prices_loop.append(price * 1.1)

# The list comprehension way
# [expression for item in iterable]
new_prices_comp = [price * 1.1 for price in prices]

print(f"New prices (from loop): {[f'${p:.2f}' for p in new_prices_loop]}")
print(f"New prices (from comprehension): {[f'${p:.2f}' for p in new_prices_comp]}")
print("-" * 20)


# --- Example 2: Filtering Data (Finding Large Sales) ---
print("--- Filtering for Large Sales Transactions ---")
sales = [500, 1200, 800, 1500, 300, 2500]
print(f"All sales: {sales}")

# The 'for' loop way (for comparison)
large_sales_loop = []
for sale in sales:
    if sale > 1000:
        large_sales_loop.append(sale)

# The list comprehension way with a condition
# [expression for item in iterable if condition]
large_sales_comp = [sale for sale in sales if sale > 1000]

print(f"Large sales (from loop): {large_sales_loop}")
print(f"Large sales (from comprehension): {large_sales_comp}")
print("-" * 20)


# --- Example 3: Filtering and Transforming (Complex Example) ---
print("--- Extracting Names of High-Performing Sales Staff ---")
employees = [
    {"name": "Alice", "department": "Sales", "quarterly_sales": 12000},
    {"name": "Bob", "department": "Engineering", "quarterly_sales": 0},
    {"name": "Charlie", "department": "Sales", "quarterly_sales": 8000},
    {"name": "David", "department": "Sales", "quarterly_sales": 15000}
]
sales_target = 10000

# We want to get the names of sales staff who exceeded the target.
# The expression transforms the item (employee dict) into just the name.
# The condition filters for the correct department AND sales amount.
top_performers = [
    employee["name"]
    for employee in employees
    if employee["department"] == "Sales" and employee["quarterly_sales"] > sales_target
]

print(f"Top performing sales staff (sales > ${sales_target}): {top_performers}")
print("-" * 20)
