"""Regression tests for the Day 50 MLOps helpers."""

import os
import sys
from pathlib import Path

import numpy as np
import pytest
from sklearn.metrics import accuracy_score

sys.path.insert(0, os.path.abspath(Path(__file__).resolve().parents[1]))

from Day_50_MLOps.solutions import (  # noqa: E402
    load_model,
    predict_sample,
    save_model,
    train_iris_model,
)


def test_model_round_trip(tmp_path: Path) -> None:
    model, accuracy, X_test, y_test, target_names = train_iris_model(
        random_state=123, subset_size=90
    )

    baseline_predictions = model.predict(X_test)

    model_path = save_model(model, tmp_path / "iris_model.joblib")
    assert model_path.exists()

    reloaded_model = load_model(model_path)
    reloaded_predictions = reloaded_model.predict(X_test)
    reloaded_accuracy = accuracy_score(y_test, reloaded_predictions)

    assert accuracy == pytest.approx(reloaded_accuracy)
    np.testing.assert_array_equal(baseline_predictions, reloaded_predictions)

    predicted_index, predicted_label = predict_sample(
        reloaded_model, X_test[0], target_names
    )
    assert predicted_index == baseline_predictions[0]
    assert predicted_label == target_names[baseline_predictions[0]]
