"""g8-02 Measuring an Economy: GDP.

largest.csv      pos, iso3, label, total, per_person: the ten largest economies by GDP at purchasing-power parity, 2024:
                 total in trillions and per person in thousands of constant 2021 international dollars (WDI
                 NY.GDP.MKTP.PP.KD and NY.GDP.PCAP.PP.KD); pos 10 = the largest, at the top of the chart
brenland_gdp.csv item, value, share: Brenland's GDP by spending, 2025, millions of current dalens (C, I, G, X - M)
facts.csv        name, value
"""
import pandas as pd

from country import load
from econdata import wdi
from figout import write_table

NAMES = {"CHN": "China", "USA": "United States", "IND": "India", "RUS": "Russia", "JPN": "Japan",
         "DEU": "Germany", "BRA": "Brazil", "IDN": "Indonesia", "FRA": "France", "GBR": "United Kingdom"}


def largest():
    t = wdi("NY.GDP.MKTP.PP.KD", since=2024, until=2024, countries_only=True)
    t = t.sort_values("value", ascending=False).head(10)
    pp = wdi("NY.GDP.PCAP.PP.KD", since=2024, until=2024, countries_only=True).set_index("iso3").value
    out = pd.DataFrame({"iso3": t.iso3.values, "total": (t.value / 1e12).round(1).values,
                        "per_person": (pp[t.iso3].values / 1000).round(1)})
    out["label"] = out.iso3.map(NAMES)
    out["pos"] = range(10, 0, -1)
    return out[["pos", "iso3", "label", "total", "per_person"]]


def brenland_gdp():
    a = load("accounts").set_index("year").loc[2025]
    items = [("Consumption (C)", a.C), ("Investment (I)", a.I), ("Government (G)", a.G),
             ("Net exports (X - M)", a.X - a.M)]
    d = pd.DataFrame(items, columns=["item", "value"])
    d["share"] = (100 * d.value / a.gdp).round(1)
    return d


def brenland_spending():
    """Signed spending items, billions of dalens (thousands of millions), 2025, for the horizontal bar chart."""
    a = load("accounts").set_index("year").loc[2025]
    items = [("Consumption (C)", a.C), ("Investment (I)", a.I), ("Government (G)", a.G), ("Exports (X)", a.X),
             ("Imports (M)", -a.M), ("GDP", a.gdp)]
    d = pd.DataFrame(items, columns=["item", "value"])
    d["value"] = (d.value / 1000).round(1)
    d["pos"] = range(len(d), 0, -1)
    return d


def facts():
    a = load("accounts").set_index("year").loc[2025]
    rows = [(k, a[k]) for k in ["pop", "gdp", "C", "I", "G", "X", "M"]]
    rows.append(("gdp_per_person", round(a.gdp * 1e6 / (a["pop"] * 1e3))))
    b = load("accounts").set_index("year").loc[2024]
    rows += [("gdp_2024", b.gdp), ("pop_2024", b["pop"]), ("gdp_per_person_2024", round(b.gdp * 1e6 / (b["pop"] * 1e3))),
             ("deflator_2024", b.deflator), ("deflator_2025", a.deflator)]
    w = wdi("NY.GDP.MKTP.PP.KD", since=2024, until=2024).set_index("iso3").value
    rows.append(("world_total", round(w["WLD"] / 1e12, 1)))
    rows.append(("top10_share", round(100 * largest().total.sum() / round(w["WLD"] / 1e12, 1), 1)))
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(largest(), __file__, "largest")
    write_table(brenland_gdp(), __file__, "brenland_gdp")
    write_table(brenland_spending(), __file__, "brenland_spending")
    write_table(facts(), __file__, "facts")
