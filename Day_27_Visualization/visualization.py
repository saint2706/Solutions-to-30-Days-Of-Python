"""
Day 27: Creating Business Visualizations

This script demonstrates how to create common business charts
using the Seaborn and Matplotlib libraries with a sample dataset.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Load and Prepare Data ---
# We use the cleaned data from Day 24 for reliable plotting.
try:
    # parse_dates=['Date'] tells pandas to automatically convert the 'Date' column
    df = pd.read_csv(r"Day_24_Pandas_Advanced\sales_data.csv", parse_dates=["Date"])
    df.dropna(inplace=True)  # Drop rows with missing values for simplicity
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: sales_data.csv not found. Please run Day 24 first.")
    df = pd.DataFrame()


if not df.empty:
    # --- 1. Bar Chart: Sales by Region ---
    plt.figure(figsize=(10, 6))  # Create a figure with a specific size
    sns.barplot(x="Region", y="Revenue", data=df, estimator=sum, errorbar=None)
    plt.title("Total Revenue by Region", fontsize=16)
    plt.ylabel("Total Revenue ($)")
    plt.xlabel("Region")
    # plt.savefig('revenue_by_region.png') # You can save the plot to a file
    print(
        "Displaying Bar Chart: Total Revenue by Region. Please close the plot window to continue."
    )
    plt.show()

    # --- 2. Line Chart: Revenue Over Time ---
    # We group by date to ensure one data point per day
    daily_revenue = df.groupby("Date")["Revenue"].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Revenue", data=daily_revenue)
    plt.title("Daily Revenue Trend", fontsize=16)
    plt.xlabel("Date")
    plt.ylabel("Total Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for rotated labels
    print(
        "Displaying Line Chart: Daily Revenue Trend. Please close the plot window to continue."
    )
    plt.show()

    # --- 3. Histogram: Distribution of Units Sold ---
    plt.figure(figsize=(10, 6))
    sns.histplot(x="Units Sold", data=df, bins=10, kde=True)  # kde adds a density curve
    plt.title("Distribution of Units Sold per Transaction", fontsize=16)
    plt.xlabel("Units Sold")
    plt.ylabel("Frequency")
    print(
        "Displaying Histogram: Distribution of Units Sold. Please close the plot window to continue."
    )
    plt.show()

    # --- 4. Scatter Plot: Price vs. Units Sold ---
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Price", y="Units Sold", data=df, hue="Product")
    plt.title("Price vs. Units Sold", fontsize=16)
    plt.xlabel("Price ($)")
    plt.ylabel("Units Sold")
    plt.legend(title="Product")
    print(
        "Displaying Scatter Plot: Price vs. Units Sold. Please close the plot window to continue."
    )
    plt.show()
