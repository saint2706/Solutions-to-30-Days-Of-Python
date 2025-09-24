"""
Day 6: Using Tuples for Immutable Business Data

This script demonstrates the creation and use of tuples to store
data that should not be changed, such as transaction records or
fixed coordinates.
"""

# --- Using a Tuple for Fixed Data ---
# Tuples are defined with parentheses ().
# They are perfect for data that is constant, like a location.

print("--- Storing Fixed Location Data ---")
hq_location = (40.7128, -74.0060)  # (Latitude, Longitude)

# Accessing tuple data is the same as with lists.
print(f"Headquarters Latitude: {hq_location[0]}")
print(f"Headquarters Longitude: {hq_location[1]}")
print()

# Attempting to change a tuple will result in an error.
# The following line is commented out because it would crash the script.
# hq_location[0] = 41.8781  # This will raise a TypeError!


# --- Unpacking Tuples for Readability ---
# "Unpacking" is a clean way to assign tuple items to variables.
print("--- Unpacking a Transaction Record ---")
transaction = (1001, "2024-03-15", 499.99)
trans_id, date, amount = transaction

print(f"Transaction ID: {trans_id}")
print(f"Date: {date}")
print(f"Amount: ${amount}")
print("-" * 20)


# --- List vs. Tuple: Choosing the Right Tool ---
print("--- Choosing Between a List and a Tuple ---")

# Scenario A: Storing the monthly sales figures for the past year.
# Choice: List. Sales data is likely to be updated or amended.
monthly_sales = [45000, 52000, 48000, 55000]  # ... and so on
print(
    f"Scenario A (Monthly Sales): Use a list. Data might change. Example: {monthly_sales}"
)

# Scenario B: Storing the RGB color code for your company's official logo.
# Choice: Tuple. The brand color is a fixed constant and should not change.
brand_color_rgb = (45, 85, 150)
print(
    f"Scenario B (Brand Color): Use a tuple. Data is constant. Example: {brand_color_rgb}"
)

# Scenario C: Storing the names of employees in a department.
# Choice: List. Employees can be added or removed from the department.
marketing_team = ["Alice", "Bob", "Charlie"]
print(
    f"Scenario C (Team Roster): Use a list. Roster changes. Example: {marketing_team}"
)

# Scenario D: Storing the name, founding year, and stock ticker symbol for a company.
# Choice: Tuple. This core identifying information for a company is fixed.
company_profile = ("InnovateCorp", 2015, "INVC")
print(
    f"Scenario D (Company Profile): Use a tuple. Core info is fixed. Example: {company_profile}"
)
print("-" * 20)
