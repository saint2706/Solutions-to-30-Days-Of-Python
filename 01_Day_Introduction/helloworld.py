"""
Day 1: Python for Business Analytics - First Steps

This script demonstrates basic Python concepts using business-relevant examples.
We will perform a simple profit calculation and check the types of various
business-related data points.
"""

# The print() function is used to display output.
# Let's start with a welcome message for our analytics dashboard.
print("Welcome to the Quarterly Business Review Dashboard")
print()  # This prints a blank line for spacing.

# --- Basic Business Calculations ---
# Let's calculate the Gross Profit for a product.
# Gross Profit = Revenue - Cost of Goods Sold (COGS)

revenue = 500000
cogs = 350000
gross_profit = revenue - cogs

# We use an f-string (formatted string literal) to print the result.
# This is a modern and readable way to mix text and variables.
print(f"Total Revenue: ${revenue}")
print(f"Cost of Goods Sold: ${cogs}")
print(f"Gross Profit: ${gross_profit}")
print()

# Now, let's calculate the Gross Profit Margin.
# Gross Profit Margin = (Gross Profit / Revenue) * 100
gross_profit_margin = (gross_profit / revenue) * 100

# The :.2f inside the curly braces formats the number to two decimal places.
print(f"Gross Profit Margin: {gross_profit_margin:.2f}%")
print("-" * 20)  # Prints a separator line for clarity.

# --- Understanding Data Types in a Business Context ---
# Python automatically detects the type of data you are using.
# We can use the type() function to see what Python thinks a piece of data is.

print("Checking the types of some common business data points:")

# An integer (int) is a whole number.
units_sold = 1500
print(f"Data: {units_sold}, Type: {type(units_sold)}")

# A float is a number with a decimal point.
product_price = 49.99
print(f"Data: {product_price}, Type: {type(product_price)}")

# A string (str) is text, enclosed in quotes.
company_name = "InnovateCorp"
print(f"Data: '{company_name}', Type: {type(company_name)}")

# A boolean (bool) is either True or False.
is_in_stock = True
print(f"Data: {is_in_stock}, Type: {type(is_in_stock)}")

# A list is a collection of items.
quarterly_sales = [110000, 120000, 135000, 140000]
print(f"Data: {quarterly_sales}, Type: {type(quarterly_sales)}")
