"""Institutional visual design tokens for public research artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

COLORS: dict[str, str] = {
    "bg": "#FAFAF7",
    "surface": "#FFFFFF",
    "surface2": "#F3F4F6",
    "grid": "#D9DEE7",
    "axis": "#E5E7EB",
    "text": "#111827",
    "muted": "#6B7280",
    "faint": "#9CA3AF",
    "btc": "#F7931A",
    "eth": "#627EEA",
    "macro": "#2563EB",
    "institutional": "#0F766E",
    "liquidity": "#16A34A",
    "stablecoin": "#059669",
    "native": "#7C3AED",
    "risk": "#DC2626",
    "gold": "#D97706",
    "neutral": "#6B7280",
    "positive": "#16A34A",
    "negative": "#DC2626",
    "white": "#FFFFFF",
}

FACTOR_COLORS: dict[str, str] = {
    "BTC ETF Flow": COLORS["institutional"],
    "ETH ETF Flow": COLORS["institutional"],
    "BTC MVRV": COLORS["native"],
    "ETH MVRV": COLORS["native"],
    "BTC Native ex MVRV": "#C084FC",
    "Native": COLORS["native"],
    "Macro": COLORS["macro"],
    "TradFi": COLORS["gold"],
    "Liquidity": COLORS["liquidity"],
    "Sentiment": COLORS["neutral"],
    "Risk": COLORS["risk"],
}

EVENTS: tuple[tuple[date, str, str], ...] = (
    (date(2022, 11, 8), "FTX", COLORS["risk"]),
    (date(2023, 3, 10), "SVB", COLORS["gold"]),
    (date(2024, 1, 11), "BTC ETF", COLORS["institutional"]),
    (date(2024, 4, 20), "Halving", COLORS["native"]),
    (date(2024, 7, 23), "ETH ETF", COLORS["eth"]),
)

FONT_FAMILY: list[str] = ["Inter", "Segoe UI", "DejaVu Sans", "Arial", "sans-serif"]
MONO_FONT_FAMILY: list[str] = ["Consolas", "DejaVu Sans Mono", "monospace"]

EXPORT_DPI = 160
SVG_DPI = 160
HERO_SIZE = (10.0, 5.625)
DETAIL_SIZE = (10.0, 6.4)
CONTACT_SHEET_SIZE = (16.0, 10.5)

HEADER_Y = 0.935
SUBTITLE_Y = 0.885
FOOTER_Y = 0.035

GRID_ALPHA = 0.45
LINE_WIDTH = 1.8
THIN_LINE = 0.9
MARKER_SIZE = 28
PANEL_RADIUS = 0.018

TEXT_DENSITY = "minimal"


@dataclass(frozen=True)
class FigureMeta:
    """Metadata attached to a generated public figure."""

    filename: str
    title: str
    source_table: str
    model_card: str
    method: str


FIGURE_SET: tuple[FigureMeta, ...] = (
    FigureMeta(
        "01_common_factor_tail_dependence.png",
        "Common Factor and Tail Dependence",
        "research/01_cross_asset_dependence_regimes/tables/common_factor_results.csv",
        "research/01_cross_asset_dependence_regimes/methodology.md",
        "leave-one-out factor and moving-block tail dependence",
    ),
    FigureMeta(
        "02_dynamic_tradfi_integration.png",
        "Dynamic TradFi Integration",
        "research/02_macro_tradfi_integration/tables/dynamic_tradfi_exposures.csv",
        "research/02_macro_tradfi_integration/methodology.md",
        "rolling exposure and era interaction",
    ),
    FigureMeta(
        "04_institutional_market_plumbing.png",
        "Institutional Market Plumbing",
        "research/04_etf_institutional_flows/tables/etf_distributed_lags.csv",
        "research/04_etf_institutional_flows/methodology.md",
        "simultaneous ETF lag bands and CFTC positioning eras",
    ),
    FigureMeta(
        "03_leverage_tail_connectedness.png",
        "Leverage, Tail Stress, and Connectedness",
        "research/03_derivatives_leverage_liquidations/tables/leverage_tail_model.csv",
        "research/03_derivatives_leverage_liquidations/methodology.md",
        "spline marginal association and generalized FEVD",
    ),
    FigureMeta(
        "07_pit_concentration_turnover.png",
        "PIT Concentration and Turnover",
        "research/07_chain_fundamentals_sector_dynamics/tables/pit_concentration.csv",
        "research/07_chain_fundamentals_sector_dynamics/methodology.md",
        "effective breadth and monthly membership turnover",
    ),
)


def factor_color(name: str) -> str:
    """Return a stable color for a factor or block label."""

    return FACTOR_COLORS.get(name, COLORS["neutral"])
