# 📘 Day 14: Higher-Order Functions & Lambda - Advanced Data Processing

Today, we're going to explore a more advanced—but incredibly powerful—concept in Python: **higher-order functions**. This is a style of programming that is heavily used in data analysis for its conciseness and power.

## What is a Higher-Order Function?

A higher-order function is a function that does at least one of the following:

1. Takes one or more functions as arguments.
2. Returns a function as its result.

In a business context, this allows you to create flexible, generic tools. Imagine a function that can apply *any* calculation to a list of numbers. You could pass it a `calculate_tax` function or a `calculate_bonus` function. The core logic of applying the calculation is separated from the calculation itself.

## Key Higher-Order Functions: `map` and `filter`

Python has several built-in higher-order functions. For data analysis, `map` and `filter` are the most important.

### `map(function, iterable)`

The `map` function applies a given function to every item of an iterable (like a list) and returns a map object (which can be converted to a list).

**Business Scenario:** You have a list of employee salaries and you need to apply a 10% bonus to each one.

```python
def apply_bonus(salary):
    return salary * 1.10

salaries = [50000, 80000, 120000]

# map applies the apply_bonus function to each salary
new_salaries = list(map(apply_bonus, salaries))
# new_salaries is now [55000.0, 88000.0, 132000.0]
```

### `filter(function, iterable)`

The `filter` function constructs an iterator from elements of an iterable for which a function returns `True`.

**Business Scenario:** You have a list of project ROI percentages and you want to find all the "high-yield" projects (ROI > 15%).

```python
def is_high_yield(roi):
    return roi > 15

project_rois = [12, 20, 8, 25, 14]

# filter keeps only the items for which is_high_yield returns True
high_yield_projects = list(filter(is_high_yield, project_rois))
# high_yield_projects is now [20, 25]
```

## Lambda Functions: Quick, Anonymous Functions

Sometimes, the function you want to use with `map` or `filter` is very simple and you only need it once. Writing a full `def` statement for it can feel clunky.

A **lambda function** is a small, anonymous function defined with the `lambda` keyword.

`lambda arguments: expression`

Let's rewrite our `map` and `filter` examples using lambda functions.

**`map` with `lambda`:**

```python
salaries = [50000, 80000, 120000]
# The lambda function `lambda s: s * 1.10` does the same as our apply_bonus function
new_salaries = list(map(lambda s: s * 1.10, salaries))
```

**`filter` with `lambda`:**

```python
project_rois = [12, 20, 8, 25, 14]
# The lambda function `lambda r: r > 15` does the same as our is_high_yield function
high_yield_projects = list(filter(lambda r: r > 15, project_rois))
```

This syntax is extremely common in data analysis libraries like Pandas.

## 💻 Exercises: Day 14

1. **Standardize Department Names:**
    * You have a list of department names in various formats: `departments = ["Sales", " marketing ", "  Engineering", "HR  "]`.
    * Use `map` and a `lambda` function to create a new list where each department name is cleaned (whitespace stripped) and converted to lowercase.

2. **Filter Active Subscriptions:**
    * You have a list of customer dictionaries.
    * Use `filter` and a `lambda` function to create a new list containing only the customers whose `"subscription_status"` is `"active"`.

        ```python
        customers = [
            {"id": 1, "status": "active"},
            {"id": 2, "status": "inactive"},
            {"id": 3, "status": "active"},
            {"id": 4, "status": "cancelled"}
        ]
        ```

3. **Sort Complex Data:**
    * Python's `sorted()` function is a higher-order function that can take a `key` function.
    * You have a list of product dictionaries. You want to sort them by `price` from lowest to highest.
    * Use `sorted()` with a `lambda` function as the `key` to achieve this. The lambda function should extract the price from each dictionary.

        ```python
        products = [
            {"name": "Laptop", "price": 1200},
            {"name": "Mouse", "price": 25},
            {"name": "Keyboard", "price": 75}
        ]
        # Hint: sorted(products, key=lambda p: ...)
        ```

🎉 **Congratulations!** This was a conceptually challenging day. Higher-order functions and lambdas are a gateway to a more powerful and expressive style of programming that you will see everywhere in the world of data science.
