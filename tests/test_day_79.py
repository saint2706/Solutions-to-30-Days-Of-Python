"""Tests for the Day 79 BI Storytelling and Stakeholder Influence helpers."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_79_BI_Storytelling_and_Stakeholder_Influence import (
    build_influence_brief,
    generate_story_arc,
    influence_lever_template,
    load_topics,
    narrative_asset_template,
)

EXPECTED_NARRATIVE_TITLES = [
    "Storytelling Framework",
    "Communication & Storytelling",
    "Presentation Design",
    "Writing Executive Summaries",
    "Dashboard Design",
]

EXPECTED_INFLUENCE_TITLES = [
    "Stakeholder Management",
    "Change Management",
    "Project Management",
    "Business Acumen",
    "Critical Thinking",
    "Soft Skills",
]


def test_grouped_topics_include_expected_titles() -> None:
    """The grouped topics should expose both narrative and influence clusters."""

    grouped = load_topics()
    assert set(grouped) == {"Narrative assets", "Influence levers"}

    narrative_titles = [topic.title for topic in grouped["Narrative assets"]]
    influence_titles = [topic.title for topic in grouped["Influence levers"]]

    assert narrative_titles == EXPECTED_NARRATIVE_TITLES
    assert influence_titles == EXPECTED_INFLUENCE_TITLES


def test_narrative_template_contains_all_titles() -> None:
    """Narrative asset prompts should include each roadmap title exactly once."""

    template = narrative_asset_template()
    titles = [entry["title"] for entry in template]
    prompts = [entry["coaching_prompt"] for entry in template]

    assert titles == EXPECTED_NARRATIVE_TITLES
    assert all(prompt for prompt in prompts)


def test_influence_template_contains_all_titles() -> None:
    """Influence lever prompts should include each roadmap title exactly once."""

    template = influence_lever_template()
    titles = [entry["title"] for entry in template]
    prompts = [entry["coaching_prompt"] for entry in template]

    assert titles == EXPECTED_INFLUENCE_TITLES
    assert all(prompt for prompt in prompts)


def test_generate_story_arc_structure() -> None:
    """Story arcs should follow the defined stage order and include guidance text."""

    arc = generate_story_arc(
        metric_name="net revenue retention",
        insight="NRR dropped four points",
        audience="executive sponsors",
        call_to_action="approve enablement resources",
    )

    assert arc["metric"] == "net revenue retention"
    assert arc["audience"] == "executive sponsors"
    assert arc["insight"] == "NRR dropped four points"
    assert arc["call_to_action"] == "approve enablement resources"

    steps = arc["arc"]
    assert [step["linked_topic"] for step in steps] == EXPECTED_NARRATIVE_TITLES
    assert [step["stage"] for step in steps] == [
        "Opening",
        "Tension",
        "Visualization",
        "Decision",
        "Reinforcement",
    ]
    assert all(step["guidance"] for step in steps)


def test_build_influence_brief_structure() -> None:
    """Influence briefs should align prompts with each roadmap title in order."""

    brief = build_influence_brief(
        stakeholder="customer success leadership",
        objective="stabilize renewals",
        change_risk="manager fatigue",
    )

    assert brief["stakeholder"] == "customer success leadership"
    assert brief["objective"] == "stabilize renewals"
    assert brief["change_risk"] == "manager fatigue"

    plan = brief["plan"]
    assert [entry["lever"] for entry in plan] == EXPECTED_INFLUENCE_TITLES
    assert all(entry["guidance"] for entry in plan)
