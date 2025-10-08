"""Tests for Day 54 probabilistic modelling utilities."""

from __future__ import annotations

import numpy as np
import pytest

from Day_54_Probabilistic_Modeling import solutions as day54


@pytest.fixture(scope="module")
def gaussian_dataset() -> tuple[np.ndarray, np.ndarray]:
    return day54.generate_probabilistic_dataset(n_samples=320, random_state=7)


def test_gaussian_mixture_log_likelihood_is_reproducible(gaussian_dataset) -> None:
    X, _ = gaussian_dataset
    model = day54.fit_gaussian_mixture(X, n_components=2, random_state=7)
    log_like = day54.mixture_log_likelihood(model, X)
    assert log_like == pytest.approx(-938.4860, rel=1e-3)


def test_expectation_maximisation_returns_strong_lower_bound(gaussian_dataset) -> None:
    X, _ = gaussian_dataset
    _, lower_bound = day54.run_expectation_maximisation(
        X, n_components=2, random_state=7
    )
    assert lower_bound == pytest.approx(-2.93277, rel=1e-4)


def test_bayesian_posteriors_normalise_to_one(gaussian_dataset) -> None:
    X, y = gaussian_dataset
    model = day54.train_bayesian_classifier(X, y)
    log_post = day54.bayesian_log_posterior(model, X[:8])
    probs = np.exp(log_post)
    assert np.allclose(probs.sum(axis=1), 1.0, atol=1e-6)


def test_hidden_markov_log_likelihood_matches_expected() -> None:
    hmm = day54.build_demo_hmm(random_state=7)
    observations = np.array([[0.2], [-0.3], [2.6], [3.3], [2.9]])
    log_like = day54.hmm_log_likelihood(hmm, observations)
    assert log_like == pytest.approx(-6.69642, rel=1e-5)
