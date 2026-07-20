"""Fetch and normalize official CFTC financial-futures positioning archives."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import zipfile
from pathlib import Path

import pandas as pd
import requests

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from config.paths import (  # noqa: E402
    DATA_LOCAL_METADATA_DIR,
    DATA_LOCAL_PROCESSED_DIR,
    provider_data_dir,
)

ARCHIVE_URL = "https://www.cftc.gov/files/dea/history/fut_fin_txt_{year}.zip"
CONTRACTS = {
    "133741": ("BTC", "CME Bitcoin", False),
    "133742": ("BTC", "CME Micro Bitcoin", True),
    "146021": ("ETH", "CME Ether", False),
    "146022": ("ETH", "CME Micro Ether", True),
}
CUTOFF = pd.Timestamp("2026-06-30")
USER_AGENT = (
    "moltovy Crypto Market Dynamics research https://github.com/moltovy/crypto-market-dynamics"
)


def fetch_archives(
    root: Path = ROOT,
    start_year: int = 2017,
    end_year: int = 2026,
    *,
    download_missing: bool = True,
) -> Path:
    """Download annual archives and write a contract-level normalized parquet."""

    raw_dir = provider_data_dir("cftc")
    raw_dir.mkdir(parents=True, exist_ok=True)
    archive_records: list[dict[str, object]] = []
    frames: list[pd.DataFrame] = []
    for year in range(start_year, end_year + 1):
        url = ARCHIVE_URL.format(year=year)
        archive = raw_dir / f"fut_fin_txt_{year}.zip"
        if not archive.exists():
            if not download_missing:
                raise FileNotFoundError(f"missing CFTC archive required for local build: {archive}")
            response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=90)
            response.raise_for_status()
            _atomic_bytes(archive, response.content)
        payload = archive.read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        with zipfile.ZipFile(io.BytesIO(payload)) as zipped:
            members = [name for name in zipped.namelist() if name.lower().endswith(".txt")]
            if len(members) != 1:
                raise ValueError(f"{archive.name}: expected one text member, found {members}")
            with zipped.open(members[0]) as handle:
                frame = pd.read_csv(
                    handle, low_memory=False, dtype={"CFTC_Contract_Market_Code": str}
                )
        frames.append(_normalize(frame))
        archive_records.append(
            {
                "year": year,
                "url": url,
                "path": f"data_local/raw/cftc/{archive.name}",
                "bytes": len(payload),
                "sha256": digest,
            }
        )

    normalized = pd.concat(frames, ignore_index=True)
    normalized = normalized[normalized["report_date"].le(CUTOFF)].copy()
    normalized = normalized.sort_values(["report_date", "contract_code"]).drop_duplicates(
        ["report_date", "contract_code"], keep="last"
    )
    output = DATA_LOCAL_PROCESSED_DIR / "cftc_financial_futures.parquet"
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".parquet.tmp")
    normalized.to_parquet(temporary, index=False)
    temporary.replace(output)

    metadata = {
        "cutoff": CUTOFF.date().isoformat(),
        "archives": archive_records,
        "rows": len(normalized),
        "first_report_date": normalized["report_date"].min().date().isoformat(),
        "last_report_date": normalized["report_date"].max().date().isoformat(),
        "contract_codes": sorted(normalized["contract_code"].unique()),
        "availability_rule": "report_date plus three calendar days; conservative Friday proxy",
    }
    metadata_path = DATA_LOCAL_METADATA_DIR / "cftc_financial_futures.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_metadata = metadata_path.with_suffix(".json.tmp")
    temporary_metadata.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    temporary_metadata.replace(metadata_path)
    return output


def _normalize(frame: pd.DataFrame) -> pd.DataFrame:
    selected = frame[frame["CFTC_Contract_Market_Code"].isin(CONTRACTS)].copy()
    selected["report_date"] = pd.to_datetime(selected["Report_Date_as_YYYY-MM-DD"])
    selected["available_date"] = selected["report_date"] + pd.Timedelta(days=3)
    selected["contract_code"] = selected["CFTC_Contract_Market_Code"]
    selected["asset"] = selected["contract_code"].map(lambda value: CONTRACTS[value][0])
    selected["contract_name"] = selected["contract_code"].map(lambda value: CONTRACTS[value][1])
    selected["is_micro"] = selected["contract_code"].map(lambda value: CONTRACTS[value][2])
    mappings = {
        "open_interest": "Open_Interest_All",
        "dealer_long": "Dealer_Positions_Long_All",
        "dealer_short": "Dealer_Positions_Short_All",
        "asset_manager_long": "Asset_Mgr_Positions_Long_All",
        "asset_manager_short": "Asset_Mgr_Positions_Short_All",
        "leveraged_money_long": "Lev_Money_Positions_Long_All",
        "leveraged_money_short": "Lev_Money_Positions_Short_All",
    }
    for output, source in mappings.items():
        selected[output] = pd.to_numeric(selected[source], errors="coerce")
    for category in ["dealer", "asset_manager", "leveraged_money"]:
        selected[f"{category}_net"] = selected[f"{category}_long"] - selected[f"{category}_short"]
        selected[f"{category}_net_share_oi"] = selected[f"{category}_net"] / selected[
            "open_interest"
        ].where(selected["open_interest"].gt(0))
    columns = [
        "report_date",
        "available_date",
        "asset",
        "contract_code",
        "contract_name",
        "is_micro",
        "open_interest",
        *[
            column
            for column in selected
            if column.endswith(("_long", "_short", "_net", "_net_share_oi"))
        ],
    ]
    return selected[columns]


def _atomic_bytes(path: Path, payload: bytes) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(payload)
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-year", type=int, default=2017)
    parser.add_argument("--end-year", type=int, default=2026)
    args = parser.parse_args()
    output = fetch_archives(ROOT, args.start_year, args.end_year)
    print(output)


if __name__ == "__main__":
    main()
