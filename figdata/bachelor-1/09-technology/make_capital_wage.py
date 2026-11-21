"""Charts of b1 ch. 9 (PWT 11.0).

Opening: capital per hour worked (cn / (emp * avh)) against labour compensation per
hour (labsh * cgdpo / (emp * avh)), 2019, both 2021 dollars at PPP, every country with
the data; least-squares slope of the logs.
Second: the capital-labour ratio (rnna per hour) and the wage-rental ratio
(labsh / (1 - labsh) * rnna / hours), United States and Korea, 1953-2019, both
indexed to 1980 = 1, and the log slopes 1980-2019.
"""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

d = pwt(None, 2019, 2019, ["cn", "emp", "avh", "labsh", "cgdpo"]).dropna()
d = d[(d.emp > 0) & (d.avh > 0)]
hours = d.emp * d.avh
d["kph"] = (d.cn / hours).round(2)
d["wph"] = (d.labsh * d.cgdpo / hours).round(2)
lab = d.labsh.quantile([0.1, 0.9]).round(2)
d["country"] = d.country.str.replace(",", "")
d = d[["iso3", "country", "kph", "wph"]].sort_values("iso3")
slope, icept = np.polyfit(np.log(d.wph), np.log(d.kph), 1)
corr = np.corrcoef(np.log(d.wph), np.log(d.kph))[0, 1]
write_table(d, __file__, "capital_wage_2019")
x = np.array([d.wph.min(), d.wph.max()])
write_table(pd.DataFrame({"wph": x.round(2), "fit": np.exp(icept + slope * np.log(x)).round(2)}),
            __file__, "capital_wage_fit")
write_table(pd.DataFrame([{"n": len(d), "slope": round(slope, 2), "corr": round(corr, 2),
                            "labsh_p10": lab[0.1], "labsh_p90": lab[0.9]}]),
            __file__, "capital_wage_stats")



def drop_backfill(df, col):
    """Drop, country by country, the opening run of identical values of col
    except its last year: PWT fills the years before a country's first
    labour-share observation with that value (Korea before 1970)."""
    keep = []
    for _, g in df.dropna(subset=[col]).sort_values("year").groupby("iso3"):
        v = g[col].to_numpy()
        k = 0
        while k + 1 < len(v) and v[k + 1] == v[0]:
            k += 1
        keep.append(g.iloc[k:])
    return pd.concat(keep)


t = drop_backfill(pwt(["USA", "KOR"], 1953, 2019, ["rnna", "emp", "avh", "labsh"]).dropna(), "labsh")
t["kl"] = t.rnna / (t.emp * t.avh)
t["wr"] = t.labsh / (1 - t.labsh) * t.kl
rows, slopes = [], []
for iso, g in t.groupby("iso3"):
    g = g.set_index("year")
    base = g.loc[1980]
    rows.append(pd.DataFrame({"year": g.index, "iso3": iso, "kl": (g.kl / base.kl).round(3),
                              "wr": (g.wr / base.wr).round(3)}))
    a, b = g.loc[1980], g.loc[2019]
    s = np.log(b.kl / a.kl) / np.log(b.wr / a.wr)
    slopes.append({"iso3": iso, "first": int(g.index.min()), "kl2019": round(b.kl / a.kl, 3),
                   "wr2019": round(b.wr / a.wr, 3), "sigma": round(s, 2),
                   "labsh1980": round(a.labsh, 3), "labsh2019": round(b.labsh, 3)})
s = pd.concat(rows)
w = s.pivot(index="year", columns="iso3", values=["kl", "wr"])
w.columns = [f"{v}_{i.lower()}" for v, i in w.columns]
write_table(w.reset_index(), __file__, "kl_wr_paths")
write_table(pd.DataFrame(slopes), __file__, "kl_wr_slopes")
