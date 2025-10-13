# 📘 Day 3: Operators - The Tools for Business Calculation and Logic

An **operator** is a symbol that tells the computer to perform a specific mathematical or logical manipulation. For a business analyst, operators are the tools you'll use to calculate financial metrics, compare results, and create business rules.

## Key Operator Types

- **Arithmetic Operators (`+`, `-`, `*`, `/`, `**`):** The foundation of any quantitative analysis, used for calculations like profit margin and compound interest.
- **Assignment Operators (`=`, `+=`, `-=`):** Used to assign and update values in variables, such as accumulating total sales.
- **Comparison Operators (`==`, `!=`, `>`, `<`):** Used to compare two values, resulting in `True` or `False`. This is the basis for filtering data and making decisions.
- **Logical Operators (`and`, `or`, `not`):** Used to combine conditional statements to create complex business rules, like determining bonus eligibility.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `operators.py`, has been refactored into functions to make the logic clear, reusable, and testable.

1. **Review the Code:** Open `Day_03_Operators/operators.py`. Each business calculation or rule (e.g., `calculate_compound_interest()`, `check_bonus_eligibility()`) is now its own function.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_03_Operators/operators.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function:
   ```bash
   pytest tests/test_day_03.py
   ```

## 💻 Exercises: Day 3

1. **Calculate Net Profit Margin:**

   - In a new script (`my_solutions_03.py`), create a function `calculate_net_profit_margin(revenue, expenses)`.
   - The function should return the net profit margin (`(revenue - expenses) / revenue`).
   - Call the function with a `revenue` of 1,200,000 and `total_expenses` of 850,000.
   - Print the result formatted as a percentage with two decimal places.

1. **Inventory Check Function:**

   - Create a function `check_reorder_status(inventory_count, low_stock_threshold, reorder_threshold)`.
   - The function should return a dictionary with two keys: `is_low_stock` (boolean) and `needs_reorder` (boolean).
   - Call the function with an `inventory_count` of 45, a `low_stock_threshold` of 50, and a `reorder_threshold` of 25. Print the results.

1. **Sales Bonus Eligibility Function:**

   - The logic for bonus eligibility is already in the `check_bonus_eligibility` function in `operators.py`.
   - In your own script, import this function: `from Day_03_Operators.operators import check_bonus_eligibility`.
   - Call the function with a few different scenarios for `sales`, `years_of_service`, and `top_performer_last_quarter` to see the results.

🎉 **Excellent work!** You're now equipped with the operators needed to perform the vast majority of business calculations and logical checks you'll encounter.

Day 3: Solutions to Exercises

```python

# --- Exercise 1: Calculate Net Profit Margin ---
print("--- Solution to Exercise 1 ---")
revenue = 1200000
total_expenses = 850000

# Calculate the profit
profit = revenue - total_expenses

# Calculate the net profit margin
# It's good practice to check if revenue is zero to avoid a DivisionByZeroError
if revenue > 0:
    net_profit_margin = (profit / revenue) * 100
    print(f"Revenue: ${revenue:,.2f}")
    print(f"Expenses: ${total_expenses:,.2f}")
    print(f"Profit: ${profit:,.2f}")
    print(f"Net Profit Margin: {net_profit_margin:.2f}%")
else:
    print("Cannot calculate margin as revenue is zero.")
print("-" * 20)


# --- Exercise 2: Inventory Check ---
print("--- Solution to Exercise 2 ---")
inventory_count = 45
low_stock_threshold = 50
reorder_threshold = 25

is_low_stock = inventory_count < low_stock_threshold
reorder_required = inventory_count <= reorder_threshold

print(f"Inventory count: {inventory_count} units")
print(f"Is inventory considered low stock? {is_low_stock}")
print(f"Is a reorder required? {reorder_required}")
print("-" * 20)


# --- Exercise 3: Sales Bonus Eligibility ---
print("--- Solution to Exercise 3 ---")


def check_bonus_eligibility(sales, years_of_service, top_performer_last_quarter):
    """A helper function to test different scenarios easily."""
    is_eligible = (sales > 10000 and years_of_service > 2) or top_performer_last_quarter
    print(
        f"Scenario: Sales=${sales}, Service={years_of_service}yrs, Top Performer={top_performer_last_quarter} -> Eligible? {is_eligible}"
    )


# Scenario 1: High sales but new employee
check_bonus_eligibility(12000, 1, False)

# Scenario 2: Low sales but top performer
check_bonus_eligibility(8000, 3, True)

# Scenario 3: High sales and long service
check_bonus_eligibility(15000, 5, False)

# Scenario 4: Not eligible on any count
check_bonus_eligibility(9000, 1, False)
print("-" * 20)

```
