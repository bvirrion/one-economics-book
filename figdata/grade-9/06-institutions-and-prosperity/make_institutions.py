"""g9-06 Why Some Countries Are Rich: Institutions.

koreas.csv          year, south, north: GDP per person, 2011 dollars (Maddison Project, KOR and PRK), 1940-2022; North
                    Korea has no estimate for 1944-1989 (written nan, the line breaks)
china.csv           year, gdppc: China, 1950-2022 (Maddison Project)
bribery_income.csv  iso3, year, income, bribery: share of firms asked for a bribe (percent; World Bank Enterprise
                    Surveys via WDI IC.FRM.BRIB.ZS), latest survey per country since 2016, against GDP per person at PPP in
                    that year (WDI NY.GDP.PCAP.PP.KD, 2021 dollars)
valleys.csv         year, a, b, ratio: the weekend problem's two invented valleys (output per person)
facts.csv           name, value
"""
import math

import pandas as pd

from econdata import maddison, wdi
from figout import write_table

SINCE_SURVEY = 2016
GROWTH_A, GROWTH_B, GROWTH_B_REFORM = 0.03, 0.01, 0.05


def koreas():
    k = maddison(["KOR", "PRK"], since=1940).pivot(index="year", columns="iso3", values="gdppc")
    k = k.reindex(range(1940, 2023)).rename(columns={"KOR": "south", "PRK": "north"})
    return k[["south", "north"]].round(0).reset_index()


def china():
    return maddison(["CHN"], since=1950)[["year", "gdppc"]].round(0).reset_index(drop=True)


def bribery_income():
    b = wdi("IC.FRM.BRIB.ZS", since=SINCE_SURVEY, countries_only=True).dropna(subset=["value"])
    b = b.sort_values("year").groupby("iso3").tail(1)[["iso3", "year", "value"]].rename(columns={"value": "bribery"})
    i = wdi("NY.GDP.PCAP.PP.KD", since=SINCE_SURVEY, countries_only=True)[["iso3", "year", "value"]]
    d = b.merge(i.rename(columns={"value": "income"}), on=["iso3", "year"]).dropna()
    d["income"] = d.income.round()
    d["bribery"] = d.bribery.round(1)
    return d[["iso3", "year", "income", "bribery"]].sort_values("income").reset_index(drop=True)


def valleys():
    """Twenty years apart (A 3 %, B 1 %), then B reformed (5 %) while A keeps 3 %; values rounded each year."""
    rows, a, b = [], 1000.0, 1000.0
    for y in range(0, 41):
        rows.append((y, round(a), round(b), round(a / b, 3)))
        a *= 1 + GROWTH_A
        b *= 1 + (GROWTH_B if y < 20 else GROWTH_B_REFORM)
    return pd.DataFrame(rows, columns=["year", "a", "b", "ratio"])


def facts():
    k = koreas().set_index("year")
    c = china().set_index("year").gdppc
    rows = [(f"kor_{s}_{y}", k.loc[y, s]) for s in ["south", "north"] for y in [1940, 1990, 2022]]
    rows += [("kor_ratio_2022", round(k.south[2022] / k.north[2022], 1)),
             ("kor_south_growth_90_22", round(((k.south[2022] / k.south[1990]) ** (1 / 32) - 1) * 100, 1)),
             ("kor_north_growth_90_22", round(((k.north[2022] / k.north[1990]) ** (1 / 32) - 1) * 100, 1)),
             ("chn_1950", c[1950]), ("chn_1978", c[1978]), ("chn_2022", c[2022]),
             ("chn_ratio_78_22", round(c[2022] / c[1978], 2)),
             ("chn_growth_50_78", round(((c[1978] / c[1950]) ** (1 / 28) - 1) * 100, 1)),
             ("chn_growth_78_22", round(((c[2022] / c[1978]) ** (1 / 44) - 1) * 100, 1))]
    d = bribery_income()
    rows += [("brib_n", len(d)), ("brib_median_below_5000", round(d[d.income < 5000].bribery.median(), 1)),
             ("brib_n_below_5000", int((d.income < 5000).sum())),
             ("brib_median_above_30000", round(d[d.income > 30000].bribery.median(), 1)),
             ("brib_n_above_30000", int((d.income > 30000).sum()))]
    v = valleys().set_index("year")
    target = 1 + (v.ratio[20] - 1) / 2
    halved = int(v[(v.index > 20) & (v.ratio <= target)].index[0])
    rows += [("valley_a_20", v.a[20]), ("valley_b_20", v.b[20]), ("valley_ratio_20", v.ratio[20]),
             ("valley_target_ratio", round(target, 3)), ("valley_halved_year", halved),
             ("valley_halved_years_after_reform", halved - 20),
             ("valley_halved_exact", round(math.log(v.ratio[20] / target) / math.log(1.05 / 1.03), 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


def nan_csv(df):
    return df.astype(object).where(df.notna(), "nan")


if __name__ == "__main__":
    write_table(nan_csv(koreas()), __file__, "koreas")
    write_table(china(), __file__, "china")
    write_table(bribery_income(), __file__, "bribery_income")
    write_table(valleys(), __file__, "valleys")
    write_table(facts(), __file__, "facts")
