"""Expanding-window walk-forward folds. Train always strictly precedes test."""
from collections.abc import Iterator
from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class Fold:
    train_start: pd.Timestamp
    train_end: pd.Timestamp  # exclusive
    test_start: pd.Timestamp  # inclusive
    test_end: pd.Timestamp  # exclusive


def make_folds(
    index: pd.DatetimeIndex,
    initial_train_days: int,
    test_days: int,
    step_days: int | None = None,
    gap_days: int = 0,
    final_holdout_days: int = 0,
) -> Iterator[Fold]:
    """Yield expanding-window folds, leaving `final_holdout_days` untouched at the end."""
    step = step_days or test_days
    start = index.min()
    usable_end = index.max() - pd.Timedelta(days=final_holdout_days)
    train_end = start + pd.Timedelta(days=initial_train_days)
    while True:
        test_start = train_end + pd.Timedelta(days=gap_days)
        test_end = test_start + pd.Timedelta(days=test_days)
        if test_end > usable_end:
            return
        yield Fold(start, train_end, test_start, test_end)
        train_end = train_end + pd.Timedelta(days=step)
