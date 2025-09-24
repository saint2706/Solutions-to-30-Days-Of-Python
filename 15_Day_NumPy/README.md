# 📘 Day 15: NumPy - The Foundation of Numerical Computing

Welcome to the core of data analytics in Python. While Python's lists are flexible, they are not efficient for large-scale numerical operations. For this, we have **NumPy** (Numerical Python).

NumPy is the fundamental package for scientific and numerical computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the bedrock upon which almost all data science libraries, including Pandas, are built.

## Why NumPy for Business?

Imagine you have sales data for 10,000 products. If you wanted to apply a 5% price increase using a standard Python list, you would have to loop through every single item. With NumPy, you can perform this operation on the entire dataset at once. This is called **vectorization**.

Vectorization provides two key benefits:
1.  **Speed:** NumPy operations are performed in highly optimized, pre-compiled C code, making them orders of magnitude faster than Python loops.
2.  **Readability:** The code is much more concise and easier to read and write. `new_prices = prices * 1.05` is much clearer than a `for` loop.

## The NumPy Array

The core data structure in NumPy is the `ndarray` (n-dimensional array). It's similar to a Python list, but with a few key differences:
*   **Homogeneous:** All items in a NumPy array must be of the same data type (e.g., all integers or all floats).
*   **Fixed Size:** The size of an array cannot be changed once it is created.
*   **Efficient:** Takes up less memory and is much faster for numerical operations.

You typically create a NumPy array from a Python list.

```python
import numpy as np  # The standard alias for numpy

# From a list of product prices
prices_list = [19.99, 25.00, 15.50, 30.00]
prices_array = np.array(prices_list)
```

## Vectorized Operations

Here is where NumPy shines. You can perform mathematical operations on entire arrays at once, without a loop.

```python
import numpy as np

prices = np.array([19.99, 25.00, 15.50, 30.00])
units_sold = np.array([100, 80, 120, 90])

# Calculate revenue for each product at once
revenue_array = prices * units_sold
# Result: array([1999. , 2000. , 1860. , 2700. ])

# Calculate total revenue
total_revenue = revenue_array.sum() # Use the array's sum() method
```

## Useful Array Attributes and Methods

*   `array.shape`: Returns a tuple with the dimensions of the array.
*   `array.dtype`: Returns the data type of the array's elements.
*   `array.sum()`: Returns the sum of all elements.
*   `array.mean()`: Returns the average of all elements.
*   `array.max()` / `array.min()`: Returns the maximum or minimum element.
*   `array.std()`: Returns the standard deviation.

## 💻 Exercises: Day 15

1.  **Array Creation and Vectorization:**
    *   Create two Python lists: `prices = [12.50, 15.00, 22.50, 18.00]` and `units = [100, 85, 120, 95]`.
    *   Convert both lists into NumPy arrays.
    *   Calculate the total revenue for each product using a single vectorized multiplication.
    *   Print the resulting revenue array.

2.  **Sales Data Analysis:**
    *   You have a NumPy array of sales figures for a week: `sales_data = np.array([250, 300, 280, 450, 500, 220, 180])`.
    *   Calculate and print the following metrics:
        *   Total weekly sales (`.sum()`).
        *   The average daily sales (`.mean()`).
        *   The best sales day (`.max()`).
        *   The worst sales day (`.min()`).

3.  **Conditional Filtering with Arrays:**
    *   Using the `sales_data` array from the previous exercise, you can use a comparison operator to create a boolean array. For example: `high_days_boolean = sales_data > 300` will result in `[False, False, False, True, True, False, False]`.
    *   You can then use this boolean array to "index" the original array and select only the `True` values: `high_sales_days = sales_data[high_days_boolean]`.
    *   Perform this filtering to create a new array called `good_sales_days` containing only the sales figures greater than the average daily sales.
    *   Print the `good_sales_days` array.

🎉 **Fantastic start!** NumPy is the essential first step into the world of high-performance data analysis in Python. Understanding vectorization and the NumPy array will make all subsequent topics, especially Pandas, much easier to grasp.
