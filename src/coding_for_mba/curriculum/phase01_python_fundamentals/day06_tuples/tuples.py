"""
Day 6: Using Tuples for Immutable Business Data (Refactored)

This script demonstrates the creation and use of tuples to store
data that should not be changed, such as transaction records or
fixed coordinates. This version is refactored into functions for
better organization and testability.
"""


def get_location_coordinates(location_tuple):
    """
    Returns the latitude and longitude from a location tuple.
    Assumes the tuple is in the format (latitude, longitude).
    """
    if isinstance(location_tuple, tuple) and len(location_tuple) == 2:
        return location_tuple[0], location_tuple[1]
    return None, None


def unpack_transaction(transaction_tuple):
    """
    Unpacks a transaction tuple into a dictionary.
    Assumes tuple format is (id, date, amount).
    """
    if isinstance(transaction_tuple, tuple) and len(transaction_tuple) == 3:
        trans_id, date, amount = transaction_tuple
        return {"id": trans_id, "date": date, "amount": amount}
    return None


def demonstrate_list_vs_tuple():
    """
    Prints scenarios demonstrating when to use a list vs. a tuple.
    """
    print("--- Choosing Between a List and a Tuple ---")

    # Scenario A: Storing the monthly sales figures for the past year.
    # Choice: List. Sales data is likely to be updated or amended.
    monthly_sales = [45000, 52000, 48000, 55000]
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


if __name__ == "__main__":
    # --- Using a Tuple for Fixed Data ---
    print("--- Storing Fixed Location Data ---")
    hq_coords = (40.7128, -74.0060)
    lat, lon = get_location_coordinates(hq_coords)
    if lat is not None:
        print(f"Headquarters Latitude: {lat}")
        print(f"Headquarters Longitude: {lon}")
    print()

    # --- Unpacking Tuples for Readability ---
    print("--- Unpacking a Transaction Record ---")
    transaction_data = (1001, "2024-03-15", 499.99)
    unpacked_data = unpack_transaction(transaction_data)
    if unpacked_data:
        print(f"Transaction ID: {unpacked_data['id']}")
        print(f"Date: {unpacked_data['date']}")
        print(f"Amount: ${unpacked_data['amount']}")
    print("-" * 20)

    # --- List vs. Tuple Demonstration ---
    demonstrate_list_vs_tuple()
