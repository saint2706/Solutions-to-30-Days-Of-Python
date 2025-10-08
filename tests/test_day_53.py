"""Tests for Day 53 tuning and feature selection."""

from __future__ import annotations

from Day_53_Model_Tuning_and_Feature_Selection.solutions import (
    compute_permutation_importance,
    evaluate_selected_features,
    generate_tuning_dataset,
    run_bayesian_optimisation,
    run_grid_search,
    run_recursive_feature_elimination,
)


def test_grid_and_bayesian_search_find_high_auc_solutions() -> None:
    X, y = generate_tuning_dataset(random_state=11)
    grid = run_grid_search(X, y, cv=4, random_state=11)
    bayes = run_bayesian_optimisation(X, y, n_iter=12, cv=4, random_state=11)
    assert grid.best_score > 0.85
    assert bayes.best_score > 0.85
    assert set(grid.best_params.keys()) == {
        "logisticregression__C",
        "logisticregression__penalty",
    }


def test_feature_selection_and_permutation_importance_agree_on_signal() -> None:
    X, y = generate_tuning_dataset(random_state=17)
    grid = run_grid_search(X, y, cv=3, random_state=17)
    best_estimator = grid.search.best_estimator_
    permutation_df = compute_permutation_importance(best_estimator, X, y)
    selector, support = run_recursive_feature_elimination(
        X, y, n_features_to_select=5, random_state=17
    )
    selected_score = evaluate_selected_features(selector, X, y, cv=3)

    assert permutation_df["importance_mean"].is_monotonic_decreasing
    assert support.sum() == 5
    assert selected_score > 0.85
