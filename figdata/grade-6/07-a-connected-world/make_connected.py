"""g6-07 A Connected World.

trade_share.csv         year, jst_median (1870-2020: median over the 18 JST economies of exports plus imports as a
                        percent of GDP), world (1970-2024: WDI NE.TRD.GNFS.ZS, WLD); empty where a series has no data
mobile_early.csv        year, mobile (WDI IT.CEL.SETS.P2, WLD), 1987-1999 (the world aggregate stops in 1999 ...)
connections.csv         year, mobile, internet (IT.NET.USER.ZS, WLD), 2005-2024 (... and restarts in 2005)
computer_prices.csv     year, index: euro-area HICP for information-processing equipment (CP0913) divided by
                        all items (CP00), 1996 = 100 (Eurostat prc_hicp_aind, EA)
facts.csv               name, value
brenland_trade.csv      year, gdp, exports, imports, share, to_kestria, from_kestria (Brenland, 2000 and 2025)
"""
import pandas as pd

from cited import load_cited
from country import load
from econdata import bls_cpi, eurostat, jst, wdi
from figout import write_table


def trade_share():
    j = jst(cols=["exports", "imports", "gdp"]).dropna(subset=["exports", "imports", "gdp"])
    j = j.assign(ts=100 * (j.exports + j.imports) / j.gdp)
    m = j.groupby("year").ts.median().round(1).rename("jst_median")
    w = wdi("NE.TRD.GNFS.ZS", isos="WLD", until=2024).dropna().set_index("year").value.round(1).rename("world")
    d = pd.concat([m, w], axis=1).sort_index()
    d.index = d.index.astype(int)
    d.index.name = "year"
    return d.reset_index()


def _wld(code):
    s = wdi(code, isos="WLD").dropna().set_index("year").value.round(1)
    s.index = s.index.astype(int)
    return s


def mobile_early():
    s = _wld("IT.CEL.SETS.P2")
    return s.loc[1987:1999].rename("mobile").rename_axis("year").reset_index()


def connections():
    d = pd.concat([_wld("IT.CEL.SETS.P2").rename("mobile"), _wld("IT.NET.USER.ZS").rename("internet")], axis=1)
    return d.loc[2005:2024].rename_axis("year").reset_index()


def computer_prices():
    e = eurostat("prc_hicp_aind")
    x = e[(e.geo == "EA") & (e.unit == "INX_A_AVG") & e.coicop.isin(["CP0913", "CP00"])]
    x = x.pivot(index="time", columns="coicop", values="value").sort_index()
    r = x.CP0913 / x.CP00
    return (100 * r / r.iloc[0]).round(2).rename("index").rename_axis("year").reset_index()


def facts():
    t = trade_share().set_index("year")
    m = _wld("IT.CEL.SETS.P2")
    i = _wld("IT.NET.USER.ZS")
    cp = computer_prices().set_index("year")["index"]
    cpi = bls_cpi()
    cpi = cpi[cpi.period == "M13"].set_index("year").value
    call = load_cited(__file__, "call").iloc[0]
    jst_n = jst(cols=["exports", "imports", "gdp"]).dropna(subset=["exports", "imports", "gdp"]).iso3.nunique()
    sgp = wdi("NE.TRD.GNFS.ZS", isos="SGP", since=2024, until=2024).value.iloc[0]
    rows = [("jst_economies", jst_n)]
    rows += [(f"jst_{y}", t.jst_median[y]) for y in (1870, 1913, 1932, 1938, 1945, 1950, 2008, 2009, 2020)]
    rows += [(f"world_{y}", t.world[y]) for y in (1970, 2008, 2009, 2024)]
    rows += [("mobile_1990", m[1990]), ("mobile_2024", m[2024]), ("mobile_pass50_year", int(m[m > 50].index.min())),
             ("internet_2005", i[2005]), ("internet_2024", i[2024]),
             ("computers_2025_index", cp[2025]), ("computers_times_cheaper", round(100 / cp[2025], 1)),
             ("call_1927_dollars", call.dollars), ("cpi_1927", cpi[1927]), ("cpi_2025", round(cpi[2025], 1)),
             ("call_1927_in_2025_dollars", round(call.dollars * cpi[2025] / cpi[1927])),
             ("singapore_trade_2024", round(sgp, 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


def brenland_trade():
    a = load("accounts").set_index("year")
    t = load("trade").set_index("year")
    d = pd.DataFrame({"gdp": a.gdp, "exports": a.X, "imports": a.M,
                      "to_kestria": t.exports_to_kestria, "from_kestria": t.imports_from_kestria}).loc[[2000, 2025]]
    d["share"] = (100 * (d.exports + d.imports) / d.gdp).round(1)
    return d.rename_axis("year").reset_index()


if __name__ == "__main__":
    write_table(trade_share(), __file__, "trade_share")
    write_table(mobile_early(), __file__, "mobile_early")
    write_table(connections(), __file__, "connections")
    write_table(computer_prices(), __file__, "computer_prices")
    write_table(facts(), __file__, "facts")
    write_table(brenland_trade(), __file__, "brenland_trade")
