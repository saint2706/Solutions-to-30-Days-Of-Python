"""Tests for Day 52 ensemble methods."""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

from Day_52_Ensemble_Methods.solutions import (
    export_feature_importance,
    generate_classification_data,
    train_random_forest,
)


def test_random_forest_oob_score_aligns_with_cross_validation() -> None:
    X, y = generate_classification_data(random_state=7)
    rf = train_random_forest(X, y, n_estimators=300, random_state=7)

    baseline = RandomForestClassifier(
        n_estimators=300,
        random_state=7,
        n_jobs=-1,
    )
    cv_scores = cross_val_score(baseline, X, y, cv=5, scoring="accuracy")
    assert abs(rf.oob_score_ - float(np.mean(cv_scores))) < 0.05


def test_feature_importance_export_preserves_importance_mass(tmp_path) -> None:
    X, y = generate_classification_data(random_state=9)
    rf = train_random_forest(X, y, random_state=9)
    feature_names = [f"f{i}" for i in range(X.shape[1])]
    output_file = tmp_path / "importances.csv"

    df = export_feature_importance(rf, feature_names, output_file)
    assert np.isclose(df["importance"].sum(), 1.0)
    assert set(df["feature"]) == set(feature_names)
    reloaded = export_feature_importance(rf, feature_names)
    assert df.equals(reloaded)
    assert output_file.exists()
