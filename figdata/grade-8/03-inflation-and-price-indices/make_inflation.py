"""g8-03 Inflation and Price Indices.

inflation_century.csv year, usa, gbr, fra, jpn: consumer-price inflation, percent, 1920-2020 (JST, cpi)
germany.csv           year, level: Germany's consumer price level, 1914 = 1, 1914-1923 (JST, cpi)
basket.csv            good, qty, p2015, p2024, p2025, c2015, c2024, c2025: Brenland's 2015 basket priced (invented)
facts.csv             name, value
"""
import pandas as pd

from country import load
from econdata import bls_cpi, jst
from figout import write_table

C4 = {"USA": "usa", "GBR": "gbr", "FRA": "fra", "JPN": "jpn"}


def _cpi():
    d = jst(cols=["cpi"])
    return d.pivot(index="year", columns="iso3", values="cpi")


def inflation_century():
    p = _cpi()[list(C4)]
    i = (100 * p.pct_change()).round(1).loc[1920:2020].rename(columns=C4)
    return i.rename_axis("year").reset_index()


def germany():
    g = _cpi()["DEU"].loc[1914:1923]
    return pd.DataFrame({"year": g.index, "level": (g / g[1914]).values})


def basket():
    b = load("basket")
    p = b.pivot(index="good", columns="year", values="price")
    q = b[b.year == 2015].set_index("good").qty_2015
    out = pd.DataFrame({"qty": q})
    for y in (2015, 2024, 2025):
        out[f"p{y}"] = p[y]
        out[f"c{y}"] = (q * p[y]).round(2)
    order = ["bread", "rent", "transport", "clothing", "energy"]
    return out.loc[order].rename_axis("good").reset_index()


def facts():
    i = inflation_century().set_index("year")
    g = germany().set_index("year").level
    b = bls_cpi()
    b = b[b.period == "M13"].set_index("year").value
    a = load("accounts").set_index("year")
    bk = basket()
    rows = [("jpn_1945", i.jpn[1945]), ("jpn_1947", i.jpn[1947]), ("fra_1948", i.fra[1948]),
            ("gbr_1975", i.gbr[1975]), ("usa_1980", i.usa[1980]), ("usa_1921", i.usa[1921]),
            ("usa_1932", i.usa[1932]), ("jpn_2009", i.jpn[2009]),
            ("deflation_years_usa", int((i.usa < 0).sum())), ("deflation_years_jpn", int((i.jpn < 0).sum())),
            ("deu_1919", round(g[1919], 1)), ("deu_1922", round(g[1922], 0)), ("deu_1923", float(f"{g[1923]:.3g}")),
            ("us_cpi_2020", b[2020]), ("us_cpi_2021", b[2021]), ("us_cpi_2022", b[2022]), ("us_cpi_2025", b[2025]),
            ("us_inf_2021", round(100 * (b[2021] / b[2020] - 1), 1)), ("us_inf_2022", round(100 * (b[2022] / b[2021] - 1), 1)),
            ("us_inf_2025", round(100 * (b[2025] / b[2024] - 1), 1)),
            ("basket_2015", bk.c2015.sum()), ("basket_2024", round(bk.c2024.sum(), 2)), ("basket_2025", round(bk.c2025.sum(), 2)),
            ("cpi_2024", a.cpi[2024]), ("cpi_2025", a.cpi[2025]), ("cpi_2005", a.cpi[2005]),
            ("gdp_2005", a.gdp[2005]), ("gdp_2025", a.gdp[2025]), ("defl_2005", a.deflator[2005]), ("defl_2025", a.deflator[2025])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(inflation_century(), __file__, "inflation_century")
    write_table(germany(), __file__, "germany")
    write_table(basket(), __file__, "basket")
    write_table(facts(), __file__, "facts")
