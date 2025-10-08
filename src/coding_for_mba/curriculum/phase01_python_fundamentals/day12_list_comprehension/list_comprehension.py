"""
Day 12: Elegant Data Manipulation with List Comprehensions (Refactored)

This script demonstrates how to use list comprehensions to
efficiently transform and filter lists of business data. This version
is refactored into functions for better organization and testability.
"""


def apply_price_increase(prices, increase_percentage):
    """
    Applies a percentage price increase to a list of prices
    using a list comprehension.
    """
    increase_multiplier = 1 + increase_percentage
    # [expression for item in iterable]
    return [price * increase_multiplier for price in prices]


def filter_large_sales(sales, threshold):
    """
    Filters a list of sales to find those above a given threshold
    using a list comprehension.
    """
    # [expression for item in iterable if condition]
    return [sale for sale in sales if sale > threshold]


def get_top_sales_performers(employees, sales_target):
    """
    Filters and transforms a list of employee dictionaries to get the
    names of top-performing sales staff.
    """
    # [expression for item in iterable if condition]
    return [
        employee["name"]
        for employee in employees
        if employee.get("department") == "Sales"
        and employee.get("quarterly_sales", 0) > sales_target
    ]


def main():
    """Main function to demonstrate list comprehensions."""
    # --- Example 1: Transforming Data ---
    print("--- Applying a Price Increase ---")
    original_prices = [100.00, 150.50, 200.00, 80.25]
    print(f"Original prices: {original_prices}")

    increased_prices = apply_price_increase(original_prices, 0.10)  # 10% increase
    print(f"New prices (from comprehension): {[f'${p:.2f}' for p in increased_prices]}")
    print("-" * 20)

    # --- Example 2: Filtering Data ---
    print("--- Filtering for Large Sales Transactions ---")
    sales_data = [500, 1200, 800, 1500, 300, 2500]
    print(f"All sales: {sales_data}")

    large_sales_data = filter_large_sales(sales_data, 1000)
    print(f"Large sales (from comprehension): {large_sales_data}")
    print("-" * 20)

    # --- Example 3: Filtering and Transforming ---
    print("--- Extracting Names of High-Performing Sales Staff ---")
    employee_data = [
        {"name": "Alice", "department": "Sales", "quarterly_sales": 12000},
        {"name": "Bob", "department": "Engineering", "quarterly_sales": 0},
        {"name": "Charlie", "department": "Sales", "quarterly_sales": 8000},
        {"name": "David", "department": "Sales", "quarterly_sales": 15000},
    ]
    target = 10000
    top_performers_list = get_top_sales_performers(employee_data, target)
    print(f"Top performing sales staff (sales > ${target}): {top_performers_list}")
    print("-" * 20)


if __name__ == "__main__":
    main()
