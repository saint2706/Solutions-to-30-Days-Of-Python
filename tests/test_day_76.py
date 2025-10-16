"""Tests for the Day 76 BI Platforms and Automation Tools helpers."""

from __future__ import annotations

import os
import sys

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_76_BI_Platforms_and_Automation_Tools import (  # noqa: E402
    build_platform_matrix,
    compare_export_formats,
    load_topics,
    simulate_refresh_workflow,
)

EXPECTED_TITLES = {
    "Power BI",
    "Tableau",
    "Qlik",
    "Looker",
    "BI Platforms",
    "Python",
    "R",
    "Standardisation",
    "Excel",
}


def test_all_topics_are_grouped() -> None:
    """Every requested roadmap title should be represented."""

    grouped = load_topics()
    discovered = {topic.title for topics in grouped.values() for topic in topics}
    assert EXPECTED_TITLES <= discovered


def test_platform_matrix_includes_metadata() -> None:
    """The platform matrix should expose export and automation metadata."""

    frame = build_platform_matrix()
    assert isinstance(frame, pd.DataFrame)
    power_bi = frame.loc[frame["platform"] == "Power BI"].iloc[0]
    assert "PowerPoint" in power_bi["export_formats"]
    assert "Power Automate" in power_bi["automation"]


def test_export_format_comparison_highlights_differences() -> None:
    """Export comparison should show Looker's Google Sheets delivery."""

    exports = compare_export_formats()
    looker_row = exports.loc[exports["platform"] == "Looker"].iloc[0]
    assert bool(looker_row["Google Sheets"]) is True
    assert bool(looker_row.get("PowerPoint", False)) is False


def test_refresh_workflow_reflects_python_r_handoff() -> None:
    """Automation workflow should include both scripting languages."""

    plan = simulate_refresh_workflow("Power BI", languages=("Python", "R"))
    assert plan["languages"] == ("Python", "R")
    assert any("Python" in step for step in plan["steps"])
    assert any("R" in step for step in plan["steps"])
    assert tuple(plan["connectors"])[:2] == ("Power Automate", "REST API")
