# 📘 Day 3: Operators - The Tools for Business Calculation and Logic

In programming, an **operator** is a symbol that tells the computer to perform a specific mathematical or logical manipulation. For a business analyst, operators are the tools you'll use to calculate financial metrics, compare results, and create business rules.

## Arithmetic Operators

These are the operators you know from basic math. They are the foundation of any quantitative analysis.

| Operator | Name           | Example (in Python) | Business Context                  |
| :------- | :------------- | :------------------ | :-------------------------------- |
| `+`      | Addition       | `revenue + bonus`   | Calculating total compensation    |
| `-`      | Subtraction    | `sales - returns`   | Calculating net sales             |
| `*`      | Multiplication | `units * price`     | Calculating total revenue         |
| `/`      | Division       | `profit / revenue`  | Calculating profit margin         |
| `%`      | Modulus        | `10 % 3` (is 1)     | Finding remainder (e.g., in batch processing) |
| `**`     | Exponent       | `(1 + 0.05) ** 3`   | Calculating compound interest     |
| `//`     | Floor Division | `10 // 3` (is 3)    | Finding how many full units fit   |

## Assignment Operators

Assignment operators are used to assign values to variables. We've already used the basic one, `=`. But there are shorthand operators that are very common.

| Operator | Example      | Equivalent to     | Business Context                  |
| :------- | :----------- | :---------------- | :-------------------------------- |
| `=`      | `x = 5`      | `x = 5`           | Setting an initial value          |
| `+=`     | `x += 5`     | `x = x + 5`       | Accumulating a total (e.g., summing daily sales) |
| `-=`     | `x -= 5`     | `x = x - 5`       | Depleting a budget                |
| `*=`     | `x *= 5`     | `x = x * 5`       | Applying a multiplier             |

## Comparison Operators

These operators are used to compare two values, and the result is always a Boolean (`True` or `False`). This is the foundation of filtering data and making decisions in your code.

| Operator | Name                       | Example                | Business Context                                  |
| :------- | :------------------------- | :--------------------- | :------------------------------------------------ |
| `==`     | Equal to                   | `region == "North"`    | Is the sale from the North region?                |
| `!=`     | Not equal to               | `status != "Shipped"`  | Is the order status something other than shipped? |
| `>`      | Greater than               | `revenue > 10000`      | Did we exceed the revenue target?                 |
| `<`      | Less than                  | `inventory < 50`       | Is the inventory level low?                       |
| `>=`     | Greater than or equal to   | `score >= 0.8`         | Is the customer's credit score high enough?       |
| `<=`     | Less than or equal to      | `discount <= 0.15`     | Is the discount within the allowed limit?         |

## Logical Operators

Logical operators are used to combine conditional statements. They allow you to create complex business rules.

| Operator | Description                               | Example                                  | Business Context                                        |
| :------- | :---------------------------------------- | :--------------------------------------- | :------------------------------------------------------ |
| `and`    | Returns `True` if both statements are true | `revenue > 10000 and region == "North"`  | Finding high-value sales from the North region.         |
| `or`     | Returns `True` if one of the statements is true | `status == "Urgent" or inventory < 10` | Flagging an order if it's marked urgent or if stock is low. |
| `not`    | Reverses the result, returns `False` if the result is true | `not is_holiday`          | Checking if today is a business day.                    |

## 💻 Exercises: Day 3

1.  **Calculate Net Profit Margin:**
    *   A company has a `revenue` of 1,200,000 and `total_expenses` of 850,000.
    *   Calculate the `profit` (`revenue - total_expenses`).
    *   Calculate the `net_profit_margin` (`profit / revenue`).
    *   Print the net profit margin as a percentage, rounded to two decimal places.

2.  **Inventory Check:**
    *   You have `inventory_count` of 45 units for a product.
    *   The `low_stock_threshold` is 50 units.
    *   The `reorder_threshold` is 25 units.
    *   Write a Python script that prints:
        *   `True` or `False` if the inventory is considered low stock.
        *   `True` or `False` if a reorder is required.

3.  **Sales Bonus Eligibility:**
    *   A salesperson is eligible for a bonus if they meet one of two conditions:
        *   Condition A: They made over $10,000 in `sales` **and** have been with the company for more than 2 `years_of_service`.
        *   Condition B: They are the `top_performer_last_quarter` (a Boolean variable).
    *   Create variables for `sales`, `years_of_service`, and `top_performer_last_quarter`.
    *   Test your logic with a few different scenarios (e.g., high sales but new employee, low sales but top performer, etc.). Print whether the salesperson is eligible for a bonus (`True` or `False`).

🎉 **Excellent work!** You're now equipped with the operators needed to perform the vast majority of business calculations and logical checks you'll encounter. These are the verbs of data analysis.
