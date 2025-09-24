"""
Day 20: Advanced Visualization and Customization

This script demonstrates how to customize plots for presentation
and arrange multiple plots into a single dashboard figure.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Load and Prepare Data ---
try:
    df = pd.read_csv(r"Day_24_Pandas_Advanced\sales_data.csv", parse_dates=["Date"])
    df.dropna(inplace=True)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: sales_data.csv not found in '17_Day_Pandas_Adv' directory.")
    df = pd.DataFrame()

if not df.empty:
    # --- 1. Creating a Single, Customized Plot ---
    print("\n--- 1. Creating a Customized Plot ---")

    # Calculate average revenue to use as a target line
    avg_revenue = df["Revenue"].mean()

    plt.figure(figsize=(12, 7))
    sns.barplot(
        x="Product",
        y="Revenue",
        data=df,
        estimator=sum,
        errorbar=None,
        palette="viridis",
    )

    # --- Customizations ---
    plt.title("Total Revenue per Product", fontsize=18, weight="bold")
    plt.xlabel("Product Category", fontsize=12)
    plt.ylabel("Total Revenue (in USD)", fontsize=12)
    plt.xticks(rotation=45)  # Rotate labels if they overlap

    # Add a horizontal line for the average revenue
    plt.axhline(
        y=avg_revenue,
        color="red",
        linestyle="--",
        label=f"Avg Revenue (${avg_revenue:,.2f})",
    )
    plt.legend()  # Display the label for the line

    plt.tight_layout()
    # Save the figure before showing it
    # plt.savefig('customized_product_revenue.png', dpi=300)
    print(
        "Displaying customized product revenue plot. Please close the plot window to continue."
    )
    plt.show()

    # --- 2. Creating a Dashboard with Subplots ---
    print("\n--- 2. Creating a 2x1 Dashboard ---")

    # Create a figure and a set of subplots. 2 rows, 1 column.
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

    # --- Top Plot: Revenue Trend ---
    daily_revenue = df.groupby("Date")["Revenue"].sum().reset_index()
    sns.lineplot(x="Date", y="Revenue", data=daily_revenue, ax=axes[0], color="blue")
    axes[0].set_title("Daily Revenue Trend", fontsize=14)
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Revenue ($)")

    # --- Bottom Plot: Revenue Distribution ---
    sns.histplot(data=df, x="Revenue", bins=15, kde=True, ax=axes[1], color="green")
    axes[1].set_title("Distribution of Individual Sale Revenue", fontsize=14)
    axes[1].set_xlabel("Revenue per Sale ($)")
    axes[1].set_ylabel("Frequency")

    # --- Final Touches ---
    fig.suptitle("Company Sales Dashboard", fontsize=20, weight="bold")
    plt.tight_layout(rect=(0, 0.03, 1, 0.95))  # Adjust layout to make room for suptitle

    print("Displaying 2x1 sales dashboard. Please close the plot window to continue.")
    plt.show()
