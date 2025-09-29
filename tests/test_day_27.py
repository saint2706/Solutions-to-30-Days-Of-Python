import os
import sys

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  # Set backend before import

# Add repository root to Python path so lesson modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_27_Visualization.visualization import (
    build_daily_revenue_plot,
    build_price_vs_units_sold_plot,
    build_revenue_by_region_plot,
    build_units_sold_distribution_plot,
)


@pytest.fixture()
def sample_sales_dataframe() -> pd.DataFrame:
    """Provide a compact dataset for chart testing."""

    data = {
        "Date": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-01", "2024-01-03"]),
        "Region": ["North", "South", "East", "West"],
        "Revenue": [1200, 800, 500, 1300],
        "Units Sold": [15, 12, 8, 20],
        "Price": [50.0, 60.0, 45.0, 65.0],
        "Product": ["Laptop", "Laptop", "Tablet", "Monitor"],
    }
    return pd.DataFrame(data)


def _close(fig: plt.Figure) -> None:
    plt.close(fig)


def test_build_revenue_by_region_plot(sample_sales_dataframe: pd.DataFrame) -> None:
    fig = build_revenue_by_region_plot(sample_sales_dataframe)
    ax = fig.axes[0]
    assert ax.get_title() == "Total Revenue by Region"
    assert ax.get_ylabel() == "Total Revenue ($)"
    assert ax.get_xlabel() == "Region"
    _close(fig)


def test_build_daily_revenue_plot(sample_sales_dataframe: pd.DataFrame) -> None:
    fig = build_daily_revenue_plot(sample_sales_dataframe)
    ax = fig.axes[0]
    assert ax.get_title() == "Daily Revenue Trend"
    assert ax.get_ylabel() == "Total Revenue ($)"
    assert ax.get_xlabel() == "Date"
    _close(fig)


def test_build_units_sold_distribution_plot(sample_sales_dataframe: pd.DataFrame) -> None:
    fig = build_units_sold_distribution_plot(sample_sales_dataframe)
    ax = fig.axes[0]
    assert ax.get_title() == "Distribution of Units Sold per Transaction"
    assert ax.get_xlabel() == "Units Sold"
    assert ax.get_ylabel() == "Frequency"
    _close(fig)


def test_build_price_vs_units_sold_plot(sample_sales_dataframe: pd.DataFrame) -> None:
    fig = build_price_vs_units_sold_plot(sample_sales_dataframe)
    ax = fig.axes[0]
    assert ax.get_title() == "Price vs. Units Sold"
    assert ax.get_xlabel() == "Price ($)"
    assert ax.get_ylabel() == "Units Sold"
    legend = ax.get_legend()
    assert legend is not None
    assert legend.get_title().get_text() == "Product"
    _close(fig)
