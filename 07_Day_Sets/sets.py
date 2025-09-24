"""
Day 7: Using Sets for Unique Data and Segmentation

This script demonstrates how to use sets to de-duplicate data
and perform segmentation analysis on business data.
"""

# --- Using a Set to Find Unique Items ---
print("--- Finding Unique Customer Cities ---")
# This list contains duplicate city names.
order_cities = ["New York", "Los Angeles", "Chicago", "New York", "Boston", "Los Angeles", "Chicago"]
print(f"Original list of cities: {order_cities}")

# Converting a list to a set automatically removes all duplicates.
unique_cities = set(order_cities)
print(f"Unique cities set: {unique_cities}")
print(f"Number of unique cities: {len(unique_cities)}")
print("-" * 20)


# --- Using Set Operations for Customer Segmentation ---
print("--- Analyzing Website Visitor Segments ---")
# Imagine we have two groups of visitors: one viewed the pricing page,
# the other viewed the contact page.
pricing_visitors = {"user1", "user3", "user5", "user7", "user8"}
contact_visitors = {"user2", "user3", "user4", "user5", "user9"}

# Intersection (&): Find users who are in BOTH sets.
# These are highly engaged leads who looked at pricing AND wanted to contact us.
highly_engaged_users = pricing_visitors.intersection(contact_visitors)
print(f"Users who visited Pricing AND Contact pages: {highly_engaged_users}")

# Difference (-): Find users in the first set but NOT the second.
# These users looked at pricing but didn't try to contact us. Maybe a follow-up is needed.
pricing_only_users = pricing_visitors.difference(contact_visitors)
print(f"Users who only visited the Pricing page: {pricing_only_users}")

# Union (|): Find all unique users who are in EITHER set.
# This gives us the total unique audience for these key pages.
total_unique_visitors = pricing_visitors.union(contact_visitors)
print(f"All unique visitors to either page: {total_unique_visitors}")
print("-" * 20)


# --- Modifying Sets to Manage Product Plans ---
print("--- Managing Product Plan Features ---")
standard_features = {"reporting", "data_export", "basic_support"}
print(f"Standard Plan Features: {standard_features}")

# Start the Pro plan with all the features of the standard plan.
pro_features = standard_features.copy()

# .add() a single new feature
pro_features.add("api_access")

# .update() with multiple new features from a list
pro_features.update(["priority_support", "24/7_monitoring"])

print(f"Pro Plan Features: {pro_features}")

# We can now see what the "pro-only" features are using a difference.
pro_only_features = pro_features.difference(standard_features)
print(f"Features unique to the Pro Plan: {pro_only_features}")
print("-" * 20)
