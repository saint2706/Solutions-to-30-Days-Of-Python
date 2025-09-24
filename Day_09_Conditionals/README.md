# 📘 Day 9: Conditionals - Implementing Business Logic

Business is full of rules and decisions. "If a customer spends over $1000, they get a 10% discount." "If inventory is below 50 units, flag it for reorder." "If a payment is overdue, send a reminder email."

In Python, we implement this decision-making process using **conditional statements**. They allow your code to execute different actions based on different conditions.

## The `if` Statement

The `if` statement is the simplest conditional. It executes a block of code **only if** a certain condition is `True`.

```python
revenue = 120000
sales_target = 100000

if revenue > sales_target:
    print("Congratulations! You have exceeded the sales target.")
    # This block of code is indented, showing it's part of the if statement.
```

## The `else` Statement

What if the condition is `False`? The `else` statement lets you define an alternative block of code to execute.

```python
inventory_level = 35
low_stock_threshold = 50

if inventory_level < low_stock_threshold:
    print("Alert: Inventory is low. Please reorder.")
else:
    print("Inventory level is sufficient.")
```

## The `elif` Statement

Sometimes you have more than two possibilities. The `elif` (short for "else if") statement lets you check for multiple conditions in sequence.

```python
# Classifying a customer based on their total spending
total_spent = 750

if total_spent > 1000:
    customer_tier = "Gold"
elif total_spent > 500:
    customer_tier = "Silver"  # This will be chosen, since 750 > 500
elif total_spent > 100:
    customer_tier = "Bronze"
else:
    customer_tier = "Standard"

print(f"Customer Tier: {customer_tier}")
```

Python checks the conditions from top to bottom and executes the *first* block where the condition is `True`. It then skips the rest.

## Combining Conditions

You can create complex business rules by combining conditions with the logical operators (`and`, `or`, `not`) we learned about in Day 3.

```python
# Approving a loan application
credit_score = 720
has_stable_income = True

if credit_score > 700 and has_stable_income:
    print("Loan application approved.")
else:
    print("Loan application requires further review.")
```

## 💻 Exercises: Day 9

1. **Discount Policy Automation:**
    * Write a script that determines a customer's discount based on their purchase amount.
    * `purchase_amount = 120` (you can change this value to test).
    * The rules are:
        * If the purchase is over $100, the discount is 10%.
        * If the purchase is over $50 but not over $100, the discount is 5%.
        * Otherwise, the discount is 0%.
    * Calculate the final price and print it.

2. **Shipping Cost Calculator:**
    * Create a script that calculates shipping cost based on the customer's location and order weight.
    * Create variables for `country` ("USA" or "Canada") and `order_weight_kg`.
    * The rules are:
        * If the country is "USA":
            * If the weight is over 50kg, shipping is $75.
            * Otherwise, shipping is $50.
        * If the country is "Canada":
            * If the weight is over 50kg, shipping is $100.
            * Otherwise, shipping is $65.
        * For any other country, print "Shipping not available."
    * Print the calculated shipping cost.

3. **Employee Bonus Calculation:**
    * An employee's bonus is based on their `performance_rating` (a number from 1 to 5) and their `department`.
    * The rules:
        * If the rating is 4 or 5, they get a bonus.
            * If their department is "Sales", the bonus is 15% of their `salary`.
            * For any other department, the bonus is 10% of their `salary`.
        * If the rating is 3, the bonus is 5% of their `salary`, regardless of department.
        * If the rating is 1 or 2, the bonus is 0.
    * Write a script that calculates and prints the bonus amount.

🎉 **Fantastic progress!** You can now translate complex business rules into code that makes decisions automatically. This is a fundamental skill for automating reports, classifying data, and building analytical models.
