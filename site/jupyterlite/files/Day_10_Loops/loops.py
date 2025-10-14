"""
Day 10: Automating Tasks with Loops (Refactored)

This script demonstrates how to use for and while loops to
process collections of business data automatically. This version
is refactored into functions for better organization and testability.
"""


def calculate_total_from_list(numbers_list):
    """Calculates the sum of all numbers in a list using a for loop."""
    total = 0
    for number in numbers_list:
        total += number
    return total


def filter_high_value_customers(customers_list, threshold=2000):
    """
    Filters a list of customer dictionaries to find those who spent above a threshold.
    Returns a list of their names.
    """
    high_priority = []
    for customer in customers_list:
        if customer.get("total_spent", 0) > threshold:
            high_priority.append(customer.get("name"))
    return high_priority


def check_inventory_levels(inventory_dict, threshold=50):
    """
    Checks an inventory dictionary and returns a list of products
    that are below a specified stock threshold.
    """
    low_stock_alerts = []
    for product, count in inventory_dict.items():
        if count < threshold:
            low_stock_alerts.append(product)
    return low_stock_alerts


def simulate_investment_growth(initial_investment, target_amount, interest_rate):
    """
    Simulates the number of years it takes for an investment to reach a target.
    Returns the number of years.
    """
    if initial_investment <= 0 or interest_rate <= 0:
        return -1  # Indicate invalid input

    investment = initial_investment
    years = 0
    while investment < target_amount:
        investment *= 1 + interest_rate
        years += 1
    return years


if __name__ == "__main__":
    # --- Using a for loop to aggregate data ---
    print("--- Calculating Total Monthly Revenue ---")
    sales_data = [2340.50, 3100.25, 2900.00, 4500.75]
    total_rev = calculate_total_from_list(sales_data)
    print(f"Total Revenue for the month: ${total_rev:.2f}")
    print("-" * 20)

    # --- Using a for loop with a conditional to filter data ---
    print("--- Filtering High-Value Customers ---")
    customer_data = [
        {"name": "InnovateCorp", "total_spent": 5500},
        {"name": "DataDriven Inc.", "total_spent": 1200},
        {"name": "Analytics LLC", "total_spent": 2100},
        {"name": "Global Solutions", "total_spent": 850},
    ]
    priority_customers = filter_high_value_customers(customer_data)
    print(f"High-priority customers to contact: {priority_customers}")
    print("-" * 20)

    # --- Looping through a dictionary for inventory alerts ---
    print("--- Inventory Stock Level Alerts ---")
    inventory_levels = {"Laptops": 15, "Mice": 150, "Keyboards": 45, "Monitors": 25}
    low_stock_items = check_inventory_levels(inventory_levels)
    for item in low_stock_items:
        print(
            f"ALERT: {item} are low on stock ({inventory_levels[item]} units remaining)."
        )
    print("-" * 20)

    # --- Using a while loop for financial simulation ---
    print("--- Investment Growth Simulation ---")
    initial = 10000
    target_val = 20000
    rate = 0.07
    years_to_double = simulate_investment_growth(initial, target_val, rate)
    print(
        f"It will take {years_to_double} years for the initial investment of ${initial} to double at a {rate * 100}% interest rate."
    )
    print("-" * 20)
