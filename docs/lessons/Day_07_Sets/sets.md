# 📘 Day 7: Sets - Managing Unique Business Data

We've seen lists for ordered data and tuples for immutable data. Now we'll learn about **sets**, which are powerful for two main business reasons: ensuring uniqueness and performing membership analysis.

## What is a Set?

A set is an **unordered** collection of **unique** items.

- **Unordered:** Items have no defined order.
- **Unique:** A set cannot contain duplicate items.

This de-duplication feature is one of the most common uses for sets in data analysis.

## Set Operations: The Foundation of Segmentation

The true power of sets comes from their mathematical operations, which are invaluable for customer segmentation and cohort analysis.

| Operation | Python Operator | Business Question Answered |
| :------------- | :-------------- | :------------------------------------------------------- |
| **Union** | `A | B` | What is the total unique audience for two groups? |
| **Intersection** | `A & B` | Which customers are in *both* Group A *and* Group B? |
| **Difference** | `A - B` | Which customers are in Group A *but not* in Group B? |

## Environment Setup

Before you begin, ensure you have followed the setup instructions in the main [README.md](../../README.md) to set up your virtual environment and install the required libraries.

## Exploring the Refactored Code

The script for this lesson, `sets.py`, has been refactored into functions to make the logic for de-duplication and segmentation reusable and testable.

1. **Review the Code:** Open `Day_07_Sets/sets.py`. Notice the functions `get_unique_items()`, `analyze_visitor_segments()`, and `upgrade_plan_features()`.
1. **Run the Script:** From the root directory of the project (`Coding-For-MBA`), run the script to see the functions in action:
   ```bash
   python Day_07_Sets/sets.py
   ```
1. **Run the Tests:** You can run the tests for this lesson to verify the correctness of each function:
   ```bash
   pytest tests/test_day_07.py
   ```

## 💻 Exercises: Day 7

1. **Find Unique Customer Cities:**

   - In a new script (`my_solutions_07.py`), you have a list of cities: `order_cities = ["New York", "Los Angeles", "Chicago", "New York", "Boston", "Los Angeles"]`.
   - Import the `get_unique_items` function from the lesson script.
   - Call the function with your list to get a set of unique cities and print the result.

1. **Analyze Website Visitor Activity:**

   - You have two sets of user IDs:
     - `pricing_visitors = {"user1", "user3", "user5", "user7"}`
     - `contact_visitors = {"user2", "user3", "user4", "user5"}`
   - Import the `analyze_visitor_segments` function.
   - Call the function with these two sets.
   - Print the `intersection` and `difference_a_b` from the returned dictionary to find highly engaged users and users who only viewed pricing.

1. **Manage Product Features:**

   - Your "Standard Plan" has a set of features: `standard_features = {"reporting", "data_export", "basic_support"}`.
   - You want to add `["api_access", "priority_support"]` for the "Pro Plan".
   - Import and use the `upgrade_plan_features` function to create the new feature set for the Pro Plan.
   - Print the resulting Pro Plan feature set.

🎉 **Well done!** Sets are a specialized but incredibly efficient tool. When you need to de-duplicate a list or analyze the overlap between two groups, sets are the best tool for the job.

Day 7: Using Sets for Unique Data and Segmentation (Refactored)

This script demonstrates how to use sets to de-duplicate data
and perform segmentation analysis on business data. This version
is refactored into functions for better organization and testability.

```python


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

```
