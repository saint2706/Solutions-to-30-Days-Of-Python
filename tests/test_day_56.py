"""Smoke tests for Day 56 time-series helpers."""

from __future__ import annotations

import numpy as np

from Day_56_Time_Series_and_Forecasting import solutions as day56


def test_arima_and_sarimax_forecasts_are_reasonable() -> None:
    series = day56.generate_seasonal_series(random_state=23)
    train, test = day56.train_test_split_series(series, test_size=12)

    arima_result = day56.fit_arima_forecast(train, steps=len(test))
    sarimax_result = day56.fit_sarimax_forecast(train, steps=len(test))

    assert len(arima_result.forecast) == len(test)
    assert len(sarimax_result.forecast) == len(test)

    arima_metrics = day56.forecast_metrics(test.values, arima_result.forecast.values)
    sarimax_metrics = day56.forecast_metrics(
        test.values, sarimax_result.forecast.values
    )

    assert arima_metrics["rmse"] < 3.5
    assert sarimax_metrics["mae"] < 0.8


def test_prophet_style_forecast_tracks_seasonality() -> None:
    series = day56.generate_seasonal_series(random_state=42)
    train, test = day56.train_test_split_series(series, test_size=12)
    forecast = day56.prophet_style_forecast(train, steps=len(test))
    metrics = day56.forecast_metrics(test.values, forecast.forecast.values)
    assert metrics["smape"] < 3.0


def test_rolling_origin_backtest_runs_without_error() -> None:
    series = day56.generate_seasonal_series(random_state=19)
    backtest = day56.rolling_origin_backtest(
        series,
        initial_train_size=72,
        horizon=6,
        model_builder=lambda train_series, steps: day56.fit_sarimax_forecast(
            train_series, steps=steps
        ),
    )
    assert {"mae", "rmse", "mape", "smape", "start"}.issubset(backtest.columns)
    assert float(np.mean(backtest["mae"])) < 1.5
    assert len(backtest) > 5
