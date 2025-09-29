import os
import sys

import numpy as np
import pandas as pd
import pytest

# Add project root to import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_26_Statistics.stats import (  # noqa: E402
    build_correlation_heatmap,
    build_revenue_distribution_chart,
    compute_correlations,
    load_sales_data,
    run_ab_test,
    summarize_revenue,
)


def test_load_sales_data_drops_missing_rows(tmp_path):
    raw = pd.DataFrame(
        {
            "Units Sold": [10, 20, np.nan],
            "Price": [2.5, 3.0, 4.0],
            "Revenue": [25.0, 60.0, 80.0],
        }
    )
    csv_path = tmp_path / "sales.csv"
    raw.to_csv(csv_path, index=False)

    cleaned = load_sales_data(csv_path)

    assert cleaned.shape == (2, 3)
    assert cleaned["Units Sold"].isna().sum() == 0


def test_summarize_revenue_returns_expected_metrics():
    df = pd.DataFrame({"Revenue": [100.0, 150.0, 250.0]})

    summary = summarize_revenue(df)

    assert summary["mean"] == pytest.approx(166.6666, rel=1e-4)
    assert summary["median"] == 150.0
    assert summary["std"] == pytest.approx(76.376, rel=1e-3)
    assert summary["min"] == 100.0
    assert summary["max"] == 250.0
    pd.testing.assert_series_equal(summary["describe"].loc["mean"], df.describe().loc["mean"])


def test_compute_correlations_matches_pandas_corr():
    df = pd.DataFrame(
        {
            "Units Sold": [10, 20, 30, 40],
            "Price": [5.0, 6.0, 7.0, 8.0],
            "Revenue": [50.0, 120.0, 210.0, 320.0],
        }
    )

    correlation_matrix = compute_correlations(df)
    expected = df[["Units Sold", "Price", "Revenue"]].corr()

    pd.testing.assert_frame_equal(correlation_matrix, expected)


def test_run_ab_test_returns_ttest_metrics():
    group_a = [10.5, 12.1, 11.8, 13.0, 12.5, 11.9, 12.3]
    group_b = [12.8, 13.5, 13.2, 14.0, 13.8, 14.1, 13.6]

    results = run_ab_test(group_a, group_b, alpha=0.05)

    assert results["t_statistic"] == pytest.approx(-4.5575, rel=1e-4)
    assert results["p_value"] == pytest.approx(0.0006575, rel=1e-4)
    assert results["is_significant"] is True
    assert results["alpha"] == 0.05


def test_build_revenue_distribution_chart_returns_histogram():
    df = pd.DataFrame({"Revenue": [100.0, 150.0, 200.0, 200.0]})

    figure = build_revenue_distribution_chart(df)

    assert figure.data, "Expected histogram trace to be present"
    histogram = figure.data[0]
    assert histogram.type == "histogram"
    assert list(histogram.x) == df["Revenue"].tolist()


def test_build_correlation_heatmap_uses_compute_correlations():
    df = pd.DataFrame(
        {
            "Units Sold": [10, 20, 30, 40],
            "Price": [5.0, 6.0, 7.0, 8.0],
            "Revenue": [50.0, 120.0, 210.0, 320.0],
        }
    )

    figure = build_correlation_heatmap(df)
    heatmap = figure.data[0]

    correlations = compute_correlations(df)

    assert heatmap.type == "heatmap"
    assert list(heatmap.x) == list(correlations.columns)
    assert list(heatmap.y) == list(correlations.index)
    np.testing.assert_allclose(heatmap.z, correlations.values)
