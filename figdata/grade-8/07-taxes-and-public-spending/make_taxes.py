"""g8-07 Taxes and Public Spending.

public_spending.csv year, usa, gbr, fra, swe, jpn, deu: central government expenditure, percent of GDP, 1880-2020
                    (JST expenditure / gdp; central government only, as JST defines it)
debt_gdp.csv        year, usa, gbr, fra, swe, jpn, deu: public debt, percent of GDP, 1880-2020 (JST debtgdp x 100)
tax_bands.csv       income, rate: Brenland's marginal income-tax rate (percent) as a step function, 0-140000 dalens
budget.csv          year, gdp, revenue, spending, deficit, debt: Brenland 2014-2025, millions of dalens (invented)
facts.csv           name, value
"""
import pandas as pd

from country import TAX_BANDS, load
from econdata import jst
from figout import write_table

C6 = {"USA": "usa", "GBR": "gbr", "FRA": "fra", "SWE": "swe", "JPN": "jpn", "DEU": "deu"}


def _jst():
    return jst(cols=["expenditure", "gdp", "debtgdp"])


def _wide(col):
    return _jst().pivot(index="year", columns="iso3", values=col).loc[1880:2020, list(C6)]


def public_spending():
    e = (100 * _wide("expenditure") / _wide("gdp")).round(1)
    return e.rename(columns=C6).rename_axis("year").reset_index()


def debt_gdp():
    return (100 * _wide("debtgdp")).round(1).rename(columns=C6).rename_axis("year").reset_index()


def tax(g):
    t = 0.0
    for (lo, r), nxt in zip(TAX_BANDS, TAX_BANDS[1:] + [(float("inf"), 0)]):
        if g > lo:
            t += (min(g, nxt[0]) - lo) * r
    return t


def tax_bands():
    rows = []
    for (lo, r), nxt in zip(TAX_BANDS, TAX_BANDS[1:] + [(140_000, 0)]):
        rows += [(lo, 100 * r), (nxt[0], 100 * r)]
    return pd.DataFrame(rows, columns=["income", "rate"])


def budget():
    a = load("accounts").set_index("year").loc[2014:2025, ["gdp", "revenue", "spending", "deficit", "debt"]]
    return a.reset_index()


def facts():
    e = public_spending().set_index("year")
    d = debt_gdp().set_index("year")
    rows = []
    for c in ["usa", "gbr"]:
        rows += [(f"spend_{c}_1913", e[c][1913]), (f"spend_{c}_1950", e[c][1950]), (f"spend_{c}_2019", e[c][2019])]
    rows += [("spend_fra_1918", e.fra[1918]), ("spend_gbr_1944", e.gbr[1944]), ("spend_usa_1944", e.usa[1944])]
    for c in C6.values():
        rows += [(f"debt_{c}_max", d[c].max()), (f"debt_{c}_max_year", int(d[c].idxmax()))]
    rows += [("debt_usa_1946", d.usa[1946]), ("debt_gbr_1946", d.gbr[1946]), ("debt_gbr_1919", d.gbr[1919]),
             ("debt_usa_2020", d.usa[2020]), ("debt_jpn_2020", d.jpn[2020])]
    rows += [(f"tax_{g}", tax(g)) for g in (30_000, 45_000, 60_000)]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(public_spending(), __file__, "public_spending")
    write_table(debt_gdp(), __file__, "debt_gdp")
    write_table(tax_bands(), __file__, "tax_bands")
    write_table(budget(), __file__, "budget")
    write_table(facts(), __file__, "facts")
