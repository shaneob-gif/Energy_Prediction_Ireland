import pandas as pd

from forecast.validation.walk_forward import make_folds


def _index():
    return pd.date_range("2018-01-01", "2023-12-31 23:00", freq="h")


def test_train_strictly_precedes_test():
    folds = list(make_folds(_index(), 730, 180, gap_days=1))
    assert folds, "expected at least one fold"
    for f in folds:
        assert f.train_end < f.test_start


def test_holdout_is_never_touched():
    idx = _index()
    holdout_start = idx.max() - pd.Timedelta(days=365)
    for f in make_folds(idx, 730, 180, final_holdout_days=365):
        assert f.test_end <= holdout_start


def test_folds_expand_and_dont_overlap_tests():
    folds = list(make_folds(_index(), 730, 180))
    for a, b in zip(folds, folds[1:]):
        assert b.train_end > a.train_end
        assert b.test_start >= a.test_end
