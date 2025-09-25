# 📘 Day 14: Modules - Organizing Your Business Logic

As you write more functions, your script files can get long and disorganized. Imagine having one giant file with all your financial calculations, HR logic, and marketing analytics tools mixed together. It would be a mess!

In Python, we solve this problem using **modules**. A module is simply a Python file (`.py`) that contains functions, variables, and other code. By organizing your related functions into modules, you create a clean, maintainable, and scalable project structure.

## Why Use Modules?

Think of your analytics project like a company. You have different departments, each with a specific role.

* **Finance Department:** Handles all financial calculations.
* **HR Department:** Handles all employee-related logic.
* **Sales Department:** Handles all sales data analysis.

In Python, each of these "departments" would be a module:

* `financials.py` (module)
* `human_resources.py` (module)
* `sales_analytics.py` (module)

This separation makes your code easier to navigate, debug, and reuse across different projects.

## How to Create and Use a Module

1. **Create a file:** Create a new Python file (e.g., `my_calculations.py`) and put some functions inside it.
2. **Import it:** In another Python file (e.g., `main_report.py`), use the `import` statement to gain access to the code in your module.

### Different Ways to Import

There are a few ways to import code, each with its own use case.

**1. Import the entire module:**
This is the most common and recommended way.

```python
# In main_report.py
import my_calculations

# You access functions using the module_name.function_name syntax
profit = my_calculations.get_net_profit(1000, 800)
```

**2. Import a specific function:**
If you only need one or two functions from a large module.

```python
# In main_report.py
from my_calculations import get_net_profit, calculate_commission

# Now you can call the function directly by its name
profit = get_net_profit(1000, 800)
commission = calculate_commission(5000)
```

**3. Import with an alias:**
If a module has a long name, you can give it a shorter alias. This is extremely common with data analysis libraries.

```python
# In main_report.py
import my_calculations as calc

profit = calc.get_net_profit(1000, 800)
```

## Python's Built-in Modules

Python comes with a huge **Standard Library** of built-in modules that you can use without installing anything. Here are a few that are very useful for business:

* `math`: Contains advanced mathematical functions (e.g., `math.sqrt()` for square root, `math.log()` for logarithms).
* `datetime`: For working with dates and times, which is essential for time-series analysis.
* `random`: For generating random numbers, useful for sampling data or running simulations.
* `csv`: For reading and writing data in the common Comma-Separated Values (CSV) format.

## 💻 Exercises: Day 14

1. **Create a Finance Module:**
    * Create a new file named `finance_tools.py`.
    * Inside this file, define two functions:
        * `calculate_roi(investment, profit)` which returns `(profit / investment) * 100`.
        * `calculate_future_value(principal, rate, years)` which returns `principal * ((1 + rate) ** years)`.
    * Create a second file named `main_analysis.py`.
    * In `main_analysis.py`, `import` your `finance_tools` module.
    * Call both functions with some sample data and print the results.

2. **Use the `datetime` Module:**
    * In a new script, `import` the `datetime` module.
    * Get the current date and time using `datetime.datetime.now()`.
    * Print the current date.
    * Print just the current year from the date object (e.g., `my_date.year`).

3. **Use the `math` Module:**
    * A company's sales are growing by the square root of its marketing budget.
    * `import` the `math` module.
    * Create a variable `marketing_budget = 100000`.
    * Use `math.sqrt()` to calculate the growth factor.
    * Print the result.

🎉 **Well done!** You've learned how to organize your code into modules. This is a critical skill for building any project that's more than a few dozen lines long. It allows you to create your own libraries of reusable tools.
