"""Opening chart: GDP per person in China, 1950--2022, and Maddison's own regional
estimates for Western and Eastern Europe (2011 dollars; the regional rows exist for
1950, every ten years to 2010, then every year from 2015). Writes out/china.csv,
out/europe_west.csv, out/europe_east.csv and out/opening_stats.csv."""
import numpy as np
import pandas as pd
from econdata import maddison, maddison_regions
from figout import write_table


def tables():
    c = maddison(isos=["CHN"], since=1950, until=2022)[["year", "gdppc"]].dropna()
    r = maddison_regions(["Western Europe", "Eastern Europe"], since=1950)
    w = r.pivot(index="year", columns="region", values="gdppc")
    west = w["Western Europe"].dropna().rename("gdppc").reset_index()
    east = w["Eastern Europe"].dropna().rename("gdppc").reset_index()
    s = c.set_index("year").gdppc
    st = {"chn1950": s[1950], "chn1978": s[1978], "chn2022": s[2022],
          "g50_78": 100 * np.log(s[1978] / s[1950]) / 28,
          "g78_22": 100 * np.log(s[2022] / s[1978]) / 44}
    for y in (1950, 1990, 2022):
        ratio = w.loc[y, "Eastern Europe"] / w.loc[y, "Western Europe"]
        st[f"east_west_{y}"] = 100 * ratio
    return c, west, east, pd.DataFrame({"stat": list(st), "value": list(st.values())})


if __name__ == "__main__":
    c, west, east, st = tables()
    write_table(c, __file__, "china")
    write_table(west, __file__, "europe_west")
    write_table(east, __file__, "europe_east")
    write_table(st, __file__, "opening_stats")
