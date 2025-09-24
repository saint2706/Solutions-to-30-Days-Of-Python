# 🛡️ Day 15: Exception Handling

## Welcome to Day 15

Today, we'll explore a fundamental concept in programming: **exception handling**. This is a crucial skill for building robust and reliable applications.

## Why is Exception Handling Important for Business Analytics?

In the world of business analytics, you'll often be working with data from various sources, which can be unpredictable and messy. Your scripts might encounter errors like:

- Trying to read a file that doesn't exist.
- Performing calculations on missing or invalid data.
- Connecting to a database that is temporarily unavailable.

Without proper exception handling, these errors would crash your program, interrupting your analysis and potentially leading to data loss. By handling exceptions, you can ensure that your scripts can gracefully handle errors, log them for review, and continue with the rest of the analysis.

## Key Concepts in Python

In Python, we use `try...except` blocks to handle exceptions.

- **`try` block**: The code that might raise an exception is placed inside the `try` block.
- **`except` block**: If an exception occurs in the `try` block, the code inside the `except` block is executed.

### Example: `exception.py`

The `exception.py` script in this folder provides a simple example of exception handling combined with extended iterable unpacking.

```python
"""
Day 15: Exception Handling

This script demonstrates the use of extended iterable unpacking and a try-except block.
"""

# A list of country names
country_names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

try:
    # This is an example of extended iterable unpacking.
    # The '*' operator is used to assign multiple items to a single variable.
    # In this case, 'nordic_countries' will be a list of the first n-2 items,
    # 'estonia' will be the second to last item, and 'russia' will be the last item.
    *nordic_countries, estonia, russia = country_names

    print("Nordic Countries:", nordic_countries)
    print("Estonia:", estonia)
    print("Russia:", russia)

except Exception as e:
    # This block will be executed if any exception occurs in the 'try' block.
    # It's a good practice to catch specific exceptions instead of the general 'Exception',
    # but for this educational example, we are catching any possible exception.
    print(f"An error occurred: {e}")
```

## 💻 Exercises: Day 15

1. **Handling a `ValueError`**:
    - Write a script that asks the user to enter their age.
    - Use a `try...except` block to handle the `ValueError` that might occur if the user enters a non-numeric value.
    - Print a user-friendly error message if a `ValueError` occurs.

2. **Handling a `ZeroDivisionError`**:
    - Write a script that asks the user for two numbers and divides the first number by the second number.
    - Use a `try...except` block to handle the `ZeroDivisionError` that might occur if the user enters 0 as the second number.

3. **Refactor `exception.py`**:
    - Modify the `exception.py` script to handle the case where the `country_names` list has fewer than two elements. What kind of error do you get? How can you handle it specifically?

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned how to make your Python scripts more robust and reliable using exception handling. This is a critical skill for any data analyst or developer.
