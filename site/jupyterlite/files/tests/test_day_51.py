"""Tests for Day 51 regularised models."""

from __future__ import annotations

import numpy as np

from Day_51_Regularized_Models.solutions import (
    build_regularised_pipeline,
    evaluate_models_with_cv,
    fit_poisson_glm,
    load_synthetic_regression,
    summarise_coefficients,
)


def test_lasso_shrinks_coefficients_and_cross_val_scores_are_recorded() -> None:
    X, y, _ = load_synthetic_regression(random_state=0)
    models = {
        "linear": build_regularised_pipeline("linear"),
        "ridge": build_regularised_pipeline("ridge", alpha=1.0),
        "lasso": build_regularised_pipeline("lasso", alpha=0.05),
    }
    results = evaluate_models_with_cv(models, X, y)
    summary = summarise_coefficients(results)

    assert results["linear"].cv_score < 0.0
    assert results["ridge"].cv_score < 0.0
    assert summary["lasso"]["l1_norm"] < summary["linear"]["l1_norm"]
    assert summary["lasso"]["l2_norm"] < summary["linear"]["l2_norm"]


def test_poisson_glm_deviance_is_small_for_simulated_counts() -> None:
    rng = np.random.default_rng(123)
    X_counts = rng.poisson(4.0, size=(250, 4))
    rate = np.exp(0.35 * X_counts[:, 0] - 0.25 * X_counts[:, 1] + 0.15 * X_counts[:, 2])
    y_counts = rng.poisson(rate)
    _, deviance = fit_poisson_glm(X_counts, y_counts)
    assert deviance < 1.25
