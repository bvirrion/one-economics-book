"""The Ramsey model, chapter 23.

Opening chart: gross domestic saving, per cent of GDP, Korea and China 1960-2024, Japan
1970-2024 (WDI NY.GDS.TOTL.ZS). Chart 2: Korea's capital-output ratio, 1980-2023 (PWT
rnna / rgdpna, constant national prices). PWT builds the stock from an assumed stock in
1953; what survives of that guess is 85 per cent of the 1960 stock, 41 per cent of the
1970 one and 10 per cent of the 1980 one (initial_share), so the chart starts in 1980. Model charts (invented parameters, the
chapter's: alpha 1/3, delta 0.05, rho 0.03, n 0.01): the saddle path in (k, c) for
theta = 2, from k*/4 and from 2 k*; time paths of k / k* and of the saving rate from
k*/4 for theta = 2 and theta = 6.
Writes
  out/saving.csv           year, KOR, JPN, CHN
  out/saving_summary.csv   one row per country: iso3, first year, first, peak, peak
                           year, last
  out/ky.csv               year, ky
  out/ky_summary.csv       one row: 1980, minimum and its year, 2023
  out/saddle.csv           k, c (theta 2; points from below and from above k*)
  out/paths.csv            t, k2, s2, k6, s6 (k / k*, saving rate)
"""

import pandas as pd
from econdata import pwt, wdi
from figout import write_table

ALPHA, DELTA, RHO, N = 1 / 3, 0.05, 0.03, 0.01
K_STAR = (ALPHA / (RHO + DELTA)) ** (1 / (1 - ALPHA))


def saving():
    w = wdi("NY.GDS.TOTL.ZS", isos=["KOR", "JPN", "CHN"], since=1960, until=2024)
    p = w.pivot(index="year", columns="iso3", values="value")[["KOR", "JPN", "CHN"]]
    return p.round(2).reset_index()


def saving_summary():
    p = saving().set_index("year")
    rows = []
    for c in p.columns:
        s = p[c].dropna()
        rows.append(
            {
                "iso3": c,
                "first_year": int(s.index[0]),
                "first": round(s.iloc[0], 1),
                "peak": round(s.max(), 1),
                "peak_year": int(s.idxmax()),
                "last": round(s.iloc[-1], 1),
            }
        )
    return pd.DataFrame(rows)


KY_START = 1980


def initial_share():
    """Share of each year's PWT capital stock that is what remains, after depreciation,
    of the assumed 1953 stock."""
    p = pwt(isos=["KOR"]).set_index("year")
    first = int(p.rnna.first_valid_index())
    survive = (1 - p.delta.loc[first + 1 :]).cumprod()
    share = p.rnna[first] * survive / p.rnna.loc[first + 1 :]
    return pd.DataFrame({"share": share.round(3)}).reset_index()


def ky():
    p = pwt(isos=["KOR"], since=KY_START).set_index("year")
    return pd.DataFrame({"ky": (p.rnna / p.rgdpna).round(3)}).reset_index()


def ky_summary():
    s = ky().set_index("year").ky
    return pd.DataFrame(
        [
            {
                "y1980": round(s[KY_START], 2),
                "min": round(s.min(), 2),
                "min_year": int(s.idxmin()),
                "y2023": round(s[2023], 2),
            }
        ]
    )


def _path(c, theta, k, dt=0.01, years=150):
    out = []
    for step in range(int(years / dt)):
        if step % 100 == 0:
            out.append((k, c))
        dk = k**ALPHA - c - (N + DELTA) * k
        dc = c * (ALPHA * k ** (ALPHA - 1) - DELTA - RHO) / theta
        below = k < K_STAR
        if (dk < 0) if below else (dk > 0):
            return "high" if below else "low"
        if (dc < 0) if below else (dc > 0):
            return "low" if below else "high"
        k, c = k + dk * dt, c + dc * dt
    return out


def _saddle(theta, k0):
    lo, hi, best = 0.0, k0**ALPHA, None
    for _ in range(50):
        mid = (lo + hi) / 2
        res = _path(mid, theta, k0)
        if isinstance(res, list):
            best = res
        lo, hi = (mid, hi) if res == "low" else (lo, mid)
    return best


def saddle():
    rows = []
    for k0 in (K_STAR / 4, 2 * K_STAR):
        p = _saddle(2, k0)[:80]
        rows += [{"k": round(k, 4), "c": round(c, 4)} for k, c in p]
    return pd.DataFrame(rows).sort_values("k")


def paths():
    p2, p6 = _saddle(2, K_STAR / 4)[:61], _saddle(6, K_STAR / 4)[:61]
    return pd.DataFrame(
        {
            "t": range(61),
            "k2": [round(k / K_STAR, 4) for k, _ in p2],
            "s2": [round(1 - c / k**ALPHA, 4) for k, c in p2],
            "k6": [round(k / K_STAR, 4) for k, _ in p6],
            "s6": [round(1 - c / k**ALPHA, 4) for k, c in p6],
        }
    )


if __name__ == "__main__":
    write_table(saving(), __file__, "saving")
    write_table(saving_summary(), __file__, "saving_summary")
    write_table(ky(), __file__, "ky")
    write_table(ky_summary(), __file__, "ky_summary")
    write_table(saddle(), __file__, "saddle")
    write_table(paths(), __file__, "paths")
