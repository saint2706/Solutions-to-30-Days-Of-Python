# 📘 Day 13: List Comprehension - Elegant Data Manipulation

In data analysis, you constantly need to create new lists by transforming or filtering existing ones. For example, creating a list of adjusted prices from a list of base prices, or filtering a list of all sales to get only the ones from a specific region.

We know how to do this with a `for` loop and an `if` statement. But Python provides a more concise and elegant way to do this called **list comprehension**. It's a hallmark of clean, professional Python code.

## From `for` Loop to List Comprehension

Let's say we have a list of sales and we want to create a new list containing only the sales that are over $1000.

**The `for` loop way:**

```python
sales = [500, 1200, 800, 1500, 300]
large_sales = []
for sale in sales:
    if sale > 1000:
        large_sales.append(sale)
# large_sales is now [1200, 1500]
```
This takes 4 lines of code. It works, but we can do better.

**The list comprehension way:**

```python
sales = [500, 1200, 800, 1500, 300]
large_sales = [sale for sale in sales if sale > 1000]
# large_sales is now [1200, 1500]
```
This does the exact same thing in a single, highly readable line.

## The Syntax of List Comprehension

A list comprehension is made of a few parts inside square brackets `[]`:

`new_list = [expression for item in iterable if condition]`

1.  **Expression:** What to do with each item. This could be the item itself (`sale`), or a calculation (`sale * 1.1`).
2.  **`for item in iterable`:** The loop part, which iterates through the original list (the `iterable`).
3.  **`if condition` (Optional):** A filter that decides whether or not to include the item in the new list.

### Example: Applying a Price Increase

Let's apply a 10% price increase to a list of product prices.

```python
prices = [100, 150, 200, 80]

# The 'expression' is the calculation we want to perform
new_prices = [price * 1.1 for price in prices]
# new_prices is now [110.0, 165.0, 220.0, 88.0]
```

### Example: Extracting Employee Names

Let's get a simple list of names from a more complex list of employee dictionaries.

```python
employees = [
    {"name": "Alice", "department": "Sales"},
    {"name": "Bob", "department": "Engineering"},
    {"name": "Charlie", "department": "Sales"}
]

# The 'expression' is accessing the value of the "name" key
sales_team_names = [employee["name"] for employee in employees if employee["department"] == "Sales"]
# sales_team_names is now ["Alice", "Charlie"]
```

## 💻 Exercises: Day 13

1.  **Calculate Sales Commissions:**
    *   You have a list of sales figures: `sales = [2500, 8000, 12000, 5500]`.
    *   The commission rate is 10%.
    *   Use a list comprehension to create a new list called `commissions` where each element is 10% of the corresponding sale.
    *   Print the `commissions` list.

2.  **Filter Products by Category:**
    *   You have a list of product dictionaries.
    *   Use a list comprehension to create a new list containing only the names of products that are in the "electronics" category.
    *   Print the resulting list.
        ```python
        products = [
            {"name": "Laptop", "category": "electronics"},
            {"name": "T-Shirt", "category": "apparel"},
            {"name": "Keyboard", "category": "electronics"},
            {"name": "Coffee Mug", "category": "homeware"}
        ]
        ```

3.  **Format Prices for Display:**
    *   You have a list of prices as floats: `prices = [49.99, 199.99, 19.95, 24.50]`.
    *   Use a list comprehension to create a new list called `display_prices`.
    *   Each item in the new list should be a string, formatted as currency (e.g., `"$49.99"`).
    *   Hint: The expression part can include calling a function or using an f-string.

🎉 **Excellent!** List comprehensions are a powerful tool for writing clean, efficient, and professional Python code. They are heavily used in data analysis for quick and readable data transformations.
