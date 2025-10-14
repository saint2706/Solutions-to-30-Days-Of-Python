import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_05_Lists.lists import (
    add_product,
    analyze_team_sales,
    get_first_half_sales,
    get_list_element,
    remove_product,
)


def test_get_list_element():
    """Tests safe element access from a list."""
    data = ["a", "b", "c"]
    assert get_list_element(data, 0) == "a"
    assert get_list_element(data, -1) == "c"
    assert get_list_element(data, 3) is None  # Test out-of-bounds
    assert get_list_element(data, -4) is None  # Test out-of-bounds


def test_get_first_half_sales():
    """Tests slicing the first half of a list."""
    assert get_first_half_sales([1, 2, 3, 4]) == [1, 2]
    assert get_first_half_sales([1, 2, 3, 4, 5]) == [1, 2]
    assert get_first_half_sales([1]) == []
    assert get_first_half_sales([]) == []


def test_add_product():
    """Tests adding a product to a list."""
    original = ["Laptop", "Mouse"]
    result = add_product(original, "Keyboard")
    assert result == ["Laptop", "Mouse", "Keyboard"]
    # Ensure the original list is not modified
    assert original == ["Laptop", "Mouse"]


def test_remove_product():
    """Tests removing a product from a list."""
    original = ["Laptop", "Mouse", "Keyboard"]
    result = remove_product(original, "Mouse")
    assert result == ["Laptop", "Keyboard"]
    # Ensure the original list is not modified
    assert original == ["Laptop", "Mouse", "Keyboard"]
    # Test removing an item that doesn't exist
    result_no_change = remove_product(original, "Webcam")
    assert result_no_change == original


def test_analyze_team_sales():
    """Tests the sales analysis function."""
    sales = [5000, 8000, 4500, 12000, 6000, 11000]
    result = analyze_team_sales(sales)
    assert result["sorted_sales"] == [12000, 11000, 8000, 6000, 5000, 4500]
    assert result["top_3_sales"] == [12000, 11000, 8000]
    assert result["total_top_sales"] == 31000


def test_analyze_team_sales_empty():
    """Tests the sales analysis function with an empty list."""
    assert analyze_team_sales([]) is None
