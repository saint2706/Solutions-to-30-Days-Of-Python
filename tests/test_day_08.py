import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_08_Dictionaries.dictionaries import (
    create_customer_profile,
    get_customer_attribute,
    update_customer_record,
    remove_customer_attribute,
    add_project_to_employee,
)


def test_create_customer_profile():
    """Tests the creation of a customer profile dictionary."""
    profile = create_customer_profile(
        "C01", "Jane", "Doe", "j.doe@email.com", "JD Inc.", False, 100.0
    )
    assert profile["customer_id"] == "C01"
    assert profile["first_name"] == "Jane"
    assert profile["total_spent"] == 100.0
    assert not profile["is_premium_member"]


def test_get_customer_attribute():
    """Tests safe attribute access from a profile."""
    profile = {"name": "Test", "value": 99}
    assert get_customer_attribute(profile, "name") == "Test"
    assert get_customer_attribute(profile, "value") == 99
    assert get_customer_attribute(profile, "non_existent_key") == "N/A"
    assert (
        get_customer_attribute(profile, "non_existent_key", default_value="Not Found")
        == "Not Found"
    )


def test_update_customer_record():
    """Tests updating and adding values to a customer record."""
    profile = {"id": 1, "total_spent": 100}
    # Test adding a new attribute
    updated_profile = update_customer_record(profile, "tier", "Gold", is_new=True)
    assert updated_profile["tier"] == "Gold"
    # Test updating an existing numerical value
    updated_profile_spent = update_customer_record(updated_profile, "total_spent", 50)
    assert updated_profile_spent["total_spent"] == 150
    # Ensure original dictionary is not modified
    assert "tier" not in profile
    assert profile["total_spent"] == 100


def test_remove_customer_attribute():
    """Tests removing an attribute from a profile."""
    profile = {"id": 1, "name": "Test", "status": "active"}
    updated_profile = remove_customer_attribute(profile, "status")
    assert "status" not in updated_profile
    assert updated_profile["id"] == 1
    # Test removing a key that doesn't exist (should not error)
    no_change_profile = remove_customer_attribute(profile, "non_existent_key")
    assert no_change_profile == profile
    # Ensure original dictionary is not modified
    assert "status" in profile


def test_add_project_to_employee():
    """Tests adding a project to an employee's project list."""
    employee = {"name": "Jane", "projects": ["Project A"]}
    updated_employee = add_project_to_employee(employee, "Project B")
    assert updated_employee["projects"] == ["Project A", "Project B"]
    # Ensure original employee dictionary and its inner list are not modified
    assert employee["projects"] == ["Project A"]

    # Test on employee with no projects key
    employee_no_projects = {"name": "John"}
    updated_employee_no_projects = add_project_to_employee(
        employee_no_projects, "Project C"
    )
    assert updated_employee_no_projects == employee_no_projects
