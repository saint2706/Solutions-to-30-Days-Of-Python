# 📘 Day 7: Sets - Managing Unique Business Data

We've seen lists for ordered data and tuples for immutable data. Now we'll learn about **sets**, which are powerful for two main business reasons: ensuring uniqueness and performing membership analysis.

## What is a Set?

A set is an **unordered** collection of **unique** items.

*   **Unordered:** The items in a set do not have a defined order. You cannot access them using an index like `my_set[0]`.
*   **Unique:** A set cannot contain duplicate items. If you try to add an item that's already in the set, nothing happens.

You create a set using curly braces `{}` or the `set()` function on a list.

```python
# A list with duplicate sales regions
sales_regions_list = ["North", "South", "North", "West", "East", "South"]

# Creating a set automatically removes duplicates
unique_sales_regions = set(sales_regions_list)
# The set will be: {"North", "South", "West", "East"} (order is not guaranteed)
```
This de-duplication feature is one of the most common uses for sets in data analysis.

## Set Operations: The Foundation of Segmentation

The true power of sets in business analytics comes from their mathematical operations. These are invaluable for customer segmentation, cohort analysis, and more.

Imagine we have two sets of customers: those who bought Product A and those who bought Product B.

```python
customers_A = {"John", "Mary", "Peter", "Jane"}
customers_B = {"Peter", "Jane", "Chris", "Anna"}
```

| Operation      | Python Operator | Python Method        | Result                                        | Business Question Answered                               |
| :------------- | :-------------- | :------------------- | :-------------------------------------------- | :------------------------------------------------------- |
| **Union**      | `A | B`         | `A.union(B)`         | `{"John", "Mary", "Peter", "Jane", "Chris", "Anna"}` | Who are all the customers who bought *either* Product A *or* Product B? |
| **Intersection** | `A & B`         | `A.intersection(B)`  | `{"Peter", "Jane"}`                           | Which customers bought *both* Product A *and* Product B? |
| **Difference**   | `A - B`         | `A.difference(B)`    | `{"John", "Mary"}`                            | Which customers bought Product A *but not* Product B?    |
| **Symmetric Difference** | `A ^ B` | `A.symmetric_difference(B)` | `{"John", "Mary", "Chris", "Anna"}` | Which customers bought Product A *or* Product B, but *not both*? |

## Modifying Sets

While sets are used for analysis, you can also modify them.

*   `.add(item)`: Adds a single item to the set.
*   `.update(other_set)`: Adds all items from another set into the current set.
*   `.remove(item)`: Removes a specified item. Will raise an error if the item is not found.
*   `.discard(item)`: Also removes an item, but will *not* raise an error if the item isn't there. This is often safer.

## 💻 Exercises: Day 7

1.  **Find Unique Customer Cities:**
    *   You have a list of cities from where orders were placed, with many duplicates: `order_cities = ["New York", "Los Angeles", "Chicago", "New York", "Boston", "Los Angeles"]`.
    *   Convert this list into a set to find the unique cities.
    *   Print the set of unique cities and the number of unique cities.

2.  **Analyze Website Visitor Activity:**
    *   You have two sets of user IDs. One set for users who visited the "Pricing" page, and another for users who visited the "Contact Us" page.
    *   `pricing_visitors = {"user1", "user3", "user5", "user7"}`
    *   `contact_visitors = {"user2", "user3", "user4", "user5"}`
    *   Find and print the following:
        *   The users who visited *both* the pricing and contact pages (intersection).
        *   The users who visited the pricing page but *not* the contact page (difference).
        *   A complete set of all unique users who visited *either* page (union).

3.  **Manage Product Features:**
    *   Your "Standard Plan" has a set of features: `standard_features = {"reporting", "data_export", "basic_support"}`.
    *   Your "Pro Plan" has all the standard features plus some new ones.
    *   Start by creating a copy of the standard features for the "Pro Plan": `pro_features = standard_features.copy()`.
    *   Now, `.update()` the `pro_features` set with a list of new features: `["api_access", "priority_support"]`.
    *   Print both the standard and pro feature sets.

🎉 **Well done!** Sets are a specialized but incredibly efficient tool. When you need to de-duplicate a list or analyze the overlap between two groups, sets are the best tool for the job.
