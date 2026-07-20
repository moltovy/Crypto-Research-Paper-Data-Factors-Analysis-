"""Build actual sample membership and coverage from declared sample rules."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yaml

from cqresearch.core.artifacts import write_csv
from cqresearch.data.contracts import DATA_CUTOFF, resolve_raw_data_root, sample_registry

STABLE_SYMBOLS = {
    "USDT",
    "USDC",
    "DAI",
    "BUSD",
    "FDUSD",
    "TUSD",
    "USDE",
    "USDS",
    "PYUSD",
    "USDP",
    "USDD",
}
WRAPPED_SYMBOLS = {"WBTC", "WETH", "STETH", "WSTETH", "RETH", "WEETH", "WBETH", "CBETH"}


def build_sample_registries(root: Path) -> list[Path]:
    membership = _sample_membership(root)
    definitions = sample_registry(root)
    summaries = []
    for definition in definitions.itertuples(index=False):
        selected = membership[
            membership["sample_id"].eq(definition.sample_id) & membership["included"].eq(True)
        ]
        summaries.append(
            {
                **definition._asdict(),
                "actual_start": selected["first_date"].min() if not selected.empty else "",
                "actual_end": selected["last_date"].max() if not selected.empty else "",
                "constituents": int(selected["asset"].nunique()),
                "membership_rows": int(len(selected)),
                "time_periods": int(selected["period"].replace("", pd.NA).nunique()),
                "observations_total": int(selected["observations"].sum())
                if not selected.empty
                else 0,
                "observations_min": int(selected["observations"].min())
                if not selected.empty
                else 0,
                "observations_max": int(selected["observations"].max())
                if not selected.empty
                else 0,
            }
        )
    return [
        write_csv(root / "research" / "sample_manifest.csv", pd.DataFrame(summaries)),
        write_csv(root / "research" / "sample_membership.csv", membership),
    ]


def stable_core_returns(root: Path) -> pd.DataFrame:
    path = root / "data_local" / "processed" / "binance_spot_daily.parquet"
    if not path.exists():
        raise FileNotFoundError(
            "S2 requires data_local/processed/binance_spot_daily.parquet; "
            "run tools/data_collection/fetch_binance_stable_core.py"
        )
    frame = pd.read_parquet(path)
    frame["date"] = pd.to_datetime(frame["date"])
    membership = _s2_membership(root, frame)
    assets = membership.loc[membership["included"], "asset"].tolist()
    pivot = frame[frame["symbol"].isin(assets)].pivot(
        index="date", columns="symbol", values="close"
    )
    returns = pivot.apply(lambda series: pd.to_numeric(series, errors="coerce")).pipe(
        lambda value: value.where(value > 0)
    )
    returns = returns.apply(lambda series: pd.Series(series).pipe(lambda x: x).transform("log"))
    returns = returns.diff().replace([float("inf"), float("-inf")], pd.NA).astype(float)
    returns.index.name = "date"
    return returns


def _sample_membership(root: Path) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    feature_path = root / "data_local" / "processed" / "feature_store_daily.parquet"
    if feature_path.exists():
        daily = pd.read_parquet(feature_path)
        for asset in ["BTC", "ETH"]:
            column = f"{asset.lower()}_ret"
            valid = daily[column].dropna() if column in daily else pd.Series(dtype=float)
            rows.append(_row("S1", asset, valid, True, "BTC/ETH anchor"))
    binance_path = root / "data_local" / "processed" / "binance_spot_daily.parquet"
    if binance_path.exists():
        binance = pd.read_parquet(binance_path)
        binance["date"] = pd.to_datetime(binance["date"])
        rows.extend(_s2_membership(root, binance).to_dict("records"))
    rows.extend(_s3_membership(root))
    rows.extend(_s4_membership(root))
    rows.extend(_s5_membership(root))
    frame = pd.DataFrame(rows)
    if frame.empty:
        return pd.DataFrame(
            columns=[
                "sample_id",
                "asset",
                "included",
                "reason",
                "first_date",
                "last_date",
                "observations",
                "expected_observations",
                "coverage",
                "period",
            ]
        )
    return frame.sort_values(["sample_id", "included", "asset"], ascending=[True, False, True])


def _s2_membership(root: Path, binance: pd.DataFrame) -> pd.DataFrame:
    pit = _pit(root)
    anchor = pit[pit["snapshot_date"].eq(pd.Timestamp("2021-01-31"))].nsmallest(
        20, "rank_full_market"
    )
    excluded_symbols = _excluded_asset_symbols(root)
    candidates = anchor[~anchor["symbol"].isin(excluded_symbols)].copy()
    rows = []
    expected = len(pd.date_range("2021-01-01", DATA_CUTOFF, freq="D"))
    available = set(binance["symbol"].astype(str))
    for item in candidates.itertuples(index=False):
        asset = str(item.symbol)
        values = binance.loc[
            binance["symbol"].eq(asset)
            & binance["date"].between(pd.Timestamp("2021-01-01"), DATA_CUTOFF),
            ["date", "close"],
        ].dropna()
        coverage = len(values) / expected
        included = asset in available and coverage >= 0.95 and asset != "HYPE"
        reason = (
            "passes PIT, history, coverage, and identity rules"
            if included
            else "fails full-history or coverage rule"
        )
        rows.append(
            _row("S2", asset, values.set_index("date")["close"], included, reason, expected)
        )
    return pd.DataFrame(rows)


def _s3_membership(root: Path) -> list[dict[str, object]]:
    path = (
        resolve_raw_data_root(root)
        / "market_structure"
        / "DefiLlama"
        / "crypto_constituents_daily_ohlcv_top50_current_2020_2026.csv"
    )
    if not path.exists():
        return []
    frame = pd.read_csv(path, parse_dates=["date"])
    pit_symbols = set(_pit(root)["symbol"].dropna().astype(str))
    excluded_symbols = _excluded_asset_symbols(root)
    rows = []
    for asset, group in frame.groupby("symbol"):
        valid = group.dropna(subset=["date", "close_usd"]).sort_values("date")
        expected = (
            len(pd.date_range(valid["date"].min(), valid["date"].max(), freq="D"))
            if len(valid)
            else 0
        )
        coverage = len(valid) / expected if expected else 0.0
        excluded_type = asset in excluded_symbols
        identity_resolved = (
            "coingecko_id" in valid
            and valid["coingecko_id"].notna().all()
            and valid["coingecko_id"].astype(str).nunique() == 1
        )
        included = (
            asset in pit_symbols
            and len(valid) >= 365
            and coverage >= 0.90
            and not excluded_type
            and identity_resolved
        )
        reason = (
            "broad unbalanced supplementary member; current-cohort source limitation applies"
            if included
            else "fails PIT, history, coverage, or asset-type rule"
        )
        rows.append(
            _row("S3", str(asset), valid.set_index("date")["close_usd"], included, reason, expected)
        )
    return rows


def _s4_membership(root: Path) -> list[dict[str, object]]:
    pit = _pit(root)
    primary = pit[
        pit["snapshot_date"].le(DATA_CUTOFF)
        & ~pit.get("is_partial_month", pd.Series(False, index=pit.index)).fillna(False)
        & pit["rank_full_market"].le(100)
    ]
    rows = []
    for item in primary.sort_values(["snapshot_date", "rank_full_market"]).itertuples(index=False):
        date = pd.Timestamp(item.snapshot_date)
        values = pd.Series([item.market_cap_usd], index=pd.DatetimeIndex([date]))
        rows.append(
            _row(
                "S4",
                str(item.symbol),
                values,
                True,
                "complete monthly PIT top-100 asset-month",
                period=date.date().isoformat(),
            )
        )
    return rows


def _s5_membership(root: Path) -> list[dict[str, object]]:
    path = root / "data_local" / "processed" / "feature_store_etf_trading_daily.parquet"
    if not path.exists():
        return []
    frame = pd.read_parquet(path)
    rows = []
    for asset, start in [("BTC ETF", "2024-01-11"), ("ETH ETF", "2024-07-23")]:
        column = f"{asset.split()[0].lower()}_etf_net_flow_usd"
        valid = frame.loc[frame.index >= pd.Timestamp(start), column].dropna()
        rows.append(_row("S5", asset, valid, True, "actual reported ETF dates only"))
    return rows


def _pit(root: Path) -> pd.DataFrame:
    path = root / "data_local" / "processed" / "market_structure_monthly.parquet"
    if path.exists():
        frame = pd.read_parquet(path).reset_index(drop=True)
    else:
        path = (
            resolve_raw_data_root(root)
            / "market_structure"
            / "DefiLlama"
            / "crypto_universe_monthly_2020_2026.csv"
        )
        frame = pd.read_csv(path)
    frame["snapshot_date"] = pd.to_datetime(frame["snapshot_date"])
    return frame


def _row(
    sample_id: str,
    asset: str,
    values: pd.Series,
    included: bool,
    reason: str,
    expected: int | None = None,
    period: str = "",
) -> dict[str, object]:
    valid = values.dropna()
    expected_count = expected if expected is not None else len(valid)
    return {
        "sample_id": sample_id,
        "asset": asset,
        "included": included,
        "reason": reason,
        "first_date": valid.index.min().date().isoformat() if not valid.empty else "",
        "last_date": valid.index.max().date().isoformat() if not valid.empty else "",
        "observations": int(len(valid)),
        "expected_observations": int(expected_count),
        "coverage": float(len(valid) / expected_count) if expected_count else 0.0,
        "period": period,
    }


def _excluded_asset_symbols(root: Path) -> set[str]:
    """Load stable-like, wrapped, and productized exclusions from canonical taxonomies."""

    excluded = set(STABLE_SYMBOLS | WRAPPED_SYMBOLS)
    taxonomy = yaml.safe_load((root / "config" / "asset_taxonomy.yml").read_text(encoding="utf-8"))
    excluded.update(taxonomy.get("stable_like", []))
    excluded.update(taxonomy.get("productized_wrapped", []))
    overrides = yaml.safe_load(
        (root / "config" / "asset_classification_overrides.yml").read_text(encoding="utf-8")
    )
    for key in [
        "stablecoins",
        "synthetic_stables",
        "stable_yield_tokens",
        "bridged_stables",
        "wrapped_assets",
        "tokenized_commodities",
        "tokenized_rwa",
        "lst_restaking",
        "bridged_duplicates",
    ]:
        excluded.update(overrides.get(key, []))
    return {str(symbol).upper() for symbol in excluded}
