"""
Day 22: NumPy in Action for Business Analytics

This script demonstrates fundamental NumPy operations for
efficient numerical analysis of business data.
"""

# It is the standard convention to import numpy with the alias 'np'
import numpy as np

# --- Example 1: Array Creation and Vectorized Calculations ---
print("--- Calculating Revenue with Vectorization ---")
# Original data in Python lists
prices_list = [12.50, 15.00, 22.50, 18.00, 19.99]
units_list = [100, 85, 120, 95, 110]

# Convert lists to NumPy arrays
prices_array = np.array(prices_list)
units_array = np.array(units_list)
print(f"Prices array: {prices_array}")
print(f"Units sold array: {units_array}")

# With NumPy, we can multiply the arrays directly. No 'for' loop needed!
# This is called a vectorized operation.
revenue_array = prices_array * units_array

print(f"Revenue per product (vectorized): {revenue_array}")
print("-" * 20)


# --- Example 2: Sales Data Analysis with Array Methods ---
print("--- Analyzing Weekly Sales Data ---")
# A NumPy array of sales figures for a week
sales_data = np.array([250, 300, 280, 450, 500, 220, 180])
print(f"Sales for the week: {sales_data}")

# NumPy arrays have built-in methods for common calculations.
total_sales = sales_data.sum()
average_sales = sales_data.mean()
best_day = sales_data.max()
worst_day = sales_data.min()
sales_std_dev = sales_data.std()  # Standard deviation

print(f"Total weekly sales: ${total_sales:.2f}")
print(f"Average daily sales: ${average_sales:.2f}")
print(f"Best sales day: ${best_day:.2f}")
print(f"Worst sales day: ${worst_day:.2f}")
print(f"Standard deviation of sales: ${sales_std_dev:.2f}")
print("-" * 20)


# --- Example 3: Conditional Filtering with Boolean Arrays ---
print("--- Filtering for Above-Average Sales Days ---")
# The power of NumPy allows you to filter arrays using a condition.

# This comparison creates a boolean array: [False, False, False, True, True, False, False]
above_average_bool = sales_data > average_sales
print(f"Days with above-average sales (boolean mask): {above_average_bool}")

# You can use this boolean array to "index" the original array.
# This selects only the elements where the boolean array is True.
good_sales_days = sales_data[above_average_bool]

print(f"The sales figures for good days were: {good_sales_days}")
print(f"Number of good sales days: {len(good_sales_days)}")
print("-" * 20)
