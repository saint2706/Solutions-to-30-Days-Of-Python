# 📘 Day 19: Data Visualization - Communicating Insights

Numbers and tables are great for analysis, but to communicate your findings effectively, you need to visualize your data. A good chart can reveal patterns, trends, and insights far more effectively than a table of numbers.

Today, we'll learn how to create fundamental business charts using two of Python's most popular visualization libraries: **Matplotlib** and **Seaborn**.

* **Matplotlib:** The foundational plotting library in Python. It's powerful and highly customizable, but can sometimes be complex for standard plots.
* **Seaborn:** Built on top of Matplotlib, Seaborn provides a high-level interface for drawing attractive and informative statistical graphics. It makes creating common chart types much easier.

We will primarily use Seaborn for its simplicity and aesthetic appeal, but it's important to know that Matplotlib is working under the hood.

## The Grammar of a Plot

Most plots you create will have a few key components:

* The **Figure**: The overall window or page that everything is drawn on.
* The **Axes**: The actual plot or chart area.
* The **Title**: A title for your chart.
* **X-axis and Y-axis labels**: Descriptions for what the axes represent.
* The **Data**: The actual bars, lines, or points on the chart.

## Common Business Charts

### 1. Bar Chart

**Use Case:** Comparing a numerical value across different categories.
*Example: Comparing total sales revenue across different regions.*

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is a DataFrame with 'Region' and 'Revenue'
sns.barplot(x='Region', y='Revenue', data=df)
plt.title('Total Revenue by Region')
plt.show() # This command displays the plot
```

### 2. Line Chart

**Use Case:** Showing a trend over a continuous interval, usually time.
*Example: Tracking monthly sales over the course of a year.*

```python
# Assuming 'df' has a 'Date' column and 'Sales' column
sns.lineplot(x='Date', y='Sales', data=df)
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45) # Rotate x-axis labels for readability
plt.show()
```

### 3. Histogram

**Use Case:** Understanding the distribution of a single numerical variable.
*Example: Analyzing the distribution of product prices to understand price points.*

```python
# Assuming 'df' has a 'Price' column
sns.histplot(df['Price'], bins=10) # 'bins' controls the number of bars
plt.title('Distribution of Product Prices')
plt.show()
```

### 4. Scatter Plot

**Use Case:** Investigating the relationship between two numerical variables.
*Example: Seeing if there's a correlation between marketing spend and sales revenue.*

```python
# Assuming 'df' has 'Marketing_Spend' and 'Sales'
sns.scatterplot(x='Marketing_Spend', y='Sales', data=df)
plt.title('Marketing Spend vs. Sales')
plt.show()
```

## 💻 Exercises: Day 19

For these exercises, you will use the cleaned `sales_data.csv` from Day 17.

1. **Sales by Product:**
    * Load the cleaned sales data.
    * Create a bar chart that shows the total `Units Sold` for each `Product`.
    * Give your chart a descriptive title.

2. **Revenue Over Time:**
    * Load the cleaned sales data, making sure the 'Date' column is converted to datetime objects (`parse_dates=['Date']` in `read_csv`).
    * Group the data by date and sum the revenue for each day. (Hint: `daily_revenue = df.groupby('Date')['Revenue'].sum().reset_index()`).
    * Create a line chart that shows the `Revenue` over `Date`.
    * Give your chart a title and rotate the x-axis labels for better readability.

3. **Price Distribution:**
    * Load the cleaned sales data.
    * Create a histogram to show the distribution of the `Price` column.
    * Give your chart a title.

🎉 **Excellent!** You can now turn raw data into insightful charts. Visualization is a crucial skill for any analyst, allowing you to not only understand your data better but also to share your findings with others in a clear and compelling way.
