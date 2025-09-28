import sys
import os
import pytest
from datetime import datetime, date, timedelta

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_19_Python_Date_Time.date_time import (
    get_current_datetime_components,
    format_datetime_to_string,
    parse_string_to_datetime,
    calculate_date_difference,
)

def test_get_current_datetime_components():
    """Tests that the components dictionary is returned with the correct keys."""
    components = get_current_datetime_components()
    assert "day" in components
    assert "month" in components
    assert "year" in components
    assert "hour" in components
    assert "minute" in components
    assert "timestamp" in components
    assert isinstance(components["year"], int)

def test_format_datetime_to_string():
    """Tests formatting a datetime object into a string."""
    dt = datetime(2023, 10, 26, 14, 30)
    assert format_datetime_to_string(dt, "%Y-%m-%d %H:%M") == "2023-10-26 14:30"
    assert format_datetime_to_string(dt, "%A, %B %d, %Y") == "Thursday, October 26, 2023"

def test_parse_string_to_datetime():
    """Tests parsing a string into a datetime object."""
    date_str = "25-Mar-2023 10:00"
    dt_obj = parse_string_to_datetime(date_str, "%d-%b-%Y %H:%M")
    assert dt_obj.year == 2023
    assert dt_obj.month == 3
    assert dt_obj.day == 25
    assert dt_obj.hour == 10

    # Test invalid format
    assert parse_string_to_datetime("invalid-date", "%Y-%m-%d") is None

def test_calculate_date_difference():
    """Tests calculating the difference between two dates."""
    date1 = date(2023, 1, 10)
    date2 = date(2023, 1, 1)
    difference = calculate_date_difference(date1, date2)
    assert isinstance(difference, timedelta)
    assert difference.days == 9

    difference_negative = calculate_date_difference(date2, date1)
    assert difference_negative.days == -9