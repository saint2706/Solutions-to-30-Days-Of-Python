"""
Day 8: Structuring Business Data with Dictionaries (Refactored)

This script demonstrates how to create, access, and modify
dictionaries that represent complex business records. This version
is refactored into functions for better organization and testability.
"""


def create_customer_profile(cust_id, first, last, email, company, is_premium, spent):
    """Creates a dictionary representing a customer profile."""
    return {
        "customer_id": cust_id,
        "first_name": first,
        "last_name": last,
        "email": email,
        "company": company,
        "is_premium_member": is_premium,
        "total_spent": spent,
    }


def get_customer_attribute(customer_profile, attribute, default_value="N/A"):
    """Safely gets an attribute from a customer profile, returning a default if not found."""
    return customer_profile.get(attribute, default_value)


def update_customer_record(customer_profile, key, value, is_new=False):
    """Updates or adds a key-value pair to a customer profile."""
    profile_copy = customer_profile.copy()
    if is_new:
        profile_copy[key] = value
    else:
        # Assumes the key exists and we are modifying it (e.g., incrementing)
        if key in profile_copy:
            profile_copy[key] += value
    return profile_copy


def remove_customer_attribute(customer_profile, attribute):
    """Removes an attribute from a customer profile if it exists."""
    profile_copy = customer_profile.copy()
    if attribute in profile_copy:
        del profile_copy[attribute]
    return profile_copy


def add_project_to_employee(employee_profile, new_project):
    """Adds a new project to an employee's project list."""
    profile_copy = employee_profile.copy()
    # Ensure the 'projects' key exists and is a list
    if "projects" in profile_copy and isinstance(profile_copy["projects"], list):
        # To avoid modifying a list within the original dict, we copy it too
        profile_copy["projects"] = profile_copy["projects"].copy()
        profile_copy["projects"].append(new_project)
    return profile_copy


if __name__ == "__main__":
    # --- Creating a Dictionary for a Customer Profile ---
    print("--- Customer Profile Dictionary ---")
    customer_record = create_customer_profile(
        "CUST-001", "John", "Doe", "john.doe@example.com", "InnovateCorp", True, 2500.75
    )
    print(f"Original customer record: {customer_record}")

    # Accessing data using keys
    email_address = get_customer_attribute(customer_record, "email")
    print(f"Customer's email: {email_address}")

    # Safer access for a key that might not exist
    phone_num = get_customer_attribute(customer_record, "phone")
    print(f"Customer's phone: {phone_num}")
    print()

    # --- Modifying a Dictionary ---
    print("--- Modifying Customer Record ---")
    customer_record_with_phone = update_customer_record(
        customer_record, "phone", "555-123-4567", is_new=True
    )
    print(
        f"Added phone number: {get_customer_attribute(customer_record_with_phone, 'phone')}"
    )

    customer_record_updated_spent = update_customer_record(
        customer_record_with_phone, "total_spent", 500.25
    )
    print(f"Updated total spent: ${customer_record_updated_spent['total_spent']:.2f}")

    customer_record_no_premium = remove_customer_attribute(
        customer_record_updated_spent, "is_premium_member"
    )
    print(f"Record after removing premium status: {customer_record_no_premium}")
    print("-" * 20)

    # --- Nested Dictionaries for Complex Structures ---
    print("--- Nested Dictionary for an Employee Profile ---")
    employee_record = {
        "employee_id": "EMP-042",
        "name": "Jane Smith",
        "department": "Marketing",
        "contact_info": {"email": "jane.smith@example.com", "phone_ext": 112},
        "projects": ["Q1 Campaign", "Website Redesign"],
    }

    employee_email_address = employee_record.get("contact_info", {}).get("email")
    print(f"Employee Email: {employee_email_address}")

    first_proj = employee_record.get("projects", ["N/A"])[0]
    print(f"First project assigned: {first_proj}")

    employee_with_new_project = add_project_to_employee(
        employee_record, "2025 Strategy"
    )
    print(f"Updated projects: {employee_with_new_project['projects']}")
    print("-" * 20)
