import os
import sys

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_07_Sets.sets import (
    analyze_visitor_segments,
    get_unique_items,
    upgrade_plan_features,
)


def test_get_unique_items():
    """Tests the de-duplication of a list using a set."""
    items = ["a", "b", "a", "c", "b", "d"]
    unique_set = get_unique_items(items)
    assert unique_set == {"a", "b", "c", "d"}
    assert len(unique_set) == 4


def test_analyze_visitor_segments():
    """Tests the segmentation analysis of two sets."""
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    result = analyze_visitor_segments(set_a, set_b)

    assert result["intersection"] == {3, 4}
    assert result["difference_a_b"] == {1, 2}
    assert result["union"] == {1, 2, 3, 4, 5, 6}


def test_upgrade_plan_features():
    """Tests adding new features to a base set."""
    base = {"reporting", "export"}
    new_features = ["api_access", "priority_support"]

    upgraded = upgrade_plan_features(base, new_features)

    assert upgraded == {"reporting", "export", "api_access", "priority_support"}
    # Ensure the original set was not modified
    assert base == {"reporting", "export"}
