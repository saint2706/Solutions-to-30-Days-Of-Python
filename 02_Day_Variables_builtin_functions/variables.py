"""
Day 2: Storing and Analyzing Business Data

This script demonstrates the use of variables to store business data
and built-in functions to perform basic analysis.
"""

# --- Storing Company Profile in Variables ---
# Variables make our data meaningful. Instead of just "InnovateCorp",
# we know it's the company_name.

company_name = "InnovateCorp"
year_founded = 2015
current_revenue = 2500000.50
is_publicly_traded = False

print("--- Company Profile ---")
print(f"Company Name: {company_name}")
print(f"Year Founded: {year_founded}")
print(f"Current Revenue: ${current_revenue}")
print(f"Is Publicly Traded: {is_publicly_traded}")
print("-" * 20)

# --- Using Built-in Functions for Sales Analysis ---
# Here's a list of sales transactions for the week.
weekly_sales = [150.50, 200.00, 75.25, 300.75, 120.00, 450.50, 275.00]

print("--- Weekly Sales Analysis ---")

# len() - to find the number of sales transactions
num_transactions = len(weekly_sales)
print(f"Number of Transactions: {num_transactions}")

# sum() - to find the total revenue
total_revenue = sum(weekly_sales)
print(f"Total Weekly Revenue: ${total_revenue:.2f}")

# min() and max() - to find the smallest and largest sales
smallest_sale = min(weekly_sales)
largest_sale = max(weekly_sales)
print(f"Smallest Sale: ${smallest_sale:.2f}")
print(f"Largest Sale: ${largest_sale:.2f}")

# We can combine functions to get more insights
# round() - to present the average sale amount cleanly
average_sale = total_revenue / num_transactions
print(f"Average Sale Amount: ${round(average_sale, 2)}")
print("-" * 20)

# --- Getting User Input ---
# The input() function prompts the user for information.
# This makes scripts interactive.

print("--- Interactive Profit Calculator ---")
# We use float() to convert the user's text input into a number.
try:
    user_revenue = float(input("Enter your total revenue: "))
    user_expenses = float(input("Enter your total expenses: "))

    # Calculate the profit
    profit = user_revenue - user_expenses

    print(f"Your calculated profit is: ${profit:.2f}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
