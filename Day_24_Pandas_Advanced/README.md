# 📘 Day 24: Advanced Pandas - Working with Real Data

You'll rarely create data from scratch. The most common workflow is to load data from external sources like CSV files. Today, we'll focus on loading data and using powerful methods to select, filter, and clean it.

## Advanced Selection: `.loc` and `.iloc`

For complex selections, Pandas provides two powerful indexers:

*   **`.loc` (Label-based):** Selects data based on **row and column labels**.
    ```python
    # Selects row with index label 3, and only the 'Product' and 'Revenue' columns
    subset = df.loc[3, ['Product', 'Revenue']]
    ```
*   **`.iloc` (Integer-position based):** Selects data based on its **integer position**.
    ```python
    # Selects the first three rows (positions 0, 1, 2) and the first two columns (0, 1)
    subset = df.iloc[0:3, 0:2]
    ```

## Conditional Filtering (Boolean Indexing)

This is one of the most powerful features of Pandas. You can filter your DataFrame by providing a boolean (`True`/`False`) condition.

```python
# Find all high-revenue sales from the 'North' region
# Note the parentheses around each condition
high_rev_north = df[(df['Revenue'] > 50000) & (df['Region'] == 'North')]
```

## Handling Missing Data

Real-world data is often messy and has missing values, represented as `NaN`.

*   `df.isnull().sum()`: A crucial command to count missing values in each column.
*   `df.dropna()`: Drops rows that contain any missing values.
*   `df.fillna(value)`: Fills missing values with a specified value (e.g., 0 or the column's mean).

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `pandas_adv.py`, has been refactored to place each advanced operation into its own testable function.

1.  **Review the Code:** Open `Day_24_Pandas_Advanced/pandas_adv.py`. Examine functions like `filter_by_high_revenue()`, `filter_by_product_and_region()`, and `handle_missing_data()`.
2.  **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
    ```bash
    python Day_24_Pandas_Advanced/pandas_adv.py
    ```
3.  **Run the Tests:** The tests use a sample DataFrame created in memory, so they don't depend on the external CSV file.
    ```bash
    pytest tests/test_day_24.py
    ```

## 💻 Exercises: Day 24

1.  **Load and Inspect:**
    *   In a new script (`my_solutions_24.py`), import `pandas as pd` and `pathlib`.
    *   Load the `sales_data.csv` file (located in the `Day_24_Pandas_Advanced` directory) into a DataFrame.
    *   Use `.head()` and `.info()` to inspect the loaded data.

2.  **Select and Filter:**
    *   Using the DataFrame from the previous exercise, import and use the `filter_by_product_and_region` function to find all sales of `"Mouse"` in the `"South"` region. Print the result.
    *   Import and use the `filter_by_high_revenue` function to find all sales with revenue over $70,000.

3.  **Basic Data Cleaning:**
    *   Import the `handle_missing_data` function.
    *   Call the function twice on your DataFrame:
        *   Once with `strategy='drop'` to remove rows with missing data.
        *   Once with `strategy='fill'` to fill missing revenue with the column average.
    *   Print the `.shape` of both resulting DataFrames to see how they differ.

🎉 **Excellent work!** You're now working with data like a real analyst—loading it from files, inspecting it, and using powerful tools to filter and clean it. These are foundational skills for every data analysis project.