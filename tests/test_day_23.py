import sys
import os
import pytest
import pandas as pd
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_23_Pandas.pandas_from_csv import (
    load_data_from_csv,
    filter_by_title,
)

@pytest.fixture
def sample_dataframe():
    """Provides a sample Pandas DataFrame for testing."""
    data = {
        'id': [1, 2, 3, 4],
        'title': [
            'A Great Article on Python',
            'JavaScript Frameworks Guide',
            'Advanced Python Programming',
            'Data Science with R'
        ],
        'url': ['url1', 'url2', 'url3', 'url4']
    }
    return pd.DataFrame(data)

def test_load_data_from_csv(tmp_path: Path):
    """Tests loading data from a CSV file."""
    # Create a temporary CSV file
    csv_content = "id,title,url\n1,Test Title,test_url"
    file_path = tmp_path / "test.csv"
    file_path.write_text(csv_content)

    df = load_data_from_csv(str(file_path))
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert df.shape == (1, 3)
    assert df.iloc[0]['title'] == 'Test Title'

def test_load_data_from_csv_not_found():
    """Tests that loading a non-existent file returns None."""
    df = load_data_from_csv("non_existent_file.csv")
    assert df is None

def test_filter_by_title(sample_dataframe):
    """Tests filtering a DataFrame by a keyword in the title."""
    # Test for 'Python'
    python_df = filter_by_title(sample_dataframe, "Python")
    assert len(python_df) == 2
    assert python_df.iloc[0]['id'] == 1
    assert python_df.iloc[1]['id'] == 3

    # Test for 'JavaScript'
    js_df = filter_by_title(sample_dataframe, "JavaScript")
    assert len(js_df) == 1
    assert js_df.iloc[0]['id'] == 2

    # Test for a keyword that doesn't exist
    none_df = filter_by_title(sample_dataframe, "GoLang")
    assert len(none_df) == 0

def test_filter_by_title_invalid_df():
    """Tests that filtering returns an empty DataFrame for invalid input."""
    empty_df = filter_by_title(None, "Python")
    assert isinstance(empty_df, pd.DataFrame)
    assert empty_df.empty

    df_no_title = pd.DataFrame({'id': [1, 2]})
    empty_df_no_title = filter_by_title(df_no_title, "Python")
    assert isinstance(empty_df_no_title, pd.DataFrame)
    assert empty_df_no_title.empty