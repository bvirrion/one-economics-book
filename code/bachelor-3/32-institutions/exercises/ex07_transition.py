"""Exercise 7: the transition recessions. For four economies, GDP per person
(Maddison Project 2023) as an index with 1989 = 100: the trough, its depth, the
number of years from 1989 to the trough, and the first year back at the 1989 level."""
from econdata import maddison

COUNTRIES = {"POL": "Poland", "CZE": "Czechia", "RUS": "Russia", "UKR": "Ukraine"}
m = maddison(isos=list(COUNTRIES), since=1989, until=2022)
w = m.pivot(index="year", columns="iso3", values="gdppc")
for iso, name in COUNTRIES.items():
    s = 100 * w[iso] / w[iso][1989]
    trough = s.idxmin()
    later = s[(s.index > trough) & (s >= 100)]
    back = later.index[0] if len(later) else "not by 2022"
    print(f"{name:8s} trough {trough} at {s.min():5.1f} "
          f"(a fall of {100 - s.min():4.1f} %, {trough - 1989} years); back in {back}")
