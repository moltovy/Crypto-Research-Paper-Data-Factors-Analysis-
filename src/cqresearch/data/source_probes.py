"""Bounded no-account probes for optional official external sources."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import pandas as pd
import requests

USER_AGENT = (
    "moltovy Crypto Market Dynamics research https://github.com/moltovy/crypto-market-dynamics"
)
TIMEOUT = 20


@dataclass
class ProbeResult:
    source_id: str
    gate_status: str
    access: str
    authentication: str
    terms: str
    earliest_date: str
    latest_date: str
    cadence: str
    missingness: str
    duplicates: str
    staleness: str
    timezone: str
    checksum: str
    enabled_analysis: str
    evidence: str
    checked_at: str


def run_source_probes(root: Path) -> pd.DataFrame:
    """Run small official-endpoint probes and write metadata-only evidence."""

    probes = [
        ("binance_vision", _probe_binance),
        ("cftc_cot_historical", _probe_cftc),
        ("sec_edgar", _probe_sec),
        ("defillama", _probe_defillama),
        ("fred_direct_download", _probe_fred),
        ("deribit_public_volatility", _probe_deribit),
        ("coinbase_exchange_candles", _probe_coinbase),
        ("official_issuer_downloads", _probe_issuers),
    ]
    results: list[ProbeResult] = []
    for source_id, probe in probes:
        try:
            results.append(probe())
        except requests.RequestException as exc:
            results.append(_network_failure(source_id, exc))
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            results.append(_schema_failure(source_id, exc))
    frame = pd.DataFrame(asdict(result) for result in results).sort_values("source_id")
    metadata = root / "data_local" / "metadata" / "source_probes.json"
    metadata.parent.mkdir(parents=True, exist_ok=True)
    metadata.write_text(frame.to_json(orient="records", indent=2), encoding="utf-8")
    public = frame.drop(columns=["checked_at"])
    public.to_csv(root / "research" / "source_decisions.csv", index=False)
    return frame


def _head(url: str, headers: dict[str, str] | None = None) -> tuple[int, dict[str, str]]:
    response = requests.head(
        url,
        headers={"User-Agent": USER_AGENT, **(headers or {})},
        timeout=TIMEOUT,
        allow_redirects=True,
    )
    return response.status_code, dict(response.headers)


def _json(url: str, params: dict[str, Any] | None = None) -> tuple[int, Any, str]:
    response = requests.get(
        url,
        params=params,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    digest = hashlib.sha256(response.content).hexdigest()
    return response.status_code, response.json(), digest


def _text(url: str) -> tuple[int, str, str]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT)
    response.raise_for_status()
    return response.status_code, response.text, hashlib.sha256(response.content).hexdigest()


def _probe_binance() -> ProbeResult:
    base = "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1d"
    first = f"{base}/BTCUSDT-1d-2020-01.zip"
    latest = f"{base}/BTCUSDT-1d-2026-06.zip"
    first_status, first_headers = _head(first)
    latest_status, latest_headers = _head(latest)
    checksum_status, _ = _head(latest + ".CHECKSUM")
    passed = first_status == latest_status == checksum_status == 200
    return _result(
        "binance_vision",
        passed,
        f"HEAD first={first_status}, latest={latest_status}, checksum={checksum_status}",
        "2020-01-01" if first_status == 200 else "",
        "2026-06-30" if latest_status == 200 else "",
        "daily archive",
        "requires post-download gap audit" if passed else "not evaluated",
        "requires post-download duplicate audit" if passed else "not evaluated",
        "current through frozen cutoff" if latest_status == 200 else "cutoff archive unavailable",
        "UTC",
        str(first_headers.get("ETag", "")) + str(latest_headers.get("ETag", "")),
        "venue robustness only" if passed else "none",
        "official ZIP and checksum objects; raw retrieval remains a later explicit step",
    )


def _probe_cftc() -> ProbeResult:
    index_url = (
        "https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm"
    )
    index_status, text, digest = _text(index_url)
    first_status, _ = _head("https://www.cftc.gov/files/dea/history/fut_fin_txt_2017.zip")
    recent_status, _ = _head("https://www.cftc.gov/files/dea/history/fut_fin_txt_2026.zip")
    passed = index_status == first_status == recent_status == 200 and "Historical" in text
    return _result(
        "cftc_cot_historical",
        passed,
        f"GET index={index_status}, HEAD 2017={first_status}, 2026={recent_status}",
        "2017" if first_status == 200 else "",
        "2026-06-30" if recent_status == 200 else "",
        "weekly report",
        "contract-code audit required after accepted retrieval" if passed else "not evaluated",
        "annual archives are distinct",
        "current-year archive available through the frozen cutoff",
        "US report date; as-of and release dates both required",
        digest,
        "regulated positioning context" if passed else "none",
        "official index and annual compressed archives; classification continuity remains a model gate",
    )


def _probe_sec() -> ProbeResult:
    docs = "https://www.sec.gov/search-filings/edgar-application-programming-interfaces"
    data = "https://data.sec.gov/submissions/CIK0001050446.json"
    docs_status, _, docs_digest = _text(docs)
    data_status, payload, data_digest = _json(data)
    history = payload.get("filings", {}).get("files", []) if isinstance(payload, dict) else []
    passed = docs_status == data_status == 200 and isinstance(history, list)
    return _result(
        "sec_edgar",
        passed,
        f"GET docs={docs_status}, submissions={data_status}",
        "entity filing history exposed by submissions API" if passed else "",
        "current submission metadata" if passed else "",
        "filing event",
        "amendments and taxonomy changes require explicit handling",
        "accession number is the immutable filing key",
        "current",
        "SEC accepted timestamp and filing date",
        hashlib.sha256((docs_digest + data_digest).encode()).hexdigest(),
        "descriptive corporate exposure-era metadata" if passed else "none",
        "official API with public project User-Agent; filing facts require entity/tag validation",
    )


def _probe_defillama() -> ProbeResult:
    status, payload, digest = _json("https://api.llama.fi/v2/historicalChainTvl")
    dates = pd.to_datetime(
        [item.get("date") for item in payload if isinstance(item, dict)], unit="s", errors="coerce"
    ).dropna()
    earliest = dates.min().date().isoformat() if len(dates) else ""
    latest = dates.max().date().isoformat() if len(dates) else ""
    passed = status == 200 and earliest <= "2020-01-01" and latest >= "2026-06-01"
    return _result(
        "defillama",
        passed,
        f"GET historicalChainTvl={status}",
        earliest,
        latest,
        "daily aggregate TVL",
        "aggregate endpoint only; each proposed chain/metric still requires its own gate",
        "timestamp uniqueness checked after retrieval",
        "current" if passed else "insufficient cutoff coverage",
        "UTC",
        digest,
        "aggregate TVL refresh only" if passed else "existing local snapshot only",
        "endpoint-specific pass does not authorize unprobed fees, revenue, bridge, or chain panels",
    )


def _probe_fred() -> ProbeResult:
    status, text, digest = _text("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10")
    lines = [line for line in text.splitlines()[1:] if line.strip()]
    earliest = lines[0].split(",", 1)[0] if lines else ""
    latest = lines[-1].split(",", 1)[0] if lines else ""
    passed = status == 200 and earliest <= "2020-01-01" and latest >= "2026-06-01"
    return _result(
        "fred_direct_download",
        passed,
        f"GET fredgraph DGS10={status}",
        earliest,
        latest,
        "business observation",
        "source missing markers preserved",
        "one observation per date expected",
        "current" if passed else "insufficient cutoff coverage",
        "FRED observation date; release lag is series-specific",
        digest,
        "macro refresh with latest-vintage caveat" if passed else "existing local export only",
        "coverage passes for DGS10; every additional series retains a series-specific contract",
    )


def _probe_deribit() -> ProbeResult:
    endpoint = "https://www.deribit.com/api/v2/public/get_volatility_index_data"
    start = int(pd.Timestamp("2020-01-01", tz="UTC").timestamp() * 1000)
    end = int(pd.Timestamp("2020-01-03", tz="UTC").timestamp() * 1000)
    status, payload, digest = _json(
        endpoint,
        {"currency": "BTC", "start_timestamp": start, "end_timestamp": end, "resolution": "3600"},
    )
    rows = payload.get("result", {}).get("data", []) if isinstance(payload, dict) else []
    passed = status == 200 and bool(rows)
    return _result(
        "deribit_public_volatility",
        passed,
        f"GET BTC DVOL 2020 window={status}, rows={len(rows)}",
        "2020-01-01" if rows else "",
        "probe window only",
        "hourly volatility index",
        "full institutional-period pagination still required"
        if passed
        else "no early history returned",
        "requires timestamp audit after accepted retrieval",
        "full-cutoff coverage not established by bounded probe",
        "UTC milliseconds",
        digest,
        "none_until_full_history" if passed else "none",
        "access passes but full-period eligibility remains failed until deterministic pagination is proven",
        force_fail=True,
    )


def _probe_coinbase() -> ProbeResult:
    endpoint = "https://api.exchange.coinbase.com/products/BTC-USD/candles"
    status, payload, digest = _json(
        endpoint,
        {"granularity": 86400, "start": "2020-01-01T00:00:00Z", "end": "2020-01-07T00:00:00Z"},
    )
    passed = status == 200 and isinstance(payload, list) and len(payload) >= 5
    return _result(
        "coinbase_exchange_candles",
        passed,
        f"GET BTC-USD 2020 daily window={status}, rows={len(payload) if isinstance(payload, list) else 0}",
        "2020-01-01" if passed else "",
        "bounded probe window",
        "daily candle",
        "deterministic pagination and sparse-bucket audit required",
        "timestamp uniqueness required after accepted retrieval",
        "full cutoff not established by bounded probe",
        "UTC bucket open",
        digest,
        "none_until_full_history" if passed else "none",
        "anonymous access passes but complete deterministic history remains unproven",
        force_fail=True,
    )


def _probe_issuers() -> ProbeResult:
    status, headers = _head("https://www.ishares.com/us/products/333011/ishares-bitcoin-trust-etf")
    return _result(
        "official_issuer_downloads",
        False,
        f"HEAD representative issuer product page={status}",
        "",
        "",
        "issuer-specific",
        "launch-to-cutoff archives not demonstrated",
        "not evaluated",
        "current-snapshot pages do not establish history",
        "issuer-specific",
        str(headers.get("ETag", "")),
        "Farside flows only; no issuer AUM or holdings claim",
        "failed full-history gate; no account, cookie-wall, or unstable snapshot workaround",
    )


def _result(
    source_id: str,
    passed: bool,
    access: str,
    earliest_date: str,
    latest_date: str,
    cadence: str,
    missingness: str,
    duplicates: str,
    staleness: str,
    timezone: str,
    checksum: str,
    enabled_analysis: str,
    evidence: str,
    *,
    force_fail: bool = False,
) -> ProbeResult:
    return ProbeResult(
        source_id=source_id,
        gate_status="pass" if passed and not force_fail else "fail",
        access=access,
        authentication="none",
        terms="official public endpoint; metadata access only; redistribution is not inferred",
        earliest_date=earliest_date,
        latest_date=latest_date,
        cadence=cadence,
        missingness=missingness,
        duplicates=duplicates,
        staleness=staleness,
        timezone=timezone,
        checksum=checksum,
        enabled_analysis=enabled_analysis,
        evidence=evidence,
        checked_at=datetime.now(UTC).replace(microsecond=0).isoformat(),
    )


def _network_failure(source_id: str, exc: Exception) -> ProbeResult:
    return _result(
        source_id,
        False,
        f"network failure: {type(exc).__name__}",
        "",
        "",
        "",
        "not evaluated",
        "not evaluated",
        "not evaluated",
        "",
        "",
        "none",
        "bounded probe failed; dependent analysis omitted",
    )


def _schema_failure(source_id: str, exc: Exception) -> ProbeResult:
    return _result(
        source_id,
        False,
        f"schema failure: {type(exc).__name__}",
        "",
        "",
        "",
        "not evaluated",
        "not evaluated",
        "not evaluated",
        "",
        "",
        "none",
        "bounded probe response did not satisfy the declared schema",
    )
