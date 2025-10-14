import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Day_44_Unsupervised_Learning.solutions import (  # noqa: E402
    fit_kmeans,
    generate_blobs,
    load_iris_data,
    run_pca,
)


def test_generate_blobs_produces_expected_shapes():
    X, y = generate_blobs(n_samples=120, centers=3, random_state=0)

    assert X.shape == (120, 2)
    assert y.shape == (120,)
    assert len(np.unique(y)) == 3


def test_fit_kmeans_returns_cluster_centers_with_expected_shape():
    X, _ = generate_blobs(n_samples=150, centers=3, random_state=1)

    _, labels, centers = fit_kmeans(X, n_clusters=3, random_state=1)

    assert centers.shape == (3, X.shape[1])
    assert len(np.unique(labels)) == 3


def test_run_pca_returns_expected_variance():
    features, _, _ = load_iris_data()

    transformed, pca_model, scaler = run_pca(features, n_components=2)

    assert transformed.shape == (features.shape[0], 2)
    assert scaler.mean_.shape[0] == features.shape[1]
    assert pytest.approx(pca_model.explained_variance_ratio_.sum(), abs=1e-3) == 0.958
