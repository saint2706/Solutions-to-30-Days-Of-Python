"""
Day 25: Data Cleaning in Practice (Optimized)

This script demonstrates common data cleaning techniques on a
messy, real-world-style dataset using Pandas. This version includes
performance optimizations.
"""

import pandas as pd
from pathlib import Path
import re

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the sales data by correcting data types, standardizing text,
    and removing duplicates.
    """
    # --- 1. Correcting Data Types ---
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # Optimized price cleaning using a single regex
    df["Price"] = df["Price"].str.replace(r'[$,]', '', regex=True).astype(float)

    # --- 2. Cleaning and Standardizing Text Data ---
    df["Region"] = df["Region"].str.strip().str.lower()
    df["Product"] = df["Product"].str.lower()
    df["Region"] = df["Region"].replace({"usa": "united states"})

    # --- 3. Handling Duplicates ---
    df.drop_duplicates(inplace=True)
    df.drop_duplicates(subset=["Order ID"], keep="first", inplace=True)

    return df

def main():
    """
    Main function to load, clean, and inspect the data.
    """
    # --- Load the Messy Data ---
    resource_dir = Path(__file__).resolve().parent
    data_path = resource_dir / "messy_sales_data.csv"

    print("--- Loading and Inspecting Messy Data ---")
    try:
        df = pd.read_csv(data_path)
        print("Original data types (df.info()):")
        df.info()
        print("\nOriginal data head:")
        print(df.head())
    except FileNotFoundError:
        print(
            "Error: messy_sales_data.csv not found in the Day_25_Data_Cleaning folder."
        )
        return

    # --- Clean the Data ---
    df_cleaned = clean_sales_data(df.copy()) # Use a copy to avoid SettingWithCopyWarning

    # --- Inspect Cleaned Data ---
    print("\n--- Inspecting Cleaned Data ---")
    print("\nCleaned data types (df.info()):")
    df_cleaned.info()
    print("\nCleaned data head:")
    print(df_cleaned.head())
    print("\nUnique values in 'Region' column:", df_cleaned["Region"].unique())


if __name__ == "__main__":
    main()