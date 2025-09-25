"""
Day 36: Solution to the Capstone Case Study
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1 & 2: Load and Clean the Data ---
print("--- Step 1 & 2: Loading and Cleaning Data ---")
try:
    df = pd.read_csv("case_study_sales.csv", parse_dates=["Date"])
    print("Data loaded successfully.")

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print("Missing values found. Dropping rows with missing data.")
        df.dropna(inplace=True)

    # Add a 'Revenue' column for analysis
    df["Revenue"] = df["Price"] * df["Units Sold"]

    print("Data cleaned and 'Revenue' column created.")

except FileNotFoundError:
    print("Error: case_study_sales.csv not found.")
    df = pd.DataFrame()

if not df.empty:
    # --- Step 3: Exploratory Data Analysis (EDA) ---
    print("\n--- Step 3: Answering Key Business Questions ---")

    # 1. Top 5 products by total revenue
    top_products = (
        df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
    )
    print("\n1. Top 5 Products by Revenue:")
    print(top_products)

    # 2. Top sales region by revenue
    top_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    print("\n2. Revenue by Region:")
    print(top_region)

    # 3. Correlation between Price and Units Sold
    correlation = df[["Price", "Units Sold"]].corr()
    print("\n3. Correlation between Price and Units Sold:")
    print(correlation)

    # --- Step 4: Visualize Your Findings ---
    print("\n--- Step 4: Generating Visualizations ---")

    # Plot 1: Top 5 Products by Revenue
    plt.figure(figsize=(10, 6))
    top_products.plot(kind="bar")
    plt.title("Top 5 Products by Total Revenue", fontsize=16)
    plt.ylabel("Total Revenue ($)")
    plt.xlabel("Product")
    plt.xticks(rotation=45)
    print("Displaying plot 1...")
    plt.show()

    # Plot 2: Revenue by Region
    plt.figure(figsize=(10, 6))
    top_region.plot(kind="pie", autopct="%1.1f%%", startangle=90)
    plt.title("Revenue Contribution by Region", fontsize=16)
    plt.ylabel("")  # Hide the y-label for pie charts
    print("Displaying plot 2...")
    plt.show()

    # Plot 3: Daily Revenue Trend
    daily_revenue = df.groupby("Date")["Revenue"].sum()
    plt.figure(figsize=(12, 6))
    daily_revenue.plot(kind="line")
    plt.title("Daily Revenue Trend", fontsize=16)
    plt.ylabel("Total Revenue ($)")
    plt.xlabel("Date")
    print("Displaying plot 3...")
    plt.show()

    # --- Step 5: Summary and Recommendations ---
    print("\n--- Step 5: Summary and Recommendations ---")
    summary = """
    Key Insights:
    1. The 'Laptop' is by far the highest-grossing product, generating significantly more revenue than any other item.
    2. The 'North' and 'South' regions are our top-performing territories, contributing the majority of the revenue.
    3. There is a weak negative correlation between price and units sold, which is expected but not strong enough to be a primary driver.

    Recommendations:
    1. Double-down on Laptop sales: Focus marketing campaigns and inventory management on our best-selling product, the Laptop.
    2. Regional Focus: Allocate additional sales resources to the North and South regions to maximize growth. Investigate why the East and West regions are underperforming in comparison.
    """
    print(summary)

else:
    print("\nSkipping analysis as DataFrame could not be loaded.")
