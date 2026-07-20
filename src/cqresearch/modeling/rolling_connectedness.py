"""Rolling VAR/FEVD connectedness diagnostics."""

from __future__ import annotations

import pandas as pd

from cqresearch.modeling.var_fevd import connectedness_index, fit_var_fevd


def rolling_fevd_connectedness(
    df: pd.DataFrame,
    window: int = 252,
    step: int = 30,
    horizon: int = 10,
    maxlags: int = 5,
) -> pd.DataFrame:
    """Compute rolling Diebold-Yilmaz-style connectedness with stepped windows."""

    clean = df.dropna()
    rows: list[dict[str, object]] = []
    for end in range(window - 1, len(clean), step):
        chunk = clean.iloc[end - window + 1 : end + 1].reset_index(drop=True)
        try:
            fevd = fit_var_fevd(chunk, horizon=horizon, maxlags=maxlags)
            rows.append(
                {
                    "date": clean.index[end],
                    "window": window,
                    "step": step,
                    "horizon": horizon,
                    "connectedness_pct": connectedness_index(fevd),
                    "lag_order": fevd.lag_order,
                    "n": fevd.n,
                    "stable": fevd.stable,
                    "row_sum_max_error": fevd.row_sum_max_error,
                    "method": fevd.method,
                    "error": "",
                }
            )
        except Exception as exc:
            rows.append(
                {
                    "date": clean.index[end],
                    "window": window,
                    "step": step,
                    "horizon": horizon,
                    "connectedness_pct": float("nan"),
                    "lag_order": float("nan"),
                    "n": len(chunk),
                    "stable": False,
                    "row_sum_max_error": float("nan"),
                    "method": "Pesaran-Shin generalized FEVD",
                    "error": str(exc),
                }
            )
    return pd.DataFrame(rows)


def connectedness_by_regime(connectedness: pd.DataFrame, split_date: pd.Timestamp) -> pd.DataFrame:
    """Summarize rolling connectedness before and after ``split_date``."""

    out = connectedness.copy()
    out["regime"] = ["pre" if pd.Timestamp(d) < split_date else "post" for d in out["date"]]
    return (
        out.groupby("regime")["connectedness_pct"]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
    )


__all__ = ["connectedness_by_regime", "rolling_fevd_connectedness"]
