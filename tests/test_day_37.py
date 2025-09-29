"""Tests for the Day 37 recap helpers."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_37_Conclusion.conclusion import (  # noqa: E402
    get_next_steps,
    get_recap_checklist,
    main,
)


def test_get_recap_checklist_returns_expected_items():
    expected = [
        "Review the Python foundations covered across the 50-day journey.",
        "Revisit data analytics workflows, from cleaning through visualization.",
        "Connect the dots between statistical thinking and business strategy.",
        "Reflect on automation opportunities identified during the lessons.",
    ]
    checklist = get_recap_checklist()

    assert isinstance(checklist, list)
    assert checklist == expected


def test_get_next_steps_returns_expected_actions():
    expected = [
        {
            "title": "Build a portfolio project",
            "description": (
                "Apply the analytics-to-insights pipeline on a business dataset "
                "and document the impact for stakeholders."
            ),
        },
        {
            "title": "Deepen machine learning skills",
            "description": (
                "Experiment with supervised and unsupervised models using the "
                "frameworks introduced in later lessons."
            ),
        },
        {
            "title": "Share knowledge with peers",
            "description": (
                "Host a lunch-and-learn or internal workshop to reinforce your "
                "understanding and surface collaboration ideas."
            ),
        },
    ]
    next_steps = get_next_steps()

    assert isinstance(next_steps, list)
    assert next_steps == expected


def test_main_outputs_requested_section(capsys):
    main(["--section", "checklist"])
    captured = capsys.readouterr()
    assert "Day 37 Recap Checklist:" in captured.out
    assert "Recommended Next Steps" not in captured.out

    main(["--section", "next-steps"])
    captured = capsys.readouterr()
    assert "Recommended Next Steps:" in captured.out
    assert "Day 37 Recap Checklist" not in captured.out
