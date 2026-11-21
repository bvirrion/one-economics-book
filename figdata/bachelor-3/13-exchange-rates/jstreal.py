"""Real exchange rates against the dollar from the Jordà--Schularick--Taylor
Macrohistory Database: q = log(xrusd) + log(cpi_USA) - log(cpi), where xrusd is
local currency per dollar; a rise is a real depreciation against the dollar."""
import numpy as np
import pandas as pd
from econdata import jst


def real_rates(since=1870, until=2020):
    j = jst(cols=["xrusd", "cpi"], since=since, until=until)
    us = j[j.iso3 == "USA"].set_index("year").cpi
    j = j[j.iso3 != "USA"].copy()
    j["q"] = np.log(j.xrusd) + np.log(j.year.map(us)) - np.log(j.cpi)
    return j[["iso3", "year", "q"]].dropna().reset_index(drop=True)


def half_life(q: pd.Series):
    """AR(1) by OLS on consecutive years: q_t = a + rho q_{t-1}; (rho, half-life)."""
    s = q.sort_index()
    prev = s.shift(1)
    ok = prev.notna() & (s.index.to_series().diff() == 1)
    rho = np.polyfit(prev[ok], s[ok], 1)[0]
    return rho, (np.log(0.5) / np.log(rho) if 0 < rho < 1 else np.nan)
