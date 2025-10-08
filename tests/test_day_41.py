import pytest
from importlib import import_module


sol = import_module("Day_41_Supervised_Learning_Regression.solutions")


@pytest.fixture()
def regression_workflow():
    X, y = sol.generate_regression_data()
    X_train, X_test, y_train, y_test = sol.split_regression_data(X, y)
    model = sol.train_regression_model(X_train, y_train)
    y_pred = sol.make_regression_predictions(model, X_test)
    metrics = sol.evaluate_regression_model(y_test, y_pred)
    return X_test, y_test, y_pred, metrics


def test_regression_metrics(regression_workflow):
    _, _, _, metrics = regression_workflow
    assert metrics["mse"] == pytest.approx(0.8587423292571856)
    assert metrics["r2"] == pytest.approx(0.6564550820484416)


def test_regression_plot_creation(tmp_path, regression_workflow):
    X_test, y_test, y_pred, _ = regression_workflow
    fig, output_path = sol.plot_regression_results(
        X_test, y_test, y_pred, tmp_path / "plot.png"
    )
    try:
        assert output_path.exists()
        assert fig.axes
    finally:
        import matplotlib.pyplot as plt

        plt.close(fig)


def test_demo_returns_metrics(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    metrics = sol.run_linear_regression_demo()
    assert set(metrics) == {"mse", "r2"}
    assert (tmp_path / "regression_fit.png").exists()
