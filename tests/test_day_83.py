"""Tests for the Day 83 BI Cloud and Modern Data Stack module."""

from __future__ import annotations

from Day_83_BI_Cloud_and_Modern_Data_Stack import (
    CLOUD_TITLES,
    build_cloud_topic_dataframe,
    build_provider_comparison_frame,
    group_cloud_topics,
)


def test_cloud_topic_dataframe_includes_all_titles() -> None:
    """Every required cloud title should appear in the lesson dataframe."""

    frame = build_cloud_topic_dataframe()
    assert set(frame["title"]) == set(CLOUD_TITLES)
    assert {"section", "title", "description", "cost_trade_off"}.issubset(frame.columns)


def test_grouped_topics_cover_all_titles() -> None:
    """Grouped topics should account for each roadmap node exactly once."""

    groups = group_cloud_topics()
    gathered_titles = [topic.title for topics in groups.values() for topic in topics]
    assert sorted(gathered_titles) == sorted(CLOUD_TITLES)


def test_provider_comparison_covers_all_clouds() -> None:
    """The provider comparison helper should include AWS, GCP, and Azure."""

    frame = build_provider_comparison_frame()
    assert list(frame["provider"]) == ["AWS", "Azure", "GCP"]
    expected_columns = {
        "provider",
        "managed_warehouse",
        "analytics_services",
        "orchestration",
        "pricing_highlight",
        "notable_integration",
    }
    assert expected_columns.issubset(set(frame.columns))
    assert frame.notna().all().all()
