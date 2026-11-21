"""Chart 4: old-age dependency ratio (people 65 and over per 100 aged 15--64),
1960--2025, six economies (WDI SP.POP.DPND.OL). Writes out/dep_<iso3>.csv and
out/dependency_stats.csv."""
import pandas as pd
from econdata import wdi
from figout import write_table

SHOWN = ["JPN", "ITA", "FRA", "USA", "CHN", "NGA"]


def tables():
    w = wdi("SP.POP.DPND.OL", isos=SHOWN, since=1960, until=2025)
    w = w.dropna(subset=["value"])
    out = {c: w[w.iso3 == c][["year", "value"]].rename(columns={"value": "dep"})
           .reset_index(drop=True) for c in SHOWN}
    st = pd.DataFrame([{"iso3": c, "y1960": d.set_index("year").dep[1960],
                        "y2025": d.set_index("year").dep[2025]}
                       for c, d in out.items()])
    return out, st


if __name__ == "__main__":
    out, st = tables()
    for c, d in out.items():
        write_table(d, __file__, f"dep_{c}")
    write_table(st, __file__, "dependency_stats")
