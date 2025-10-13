# 📘 Day 2: Storing and Analyzing Business Data

In Day 1, we performed basic calculations. Now, we'll learn how to store data in **variables** and use Python's **built-in functions** to analyze it.

## What is a Variable?

A variable is a labeled container for information. Instead of using a raw number like `500000`, we can store it in a variable called `revenue`, making our code more readable and manageable.

**`revenue = 500000`**

### Naming Conventions

- **Be Descriptive:** `quarterly_sales` is better than `qs`.
- **Use Snake Case:** Separate words with underscores, like `cost_of_goods_sold`.

## Built-in Functions: Your Basic Toolkit

Python includes pre-built functions for common tasks:

- `len()`: Finds the length (e.g., number of items in a list).
- `sum()`: Calculates the sum of numbers in a list.
- `min()` and `max()`: Find the minimum and maximum values.
- `round()`: Rounds a number to a specified number of decimal places.

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `variables.py`, has been refactored into functions to promote code reuse and testability.

1. **Review the Code:** Open `Day_02_Variables_Builtin_Functions/variables.py`. Notice how the logic is now organized into functions like `display_company_profile()` and `analyze_weekly_sales()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script:
   ```bash
   python Day_02_Variables_Builtin_Functions/variables.py
   ```
   You will see the output from the example scenarios defined at the bottom of the script.
1. **Run the Tests:** You can also run the tests for this lesson to see how we verify the functions' correctness:
   ```bash
   pytest tests/test_day_02.py
   ```

## 💻 Exercises: Day 2

1. **Company Profile Variables:**

   - In a new Python script (`my_solutions_02.py`), declare variables for a fictional company: `company_name`, `year_founded`, `current_revenue`, and `is_publicly_traded`.
   - Print each of these variables with a descriptive label.

1. **Sales Analysis:**

   - A list of sales transactions is: `[150.50, 200.00, 75.25, 300.75, 120.00]`.
   - Store these in a variable called `weekly_sales`.
   - Use built-in functions to calculate and print:
     - The total number of sales (`len()`).
     - The total revenue (`sum()`).
     - The smallest and largest sales (`min()`, `max()`).
     - The average sale amount.

1. **Profit Calculator Function:**

   - Create a function `calculate_profit(revenue, expenses)` that takes two numbers and returns the difference.
   - Call this function with some example numbers (e.g., `calculate_profit(50000, 35000)`) and print the result.

🎉 **Well done!** You've learned how to store data in variables and use Python's built-in functions for analysis—foundational skills for everything that comes next.

Day 2: Storing and Analyzing Business Data (Refactored)

This script demonstrates the use of variables to store business data
and built-in functions to perform basic analysis. This version is
refactored into functions for better organization and testability.

```python


def display_company_profile(name, founded, revenue, is_public):
    """Displays the company's profile information."""
    print("--- Company Profile ---")
    print(f"Company Name: {name}")
    print(f"Year Founded: {founded}")
    print(f"Current Revenue: ${revenue}")
    print(f"Is Publicly Traded: {is_public}")
    print("-" * 20)


def analyze_weekly_sales(sales_data):
    """Analyzes and prints a summary of weekly sales data."""
    if not sales_data:
        print("No sales data to analyze.")
        return

    print("--- Weekly Sales Analysis ---")
    num_transactions = len(sales_data)
    total_revenue = sum(sales_data)
    smallest_sale = min(sales_data)
    largest_sale = max(sales_data)
    average_sale = total_revenue / num_transactions if num_transactions > 0 else 0

    print(f"Number of Transactions: {num_transactions}")
    print(f"Total Weekly Revenue: ${total_revenue:.2f}")
    print(f"Smallest Sale: ${smallest_sale:.2f}")
    print(f"Largest Sale: ${largest_sale:.2f}")
    print(f"Average Sale Amount: ${round(average_sale, 2)}")
    print("-" * 20)

    return {
        "num_transactions": num_transactions,
        "total_revenue": total_revenue,
        "smallest_sale": smallest_sale,
        "largest_sale": largest_sale,
        "average_sale": average_sale,
    }


def interactive_profit_calculator():
    """Handles user input to calculate and display profit."""
    print("--- Interactive Profit Calculator ---")
    try:
        user_revenue = float(input("Enter your total revenue: "))
        user_expenses = float(input("Enter your total expenses: "))
        profit = user_revenue - user_expenses
        print(f"Your calculated profit is: ${profit:.2f}")
        return profit
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None


if __name__ == "__main__":
    # --- Storing Company Profile in Variables ---
    display_company_profile("InnovateCorp", 2015, 2500000.50, False)

    # --- Using Built-in Functions for Sales Analysis ---
    weekly_sales_data = [150.50, 200.00, 75.25, 300.75, 120.00, 450.50, 275.00]
    analyze_weekly_sales(weekly_sales_data)

    # --- Getting User Input ---
    # Note: This part is not easily testable in an automated way without mocking input.
    # The function is separated to keep the core logic testable.
    # interactive_profit_calculator() # Uncomment to run the interactive part

```
