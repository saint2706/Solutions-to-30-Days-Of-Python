# 📘 Day 10: Loops - Automating Repetitive Business Tasks

What if you have a list of 10,000 sales transactions? You won't write code for each one. This is where **loops** come in. Loops allow you to perform the same action on every item in a collection, automating what would otherwise be an impossibly tedious task.

## Key Loop Types

- **`for` loop:** The most common loop. It iterates over a sequence (like a list or dictionary) and executes a block of code for each item.
  ```python
  # Calculate total revenue from a list of sales
  total_revenue = 0
  for sale in monthly_sales:
      total_revenue += sale
  ```
- **`while` loop:** Runs as long as a certain condition is `True`. It's used when you don't know beforehand how many times you need to loop, such as in a simulation.

## Combining Loops and Conditionals

The real power comes from combining loops with `if` statements. This allows you to perform an action on only the items that meet a certain criteria, which is the foundation of filtering and transforming data.

```python
# Find all transactions over a certain amount
large_transactions = []
for amount in transactions:
    if amount > 500:
        large_transactions.append(amount)
```

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `loops.py`, has been refactored to place each looping task into its own testable function.

1. **Review the Code:** Open `Day_10_Loops/loops.py`. Notice the functions `calculate_total_from_list()`, `filter_high_value_customers()`, and `simulate_investment_growth()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_10_Loops/loops.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function:
   ```bash
   pytest tests/test_day_10.py
   ```

## 💻 Exercises: Day 10

1. **Calculate Average Employee Age:**

   - In a new script (`my_solutions_10.py`), create a list of employee dictionaries: `employees = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Charlie", "age": 35}]`.
   - Create a function `calculate_average_age(employee_list)` that takes a list of employee dictionaries.
   - Inside the function, use a `for` loop to get the sum of all ages.
   - Return the average age (`total_age / number_of_employees`).
   - Call your function and print the result.

1. **Filter High-Priority Customers:**

   - You have a list of customer dictionaries (see `loops.py` for an example).
   - Import the `filter_high_value_customers` function from the lesson script.
   - Call the function with your list of customers and print the result.

1. **Inventory Stock Alert:**

   - You have a dictionary of product inventory: `inventory = {"Laptops": 15, "Mice": 150, "Keyboards": 45}`.
   - Import the `check_inventory_levels` function.
   - Call the function to get a list of low-stock items.
   - Loop through the returned list and print an alert for each item.

🎉 **Incredible!** The combination of loops and conditionals is the foundation of almost all data processing and analysis tasks. You've completed the core structures of Python!

Day 10: Solutions to Exercises

```python

# --- Exercise 1: Calculate Average Employee Age ---
print("--- Solution to Exercise 1 ---")
employees = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 45},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28},
]

total_age = 0
for employee in employees:
    total_age += employee["age"]

# Ensure we don't divide by zero if the list is empty
if len(employees) > 0:
    average_age = total_age / len(employees)
    print(f"The average age of employees is: {average_age:.1f} years")
else:
    print("No employees in the list.")
print("-" * 20)


# --- Exercise 2: Filter High-Priority Customers ---
print("--- Solution to Exercise 2 ---")
customers = [
    {"name": "InnovateCorp", "total_spent": 5500},
    {"name": "DataDriven Inc.", "total_spent": 1200},
    {"name": "Analytics LLC", "total_spent": 2100},
    {"name": "Key Insights", "total_spent": 1800},
]

high_priority_customers = []
for customer in customers:
    if customer["total_spent"] > 2000:
        high_priority_customers.append(customer["name"])

print(f"High-priority customers (spent > $2000): {high_priority_customers}")
print("-" * 20)


# --- Exercise 3: Inventory Stock Alert ---
print("--- Solution to Exercise 3 ---")
inventory = {"Laptops": 15, "Mice": 150, "Keyboards": 45, "Monitors": 25}
low_stock_threshold = 50

print("Checking inventory levels...")
for product, count in inventory.items():
    if count < low_stock_threshold:
        print(f"  - ALERT: {product} are low on stock ({count} units remaining).")
print("-" * 20)

```
