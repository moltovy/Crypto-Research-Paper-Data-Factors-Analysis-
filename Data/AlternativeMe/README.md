# AlternativeMe

**Source**: https://alternative.me/crypto/fear-and-greed-index/

Crypto Fear & Greed Index — a daily 0–100 composite sentiment score blending volatility, momentum, social media, surveys, BTC dominance, and search trends. Useful as a broad, exogenous sentiment control.

**Date convention**: `date` is ISO `YYYY-MM-DD` ascending, one row per calendar day.

**Units**: `fng_value` is 0–100 integer. `fng_classification` is the bucket label (`Extreme Fear`, `Fear`, `Neutral`, `Greed`, `Extreme Greed`).

**Frequency hint**: Daily, calendar-day cadence (no gaps).

**Licensing**: Alternative.me; free with attribution.

## Files (1)

| File | Topic | Date range | Rows | Freq | Missing days | Cols | SHA |
| --- | --- | --- | ---: | --- | ---: | ---: | --- |
| `fear_greed_index__daily.csv` | Crypto Fear & Greed index | 2018-02-01 .. 2026-04-17 | 2,994 | daily | 4 | 3 | `e61ecae2b7a2` |

## Sample rows (first 2 rows per file — truncated to 10 columns)

**`fear_greed_index__daily.csv`**

```csv
date,fng_value,fng_classification
2018-02-01,30,Fear
2018-02-02,15,Extreme Fear
```

---
_Auto-generated on 2026-04-17 by `tools/data_curation/06_build_inventory.py`. Regenerate after any data refresh._
