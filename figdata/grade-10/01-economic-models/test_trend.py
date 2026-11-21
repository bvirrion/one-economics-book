import pandas as pd
from pathlib import Path

import make_trend as M

OUT = Path(__file__).parent / "out"


def test_us_values_match_maddison():
    d = pd.read_csv(OUT / "obs_usa.csv")
    assert d.year.min() == 1870 and d.year.max() == 2022
    assert d.loc[d.year == 1870, "gdppc"].item() == 4803
    assert d.loc[d.year == 2022, "gdppc"].item() == 58488


def test_fitted_line_passes_near_the_fit_period():
    lines = pd.read_csv(OUT / "trend_lines.csv").set_index("year")
    us = pd.read_csv(OUT / "obs_usa.csv").set_index("year").gdppc
    # within 25 % of the observed value in 1880 and 1910 (the fit period)
    for y in (1880, 1910):
        assert abs(lines.loc[y, "usa"] / us[y] - 1) < 0.25


def test_misses_are_complete_countries_sorted():
    m = pd.read_csv(OUT / "trend_misses.csv")
    assert list(m.pct) == sorted(m.pct)
    assert "JPN" not in set(m.iso3)          # Maddison has only 47 years of 1870-1929 for Japan
    assert "ARG" in set(m.iso3)
    f = pd.read_csv(OUT / "trend_fit.csv").set_index("iso3")
    assert 100 < f.loc["USA", "pct"] < 125 and f.loc["ARG", "pct"] < 60
