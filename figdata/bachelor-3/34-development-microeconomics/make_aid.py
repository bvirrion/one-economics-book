"""Chart 3: aid and growth. Country averages, 1990--2019, of net official development
assistance received (% of GNI, WDI DT.ODA.ODAT.GN.ZS) and of growth of GDP per person
(WDI NY.GDP.PCAP.KD.ZG), for countries with at least 20 years of both. Writes
out/aid.csv, out/aid_fit.csv and out/aid_stats.csv."""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table


def table():
    a = wdi("DT.ODA.ODAT.GN.ZS", since=1990, until=2019, countries_only=True)
    g = wdi("NY.GDP.PCAP.KD.ZG", since=1990, until=2019, countries_only=True)
    am = a.dropna(subset=["value"]).groupby("iso3").value.agg(["mean", "count"])
    gm = g.dropna(subset=["value"]).groupby("iso3").value.agg(["mean", "count"])
    d = am.add_suffix("_a").join(gm.add_suffix("_g")).dropna()
    d = d[(d.count_a >= 20) & (d.count_g >= 20) & (d.mean_a > 0)]
    return pd.DataFrame({"iso3": d.index, "aid": d.mean_a.to_numpy(),
                         "growth": d.mean_g.to_numpy()}).reset_index(drop=True)


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "aid")
    b, a = np.polyfit(d.aid, d.growth, 1)
    xs = np.array([0, d.aid.max()])
    write_table(pd.DataFrame({"aid": xs, "growth": a + b * xs}), __file__, "aid_fit")
    r = np.corrcoef(d.aid, d.growth)[0, 1]
    write_table(pd.DataFrame({"stat": ["n", "slope", "corr"], "value": [len(d), b, r]}),
                __file__, "aid_stats")
