"""
Day 3: Operators in Action for Business Analysis (Refactored)

This script demonstrates how different Python operators can be used
to perform business calculations and logical checks. This version is
refactored into functions for better organization and testability.
"""


def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculates the final amount of an investment with compound interest.
    A = P(1 + r/n)^(nt)
    """
    # The ** operator is used for exponents
    final_amount = principal * (1 + rate / n) ** (n * time)
    return final_amount


def accumulate_sales(initial_sales, daily_sales):
    """
    Accumulates daily sales into a total.
    """
    total = initial_sales
    for sale in daily_sales:
        total += sale  # The += operator adds a value to a variable
    return total


def check_inventory_status(inventory_count, low_stock_threshold):
    """Checks if the inventory count is below the low stock threshold."""
    # The < operator checks if a value is less than another
    return inventory_count < low_stock_threshold


def check_sales_target(current_sales, sales_target):
    """Checks if the current sales have met or exceeded the sales target."""
    # The >= operator checks for "greater than or equal to"
    return current_sales >= sales_target


def check_bonus_eligibility(sales, years_of_service, top_performer_last_quarter):
    """
    Determines bonus eligibility based on complex business rules.
    The 'and' requires both conditions to be true.
    The 'or' allows either condition to be true.
    """
    is_eligible = (sales > 10000 and years_of_service > 2) or top_performer_last_quarter
    return is_eligible


if __name__ == "__main__":
    # --- Arithmetic Operators for Financial Calculations ---
    print("--- Financial Calculations ---")
    principal_amount = 10000
    interest_rate = 0.05
    investment_time = 3
    final_investment_amount = calculate_compound_interest(
        principal_amount, interest_rate, investment_time
    )
    print(
        f"Investment of ${principal_amount} after {investment_time} years at {interest_rate * 100}% interest will be: ${final_investment_amount:.2f}"
    )
    print("-" * 20)

    # --- Assignment Operators for Accumulating Data ---
    print("--- Accumulating Daily Sales ---")
    sales_over_three_days = [1500, 2200, 1850]
    total_sales_figure = accumulate_sales(0, sales_over_three_days)
    print(f"Total sales after 3 days: ${total_sales_figure}")
    print("-" * 20)

    # --- Comparison Operators for Business Rules ---
    print("--- Inventory and Sales Target Checks ---")
    is_low = check_inventory_status(inventory_count=45, low_stock_threshold=50)
    print(f"Is inventory low? {is_low}")

    target_met = check_sales_target(current_sales=265000, sales_target=250000)
    print(f"Has the sales target been met? {target_met}")
    print("-" * 20)

    # --- Logical Operators for Complex Eligibility Rules ---
    print("--- Sales Bonus Eligibility Test ---")
    # Scenario 1
    eligible_s1 = check_bonus_eligibility(
        sales=12000, years_of_service=1, top_performer_last_quarter=False
    )
    print(f"Scenario 1 (High Sales, New Employee): Eligible? {eligible_s1}")
    # Scenario 2
    eligible_s2 = check_bonus_eligibility(
        sales=8000, years_of_service=3, top_performer_last_quarter=True
    )
    print(f"Scenario 2 (Top Performer): Eligible? {eligible_s2}")
    # Scenario 3
    eligible_s3 = check_bonus_eligibility(
        sales=9000, years_of_service=1, top_performer_last_quarter=False
    )
    print(f"Scenario 3 (Not Eligible): Eligible? {eligible_s3}")
