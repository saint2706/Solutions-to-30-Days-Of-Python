"""
Day 18: Data Cleaning in Practice

This script demonstrates common data cleaning techniques on a
messy, real-world-style dataset using Pandas.
"""

import pandas as pd

# --- Load the Messy Data ---
print("--- Loading and Inspecting Messy Data ---")
try:
    df = pd.read_csv('messy_sales_data.csv')
    print("Original data types (df.info()):")
    df.info()
    print("\nOriginal data head:")
    print(df.head())
except FileNotFoundError:
    print("Error: messy_sales_data.csv not found.")
    df = pd.DataFrame() # Create empty df to prevent crash

if not df.empty:
    # --- 1. Correcting Data Types ---
    print("\n--- 1. Correcting Data Types ---")

    # Convert 'Order Date' to datetime objects
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Clean and convert 'Price' column to float
    # .str accessor works on Series to apply string methods element-wise
    df['Price'] = df['Price'].str.replace('$', '').str.replace(',', '').astype(float)

    print("\nData types after correction (df.info()):")
    df.info()
    print("\nHead after data type correction:")
    print(df.head())

    # --- 2. Cleaning and Standardizing Text Data ---
    print("\n--- 2. Standardizing Text Data ---")

    # Use .str.strip() to remove leading/trailing whitespace
    df['Region'] = df['Region'].str.strip()

    # Use .str.lower() to standardize product names
    df['Product'] = df['Product'].str.lower()

    # Use .replace() to standardize categorical data
    df['Region'] = df['Region'].replace({"USA": "United States"})

    print("\n'Region' and 'Product' columns after cleaning:")
    print(df[['Region', 'Product']].head())
    print("\nUnique values in 'Region' column:", df['Region'].unique())

    # --- 3. Handling Duplicates ---
    print("\n--- 3. Handling Duplicates ---")

    # Check for fully duplicate rows
    duplicate_row_count = df.duplicated().sum()
    print(f"\nNumber of fully duplicate rows found: {duplicate_row_count}")

    # Remove full duplicates
    df_no_rows = df.drop_duplicates()
    print(f"Shape after dropping full duplicates: {df_no_rows.shape}")

    # Check for duplicate Order IDs
    duplicate_order_id_count = df_no_rows.duplicated(subset=['Order ID']).sum()
    print(f"\nNumber of duplicate Order IDs found: {duplicate_order_id_count}")

    # Remove duplicates based on a subset of columns, keeping the first entry
    df_final = df_no_rows.drop_duplicates(subset=['Order ID'], keep='first')
    print(f"Shape after dropping duplicate Order IDs: {df_final.shape}")

    print("\nFinal cleaned data head:")
    print(df_final.head())
