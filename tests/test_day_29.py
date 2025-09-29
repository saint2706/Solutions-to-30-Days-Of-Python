import os
import sys

import pandas as pd
import plotly.graph_objects as go
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_29_Interactive_Visualization import interactive_visualization as iv


@pytest.fixture()
def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Date": pd.to_datetime(
                [
                    "2024-01-01",
                    "2024-01-01",
                    "2024-01-02",
                    "2024-01-03",
                ]
            ),
            "Region": ["North", "South", "North", "West"],
            "Revenue": [100.0, 80.0, 120.0, 90.0],
            "Product": ["A", "B", "A", "C"],
            "Price": [10.0, 12.0, 11.0, 13.0],
            "Units Sold": [10, 7, 11, 8],
        }
    )


def test_build_region_revenue_bar(sample_df: pd.DataFrame) -> None:
    fig = iv.build_region_revenue_bar(sample_df)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == sample_df["Region"].nunique()
    categories = [trace.x[0] for trace in fig.data]
    assert categories == sorted(sample_df["Region"].unique())
    for trace in fig.data:
        assert isinstance(trace, go.Bar)
        assert trace.name == trace.x[0]
        assert trace.y[0] == pytest.approx(
            sample_df.loc[sample_df["Region"] == trace.name, "Revenue"].sum()
        )


def test_build_daily_revenue_line(sample_df: pd.DataFrame) -> None:
    fig = iv.build_daily_revenue_line(sample_df)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 1
    trace = fig.data[0]
    assert isinstance(trace, go.Scatter)
    assert trace.mode == "lines+markers"
    expected_dates = list(
        pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]).to_pydatetime()
    )
    assert list(trace.x) == expected_dates
    assert list(trace.y) == [180.0, 120.0, 90.0]


def test_build_price_units_scatter(sample_df: pd.DataFrame) -> None:
    fig = iv.build_price_units_scatter(sample_df)
    assert isinstance(fig, go.Figure)
    assert len(fig.data) == sample_df["Product"].nunique()
    products = {trace.name for trace in fig.data}
    assert products == set(sample_df["Product"].unique())
    assert fig.layout.legend.title.text == "Product"
    for trace in fig.data:
        assert isinstance(trace, go.Scatter)
        assert all(size > 0 for size in trace.marker.size)


def test_missing_columns_raise(sample_df: pd.DataFrame) -> None:
    with pytest.raises(ValueError):
        iv.build_region_revenue_bar(sample_df.drop(columns=["Region"]))
    with pytest.raises(ValueError):
        iv.build_daily_revenue_line(sample_df.drop(columns=["Date"]))
    with pytest.raises(ValueError):
        iv.build_price_units_scatter(sample_df.drop(columns=["Product"]))


def test_empty_dataframe_raise(sample_df: pd.DataFrame) -> None:
    empty_df = sample_df.iloc[0:0]
    with pytest.raises(ValueError):
        iv.build_region_revenue_bar(empty_df)
    with pytest.raises(ValueError):
        iv.build_daily_revenue_line(empty_df)
    with pytest.raises(ValueError):
        iv.build_price_units_scatter(empty_df)
