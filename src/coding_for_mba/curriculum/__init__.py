"""Curriculum phases for Coding for MBA."""

from importlib import import_module
from typing import Any

__all__ = [
    "phase01_python_fundamentals",
    "phase02_data_tooling",
    "phase03_machine_learning",
    "phase04_mlops",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - thin forwarding shim
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
