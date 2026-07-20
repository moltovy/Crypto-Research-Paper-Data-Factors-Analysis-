"""Generate the public research report and visual-QA page renders."""

from __future__ import annotations

import base64
import re
import shutil
import subprocess
from pathlib import Path

import fitz
import markdown
import pandas as pd

from cqresearch.core.artifacts import write_text
from cqresearch.research.registry import module_by_id

REPORT_FIGURES = [
    ("01_cross_asset_dependence_regimes", "01_common_factor_tail_dependence.png"),
    ("02_macro_tradfi_integration", "02_dynamic_tradfi_integration.png"),
    ("04_etf_institutional_flows", "04_institutional_market_plumbing.png"),
    ("03_derivatives_leverage_liquidations", "03_leverage_tail_connectedness.png"),
    ("07_chain_fundamentals_sector_dynamics", "07_pit_concentration_turnover.png"),
    ("05_stablecoin_defi_liquidity", "05_liquidity_measurement_diagnostics.png"),
    ("09_event_stress_cross_module_synthesis", "09_event_atlas_appendix.png"),
]


def build_report(root: Path) -> list[Path]:
    reports = root / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    markdown_path = reports / "crypto_market_dynamics_research_report.md"
    html_path = reports / "crypto_market_dynamics_research_report.html"
    pdf_path = reports / "crypto_market_dynamics_research_report.pdf"
    write_text(markdown_path, _report_markdown(root))
    write_text(html_path, _self_contained_html(markdown_path))
    _render_pdf(html_path, pdf_path)
    pages = rasterize_pdf(pdf_path, root / "data_local" / "cache" / "pdf_pages")
    return [markdown_path, html_path, pdf_path, *pages]


