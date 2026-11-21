"""g6-04 Longer Lives, Smaller Families.

life_expectancy_early.csv / _late.csv  year + six Gapminder regions + world (two tables, so that
    the chart leaves 1950-1959 empty):
    1800-1949 Gapminder lex weighted by Gapminder pop; 1960-2024 WDI SP.DYN.LE00.IN weighted by
    SP.POP.TOTL, countries mapped to the same six regions by iso3; world from 1960 = WDI WLD.
child_mortality_income.csv   iso3, income (NY.GDP.PCAP.PP.KD, 2021 PPP dollars), mortality (SH.DYN.MORT), 2024
child_mortality_income has no country-name column (names with commas break pgfplots)
child_mortality_pairs.csv    two pairs of countries with close incomes and very different child mortality
fertility_regions.csv        year + WB regions + world, births per woman (SP.DYN.TFRT.IN), 1960-2024
facts.csv                    name, value: Gapminder child mortality 1800 min/max, urban share 1960/2025, old-age dependency 1960/2024, world lex
"""
import pandas as pd

from econdata import gapminder, wdi
from figout import write_table

R6 = ["america", "east_asia_pacific", "europe_central_asia", "middle_east_north_africa",
      "south_asia", "sub_saharan_africa"]
FERT = {"EAS": "eas", "ECS": "ecs", "LCN": "lcn", "MEA": "mea", "NAC": "nac", "SAS": "sas",
        "SSF": "ssf", "WLD": "wld"}
YEAR = 2024


def _wmean(d, by):
    d = d.assign(w=d.value * d["pop"])
    g = d.groupby(by)[["w", "pop"]].sum()
    return g.w / g["pop"]


def life_expectancy():
    lex = gapminder("lex")
    pop = gapminder("pop")[["iso3", "year", "value"]].rename(columns={"value": "pop"})
    early = lex.merge(pop, on=["iso3", "year"])
    e_reg = _wmean(early, ["year", "world_6region"]).unstack()[R6]
    e_reg["world"] = _wmean(early, "year")
    region = lex.drop_duplicates("iso3").set_index("iso3").world_6region
    le = wdi("SP.DYN.LE00.IN", countries_only=True, since=1960, until=YEAR)
    wp = wdi("SP.POP.TOTL", countries_only=True, since=1960, until=YEAR)[["iso3", "year", "value"]]
    late = le.merge(wp.rename(columns={"value": "pop"}), on=["iso3", "year"]).dropna(subset=["value", "pop"])
    late = late.assign(reg=late.iso3.map(region)).dropna(subset=["reg"])
    l_reg = _wmean(late, ["year", "reg"]).unstack()[R6]
    l_reg["world"] = wdi("SP.DYN.LE00.IN", isos="WLD", since=1960, until=YEAR).set_index("year")["value"]
    out = pd.concat([e_reg, l_reg]).round(1)
    out.index = out.index.astype(int)
    out.index.name = "year"
    return out.reset_index()


def child_mortality():
    m = wdi("SH.DYN.MORT", countries_only=True, since=YEAR, until=YEAR)[["iso3", "country", "value"]]
    g = wdi("NY.GDP.PCAP.PP.KD", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    d = m.merge(g, on="iso3", suffixes=("_m", "_g")).dropna()
    d = d.rename(columns={"value_m": "mortality", "value_g": "income"}).sort_values("iso3")
    d["income"] = d.income.round(0)
    d["mortality"] = d.mortality.round(1)
    return d[["iso3", "country", "income", "mortality"]].reset_index(drop=True)


def pairs(d):
    """For each country, the country with income within 10 % and the largest mortality ratio;
    keep the two pairs with the largest ratios, no country used twice."""
    rows = []
    for _, a in d.iterrows():
        near = d[(d.income / a.income).between(0.9, 1.1) & (d.iso3 != a.iso3)]
        for _, b in near.iterrows():
            if a.mortality > b.mortality:
                rows.append((round(a.mortality / b.mortality, 2), a.iso3, b.iso3))
    rows.sort(key=lambda r: (-r[0], r[1], r[2]))
    used, keep = set(), []
    for r, hi, lo in rows:
        if hi in used or lo in used:
            continue
        keep.append((hi, lo))
        used |= {hi, lo}
        if len(keep) == 2:
            break
    s = d.set_index("iso3")
    return pd.DataFrame([dict(high=hi, high_name=s.country[hi], high_income=s.income[hi], high_mort=s.mortality[hi],
                              low=lo, low_name=s.country[lo], low_income=s.income[lo], low_mort=s.mortality[lo])
                         for hi, lo in keep])


def fertility():
    f = wdi("SP.DYN.TFRT.IN", isos=list(FERT), since=1960, until=YEAR)
    p = f.pivot(index="year", columns="iso3", values="value")[list(FERT)].rename(columns=FERT).round(2)
    p.index = p.index.astype(int)
    return p.reset_index()


def facts():
    u = wdi("SP.URB.TOTL.IN.ZS", isos="WLD").set_index("year")["value"]
    o = wdi("SP.POP.DPND.OL", isos="WLD").set_index("year")["value"]
    c = gapminder("child_mortality_0_5_year_olds_dying_per_1000_born", since=1800, until=1800)["value"]
    return pd.DataFrame([dict(name="cm_1800_min", value=round(c.min())), dict(name="cm_1800_max", value=round(c.max())),
                         dict(name="urban_1960", value=round(u[1960], 1)), dict(name="urban_2025", value=round(u[2025], 1)),
                         dict(name="old_dep_1960", value=round(o[1960], 1)), dict(name="old_dep_2024", value=round(o[2024], 1))])


if __name__ == "__main__":
    le = life_expectancy()
    write_table(le[le.year < 1950], __file__, "life_expectancy_early")
    write_table(le[le.year >= 1960], __file__, "life_expectancy_late")
    cm = child_mortality()
    write_table(cm.drop(columns="country"), __file__, "child_mortality_income")
    write_table(pairs(cm), __file__, "child_mortality_pairs")
    write_table(fertility(), __file__, "fertility_regions")
    write_table(facts(), __file__, "facts")
