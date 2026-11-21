"""Exercise 5: the long decline of annual hours (Penn World Table, avh).

Average annual change in log hours per person employed, from 1950 or the first year
whose value is observed rather than interpolated (Germany 1960, Japan 1953, Korea
1963: before these the source's series grows at a constant rate), to 2023.
"""
import numpy as np
from econdata import pwt

FIRST = {"DEU": 1960, "JPN": 1953, "KOR": 1963}
p = pwt(cols=["avh"]).dropna(subset=["avh"])
for iso in ["USA", "DEU", "FRA", "GBR", "JPN", "KOR"]:
    s = p[p.iso3 == iso].set_index("year").avh
    y0 = FIRST.get(iso, 1950)
    g = 100 * (np.log(s.loc[2023]) - np.log(s.loc[y0])) / (2023 - y0)
    print(f"{iso}: {s.loc[y0]:.0f} hours in {y0}, {s.loc[2023]:.0f} in 2023, "
          f"{g:.2f} % a year")
