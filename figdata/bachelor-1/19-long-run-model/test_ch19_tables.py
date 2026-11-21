"""Facts the charts of b1 ch. 19 show."""
from pathlib import Path

import pandas as pd
from econdata import pwt

OUT = Path(__file__).resolve().parent / "out"


def test_labsh():
    d = pd.read_csv(OUT / "labsh.csv")
    assert len(d) == 74 and d.shape[1] == 6
    v = d.drop(columns="year")
    s = v.stack().dropna()
    assert ((s > 0.4) & (s < 0.8)).all()


def test_no_backfilled_run():
    # No series opens with two equal values: the back-filled years are gone.
    d = pd.read_csv(OUT / "labsh.csv")
    for c in ["fra", "deu", "jpn", "gbr", "usa"]:
        s = d[c].dropna().round(3)
        assert s.iloc[0] != s.iloc[1] or c in ("deu", "gbr", "jpn") and s.iloc[1] != s.iloc[2]


def test_first_real_years_from_raw_pwt():
    # Recomputed from the raw series: the last year of each opening flat run.
    raw = pwt(["DEU", "JPN", "GBR"], 1950, 2023, ["labsh"]).sort_values("year")
    d = pd.read_csv(OUT / "labsh.csv")
    for iso in ["DEU", "JPN", "GBR"]:
        r = raw[raw.iso3 == iso].set_index("year").labsh
        later = r[r != r.iloc[0]]
        first_real = later.index.min() - 1
        assert d.loc[d[iso.lower()].notna(), "year"].min() == first_real
    pts = pd.read_csv(OUT / "labsh_points.csv")
    assert pts[(pts.iso3 == "JPN") & (pts.year == 1970)].labsh.iloc[0] == 0.508
