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

Day 28: Solutions to Exercises

```python

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# --- Load and Prepare Data ---
# We use the cleaned data from Day 24 for reliable plotting.
resource_dir = Path(__file__).resolve().parent
data_path = resource_dir / "sales_data.csv"

try:
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.dropna(inplace=True)  # Drop rows with missing values for simplicity
    print("Data loaded successfully for exercises.")
except FileNotFoundError:
    print("Error: sales_data.csv not found. Keep the CSV beside this script.")
    df = pd.DataFrame()


if not df.empty:
    # --- Exercise 1: Create a Customized Sales Chart ---
    print("\n--- Solution to Exercise 1 ---")

    # Calculate total and average revenue by product
    product_revenue = df.groupby("Product")["Revenue"].sum()
    average_revenue = product_revenue.mean()

    plt.figure(figsize=(10, 7))
    sns.barplot(x=product_revenue.index, y=product_revenue.values)

    # Customizations
    plt.title("Total Revenue per Product", fontsize=16)
    plt.ylabel("Total Revenue (USD)", fontsize=12)
    plt.xlabel("Product", fontsize=12)
    plt.axhline(
        y=average_revenue,
        color="red",
        linestyle="--",
        label=f"Average Revenue (${average_revenue:,.2f})",
    )
    plt.legend()

    # Save the figure
    plt.savefig("product_revenue.png", dpi=300)
    print("Plot for Exercise 1 saved to 'product_revenue.png'. Displaying plot now.")
    plt.show()

    # --- Exercise 2: Build a 2x1 Dashboard ---
    print("\n--- Solution to Exercise 2 ---")

    # Create the figure and axes grid
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

    # --- Top Plot: Units Sold Trend ---
    daily_units = df.groupby("Date")["Units Sold"].sum().reset_index()
    sns.lineplot(x="Date", y="Units Sold", data=daily_units, ax=axes[0])
    axes[0].set_title("Trend of Units Sold Over Time", fontsize=14)
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Total Units Sold")

    # --- Bottom Plot: Price vs. Units Sold ---
    sns.scatterplot(x="Price", y="Units Sold", data=df, ax=axes[1], hue="Region")
    axes[1].set_title("Price vs. Units Sold by Region", fontsize=14)
    axes[1].set_xlabel("Price per Unit ($)")
    axes[1].set_ylabel("Units Sold per Transaction")

    # --- Final Touches ---
    fig.suptitle("Sales Analysis Dashboard", fontsize=20, weight="bold")
    plt.tight_layout(rect=(0, 0.03, 1, 0.95))

    print("Displaying plot for Exercise 2. Please close the plot window.")
    plt.show()

else:
    print("\nSkipping exercises as DataFrame could not be loaded.")

```
