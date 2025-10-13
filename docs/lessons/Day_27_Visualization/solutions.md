# 📘 Day 27: Data Visualization - Communicating Insights

Visualising key business metrics makes it easier to communicate findings and uncover patterns. Day 27 introduces reusable Matplotlib and Seaborn helpers that create core business charts for the sales dataset you prepared in Day 24.

## Environment Setup

1. (Recommended) Create a virtual environment and activate it.
1. Install dependencies from the root of the repository:
   ```bash
   pip install -r requirements.txt
   ```
1. Ensure `sales_data.csv` from Day 24 is available in this lesson folder (or update the helper to point to your copy).

## Run the Script

Generate the four lesson visuals from the command line:

```bash
python Day_27_Visualization/visualization.py
```

Each call loads the shared plotting helpers, displays a chart, and waits for you to close the window before moving on.

## Explore the Notebook

Open the companion notebook to iterate on the visuals and review interpretation guidance:

```bash
jupyter notebook Day_27_Visualization/visualization.ipynb
```

The notebook reuses the same plotting functions so you can experiment without duplicating logic.

## Run Tests

A pytest suite validates the chart configuration (titles, labels, legends) using a headless Matplotlib backend:

```bash
pytest tests/test_day_27.py
```

Running the full repository test suite is also supported:

```bash
pytest
```

Day 27: Solutions to Exercises

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
    # We use the data from Day 24, so we need to reference its path
    # parse_dates=['Date'] tells pandas to automatically convert the 'Date' column
    df = pd.read_csv(data_path, parse_dates=["Date"])
    df.dropna(inplace=True)  # Drop rows with missing values for simplicity
    print("Data loaded successfully for exercises.")
except FileNotFoundError:
    print("Error: sales_data.csv not found. Keep the CSV beside this script.")
    df = pd.DataFrame()


if not df.empty:
    # --- Exercise 1: Sales by Product ---
    print("\n--- Solution to Exercise 1 ---")
    plt.figure(figsize=(10, 6))
    # Group by Product and sum the Units Sold for each
    product_sales = df.groupby("Product")["Units Sold"].sum().reset_index()
    sns.barplot(x="Product", y="Units Sold", data=product_sales)
    plt.title("Total Units Sold by Product")
    plt.xlabel("Product Category")
    plt.ylabel("Total Units Sold")
    print("Displaying plot for Exercise 1. Please close the plot window.")
    plt.show()

    # --- Exercise 2: Revenue Over Time ---
    print("\n--- Solution to Exercise 2 ---")
    # Group the data by date and sum the revenue for each day
    daily_revenue = df.groupby("Date")["Revenue"].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Date", y="Revenue", data=daily_revenue)
    plt.title("Daily Revenue Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    print("Displaying plot for Exercise 2. Please close the plot window.")
    plt.show()

    # --- Exercise 3: Price Distribution ---
    print("\n--- Solution to Exercise 3 ---")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="Price", bins=8, kde=False)
    plt.title("Distribution of Product Prices")
    plt.xlabel("Price Bins ($)")
    plt.ylabel("Number of Products")
    print("Displaying plot for Exercise 3. Please close the plot window.")
    plt.show()
else:
    print("\nSkipping exercises as DataFrame could not be loaded.")

```
