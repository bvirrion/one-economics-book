import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_fedfunds():
    d = pd.read_csv(OUT / "fedfunds.csv")
    assert d.t.min() < 1965.1 and d.rate.max() > 15 and d.infl.max() > 13


def test_rule_and_key():
    k = pd.read_csv(OUT / "policy_key.csv").iloc[0]
    assert k.corr_8707 > 0.5 and k.rule2022 - k.actual2022 > 8 and k.assets_peak > 8


def test_brenland():
    b = pd.read_csv(OUT / "brenland.csv").set_index("year")
    assert len(b) == 11
    r = b.loc[2022]
    assert abs(r.rule - (2 + r.infl + 0.5 * (r.infl - 2) + 0.5 * r.gap)) < 0.01
