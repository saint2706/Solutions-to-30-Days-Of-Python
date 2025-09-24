# 📘 Day 25: Capstone Case Study - Tying It All Together

Congratulations on making it to the capstone of our data analysis section! It's time to combine everything you've learned—from data cleaning and manipulation with Pandas to statistical analysis and visualization—to solve a realistic business problem from start to finish.

## The Business Problem

You are a business analyst at a mid-sized e-commerce company. The Head of Sales wants to understand the performance of different products and regions for the last quarter. They have provided you with a dataset of sales transactions and have asked you to answer the following key questions:

1. Which were the top 5 products by total revenue?
2. Which sales region generated the most revenue?
3. Is there a correlation between the price of a product and the number of units sold?
4. How did revenue trend over the quarter?
5. What are your key recommendations based on this analysis?

## Your Task: The Analysis Workflow

Your task is to perform a complete analysis by following the standard data analysis workflow. The `case_study_sales.csv` file is provided for this exercise.

### Step 1: Load and Inspect the Data

* Load the `case_study_sales.csv` into a Pandas DataFrame.
* Use `.head()`, `.info()`, and `.isnull().sum()` to get a first look at the data and identify any immediate issues (like missing values).

### Step 2: Clean the Data

* Handle any missing values. For this dataset, you can drop rows with missing data.
* Ensure all columns have the correct data type (e.g., 'Date' should be datetime, 'Price' should be a float).

### Step 3: Exploratory Data Analysis (EDA) & Answering Key Questions

* **Top Products:** Group the data by 'Product' and calculate the sum of 'Revenue' for each. Sort the results to find the top 5.
* **Top Region:** Group the data by 'Region' and calculate the sum of 'Revenue' for each.
* **Correlation:** Calculate the correlation between the 'Price' and 'Units Sold' columns.
* **Time-Series Analysis:** Group the data by 'Date' and calculate the sum of 'Revenue' to see the daily trend.

### Step 4: Visualize Your Findings

* Create a **bar chart** showing the top 5 products by revenue.
* Create a **pie chart** or **bar chart** showing the revenue contribution of each region.
* Create a **line chart** showing the daily revenue trend over the quarter.

### Step 5: Write Your Summary

* Based on your analysis and visualizations, write a brief, non-technical summary of your findings.
* What are 1-2 actionable recommendations you would give to the Head of Sales? (e.g., "Focus marketing efforts on our top products," or "Investigate why the West region is underperforming.")

A complete, end-to-end solution is provided in the `solutions.py` file for this lesson. Try to complete the case study on your own first!

🎉 **Incredible Achievement!** Completing a case study like this means you have a solid, practical foundation in data analysis. You can now take a raw dataset, clean it, analyze it, visualize it, and extract actionable business insights. This is the core skill set of a data analyst.
