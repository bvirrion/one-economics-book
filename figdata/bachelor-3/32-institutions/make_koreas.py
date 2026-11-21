"""Chart 2: GDP per person in South and North Korea, 1990--2022 (Maddison Project
2023; the North Korea series starts in 1990). Writes out/korea_south.csv,
out/korea_north.csv and out/koreas_stats.csv."""
import pandas as pd
from econdata import maddison
from figout import write_table


def tables():
    m = maddison(isos=["KOR", "PRK"], since=1990, until=2022).dropna(subset=["gdppc"])
    w = m.pivot(index="year", columns="iso3", values="gdppc")
    st = pd.DataFrame({"stat": ["kor1990", "prk1990", "kor2022", "prk2022",
                                "ratio1990", "ratio2022"],
                       "value": [w.KOR[1990], w.PRK[1990], w.KOR[2022], w.PRK[2022],
                                 w.KOR[1990] / w.PRK[1990], w.KOR[2022] / w.PRK[2022]]})
    south = w.KOR.rename("gdppc").reset_index()
    north = w.PRK.rename("gdppc").reset_index()
    return south, north, st


if __name__ == "__main__":
    s, n, st = tables()
    write_table(s, __file__, "korea_south")
    write_table(n, __file__, "korea_north")
    write_table(st, __file__, "koreas_stats")
