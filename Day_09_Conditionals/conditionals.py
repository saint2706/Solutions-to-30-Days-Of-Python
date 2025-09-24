"""
Day 9: Implementing Business Logic with Conditionals

This script demonstrates how to use if, elif, and else statements
to create business rules and make decisions in code.
"""

# --- Example 1: Customer Discount Policy ---
print("--- Customer Discount Calculator ---")
purchase_amount = 125.50

if purchase_amount > 100.00:
    discount_percent = 0.10  # 10% discount
elif purchase_amount > 50.00:
    discount_percent = 0.05  # 5% discount
else:
    discount_percent = 0.00  # 0% discount

discount_amount = purchase_amount * discount_percent
final_price = purchase_amount - discount_amount

print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount ({discount_percent*100}%): ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")
print("-" * 20)


# --- Example 2: Nested Conditionals for Shipping Costs ---
print("--- Shipping Cost Calculator ---")
country = "Canada"
order_weight_kg = 60

if country == "USA":
    if order_weight_kg > 50:
        shipping_cost = 75
    else:
        shipping_cost = 50
elif country == "Canada":
    if order_weight_kg > 50:
        shipping_cost = 100
    else:
        shipping_cost = 65
else:
    shipping_cost = -1 # Using -1 to indicate not available

if shipping_cost != -1:
    print(f"Shipping to {country} for a {order_weight_kg}kg package costs: ${shipping_cost}")
else:
    print(f"Sorry, shipping to {country} is not available.")
print("-" * 20)


# --- Example 3: Complex Bonus Calculation ---
print("--- Employee Bonus Calculator ---")
performance_rating = 5  # Scale of 1-5
department = "Sales"
salary = 80000
bonus = 0 # Default bonus is 0

if performance_rating >= 4:
    print("Performance: Excellent")
    if department == "Sales":
        bonus = salary * 0.15
    else:
        bonus = salary * 0.10
elif performance_rating == 3:
    print("Performance: Met Expectations")
    bonus = salary * 0.05
else:
    print("Performance: Needs Improvement")
    bonus = 0

print(f"Employee in {department} with rating {performance_rating} gets a bonus of: ${bonus:.2f}")
print("-" * 20)
