import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(Path(__file__).resolve().parents[1]))

from Day_67_Model_Monitoring_and_Reliability import solutions  # noqa: E402


def test_compute_mean_drift_triggers_on_shift():
    baseline = [0.1, 0.15, 0.2]
    current = [0.5, 0.55, 0.6]
    report = solutions.compute_mean_drift(baseline, current, threshold=0.5)
    assert report.triggered is True
    assert report.drift_score >= 0.5


def test_canary_verdict_blocks_high_latency():
    baseline_metrics = {"latency": 0.2, "accuracy": 0.85, "error_rate": 0.05}
    candidate_metrics = {"latency": 0.4, "accuracy": 0.86, "error_rate": 0.05}
    verdict = solutions.evaluate_canary(baseline_metrics, candidate_metrics, allowed_latency_delta=0.15)
    assert verdict.promote is False
    assert verdict.reason == "Latency regression"


def test_enqueue_retraining_respects_accuracy_drop():
    reports = solutions.detect_drift_across_features(
        {"feat_a": [0.1, 0.2, 0.3]},
        {"feat_a": [0.12, 0.22, 0.32]},
        threshold=10.0,
    )
    queue = solutions.enqueue_retraining_tasks(reports, accuracy=0.7, latency=0.2)
    assert queue == ["feat_a"]


def test_observability_snapshot_contains_metrics():
    report = solutions.DriftReport("feat_a", 0.1, 0.3, 1.2, True)
    verdict = solutions.CanaryVerdict(False, "Accuracy below threshold", {"accuracy": 0.7})
    snapshot = solutions.build_observability_snapshot(report, verdict, predictions_served=42)
    assert snapshot["drift"]["triggered"] is True
    assert snapshot["canary"]["promote"] is False
    assert snapshot["counters"]["predictions_served_total"] == 42
