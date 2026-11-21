import pandas as pd
from pathlib import Path

import country

OUT = Path(__file__).parent / "out"


def test_us_items():
    s = pd.read_csv(OUT / "us_summary.csv").set_index("item").idx2025
    assert s["computers"] < 15 and s["tuition"] > 250 and 150 < s["all"] < 220


def test_laspeyres_matches_accounts_cpi():
    las = pd.read_csv(OUT / "bren_laspeyres.csv").set_index("year").cpi
    acc = country.load("accounts").set_index("year").cpi
    assert (abs(las.round(1) - acc.loc[las.index]) <= 0.1).all()
