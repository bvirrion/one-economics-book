"""g8-04 Growth and Compounding.

three_speeds.csv  year, slow, mid, fast: real GDP per person, constant 2015 US dollars, 1960-2024 (WDI NY.GDP.PCAP.KD),
                  for the three candidate countries whose average growth 1960-2024 is closest to 1, 2 and 6 percent
speeds.csv        role, iso3, name, y1960, y2024, growth: the chosen countries and their average yearly growth (percent)
us_two_centuries.csv year, gdppc, steady: US GDP per person 1820-2022 (Maddison Project, 2011 dollars) and the steady
                  path from 1870 at the 1870-2022 average rate
compound.csv      year, simple, compound: 100 growing by 10 a year, and by 10 % a year, years 0-10
neighbours.csv    year, brenland, kestria: real GDP per person (2015 dalens); Brenland from its accounts. Kestria's
                  2025 value is tied to the frozen package and to the other chapters: 30 000 kests per person
                  (g8-02 ex. 6, g9-05 pb), converted at the 2025 market rate (trade.csv) and deflated by
                  Brenland's 2025 deflator (accounts.csv): 30000 * 1.242 / 1.345 = 27 700. Earlier years are
                  invented here: 4 % a year back to 2000 (10 400), with a seeded wobble that vanishes at both ends
facts.csv         name, value
"""
import numpy as np
import pandas as pd

from country import load
from econdata import maddison, wdi
from figout import write_table

CANDIDATES = {"ARG": "Argentina", "MEX": "Mexico", "USA": "United States", "FRA": "France",
              "KOR": "South Korea", "CHN": "China"}
TARGETS = {"slow": 1.0, "mid": 2.0, "fast": 6.0}


def _growth(a, b, n):
    return 100 * ((b / a) ** (1 / n) - 1)


def speeds():
    d = wdi("NY.GDP.PCAP.KD", isos=list(CANDIDATES), since=1960, until=2024)
    p = d.pivot(index="year", columns="iso3", values="value")
    g = {c: _growth(p.loc[1960, c], p.loc[2024, c], 64) for c in CANDIDATES}
    rows = []
    for role, t in TARGETS.items():
        c = min(g, key=lambda k: abs(g[k] - t))
        rows.append((role, c, CANDIDATES[c], round(p.loc[1960, c]), round(p.loc[2024, c]), round(g[c], 2)))
    return pd.DataFrame(rows, columns=["role", "iso3", "name", "y1960", "y2024", "growth"])


def three_speeds():
    s = speeds()
    d = wdi("NY.GDP.PCAP.KD", isos=list(s.iso3), since=1960, until=2024)
    p = d.pivot(index="year", columns="iso3", values="value").round(0)
    p = p[list(s.iso3)]
    p.columns = list(s.role)
    return p.rename_axis("year").reset_index()


def us_two_centuries():
    m = maddison(isos=["USA"], since=1820).set_index("year").gdppc
    g = _growth(m[1870], m[2022], 152) / 100
    out = pd.DataFrame({"year": m.index, "gdppc": m.round(0).values})
    out["steady"] = [round(m[1870] * (1 + g) ** (y - 1870)) if y >= 1870 else np.nan for y in m.index]
    return out


def compound():
    y = np.arange(0, 11)
    return pd.DataFrame({"year": y, "simple": 100 + 10 * y, "compound": np.round(100 * 1.1 ** y, 1)})


KESTRIA_GDPPC_2025_KESTS = 30000  # 120 000 million kests / 4 million people (g8-02 ex. 6; g9-05 pb q10)


def neighbours():
    a = load("accounts").set_index("year")
    b = (a.real_gdp / a["pop"] * 1000).round(-1)
    years = np.arange(2000, 2026)
    rng = np.random.default_rng(20261120)
    wob = np.cumsum(rng.normal(0, 0.012, len(years)))
    wob = wob - np.linspace(wob[0], wob[-1], len(years))
    rate = load("trade").set_index("year").rate[2025]
    k25 = round(KESTRIA_GDPPC_2025_KESTS * rate / (a.deflator[2025] / 100), -2)
    k00 = round(k25 / 1.04 ** 25, -2)
    k = k00 * (k25 / k00) ** ((years - 2000) / 25) * np.exp(wob)
    return pd.DataFrame({"year": years, "brenland": b.loc[years].astype(int).values, "kestria": np.round(k, -1).astype(int)})


def facts():
    u = us_two_centuries().set_index("year").gdppc
    rows = [("us_1820", u[1820]), ("us_1870", u[1870]), ("us_2022", u[2022]),
            ("us_growth_1870", round(_growth(u[1870], u[2022], 152), 2)),
            ("us_1929", u[1929]), ("us_1933", u[1933])]
    for r in speeds().itertuples():
        rows += [(f"{r.role}_1960", r.y1960), (f"{r.role}_2024", r.y2024), (f"{r.role}_growth", r.growth),
                 (f"{r.role}_ratio", round(r.y2024 / r.y1960, 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(speeds(), __file__, "speeds")
    write_table(three_speeds(), __file__, "three_speeds")
    write_table(us_two_centuries(), __file__, "us_two_centuries")
    write_table(compound(), __file__, "compound")
    write_table(neighbours(), __file__, "neighbours")
    write_table(facts(), __file__, "facts")
