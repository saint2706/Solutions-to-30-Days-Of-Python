"""
Day 9: Implementing Business Logic with Conditionals (Refactored)

This script demonstrates how to use if, elif, and else statements
to create business rules and make decisions in code. This version is
refactored into functions for better organization and testability.
"""

def calculate_discount_percent(purchase_amount):
    """Calculates a discount percentage based on the purchase amount."""
    if not isinstance(purchase_amount, (int, float)) or purchase_amount < 0:
        return 0.0

    if purchase_amount > 100.00:
        return 0.10  # 10% discount
    elif purchase_amount > 50.00:
        return 0.05  # 5% discount
    else:
        return 0.00  # 0% discount

def calculate_shipping_cost(country, order_weight_kg):
    """Calculates shipping cost based on destination and weight."""
    if country == "USA":
        if order_weight_kg > 50:
            return 75
        else:
            return 50
    elif country == "Canada":
        if order_weight_kg > 50:
            return 100
        else:
            return 65
    else:
        return -1  # Using -1 to indicate not available

def calculate_employee_bonus(performance_rating, department, salary):
    """Calculates an employee's bonus based on performance and department."""
    if performance_rating >= 4:
        if department == "Sales":
            return salary * 0.15
        else:
            return salary * 0.10
    elif performance_rating == 3:
        return salary * 0.05
    else:
        return 0.0

if __name__ == "__main__":
    # --- Example 1: Customer Discount Policy ---
    print("--- Customer Discount Calculator ---")
    customer_purchase = 125.50
    discount_rate = calculate_discount_percent(customer_purchase)
    discount = customer_purchase * discount_rate
    final = customer_purchase - discount

    print(f"Original Price: ${customer_purchase:.2f}")
    print(f"Discount ({discount_rate*100}%): ${discount:.2f}")
    print(f"Final Price: ${final:.2f}")
    print("-" * 20)

    # --- Example 2: Nested Conditionals for Shipping Costs ---
    print("--- Shipping Cost Calculator ---")
    shipping_country = "Canada"
    weight = 60
    cost = calculate_shipping_cost(shipping_country, weight)

    if cost != -1:
        print(f"Shipping to {shipping_country} for a {weight}kg package costs: ${cost}")
    else:
        print(f"Sorry, shipping to {shipping_country} is not available.")
    print("-" * 20)

    # --- Example 3: Complex Bonus Calculation ---
    print("--- Employee Bonus Calculator ---")
    emp_rating = 5
    emp_dept = "Sales"
    emp_salary = 80000
    bonus_amount = calculate_employee_bonus(emp_rating, emp_dept, emp_salary)

    print(f"Employee in {emp_dept} with rating {emp_rating} gets a bonus of: ${bonus_amount:.2f}")
    print("-" * 20)