# 🏛️ Day 18: Classes and Objects

## Welcome to Day 18

Today, we're going to explore one of the most important concepts in modern programming: **Object-Oriented Programming (OOP)**, and its fundamental building blocks: **classes** and **objects**.

## Why is OOP Important for Business Analytics?

Object-Oriented Programming allows you to structure your code in a way that models real-world business concepts. For example, you could have a `Customer` object that stores all the information about a customer (name, email, purchase history), and has methods to calculate their total spending or identify their last purchase date.

This approach makes your code more organized, reusable, and easier to understand, which is especially important when you're building complex analytical models.

## Classes and Objects in Python

In Python, a **class** is a blueprint for creating objects. An **object** is an instance of a class.

## Exploring `CaO.py`

The `CaO.py` script in this folder provides two great examples of classes in Python: `Statistics` and `PersonAccount`.

### The `Statistics` Class

This class is a blueprint for creating objects that can perform statistical calculations on a list of numbers.

### The `PersonAccount` Class

This class is a blueprint for creating objects that can manage a person's income and expenses.

## 💻 Exercises: Day 18

1. **Create a `Car` class**:
    * Create a class named `Car` with the following attributes: `make`, `model`, and `year`.
    * Add a method named `display_info` that prints the car's information in a user-friendly format.
    * Create an instance of the `Car` class and call the `display_info` method.

2. **Add a `get_age` method to the `Car` class**:
    * Add a method to the `Car` class that calculates the age of the car (current year - year of the car).
    * You can use the `datetime` module to get the current year.

3. **Extend the `PersonAccount` class**:
    * Add a new method to the `PersonAccount` class named `get_income_sources` that returns a list of all the income sources.
    * Add a new method named `get_expense_sources` that returns a list of all the expense sources.

### Solutions

You can find the solutions to these exercises in the `solutions.py` file in this directory.

🎉 **Congratulations!** You've learned the basics of object-oriented programming in Python. This will enable you to write more organized and powerful analytical scripts.
