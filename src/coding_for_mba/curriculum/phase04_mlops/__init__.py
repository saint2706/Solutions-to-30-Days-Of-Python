"""Exports for phase04 mlops."""
from importlib import import_module
from typing import Any

__all__ = [
    "day60_graph_and_geometric_learning",
    "day61_reinforcement_and_offline_learning",
    "day62_model_interpretability_and_fairness",
    "day63_causal_inference_and_uplift",
    "day64_modern_nlp_pipelines",
    "day65_mlops_pipelines_and_ci",
    "day66_model_deployment_and_serving",
    "day67_model_monitoring_and_reliability",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - thin forwarding shim
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
