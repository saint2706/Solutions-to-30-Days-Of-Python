# 📘 Day 28: Advanced Visualization & Customization

Creating a basic chart is just the first step. To effectively communicate your story, you need to customize your visualizations to make them clear, compelling, and professional. Today, we'll learn how to customize our plots and how to combine multiple plots into a single figure, like a dashboard.

We'll continue to use **Seaborn** for plotting and **Matplotlib** for customization.

## Customizing Your Plots

Once you've created a plot with Seaborn, you can use Matplotlib functions to fine-tune it.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Start with a basic plot
sns.barplot(x='Region', y='Revenue', data=df)

# --- Customizations ---
# Add a title with a specific font size
plt.title('Total Revenue by Region', fontsize=16)

# Add more descriptive axis labels
plt.xlabel('Sales Region', fontsize=12)
plt.ylabel('Total Revenue (in USD)', fontsize=12)

# Change the limits of the y-axis
plt.ylim(0, 200000)

# Add a horizontal line, for example, to show a target
plt.axhline(y=150000, color='r', linestyle='--', label='Sales Target')
plt.legend() # Display the label for the horizontal line

# Ensure labels fit
plt.tight_layout()

# Display the customized plot
plt.show()
```

## Creating Multiple Plots (Subplots)

Often, you want to display multiple charts together to tell a more complete story. Matplotlib's `subplots()` function is perfect for this. It creates a figure and a grid of axes.

`fig, axes = plt.subplots(nrows=, ncols=, figsize=())`

- `nrows`, `ncols`: The number of rows and columns in your grid of plots.
- `figsize`: A tuple specifying the width and height of the entire figure in inches.

You can then tell each Seaborn plot which `ax` (axis) to draw on.

```python
# Create a 1x2 grid of plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# --- First Plot (on the left axis) ---
sns.barplot(x='Region', y='Revenue', data=df, ax=axes[0])
axes[0].set_title('Revenue by Region')

# --- Second Plot (on the right axis) ---
sns.histplot(df['Revenue'], bins=10, ax=axes[1])
axes[1].set_title('Distribution of Revenue')

# Add a title for the entire figure
fig.suptitle('Sales Performance Overview', fontsize=20)

# Display the dashboard
plt.show()
```

## 💻 Exercises: Day 28

For these exercises, you will use the cleaned `sales_data.csv` from Day 24.

1. **Create a Customized Sales Chart:**

   - Load the cleaned sales data.
   - Create a bar chart showing the total `Revenue` for each `Product`.
   - **Customize it:**
     - Give it the title "Total Revenue per Product".
     - Set the y-axis label to "Total Revenue (USD)".
     - Add a horizontal red dashed line representing the average revenue across all products.
     - Save the figure to a file named `product_revenue.png`.

1. **Build a 2x1 Dashboard:**

   - Create a figure with two rows and one column of subplots.
   - **Top Plot:** A line chart showing the trend of `Units Sold` over `Date`. Make sure the date is on the x-axis.
   - **Bottom Plot:** A scatter plot showing the relationship between `Price` and `Units Sold`.
   - Give each plot its own descriptive title.
   - Add an overall title to the entire figure: "Sales Analysis Dashboard".

🎉 **Fantastic!** You can now create presentation-ready charts and combine them into simple dashboards. This ability to not just analyze, but also to present data in a customized and professional format is a key skill that separates great analysts from good ones.

Utility functions for Day 28 advanced visualization examples.

```python

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _require_columns(df: pd.DataFrame, required: Iterable[str]) -> None:
    """Raise a ``ValueError`` if any of the ``required`` columns are missing."""

    missing = set(required) - set(df.columns)
    if missing:
        raise ValueError(f"DataFrame is missing required columns: {sorted(missing)}")


def build_product_revenue_bar(df: pd.DataFrame) -> plt.Figure:
    """Return a bar chart showing total revenue per product."""

    _require_columns(df, ["Product", "Revenue"])
    if df.empty:
        raise ValueError("DataFrame must contain at least one row to build the chart.")

    product_revenue = (
        df.groupby("Product", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
    )
    avg_revenue = product_revenue["Revenue"].mean()

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(
        x="Product",
        y="Revenue",
        data=product_revenue,
        hue="Product",
        palette="viridis",
        legend=False,
        ax=ax,
    )

    ax.set_title("Total Revenue per Product", fontsize=18, weight="bold")
    ax.set_xlabel("Product Category", fontsize=12)
    ax.set_ylabel("Total Revenue (in USD)", fontsize=12)
    ax.tick_params(axis="x", rotation=45)

    ax.axhline(
        y=avg_revenue,
        color="red",
        linestyle="--",
        label=f"Avg Revenue (${avg_revenue:,.2f})",
    )
    ax.legend()
    fig.tight_layout()
    return fig


def build_sales_dashboard(df: pd.DataFrame) -> plt.Figure:
    """Return a dashboard with a daily revenue line chart and revenue distribution histogram."""

    _require_columns(df, ["Date", "Revenue"])
    if df.empty:
        raise ValueError(
            "DataFrame must contain at least one row to build the dashboard."
        )

    daily_revenue = df.groupby("Date")["Revenue"].sum().sort_index().reset_index()

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
    sns.lineplot(x="Date", y="Revenue", data=daily_revenue, ax=axes[0], color="blue")
    axes[0].set_title("Daily Revenue Trend", fontsize=14)
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Revenue ($)")

    sns.histplot(data=df, x="Revenue", bins=15, kde=True, ax=axes[1], color="green")
    axes[1].set_title("Distribution of Individual Sale Revenue", fontsize=14)
    axes[1].set_xlabel("Revenue per Sale ($)")
    axes[1].set_ylabel("Frequency")

    fig.suptitle("Company Sales Dashboard", fontsize=20, weight="bold")
    fig.tight_layout(rect=(0, 0.03, 1, 0.95))
    return fig


def load_sales_data(data_path: Path | None = None) -> pd.DataFrame:
    """Load the ``sales_data.csv`` file bundled with the lesson."""

    if data_path is None:
        resource_dir = Path(__file__).resolve().parent
        data_path = resource_dir / "sales_data.csv"

    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.dropna(inplace=True)
    return df


def main() -> None:
    """Run the example workflow and display the generated figures."""

    try:
        df = load_sales_data()
    except FileNotFoundError:
        print("Error: sales_data.csv not found. Keep the CSV beside this script.")
        return

    print("Data loaded successfully.")

    print("\n--- 1. Creating a Customized Plot ---")
    fig_bar = build_product_revenue_bar(df)
    fig_bar.show()

    print("\n--- 2. Creating a 2x1 Dashboard ---")
    fig_dashboard = build_sales_dashboard(df)
    fig_dashboard.show()


if __name__ == "__main__":
    main()

```
