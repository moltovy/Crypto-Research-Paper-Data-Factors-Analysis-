"""Fetch checksum-verified Binance Vision daily klines for the fixed S2 allowlist."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
import requests
import yaml

ROOT = Path(__file__).resolve().parents[2]
BASE = "https://data.binance.vision/data/spot/monthly/klines"
USER_AGENT = (
    "moltovy Crypto Market Dynamics research "
    "https://github.com/moltovy/crypto-market-dynamics"
)
KLINE_COLUMNS = [
    "open_time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "close_time",
    "quote_asset_volume",
    "trade_count",
    "taker_buy_base_volume",
    "taker_buy_quote_volume",
    "ignore",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=8)
    return parser.parse_args()


def month_range(start: str, end: str) -> list[str]:
    return [value.strftime("%Y-%m") for value in pd.period_range(start, end, freq="M")]


def fetch_archive(symbol: str, month: str, raw_root: Path) -> dict[str, str]:
    name = f"{symbol}-1d-{month}.zip"
    url = f"{BASE}/{symbol}/1d/{name}"
    target = raw_root / symbol / "1d" / name
    target.parent.mkdir(parents=True, exist_ok=True)
    checksum_url = url + ".CHECKSUM"
    checksum_response = _get(checksum_url)
    expected = checksum_response.text.strip().split()[0].lower()
    if target.exists() and _sha256(target.read_bytes()) == expected:
        return {"symbol": symbol, "month": month, "path": str(target), "sha256": expected}
    payload = _get(url).content
    actual = _sha256(payload)
    if actual != expected:
        raise ValueError(f"checksum mismatch for {name}: expected {expected}, got {actual}")
    temporary = target.with_suffix(".zip.part")
    temporary.write_bytes(payload)
    temporary.replace(target)
    return {"symbol": symbol, "month": month, "path": str(target), "sha256": actual}


def _get(url: str) -> requests.Response:
    for attempt in range(5):
        response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
        if response.status_code == 200:
            return response
        if response.status_code in {429, 500, 502, 503, 504}:
            time.sleep(2**attempt)
            continue
        response.raise_for_status()
    raise RuntimeError(f"retries exhausted: {url}")


def normalize_archives(records: list[dict[str, str]]) -> pd.DataFrame:
    frames = []
    for record in sorted(records, key=lambda item: (item["symbol"], item["month"])):
        path = Path(record["path"])
        with zipfile.ZipFile(path) as archive:
            member = archive.namelist()[0]
            frame = pd.read_csv(
                io.BytesIO(archive.read(member)), names=KLINE_COLUMNS, header=None
            )
        raw_time = pd.to_numeric(frame["open_time"], errors="coerce")
        unit = "us" if raw_time.dropna().median() > 100_000_000_000_000 else "ms"
        frame["date"] = pd.to_datetime(raw_time, unit=unit, utc=True, errors="coerce").dt.tz_localize(None)
        frame["symbol"] = record["symbol"].removesuffix("USDT")
        for column in [
            "open",
            "high",
            "low",
            "close",
            "volume",
            "quote_asset_volume",
            "trade_count",
        ]:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
        frames.append(
            frame[
                [
                    "date",
                    "symbol",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "quote_asset_volume",
                    "trade_count",
                ]
            ]
        )
    result = pd.concat(frames, ignore_index=True)
    result = result.dropna(subset=["date"]).sort_values(["symbol", "date"])
    duplicates = result.duplicated(["symbol", "date"], keep=False)
    if duplicates.any():
        raise ValueError(f"duplicate symbol/date rows: {int(duplicates.sum())}")
    return result.reset_index(drop=True)


def normalize_existing_archives(root: Path, raw_root: Path) -> Path:
    """Normalize the complete configured archive set without network access."""

    config = yaml.safe_load(
        (root / "config" / "binance_datasets.yml").read_text(encoding="utf-8")
    )
    defaults = config["defaults"]
    archive_root = raw_root / Path(config["raw_cache"]).relative_to(
        Path("data_local/raw/binance")
    )
    records: list[dict[str, str]] = []
    missing: list[str] = []
    for symbol in defaults["stable_core_candidates"]:
        for month in month_range(defaults["start_month"], defaults["end_month"]):
            archive = archive_root / symbol / "1d" / f"{symbol}-1d-{month}.zip"
            if not archive.exists():
                missing.append(archive.relative_to(raw_root).as_posix())
                continue
            records.append(
                {
                    "symbol": symbol,
                    "month": month,
                    "path": str(archive),
                    "sha256": _sha256(archive.read_bytes()),
                }
            )
    if missing:
        raise FileNotFoundError(f"missing configured Binance archives: {missing[:10]}")
    panel = normalize_archives(records)
    output = root / config["curated_root"]
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".parquet.tmp")
    panel.to_parquet(temporary, index=False)
    temporary.replace(output)
    return output


def main() -> None:
    args = parse_args()
    config = yaml.safe_load((ROOT / "config" / "binance_datasets.yml").read_text(encoding="utf-8"))
    defaults = config["defaults"]
    symbols = list(defaults["stable_core_candidates"])
    months = month_range(defaults["start_month"], defaults["end_month"])
    raw_root = ROOT / config["raw_cache"]
    records: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        jobs = {
            executor.submit(fetch_archive, symbol, month, raw_root): (symbol, month)
            for symbol in symbols
            for month in months
        }
        for job in as_completed(jobs):
            records.append(job.result())
    panel = normalize_archives(records)
    panel_path = ROOT / config["curated_root"]
    panel_path.parent.mkdir(parents=True, exist_ok=True)
    panel.to_parquet(panel_path, index=False)
    coverage = (
        panel.groupby("symbol")
        .agg(first_date=("date", "min"), last_date=("date", "max"), observations=("date", "size"))
        .reset_index()
    )
    expected = len(pd.date_range(defaults["start_month"] + "-01", "2026-06-30", freq="D"))
    coverage["expected_days"] = expected
    coverage["coverage"] = coverage["observations"] / expected
    coverage.to_csv(ROOT / "data_local" / "metadata" / "binance_stable_core_coverage.csv", index=False)
    manifest = {
        "source": "Binance Vision official monthly archive",
        "retrieved_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "symbols": symbols,
        "start_month": defaults["start_month"],
        "end_month": defaults["end_month"],
        "archives": sorted(records, key=lambda item: (item["symbol"], item["month"])),
        "panel_sha256": _sha256(panel_path.read_bytes()),
        "rows": len(panel),
    }
    (ROOT / "data_local" / "metadata" / "binance_stable_core_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    print(coverage.to_string(index=False))


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


if __name__ == "__main__":
    main()
