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

Day 9: Solutions to Exercises

```python

# --- Exercise 1: Discount Policy Automation ---
print("--- Solution to Exercise 1 ---")
purchase_amount = 120

if purchase_amount > 100:
    discount = 0.10
elif purchase_amount > 50:
    discount = 0.05
else:
    discount = 0.0

final_price = purchase_amount * (1 - discount)

print(f"Original Amount: ${purchase_amount:.2f}")
print(f"Discount Rate: {discount * 100}%")
print(f"Final Price: ${final_price:.2f}")
print("-" * 20)


# --- Exercise 2: Shipping Cost Calculator ---
print("--- Solution to Exercise 2 ---")


# We can wrap this in a function to easily test different scenarios
def get_shipping_cost(country, order_weight_kg):
    cost = 0
    if country == "USA":
        if order_weight_kg > 50:
            cost = 75
        else:
            cost = 50
    elif country == "Canada":
        if order_weight_kg > 50:
            cost = 100
        else:
            cost = 65
    else:
        return "Shipping not available."

    return f"Shipping cost: ${cost}"


# Test cases
print(f"USA, 60kg -> {get_shipping_cost('USA', 60)}")
print(f"Canada, 40kg -> {get_shipping_cost('Canada', 40)}")
print(f"Mexico, 30kg -> {get_shipping_cost('Mexico', 30)}")
print("-" * 20)


# --- Exercise 3: Employee Bonus Calculation ---
print("--- Solution to Exercise 3 ---")


def calculate_bonus(rating, department, salary):
    bonus_rate = 0
    if rating >= 4:
        if department == "Sales":
            bonus_rate = 0.15
        else:
            bonus_rate = 0.10
    elif rating == 3:
        bonus_rate = 0.05
    # No need for an else for rating 1 or 2, as bonus_rate is already 0

    bonus_amount = salary * bonus_rate
    return bonus_amount


# Test cases
salary = 90000
print(
    f"Sales employee with rating 5 gets bonus: ${calculate_bonus(5, 'Sales', salary):,.2f}"
)
print(
    f"Engineering employee with rating 4 gets bonus: ${calculate_bonus(4, 'Engineering', salary):,.2f}"
)
print(
    f"Sales employee with rating 3 gets bonus: ${calculate_bonus(3, 'Sales', salary):,.2f}"
)
print(f"HR employee with rating 2 gets bonus: ${calculate_bonus(2, 'HR', salary):,.2f}")
print("-" * 20)

```
