"""
Day 7: Using Sets for Unique Data and Segmentation (Refactored)

This script demonstrates how to use sets to de-duplicate data
and perform segmentation analysis on business data. This version
is refactored into functions for better organization and testability.
"""


def get_unique_items(items_list):
    """Converts a list to a set to get unique items."""
    return set(items_list)


def analyze_visitor_segments(set_a, set_b):
    """
    Performs intersection, difference, and union operations on two sets.
    Returns a dictionary with the results.
    """
    intersection = set_a.intersection(set_b)
    difference = set_a.difference(set_b)
    union = set_a.union(set_b)

    return {"intersection": intersection, "difference_a_b": difference, "union": union}


def upgrade_plan_features(base_features, new_features_list):
    """
    Adds new features to a base set of features.
    """
    upgraded_plan = base_features.copy()
    upgraded_plan.update(new_features_list)
    return upgraded_plan


if __name__ == "__main__":
    # --- Using a Set to Find Unique Items ---
    print("--- Finding Unique Customer Cities ---")
    order_cities_list = [
        "New York",
        "Los Angeles",
        "Chicago",
        "New York",
        "Boston",
        "Los Angeles",
        "Chicago",
    ]
    print(f"Original list of cities: {order_cities_list}")
    unique_cities_set = get_unique_items(order_cities_list)
    print(f"Unique cities set: {unique_cities_set}")
    print(f"Number of unique cities: {len(unique_cities_set)}")
    print("-" * 20)

    # --- Using Set Operations for Customer Segmentation ---
    print("--- Analyzing Website Visitor Segments ---")
    pricing_page_visitors = {"user1", "user3", "user5", "user7", "user8"}
    contact_page_visitors = {"user2", "user3", "user4", "user5", "user9"}

    segment_analysis = analyze_visitor_segments(
        pricing_page_visitors, contact_page_visitors
    )

    print(
        f"Users who visited Pricing AND Contact pages: {segment_analysis['intersection']}"
    )
    print(
        f"Users who only visited the Pricing page: {segment_analysis['difference_a_b']}"
    )
    print(f"All unique visitors to either page: {segment_analysis['union']}")
    print("-" * 20)

    # --- Modifying Sets to Manage Product Plans ---
    print("--- Managing Product Plan Features ---")
    standard_plan_features = {"reporting", "data_export", "basic_support"}
    print(f"Standard Plan Features: {standard_plan_features}")

    features_to_add_for_pro = ["api_access", "priority_support", "24/7_monitoring"]
    pro_plan_features = upgrade_plan_features(
        standard_plan_features, features_to_add_for_pro
    )

    print(f"Pro Plan Features: {pro_plan_features}")

    pro_only = pro_plan_features.difference(standard_plan_features)
    print(f"Features unique to the Pro Plan: {pro_only}")
    print("-" * 20)
