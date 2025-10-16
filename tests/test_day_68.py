"""Tests for the Day 68 BI Analyst Foundations lesson utilities."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_68_BI_Analyst_Foundations import build_topic_dataframe, load_topics

EXPECTED_TITLES = {
    "Introduction",
    "What is BI?",
    "Why BI Matters?",
    "Responsibilities",
    "Skills",
    "BI Analyst vs Other Roles",
}


def test_load_topics_returns_foundations_grouping() -> None:
    grouped = load_topics()
    assert list(grouped.keys()) == ["Foundations"]
    titles = {topic.title for topic in grouped["Foundations"]}
    assert titles == EXPECTED_TITLES


def test_build_topic_dataframe_contains_all_titles() -> None:
    frame = build_topic_dataframe()
    assert set(frame["title"]) == EXPECTED_TITLES
    assert set(frame["section"]) == {"Foundations"}
    assert frame["description"].str.len().min() > 0
