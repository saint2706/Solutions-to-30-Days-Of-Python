# 📘 Day 11: Functions - Creating Reusable Business Tools

As you perform more complex analysis, you'll write the same code repeatedly. **Functions** are named, reusable blocks of code that perform a specific task, helping you avoid repetition and write cleaner, more maintainable code.

## Key Function Concepts

- **Definition (`def`):** You define a function using the `def` keyword.
- **Parameters:** Inputs to your function that allow you to pass data to it (e.g., `revenue`, `expenses`).
- **`return` Statement:** Sends a value *back* from the function, so you can use the result in other parts of your code.
- **Type Hinting:** A modern Python feature that lets you specify the expected data types for parameters and the return value (e.g., `def get_net_profit(revenue: float) -> float:`). This improves code clarity and helps prevent bugs.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `functions.py`, is already well-structured, with each piece of business logic encapsulated in its own function. We've made a minor improvement by wrapping the example usage in a `main()` function, which is a standard convention.

1. **Review the Code:** Open `Day_11_Functions/functions.py`. Examine the different functions like `get_net_profit()`, `calculate_commission()`, and `format_currency()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_11_Functions/functions.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function:
   ```bash
   pytest tests/test_day_11.py
   ```

## 💻 Exercises: Day 11

1. **Commission Calculator Function:**

   - The `calculate_commission` function is already created in `functions.py`.
   - In a new script (`my_solutions_11.py`), import this function: `from Day_11_Functions.functions import calculate_commission`.
   - Call the function with a sample sales amount and print the returned commission.

1. **Employee Bonus Eligibility Function:**

   - Import the `is_eligible_for_bonus` function.
   - Call the function with a few different scenarios for `performance_rating` and `years_of_service` and print the `True`/`False` results.

1. **Advanced Currency Formatter:**

   - Create a new function `format_currency_with_symbol(amount, symbol='$')`.
   - This function should take an amount and an optional `symbol` parameter that defaults to `'$'`.
   - It should return a formatted string like `€1,250.50` if the symbol is `'€'`.
   - Test your new function by calling it with and without the `symbol` parameter.

🎉 **Great work!** Functions are the key to writing clean, organized, and professional code. By packaging your logic into reusable tools, you're moving from a simple scripter to a true programmer.

Day 11: Solutions to Exercises

```python

# --- Exercise 1: Commission Calculator Function ---
print("--- Solution to Exercise 1 ---")


def calculate_commission(sales_amount: float) -> float:
    """
    Calculates a commission of 15% of the sales amount.
    Takes sales_amount as a float, returns the commission as a float.
    """
    commission_rate = 0.15
    return sales_amount * commission_rate


# Example usage:
sample_sale = 5000.00
commission_earned = calculate_commission(sample_sale)
print(f"A sale of ${sample_sale:,.2f} earns a commission of ${commission_earned:,.2f}.")
print("-" * 20)


# --- Exercise 2: Employee Bonus Eligibility Function ---
print("--- Solution to Exercise 2 ---")


def is_eligible_for_bonus(performance_rating: int, years_of_service: int) -> bool:
    """
    Returns True if rating is 4 or 5 AND service is more than 2 years.
    """
    return performance_rating >= 4 and years_of_service > 2


# Test cases:
print(
    f"Rating 5, 3 years service -> Eligible? {is_eligible_for_bonus(5, 3)}"
)  # Expected: True
print(
    f"Rating 4, 3 years service -> Eligible? {is_eligible_for_bonus(4, 3)}"
)  # Expected: True
print(
    f"Rating 5, 1 year service  -> Eligible? {is_eligible_for_bonus(5, 1)}"
)  # Expected: False
print(
    f"Rating 3, 5 years service -> Eligible? {is_eligible_for_bonus(3, 5)}"
)  # Expected: False
print("-" * 20)


# --- Exercise 3: Format Currency Function ---
print("--- Solution to Exercise 3 ---")


def format_currency(number: float) -> str:
    """
    Returns a string formatted as currency with a dollar sign and commas.
    Example: 1250.5 -> "$1,250.50"
    """
    return f"${number:,.2f}"


# Example usage:
amount1 = 1250.5
amount2 = 500
print(f"{amount1} -> {format_currency(amount1)}")
print(f"{amount2} -> {format_currency(amount2)}")
print("-" * 20)

```
