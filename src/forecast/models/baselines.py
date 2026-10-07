"""Naive baselines every model must beat."""
import pandas as pd


def same_hour_last_week(demand: pd.Series) -> pd.Series:
    """Forecast = demand at the same time 7 days earlier. Needs a DatetimeIndex."""
    return demand.shift(freq="7D").reindex(demand.index)


def same_hour_yesterday(demand: pd.Series) -> pd.Series:
    return demand.shift(freq="1D").reindex(demand.index)
