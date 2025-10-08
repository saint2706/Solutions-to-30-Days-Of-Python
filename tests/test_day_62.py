import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_62_Model_Interpretability_and_Fairness import solutions as day62


def _encode_row(row):
    return np.array(
        [row["credit_score"], row["income"], float(row["gender"] == "F")], dtype=float
    )


def test_shap_values_sum_to_prediction():
    model = day62.train_default_risk_model()
    dataset = day62.load_credit_dataset()
    row = dataset.iloc[3]
    features = _encode_row(row)
    shap = day62.compute_shap_values(model, features, dataset)
    prediction = model.predict(features)
    assert math.isclose(shap.reconstructed_prediction(), prediction, rel_tol=1e-9)


def test_lime_local_prediction_matches_model():
    model = day62.train_default_risk_model()
    dataset = day62.load_credit_dataset()
    row = dataset.iloc[10]
    features = _encode_row(row)
    lime = day62.lime_explanation(model, features, num_samples=300, random_state=42)
    local_prediction = lime.local_prediction(features)
    model_prediction = model.predict(features)
    assert math.isclose(local_prediction, model_prediction, rel_tol=0.05)


def test_counterfactual_moves_prediction_towards_target():
    model = day62.train_default_risk_model()
    dataset = day62.load_credit_dataset()
    row = dataset.iloc[5]
    features = _encode_row(row)
    target = 0.05
    bounds = {
        "credit_score": (520, 800),
        "income": (35_000, 110_000),
        "is_female": (0.0, 1.0),
    }
    result = day62.generate_counterfactual(
        model, features, target=target, bounds=bounds
    )
    assert abs(result.counterfactual_prediction - target) < abs(
        result.original_prediction - target
    )
    assert np.all(result.counterfactual_features >= np.array([520, 35_000, 0.0]))
    assert np.all(result.counterfactual_features <= np.array([800, 110_000, 1.0]))


def test_fairness_mitigation_reduces_gap():
    dataset = day62.load_credit_dataset()
    baseline = day62.fairness_metrics(dataset)
    mitigated = day62.mitigation_effect(dataset)
    assert abs(mitigated.statistical_parity) < abs(baseline.statistical_parity)
    assert mitigated.disparate_impact >= baseline.disparate_impact - 1e-6
