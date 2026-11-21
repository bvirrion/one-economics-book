import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / "out"


def test_span_and_base():
    d = pd.read_csv(OUT / "oil_us.csv").set_index("year")
    assert d.index.min() == 1976 and d.index.max() == 2024
    assert abs(d.loc[2024, "price"] - 3.45) < 0.01      # 2024 dollars: the nominal 2024 price


def test_the_two_price_peaks_cut_use():
    d = pd.read_csv(OUT / "oil_us.csv").set_index("year")
    assert d.loc[1981, "price"] > 1.4 * d.loc[1978, "price"] and d.loc[1983, "bpp"] < 0.8 * d.loc[1978, "bpp"]
    assert d.loc[2012, "bpp"] < d.loc[2005, "bpp"]
    s = pd.read_csv(OUT / "oil_summary.csv").iloc[0]
    assert s.n == 48 and s.opposite > s.n / 2
