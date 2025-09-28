import sys
import os
import pytest
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_16_File_Handling.fh import (
    count_words_and_lines,
    find_most_common_words,
    extract_emails_from_file,
    analyze_sales_csv,
)

# Use a temporary directory for test files provided by pytest
@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path

def test_count_words_and_lines(temp_dir):
    """Tests counting words and lines from a file."""
    file_path = temp_dir / "test.txt"
    content = "First line with four words.\nSecond line has five words.\nThird."
    file_path.write_text(content)

    words, lines = count_words_and_lines(str(file_path))
    assert words == 11
    assert lines == 3

    # Test file not found
    words_nf, lines_nf = count_words_and_lines("non_existent_file.txt")
    assert words_nf == 0
    assert lines_nf == 0

def test_find_most_common_words(temp_dir):
    """Tests finding the most common words, ignoring stop words."""
    file_path = temp_dir / "common_words.txt"
    content = "sales report shows great sales figures and great profit"
    file_path.write_text(content)

    common = find_most_common_words(str(file_path), 2)
    assert common == [("sales", 2), ("great", 2)]

def test_extract_emails_from_file(temp_dir):
    """Tests extracting unique emails from a text file."""
    file_path = temp_dir / "emails.txt"
    content = "Contact support@example.com or sales@example.com for help. Invalid email: user@.com. Duplicate: support@example.com."
    file_path.write_text(content)

    emails = extract_emails_from_file(str(file_path))
    assert emails == ["sales@example.com", "support@example.com"]

def test_analyze_sales_csv(temp_dir):
    """Tests reading and analyzing a sales CSV file."""
    file_path = temp_dir / "sales.csv"
    content = "Product,Price,Quantity\nLaptop,1200,2\nMouse,25,10\nKeyboard,75,5\nMalformed,row\n"
    file_path.write_text(content)

    result = analyze_sales_csv(str(file_path))
    assert result is not None
    # Total Revenue = (1200*2) + (25*10) + (75*5) = 2400 + 250 + 375 = 3025
    assert result["total_revenue"] == pytest.approx(3025.0)
    assert result["average_transaction"] == pytest.approx(3025.0 / 3)

    # Test with empty file
    empty_file = temp_dir / "empty.csv"
    empty_file.write_text("Product,Price,Quantity\n")
    assert analyze_sales_csv(str(empty_file)) is None

    # Test file not found
    assert analyze_sales_csv("non_existent_file.csv") is None