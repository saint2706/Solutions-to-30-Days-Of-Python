"""Exports for phase02 data tooling."""
from importlib import import_module
from typing import Any

__all__ = [
    "day22_numpy",
    "day23_pandas",
    "day24_pandas_advanced",
    "day25_data_cleaning",
    "day26_statistics",
    "day27_visualization",
    "day28_advanced_visualization",
    "day29_interactive_visualization",
    "day30_web_scraping",
    "day31_databases",
    "day32_other_databases",
    "day33_api",
    "day34_building_an_api",
    "day35_flask_web_framework",
    "day36_case_study",
    "day37_conclusion",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - thin forwarding shim
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
