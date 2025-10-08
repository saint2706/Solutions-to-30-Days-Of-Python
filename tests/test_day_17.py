import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_17_Regular_Expressions.regex import (
    clean_text_advanced,
    extract_and_analyze_numbers,
    find_most_common_words,
    is_valid_python_variable,
)


def test_find_most_common_words():
    """Tests finding the most common words in a text."""
    text = "The quick brown fox jumps over the lazy dog. The dog was happy."
    # Expected counts: the: 3, dog: 2, quick: 1, brown: 1, etc.
    common = find_most_common_words(text, 2)
    assert common == [("the", 3), ("dog", 2)]


def test_extract_and_analyze_numbers():
    """Tests extracting numbers and calculating their range."""
    text = "Values are -10, 5, 0, and 15."
    result = extract_and_analyze_numbers(text)
    assert result["sorted_numbers"] == [-10, 0, 5, 15]
    assert result["distance"] == 25

    # Test with no numbers
    result_no_nums = extract_and_analyze_numbers("No numbers here.")
    assert result_no_nums["sorted_numbers"] == []
    assert result_no_nums["distance"] == 0


def test_is_valid_python_variable():
    """Tests the Python variable name validation."""
    assert is_valid_python_variable("valid_name") is True
    assert is_valid_python_variable("_valid_too") is True
    assert is_valid_python_variable("ValidName123") is True
    assert is_valid_python_variable("invalid-name") is False
    assert is_valid_python_variable("1invalid") is False
    assert is_valid_python_variable(" with_space") is False
    assert is_valid_python_variable("name with space") is False


def test_clean_text_advanced():
    """Tests the advanced text cleaning function."""
    text = "Hello! This is a test... with 123 numbers & symbols%."
    cleaned = clean_text_advanced(text)
    assert cleaned == "hello this is a test with 123 numbers  symbols"
