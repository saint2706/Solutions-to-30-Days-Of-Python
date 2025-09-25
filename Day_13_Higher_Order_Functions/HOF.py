"""
Day 13: Advanced Data Processing with Higher-Order Functions

This script demonstrates using map, filter, and lambda functions
for concise and powerful data manipulation.
"""

# --- Using map() to transform a list ---
print("--- Applying a Bonus to All Salaries ---")
salaries = [50000, 80000, 120000, 65000]
print(f"Original salaries: {salaries}")


# We can define a function to use with map
def apply_bonus(salary):
    return salary * 1.10


# But it's often quicker to use a lambda function directly in the map call
# lambda s: s * 1.10 is a short, anonymous function that does the same thing.
new_salaries = list(map(lambda s: s * 1.10, salaries))
print(f"Salaries after 10% bonus: {new_salaries}")
print("-" * 20)


# --- Using filter() to select data ---
print("--- Filtering for High-Yield Projects ---")
# A list of tuples, where each tuple is (project_name, roi_percentage)
projects = [("Project A", 12), ("Project B", 20), ("Project C", 8), ("Project D", 25)]
print(f"All projects: {projects}")

# We want to find projects where the ROI (the second item, index 1) is > 15%
# lambda p: p[1] > 15 is a function that returns True or False for each project
high_yield_projects = list(filter(lambda p: p[1] > 15, projects))
print(f"High-yield projects (ROI > 15%): {high_yield_projects}")
print("-" * 20)


# --- Combining map() and filter() ---
print("--- Analyzing High-Value Customer Data ---")
customers = [
    {"name": "InnovateCorp", "subscription_status": "active", "monthly_spend": 550},
    {
        "name": "DataDriven Inc.",
        "subscription_status": "inactive",
        "monthly_spend": 120,
    },
    {"name": "Analytics LLC", "subscription_status": "active", "monthly_spend": 210},
]

# Goal: Get the names of all 'active' customers.

# Step 1: Filter the list to get only active customers.
active_customers = list(
    filter(lambda c: c["subscription_status"] == "active", customers)
)

# Step 2: Map the filtered list to get just the names.
active_customer_names = list(map(lambda c: c["name"], active_customers))

print(f"Original customer data: {customers}")
print(f"Filtered active customers: {active_customers}")
print(f"Names of active customers: {active_customer_names}")
print("-" * 20)


# --- Using sorted() with a lambda key ---
print("--- Sorting Products by Price ---")
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300},
]
print(f"Original product list: {products}")

# sorted() is a higher-order function. The 'key' argument takes a function.
# We provide a lambda function that tells sorted() to look at the 'price'
# of each dictionary when it's comparing them.
products_sorted_by_price = sorted(products, key=lambda p: p["price"])
print(f"Products sorted by price: {products_sorted_by_price}")
print("-" * 20)
