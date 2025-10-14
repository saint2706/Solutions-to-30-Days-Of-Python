import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(Path(__file__).resolve().parents[1]))

from Day_65_MLOps_Pipelines_and_CI import solutions  # noqa: E402


def test_pipeline_executes_in_topological_order():
    raw_rows = [
        {"entity_id": 1, "feature_value": 0.4},
        {"entity_id": 2, "feature_value": 0.6},
    ]
    dag = solutions.build_mlops_pipeline(raw_rows)
    context = getattr(dag, "base_context", {})
    results = dag.execute(context)
    assert results["execution_order"] == [
        "feature_store",
        "model_training",
        "model_registry",
        "deployment",
    ]


def test_pipeline_produces_registry_and_deployment_status():
    raw_rows = [
        {"entity_id": "user-1", "feature_value": 0.55},
        {"entity_id": "user-2", "feature_value": 0.45},
    ]
    results = solutions.run_pipeline(raw_rows)
    registry_entry = results["model_registry"]
    assert registry_entry["name"] == "churn_model"
    assert registry_entry["stage"] == "Staging"
    deployment_status = results["deployment"]
    assert deployment_status["status"] in {"success", "failed"}
    assert "environment" in deployment_status or "reason" in deployment_status


def test_feature_store_upsert_overwrites_duplicates():
    rows = [
        {"entity_id": 1, "feature_value": 0.1},
        {"entity_id": 1, "feature_value": 0.9},
    ]
    store = solutions.upsert_feature_store(rows)
    assert len(store) == 1
    assert store["1"]["feature_value"] == 0.9
