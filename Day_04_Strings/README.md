# 📘 Day 4: Working with Text Data - Strings

In business analytics, not all data is numeric. Text data—like customer names, product reviews, addresses, and report narratives—is everywhere. In Python, we handle text using **strings**.

## What is a String?

A string is simply a sequence of characters enclosed in quotes. You can use single (`'`) or double (`"`) quotes.

```python
company_name = "InnovateCorp Inc."
report_status = 'Pending'
```

## String Concatenation

You can combine strings using the `+` operator. This is called concatenation.

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Results in "John Doe"
```

## F-Strings: The Modern Way to Format Strings

Concatenation is clumsy for complex strings. A much better way is to use **f-strings** (formatted string literals), which we've already seen. They let you embed expressions directly inside a string by prefixing it with an `f` and putting variables in curly braces `{}`.

```python
revenue = 500000
cogs = 350000
report_summary = f"Company: {company_name}, Revenue: ${revenue}, COGS: ${cogs}"
```

This is the standard and most readable way to build strings from variables.

## String Methods: Your Text-Editing Toolkit

Strings come with many built-in **methods**, which are functions attached to the string that let you manipulate it. Here are some of the most useful ones for data cleaning and preparation:

| Method         | Description                                        | Example                                    | Business Use Case                     |
| :------------- | :------------------------------------------------- | :----------------------------------------- | :------------------------------------ |
| `.lower()`     | Converts the entire string to lowercase.           | `"InnovateCorp".lower()` -> `"innovatecorp"` | Standardizing company names or categories. |
| `.upper()`     | Converts the entire string to uppercase.           | `"Urgent".upper()` -> `"URGENT"`             | Emphasizing a status or header.       |
| `.strip()`     | Removes whitespace from the beginning and end.     | `"  John Doe  ".strip()` -> `"John Doe"`     | Cleaning up user-entered data.        |
| `.replace()`   | Replaces a substring with another.                 | `"2023-Jan-15".replace("-", "/")` -> `"2023/Jan/15"` | Correcting or reformatting data.      |
| `.split()`     | Splits the string into a list of substrings.       | `"John,Doe,CEO".split(",")` -> `['John', 'Doe', 'CEO']` | Parsing comma-separated data.         |
| `.startswith()`| Checks if the string starts with a substring.      | `"INV-001".startswith("INV-")` -> `True`   | Identifying invoice numbers.          |
| `.endswith()`  | Checks if the string ends with a substring.        | `"report.pdf".endswith(".pdf")` -> `True`    | Checking file types.                  |
| `.find()`      | Finds the first occurrence of a substring.         | `"John Doe".find("Doe")` -> `5`              | Locating a piece of information.      |

## 💻 Exercises: Day 4

1. **Generate a Report Header:**
    * Create variables for `report_title` ("Quarterly Sales Report") and `fiscal_year` (2024).
    * Using an f-string, create a header that looks like: `*** QUARTERLY SALES REPORT - FY2024 ***`
    * Print the header. (Hint: you can use `.upper()` on the title).

2. **Clean Up Customer Data:**
    * You receive a customer name as a string: `customer_name = "  john doe  "`.
    * Write a script that cleans this name by:
        * Removing leading/trailing whitespace.
        * Capitalizing it to "John Doe". (Hint: there's a `.title()` method, or you can get creative with `.upper()` and slicing).
    * Print the cleaned name.

3. **Parse Product SKU:**
    * A product Stock Keeping Unit (SKU) is given as a string: `sku = "PROD-G_ADGET-001"`.
    * The SKU format is `TYPE-PRODUCT-ID`.
    * Use the `.split()` method to break the SKU into its three components.
    * Print the product type, product name, and ID on separate lines.

🎉 **Fantastic!** You can now manipulate text data, which is a massive part of any real-world data analysis task. Cleaning, formatting, and parsing strings are skills you'll use every single day.
