# 📘 Day 11: Functions - Creating Reusable Business Tools

As you perform more complex analysis, you'll find yourself writing the same pieces of code over and over. For example, calculating the net profit margin for different products or departments. Copying and pasting code is tedious and error-prone. What if you make a mistake in one copy but not the others?

The solution is to package your reusable code into **functions**. A function is a named, reusable block of code that performs a specific task.

## Why Use Functions in Business Analysis?

1. **Reusability:** Write a complex calculation once (e.g., for calculating customer lifetime value) and use it anywhere in your project.
2. **Readability:** Instead of a long, complex script, you can have a series of well-named functions. `calculate_roi()` is much clearer than a block of raw math.
3. **Maintainability:** If a business rule changes (e.g., the way a bonus is calculated), you only have to update the code in one place: the function where it's defined.

## Defining a Function

You define a function using the `def` keyword, followed by the function's name, parentheses `()`, and a colon `:`. The code inside the function must be indented.

```python
def greet_team():
    print("Hello, Analytics Team!")

# To run the code inside the function, you "call" it:
greet_team()
```

## Parameters: Providing Inputs to Your Function

Functions become truly powerful when you can give them data to work with. These inputs are called **parameters** (or arguments).

```python
def calculate_gross_margin(revenue, cogs):
    gross_profit = revenue - cogs
    margin = (gross_profit / revenue) * 100
    print(f"The Gross Profit Margin is {margin:.2f}%.")

# Now we can call the function with different data
calculate_gross_margin(500000, 350000) # For Product A
calculate_gross_margin(250000, 180000) # For Product B
```

## Return Values: Getting Outputs from Your Function

Printing a result is good, but often you need to get a value *back* from a function to use in another calculation. The `return` statement sends a value back to whoever called the function.

```python
def get_net_profit(revenue, expenses):
    net_profit = revenue - expenses
    return net_profit

# We can store the returned value in a variable
product_a_profit = get_net_profit(500000, 400000)
product_b_profit = get_net_profit(250000, 210000)

total_profit = product_a_profit + product_b_profit
print(f"Total Net Profit from both products: ${total_profit}")
```

## Default Parameter Values

You can provide a default value for a parameter. If the person calling the function doesn't provide a value for that parameter, the default will be used.

```python
def calculate_final_price(base_price, tax_rate=0.08): # 8% default tax rate
    final_price = base_price * (1 + tax_rate)
    return final_price

price_in_ca = calculate_final_price(100, tax_rate=0.09) # Provide a specific tax rate
price_in_tx = calculate_final_price(100) # Use the default 8% tax rate
```

## 💻 Exercises: Day 11

1. **Commission Calculator Function:**
    * Create a function called `calculate_commission`.
    * It should take `sales_amount` as a parameter.
    * Inside the function, calculate a commission of 15% of the sales amount.
    * The function should `return` the calculated commission amount.
    * Call the function with a sample sales amount and print the returned commission.

2. **Employee Bonus Eligibility Function:**
    * Create a function called `is_eligible_for_bonus`.
    * It should take two parameters: `performance_rating` (a number) and `years_of_service`.
    * The function should `return` `True` if the rating is 4 or 5 AND they have more than 2 years of service. Otherwise, it should `return` `False`.
    * Call the function with a few different scenarios and print the results.

3. **Format Currency Function:**
    * Create a function called `format_currency`.
    * It should take a `number` as a parameter.
    * It should `return` a string formatted as currency (e.g., `$1,250.50`).
    * Hint: You can use an f-string with formatting for the comma and decimal places: `f"${number:,.2f}"`.
    * Call the function with a number and print the result.

🎉 **Great work!** Functions are the key to writing clean, organized, and professional code. By packaging your logic into reusable tools, you're moving from a simple scripter to a true programmer.
