"""
Day 2: Storing and Analyzing Business Data (Refactored)

This script demonstrates the use of variables to store business data
and built-in functions to perform basic analysis. This version is
refactored into functions for better organization and testability.
"""


def display_company_profile(name, founded, revenue, is_public):
    """Displays the company's profile information."""
    print("--- Company Profile ---")
    print(f"Company Name: {name}")
    print(f"Year Founded: {founded}")
    print(f"Current Revenue: ${revenue}")
    print(f"Is Publicly Traded: {is_public}")
    print("-" * 20)


def analyze_weekly_sales(sales_data):
    """Analyzes and prints a summary of weekly sales data."""
    if not sales_data:
        print("No sales data to analyze.")
        return

    print("--- Weekly Sales Analysis ---")
    num_transactions = len(sales_data)
    total_revenue = sum(sales_data)
    smallest_sale = min(sales_data)
    largest_sale = max(sales_data)
    average_sale = total_revenue / num_transactions if num_transactions > 0 else 0

    print(f"Number of Transactions: {num_transactions}")
    print(f"Total Weekly Revenue: ${total_revenue:.2f}")
    print(f"Smallest Sale: ${smallest_sale:.2f}")
    print(f"Largest Sale: ${largest_sale:.2f}")
    print(f"Average Sale Amount: ${round(average_sale, 2)}")
    print("-" * 20)

    return {
        "num_transactions": num_transactions,
        "total_revenue": total_revenue,
        "smallest_sale": smallest_sale,
        "largest_sale": largest_sale,
        "average_sale": average_sale,
    }


def interactive_profit_calculator():
    """Handles user input to calculate and display profit."""
    print("--- Interactive Profit Calculator ---")
    try:
        user_revenue = float(input("Enter your total revenue: "))
        user_expenses = float(input("Enter your total expenses: "))
        profit = user_revenue - user_expenses
        print(f"Your calculated profit is: ${profit:.2f}")
        return profit
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None


if __name__ == "__main__":
    # --- Storing Company Profile in Variables ---
    display_company_profile("InnovateCorp", 2015, 2500000.50, False)

    # --- Using Built-in Functions for Sales Analysis ---
    weekly_sales_data = [150.50, 200.00, 75.25, 300.75, 120.00, 450.50, 275.00]
    analyze_weekly_sales(weekly_sales_data)

    # --- Getting User Input ---
    # Note: This part is not easily testable in an automated way without mocking input.
    # The function is separated to keep the core logic testable.
    # interactive_profit_calculator() # Uncomment to run the interactive part
