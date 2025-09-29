# 📘 Day 26: Practical Statistics for Business Analysis

On Day 26 you expand beyond data wrangling and apply core statistical tools to
business datasets. The refactored lesson script now exposes reusable helper
functions for descriptive statistics, correlation analysis, and hypothesis
testing so you can integrate them directly into your own notebooks or projects.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main
[README.md](../../README.md) to create your virtual environment and install the
required libraries.

## Exploring the Refactored Code

The `stats.py` module has been organized into testable functions that separate
computation from presentation.

1. **Review the Code:** Open `Day_26_Statistics/stats.py` and look at the new
   helpers:
   * `load_sales_data()` reads `sales_data.csv` and removes missing rows.
   * `summarize_revenue()` returns key revenue metrics and the full
     `DataFrame.describe()` output.
   * `compute_correlations()` produces a correlation matrix for the numeric
     sales fields.
   * `run_ab_test()` wraps SciPy's independent t-test and reports whether the
     difference is statistically significant.
2. **Run the Script:** From the project root, execute the module to see the
   printed analysis that the helpers power.
   ```bash
   python Day_26_Statistics/stats.py
   ```
3. **Run the Tests:** The automated tests create in-memory DataFrames and
   duration samples to validate each helper without touching disk.
   ```bash
   pytest tests/test_day_26.py
   ```

🎉 **Great job!** With these reusable statistics utilities you can move from
simple summaries to rigorous, testable insights in your analyses.
