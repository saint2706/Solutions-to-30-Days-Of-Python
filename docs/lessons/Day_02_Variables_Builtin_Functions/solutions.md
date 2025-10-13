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

Day 2: Solutions to Exercises

```python

# --- Exercise 1: Company Profile Variables ---
print("--- Solution to Exercise 1 ---")
company_name = "InnovateCorp"
year_founded = 2015
current_revenue = 2500000.50
is_publicly_traded = False

print(f"Company Name: {company_name}")
print(f"Year Founded: {year_founded}")
print(f"Current Revenue: ${current_revenue}")
print(f"Is Publicly Traded: {is_publicly_traded}")
print("-" * 20)


# --- Exercise 2: Sales Analysis ---
print("--- Solution to Exercise 2 ---")
weekly_sales = [150.50, 200.00, 75.25, 300.75, 120.00]
print(f"Sales data: {weekly_sales}")

# The total number of sales transactions
num_transactions = len(weekly_sales)
print(f"Total number of transactions: {num_transactions}")

# The total revenue for the week
total_revenue = sum(weekly_sales)
print(f"Total revenue: ${total_revenue:.2f}")

# The smallest sale
min_sale = min(weekly_sales)
print(f"Smallest sale: ${min_sale:.2f}")

# The largest sale
max_sale = max(weekly_sales)
print(f"Largest sale: ${max_sale:.2f}")

# The average sale amount
average_sale = total_revenue / num_transactions
print(f"Average sale amount: ${average_sale:.2f}")
print("-" * 20)


# --- Exercise 3: User Input for a Profit Calculator ---
print("--- Solution to Exercise 3 ---")
# Note: To run this interactively, you would run the python file
# in your terminal. The input() function will pause the script
# and wait for you to type a value and press Enter.

# We wrap the code in a try...except block to handle cases where the user
# might enter text instead of a number, which would cause a crash.
try:
    # float() converts the string from input() into a floating-point number
    revenue_input = float(input("Enter total revenue: "))
    expenses_input = float(input("Enter total expenses: "))

    profit = revenue_input - expenses_input
    print(f"Calculated Profit: ${profit:.2f}")

except ValueError:
    print("Invalid input. Please make sure to enter numbers only.")

print("-" * 20)

```
