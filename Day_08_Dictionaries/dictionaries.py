"""
Day 8: Structuring Business Data with Dictionaries

This script demonstrates how to create, access, and modify
dictionaries that represent complex business records.
"""

# --- Creating a Dictionary for a Customer Profile ---
print("--- Customer Profile Dictionary ---")
customer = {
    "customer_id": "CUST-001",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "company": "InnovateCorp",
    "is_premium_member": True,
    "total_spent": 2500.75,
}
print(f"Original customer record: {customer}")

# Accessing data using keys
print(f"Customer's email: {customer['email']}")

# Safer access using .get() for a key that might not exist
phone_number = customer.get("phone", "N/A")
print(f"Customer's phone: {phone_number}")
print()


# --- Modifying a Dictionary ---
print("--- Modifying Customer Record ---")
# Add a phone number
customer["phone"] = "555-123-4567"
print(f"Added phone number: {customer['phone']}")

# Update total spent
customer["total_spent"] += 500.25  # Customer made another purchase
print(f"Updated total spent: ${customer['total_spent']:.2f}")

# Remove a key-value pair
del customer["is_premium_member"]
print(f"Record after removing premium status: {customer}")
print("-" * 20)


# --- Nested Dictionaries for Complex Structures ---
print("--- Nested Dictionary for an Employee Profile ---")
employee = {
    "employee_id": "EMP-042",
    "name": "Jane Smith",
    "department": "Marketing",
    "contact_info": {"email": "jane.smith@example.com", "phone_ext": 112},
    "projects": ["Q1 Campaign", "Website Redesign"],
}

# Accessing nested data
employee_email = employee["contact_info"]["email"]
print(f"Employee Email: {employee_email}")

# Accessing an item in a list within a dictionary
first_project = employee["projects"][0]
print(f"First project assigned: {first_project}")

# Adding a new project to the list inside the dictionary
employee["projects"].append("2025 Strategy")
print(f"Updated projects: {employee['projects']}")
print("-" * 20)
