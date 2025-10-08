"""
Day 1: Python for Business Analytics - First Steps (Refactored)

This script demonstrates basic Python concepts using business-relevant examples.
We will perform a simple profit calculation and check the types of various
business-related data points. This version is refactored to use functions.
"""


def calculate_gross_profit(revenue, cogs):
    """Calculates the gross profit from revenue and COGS."""
    return revenue - cogs


def calculate_gross_profit_margin(gross_profit, revenue):
    """Calculates the gross profit margin."""
    if revenue == 0:
        return 0
    return (gross_profit / revenue) * 100


def display_business_analytics(revenue, cogs):
    """Calculates and displays key business metrics."""
    print("Welcome to the Quarterly Business Review Dashboard")
    print()

    gross_profit = calculate_gross_profit(revenue, cogs)
    gross_profit_margin = calculate_gross_profit_margin(gross_profit, revenue)

    print(f"Total Revenue: ${revenue}")
    print(f"Cost of Goods Sold: ${cogs}")
    print(f"Gross Profit: ${gross_profit}")
    print()
    print(f"Gross Profit Margin: {gross_profit_margin:.2f}%")
    print("-" * 20)


def display_data_types():
    """Displays the types of various business-related data points."""
    print("Checking the types of some common business data points:")

    units_sold = 1500
    product_price = 49.99
    company_name = "InnovateCorp"
    is_in_stock = True
    quarterly_sales = [110000, 120000, 135000, 140000]

    print(f"Data: {units_sold}, Type: {type(units_sold)}")
    print(f"Data: {product_price}, Type: {type(product_price)}")
    print(f"Data: '{company_name}', Type: {type(company_name)}")
    print(f"Data: {is_in_stock}, Type: {type(is_in_stock)}")
    print(f"Data: {quarterly_sales}, Type: {type(quarterly_sales)}")


if __name__ == "__main__":
    # --- Basic Business Calculations ---
    revenue_main = 500000
    cogs_main = 350000
    display_business_analytics(revenue_main, cogs_main)

    # --- Understanding Data Types in a Business Context ---
    display_data_types()
