import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402  # Set backend before import
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_28_Advanced_Visualization import advanced_visualization as av


@pytest.fixture()
def sample_df():
    return pd.DataFrame(
        {
            "Date": pd.to_datetime(
                ["2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03"]
            ),
            "Product": ["A", "A", "B", "B"],
            "Revenue": [100.0, 120.0, 80.0, 140.0],
        }
    )


def test_build_product_revenue_bar(sample_df):
    fig = av.build_product_revenue_bar(sample_df)
    try:
        assert isinstance(fig, plt.Figure)
        assert len(fig.axes) == 1
        ax = fig.axes[0]
        assert ax.get_title() == "Total Revenue per Product"
        legend = ax.get_legend()
        assert legend is not None
        legend_labels = [text.get_text() for text in legend.get_texts()]
        assert any(label.startswith("Avg Revenue") for label in legend_labels)
        assert len(ax.patches) == sample_df["Product"].nunique()
    finally:
        plt.close(fig)


def test_build_sales_dashboard(sample_df):
    fig = av.build_sales_dashboard(sample_df)
    try:
        assert isinstance(fig, plt.Figure)
        assert len(fig.axes) == 2
        top_ax, bottom_ax = fig.axes
        assert top_ax.get_title() == "Daily Revenue Trend"
        assert bottom_ax.get_title() == "Distribution of Individual Sale Revenue"
        assert fig._suptitle is not None
        assert fig._suptitle.get_text() == "Company Sales Dashboard"
        assert len(top_ax.lines) == 1
        assert len(bottom_ax.patches) > 0
    finally:
        plt.close(fig)


def test_missing_columns_raises(sample_df):
    with pytest.raises(ValueError):
        av.build_product_revenue_bar(sample_df.drop(columns=["Product"]))
    with pytest.raises(ValueError):
        av.build_sales_dashboard(sample_df.drop(columns=["Date"]))


def test_empty_dataframe_raises(sample_df):
    empty_df = sample_df.iloc[0:0]
    with pytest.raises(ValueError):
        av.build_product_revenue_bar(empty_df)
    with pytest.raises(ValueError):
        av.build_sales_dashboard(empty_df)
