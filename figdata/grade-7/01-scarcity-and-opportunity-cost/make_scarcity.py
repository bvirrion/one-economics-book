"""g7-01 Scarcity and Opportunity Cost.

hours_income.csv    iso3, income (PWT 11.0 rgdpe/pop, dollars of 2021 per person), hours (avh, hours worked per
                    worker in the year), 2023, every country with both
hours_pairs.csv     the same, for the countries quoted in the text
meals_away.csv      quintile, food, away, away_share: spending on food away from home as a percent of all food
                    spending, by income quintile (BLS Consumer Expenditure Surveys 2025, table 1101)
facts.csv           name, value: correlation sign check, hours of the poorest and richest thirds
"""
import pandas as pd

from econdata import cex_table, pwt
from figout import write_table

YEAR = 2023
QUOTED = ["DEU", "NLD", "NOR", "USA", "KOR", "IND", "BGD", "COL", "KHM"]


def hours_income():
    d = pwt(since=YEAR, until=YEAR, cols=["avh", "rgdpe", "pop"]).dropna()
    d = d.assign(income=(d.rgdpe / d["pop"]).round(0), hours=d.avh.round(0))
    return d[["iso3", "income", "hours"]].sort_values("iso3").reset_index(drop=True)


def _mean_after(t, lab, label):
    i = lab[lab == label].index[0]
    j = lab.loc[i:].index[(lab.loc[i:] == "Mean").values][0]
    return pd.to_numeric(t.loc[j].iloc[2:7]).values


def meals_away():
    t = cex_table("mean-item-share-average-standard-error", 2025)
    lab = t.iloc[:, 0].fillna("").astype(str).str.strip()
    d = pd.DataFrame({"quintile": [1, 2, 3, 4, 5], "food": _mean_after(t, lab, "Food"),
                      "away": _mean_after(t, lab, "Food away from home")})
    d["away_share"] = (100 * d.away / d.food).round(1)
    return d


def facts():
    h = hours_income().sort_values("income")
    n = len(h) // 3
    return pd.DataFrame([
        ("countries", len(h)),
        ("hours_poorest_third_median", h.head(n).hours.median()),
        ("hours_richest_third_median", h.tail(n).hours.median()),
        ("third_size", n),
    ], columns=["name", "value"])


if __name__ == "__main__":
    h = hours_income()
    write_table(h, __file__, "hours_income")
    write_table(h[h.iso3.isin(QUOTED)], __file__, "hours_pairs")
    write_table(meals_away(), __file__, "meals_away")
    write_table(facts(), __file__, "facts")
