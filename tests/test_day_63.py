import math
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_63_Causal_Inference_and_Uplift import solutions as day63


def test_effect_estimators_match_ground_truth():
    data = day63.generate_synthetic_treatment_data(random_state=63)
    ab_result = day63.difference_in_means(data)
    propensity_model = day63.fit_propensity_model(data, epochs=800)
    ipw_ate = day63.estimate_ipw_ate(data, propensity_model)
    dml_result = day63.double_machine_learning(data)

    true_effect = data["true_effect"].iloc[0]
    assert math.isclose(ab_result.lift, true_effect, rel_tol=0.35)
    assert math.isclose(ipw_ate, true_effect, rel_tol=0.3)
    assert math.isclose(dml_result.ate, true_effect, rel_tol=0.2)


def test_two_model_uplift_is_positive():
    data = day63.generate_synthetic_treatment_data(random_state=7)
    uplift = day63.two_model_uplift(data)
    assert uplift.uplift > 0
    assert uplift.treatment_response > uplift.control_response
