"""Current accounts of six economies; price levels and income; Brenland's real exchange rate against the kest.

Grade 12, chapter 14 (exchange rates and the balance of payments).
World Development Indicators: BN.CAB.XOKA.CD (current account balance, current dollars), USA, CHN, JPN, DEU, IND, GBR,
1980-2024, billions; PA.NUS.PRVT.PLI (price level ratio of the purchasing-power conversion factor to the market exchange
rate) and NY.GDP.PCAP.CD (GDP per person, current dollars), 2019, countries only; log-log slope and correlation.
Brenland (invented, code/shared/country): accounts (S - I = X - M; the package has no income flows, so net exports are the
current account) and trade.csv (rate, dalens per kest). Kestria's consumer price index is generated here, seeded
(SEED 20261120): yearly inflation drawn from a normal law with mean 2.5 % and standard deviation 0.8 %, 2015 = 100.
Real exchange rate q = e x P_K / P_B (dalens per kest, in Kestrian goods per Brenland good terms), 2015 = 100.
Penn World Table pl_c (price level of consumption, United States = 1), 1970-2019: for each country with 50 years of data,
an AR(1) fitted to the log price level, rho; half-life ln 0.5 / ln rho for 0 < rho < 1; the median across countries. The
price level also moves with income (the second chart), so this is an upper bound on the speed of a pure return to parity.
Eurostat une_rt_q (seasonally adjusted, 15-74, per cent of the labour force): Germany, Spain, Greece, 2009-Q1 and 2013-Q2.
Writes:
  out/ca.csv          year, USA, CHN, JPN, DEU, IND, GBR (billions of dollars; nan where missing)
  out/pli.csv         iso3, gdppc, pli
  out/pli_key.csv     n, slope, corr
  out/brenland.csv    year, S, I, CA, ca_pct, rate, cpi_b, cpi_k, q
  out/bop_key.csv     values quoted
"""
import numpy as np
import pandas as pd

import country
from econdata import eurostat, pwt, wdi
from figout import write_table

SEED = 20261120
SIX = ["USA", "CHN", "JPN", "DEU", "IND", "GBR"]


def current_accounts():
    d = wdi("BN.CAB.XOKA.CD", isos=SIX, since=1980, until=2024)
    p = (d.pivot(index="year", columns="iso3", values="value") / 1e9).reindex(range(1980, 2025))[SIX]
    return p.round(1).reset_index()


def price_levels():
    pl = wdi("PA.NUS.PRVT.PLI", since=2019, until=2019, countries_only=True).dropna()[["iso3", "value"]]
    y = wdi("NY.GDP.PCAP.CD", since=2019, until=2019, countries_only=True).dropna()[["iso3", "value"]]
    m = pl.merge(y, on="iso3", suffixes=("_pli", "_y"))
    t = pd.DataFrame({"iso3": m.iso3, "gdppc": m.value_y.round(0), "pli": m.value_pli.round(1)})
    lx, ly = np.log(t.gdppc), np.log(t.pli)
    k = pd.DataFrame([{"n": len(t), "slope": round(float(np.polyfit(lx, ly, 1)[0]), 3), "corr": round(float(np.corrcoef(lx, ly)[0, 1]), 3)}])
    return t, k


def brenland():
    a = country.load("accounts").set_index("year").loc[2015:2025]
    tr = country.load("trade").set_index("year").loc[2015:2025]
    rng = np.random.default_rng(SEED)
    infl = rng.normal(2.5, 0.8, len(a) - 1)
    cpi_k = 100 * np.concatenate([[1.0], np.cumprod(1 + infl / 100)])
    S = a.gdp - a.C - a.G
    d = pd.DataFrame({"year": a.index, "S": S.values, "I": a.I.values, "CA": (a.X - a.M).values,
                      "ca_pct": (100 * (a.X - a.M) / a.gdp).round(2).values, "rate": tr.rate.values,
                      "cpi_b": a.cpi.values, "cpi_k": cpi_k.round(1)})
    q = d.rate * d.cpi_k / d.cpi_b
    d["q"] = (100 * q / q.iloc[0]).round(1)
    return d


def half_life():
    p = pwt(since=1970, until=2019, cols=["pl_c"])
    hl = []
    for iso, g in p.groupby("iso3"):
        s = np.log(g.set_index("year").pl_c.dropna())
        if iso == "USA" or len(s) < 50:
            continue
        rho = np.polyfit(s.values[:-1], s.values[1:], 1)[0]
        if 0 < rho < 1:
            hl.append(np.log(0.5) / np.log(rho))
    h = pd.Series(hl)
    return {"hl_n": len(h), "hl_median": round(float(h.median()), 1), "hl_q25": round(float(h.quantile(0.25)), 1),
            "hl_q75": round(float(h.quantile(0.75)), 1)}


def unemployment():
    u = eurostat("une_rt_q")
    x = u[(u.s_adj == "SA") & (u.age == "Y15-74") & (u.unit == "PC_ACT") & (u.sex == "T") & u.geo.isin(["DE", "ES", "EL"])]
    p = x.pivot(index="time", columns="geo", values="value")
    return {f"u_{g}_{t[:4]}": p.loc[t, g] for g in ("DE", "ES", "EL") for t in ("2009-Q1", "2013-Q2")}


def key(ca, b):
    c = ca.set_index("year")
    B = b.set_index("year")
    return pd.DataFrame([{"usa2006": c.loc[2006, "USA"], "usa2024": c.loc[2024, "USA"], "chn2008": c.loc[2008, "CHN"],
                          "chn2024": c.loc[2024, "CHN"], "deu2015": c.loc[2015, "DEU"], "jpn2024": c.loc[2024, "JPN"],
                          "gbr2024": c.loc[2024, "GBR"], "rate2015": B.loc[2015, "rate"], "rate2025": B.loc[2025, "rate"],
                          "cpib2025": B.loc[2025, "cpi_b"], "cpik2025": B.loc[2025, "cpi_k"], "q2025": B.loc[2025, "q"],
                          "ca_mean_pct": round(float(B.ca_pct.mean()), 2), "ca_sum": int(B.CA.sum()),
                          "ca2025": B.loc[2025, "CA"], "ca2025_pct": B.loc[2025, "ca_pct"], **half_life(), **unemployment()}])


if __name__ == "__main__":
    ca = current_accounts()
    write_table(ca, __file__, "ca")
    t, k = price_levels()
    write_table(t, __file__, "pli")
    write_table(k, __file__, "pli_key")
    b = brenland()
    write_table(b, __file__, "brenland")
    write_table(key(ca, b), __file__, "bop_key")
