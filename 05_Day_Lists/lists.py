"""
Day 5: Managing and Analyzing Business Data with Lists

This script demonstrates how to create, access, modify, and analyze
lists containing business-related data.
"""

# --- Initializing Lists with Business Data ---
print("--- Initializing Business Lists ---")
departments = ["Sales", "Marketing", "Human Resources", "Engineering"]
quarterly_sales = [120000.50, 135000.75, 110000.00, 145000.25]
print(f"Company Departments: {departments}")
print(f"Quarterly Sales: {quarterly_sales}")
print("-" * 20)


# --- Accessing and Slicing List Data ---
print("--- Accessing Specific Data ---")
# Accessing by index (remember, index starts at 0)
marketing_dept = departments[1]
print(f"The second department is: {marketing_dept}")

# Accessing the last item with negative indexing
last_quarter_sales = quarterly_sales[-1]
print(f"Sales for the last quarter: ${last_quarter_sales}")

# Slicing to get a range of data (e.g., first half of the year)
first_half_sales = quarterly_sales[0:2]
print(f"First half sales: {first_half_sales}")
print("-" * 20)


# --- Modifying Lists - A Common Task ---
print("--- Modifying a Product List ---")
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
print(f"Original product list: {products}")

# .append() to add a new product
products.append("Webcam")
print(f"After adding 'Webcam': {products}")

# .remove() to remove a sold-out item
products.remove("Mouse")
print(f"After removing 'Mouse': {products}")
print("-" * 20)


# --- Analyzing List Data ---
print("--- Analyzing Sales Performance ---")
team_sales = [5000, 8000, 4500, 12000, 6000, 11000]
print(f"Sales figures for the team: {team_sales}")

# .sort() to rank performance. reverse=True sorts from highest to lowest.
team_sales.sort(reverse=True)
print(f"Sales sorted from highest to lowest: {team_sales}")

# Slicing to find the top performers
top_3_performers = team_sales[0:3]
print(f"Top 3 sales figures: {top_3_performers}")

# Calculating the total sales of the top performers
total_top_sales = sum(top_3_performers)
print(f"Total sales from top 3 performers: ${total_top_sales}")
print("-" * 20)
