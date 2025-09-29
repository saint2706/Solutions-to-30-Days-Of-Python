import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_45_Feature_Engineering_and_Evaluation.solutions import (  # noqa: E402
    create_sample_dataframe,
    evaluate_model,
    preprocess_dataframe,
)


def test_preprocess_dataframe_returns_expected_shape_and_features():
    df = create_sample_dataframe()

    processed, target, preprocessor = preprocess_dataframe(df)

    assert processed.shape == (7, 6)
    assert target.tolist() == [0, 1, 0, 1, 1, 0, 1]
    expected_features = [
        "num__age",
        "num__salary",
        "cat__city_London",
        "cat__city_New York",
        "cat__city_Paris",
        "cat__city_Tokyo",
    ]
    assert preprocessor.get_feature_names_out().tolist() == expected_features


def test_evaluate_model_returns_expected_confusion_matrix():
    df = create_sample_dataframe()

    pipeline, metrics = evaluate_model(df, test_size=0.3, random_state=42)

    assert "preprocess" in pipeline.named_steps
    np.testing.assert_array_equal(metrics["confusion_matrix"], np.array([[1, 1], [0, 1]]))
    assert "precision" in metrics["classification_report"].lower()
