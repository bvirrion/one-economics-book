"""Chart 3: business dynamism across European countries. Eurostat bd_size (business
demography by size class), business economy except public administration and holding
companies (nace_r2 B-S_X_O_S94), all size classes and ages, 2022 (in 2023 the deaths of
most large economies are still provisional, flag p; provisional values are left out,
values flagged as a break in series are kept, since the chart compares countries in one
year): ENT_BRTHR_PC, enterprises born in the year as a percentage
of active enterprises, and ENT_DTHR_PC, enterprises that died. Writes out/dynamism.csv
(countries, sorted by birth rate, with a position column) and out/dynamism_stats.csv
(EU-27 rates in 2023, the first year the aggregate has every survival measure, for
enterprises and for employment, average size at birth, survival of
the enterprises born one and two years before, the employment growth of five-year
survivors, the country medians and the cross-country correlation of the two rates)."""
import numpy as np
import pandas as pd
from econdata import eurostat
from figout import write_table

YEAR = 2022
EU_YEAR = 2023
NACE = "B-S_X_O_S94"
AGGREGATES = {"EU27_2020", "EA21", "EA20", "EA19"}


def _slice(year=YEAR):
    d = eurostat("bd_size")
    return d[(d.nace_r2 == NACE) & (d.sizeclas == "TOTAL") & (d.time == year)]


def table():
    d = _slice()
    d = d[(d.age == "TOTAL") & d.indic_sbs.isin(["ENT_BRTHR_PC", "ENT_DTHR_PC"])
          & ~d.geo.isin(AGGREGATES) & ~d.flag.fillna("").str.contains("p")]
    w = (d.pivot_table(index="geo", columns="indic_sbs", values="value").dropna()
         .rename(columns={"ENT_BRTHR_PC": "birth", "ENT_DTHR_PC": "death"}))
    w = w.sort_values("birth").reset_index()
    w["pos"] = np.arange(len(w))
    return w[["geo", "pos", "birth", "death"]]


def stats():
    d = _slice(EU_YEAR)
    eu = d[d.geo == "EU27_2020"].set_index(["age", "indic_sbs"]).value
    t = table()
    rows = {
        "countries": len(t),
        "eu_birth": eu[("TOTAL", "ENT_BRTHR_PC")], "eu_death": eu[("TOTAL", "ENT_DTHR_PC")],
        "eu_emp_birth": eu[("TOTAL", "EMP_BRTHR_PC")],
        "eu_emp_death": eu[("TOTAL", "EMP_DTHR_PC")],
        "eu_size_birth": eu[("TOTAL", "ENT_BRTH_EMPSIZE_NR")],
        "eu_surv1": eu[("Y1", "ENT_SRVLR_BRTH_PC")], "eu_surv2": eu[("Y2", "ENT_SRVLR_BRTH_PC")],
        "eu_grow5": eu[("Y5", "GRW_EMP_SRVL_PC")],
        "med_birth": t.birth.median(), "med_death": t.death.median(),
        "min_birth": t.birth.min(), "max_birth": t.birth.max(),
        "corr": np.corrcoef(t.birth, t.death)[0, 1],
    }
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


if __name__ == "__main__":
    write_table(table(), __file__, "dynamism")
    write_table(stats(), __file__, "dynamism_stats")
