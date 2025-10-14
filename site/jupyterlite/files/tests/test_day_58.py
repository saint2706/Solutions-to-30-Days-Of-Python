"""Tests for Day 58 transformer utilities."""

from __future__ import annotations

import numpy as np
import pytest

from Day_58_Transformers_and_Attention import solutions as day58


def test_tiny_transformer_predictions_are_deterministic() -> None:
    classifier = day58.TinyTransformerClassifier()
    text = "great product and amazing support"
    negative_text = "terrible slow service"
    probs_once = classifier.predict_proba(text)
    probs_twice = day58.TinyTransformerClassifier().predict_proba(text)
    for label, value in probs_once.items():
        assert value == pytest.approx(probs_twice[label])
    negative_probs = classifier.predict_proba(negative_text)
    assert negative_probs["negative"] > negative_probs["positive"]


def test_attention_heatmap_rows_sum_to_one() -> None:
    classifier = day58.TinyTransformerClassifier()
    heatmap = classifier.attention_heatmap("great product and amazing support")
    row_sums = heatmap.sum(axis=1)
    assert np.allclose(row_sums, np.ones_like(row_sums), atol=1e-6)
