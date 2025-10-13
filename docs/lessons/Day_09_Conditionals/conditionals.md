# 📘 Day 9: Conditionals - Implementing Business Logic

Business is full of rules and decisions. "If a customer spends over $100, they get a 10% discount." "If inventory is below 50 units, flag it for reorder." In Python, we implement this decision-making process using **conditional statements**.

## Key Conditional Statements

- **`if`:** Executes a block of code **only if** a certain condition is `True`.
- **`else`:** Provides an alternative block of code to execute if the `if` condition is `False`.
- **`elif` ("else if"):** Lets you check for multiple, sequential conditions. Python executes the *first* block where the condition is `True` and then skips the rest.

```python
# Classifying a customer based on their total spending
if total_spent > 1000:
    customer_tier = "Gold"
elif total_spent > 500:
    customer_tier = "Silver"
else:
    customer_tier = "Standard"
```

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `conditionals.py`, has been refactored to encapsulate each business rule into a separate, testable function.

1. **Review the Code:** Open `Day_09_Conditionals/conditionals.py`. Notice the functions `calculate_discount_percent()`, `calculate_shipping_cost()`, and `calculate_employee_bonus()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_09_Conditionals/conditionals.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function under various conditions:
   ```bash
   pytest tests/test_day_09.py
   ```

## 💻 Exercises: Day 9

1. **Discount Policy Automation:**

   - In a new script (`my_solutions_09.py`), import the `calculate_discount_percent` function.
   - Define a `purchase_amount` variable.
   - Call the function to get the discount rate, then calculate the final price (`purchase_amount * (1 - discount_rate)`).
   - Print the original amount, the discount rate, and the final price. Test it with amounts like `120`, `75`, and `40`.

1. **Shipping Cost Calculator:**

   - Import the `calculate_shipping_cost` function.
   - Call the function with different combinations of countries (`"USA"`, `"Canada"`, `"Mexico"`) and weights (`40`, `60`) to see the results. Print a user-friendly message for each case.

1. **Employee Bonus Calculation:**

   - Import the `calculate_employee_bonus` function.
   - Test the function by calling it with different scenarios and printing the result:
     - A "Sales" employee with a `performance_rating` of 5.
     - An "Engineering" employee with a `performance_rating` of 4.
     - Any employee with a rating of 2.

🎉 **Fantastic progress!** You can now translate complex business rules into code that makes decisions automatically. This is a fundamental skill for automating reports and building analytical models.

Day 9: Implementing Business Logic with Conditionals (Refactored)

This script demonstrates how to use if, elif, and else statements
to create business rules and make decisions in code. This version is
refactored into functions for better organization and testability.

```python


def calculate_discount_percent(purchase_amount):
    """Calculates a discount percentage based on the purchase amount."""
    if not isinstance(purchase_amount, (int, float)) or purchase_amount < 0:
        return 0.0

    if purchase_amount > 100.00:
        return 0.10  # 10% discount
    elif purchase_amount > 50.00:
        return 0.05  # 5% discount
    else:
        return 0.00  # 0% discount


def calculate_shipping_cost(country, order_weight_kg):
    """Calculates shipping cost based on destination and weight."""
    if country == "USA":
        if order_weight_kg > 50:
            return 75
        else:
            return 50
    elif country == "Canada":
        if order_weight_kg > 50:
            return 100
        else:
            return 65
    else:
        return -1  # Using -1 to indicate not available


def calculate_employee_bonus(performance_rating, department, salary):
    """Calculates an employee's bonus based on performance and department."""
    if performance_rating >= 4:
        if department == "Sales":
            return salary * 0.15
        else:
            return salary * 0.10
    elif performance_rating == 3:
        return salary * 0.05
    else:
        return 0.0


if __name__ == "__main__":
    # --- Example 1: Customer Discount Policy ---
    print("--- Customer Discount Calculator ---")
    customer_purchase = 125.50
    discount_rate = calculate_discount_percent(customer_purchase)
    discount = customer_purchase * discount_rate
    final = customer_purchase - discount

    print(f"Original Price: ${customer_purchase:.2f}")
    print(f"Discount ({discount_rate * 100}%): ${discount:.2f}")
    print(f"Final Price: ${final:.2f}")
    print("-" * 20)

    # --- Example 2: Nested Conditionals for Shipping Costs ---
    print("--- Shipping Cost Calculator ---")
    shipping_country = "Canada"
    weight = 60
    cost = calculate_shipping_cost(shipping_country, weight)

    if cost != -1:
        print(f"Shipping to {shipping_country} for a {weight}kg package costs: ${cost}")
    else:
        print(f"Sorry, shipping to {shipping_country} is not available.")
    print("-" * 20)

    # --- Example 3: Complex Bonus Calculation ---
    print("--- Employee Bonus Calculator ---")
    emp_rating = 5
    emp_dept = "Sales"
    emp_salary = 80000
    bonus_amount = calculate_employee_bonus(emp_rating, emp_dept, emp_salary)

    print(
        f"Employee in {emp_dept} with rating {emp_rating} gets a bonus of: ${bonus_amount:.2f}"
    )
    print("-" * 20)

```
