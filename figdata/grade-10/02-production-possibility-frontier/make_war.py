"""Output, consumption, unemployment and central government spending, United States and United
Kingdom, 1929-1950 (Jorda-Schularick-Taylor Macrohistory Database).

Grade 10, chapter 2 (production-possibility-frontier): an economy inside its frontier (the
United States, 1939) and one near it (the United Kingdom) turning to war production.
Writes out/war_usa.csv and out/war_gbr.csv:
  year; gdp_pp, cons_pp: real GDP and real consumption per person, index 1939 = 100 (JST rgdpbarro,
  rconsbarro); unemp: unemployment rate (%); gshare: central government expenditure as % of GDP.
"""
from econdata import jst
from figout import write_table

BASE = 1939


def table(iso):
    d = jst([iso], since=1929, until=1950).set_index("year").sort_index()
    b = d.loc[BASE]
    out = d.assign(gdp_pp=(d.rgdpbarro / b.rgdpbarro * 100).round(1),
                   cons_pp=(d.rconsbarro / b.rconsbarro * 100).round(1),
                   unemp=d.unemp.round(1),
                   gshare=(d.expenditure / d.gdp * 100).round(1))
    return out[["gdp_pp", "cons_pp", "unemp", "gshare"]].reset_index()


if __name__ == "__main__":
    write_table(table("USA"), __file__, "war_usa")
    write_table(table("GBR"), __file__, "war_gbr")
