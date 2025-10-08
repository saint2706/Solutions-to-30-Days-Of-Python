"""Exports for phase03 machine learning."""
from importlib import import_module
from typing import Any

__all__ = [
    "day38_linear_algebra",
    "day39_calculus",
    "day40_intro_to_ml",
    "day41_supervised_learning_regression",
    "day42_supervised_learning_classification_part_1",
    "day43_supervised_learning_classification_part_2",
    "day44_unsupervised_learning",
    "day45_feature_engineering_and_evaluation",
    "day46_intro_to_neural_networks",
    "day47_convolutional_neural_networks",
    "day48_recurrent_neural_networks",
    "day49_nlp",
    "day50_mlops",
    "day51_regularized_models",
    "day52_ensemble_methods",
    "day53_model_tuning_and_feature_selection",
    "day54_probabilistic_modeling",
    "day55_advanced_unsupervised_learning",
    "day56_time_series_and_forecasting",
    "day57_recommender_systems",
    "day58_transformers_and_attention",
    "day59_generative_models",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - thin forwarding shim
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
