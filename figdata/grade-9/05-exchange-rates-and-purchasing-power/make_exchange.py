"""g9-05 Exchange Rates and Purchasing Power.

market_vs_ppp.csv       country, iso3, market, ppp: GDP per person in 2024 at market exchange rates (WDI NY.GDP.PCAP.CD,
                        current US dollars) and at purchasing-power parity (WDI NY.GDP.PCAP.PP.CD, current
                        international dollars), ten countries
price_level_income.csv  iso3, income, pli: price level of household consumption (WDI PA.NUS.PRVT.PLI, United States =
                        100) against GDP per person at PPP, 2024, every country with both values
price_level_named.csv   iso3, income, pli, label: the named dots of that chart
brenland_rate.csv       year, rate: dalens per kest (frozen invented country, trade.csv)
facts.csv               name, value
"""
import pandas as pd

from country import load
from econdata import wdi
from figout import write_table

TEN = [("Switzerland", "CHE"), ("United States", "USA"), ("Germany", "DEU"), ("Japan", "JPN"), ("Mexico", "MEX"),
       ("China", "CHN"), ("Brazil", "BRA"), ("Indonesia", "IDN"), ("India", "IND"), ("Ethiopia", "ETH")]
NAMED = {"CHE": "Switzerland", "USA": "United States", "IND": "India", "ETH": "Ethiopia", "DEU": "Germany",
         "CHN": "China"}
YEAR = 2024


def _pair():
    a = wdi("NY.GDP.PCAP.CD", since=YEAR, until=YEAR)[["iso3", "value"]].rename(columns={"value": "market"})
    b = wdi("NY.GDP.PCAP.PP.CD", since=YEAR, until=YEAR)[["iso3", "value"]].rename(columns={"value": "ppp"})
    return a.merge(b, on="iso3")


def market_vs_ppp():
    """Ten countries, richest first at market exchange rates."""
    d = _pair().set_index("iso3")
    rows = [(name, iso, round(float(d.market[iso])), round(float(d.ppp[iso]))) for name, iso in TEN]
    return pd.DataFrame(rows, columns=["country", "iso3", "market", "ppp"])


def price_level_income():
    p = wdi("PA.NUS.PRVT.PLI", since=YEAR, until=YEAR, countries_only=True)[["iso3", "value"]]
    i = wdi("NY.GDP.PCAP.PP.CD", since=YEAR, until=YEAR, countries_only=True)[["iso3", "value"]]
    d = p.rename(columns={"value": "pli"}).merge(i.rename(columns={"value": "income"}), on="iso3").dropna()
    d["income"] = d.income.round()
    d["pli"] = d.pli.round(1)
    return d[["iso3", "income", "pli"]].sort_values("income").reset_index(drop=True)


def price_level_named():
    d = price_level_income()
    d = d[d.iso3.isin(NAMED)].copy()
    d["label"] = d.iso3.map(NAMED)
    return d


def brenland_rate():
    return load("trade")[["year", "rate"]]


def facts():
    m = market_vs_ppp().set_index("iso3")
    rows = []
    for iso in ["CHE", "USA", "IND", "ETH", "CHN"]:
        rows += [(f"market_{iso}", m.market[iso]), (f"ppp_{iso}", m.ppp[iso]),
                 (f"ratio_{iso}", round(m.ppp[iso] / m.market[iso], 2))]
    rows += [("gap_USA_IND_market", round(m.market["USA"] / m.market["IND"], 1)),
             ("gap_USA_IND_ppp", round(m.ppp["USA"] / m.ppp["IND"], 1))]
    d = price_level_income()
    rows += [("n_countries", len(d)),
             ("pli_median_below_5000", round(d[d.income < 5000].pli.median(), 1)),
             ("n_below_5000", int((d.income < 5000).sum())),
             ("pli_median_above_50000", round(d[d.income > 50000].pli.median(), 1)),
             ("n_above_50000", int((d.income > 50000).sum()))]
    n = d.set_index("iso3")
    rows += [(f"pli_{iso}", n.pli[iso]) for iso in NAMED]
    r = brenland_rate().set_index("year").rate
    rows += [("rate_2024", r[2024]), ("rate_2025", r[2025]),
             ("rate_change_pct", round((r[2025] - r[2024]) / r[2024] * 100, 1))]
    a = load("accounts").set_index("year")
    rows += [("bren_gdp_pp_2025", round(a.gdp[2025] / a["pop"][2025] * 1000))]  # gdp millions, pop thousands
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(market_vs_ppp(), __file__, "market_vs_ppp")
    write_table(price_level_income(), __file__, "price_level_income")
    write_table(price_level_named(), __file__, "price_level_named")
    write_table(brenland_rate(), __file__, "brenland_rate")
    write_table(facts(), __file__, "facts")
