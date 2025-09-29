"""Tests for the Day 31 database utilities."""

import os
import sqlite3
import sys

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_31_Databases.databases import (
    EMPLOYEE_ROWS,
    cleanup_employee_db,
    fetch_department_dataframe,
    fetch_department_salaries,
    initialize_employee_db,
)


def test_initialize_employee_db_creates_table(tmp_path):
    db_path = tmp_path / "company.db"

    initialize_employee_db(db_path)

    with sqlite3.connect(db_path) as connection:
        table_exists = connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='employees'"
        ).fetchone()
        assert table_exists is not None

        (row_count,) = connection.execute("SELECT COUNT(*) FROM employees").fetchone()
        assert row_count == len(EMPLOYEE_ROWS)


def test_fetch_department_salaries_returns_sorted_results(tmp_path):
    db_path = tmp_path / "company.db"
    initialize_employee_db(db_path)

    sales_salaries = fetch_department_salaries(db_path, "Sales")

    assert sales_salaries == [("Alice", 80_000.0), ("Charlie", 85_000.0)]


def test_fetch_department_dataframe_returns_dataframe(tmp_path):
    db_path = tmp_path / "company.db"
    initialize_employee_db(db_path)

    engineering_df = fetch_department_dataframe(db_path, "Engineering")

    assert list(engineering_df.columns) == [
        "employee_id",
        "name",
        "department",
        "salary",
    ]
    assert engineering_df["name"].tolist() == ["Bob", "Eve"]
    assert pd.api.types.is_float_dtype(engineering_df["salary"])


def test_cleanup_employee_db_removes_file(tmp_path):
    db_path = tmp_path / "company.db"
    initialize_employee_db(db_path)

    assert db_path.exists()
    cleanup_employee_db(db_path)
    assert not db_path.exists()

