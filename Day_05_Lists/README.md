# 📘 Day 5: Managing Collections of Business Data with Lists

In business, you're rarely dealing with a single piece of data. You have lists of customers, lists of quarterly sales figures, lists of products, and so on. Python's most fundamental tool for managing ordered collections of data is the **list**.

## What is a List?

A list is an ordered, changeable collection of items. You create a list by placing items inside square brackets `[]`, separated by commas.

```python
# A list of department names (strings)
departments = ["Sales", "Marketing", "Human Resources", "Engineering"]

# A list of quarterly sales figures (floats)
quarterly_sales = [120000.50, 135000.75, 110000.00, 145000.25]

# A list can even contain mixed data types
product_info = ["Gadget-X", 49.99, 1500, True] # Name, Price, Units Sold, In Stock
```

## Accessing Data in Lists: Indexing and Slicing

Because lists are ordered, you can access any item by its position, which is called its **index**. Python indexing starts at **0**.

```python
departments = ["Sales", "Marketing", "HR", "Engineering"]
# Index:         0          1        2         3

first_department = departments[0]  # Accesses "Sales"
third_department = departments[2]  # Accesses "HR"

# You can also use negative indexing to count from the end.
last_department = departments[-1] # Accesses "Engineering"
```

**Slicing** is how you get a sub-section of a list.

```python
first_two_departments = departments[0:2]  # Gets items at index 0 and 1. Result: ["Sales", "Marketing"]
all_but_first = departments[1:]         # Gets everything from index 1 to the end.
```

## Modifying Lists: Your Data Management Toolkit

Lists are dynamic. You can add, remove, and change items.

| Method         | Description                                        | Example                                    | Business Use Case                     |
| :------------- | :------------------------------------------------- | :----------------------------------------- | :------------------------------------ |
| `.append()`    | Adds an item to the end of the list.               | `sales.append(250.00)`                     | Adding a new sales transaction.       |
| `.insert()`    | Adds an item at a specified index.                 | `tasks.insert(0, "Urgent Task")`           | Adding a high-priority item to the top of a list. |
| `.remove()`    | Removes the first item with the specified value.   | `products.remove("Defective Item")`        | Removing a returned or defective product. |
| `del`          | Removes the item at a specified index.             | `del sales[0]`                             | Deleting an erroneous transaction.      |
| `.pop()`       | Removes the item at a specified index (and returns it). | `last_sale = sales.pop()`               | Processing items one by one.          |
| `.sort()`      | Sorts the list in place.                           | `sales.sort(reverse=True)`                 | Ranking sales from highest to lowest. |
| `.reverse()`   | Reverses the order of the list in place.           | `timeline.reverse()`                       | Viewing events in reverse chronological order. |

## 💻 Exercises: Day 5

1. **Manage a Product List:**
    * Create a list of product names: `["Laptop", "Mouse", "Keyboard", "Monitor"]`.
    * A new product, "Webcam", is now in stock. Add it to the end of the list.
    * The "Mouse" is sold out. Remove it from the list.
    * Print the final list of available products.

2. **Analyze Monthly Expenses:**
    * You have a list of monthly expenses: `[2200, 2350, 2600, 2130, 2190]`.
    * Find the total expenses for the period (`sum()`).
    * Find the month with the highest and lowest expenses (`min()`, `max()`).
    * A new expense of $2400 was incurred. Add it to the list.
    * Print the updated total expenses.

3. **Select Top Sales Performers:**
    * You have a list of sales figures for your team: `[5000, 8000, 4500, 12000, 6000, 11000]`.
    * Sort the list in descending order to identify the top performers.
    * "Slice" the list to get the top 3 sales figures.
    * Print the top 3 sales figures.

🎉 **Great job!** Lists are the workhorse for storing collections of data in Python. Understanding how to access, manage, and analyze data within lists is a fundamental skill for any data analyst.
