"""g9-04 International Trade.

korea_mix.csv  group, y1965, y2024: South Korea's merchandise exports by product group, percent of merchandise exports
               (WDI TX.VAL.FOOD/AGRI/FUEL/MMTL/MANF.ZS.UN); the five groups need not sum to 100 (unclassified goods)
tariffs.csv    year, USA, EUU, CHN, IND, BRA: applied tariff rate, weighted mean, all products, percent
               (WDI TM.TAX.MRCH.WM.AR.ZS); missing years written as nan (the chart breaks
               the line there); the United States 2019 value is a series break and is left out
cloth.csv      price, qd, qs: the chapter's invented cloth market of Brenland (demand 100 - 5p, supply 5p - 10)
brenland.csv   year, exports, imports, balance, to_kestria, from_kestria, with_kestria (millions of dalens; frozen
               invented country)
facts.csv      name, value (Korea shares, latest tariffs, remittances as percent of GDP, the worked tariff example)
"""
import pandas as pd

from country import load
from econdata import wdi
from figout import write_table

GROUPS = [("Food", "TX.VAL.FOOD.ZS.UN"), ("Farm raw materials", "TX.VAL.AGRI.ZS.UN"),
          ("Fuels", "TX.VAL.FUEL.ZS.UN"), ("Ores and metals", "TX.VAL.MMTL.ZS.UN"),
          ("Manufactures", "TX.VAL.MANF.ZS.UN")]
TARIFF_ISOS = ["USA", "EUU", "CHN", "IND", "BRA"]
WORLD_PRICE, TARIFF = 6, 2


def korea_mix():
    rows = []
    for name, code in GROUPS:
        d = wdi(code, isos=["KOR"], since=1965, until=2024).set_index("year")["value"]
        rows.append((name, round(float(d[1965]), 1), round(float(d[2024]), 1)))
    return pd.DataFrame(rows, columns=["group", "y1965", "y2024"])


def tariffs():
    t = wdi("TM.TAX.MRCH.WM.AR.ZS", isos=TARIFF_ISOS, since=1988, until=2022)
    t = t.pivot(index="year", columns="iso3", values="value").reindex(range(1988, 2023))
    # WDI gives the United States 13.78 % for 2019 between 1.59 (2018) and 1.52 (2020): a break in the series, not a
    # ninefold tariff rise; it is left out and the source line says so.
    t.loc[2019, "USA"] = float("nan")
    return t[TARIFF_ISOS].round(2).reset_index()


def tariffs_csv():
    """Missing years written as nan, so that pgfplots (unbounded coords=jump) breaks the line there."""
    return tariffs().astype(object).where(tariffs().notna(), "nan")


def qd(p):
    return 100 - 5 * p


def qs(p):
    return 5 * p - 10


def cloth():
    p = [x / 2 for x in range(4, 41)]
    return pd.DataFrame({"price": p, "qd": [qd(x) for x in p], "qs": [qs(x) for x in p]})


def brenland():
    a = load("accounts").set_index("year")
    t = load("trade").set_index("year")
    df = pd.DataFrame({"exports": a.X, "imports": a.M, "balance": a.X - a.M,
                       "to_kestria": t.exports_to_kestria, "from_kestria": t.imports_from_kestria})
    df["with_kestria"] = df.to_kestria - df.from_kestria
    return df.reset_index()


def tariff_example():
    p0, p1 = WORLD_PRICE, WORLD_PRICE + TARIFF
    out = {"pw": p0, "tariff": TARIFF, "pt": p1, "autarky_p": 11, "autarky_q": qd(11),
           "qd0": qd(p0), "qs0": qs(p0), "m0": qd(p0) - qs(p0),
           "qd1": qd(p1), "qs1": qs(p1), "m1": qd(p1) - qs(p1)}
    out["revenue"] = TARIFF * out["m1"]
    out["buyers_extra"] = TARIFF * out["qd1"]
    out["producers_extra"] = TARIFF * out["qs1"]
    return out


def facts():
    k = korea_mix().set_index("group")
    t = tariffs().set_index("year")
    rows = [("kor_manf_1965", k.y1965["Manufactures"]), ("kor_manf_2024", k.y2024["Manufactures"]),
            ("kor_food_1965", k.y1965["Food"]), ("kor_food_2024", k.y2024["Food"])]
    rows += [(f"tariff_{c}_2022", t.loc[2022, c]) for c in TARIFF_ISOS]
    rows += [(f"tariff_{c}_first", t[c].dropna().iloc[0]) for c in TARIFF_ISOS]
    rows += [(f"tariff_{c}_first_year", t[c].dropna().index[0]) for c in TARIFF_ISOS]
    r = wdi("BX.TRF.PWKR.DT.GD.ZS", isos=["WLD", "LMY", "TJK", "PHL", "MEX"], since=2024, until=2024)
    rows += [(f"remit_{i}_2024", round(float(v), 1)) for i, v in zip(r.iso3, r.value)]
    rows += [(f"ex_{k_}", v) for k_, v in tariff_example().items()]
    b = brenland().set_index("year")
    rows += [("bren_balance_2024", b.balance[2024]), ("bren_balance_2025", b.balance[2025]),
             ("bren_with_kestria_2025", b.with_kestria[2025])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(korea_mix(), __file__, "korea_mix")
    write_table(tariffs_csv(), __file__, "tariffs")
    write_table(cloth(), __file__, "cloth")
    write_table(brenland(), __file__, "brenland")
    write_table(facts(), __file__, "facts")
