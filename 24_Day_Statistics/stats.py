"""
Day 24: Practical Statistics in Python

This script demonstrates how to calculate descriptive statistics,
correlation, and perform a simple hypothesis test (t-test).
"""

import pandas as pd
from scipy.stats import ttest_ind

# --- 1. Descriptive Statistics with Pandas ---
print("--- 1. Descriptive Statistics of Sales Data ---")
try:
    df = pd.read_csv('../17_Day_Pandas_Adv/sales_data.csv')
    df.dropna(inplace=True) # Clean the data first

    # Select the 'Revenue' column to analyze
    revenue = df['Revenue']

    print(f"Mean Revenue: ${revenue.mean():,.2f}")
    print(f"Median Revenue: ${revenue.median():,.2f}")
    print(f"Standard Deviation of Revenue: ${revenue.std():,.2f}")
    print(f"Minimum Revenue: ${revenue.min():,.2f}")
    print(f"Maximum Revenue: ${revenue.max():,.2f}")

    print("\nFull descriptive statistics (df.describe()):")
    print(df.describe())

except FileNotFoundError:
    print("Error: sales_data.csv not found in '17_Day_Pandas_Adv' directory.")
    df = pd.DataFrame()
print("-" * 20)


# --- 2. Correlation Analysis ---
print("--- 2. Correlation Analysis ---")
if not df.empty:
    # Select only the numerical columns for correlation calculation
    numerical_df = df[['Units Sold', 'Price', 'Revenue']]

    # .corr() calculates the correlation matrix
    correlation_matrix = numerical_df.corr()

    print("Correlation Matrix:")
    print(correlation_matrix)
    print("\nAnalysis: 'Units Sold' and 'Revenue' have a strong positive correlation (0.93).")
    print("'Price' and 'Revenue' also have a strong positive correlation (0.83).")
    print("'Price' and 'Units Sold' have a weak negative correlation (-0.23), which might be expected (higher price can sometimes mean fewer units).")
else:
    print("DataFrame not available for this exercise.")
print("-" * 20)


# --- 3. Inferential Statistics (T-Test) ---
print("--- 3. A/B Test Analysis (T-Test) ---")
# Sample data for an A/B test on website headlines
group_a_durations = [10.5, 12.1, 11.8, 13.0, 12.5, 11.9, 12.3]
group_b_durations = [12.8, 13.5, 13.2, 14.0, 13.8, 14.1, 13.6]
print(f"Group A (Old Headline) Durations: {group_a_durations}")
print(f"Group B (New Headline) Durations: {group_b_durations}")

# Perform an independent t-test
# This test checks if the two independent samples have different average values.
t_statistic, p_value = ttest_ind(group_a_durations, group_b_durations)

print(f"\nT-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpret the result
# A small p-value (typically < 0.05) indicates strong evidence against the null hypothesis.
alpha = 0.05
if p_value < alpha:
    print("\nConclusion: The difference is statistically significant.")
    print("We can conclude that the new headline (Group B) likely leads to longer session durations.")
else:
    print("\nConclusion: The difference is not statistically significant.")
    print("We cannot conclude that the new headline had a real effect on session duration.")
print("-" * 20)
