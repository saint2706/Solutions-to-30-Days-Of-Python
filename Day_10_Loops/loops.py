"""
Day 10: Automating Tasks with Loops

This script demonstrates how to use for and while loops to
process collections of business data automatically.
"""

# --- Using a for loop to aggregate data ---
print("--- Calculating Total Monthly Revenue ---")
monthly_sales = [2340.50, 3100.25, 2900.00, 4500.75]
total_revenue = 0

# The 'for' loop iterates through each 'sale' in the 'monthly_sales' list.
for sale in monthly_sales:
    total_revenue += sale

print(f"Total Revenue for the month: ${total_revenue:.2f}")
print("-" * 20)


# --- Using a for loop with a conditional to filter data ---
print("--- Filtering High-Value Customers ---")
customers = [
    {"name": "InnovateCorp", "total_spent": 5500},
    {"name": "DataDriven Inc.", "total_spent": 1200},
    {"name": "Analytics LLC", "total_spent": 2100},
    {"name": "Global Solutions", "total_spent": 850},
]
high_priority_customers = []

# We loop through each customer dictionary in the list.
for customer in customers:
    # Check if the value for the "total_spent" key meets our condition.
    if customer["total_spent"] > 2000:
        # If it does, add the customer's name to our new list.
        high_priority_customers.append(customer["name"])

print(f"High-priority customers to contact: {high_priority_customers}")
print("-" * 20)


# --- Looping through a dictionary for inventory alerts ---
print("--- Inventory Stock Level Alerts ---")
inventory = {"Laptops": 15, "Mice": 150, "Keyboards": 45, "Monitors": 25}
low_stock_threshold = 50

# .items() lets us get both the key (product) and value (count) in each loop.
for product, count in inventory.items():
    if count < low_stock_threshold:
        print(f"ALERT: {product} are low on stock ({count} units remaining).")
print("-" * 20)


# --- Using a while loop for financial simulation ---
print("--- Investment Growth Simulation ---")
investment = 10000
target = 20000
interest_rate = 0.07
years = 0

# The 'while' loop continues as long as the condition is true.
while investment < target:
    investment *= 1 + interest_rate  # Apply 7% annual interest
    years += 1  # Increment the year count

print(
    f"It will take {years} years for the initial investment of $10,000 to double at a {interest_rate*100}% interest rate."
)
print("-" * 20)
