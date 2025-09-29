import importlib.util
import sys
from pathlib import Path

import pytest


def _load_module():
    module_path = (
        Path(__file__).resolve().parents[1]
        / "Day_42_Supervised_Learning_Classification_Part_1"
        / "solutions.py"
    )
    spec = importlib.util.spec_from_file_location("day_42_part_1_solutions", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sol = _load_module()


def test_load_and_prepare_iris_shapes():
    data = sol.load_and_prepare_iris()
    assert data.X_train.shape[0] == data.y_train.shape[0]
    assert data.X_test.shape[0] == data.y_test.shape[0]
    assert data.X_train_scaled.shape == data.X_train.shape
    assert data.X_test_scaled.shape == data.X_test.shape


def test_classification_metrics():
    data = sol.load_and_prepare_iris()
    log_reg = sol.train_logistic_regression(data.X_train_scaled, data.y_train)
    knn = sol.train_knn_classifier(data.X_train_scaled, data.y_train)
    log_metrics = sol.evaluate_classifier(log_reg, data.X_test_scaled, data.y_test)
    knn_metrics = sol.evaluate_classifier(knn, data.X_test_scaled, data.y_test)
    assert log_metrics["accuracy"] == pytest.approx(0.9111111111111111)
    assert knn_metrics["accuracy"] == pytest.approx(0.9111111111111111)


def test_demo_returns_metrics():
    metrics = sol.run_classification_demo()
    assert set(metrics) == {"logistic_regression", "knn"}
