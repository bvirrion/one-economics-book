"""g6-06 Food and Energy.

cereal_yields.csv   year + six FAO areas, cereal yield in tonnes per hectare, 1961-2024 (FAOSTAT)
energy_income.csv   iso3, income (NY.GDP.PCAP.PP.KD), energy (EG.USE.PCAP.KG.OE, kg of oil equivalent), 2024
energy_pairs.csv    iso3, income, energy for the countries quoted in the text
food_quintiles.csv  quintile, income, spending, food, food_share_spending, food_share_income
                    (BLS Consumer Expenditure Surveys 2025, table 1101, means per consumer unit)
so2.csv             year + five countries, sulphur dioxide emissions in millions of tonnes, 1850-2023 (CEDS)
facts.csv           name, value: SO2 peaks and values, CO2 per person 2023 (CEDS co2 / SP.POP.TOTL), water use
brenland_food.csv   quarter, disposable, food, consumption, share (Brenland survey 2025, quarters of disposable income)
"""
import pandas as pd

from country import load
from econdata import ceds, cex_table, faostat_crops, wdi
from figout import write_table

AREAS = {"World": "world", "Africa": "africa", "Asia": "asia", "Europe": "europe",
         "Northern America": "n_america", "South America": "s_america"}
SO2 = {"GBR": "gbr", "USA": "usa", "DEU": "deu", "CHN": "chn", "IND": "ind"}
YEAR = 2024
QUOTED = ["USA", "DEU", "SAU", "CHE", "IND", "NGA", "CHN", "ISL", "TCD"]


def yields():
    f = faostat_crops("Cereals, primary", "Yield")
    p = f[f.Area.isin(list(AREAS))].pivot(index="Year", columns="Area", values="Value")[list(AREAS)]
    p = (p / 1000).round(2).rename(columns=AREAS)
    p.index = p.index.astype(int)
    p.index.name = "year"
    return p.reset_index()


def energy():
    e = wdi("EG.USE.PCAP.KG.OE", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    g = wdi("NY.GDP.PCAP.PP.KD", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    d = e.merge(g, on="iso3", suffixes=("_e", "_g")).dropna()
    d = d.rename(columns={"value_e": "energy", "value_g": "income"}).sort_values("iso3")
    d["energy"] = d.energy.round(0)
    d["income"] = d.income.round(0)
    return d[["iso3", "income", "energy"]].reset_index(drop=True)


def food_quintiles():
    t = cex_table("mean-item-share-average-standard-error", 2025)
    lab = t.iloc[:, 0].astype(str).str.strip()

    def mean_after(label):
        i = lab[lab == label].index[0]
        j = lab.loc[i:].index[(lab.loc[i:] == "Mean").values][0]
        return pd.to_numeric(t.loc[j].iloc[2:7]).values

    inc, spend, food = mean_after("Income before taxes"), mean_after("Average annual expenditures"), mean_after("Food")
    d = pd.DataFrame({"quintile": [1, 2, 3, 4, 5], "income": inc, "spending": spend, "food": food})
    d["food_share_spending"] = (100 * d.food / d.spending).round(1)
    d["food_share_income"] = (100 * d.food / d.income).round(1)
    return d


def so2():
    s = ceds("so2", isos=list(SO2), since=1850, until=2023)
    p = s.pivot(index="year", columns="iso3", values="value")[list(SO2)].rename(columns=SO2)
    p = (p / 1000).round(2)
    p.index = p.index.astype(int)
    return p.reset_index()


def facts():
    p = so2().set_index("year")
    rows = []
    for c in SO2.values():
        rows += [dict(name=f"so2_{c}_peak_year", value=int(p[c].idxmax())), dict(name=f"so2_{c}_peak", value=p[c].max()),
                 dict(name=f"so2_{c}_2023", value=p[c][2023])]
    co2 = ceds("co2", isos=["USA", "DEU", "CHN", "IND", "NGA"], since=2023, until=2023).set_index("iso3")["value"]
    pop = wdi("SP.POP.TOTL", isos=["USA", "DEU", "CHN", "IND", "NGA"], since=2023, until=2023).set_index("iso3")["value"]
    for i in co2.index:
        rows.append(dict(name=f"co2_pc_{i.lower()}_2023", value=round(co2[i] * 1000 / pop[i], 1)))   # kt -> t per person
    w = wdi("ER.H2O.FWTL.ZS", isos="WLD").dropna().set_index("year")["value"]
    rows.append(dict(name="water_withdrawal_year", value=int(w.index.max())))
    rows.append(dict(name="water_withdrawal_pct", value=round(w.iloc[-1], 1)))
    return pd.DataFrame(rows)


def brenland_food():
    h = load("households")
    h = h.assign(quarter=pd.qcut(h.disposable, 4, labels=[1, 2, 3, 4]).astype(int))
    g = h.groupby("quarter")[["disposable", "food", "consumption"]].mean().round(0).reset_index()
    g["share"] = (100 * g.food / g.consumption).round(1)
    return g


if __name__ == "__main__":
    write_table(yields(), __file__, "cereal_yields")
    en = energy()
    write_table(en, __file__, "energy_income")
    write_table(en[en.iso3.isin(QUOTED)], __file__, "energy_pairs")
    write_table(food_quintiles(), __file__, "food_quintiles")
    write_table(so2(), __file__, "so2")
    write_table(facts(), __file__, "facts")
    write_table(brenland_food(), __file__, "brenland_food")
