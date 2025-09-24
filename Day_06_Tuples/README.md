# 📘 Day 6: Tuples - Storing Immutable Business Data

So far, we've worked with lists, which are excellent for collections of data that need to change. But what about data that *shouldn't* change? Think about a specific transaction record: once it's created, you wouldn't want to accidentally change the date or the amount. For this, Python gives us the **tuple**.

## What is a Tuple?

A tuple is an ordered, **immutable** collection of items. "Immutable" is a key concept: it means once a tuple is created, it cannot be changed. You can't add, remove, or modify items. This makes tuples perfect for protecting data integrity.

You create a tuple just like a list, but with parentheses `()` instead of square brackets.

```python
# A tuple to store fixed company brand colors (RGB values)
brand_colors = (45, 85, 150)

# A tuple to store a transaction record (ID, Date, Amount)
transaction = (1001, "2024-03-15", 499.99)
```

## Why Use a Tuple Instead of a List?

1. **Data Integrity:** This is the main reason. If you have data that should remain constant, using a tuple prevents accidental modification by you or someone else using your code. It's a safeguard.
2. **Performance:** Tuples are slightly more memory-efficient and faster to access than lists. For very large datasets, this can make a difference.
3. **Dictionary Keys:** As we'll see later, you can use tuples as keys in a dictionary (another data structure), but you cannot use lists. This is useful for complex data mapping.

## Working with Tuples

You can access data in a tuple using indexing and slicing, just like with lists.

```python
transaction = (1001, "2024-03-15", 499.99)
transaction_id = transaction[0]  # Accesses 1001
amount = transaction[2]         # Accesses 499.99
```

The key difference is that you **cannot** do this:
`transaction[2] = 599.99  # This will cause a TypeError!`

### Unpacking Tuples

A very common and elegant feature of tuples is "unpacking." You can assign the items of a tuple to multiple variables at once.

```python
transaction = (1001, "2024-03-15", 499.99)
trans_id, date, amount = transaction

print(f"Transaction ID: {trans_id}")
print(f"Date: {date}")
print(f"Amount: ${amount}")
```

This is much cleaner than accessing each item by its index.

## 💻 Exercises: Day 6

1. **Store Geographic Coordinates:**
    * A company's headquarters is located at latitude 40.7128 and longitude -74.0060.
    * Store these coordinates in a tuple called `hq_location`.
    * "Unpack" the tuple into `latitude` and `longitude` variables.
    * Print the latitude and longitude.

2. **Define Product Dimensions:**
    * You are defining the dimensions (length, width, height) in centimeters for a product package. These dimensions are fixed.
    * Create a tuple `package_dimensions` with the values `25`, `15`, `10`.
    * Write a print statement that uses f-string formatting and indexing to display: "Package Dimensions (LxWxH): 25cm x 15cm x 10cm".

3. **List vs. Tuple - The Right Tool for the Job:**
    * For each of the following scenarios, decide if a **list** or a **tuple** would be the more appropriate data structure. Write a comment in your Python script explaining your choice.
        * Scenario A: Storing the monthly sales figures for the past year.
        * Scenario B: Storing the RGB color code for your company's official logo.
        * Scenario C: Storing the names of employees in a department.
        * Scenario D: Storing the name, founding year, and stock ticker symbol for a company.

🎉 **Excellent!** You've now learned about immutability and how to use tuples to ensure your data remains constant and secure. Knowing when to use a tuple versus a list is a sign of a thoughtful analyst.
