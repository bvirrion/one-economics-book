"""g7-08 Firms: Costs, Revenue and Profit.

survival.csv         years, eu, nl, it, de, fr: of 100 enterprises born in 2021, how many were still active after 0..3
                     years (Eurostat bd_size, ENT_SRVLR_BRTH_CHB_PC, business economy B-S except O and S94)
survival_sector.csv  pos, label, value: EU, enterprises born in 2021 still active after three years, by sector, percent
brenland_sectors.csv sector, loss_share, margin: Brenland census of 500 firms: percent of firms with a loss, and total
                     profit per 100 dalens of output, by sector (invented)
bakery.csv           q, revenue, cost, profit: the chapter's worked example (price 2, fixed cost 3000, 0.80 per loaf)
facts.csv            name, value
"""
import pandas as pd

from country import load
from econdata import eurostat
from figout import write_table

COUNTRIES = {"EU27_2020": "eu", "NL": "nl", "IT": "it", "DE": "de", "FR": "fr"}
SECTORS = {"Q": "Health and social work", "L": "Real estate", "D": "Electricity and gas supply", "C": "Manufacturing",
           "J": "Information and communication", "M": "Professional and scientific", "F": "Construction",
           "I": "Hotels and restaurants", "G": "Shops and wholesale trade", "N": "Office and support services",
           "H": "Transport and storage"}


def _surv():
    d = eurostat("bd_size")
    return d[(d.sizeclas == "TOTAL") & (d.indic_sbs == "ENT_SRVLR_BRTH_CHB_PC") & (d.time == 2021)]


def survival():
    d = _surv()
    d = d[(d.nace_r2 == "B-S_X_O_S94") & d.geo.isin(list(COUNTRIES))]
    p = d.pivot_table(index="age", columns="geo", values="value").round(1)
    p.index = [int(a[1:]) for a in p.index]
    p = pd.concat([pd.DataFrame({g: [100.0] for g in p.columns}, index=[0]), p])
    p = p[list(COUNTRIES)].rename(columns=COUNTRIES)
    return p.rename_axis("years").reset_index()


def survival_sector():
    d = _surv()
    d = d[(d.geo == "EU27_2020") & (d.age == "Y3") & d.nace_r2.isin(list(SECTORS))]
    d = d.assign(label=d.nace_r2.map(SECTORS), value=d.value.round(1)).sort_values("value")
    d["pos"] = range(1, len(d) + 1)
    return d[["pos", "label", "value"]]


def brenland_sectors():
    f = load("firms")
    g = f.groupby("sector")
    return pd.DataFrame({"sector": list(g.groups),
                         "firms": g.size().values,
                         "losses": g.profit.apply(lambda s: int((s < 0).sum())).values,
                         "loss_share": (100 * g.profit.apply(lambda s: (s < 0).mean())).round(1).values,
                         "margin": (100 * g.profit.sum() / g.output.sum()).round(1).values})


def bakery():
    q = pd.Series([0, 1000, 2000, 2500, 3000, 4000])
    rev, cost = 2 * q, 3000 + 0.8 * q
    return pd.DataFrame({"q": q, "revenue": rev, "cost": cost.round(0).astype(int), "profit": (rev - cost).round(0).astype(int)})


def facts():
    s = survival().set_index("years")
    d = eurostat("bd_size")
    fi = d[(d.sizeclas == "TOTAL") & (d.indic_sbs == "ENT_SRVLR_BRTH_CHB_PC") & (d.time == 2019)
           & (d.nace_r2 == "B-S_X_O_S94") & (d.geo == "FI")].set_index("age").value.round(1)
    rows = [("eu_y1", s.eu[1]), ("eu_y3", s.eu[3]), ("nl_y3", s.nl[3]), ("fr_y3", s.fr[3]),
            ("fi2019_y5", fi["Y5"])]
    n = d[(d.nace_r2 == "B-S_X_O_S94") & (d.sizeclas == "TOTAL") & (d.geo == "EU27_2020") & (d.age == "TOTAL")
          & (d.time == 2021)].set_index("indic_sbs").value
    rows += [("eu_births_2021_millions", round(n["ENT_BRTH_NR"] / 1e6, 1)),
             ("eu_firms_2021_millions", round(n["ENT_NR"] / 1e6, 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(survival(), __file__, "survival")
    write_table(survival_sector(), __file__, "survival_sector")
    write_table(brenland_sectors(), __file__, "brenland_sectors")
    write_table(bakery(), __file__, "bakery")
    write_table(facts(), __file__, "facts")
