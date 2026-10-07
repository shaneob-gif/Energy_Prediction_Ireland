# Irish Electricity Demand Forecast

Day-ahead demand forecasting for Ireland using EirGrid and weather data, with regime
clustering, per-cluster models, and leakage-safe walk-forward validation.

> Status: scaffold. Results table, method and limitations to be added as the project progresses.

## Goals
- Beat naive and (where available) EirGrid's own published forecast under honest validation.
- Quantify which feature groups actually help (ablation).
- Test whether regime clustering and per-cluster models improve on a global model.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
make install
make test
```

## Layout
See `config/config.yaml` for all experiment settings. Each feature group is its own
module with a config toggle. Clustering is fit inside each walk-forward fold.

## Results
_TBD_

## Limitations
_TBD (e.g. weather actuals vs forecasts, structural breaks, data-centre growth)_
