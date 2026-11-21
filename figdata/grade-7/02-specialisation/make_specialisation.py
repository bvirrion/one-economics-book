"""g7-02 Specialisation and the Division of Labour.

farm_share_income.csv   iso3, income (NY.GDP.PCAP.PP.KD), farm (SL.AGR.EMPL.ZS, % of employment), 2024
farm_pairs.csv          the same, for the countries quoted in the text
people_per_farmer.csv   year + five countries: population (SP.POP.TOTL) divided by farm workers, where farm workers =
                        farm share x employed, and employed = labour force (SL.TLF.TOTL.IN) x (1 - SL.UEM.TOTL.ZS/100);
                        1991-2024 (the farm share is a modelled ILO estimate)
facts.csv               name, value
"""
import pandas as pd

from econdata import wdi
from figout import write_table

YEAR = 2024
FIVE = {"USA": "usa", "KOR": "kor", "BRA": "bra", "CHN": "chn", "IND": "ind"}
QUOTED = ["BDI", "NER", "ETH", "IND", "CHN", "BRA", "KOR", "USA", "DEU", "GBR"]


def farm_share_income():
    a = wdi("SL.AGR.EMPL.ZS", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    g = wdi("NY.GDP.PCAP.PP.KD", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    d = a.merge(g, on="iso3", suffixes=("_a", "_g")).dropna()
    d = d.rename(columns={"value_a": "farm", "value_g": "income"})
    d["farm"] = d.farm.round(1)
    d["income"] = d.income.round(0)
    return d[["iso3", "income", "farm"]].sort_values("iso3").reset_index(drop=True)


def _series(code, isos):
    w = wdi(code, isos=isos, since=1991, until=YEAR)
    return w.pivot(index="year", columns="iso3", values="value")


def people_per_farmer():
    isos = list(FIVE)
    pop, farm = _series("SP.POP.TOTL", isos), _series("SL.AGR.EMPL.ZS", isos)
    lf, un = _series("SL.TLF.TOTL.IN", isos), _series("SL.UEM.TOTL.ZS", isos)
    farmers = farm / 100 * lf * (1 - un / 100)
    r = (pop / farmers)[isos].rename(columns=FIVE).round(1)
    r.index = r.index.astype(int)
    return r.rename_axis("year").reset_index()


def facts():
    p = people_per_farmer().set_index("year")
    f = farm_share_income()
    rows = [("countries", len(f)),
            ("farm_median_below_5000", f[f.income < 5000].farm.median()),
            ("farm_median_above_40000", f[f.income > 40000].farm.median())]
    for c in FIVE.values():
        rows += [(f"ppf_{c}_1991", p[c][1991]), (f"ppf_{c}_2024", p[c][2024])]
    farm = _series("SL.AGR.EMPL.ZS", ["CHN", "KOR"]).round(1)
    rows += [("farm_chn_1991", farm.CHN[1991]), ("farm_chn_2024", farm.CHN[2024]),
             ("farm_kor_1991", farm.KOR[1991]), ("farm_kor_2024", farm.KOR[2024])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    f = farm_share_income()
    write_table(f, __file__, "farm_share_income")
    write_table(f[f.iso3.isin(QUOTED)], __file__, "farm_pairs")
    write_table(people_per_farmer(), __file__, "people_per_farmer")
    write_table(facts(), __file__, "facts")
