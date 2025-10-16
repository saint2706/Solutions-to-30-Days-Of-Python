"""Tests for the Day 70 BI Metrics and Data Literacy lesson utilities."""

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_70_BI_Metrics_and_Data_Literacy import build_topic_dataframe, load_topics

EXPECTED_SECTIONS: dict[str, set[str]] = {
    "Metric design": {
        "Metrics and KPIs",
        "Types of Data Analysis",
        "Descriptive Analysis",
        "Predictive Analysis",
    },
    "Data typing": {
        "Variables and Data Types",
        "Categorical vs Numerical",
    },
    "Descriptive statistics": {
        "Mode",
        "Mean",
        "Median",
    },
    "Inferential readiness": {
        "Correlation vs Causation",
        "Confidence Intervals",
        "Inferential Statistics",
    },
}


def test_load_topics_groups_expected_titles() -> None:
    grouped = load_topics()
    assert set(grouped) == set(EXPECTED_SECTIONS)
    for section, expected_titles in EXPECTED_SECTIONS.items():
        titles = {topic.title for topic in grouped[section]}
        assert titles == expected_titles


def test_build_topic_dataframe_has_no_duplicates() -> None:
    frame = build_topic_dataframe()
    assert isinstance(frame, pd.DataFrame)
    assert set(frame["section"]) == set(EXPECTED_SECTIONS)
    assert set(frame["title"]) == set().union(*EXPECTED_SECTIONS.values())
    assert frame["title"].duplicated().sum() == 0
    assert len(frame) == sum(len(titles) for titles in EXPECTED_SECTIONS.values())
