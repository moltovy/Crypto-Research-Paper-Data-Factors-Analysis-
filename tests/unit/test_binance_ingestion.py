from __future__ import annotations

import io
import zipfile

import pandas as pd
from tools.data_collection.fetch_binance_stable_core import KLINE_COLUMNS, normalize_archives


def test_normalizer_handles_millisecond_and_microsecond_timestamps(tmp_path) -> None:
    rows = [
        [1609459200000, 1, 2, 0.5, 1.5, 10, 0, 20, 3, 4, 5, 0],
        [1609545600000, 1.5, 2, 1, 1.8, 11, 0, 21, 4, 5, 6, 0],
    ]
    assert len(rows[0]) == len(KLINE_COLUMNS)
    path = tmp_path / "BTCUSDT-1d-2021-01.zip"
    buffer = io.StringIO()
    pd.DataFrame(rows).to_csv(buffer, header=False, index=False)
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("BTCUSDT-1d-2021-01.csv", buffer.getvalue())
    frame = normalize_archives(
        [{"symbol": "BTCUSDT", "month": "2021-01", "path": str(path), "sha256": "x"}]
    )
    assert frame["symbol"].eq("BTC").all()
    assert frame["date"].dt.strftime("%Y-%m-%d").tolist() == ["2021-01-01", "2021-01-02"]
