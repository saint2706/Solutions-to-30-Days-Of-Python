"""Tests for Day 55 advanced unsupervised learning helpers."""

from __future__ import annotations

import numpy as np
from sklearn.preprocessing import StandardScaler

from Day_55_Advanced_Unsupervised_Learning import solutions as day55


def test_dbscan_recovers_three_clusters() -> None:
    X, _ = day55.generate_clustering_data(random_state=13)
    result = day55.run_dbscan(X, eps=0.65, min_samples=6)
    labels = result.labels
    clusters = {label for label in labels if label != -1}
    assert clusters == {0, 1, 2}
    assert int(np.sum(labels == -1)) <= 3


def test_agglomerative_cluster_sizes_are_balanced() -> None:
    X, _ = day55.generate_clustering_data(random_state=13)
    result = day55.run_agglomerative(X, n_clusters=3)
    counts = np.bincount(result.labels)
    assert counts.tolist() == [150, 150, 150]


def test_tsne_preserves_pairwise_structure() -> None:
    X, _ = day55.generate_clustering_data(random_state=13)
    embedding = day55.compute_tsne_embedding(X, random_state=13, perplexity=35)
    corr = day55.tsne_distance_preservation(X, embedding)
    assert corr > 0.75


def test_autoencoder_flags_outliers_via_reconstruction_error() -> None:
    X, _ = day55.generate_clustering_data(random_state=13)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    auto = day55.build_autoencoder(input_dim=X_scaled.shape[1], random_state=13)
    day55.train_autoencoder(auto, X_scaled, epochs=50)
    train_errors = day55.reconstruction_errors(auto, X_scaled)
    threshold = day55.autoencoder_anomaly_threshold(train_errors, 0.95)
    anomalies = np.array([[7.5, 7.5], [-7.0, 2.0], [0.0, 8.0]])
    anomaly_errors = day55.reconstruction_errors(auto, scaler.transform(anomalies))
    assert float(anomaly_errors.mean()) > threshold * 10
    mask = day55.detect_anomalies_with_autoencoder(auto, scaler.transform(anomalies), threshold)
    assert mask.tolist() == [0, 1, 1]


def test_density_based_anomaly_scores_rank_inserted_points() -> None:
    X, _ = day55.generate_clustering_data(random_state=13)
    anomalies = np.array([[7.5, 7.5], [-7.0, 2.0], [0.0, 8.0]])
    combined = np.vstack([X, anomalies])
    lof_scores, lof_labels = day55.lof_anomaly_scores(combined)
    assert lof_labels[-3:].tolist() == [-1, -1, -1]

    iso_scores = day55.isolation_forest_scores(combined, contamination=0.05, random_state=13)
    top_indices = np.argsort(iso_scores)[-3:]
    assert set(top_indices.tolist()) == {450, 451, 452}
