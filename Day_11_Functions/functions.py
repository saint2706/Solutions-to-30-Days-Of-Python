"""
Day 11: Building Reusable Business Tools with Functions

This script demonstrates how to define and call functions
to perform repeatable business calculations.
"""

# Adding type hints (e.g., revenue: float) makes the function's expected inputs clear.
# The "-> float" indicates that the function is expected to return a float value.


def get_net_profit(revenue: float, expenses: float) -> float:
    """Calculates the net profit from revenue and expenses."""
    net_profit = revenue - expenses
    return net_profit


def calculate_commission(sales_amount: float) -> float:
    """Calculates a 15% commission on a given sales amount."""
    commission_rate = 0.15
    commission = sales_amount * commission_rate
    return commission


def is_eligible_for_bonus(performance_rating: int, years_of_service: int) -> bool:
    """
    Checks if an employee is eligible for a bonus based on performance
    and years of service.
    """
    # Returns True if rating is 4 or 5 AND service is more than 2 years.
    return performance_rating >= 4 and years_of_service > 2


def format_currency(amount: float) -> str:
    """Formats a number into a currency string (e.g., $1,234.56)."""
    return f"${amount:,.2f}"


# --- Using the Functions ---
print("--- Calculating Company-Wide Profits ---")
# Let's use our functions to analyze two different products.
product_a_revenue = 500000
product_a_expenses = 400000
product_a_profit = get_net_profit(product_a_revenue, product_a_expenses)
print(f"Product A Profit: {format_currency(product_a_profit)}")

product_b_revenue = 250000
product_b_expenses = 210000
product_b_profit = get_net_profit(product_b_revenue, product_b_expenses)
print(f"Product B Profit: {format_currency(product_b_profit)}")

total_profit = product_a_profit + product_b_profit
print(f"Total Company Profit: {format_currency(total_profit)}")
print("-" * 20)


print("--- Sales and Bonus Calculations ---")
sales_figure = 12000
commission_earned = calculate_commission(sales_figure)
print(
    f"A sale of {format_currency(sales_figure)} earns a commission of {format_currency(commission_earned)}."
)
print()

# Test the bonus eligibility function with different scenarios
employee1_rating = 5
employee1_service = 3
eligibility1 = is_eligible_for_bonus(employee1_rating, employee1_service)
print(
    f"Employee 1 (Rating: {employee1_rating}, Service: {employee1_service} yrs) is eligible for bonus: {eligibility1}"
)

employee2_rating = 4
employee2_service = 1
eligibility2 = is_eligible_for_bonus(employee2_rating, employee2_service)
print(
    f"Employee 2 (Rating: {employee2_rating}, Service: {employee2_service} yr) is eligible for bonus: {eligibility2}"
)
print("-" * 20)
