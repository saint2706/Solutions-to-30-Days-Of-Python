"""Tests for Day 60 graph learning helpers."""

from __future__ import annotations

import numpy as np

from Day_60_Graph_and_Geometric_Learning import solutions as day60


def test_graph_models_reach_high_accuracy() -> None:
    results = day60.train_node_classifiers(random_state=60)
    assert results["graphsage_accuracy"] >= 0.95
    assert results["gat_accuracy"] >= 0.95
    attention = results["attention_matrix"]
    assert np.all(attention >= 0)
    row_sums = attention.sum(axis=1)
    assert np.allclose(row_sums, np.ones_like(row_sums), atol=1e-6)
