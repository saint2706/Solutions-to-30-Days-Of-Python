# 📘 Day 23: Pandas - Your Data Analysis Superpower

If NumPy is the foundation for numerical computing, **Pandas** is the tool you will use every single day for practical data analysis. It is, without exaggeration, the most important library for data manipulation in Python. Think of it as giving Python the capabilities of a super-powered spreadsheet, like Excel or Google Sheets.

With Pandas, you can easily load data from files (like CSVs or Excel), clean it, transform it, analyze it, and prepare it for visualization or machine learning.

## The Core Data Structures: Series and DataFrame

Pandas has two main data structures you need to know.

### 1. The Series

A **Series** is a one-dimensional, labeled array. It's like a single column in a spreadsheet.

```python
import pandas as pd  # The standard alias for pandas

# A Series of product prices
prices = pd.Series([19.99, 25.00, 15.50], index=["Product A", "Product B", "Product C"])
```

Here, `["Product A", "Product B", "Product C"]` is the **index**, which provides labels for the data.

### 2. The DataFrame

A **DataFrame** is a two-dimensional, labeled data structure with columns of potentially different types. It is the single most important data structure in Pandas. **It's a table**, just like in a spreadsheet or a SQL database.

You can think of a DataFrame as a collection of Series that share the same index.

## Creating Your First DataFrame

One of the most common ways to create a DataFrame is from a Python dictionary.

```python
import pandas as pd

# A dictionary of business data
data = {
    'Product Name': ["Laptop", "Mouse", "Keyboard", "Monitor"],
    'Category': ["Electronics", "Electronics", "Electronics", "Electronics"],
    'Price': [1200, 25, 75, 300],
    'Units Sold': [150, 300, 220, 180]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)
```

This `df` variable now holds a table of your data.

## Inspecting Your Data

Once you have a DataFrame, the first thing you'll always do is inspect it to understand its structure and content.

| Method         | Description                                        |
| :------------- | :------------------------------------------------- |
| `df.head()`    | Shows the first 5 rows of the DataFrame.           |
| `df.tail()`    | Shows the last 5 rows of the DataFrame.            |
| `df.info()`    | Provides a concise summary of the DataFrame, including data types and non-null values. |
| `df.describe()`| Generates descriptive statistics for the numerical columns (count, mean, std, min, max, etc.). |
| `df.shape`     | Returns a tuple representing the dimensionality (rows, columns). |

## Selecting Columns

You can easily select a single column from a DataFrame, which will return a Pandas Series.

```python
# Select the 'Price' column
prices_column = df['Price']

# Select multiple columns by passing a list of column names
product_and_price = df[['Product Name', 'Price']]
```

## 💻 Exercises: Day 23

1. **Create an Employee DataFrame:**
    * Create a Python dictionary to store data for 3-4 employees. Each employee should have a `Name`, `Department`, and `Salary`.
    * Convert this dictionary into a Pandas DataFrame.
    * Use `.head()` to display your DataFrame.
    * Use `.info()` to see the data types.

2. **Analyze Sales Data:**
    * Using the `df` DataFrame from the lesson above:
    * Select and print just the `Product Name` column.
    * Select and print the `Product Name` and `Units Sold` columns.
    * Use `.describe()` to get a statistical summary of the numerical columns (`Price` and `Units Sold`).

3. **Calculate a New Column:**
    * Using the `df` DataFrame from the lesson, create a new column called `'Revenue'`.
    * The value of this column should be the `'Price'` column multiplied by the `'Units Sold'` column.
    * Hint: `df['Revenue'] = df['Price'] * df['Units Sold']`
    * Display the DataFrame with the new `'Revenue'` column using `.head()`.

🎉 **Welcome to Pandas!** You've just learned how to create and inspect the most fundamental object in data analysis. In the next lesson, we'll learn how to load data from files and start doing more advanced selections and filtering.
