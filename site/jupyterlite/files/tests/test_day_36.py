"""Tests for the Day 36 case study helpers."""

import os
import sys

import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_36_Case_Study.case_study import (  # noqa: E402
    clean_case_study_data,
    load_case_study_data,
    summarize_case_study,
)


def _load_cleaned_frame() -> pd.DataFrame:
    raw = load_case_study_data()
    return clean_case_study_data(raw)


def test_clean_case_study_data_types():
    cleaned = _load_cleaned_frame()

    assert pd.api.types.is_datetime64_ns_dtype(cleaned["Date"])
    assert pd.api.types.is_float_dtype(cleaned["Price"])
    assert pd.api.types.is_integer_dtype(cleaned["Units Sold"])
    assert pd.api.types.is_float_dtype(cleaned["Revenue"])


def test_summarize_case_study_outputs():
    cleaned = _load_cleaned_frame()
    summary = summarize_case_study(cleaned)

    expected_top_products = [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Gaming Console",
        "Monitor",
    ]

    assert summary["top_products"].index.tolist() == expected_top_products
    assert summary["top_products"].iloc[0] == pytest.approx(158_830.0)

    assert summary["region_revenue"].idxmax() == "North"
    assert summary["region_revenue"].loc["North"] == pytest.approx(98_100.0)

    assert summary["price_units_correlation"] == pytest.approx(-0.6828263212)

    monthly_revenue = summary["monthly_revenue"]
    january = pd.Timestamp("2024-01-31")
    assert monthly_revenue.loc[january] == pytest.approx(33_500.0)
