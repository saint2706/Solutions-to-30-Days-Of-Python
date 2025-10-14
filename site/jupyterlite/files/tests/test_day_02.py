import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_02_Variables_Builtin_Functions.variables import analyze_weekly_sales


def test_analyze_weekly_sales_positive_data():
    """Test analyze_weekly_sales with a typical list of sales."""
    sales_data = [150.50, 200.00, 75.25, 300.75, 120.00, 450.50, 275.00]
    result = analyze_weekly_sales(sales_data)
    assert result["num_transactions"] == 7
    assert result["total_revenue"] == 1572.00
    assert result["smallest_sale"] == 75.25
    assert result["largest_sale"] == 450.50
    assert round(result["average_sale"], 2) == 224.57


def test_analyze_weekly_sales_empty_list():
    """Test analyze_weekly_sales with an empty list to check for edge cases."""
    sales_data = []
    # This function prints to stdout, so we just check it doesn't crash
    # and that the dictionary it would return is effectively None
    assert analyze_weekly_sales(sales_data) is None


def test_analyze_weekly_sales_single_item():
    """Test analyze_weekly_sales with a single sale."""
    sales_data = [100.00]
    result = analyze_weekly_sales(sales_data)
    assert result["num_transactions"] == 1
    assert result["total_revenue"] == 100.00
    assert result["smallest_sale"] == 100.00
    assert result["largest_sale"] == 100.00
    assert result["average_sale"] == 100.00
