"""Chart 3: the transition recessions. GDP per person in Poland, Czechia, Russia and
Ukraine, 1985--2022, as an index with 1989 = 100 (Maddison Project 2023, which
gives the successor states' own series back to the 1970s or earlier). Writes
out/transition_<iso3>.csv and out/transition_stats.csv (trough year, trough index,
first year back at 100 after the trough, index in 2022)."""
import pandas as pd
from econdata import maddison
from figout import write_table

SHOWN = ["POL", "CZE", "RUS", "UKR"]


def index():
    m = maddison(isos=SHOWN, since=1985, until=2022)
    w = m.pivot(index="year", columns="iso3", values="gdppc")[SHOWN]
    return 100 * w / w.loc[1989]


def stats(i):
    rows = []
    for c in SHOWN:
        s = i[c]
        t = s.idxmin()
        back = s[(s.index > t) & (s >= 100)].index
        rows.append({"iso3": c, "trough_year": t, "trough": s.min(),
                     "back_year": back.min() if len(back) else 0,
                     "y2022": s[2022]})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    i = index()
    for c in SHOWN:
        write_table(i[c].rename("idx").reset_index(), __file__, f"transition_{c}")
    write_table(stats(i), __file__, "transition_stats")
