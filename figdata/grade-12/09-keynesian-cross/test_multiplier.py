import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_estimates():
    d = pd.read_csv(OUT / "multipliers.csv")
    assert len(d) == 14 and (d.hi >= d.lo).all() and d.lo.min() >= 0.3 and d.hi.max() <= 2


def test_brenland():
    k = pd.read_csv(OUT / "brenland_key.csv").iloc[0]
    assert abs(k.k_ctm - 1 / (1 - k.c * (1 - k.t) + k.m)) < 1e-3
    assert k.k_ctm < k.k_ct < k.k_c and 1 < k.k_ctm < 2
