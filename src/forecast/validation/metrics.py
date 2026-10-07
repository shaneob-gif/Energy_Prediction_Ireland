"""Forecast error metrics."""
import numpy as np
import pandas as pd


def mae(y_true, y_pred) -> float:
    return float(np.nanmean(np.abs(np.asarray(y_true) - np.asarray(y_pred))))


def mape(y_true, y_pred) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    mask = y_true != 0
    return float(np.nanmean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)


def peak_error(y_true: pd.Series, y_pred: pd.Series) -> float:
    """Mean absolute error of the daily peak (a key quantity for grid operators)."""
    t = y_true.resample("D").max()
    p = y_pred.resample("D").max()
    return mae(t, p)


def by_group(y_true: pd.Series, y_pred: pd.Series, groups: pd.Series) -> pd.DataFrame:
    """MAE/MAPE per group (e.g. season, cluster, peak vs off-peak)."""
    rows = {
        g: {"mae": mae(y_true[idx], y_pred[idx]), "mape": mape(y_true[idx], y_pred[idx]), "n": len(idx)}
        for g, idx in y_true.groupby(groups).groups.items()
    }
    return pd.DataFrame(rows).T
