import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_convergence_only_within_group():
    k = pd.read_csv(OUT / "conv_key.csv").iloc[0]
    assert k.n_eur >= 15
    assert k.corr_eur < -0.5 and k.corr_all > k.corr_eur


def test_paths_converge():
    p = pd.read_csv(OUT / "paths.csv")
    k = pd.read_csv(OUT / "solow_key.csv").iloc[0]
    last = p.iloc[-1]
    assert abs(last.low - k.kstar) < 0.05 * k.kstar and abs(last.high - k.kstar) < 0.05 * k.kstar
    assert (p.low.diff().dropna() > 0).all() and (p.high.diff().dropna() < 0).all()
    assert k.kstar2 > k.kstar and 15 < k.half_rise < 30


def test_recovery():
    r = pd.read_csv(OUT / "recovery.csv").set_index("year")
    assert r.loc[1946, "DEU"] < r.loc[1938, "DEU"] and r.loc[1960, "DEU"] > r.loc[1938, "DEU"]
