"""VAR and order-invariant generalized forecast-error variance decomposition."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR


@dataclass
class FevdResult:
    horizon: int
    table: pd.DataFrame
    lag_order: int
    n: int
    stable: bool
    row_sum_max_error: float
    method: str


def select_lag(df: pd.DataFrame, maxlags: int = 5) -> int:
    selected = VAR(df).select_order(maxlags=maxlags).bic
    return int(selected) if selected is not None else 1


def fit_var_fevd(
    df: pd.DataFrame,
    horizon: int = 10,
    maxlags: int = 5,
) -> FevdResult:
    """Fit a VAR and compute Pesaran-Shin generalized FEVD."""

    clean = df.dropna().copy()
    lag_order = max(1, select_lag(clean, maxlags=maxlags))
    result = VAR(clean).fit(lag_order)
    sigma = np.asarray(result.sigma_u)
    moving_average = result.ma_rep(maxn=horizon - 1)
    variables = sigma.shape[0]
    decomposition = np.zeros((variables, variables), dtype=float)
    denominator = np.zeros(variables, dtype=float)
    for impact in moving_average:
        impact_sigma = impact @ sigma
        denominator += np.diag(impact_sigma @ impact.T)
        for shock in range(variables):
            decomposition[:, shock] += impact_sigma[:, shock] ** 2 / sigma[shock, shock]
    decomposition = decomposition / denominator[:, None]
    decomposition = decomposition / decomposition.sum(axis=1, keepdims=True)
    table = pd.DataFrame(decomposition, index=clean.columns, columns=clean.columns)
    table.index.name = "from"
    table.columns.name = "to"
    return FevdResult(
        horizon=horizon,
        table=table,
        lag_order=lag_order,
        n=len(clean),
        stable=bool(result.is_stable()),
        row_sum_max_error=float(np.abs(table.sum(axis=1) - 1).max()),
        method="Pesaran-Shin generalized FEVD",
    )


def connectedness_index(fevd: FevdResult) -> float:
    """Diebold-Yilmaz total connectedness index, from zero to 100."""

    table = fevd.table.to_numpy()
    off_diagonal = table.sum() - np.trace(table)
    return float(100.0 * off_diagonal / table.shape[0])


__all__ = ["FevdResult", "connectedness_index", "fit_var_fevd", "select_lag"]
