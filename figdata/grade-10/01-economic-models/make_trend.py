"""A constant-growth line fitted on 1870-1929 and judged on 1930-2022 (Maddison Project Database 2023).

Grade 10, chapter 1 (economic-models): the opening chart and the chart of misses.

The line is the least-squares straight line through log10(GDP per person) on 1870-1929, the
straight line that passes closest to the points on a times-ten scale. Writes:
  out/obs_usa.csv, out/obs_arg.csv   year, gdppc (2011 dollars at purchasing-power parity)
  out/trend_lines.csv                year (1870, 1880, ..., 2020, 2022), usa, arg: the fitted line
  out/trend_fit.csv                  iso3, rate (% per year), pred2022, act2022, pct (actual / predicted, %)
  out/trend_misses.csv               every candidate with at least 50 of the 60 years of 1870-1929: name, iso3, rate, pct;
                                     sorted by pct, with pos = 1, 2, ... for the bar chart
  out/trend_points.csv               iso3, y1870, y1929, y2022 for the same countries (rounded to the dollar)
"""
import numpy as np
import pandas as pd

from econdata import maddison
from figout import write_table

FIT = (1870, 1929)
END = 2022
MIN_YEARS = 50   # of the 60 years 1870-1929
CANDIDATES = ["USA", "GBR", "AUS", "CAN", "SWE", "FRA", "ARG", "URY", "CHL", "DNK", "NLD",
              "CHE", "NZL", "ESP", "ITA", "DEU", "BEL", "NOR", "FIN", "PRT", "JPN", "BRA", "MEX"]
NAMES = {"USA": "United States", "GBR": "United Kingdom", "AUS": "Australia", "CAN": "Canada",
         "SWE": "Sweden", "FRA": "France", "ARG": "Argentina", "URY": "Uruguay", "CHL": "Chile",
         "DNK": "Denmark", "NLD": "Netherlands", "CHE": "Switzerland", "NZL": "New Zealand",
         "ESP": "Spain", "ITA": "Italy", "DEU": "Germany", "BEL": "Belgium", "NOR": "Norway",
         "FIN": "Finland", "PRT": "Portugal", "JPN": "Japan", "BRA": "Brazil", "MEX": "Mexico"}


def fit(d: pd.DataFrame):
    f = d[(d.year >= FIT[0]) & (d.year <= FIT[1])]
    b, a = np.polyfit(f.year.to_numpy(float), np.log10(f.gdppc.to_numpy(float)), 1)
    return a, b, len(f)


def tables():
    m = maddison(CANDIDATES, since=FIT[0], until=END).dropna(subset=["gdppc"])
    obs, rows, lines = {}, [], {"year": list(range(1870, 2021, 10)) + [END]}
    for iso in CANDIDATES:
        d = m[m.iso3 == iso].sort_values("year")
        a, b, n = fit(d)
        pred = 10 ** (a + b * END)
        act = float(d.loc[d.year == END, "gdppc"].iloc[0])
        rows.append(dict(name=NAMES[iso], iso3=iso, n=n, rate=round((10 ** b - 1) * 100, 2),
                         pred2022=round(pred), act2022=round(act), pct=round(act / pred * 100)))
        if iso in ("USA", "ARG"):
            obs[iso] = d[["year", "gdppc"]].round({"gdppc": 0}).reset_index(drop=True)
            lines[iso.lower()] = [round(10 ** (a + b * y)) for y in lines["year"]]
    allfit = pd.DataFrame(rows)
    misses = allfit[allfit.n >= MIN_YEARS].sort_values("pct").reset_index(drop=True)
    misses.insert(0, "pos", range(1, len(misses) + 1))
    fitted = allfit[allfit.iso3.isin(["USA", "ARG"])][["iso3", "rate", "pred2022", "act2022", "pct"]]
    pts = (m[m.iso3.isin(misses.iso3) & m.year.isin([1870, 1929, END])]
           .pivot(index="iso3", columns="year", values="gdppc").round(0).astype(int))
    pts.columns = [f"y{c}" for c in pts.columns]
    pts = pts.reset_index()
    return (obs, pd.DataFrame(lines), fitted.reset_index(drop=True),
            misses[["pos", "name", "iso3", "rate", "pct"]], pts)


if __name__ == "__main__":
    obs, lines, fitted, misses, pts = tables()
    write_table(obs["USA"], __file__, "obs_usa")
    write_table(obs["ARG"], __file__, "obs_arg")
    write_table(lines, __file__, "trend_lines")
    write_table(fitted, __file__, "trend_fit")
    write_table(misses, __file__, "trend_misses")
    write_table(pts, __file__, "trend_points")
