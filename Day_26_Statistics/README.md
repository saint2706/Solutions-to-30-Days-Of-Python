# 📘 Day 24: Practical Statistics for Business Analysis

So far, we've focused on manipulating and visualizing data. Now, let's dive into **statistics**—the science of collecting, analyzing, and interpreting data. For a business analyst, statistics provide the tools to move from simply describing data to drawing meaningful conclusions and making data-driven inferences.

## Descriptive Statistics: Summarizing Your Data

Descriptive statistics are used to summarize and describe the main features of a dataset. Pandas DataFrames have built-in methods that make this incredibly easy.

Given a DataFrame `df` with a numerical column 'Sales':

* **Measures of Central Tendency:**
  * `df['Sales'].mean()`: The average value.
  * `df['Sales'].median()`: The middle value when the data is sorted. Less affected by extreme outliers than the mean.
  * `df['Sales'].mode()`: The most frequently occurring value.
* **Measures of Spread or Dispersion:**
  * `df['Sales'].std()`: The standard deviation, which measures how spread out the data is from the mean.
  * `df['Sales'].var()`: The variance (the square of the standard deviation).
  * `df['Sales'].min()`, `df['Sales'].max()`: The minimum and maximum values.
  * `df['Sales'].quantile(q)`: The value below which a given proportion of observations fall (e.g., `df['Sales'].quantile(0.25)` is the 25th percentile).

The `df.describe()` method, which we've used before, conveniently calculates most of these for you!

## Inferential Statistics: Making Inferences from Data

Descriptive statistics describe what's in your data. **Inferential statistics** allows you to make educated guesses (inferences) about a larger population based on a smaller sample of data.

A key question in business is often: "Is the difference I'm seeing real, or is it just due to random chance?" For example, did our new marketing campaign *actually* increase sales, or was the increase just random fluctuation?

### Hypothesis Testing and the T-Test

**Hypothesis testing** is a formal procedure for investigating our ideas about the world. A **t-test** is one of the most common statistical tests, used to determine if there is a significant difference between the means of two groups.

For this, we'll use the `scipy` library, a core package for scientific computing in Python.

**Scenario:** We have sales data from before and after a marketing campaign. We want to know if the campaign had a statistically significant effect.

* **Null Hypothesis (H₀):** There is no difference in average sales before and after the campaign.
* **Alternative Hypothesis (H₁):** There is a significant difference.

```python
from scipy.stats import ttest_ind

sales_before = [20, 22, 19, 24, 25]
sales_after = [28, 30, 26, 32, 29]

t_stat, p_value = ttest_ind(sales_before, sales_after)

# The p-value is the probability of observing the data if the null hypothesis is true.
# A small p-value (typically < 0.05) suggests we can reject the null hypothesis.
if p_value < 0.05:
    print(f"The difference is statistically significant (p-value: {p_value:.3f}).")
else:
    print(f"The difference is not statistically significant (p-value: {p_value:.3f}).")
```

## Correlation: Measuring Relationships

**Correlation** measures the strength and direction of the linear relationship between two variables. The correlation coefficient ranges from -1 to +1.

* **+1:** Perfect positive correlation (as one variable increases, the other increases).
* **-1:** Perfect negative correlation (as one variable increases, the other decreases).
* **0:** No linear correlation.

Pandas DataFrames have a built-in `.corr()` method to calculate the correlation between all numerical columns.

## 💻 Exercises: Day 24

1. **Descriptive Statistics of Sales:**
    * Load the cleaned `sales_data.csv` from Day 17.
    * Select the 'Revenue' column.
    * Calculate and print the mean, median, standard deviation, min, and max of the revenue.

2. **Correlation Analysis:**
    * Using the same sales data, calculate the correlation matrix for the numerical columns ('Units Sold', 'Price', 'Revenue').
    * Print the correlation matrix.
    * Which two variables have the strongest positive correlation?

3. **A/B Test Analysis (T-Test):**
    * Imagine an A/B test where you showed two different website headlines to two groups of users and measured their session duration in minutes.
    * `group_a_durations = [10.5, 12.1, 11.8, 13.0, 12.5]`
    * `group_b_durations = [12.8, 13.5, 13.2, 14.0, 13.8]`
    * Perform an independent t-test to see if there is a statistically significant difference in session duration between the two groups.
    * Print the p-value and your conclusion.

🎉 **Amazing!** You've just scratched the surface of statistics, but you now have the tools to perform some of the most common quantitative analyses in business. Understanding these concepts is a huge leap in your journey as a data analyst.
