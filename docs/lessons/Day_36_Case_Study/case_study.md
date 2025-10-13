# 📊 Day 36 – Capstone Case Study

## Overview

Day 36 ties together the full analytics workflow. You will load the
`case_study_sales.csv` dataset, clean it, surface core revenue insights, and
present a concise set of recommendations. The helpers in this folder mirror the
solution structure so that you can focus on translating business questions into
Python code.

## Files

| File | Description |
| --- | --- |
| [`case_study.py`](case_study.py) | Student-facing template containing callable helpers and a minimal `main()` driver you can customize. |
| [`case_study_sales.csv`](case_study_sales.csv) | Sales dataset that powers the analysis. |
| [`solutions.py`](solutions.py) | Fully worked reference solution with detailed walkthrough code. |

## Suggested Workflow

1. Use `load_case_study_data()` to import the CSV with parsed dates.
1. Call `clean_case_study_data()` to enforce schema expectations and rebuild the
   `Revenue` column when necessary.
1. Explore metrics via `summarize_case_study()` or write your own aggregations
   and visualizations.
1. Capture narrative takeaways for the Head of Sales along with supporting
   charts or tables.

Running the script directly executes the helper pipeline and prints the top-line
revenue summaries:

```bash
python Day_36_Case_Study/case_study.py
```

## Tests

Automated tests validate the helpers against the bundled dataset. From the
repository root run:

```bash
pytest tests/test_day_36.py
```

Utility helpers for the Day 36 capstone case study.

```python

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import pandas as pd

DATA_PATH = Path(__file__).with_name("case_study_sales.csv")


def load_case_study_data(path: str | Path = DATA_PATH) -> pd.DataFrame:
    """Return the raw sales data as a :class:`~pandas.DataFrame`.

    Parameters
    ----------
    path:
        Location of the ``case_study_sales.csv`` file. Defaults to the copy that
        ships with the repository.
    """

    return pd.read_csv(path, parse_dates=["Date"])


def clean_case_study_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean the raw case-study data for downstream analysis.

    The helper performs a light-touch cleanup that mirrors the steps students
    complete in the lesson notebook:

    * ensure the ``Date`` column uses ``datetime64`` values,
    * coerce numeric fields to numbers while dropping unparseable records,
    * calculate ``Revenue`` from ``Price`` and ``Units Sold`` when it is
      missing.
    """

    cleaned = data.copy()

    cleaned["Date"] = pd.to_datetime(cleaned["Date"], errors="coerce")

    numeric_columns = ["Price", "Units Sold"]
    has_revenue = "Revenue" in cleaned.columns
    if has_revenue:
        numeric_columns.append("Revenue")

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned = cleaned.dropna(subset=["Date", "Price", "Units Sold"])

    if not has_revenue:
        cleaned["Revenue"] = cleaned["Price"] * cleaned["Units Sold"]
    else:
        missing_revenue = cleaned["Revenue"].isna()
        if missing_revenue.any():
            cleaned.loc[missing_revenue, "Revenue"] = (
                cleaned.loc[missing_revenue, "Price"]
                * cleaned.loc[missing_revenue, "Units Sold"]
            )

    cleaned["Units Sold"] = cleaned["Units Sold"].round().astype("Int64")
    cleaned["Revenue"] = cleaned["Revenue"].astype(float)

    return cleaned.reset_index(drop=True)


def summarize_case_study(data: pd.DataFrame, *, top_n: int = 5) -> Dict[str, Any]:
    """Generate headline metrics for the capstone analysis."""

    if data.empty:
        raise ValueError("Cannot summarize an empty DataFrame.")

    summary: Dict[str, Any] = {
        "top_products": data.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n),
        "region_revenue": data.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "segment_revenue": data.groupby("Customer Segment")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "channel_revenue": data.groupby("Sales Channel")["Revenue"]
        .sum()
        .sort_values(ascending=False),
        "price_units_correlation": data[["Price", "Units Sold"]]
        .corr()
        .loc["Price", "Units Sold"],
        "monthly_revenue": data.set_index("Date")["Revenue"].resample("M").sum(),
    }

    return summary


def main() -> None:
    """Run a minimal command-line summary for the case study."""

    raw = load_case_study_data()
    cleaned = clean_case_study_data(raw)
    summary = summarize_case_study(cleaned)

    print("Top products by revenue:")
    print(summary["top_products"])
    print("\nRevenue by region:")
    print(summary["region_revenue"])


if __name__ == "__main__":
    main()

```