def rasterize_pdf(pdf_path: Path, output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    for old in output_dir.glob("page-*.png"):
        old.unlink()
    document = fitz.open(pdf_path)
    outputs = []
    matrix = fitz.Matrix(1.5, 1.5)
    for index, page in enumerate(document):
        output = output_dir / f"page-{index + 1:02d}.png"
        page.get_pixmap(matrix=matrix, alpha=False).save(output)
        outputs.append(output)
    document.close()
    return outputs


def _report_markdown(root: Path) -> str:
    claims = _claims(root)
    figure_sections = []
    for module_id, filename in REPORT_FIGURES:
        module = module_by_id(module_id)
        module_number = module_id.split("_", 1)[0]
        claim = claims.loc[claims["module_id"].eq(module_id)].iloc[0]
        figure_path = f"../research/{module_id}/figures/{filename}"
        table = str(claim["source_table"]).split(";")[0].strip()
        table_path = f"../research/{module_id}/{table}"
        figure_sections.append(
            f"## {module_number}. {module.title}\n\n"
            f"![{module.title}]({figure_path})\n\n"
            f"**Result.** {claim['claim_text']}\n\n"
            f"**Sample.** {claim['sample']}\n\n"
            f"**Method and uncertainty.** {claim['method']} {claim['uncertainty']}\n\n"
            f"**Evidence grade.** {claim['evidence_grade']}. **Limitation.** {claim['limitation']}\n\n"
            f"**Provenance.** [Primary source table]({table_path}); "
            f"[module documentation](../research/{module_id}/README.md)."
        )
    sections = "\n\n".join(figure_sections)
    return f"""# Crypto Market Dynamics: Evidence Report

**Acquisition cutoff:** 2026-06-30<br>
**Estimator seed:** 20260713<br>
**Scope:** descriptive and associational empirical finance; no forecasting, trading strategy, portfolio-allocation, or causal claim.

## Study Design

The repository addresses four questions: realized crypto dependence and TradFi integration; institutional market plumbing; leverage, tails, and connectedness; and endogenous liquidity state with monthly point-in-time market structure. Inputs, timestamps, availability rules, transformations, denominators, missing-value rules, samples, estimands, and claims are registered under [`research/`](../research/README.md).

S1 covers BTC/ETH daily anchors. S2 fixes a January 2021 PIT-eligible stable core with at least 95% daily coverage. S3 is a supplementary unbalanced current-cohort panel and remains survivorship-biased. S4 is monthly point-in-time top-100 structure through the last complete month. S5 begins each ETF or institutional series at its actual reporting inception.

The primary uncertainty procedures are HAC covariance and deterministic moving-block bootstrap inference. Same-day MVRV is excluded from primary BTC/ETH models. ETF flows, stablecoin supply, and DeFi TVL are endogenous market-state measures.

## Estimands and Equations

| Quantity | Definition | Interpretation boundary |
|---|---|---|
| Log return | `r[i,t] = log(P[i,t] / P[i,t-1])` on the series' native calendar before joins | Realized return, not a forecast target. |
| Leave-one-out common factor | First PC of standardized S2 returns excluding asset `i`; `r[i,t] = alpha + beta * PC1[-i,t] + error` | Descriptive common variation without mechanical self-inclusion. |
| Tail excess | `Pr(r[i] <= Q[i,q], r[j] <= Q[j,q]) - q^2` | Co-exceedance relative to independence, not causal contagion. |
| ETF distributed lag | `y[t] = alpha + sum(k=0..5) beta[k] * flow_bps[t-k] + error[t]` | Timing-sensitive association; flow uses lagged market capitalization. |
| Leverage tail model | `logit Pr(r[t+1] <= Q[0.05]) = spline(leverage[t-1]) + spline(volatility[t-1])` | Conditional association, not a prediction rule. |
| Generalized FEVD connectedness | Off-diagonal generalized forecast-error variance shares divided by total shares | Descriptive stress connectedness; variable-order sensitivity is reported. |
| PIT structure | `HHI[t] = sum(i) share[i,t]^2`; entropy breadth `= exp(-sum(i) share[i,t] * log(share[i,t]))`; turnover `= (entries + exits) / size(union of adjacent memberships)` | Monthly composition only; no daily constituent-return inference. |
| Liquidity residual | Residual from HAC regression of log USD TVL growth on BTC, ETH, and TOTAL3 returns | Endogenous state proxy, not an exogenous liquidity shock. |
| MVRV identity | `d log MVRV = d log market cap - d log realized cap + residual` | Measurement-mechanics diagnostic excluded from primary return models. |

{sections}

## Cross-Module Assessment

The strongest descriptive evidence concerns broad common crypto variation, lower-tail co-exceedance above independence, time-varying cross-market exposure, nonlinear leverage-state associations, and changing monthly market breadth and turnover. Formal TradFi era interactions are weak, most ETF lag coefficients do not clear simultaneous bands, and USD TVL residualization has low explanatory power. Those weak results are retained without specification search.

## Reproducibility

```bash
uv sync --all-extras
uv run python scripts/run_all.py --mode local
uv run python scripts/execute_reproducibility_notebook.py
uv run python scripts/build_report.py
uv run python scripts/check_research_surface.py --module all
```

Public CI runs fixture scientific smoke tests and validates committed semantic outputs without requiring local provider exports. A full local build requires legally obtained inputs under `data_local/raw/` or an external read-only `CMD_DATA_ROOT`.

## References

Source attribution, event provenance, and econometric references are maintained in [`REFERENCES.md`](../REFERENCES.md). Source eligibility and fallback decisions are in [`research/source_decisions.csv`](../research/source_decisions.csv).
"""


def _claims(root: Path) -> pd.DataFrame:
    rows = []
    for module_id, _ in REPORT_FIGURES:
        path = root / "research" / module_id / "tables" / "claims.csv"
        rows.extend(pd.read_csv(path).to_dict("records"))
    return pd.DataFrame(rows)


def _self_contained_html(markdown_path: Path) -> str:
    text = markdown_path.read_text(encoding="utf-8")

    def embed(match: re.Match[str]) -> str:
        alt, target = match.group(1), match.group(2)
        path = (markdown_path.parent / target).resolve()
        if not path.exists():
            raise FileNotFoundError(path)
        mime = "image/png" if path.suffix.lower() == ".png" else "image/svg+xml"
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        return f"![{alt}](data:{mime};base64,{encoded})"

    embedded = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", embed, text)
    body = markdown.markdown(embedded, extensions=["tables", "fenced_code"])
    css = """
@page { size: Letter; margin: 0.62in; }
body { font-family: Arial, sans-serif; color: #1f2430; line-height: 1.38; max-width: 1040px; margin: 0 auto; }
h1 { font-size: 28px; margin-bottom: 8px; }
h2 { font-size: 19px; margin-top: 28px; page-break-after: avoid; }
p, li, td, th { font-size: 10.5pt; }
img { display: block; width: 100%; max-height: 5.8in; object-fit: contain; page-break-inside: avoid; }
p:has(> img) { margin: 0 0 12px; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; }
tr { break-inside: avoid; page-break-inside: avoid; }
th, td { border-bottom: 1px solid #d7dbe7; padding: 6px; text-align: left; }
code { font-family: Consolas, monospace; font-size: 9pt; }
pre { background: #f5f6f8; padding: 10px; white-space: pre-wrap; page-break-inside: avoid; }
a { color: #2e4780; }
"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def _render_pdf(html_path: Path, pdf_path: Path) -> None:
    browser = _browser_executable()
    temporary = pdf_path.with_suffix(".pdf.tmp")
    if temporary.exists():
        temporary.unlink()
    command = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={temporary}",
        html_path.resolve().as_uri(),
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=120, check=False)
    if result.returncode != 0 or not temporary.exists():
        raise RuntimeError(f"browser PDF render failed: {result.stderr or result.stdout}")
    temporary.replace(pdf_path)


def _browser_executable() -> Path:
    candidates = [
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    ]
    for name in ["microsoft-edge", "google-chrome", "chromium", "chromium-browser"]:
        found = shutil.which(name)
        if found:
            candidates.append(Path(found))
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("no headless Chrome or Edge executable found")


__all__ = ["REPORT_FIGURES", "build_report", "rasterize_pdf"]
