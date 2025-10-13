# 📘 Day 23: Pandas - Your Data Analysis Superpower

If NumPy is the foundation, **Pandas** is the tool you will use every single day for practical data analysis. It is the most important library for data manipulation in Python, giving it the capabilities of a super-powered spreadsheet.

## The Core Data Structures: Series and DataFrame

- **`Series`**: A one-dimensional labeled array, like a single column in a spreadsheet.
- **`DataFrame`**: A two-dimensional labeled table with columns of potentially different types. This is the primary object you will work with in Pandas.

## Key DataFrame Operations

- **Creation:** Create a DataFrame from a dictionary (`pd.DataFrame(my_dict)`) or by reading a file (`pd.read_csv('my_file.csv')`).
- **Inspection:** Always inspect your data after loading.
  - `df.head()`: Shows the first 5 rows.
  - `df.info()`: Provides a summary of columns, data types, and non-null values.
  - `df.describe()`: Generates descriptive statistics for numerical columns.
- **Selection:** Select a single column (`df['ColumnName']`) or multiple columns (`df[['Col1', 'Col2']]`).
- **Vectorized Operations:** Create new columns by performing operations on existing ones (e.g., `df['Revenue'] = df['Price'] * df['Units Sold']`).

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries (including `pandas`).

## Exploring the Refactored Code

The content for this lesson is split into two main files:

1. **`pandas_introduction.ipynb`**: A new Jupyter Notebook that interactively walks through creating a DataFrame from scratch, inspecting it, and creating a visualization. This is the recommended starting point for this lesson.
1. **`pandas_from_csv.py`**: A refactored Python script that demonstrates the more common workflow of loading data from a CSV file and filtering it.

### Running the Code

- To explore the notebook, you'll need to have Jupyter installed (`pip install jupyter`) and run `jupyter notebook` from your terminal.
- To run the script from the root directory of the project (`Coding-For-MBA`):
  ```bash
  python Day_23_Pandas/pandas_from_csv.py
  ```
- To run the tests for the script:
  ```bash
  pytest tests/test_day_23.py
  ```

## 💻 Exercises: Day 23

1. **Create an Employee DataFrame:**

   - In a new script (`my_solutions_23.py`), create a Python dictionary to store data for 3-4 employees (e.g., `Name`, `Department`, `Salary`).
   - Convert this dictionary into a Pandas DataFrame and print it.

1. **Analyze Sales Data from a File:**

   - Import the `load_data_from_csv` and `filter_by_title` functions from the `pandas_from_csv` script.
   - The path to the data file is `data/hacker_news.csv`. Load it using the function.
   - Use the `filter_by_title` function to find all articles with "Google" in the title and print their titles.

1. **Calculate a New Column:**

   - Create a DataFrame with `'Price'` and `'Units Sold'` columns.
   - Create a new column called `'Revenue'` by multiplying the 'Price' and 'Units Sold' columns.
   - Display the DataFrame with the new `'Revenue'` column.

🎉 **Welcome to Pandas!** You've just learned how to create and inspect the most fundamental object in data analysis. In the next lesson, we'll dive deeper into selecting, filtering, and cleaning data.

Day 23: Introduction to Pandas

This script demonstrates how to create a Pandas DataFrame,
the primary data structure for data analysis, and how to
perform basic inspections.

```python

# The standard convention for importing pandas is to use the alias 'pd'
import pandas as pd

# --- Creating a DataFrame from a Dictionary ---
# This is a common way to create a DataFrame from scratch.
# The keys of the dictionary become the column names.
# The lists of values become the data in those columns.
data = {
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics",
        "Peripherals",
    ],
    "Price": [1200, 25, 75, 300, 50],
    "Units Sold": [150, 300, 220, 180, 250],
}

# Create the DataFrame
df = pd.DataFrame(data)


# --- Inspecting the DataFrame ---
# These are the first commands you should run after creating or loading a DataFrame.
print("--- Inspecting the DataFrame ---")

# .head() shows the first 5 rows
print("First 5 rows of the data (df.head()):")
print(df.head())
print("-" * 20)

# .info() gives a summary of the DataFrame's structure
print("DataFrame summary (df.info()):")
df.info()
print("-" * 20)

# .describe() provides descriptive statistics for numerical columns
print("Descriptive statistics (df.describe()):")
print(df.describe())
print("-" * 20)


# --- Selecting Columns ---
print("--- Selecting Columns ---")

# To select a single column, use its name in square brackets.
# This returns a Pandas Series.
price_column = df["Price"]
print("The 'Price' column (a Pandas Series):")
print(price_column)
print()

# To select multiple columns, pass a list of column names.
# This returns a new, smaller DataFrame.
product_and_sales = df[["Product Name", "Units Sold"]]
print("The 'Product Name' and 'Units Sold' columns (a new DataFrame):")
print(product_and_sales)
print("-" * 20)


# --- Creating a New Column (Vectorized Operation) ---
print("--- Creating a New 'Revenue' Column ---")
# Like NumPy, Pandas allows for vectorized operations.
# We can multiply two columns together without a loop.
df["Revenue"] = df["Price"] * df["Units Sold"]

print("DataFrame after adding 'Revenue' column (df.head()):")
print(df.head())
print("-" * 20)

```
