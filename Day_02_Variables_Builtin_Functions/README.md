# 📘 Day 2: Storing Business Data in Variables

In Day 1, we performed some basic calculations. But in the real world, data is not static. It changes, it has names, and we need a way to manage it. In programming, we do this using **variables**.

## What is a Variable?

Think of a variable as a labeled container for a piece of information. Instead of working with a raw number like `500000`, we can put it in a container labeled `revenue`. This makes our code infinitely more readable and manageable.

**`revenue = 500000`**

From now on, we can just use the name `revenue` to refer to that number. If our revenue changes next quarter, we only have to update it in one place.

### Naming Conventions for Business Variables

The names you choose for your variables are important. Good variable names make your code self-explanatory. Here are some best practices:

* **Be Descriptive:** `quarterly_sales` is much better than `qs`.
* **Use Snake Case:** For variable names with multiple words, Python convention is to separate them with an underscore. For example: `cost_of_goods_sold`, `net_profit`, `employee_name`.
* **Don't Start with Numbers or Use Special Characters:** Variable names must start with a letter or an underscore.

## Built-in Functions: Your Basic Toolkit

Python comes with a set of **built-in functions** that act as a fundamental toolkit for common tasks. Think of them as pre-built actions you can use anytime. We've already used `print()` and `type()`. Let's introduce a few more that are incredibly useful for business analysis.

* `len()`: Tells you the length of something, like the number of transactions in a list or the number of characters in a company name.
* `sum()`: Calculates the sum of a list of numbers. Perfect for totaling sales or expenses.
* `min()` and `max()`: Find the minimum and maximum values in a list. Useful for identifying the best and worst-performing products.
* `round()`: Rounds a number to a specified number of decimal places, essential for presenting financial data cleanly.

You can see these functions in action in the `variables.py` file for this lesson.

## Getting Input from a User

Sometimes, you'll want your script to be interactive. The `input()` function lets you prompt the user for information. For example, you could ask a user to enter their sales region to generate a custom report.

**`region = input("Please enter your sales region: ")`**

**Important Note:** The `input()` function always returns data as a string (text). If you need to perform mathematical operations on a number you get from the user, you must first convert it to a numerical type (like `int` or `float`). We'll cover this in more detail later.

## 💻 Exercises: Day 2

1. **Company Profile Variables:**
    * In a new Python script, declare variables to store the following information for a fictional company:
        * `company_name` (e.g., "InnovateCorp")
        * `year_founded` (e.g., 2015)
        * `current_revenue` (e.g., 2500000.50)
        * `is_publicly_traded` (e.g., `False`)
    * Print each of these variables with a descriptive label.

2. **Sales Analysis:**
    * A list of sales transactions for the week is: `[150.50, 200.00, 75.25, 300.75, 120.00]`.
    * Store these sales in a variable called `weekly_sales`.
    * Use built-in functions to calculate and print the following:
        * The total number of sales transactions (`len()`).
        * The total revenue for the week (`sum()`).
        * The smallest sale (`min()`).
        * The largest sale (`max()`.
        * The average sale amount (Hint: `sum()` / `len()`).

3. **User Input for a Profit Calculator:**
    * Create a simple profit calculator that asks the user for their total revenue and total expenses.
    * Calculate the profit (revenue - expenses).
    * Print the calculated profit.
    * Remember to convert the user's input from a string to a number (e.g., `float(input("Enter revenue: "))`) before doing calculations!

🎉 **Well done!** You've learned how to store and manage data using variables and how to use Python's built-in functions to start analyzing that data. These are foundational skills for everything that comes next.
