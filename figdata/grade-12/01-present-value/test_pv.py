import pandas as pd
from pathlib import Path

import importlib.util

OUT = Path(__file__).parent / "out"
spec = importlib.util.spec_from_file_location("make_pv", Path(__file__).parent / "make_pv.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_yields_fell_and_perpetuity_rose():
    y = pd.read_csv(OUT / "yields.csv").set_index("year")
    assert y.loc[1981, "usa_lt"] > 13 and y.loc[2020, "usa_lt"] < 1
    assert y.loc[2020, "usa_perp"] > 10 * y.loc[1981, "usa_perp"]


def test_bridge():
    k = pd.read_csv(OUT / "bridge_key.csv").iloc[0]
    assert k.npv2 > k.npv4 > 0 > k.npv6
    assert abs(m.npv(k.irr / 100)) < 0.05
    assert 5.5 < k.irr < 5.75


def test_perpetuity_limit():
    # a 30-year annuity is worth less than the perpetuity NET / r
    assert m.npv(0.04) + m.COST < m.NET / 0.04
