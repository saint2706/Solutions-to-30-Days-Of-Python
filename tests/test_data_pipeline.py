"""Integration tests covering the Day 24-26 analytics pipeline."""

from __future__ import annotations

from pathlib import Path
import os
import sys
from typing import Tuple

import numpy as np
import pandas as pd
import pytest

# Ensure the project root is importable when running `pytest` from subdirectories.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Day_24_Pandas_Advanced.pandas_adv import (
    filter_by_high_revenue,
    filter_by_product_and_region,
    handle_missing_data,
    load_sales_data,
    select_by_label,
    select_by_position,
)
from Day_25_Data_Cleaning.data_cleaning import clean_sales_data
from Day_26_Statistics.stats import (
    compute_correlations,
    load_sales_data as stats_load_sales_data,
    run_ab_test,
    summarize_revenue,
)


@pytest.fixture
def raw_sales_frame() -> pd.DataFrame:
    """Create a messy sales DataFrame spanning lessons 24-26."""

    data = {
        "Order ID": [1001, 1002, 1003, 1004, 1005, 1001, 1002, 1006],
        "Order Date": [
            "2024-01-05",
            "2024-01-06",
            "2024-01-07",
            "2024-01-08",
            "2024-01-09",
            "2024-01-05",
            "2024-01-06",
            "2024-01-10",
        ],
        "Region": [
            "  North ",
            "South",
            "USA",
            "West  ",
            "North",
            "North",
            "south ",
            "East",
        ],
        "Product": [
            "Laptop",
            "Keyboard",
            "Mouse",
            "Monitor",
            "Keyboard",
            "Laptop",
            "KEYBOARD",
            "Webcam",
        ],
        "Units Sold": [90, 140, 260, 95, 130, 90, 145, 160],
        "Price": [
            "$1,200.00",
            "$80.00",
            "$22.00",
            "$320.00",
            "$78.00",
            "$1,200.00",
            "$80.00",
            "$55.00",
        ],
        "Revenue": [108000.0, 11200.0, 5720.0, 30400.0, 10140.0, 108000.0, np.nan, np.nan],
    }
    return pd.DataFrame(data)


def _run_pipeline(
    raw_df: pd.DataFrame, tmp_path
) -> Tuple[Path, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Persist the raw data and run the Day 24-26 pipeline."""

    csv_path = tmp_path / "integration_sales.csv"
    raw_df.to_csv(csv_path, index=False)

    loaded = load_sales_data(str(csv_path))
    filled = handle_missing_data(loaded, strategy="fill")
    cleaned = clean_sales_data(filled)
    return csv_path, loaded, filled, cleaned


def test_sales_pipeline_cleans_and_summarises(raw_sales_frame, tmp_path):
    """End-to-end check that cleaning and statistics align across lessons."""

    csv_path, loaded, filled, cleaned = _run_pipeline(raw_sales_frame, tmp_path)

    # Day 24 helpers should load the CSV and fill missing revenue values.
    assert loaded.shape == raw_sales_frame.shape
    assert filled["Revenue"].isna().sum() == 0

    # Day 25 cleans the types, text casing, and duplicate Order IDs.
    assert cleaned.shape[0] == 6
    assert cleaned["Order Date"].dtype.kind == "M"
    assert pd.api.types.is_float_dtype(cleaned["Price"])
    assert cleaned["Region"].str.islower().all()
    assert cleaned["Order ID"].is_unique

    loc_selection = select_by_label(cleaned, 1, ["Product", "Region"])
    assert loc_selection["Product"] == "keyboard"
    assert loc_selection["Region"] == "south"

    positional = select_by_position(cleaned, 0, slice(0, 3))
    assert positional["Order ID"] == 1001
    assert positional["Region"] == "north"

    high_revenue = filter_by_high_revenue(cleaned, 50000)
    assert set(high_revenue["Order ID"]) == {1001}

    keyboard_south = filter_by_product_and_region(cleaned, "keyboard", "south")
    assert keyboard_south.shape[0] == 1
    assert keyboard_south.iloc[0]["Revenue"] == pytest.approx(11200.0)

    # Day 26 statistics operate on the cleaned DataFrame without error.
    summary = summarize_revenue(cleaned)
    assert summary["mean"] == pytest.approx(35172.7777777778, rel=1e-12)
    assert summary["median"] == pytest.approx(20800.0)
    assert summary["std"] == pytest.approx(38739.19143403696, rel=1e-12)
    assert summary["min"] == pytest.approx(5720.0)
    assert summary["max"] == pytest.approx(108000.0)
    pd.testing.assert_series_equal(
        summary["describe"].loc["mean"], cleaned.describe().loc["mean"]
    )

    correlations = compute_correlations(cleaned)
    expected = cleaned[["Units Sold", "Price", "Revenue"]].corr()
    pd.testing.assert_frame_equal(correlations, expected)

    stats_loaded = stats_load_sales_data(csv_path)
    assert stats_loaded.shape[0] == 6

    laptop_revenue = cleaned.loc[cleaned["Product"] == "laptop", "Revenue"]
    keyboard_revenue = cleaned.loc[cleaned["Product"] == "keyboard", "Revenue"]
    ab_results = run_ab_test(keyboard_revenue, laptop_revenue)
    assert set(ab_results.keys()) == {"t_statistic", "p_value", "alpha", "is_significant"}
    assert ab_results["alpha"] == pytest.approx(0.05)


def test_pipeline_outputs_are_ready_for_visualisation(raw_sales_frame, tmp_path):
    """Aggregations derived from the pipeline should be plot-ready."""

    _, _, _, cleaned = _run_pipeline(raw_sales_frame, tmp_path)

    # Region-level revenue totals power bar charts in Day 27.
    region_totals = cleaned.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    assert list(region_totals.index[:3]) == ["north", "east", "west"]
    assert region_totals.loc["north"] == pytest.approx(118140.0)
    assert region_totals.loc["east"] == pytest.approx(45576.6666667, rel=1e-9)

    # Daily revenue series should be chronologically sorted for line plots.
    daily_revenue = cleaned.groupby("Order Date")["Revenue"].sum().sort_index()
    assert str(daily_revenue.index.dtype) == "datetime64[ns]"
    assert daily_revenue.index.is_monotonic_increasing
    assert daily_revenue.loc[pd.Timestamp("2024-01-10")] == pytest.approx(
        45576.6666667, rel=1e-9
    )
