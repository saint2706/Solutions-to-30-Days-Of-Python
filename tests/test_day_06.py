import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_06_Tuples.tuples import get_location_coordinates, unpack_transaction


def test_get_location_coordinates():
    """Tests the extraction of coordinates from a location tuple."""
    lat, lon = get_location_coordinates((40.7128, -74.0060))
    assert lat == 40.7128
    assert lon == -74.0060

    # Test with invalid data
    lat, lon = get_location_coordinates([10, 20])  # Not a tuple
    assert lat is None
    assert lon is None

    lat, lon = get_location_coordinates((10, 20, 30))  # Wrong length
    assert lat is None
    assert lon is None


def test_unpack_transaction():
    """Tests the unpacking of a transaction tuple into a dictionary."""
    transaction = (1001, "2024-03-15", 499.99)
    result = unpack_transaction(transaction)
    assert result is not None
    assert result["id"] == 1001
    assert result["date"] == "2024-03-15"
    assert result["amount"] == 499.99

    # Test with invalid data
    assert unpack_transaction([1, 2, 3]) is None  # Not a tuple
    assert unpack_transaction((1, 2)) is None  # Wrong length
