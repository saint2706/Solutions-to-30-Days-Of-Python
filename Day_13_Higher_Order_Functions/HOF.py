"""
Day 13: Advanced Data Processing with Higher-Order Functions (Refactored)

This script demonstrates using map, filter, and sorted with lambda functions
for concise and powerful data manipulation. This version is refactored
into functions for better organization and testability.
"""


def apply_bonus_to_salaries(salaries, bonus_percentage):
    """
    Applies a percentage bonus to a list of salaries using map().
    """
    bonus_multiplier = 1 + bonus_percentage
    return list(map(lambda s: s * bonus_multiplier, salaries))


def filter_high_yield_projects(projects, roi_threshold):
    """
    Filters a list of projects to find those with an ROI above a threshold.
    Assumes projects is a list of tuples: (project_name, roi_percentage).
    """
    return list(filter(lambda p: p[1] > roi_threshold, projects))


def get_active_customer_names(customers):
    """
    Filters a list of customer dictionaries for active customers and returns their names.
    """
    active_customers = filter(
        lambda c: c.get("subscription_status") == "active", customers
    )
    return list(map(lambda c: c.get("name"), active_customers))


def sort_products_by_attribute(products, attribute_name):
    """
    Sorts a list of product dictionaries by a specified attribute (e.g., 'price').
    """
    return sorted(products, key=lambda p: p.get(attribute_name, 0))


def main():
    """Main function to demonstrate higher-order functions."""
    # --- Using map() to transform a list ---
    print("--- Applying a Bonus to All Salaries ---")
    salaries_list = [50000, 80000, 120000, 65000]
    print(f"Original salaries: {salaries_list}")

    new_salaries_list = apply_bonus_to_salaries(salaries_list, 0.10)  # 10% bonus
    print(f"Salaries after 10% bonus: {new_salaries_list}")
    print("-" * 20)

    # --- Using filter() to select data ---
    print("--- Filtering for High-Yield Projects ---")
    projects_list = [
        ("Project A", 12),
        ("Project B", 20),
        ("Project C", 8),
        ("Project D", 25),
    ]
    print(f"All projects: {projects_list}")

    high_yield_list = filter_high_yield_projects(projects_list, 15)
    print(f"High-yield projects (ROI > 15%): {high_yield_list}")
    print("-" * 20)

    # --- Combining map() and filter() ---
    print("--- Analyzing High-Value Customer Data ---")
    customers_list = [
        {"name": "InnovateCorp", "subscription_status": "active", "monthly_spend": 550},
        {
            "name": "DataDriven Inc.",
            "subscription_status": "inactive",
            "monthly_spend": 120,
        },
        {
            "name": "Analytics LLC",
            "subscription_status": "active",
            "monthly_spend": 210,
        },
    ]
    print(f"Original customer data: {customers_list}")

    active_names = get_active_customer_names(customers_list)
    print(f"Names of active customers: {active_names}")
    print("-" * 20)

    # --- Using sorted() with a lambda key ---
    print("--- Sorting Products by Price ---")
    products_list = [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 75},
        {"name": "Monitor", "price": 300},
    ]
    print(f"Original product list: {products_list}")

    sorted_products = sort_products_by_attribute(products_list, "price")
    print(f"Products sorted by price: {sorted_products}")
    print("-" * 20)


if __name__ == "__main__":
    main()
