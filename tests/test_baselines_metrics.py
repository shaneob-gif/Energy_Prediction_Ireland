import numpy as np
import pandas as pd

from forecast.models.baselines import same_hour_last_week
from forecast.validation.metrics import mae, mape


def test_same_hour_last_week_uses_only_past():
    idx = pd.date_range("2024-01-01", periods=24 * 14, freq="h")
    s = pd.Series(np.arange(len(idx), dtype=float), index=idx)
    pred = same_hour_last_week(s)
    assert pred.iloc[: 24 * 7].isna().all()
    assert (pred.iloc[24 * 7 :] == s.iloc[: -24 * 7].values).all()


def test_metrics():
    assert abs(mae([1, 2, 3], [1, 2, 5]) - 2 / 3) < 1e-9
    assert round(mape([100, 200], [110, 180]), 6) == 10.0
