# 📘 Day 25: Data Cleaning - The Most Important Skill in Analytics

Welcome to one of the most critical topics in this course. It's often said that data analysts spend about 80% of their time cleaning and preparing data, and only 20% actually analyzing it. Messy, inconsistent data leads to incorrect analysis and bad business decisions. Learning to clean data effectively is a true superpower.

Today, we'll build on our Pandas knowledge to tackle common data messes.

## Correcting Data Types

Often, data is loaded from a file with the wrong data type. A numerical column like 'Price' might be loaded as a string (an "object" in Pandas terms) if it contains currency symbols or commas.

```python
# df['Price'] might be '$1,200.00' (a string)
# We need to remove the symbols and convert it to a float.
df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)

# The .astype() method is used to cast a column to a specified data type.
```

## String Manipulation on Columns

Pandas Series have a special `.str` accessor that lets you apply string methods to every element in the column at once. This is incredibly powerful for cleaning text data.

```python
# Standardize a column to be all lowercase
df['Category'] = df['Category'].str.lower()

# Remove leading/trailing whitespace from a column
df['Product Name'] = df['Product Name'].str.strip()
```

## Handling Inconsistent Categorical Data

Categorical data often has inconsistencies. For example, a 'Country' column might have "USA", "U.S.A.", and "United States". These all mean the same thing and should be standardized. The `.replace()` method is perfect for this.

```python
# Create a mapping of wrong values to the correct one
country_map = {"U.S.A.": "USA", "United States": "USA"}

# Apply the replacement
df['Country'] = df['Country'].replace(country_map)
```

## Finding and Removing Duplicates

Duplicate rows can skew your analysis (e.g., by double-counting revenue). Pandas provides easy ways to find and remove them.

* `df.duplicated()`: Returns a boolean Series indicating which rows are duplicates.
* `df.drop_duplicates()`: Returns a new DataFrame with duplicate rows removed. You can specify a `subset` of columns to consider when identifying duplicates.

```python
# Find all rows that are complete duplicates
duplicate_rows = df[df.duplicated()]

# Remove duplicate rows, keeping the first instance
df_no_duplicates = df.drop_duplicates()

# Remove rows where the 'OrderID' is duplicated
df_unique_orders = df.drop_duplicates(subset=['OrderID'])
```

## 💻 Exercises: Day 25

For these exercises, you will use a provided `messy_sales_data.csv` file.

1. **Load and Initial Clean:**
    * Load the `messy_sales_data.csv` file into a DataFrame.
    * The 'Order Date' column is loaded as a string. Convert it to a proper datetime type using `pd.to_datetime(df['Order Date'])`.
    * The 'Price' column is a string with '$' and commas. Clean it and convert it to a float data type.
    * The 'Region' column has extra whitespace. Clean it up.

2. **Standardize Categories:**
    * The 'Product' column has inconsistent capitalization (e.g., "Laptop", "laptop"). Standardize the entire column to lowercase so you can accurately group products later.
    * The 'Region' column has both "USA" and "United States". Standardize them all to be "USA".

3. **Handle Duplicates:**
    * Use `.duplicated().sum()` to check for and count any fully duplicate rows in the dataset.
    * Create a new DataFrame called `df_cleaned` that has these duplicate rows removed.
    * Check if any orders have the same 'Order ID'. If so, create a final DataFrame `df_final` that keeps only the *first* occurrence of each 'Order ID'.

🎉 **Incredible work!** You've just learned the foundational techniques for data wrangling. Being able to take a messy, real-world dataset and turn it into a clean, analysis-ready format is arguably the most valuable skill a data analyst can possess.
