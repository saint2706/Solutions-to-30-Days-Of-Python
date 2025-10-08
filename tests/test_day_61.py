"""Tests for Day 61 reinforcement learning helpers."""

from __future__ import annotations

import numpy as np

from Day_61_Reinforcement_and_Offline_Learning import solutions as day61


def test_policy_gradient_converges_with_seed() -> None:
    log = day61.run_policy_gradient_bandit(random_state=61)
    assert log.moving_average[-1] > 1.0
    assert log.policy_parameter > 2.0


def test_q_learning_and_bandit_rewards_hit_thresholds() -> None:
    q_result = day61.run_q_learning(random_state=61)
    assert np.mean(q_result.rewards[-20:]) > 0.65
    bandit = day61.run_contextual_bandit(random_state=61)
    assert bandit.average_reward > 0.95


def test_offline_evaluation_reports_stable_estimate() -> None:
    offline = day61.offline_evaluation(random_state=61)
    assert offline["estimate"] > 0.75
    assert offline["effective_sample_size"] > 50
