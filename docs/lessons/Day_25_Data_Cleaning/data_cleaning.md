# 📘 Day 25: Data Cleaning - The Most Important Skill in Analytics

It's often said that data analysts spend about 80% of their time cleaning and preparing data. Messy, inconsistent data leads to incorrect analysis and bad business decisions. Learning to clean data effectively is a true superpower.

## Common Data Cleaning Tasks

- **Correcting Data Types:** Columns are often loaded with the wrong type (e.g., a 'Price' column with '$' symbols is read as a string). Use `.astype()` to convert columns to the correct type (e.g., `float`, `datetime64[ns]`).
- **String Manipulation:** Use the `.str` accessor on a Series to apply string methods to every element at once (e.g., `df['Category'].str.lower()`, `df['Region'].str.strip()`).
- **Standardizing Categories:** Use the `.replace()` method to consolidate inconsistent values (e.g., mapping "USA" and "United States" to a single category).
- **Handling Duplicates:** Use `df.drop_duplicates()` to remove duplicate rows. The `subset` parameter lets you define which columns to check for duplicates (e.g., `subset=['OrderID']`).

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `data_cleaning.py`, has been refactored to encapsulate the entire cleaning process into a single, reusable function.

1. **Review the Code:** Open `Day_25_Data_Cleaning/data_cleaning.py`. Examine the `clean_sales_data()` function, which performs all the cleaning steps on a DataFrame.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script. It will load the messy CSV, pass it to the cleaning function, and print the results.
   ```bash
   python Day_25_Data_Cleaning/data_cleaning.py
   ```
1. **Run the Tests:** The tests use a sample messy DataFrame created in memory to verify that the entire cleaning pipeline works as expected.
   ```bash
   pytest tests/test_day_25.py
   ```

## 💻 Exercises: Day 25

For these exercises, you will use the provided `messy_sales_data.csv` file.

1. **Load and Clean:**

   - In a new script (`my_solutions_25.py`), import `pandas` and the `clean_sales_data` function from the lesson script.
   - Load the `messy_sales_data.csv` file into a DataFrame.
   - Pass your DataFrame to the `clean_sales_data` function to get a cleaned version.

1. **Verify the Cleaning:**

   - On your new `cleaned_df`, perform the following checks and print the results:
     - Use `.info()` to confirm that 'Order Date' is a datetime and 'Price' is a float.
     - Print the unique values of the 'Product' column (`cleaned_df['Product'].unique()`) to confirm they are all lowercase.
     - Check the shape of the original DataFrame versus the cleaned one to see how many rows were removed.

🎉 **Incredible work!** Being able to take a messy, real-world dataset and turn it into a clean, analysis-ready format is arguably the most valuable skill a data analyst can possess.

Day 25: Data Cleaning in Practice (Optimized)

This script demonstrates common data cleaning techniques on a
messy, real-world-style dataset using Pandas. This version includes
performance optimizations.

```python

from pathlib import Path

import pandas as pd


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the sales data by correcting data types, standardizing text,
    and removing duplicates.
    """
    # --- 1. Correcting Data Types ---
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # Optimized price cleaning using a single regex
    df["Price"] = df["Price"].str.replace(r"[$,]", "", regex=True).astype(float)

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
    df_cleaned = clean_sales_data(
        df.copy()
    )  # Use a copy to avoid SettingWithCopyWarning

    # --- Inspect Cleaned Data ---
    print("\n--- Inspecting Cleaned Data ---")
    print("\nCleaned data types (df.info()):")
    df_cleaned.info()
    print("\nCleaned data head:")
    print(df_cleaned.head())
    print("\nUnique values in 'Region' column:", df_cleaned["Region"].unique())


if __name__ == "__main__":
    main()

```
