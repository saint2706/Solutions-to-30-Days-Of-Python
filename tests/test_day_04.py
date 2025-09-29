import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_04_Strings.strings import (
    generate_report_header,
    clean_and_format_name,
    format_date_string,
    parse_sku,
    is_transaction_type,
    has_file_extension,
    feedback_contains_keyword,
)


def test_generate_report_header():
    """Tests the report header generation."""
    assert generate_report_header("Test Report", 2023) == "*** TEST REPORT - FY2023 ***"


def test_clean_and_format_name():
    """Tests name cleaning and formatting."""
    assert clean_and_format_name("  jane doe  ") == "Jane Doe"
    assert clean_and_format_name("single") == "Single"
    assert clean_and_format_name("  already Correct  ") == "Already Correct"


def test_format_date_string():
    """Tests date string formatting."""
    assert format_date_string("2023-Jan-15") == "2023/Jan/15"
    assert (
        format_date_string("2023.01.01", old_separator=".", new_separator="-")
        == "2023-01-01"
    )


def test_parse_sku():
    """Tests SKU parsing."""
    sku = "PROD-GADGET-001"
    result = parse_sku(sku)
    assert result is not None
    assert result["type"] == "PROD"
    assert result["name"] == "GADGET"
    assert result["id"] == "001"

    assert parse_sku("INVALID-SKU") is None


def test_is_transaction_type():
    """Tests transaction type checking."""
    assert is_transaction_type("INV-123", "INV") is True
    assert is_transaction_type("ORD-456", "INV") is False


def test_has_file_extension():
    """Tests file extension checking."""
    assert has_file_extension("report.pdf", ".pdf") is True
    assert has_file_extension("image.jpg", ".png") is False


def test_feedback_contains_keyword():
    """Tests keyword search in feedback."""
    feedback_positive = "The service was fast and efficient."
    feedback_negative = "The product is too slow."
    assert feedback_contains_keyword(feedback_positive, "slow") is False
    assert feedback_contains_keyword(feedback_negative, "slow") is True
