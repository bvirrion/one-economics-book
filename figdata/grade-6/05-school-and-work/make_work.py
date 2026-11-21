"""g6-05 School and Work.

literacy.csv      year + WB regions + world, adult literacy rate (%), 1975-2024 (WDI SE.ADT.LITR.ZS; blank = none)
hours_worked.csv  year + six countries, average yearly hours per worker, 1950-2023 (PWT 11.0 avh)
sectors_china.csv year, agriculture, industry, services (% of employment, China; WDI SL.*.EMPL.ZS, ILO modelled)
facts.csv         name, value: women's labour-force participation, world, 1990 and 2025 (SL.TLF.CACT.FE.ZS);
                  year services passed agriculture in China
"""
import pandas as pd

from econdata import pwt, wdi
from figout import write_table

LIT = {"EAS": "eas", "LCN": "lcn", "MEA": "mea", "SAS": "sas", "SSF": "ssf", "WLD": "wld"}
HOURS = {"USA": "usa", "GBR": "gbr", "FRA": "fra", "DEU": "deu", "JPN": "jpn", "KOR": "kor"}


def literacy():
    d = wdi("SE.ADT.LITR.ZS", isos=list(LIT), since=1975, until=2024)
    p = d.pivot(index="year", columns="iso3", values="value")[list(LIT)].rename(columns=LIT).round(1)
    p.index = p.index.astype(int)
    return p.reset_index()


def hours():
    d = pwt(list(HOURS), since=1950, cols=["avh"])
    p = d.pivot(index="year", columns="iso3", values="avh")[list(HOURS)].rename(columns=HOURS).round(0)
    p.index = p.index.astype(int)
    return p.reset_index()


def sectors():
    cols = {"SL.AGR.EMPL.ZS": "agriculture", "SL.IND.EMPL.ZS": "industry", "SL.SRV.EMPL.ZS": "services"}
    s = pd.concat({v: wdi(k, isos="CHN").set_index("year")["value"] for k, v in cols.items()}, axis=1).dropna().round(1)
    s.index = s.index.astype(int)
    s.index.name = "year"
    return s.reset_index()


def facts():
    f = wdi("SL.TLF.CACT.FE.ZS", isos="WLD").set_index("year")["value"]
    s = sectors().set_index("year")
    passed = int(s.index[(s.services > s.agriculture).values][0])
    return pd.DataFrame([dict(name="women_lfp_1990", value=round(f[1990], 1)),
                         dict(name="women_lfp_2025", value=round(f[2025], 1)),
                         dict(name="china_services_pass_year", value=passed)])


if __name__ == "__main__":
    write_table(literacy(), __file__, "literacy")
    write_table(hours(), __file__, "hours_worked")
    write_table(sectors(), __file__, "sectors_china")
    write_table(facts(), __file__, "facts")
