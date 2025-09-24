# 📘 Day 10: Loops - Automating Repetitive Business Tasks

So far, we've been working with data one item at a time. But what if you have a list of 10,000 sales transactions? Or a list of 500 employees? You're not going to write code for each one individually. This is where **loops** come in.

Loops are one of the most powerful concepts in programming. They allow you to perform the same action on every item in a collection, automating what would otherwise be an impossibly tedious task.

## The `for` Loop

The `for` loop is the most common type of loop in Python. It iterates over a sequence (like a list, tuple, or dictionary) and executes a block of code for each item in that sequence.

**The structure is:** `for item in sequence:`

```python
# Calculating total revenue from a list of sales
monthly_sales = [2340, 3100, 2900, 4500]
total_revenue = 0

for sale in monthly_sales:
    total_revenue += sale  # This line runs for each item in the list

print(f"Total Revenue: ${total_revenue}")
# This is much better than writing: 2340 + 3100 + 2900 + 4500
```

In this example, the variable `sale` takes on the value of each item in `monthly_sales` one by one.

## Looping with a Condition

The real power of loops comes when you combine them with conditionals. This allows you to perform an action on only the items that meet a certain criteria.

```python
# Find all transactions over a certain amount
transactions = [150, 99, 500, 250, 1200, 750]
large_transactions = [] # An empty list to store the results

for amount in transactions:
    if amount > 500:
        large_transactions.append(amount)

print(f"All large transactions: {large_transactions}")
```

## Looping Through Dictionaries

You can loop through dictionaries as well. The `.items()` method is particularly useful as it gives you access to both the key and the value for each item in the dictionary.

```python
product_inventory = {
    "Laptop": 25,
    "Mouse": 150,
    "Keyboard": 75
}

for product, count in product_inventory.items():
    print(f"Product: {product}, Inventory Count: {count}")
```

## The `while` Loop

A `while` loop runs as long as a certain condition is `True`. It's used when you don't know beforehand how many times you need to loop. For data analysis, `for` loops are much more common, but `while` loops can be useful for tasks like simulating a process until a target is met.

```python
# Simulate growing an investment until it doubles
investment = 10000
target = 20000
interest_rate = 0.07
years = 0

while investment < target:
    investment *= (1 + interest_rate) # Apply interest
    years += 1

print(f"It will take {years} years for the investment to double.")
```

## 💻 Exercises: Day 10

1. **Calculate Average Employee Age:**
    * You have a list of employee dictionaries:

        ```python
        employees = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 45},
            {"name": "Charlie", "age": 35}
        ]
        ```

    * Use a `for` loop to calculate the sum of all employee ages.
    * Calculate and print the average age of the employees.

2. **Filter High-Priority Customers:**
    * You have a list of customer dictionaries.
    * Use a `for` loop to iterate through the list.
    * If a customer has `"total_spent"` greater than 2000, add their `"name"` to a new list called `high_priority_customers`.
    * Print the `high_priority_customers` list at the end.

        ```python
        customers = [
            {"name": "InnovateCorp", "total_spent": 5500},
            {"name": "DataDriven Inc.", "total_spent": 1200},
            {"name": "Analytics LLC", "total_spent": 2100}
        ]
        ```

3. **Inventory Stock Alert:**
    * You have a dictionary of product inventory counts: `inventory = {"Laptops": 15, "Mice": 150, "Keyboards": 45}`.
    * The low stock threshold is 50.
    * Use a `for` loop to iterate through the inventory dictionary's items.
    * For each product, use an `if` statement to check if the count is below the threshold.
    * If a product is low on stock, print an alert message, e.g., "Alert: Laptops are low on stock (15 units remaining)."

🎉 **Incredible!** Loops are the key to unlocking automation and working with datasets of any size. The combination of loops and conditionals is the foundation of almost all data processing and analysis tasks. You've completed the core structures of Python!
