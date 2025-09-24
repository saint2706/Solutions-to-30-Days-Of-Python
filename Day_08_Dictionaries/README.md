# 📘 Day 8: Dictionaries - Structuring Complex Business Data

We've worked with simple collections like lists and tuples. But real-world business data is rarely just a simple list. It's structured. A customer has a name, an email, AND a location. A product has a price, an SKU, AND an inventory count. For this, we need **dictionaries**.

A dictionary is the most important data structure for handling structured data in Python. Think of it as a record or a profile, where each piece of information has a specific label.

## What is a Dictionary?

A dictionary is an **unordered** collection of **key-value pairs**.

* **Key:** A unique identifier for a piece of data (must be an immutable type, usually a string).
* **Value:** The data itself (can be any data type, including another dictionary).

You create a dictionary using curly braces `{}` with `key: value` pairs separated by commas.

```python
# A dictionary representing a customer profile
customer = {
    "customer_id": "CUST-001",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "company": "InnovateCorp",
    "is_premium_member": True,
    "total_spent": 2500.75
}
```

## Working with Dictionary Data

### Accessing Data

You access a value by using its key in square brackets `[]`.

```python
customer_email = customer["email"]  # Accesses "john.doe@example.com"
company_name = customer["company"]  # Accesses "InnovateCorp"
```

Using a key that doesn't exist will cause an error. A safer way is to use the `.get()` method, which returns `None` (or a default value you provide) if the key is not found.

```python
# Safer access
phone_number = customer.get("phone") # Returns None, no error
phone_number_default = customer.get("phone", "N/A") # Returns "N/A"
```

### Adding and Modifying Data

You can add a new key-value pair or modify an existing one using simple assignment.

```python
# Add a new key-value pair
customer["phone"] = "555-123-4567"

# Modify an existing value
customer["is_premium_member"] = False
```

### Removing Data

You can remove a key-value pair using the `del` keyword.

```python
del customer["total_spent"]
```

## Nested Dictionaries

The real power of dictionaries is that their values can be other dictionaries. This allows you to create complex, nested data structures that mirror real-world business objects.

```python
employee = {
    "employee_id": "EMP-042",
    "name": "Jane Smith",
    "department": "Marketing",
    "contact_info": {
        "email": "jane.smith@example.com",
        "phone_ext": 112
    },
    "projects": ["Q1 Campaign", "Website Redesign"]
}

# Accessing nested data
employee_email = employee["contact_info"]["email"]
first_project = employee["projects"][0]
```

## 💻 Exercises: Day 8

1. **Create a Product Dictionary:**
    * Create a dictionary to represent a product with the following information:
        * `product_id`: "PROD-123"
        * `product_name`: "SuperWidget"
        * `price`: 199.99
        * `in_stock`: True
        * `tags`: A list containing `"electronics"` and `"gadget"`.
    * Print the product's name and its price.

2. **Modify Employee Information:**
    * Start with the `employee` dictionary from the lesson above.
    * The employee has been promoted. Update the `department` to "Marketing Director".
    * They've been assigned a new project. Add "2025 Strategy" to the `projects` list.
    * Print the updated `employee` dictionary.

3. **Access Nested Data:**
    * Create a dictionary representing a `company` with keys for `company_name`, `year_founded`, and `headquarters`.
    * The value for `headquarters` should be another dictionary with keys for `city`, `state`, and `country`.
    * Write a script that creates this dictionary and then prints a sentence like: "[Company Name] is headquartered in [City], [State]."

🎉 **Amazing work!** Dictionaries are the cornerstone of handling structured data in Python. Almost every time you get data from an API, a database, or a complex file, it will come in the form of dictionaries. Mastering them is a huge step forward.
