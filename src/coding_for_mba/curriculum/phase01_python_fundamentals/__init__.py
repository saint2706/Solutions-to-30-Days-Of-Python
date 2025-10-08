"""Exports for phase01 python fundamentals."""
from importlib import import_module
from typing import Any

__all__ = [
    "day01_introduction",
    "day02_variables_builtin_functions",
    "day03_operators",
    "day04_strings",
    "day05_lists",
    "day06_tuples",
    "day07_sets",
    "day08_dictionaries",
    "day09_conditionals",
    "day10_loops",
    "day11_functions",
    "day12_list_comprehension",
    "day13_higher_order_functions",
    "day14_modules",
    "day15_exception_handling",
    "day16_file_handling",
    "day17_regular_expressions",
    "day18_classes_and_objects",
    "day19_python_date_time",
    "day20_python_package_manager",
    "day21_virtual_environments",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - thin forwarding shim
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
