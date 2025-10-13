# 📘 Day 22: NumPy - The Foundation of Numerical Computing

While Python lists are flexible, they aren't efficient for large-scale numerical calculations. For this, we use **NumPy** (Numerical Python), the fundamental package for scientific and numerical computing in Python. It is the bedrock upon which almost all data science libraries, including Pandas, are built.

## Why NumPy for Business?

The core advantage of NumPy is **vectorization**. Instead of looping through 10,000 sales figures to apply a price increase, you can perform the operation on the entire dataset at once. This makes your code:

1. **Faster:** NumPy operations are performed in highly optimized C code, making them orders of magnitude faster than Python loops.
1. **More Readable:** `new_prices = prices * 1.05` is much clearer than a `for` loop.

## Key NumPy Concepts

- **`ndarray`:** The core data structure, a powerful N-dimensional array. It's like a Python list but faster and more memory-efficient.
- **Vectorized Operations:** Performing math on entire arrays at once (e.g., `revenue = prices_array * units_array`).
- **Array Methods:** NumPy arrays have built-in methods for fast calculations (e.g., `.sum()`, `.mean()`, `.max()`, `.std()`).
- **Boolean Indexing:** Using a conditional to create a boolean array (`True`/`False` values) and then using that array to filter your data.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries (including `numpy`).

## Exploring the Refactored Code

The script for this lesson, `numpy_examples.py`, has been refactored to place each NumPy task into its own testable function.

1. **Review the Code:** Open `Day_22_NumPy/numpy_examples.py`. Examine the functions `calculate_revenue_vectorized()`, `analyze_sales_data()`, and `filter_above_average()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_22_NumPy/numpy_examples.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function:
   ```bash
   pytest tests/test_day_22.py
   ```

## 💻 Exercises: Day 22

1. **Vectorized Revenue Calculation:**

   - In a new script (`my_solutions_22.py`), create two Python lists: `prices = [12.50, 15.00, 22.50]` and `units = [100, 85, 120]`.
   - Import the `calculate_revenue_vectorized` function from the lesson script.
   - Call the function with your lists and print the resulting NumPy array.

1. **Sales Data Analysis:**

   - You have a list of sales figures: `sales_data = [250, 300, 280, 450, 500, 220, 180]`.
   - Import and use the `analyze_sales_data` function to get a dictionary of statistics.
   - Print the total sales and the mean sales from the returned dictionary.

1. **Conditional Filtering with Arrays:**

   - Import the `filter_above_average` function and the `numpy` library (`import numpy as np`).
   - Create a NumPy array from your `sales_data` list from the previous exercise.
   - Pass this array to the `filter_above_average` function to get a new array containing only the sales figures that were better than average.
   - Print the resulting array.

🎉 **Fantastic start!** NumPy is the essential first step into the world of high-performance data analysis in Python. Understanding vectorization will make all subsequent topics, especially Pandas, much easier to grasp.

Day 22: NumPy in Action for Business Analytics (Refactored)

This script demonstrates fundamental NumPy operations for
efficient numerical analysis of business data. This version is
refactored into functions for better organization and testability.

```python

import numpy as np


def calculate_revenue_vectorized(prices: list, units: list) -> np.ndarray:
    """
    Calculates revenue by performing a vectorized multiplication of prices and units.
    """
    prices_array = np.array(prices)
    units_array = np.array(units)
    return prices_array * units_array


def analyze_sales_data(sales: list) -> dict:
    """
    Analyzes a list of sales data and returns a dictionary of key statistics.
    """
    sales_array = np.array(sales)
    if sales_array.size == 0:
        return {}

    return {
        "total": sales_array.sum(),
        "mean": sales_array.mean(),
        "max": sales_array.max(),
        "min": sales_array.min(),
        "std_dev": sales_array.std(),
    }


def filter_above_average(data: np.ndarray) -> np.ndarray:
    """
    Filters a NumPy array to return only the elements above its average.
    """
    if data.size == 0:
        return np.array([])

    average = data.mean()
    return data[data > average]


def main():
    """Main function to demonstrate NumPy capabilities."""
    # --- Example 1: Vectorized Calculations ---
    print("--- Calculating Revenue with Vectorization ---")
    prices_data = [12.50, 15.00, 22.50, 18.00, 19.99]
    units_data = [100, 85, 120, 95, 110]

    revenue_data = calculate_revenue_vectorized(prices_data, units_data)
    print(f"Prices array: {np.array(prices_data)}")
    print(f"Units sold array: {np.array(units_data)}")
    print(f"Revenue per product (vectorized): {revenue_data}")
    print("-" * 20)

    # --- Example 2: Sales Data Analysis ---
    print("--- Analyzing Weekly Sales Data ---")
    weekly_sales_data = [250, 300, 280, 450, 500, 220, 180]
    sales_stats = analyze_sales_data(weekly_sales_data)

    print(f"Sales for the week: {np.array(weekly_sales_data)}")
    print(f"Total weekly sales: ${sales_stats['total']:.2f}")
    print(f"Average daily sales: ${sales_stats['mean']:.2f}")
    print(f"Best sales day: ${sales_stats['max']:.2f}")
    print(f"Worst sales day: ${sales_stats['min']:.2f}")
    print(f"Standard deviation of sales: ${sales_stats['std_dev']:.2f}")
    print("-" * 20)

    # --- Example 3: Conditional Filtering ---
    print("--- Filtering for Above-Average Sales Days ---")
    sales_array = np.array(weekly_sales_data)
    good_days = filter_above_average(sales_array)

    print(f"The sales figures for good days were: {good_days}")
    print(f"Number of good sales days: {len(good_days)}")
    print("-" * 20)


if __name__ == "__main__":
    main()

```
