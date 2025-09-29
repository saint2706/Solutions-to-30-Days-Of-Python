"""Utility helpers for profiling functions across the project.

This module provides lightweight wrappers around :mod:`cProfile` and
``timeit`` so that lesson scripts can share consistent profiling
behaviour.  The helpers intentionally keep the public API small and
return rich data structures that make it easy to surface results in
command-line tools or tests.

Example
-------
>>> from mypackage import profiling
>>> def slow_function():
...     return sum(range(1000))
>>> report = profiling.profile_with_cprofile(slow_function)
>>> "sum" in report.text
True

The :func:`profile_with_cprofile` helper returns a :class:`ProfileReport`
dataclass which includes both the raw result of the profiled callable and
the formatted text output from :mod:`pstats`.  :func:`time_callable`
returns a :class:`TimingReport` with summary statistics that can be used
for documentation or quick regressions checks.
"""

from __future__ import annotations

import cProfile
import io
import statistics
import timeit
from dataclasses import dataclass
from typing import Any, Callable, Optional, Tuple

import pstats


CallableType = Callable[..., Any]


@dataclass
class ProfileReport:
    """Container for the results of a :mod:`cProfile` run."""

    result: Any
    stats: pstats.Stats
    text: str


@dataclass
class TimingReport:
    """Summary statistics from a :func:`timeit.Timer.repeat` run."""

    runs: Tuple[float, ...]
    repeat: int
    number: int
    best: float
    average: float

    def format(self) -> str:
        """Return a human readable representation of the timing runs."""

        lines = [
            "Timing summary (seconds)",
            f"  repeats: {self.repeat}",
            f"  per-run calls: {self.number}",
            f"  best: {self.best:.6f}",
            f"  average: {self.average:.6f}",
            "  raw runs: " + ", ".join(f"{run:.6f}" for run in self.runs),
        ]
        return "\n".join(lines)


def profile_with_cprofile(
    func: CallableType,
    *args: Any,
    sort_by: str = "cumulative",
    print_top: Optional[int] = 30,
    **kwargs: Any,
) -> ProfileReport:
    """Profile ``func`` with :mod:`cProfile` and return a report.

    Parameters
    ----------
    func:
        The callable to profile.
    *args, **kwargs:
        Arguments forwarded to the callable.
    sort_by:
        Field name recognised by :meth:`pstats.Stats.sort_stats`.
    print_top:
        When provided, only the top ``n`` lines will be printed.  ``None``
        disables trimming.
    """

    profiler = cProfile.Profile()
    result = profiler.runcall(func, *args, **kwargs)

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).strip_dirs().sort_stats(sort_by)
    if print_top is None:
        stats.print_stats()
    else:
        stats.print_stats(print_top)
    text = stream.getvalue()
    return ProfileReport(result=result, stats=stats, text=text)


def time_callable(
    func: CallableType,
    *args: Any,
    number: int = 1,
    repeat: int = 5,
    **kwargs: Any,
) -> TimingReport:
    """Benchmark ``func`` using :func:`timeit.Timer.repeat`.

    The callable will be executed ``repeat`` times with ``number``
    invocations per timing run.  Results are returned as a
    :class:`TimingReport` which exposes helpful summary statistics.
    """

    def _target() -> Any:
        return func(*args, **kwargs)

    timer = timeit.Timer(_target)
    runs = tuple(timer.repeat(repeat=repeat, number=number))
    best = min(runs) / number
    average = statistics.fmean(runs) / number
    return TimingReport(
        runs=runs, repeat=repeat, number=number, best=best, average=average
    )


def profile_callable(
    func: CallableType,
    *args: Any,
    mode: str = "cprofile",
    number: int = 1,
    repeat: int = 5,
    **kwargs: Any,
) -> Tuple[Optional[ProfileReport], Optional[TimingReport]]:
    """Convenience helper that dispatches to profiling or timing tools.

    Parameters
    ----------
    mode:
        Either ``"cprofile"`` (default) or ``"timeit"``.  When
        ``"cprofile"`` is used only the :class:`ProfileReport` is
        populated; when ``"timeit"`` only the :class:`TimingReport` is
        returned.
    """

    mode_normalised = mode.lower()
    if mode_normalised == "cprofile":
        return profile_with_cprofile(func, *args, **kwargs), None
    if mode_normalised == "timeit":
        return None, time_callable(func, *args, number=number, repeat=repeat, **kwargs)
    raise ValueError("mode must be either 'cprofile' or 'timeit'")


def print_report(
    profile_report: Optional[ProfileReport] = None,
    timing_report: Optional[TimingReport] = None,
) -> None:
    """Pretty-print any provided reports to ``stdout``.

    The helper keeps CLI scripts tidy by centralising formatting logic in
    one place.
    """

    if profile_report is not None:
        print("\n=== cProfile report ===")
        print(profile_report.text.rstrip())
    if timing_report is not None:
        print("\n=== timeit summary ===")
        print(timing_report.format())
