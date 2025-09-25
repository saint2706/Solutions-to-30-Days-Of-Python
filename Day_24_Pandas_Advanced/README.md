# 📘 Day 24: Advanced Pandas - Working with Real Data

In the real world, you rarely create your own data in a Python script. Instead, you load it from external sources like CSV files, Excel spreadsheets, or databases. Today, we'll focus on the most common scenario: working with CSV files. We'll also learn more powerful ways to select and filter the data you need.

## Loading Data from a CSV File

A CSV (Comma-Separated Values) file is a simple text file where values are separated by commas, making it a universal format for tabular data. Pandas makes reading these files incredibly easy with the `read_csv()` function.

```python
import pandas as pd

# Load data from a CSV file into a DataFrame
# This assumes the 'sales_data.csv' file is in the same directory
df = pd.read_csv('sales_data.csv')

# Always inspect the data after loading
print(df.head())
```

## Advanced Selection: `.loc` and `.iloc`

While selecting columns with `df['Column']` is easy, for more complex selections of rows and columns, Pandas provides two powerful indexers.

### `.loc`: Label-based Selection

Selects data based on the **row and column labels** (the index).

```python
# Select the row with index label 3
row_3 = df.loc[3]

# Select rows with index labels 1 through 4
rows_1_to_4 = df.loc[1:4]

# Select a single value: row label 2, column label 'Price'
price_of_product_2 = df.loc[2, 'Price']

# Select multiple rows and columns
subset = df.loc[1:3, ['Product Name', 'Revenue']]
```

### `.iloc`: Integer-position based Selection

Selects data based on the **integer position** (from 0 to length-1).

```python
# Select the first row (position 0)
first_row = df.iloc[0]

# Select the first 3 rows (positions 0, 1, 2)
first_three_rows = df.iloc[0:3]

# Select a single value: first row, second column
val = df.iloc[0, 1] # Row 0, Column 1

# Select multiple rows and columns by position
subset = df.iloc[0:3, [0, 2]] # Rows 0-2, Columns 0 and 2
```

## Conditional Filtering (Boolean Indexing)

This is one of the most powerful features of Pandas. You can filter your DataFrame by providing a boolean condition.

```python
# Find all sales from the 'North' region
north_sales = df[df['Region'] == 'North']

# Find all high-revenue sales
high_revenue = df[df['Revenue'] > 25000]

# Combine conditions with & (and) and | (or)
# Note the parentheses around each condition are required
high_rev_north = df[(df['Revenue'] > 25000) & (df['Region'] == 'North')]
```

## Handling Missing Data

Real-world data is messy. It often has missing values, which are represented in Pandas as `NaN` (Not a Number).

* `df.isnull()`: Returns a DataFrame of the same shape with `True` for `NaN` values and `False` otherwise.
* `df.isnull().sum()`: A very common command to quickly count the number of missing values in each column.
* `df.dropna()`: Drops rows that contain any missing values.
* `df.fillna(value)`: Fills missing values with a specified value (e.g., 0, the mean, or "N/A").

## 💻 Exercises: Day 24

For these exercises, you will use a provided `sales_data.csv` file.

1. **Load and Inspect:**
    * Load the `sales_data.csv` file into a Pandas DataFrame.
    * Use `.head()` to view the first few rows.
    * Use `.info()` to check the data types and look for missing values.
    * Use `.describe()` to get a statistical overview.

2. **Select and Filter:**
    * Select and display only the 'Product' and 'Revenue' columns for the first 5 rows using `.loc`.
    * Select all sales that occurred in the 'South' region using boolean indexing.
    * Select all sales where the 'Units Sold' were greater than 100 **and** the 'Revenue' was over $20,000.

3. **Basic Data Cleaning:**
    * The `sales_data.csv` file has some missing values in the 'Revenue' column.
    * First, count how many missing values are in each column using `.isnull().sum()`.
    * Create a new DataFrame called `df_cleaned` by dropping all rows with missing values using `.dropna()`.
    * Verify that the cleaned DataFrame has no missing values by running `.isnull().sum()` on it.
    * Alternatively, create another DataFrame `df_filled` where you fill the missing 'Revenue' with the average revenue of the entire column. (Hint: `mean_revenue = df['Revenue'].mean()`, then `df.fillna(...)`).

🎉 **Excellent work!** You're now working with data like a real analyst—loading it from files, inspecting it, and using powerful tools to filter and clean it. These are the foundational skills for every data analysis project.
