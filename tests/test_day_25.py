import sys
import os
import pytest
import pandas as pd
import numpy as np

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_25_Data_Cleaning.data_cleaning import clean_sales_data

@pytest.fixture
def messy_dataframe():
    """
    Provides a messy DataFrame for testing the cleaning function.
    This includes a fully duplicate row and a duplicate Order ID with different data.
    """
    data = {
        'Order ID': [1, 2, 2, 3, 4, 1],
        'Order Date': ['2023-01-05', '2023-01-06', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09'],
        'Region': ['  North ', 'South', 'South', 'USA', 'West  ', 'North'],
        'Product': ['Laptop', 'Mouse', 'Mouse', 'KEYBOARD', 'Monitor', 'Laptop'],
        'Price': ['$1,200.00', '$25.50', '$25.50', '$75.00', '$300.99', '$1,250.00'], # Price is different for duplicate Order ID 1
        'Units Sold': [10, 50, 50, 30, 20, 15]
    }
    return pd.DataFrame(data)

def test_clean_sales_data(messy_dataframe):
    """
    Tests the entire data cleaning pipeline in the clean_sales_data function.
    """
    # Use a copy to prevent SettingWithCopyWarning and ensure test isolation
    cleaned_df = clean_sales_data(messy_dataframe.copy())

    # 1. Test final shape (should remove one full duplicate and one duplicate Order ID)
    # Original 6 -> remove full duplicate -> 5 -> remove Order ID 2 duplicate -> 4
    assert cleaned_df.shape[0] == 4

    # 2. Test data type correction
    assert pd.api.types.is_datetime64_any_dtype(cleaned_df['Order Date'])
    assert pd.api.types.is_float_dtype(cleaned_df['Price'])

    # 3. Test text cleaning and standardization
    # Test .str.strip() and .str.lower()
    assert 'north' in cleaned_df['Region'].iloc[0]
    assert 'keyboard' in cleaned_df['Product'].iloc[2]
    assert 'west' in cleaned_df['Region'].iloc[3]

    # Test .replace()
    assert 'united states' in cleaned_df['Region'].values

    # 4. Test price cleaning
    # Check the first price which had '$' and ','
    assert cleaned_df.iloc[0]['Price'] == 1200.00

    # 5. Test duplicate handling
    # Order ID 2 should only appear once
    assert cleaned_df['Order ID'].value_counts()[2] == 1
    # The original index should be preserved
    assert 0 in cleaned_df.index
    assert 1 in cleaned_df.index
    assert 3 in cleaned_df.index
    assert 4 in cleaned_df.index
    # Index 2 (the first duplicate) should be gone
    assert 2 not in cleaned_df.index