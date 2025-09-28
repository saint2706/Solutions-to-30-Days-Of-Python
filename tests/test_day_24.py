import sys
import os
import pytest
import pandas as pd
import numpy as np

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_24_Pandas_Advanced.pandas_adv import (
    select_by_label,
    select_by_position,
    filter_by_high_revenue,
    filter_by_product_and_region,
    handle_missing_data,
)

@pytest.fixture
def sample_dataframe():
    """Provides a sample DataFrame for testing advanced operations."""
    data = {
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03'],
        'Region': ['North', 'South', 'North', 'South'],
        'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard'],
        'Revenue': [60000, 1000, np.nan, 3000]
    }
    return pd.DataFrame(data)

def test_select_by_label(sample_dataframe):
    """Tests selecting data using .loc."""
    selection = select_by_label(sample_dataframe, 1, ['Product', 'Region'])
    assert selection['Product'] == 'Mouse'
    assert selection['Region'] == 'South'

def test_select_by_position(sample_dataframe):
    """Tests selecting data using .iloc."""
    selection = select_by_position(sample_dataframe, 2, slice(1, 3))
    assert selection['Region'] == 'North'
    assert selection['Product'] == 'Laptop'

def test_filter_by_high_revenue(sample_dataframe):
    """Tests conditional filtering for high revenue."""
    filtered_df = filter_by_high_revenue(sample_dataframe, 50000)
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['Product'] == 'Laptop'

def test_filter_by_product_and_region(sample_dataframe):
    """Tests multi-condition filtering."""
    filtered_df = filter_by_product_and_region(sample_dataframe, 'Laptop', 'North')
    assert len(filtered_df) == 2
    assert filtered_df.iloc[0]['Date'] == '2023-01-01'
    assert filtered_df.iloc[1]['Date'] == '2023-01-02'

def test_handle_missing_data_drop(sample_dataframe):
    """Tests handling missing data by dropping rows."""
    # Row 2 has a NaN value
    df_dropped = handle_missing_data(sample_dataframe, strategy='drop')
    assert len(df_dropped) == 3
    assert 2 not in df_dropped.index

def test_handle_missing_data_fill(sample_dataframe):
    """Tests handling missing data by filling with the mean."""
    # Mean of non-NaN revenue is (60000 + 1000 + 3000) / 3 = 21333.33
    df_filled = handle_missing_data(sample_dataframe, strategy='fill')
    assert len(df_filled) == 4
    assert df_filled.loc[2, 'Revenue'] == pytest.approx(21333.33, rel=1e-2)
    # Check that other values are unchanged
    assert df_filled.loc[0, 'Revenue'] == 60000