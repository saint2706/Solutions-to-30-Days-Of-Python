"""
Day 17: Advanced Pandas - Working with Real Data

This script demonstrates loading data from a CSV file and
using advanced selection and cleaning techniques with Pandas.
"""

import pandas as pd

# --- Loading Data from a CSV File ---
print("--- Loading and Inspecting sales_data.csv ---")
# This command reads the CSV file in the same directory into a DataFrame.
df = pd.read_csv(r"Day_24_Pandas_Advanced\sales_data.csv")

# Always inspect after loading
print("First 5 rows (df.head()):")
print(df.head())
print("\nDataFrame Info (df.info()):")
df.info()
print("-" * 20)


# --- Advanced Selection with .loc and .iloc ---
print("--- Advanced Data Selection ---")
# .loc selects by label (in this case, the default integer index)
# Select row with index 3 and the 'Product' and 'Revenue' columns
product_3_revenue = df.loc[3, ["Product", "Revenue"]] # pyright: ignore[reportCallIssue, reportArgumentType]
print(f"Product and Revenue for row index 3 (using .loc):\n{product_3_revenue}\n")

# .iloc selects by integer position
# Select the first row (position 0) and the first three columns (positions 0, 1, 2)
row_0_cols_0_to_2 = df.iloc[0, 0:3]
print(f"First row, first 3 columns (using .iloc):\n{row_0_cols_0_to_2}\n")
print("-" * 20)


# --- Conditional Filtering (Boolean Indexing) ---
print("--- Conditional Filtering ---")
# Create a boolean mask
high_revenue_mask = df["Revenue"] > 50000

# Apply the mask to the DataFrame
high_revenue_sales = df[high_revenue_mask]
print("All sales with revenue > $50,000:")
print(high_revenue_sales)
print()

# Combine multiple conditions
# Find all 'Laptop' sales in the 'North' region
laptop_north_sales = df[(df["Product"] == "Laptop") & (df["Region"] == "North")]
print("All 'Laptop' sales in the 'North' region:")
print(laptop_north_sales)
print("-" * 20)


# --- Handling Missing Data ---
print("--- Handling Missing Data ---")
# First, check for missing values in each column
print("Count of missing values per column:")
print(df.isnull().sum())
print()

# Option 1: Drop rows with any missing values
df_cleaned = df.dropna()
print("Shape of original df:", df.shape)
print("Shape of cleaned df (after dropna):", df_cleaned.shape)
print()

# Option 2: Fill missing values
# We'll fill the missing 'Revenue' with the mean of the existing revenue values
mean_revenue = df["Revenue"].mean()
df_filled = df.copy()  # Make a copy to keep the original df unchanged
df_filled["Revenue"] = df_filled["Revenue"].fillna(mean_revenue)

print("Info for the DataFrame with filled values (df_filled.info()):")
df_filled.info()
print("-" * 20)
