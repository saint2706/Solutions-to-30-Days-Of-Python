"""
Day 21: Interactive Visualization with Plotly

This script demonstrates how to create interactive, web-based
charts using the Plotly Express library.
"""

import pandas as pd
import plotly.express as px

# --- Load and Prepare Data ---
try:
    df = pd.read_csv('../17_Day_Pandas_Adv/sales_data.csv', parse_dates=['Date'])
    df.dropna(inplace=True)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: sales_data.csv not found in '17_Day_Pandas_Adv' directory.")
    df = pd.DataFrame()

if not df.empty:
    # --- 1. Interactive Bar Chart ---
    print("\n--- 1. Interactive Bar Chart: Revenue by Region ---")
    # Group data to get the sum of revenue for each region
    region_revenue = df.groupby('Region')['Revenue'].sum().reset_index()

    fig_bar = px.bar(
        region_revenue,
        x='Region',
        y='Revenue',
        title='Total Revenue by Region',
        labels={'Revenue': 'Total Revenue (USD)'}, # Customizing axis labels
        color='Region' # Color each bar differently
    )
    print("Displaying interactive bar chart. A browser window may open.")
    # fig_bar.show() # This would open in a browser, might not work in all environments


    # --- 2. Interactive Line Chart ---
    print("\n--- 2. Interactive Line Chart: Revenue Over Time ---")
    daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()

    fig_line = px.line(
        daily_revenue,
        x='Date',
        y='Revenue',
        title='Daily Revenue Trend',
        markers=True # Add markers to each data point
    )
    print("Displaying interactive line chart. A browser window may open.")
    # fig_line.show()


    # --- 3. Interactive Scatter Plot ---
    print("\n--- 3. Interactive Scatter Plot: Price vs. Units Sold ---")
    fig_scatter = px.scatter(
        df,
        x='Price',
        y='Units Sold',
        color='Product', # Color points by product category
        size='Revenue',  # Make point size proportional to revenue
        hover_data=['Region'], # Show region info on hover
        title='Price vs. Units Sold Analysis'
    )
    print("Displaying interactive scatter plot. A browser window may open.")
    # fig_scatter.show()

    # --- Saving a Plot to an HTML file ---
    # This is a reliable way to view and share the plots.
    output_filename = 'interactive_scatter_plot.html'
    fig_scatter.write_html(output_filename)
    print(f"\nScatter plot saved to '{output_filename}'. You can open this file in a web browser.")

else:
    print("\nSkipping plot generation as DataFrame could not be loaded.")
