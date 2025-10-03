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

    expected_y_test = np.array(
        [0, 0, 0, 0, 0, 0, 2, 1, 1, 2, 2, 2, 2, 1, 0, 1, 1, 2]
    )
    expected_X_test = np.array(
        [
            [5.0, 3.5, 1.6, 0.6],
            [5.0, 3.4, 1.6, 0.4],
            [5.0, 3.2, 1.2, 0.2],
            [5.4, 3.4, 1.7, 0.2],
            [4.4, 2.9, 1.4, 0.2],
            [4.8, 3.0, 1.4, 0.3],
            [5.8, 2.7, 5.1, 1.9],
            [5.7, 3.0, 4.2, 1.2],
            [5.0, 2.3, 3.3, 1.0],
            [6.5, 3.2, 5.1, 2.0],
            [7.9, 3.8, 6.4, 2.0],
            [6.5, 3.0, 5.8, 2.2],
            [6.3, 3.3, 6.0, 2.5],
            [5.0, 2.0, 3.5, 1.0],
            [4.4, 3.0, 1.3, 0.2],
            [6.7, 3.1, 4.4, 1.4],
            [5.5, 2.4, 3.8, 1.1],
            [5.8, 2.7, 5.1, 1.9],
        ]
    )

    np.testing.assert_array_equal(y_test, expected_y_test)
    np.testing.assert_allclose(X_test, expected_X_test)

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


def test_save_model_creates_nested_directory(tmp_path: Path) -> None:
    model, *_ = train_iris_model(random_state=123, subset_size=60)

    nested_path = tmp_path / "models" / "iris.joblib"
    saved_path = save_model(model, nested_path)

    assert saved_path == nested_path.resolve()
    assert saved_path.exists()
    assert saved_path.parent.is_dir()
