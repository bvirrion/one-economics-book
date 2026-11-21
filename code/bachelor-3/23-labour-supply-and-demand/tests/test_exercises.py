import re

import numpy as np
from econdata import pwt, wdi, wdi_countries


def test_ex05_rates_match_log_growth(run_exercise):
    out, _ = run_exercise("ex05_hours")
    p = pwt(cols=["avh"]).dropna(subset=["avh"])
    lines = out.splitlines()
    assert len(lines) == 6
    for line in lines:
        iso, h0, y0, h1, g = re.match(
            r"(\w+): (\d+) hours in (\d+), (\d+) in 2023, (-?[\d.]+) % a year", line).groups()
        s = p[p.iso3 == iso].set_index("year").avh
        y0 = int(y0)
        assert abs(s.loc[y0] - int(h0)) <= 0.5 and abs(s.loc[2023] - int(h1)) <= 0.5
        rate = 100 * np.log(s.loc[2023] / s.loc[y0]) / (2023 - y0)
        assert abs(rate - float(g)) <= 0.005
        assert float(g) < 0
        d = np.log(s.loc[y0:y0 + 3]).diff().dropna()
        assert d.max() - d.min() > 1e-4


def test_ex08_square_term_matches_by_hand(run_exercise):
    out, _ = run_exercise("ex08_ushape")
    lines = out.splitlines()
    assert len(lines) == 2
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    for line in lines:
        year, n, b2 = re.match(r"(\d+): (\d+) countries, square term (-?[\d.]+)",
                               line).groups()
        year = int(year)
        r = wdi("SL.TLF.CACT.FM.ZS", since=year, until=year).rename(columns={"value": "r"})
        y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).rename(columns={"value": "y"})
        d = r.merge(y[["iso3", "y"]], on="iso3").dropna()
        d = d[d.iso3.isin(real)]
        x = np.log(d.y.to_numpy())
        X = np.column_stack([np.ones_like(x), x, x**2])
        beta = np.linalg.lstsq(X, d.r.to_numpy(), rcond=None)[0]
        assert len(d) == int(n) and abs(beta[2] - float(b2)) < 0.006
        assert beta[2] > 0
