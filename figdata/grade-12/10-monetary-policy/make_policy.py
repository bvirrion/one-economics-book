"""The federal funds rate, inflation, a Taylor-type rule and the Fed's balance sheet; Brenland's rule.

Grade 12, chapter 10 (monetary policy).
Federal Reserve H.15: effective federal funds rate, monthly (RIFSPFF_N.M), 1965-01 to the latest month.
BLS CPI-U all items (CUUR0000SA0), not seasonally adjusted: 12-month inflation, monthly; annual inflation from annual means.
WDI NY.GDP.MKTP.KD, USA: output gap from a Hodrick-Prescott trend on log GDP (lambda 100), as in chapter 8.
Taylor-type rule (as on the Federal Reserve's page on policy rules): i = 2 + pi + 0.5 (pi - 2) + 0.5 gap, annual,
1965-2024, with CPI inflation (Taylor 1993 used the GDP deflator; this version is ours).
Federal Reserve H.4.1: total assets, Wednesday level (RESPPMA_N.WW), trillions of dollars, at chosen dates.
Brenland (invented): policy_rate and cpi 2015-2025; potential from a log-linear trend of real_gdp 2001-2025; the problem's
rule i = 2 + pi + 0.5 (pi - 2) + 0.5 gap.
Writes:
  out/fedfunds.csv     t (decimal year), rate, infl
  out/taylor.csv       year, actual, rule
  out/policy_key.csv   rule fit 1987-2007, rule and actual in chosen years, balance-sheet values
  out/brenland.csv     year, rate, infl, gap, rule, diff
"""
import numpy as np
import pandas as pd
from statsmodels.tsa.filters.hp_filter import hpfilter

import country
from econdata import bls_cpi, fed_series, jst, wdi
from figout import write_table


def monthly():
    f = fed_series("h15", "RIFSPFF_N.M")
    f["year"], f["month"] = f.date.dt.year, f.date.dt.month
    c = bls_cpi()
    c = c[c.period.str.fullmatch(r"M(0[1-9]|1[0-2])")].copy()
    c["month"] = c.period.str[1:].astype(int)
    c = c.sort_values(["year", "month"]).reset_index(drop=True)
    c["infl"] = 100 * (c.value / c.value.shift(12) - 1)
    m = f.merge(c[["year", "month", "infl"]], on=["year", "month"], how="left")
    m = m[m.year >= 1965]
    return pd.DataFrame({"t": (m.year + (m.month - 0.5) / 12).round(3), "rate": m.value.round(2), "infl": m.infl.round(2)})


def annual():
    f = fed_series("h15", "RIFSPFF_N.M")
    ff = f.groupby(f.date.dt.year).value.mean()
    c = bls_cpi()
    c = c[c.period.str.fullmatch(r"M(0[1-9]|1[0-2])")]
    ca = c.groupby("year").value.mean()
    pi = 100 * (ca / ca.shift(1) - 1)
    g = wdi("NY.GDP.MKTP.KD", isos=["USA"], since=1960, until=2024).dropna().set_index("year").value
    cyc, _ = hpfilter(np.log(g.values), lamb=100)
    gap = pd.Series(100 * cyc, index=g.index)
    r = pd.DataFrame({"actual": ff, "pi": pi, "gap": gap}).loc[1965:2024].dropna()
    r["rule"] = 2 + r.pi + 0.5 * (r.pi - 2) + 0.5 * r.gap
    return r


def key(r):
    s = r.loc[1987:2007]
    h = fed_series("h41", "RESPPMA_N.WW").set_index("date").value / 1e6
    k = {"corr_8707": round(float(np.corrcoef(s.actual, s.rule)[0, 1]), 2),
         "mad_8707": round(float((s.actual - s.rule).abs().mean()), 1),
         "assets_2007": round(float(h.asof(pd.Timestamp("2007-08-01"))), 2),
         "assets_2014": round(float(h.asof(pd.Timestamp("2014-12-31"))), 2),
         "assets_peak": round(float(h.max()), 2), "assets_peak_date": h.idxmax().date().isoformat()}
    m = monthly()
    i, j = m.rate.idxmax(), m.infl.idxmax()
    k.update({"max_rate": m.rate[i], "max_rate_t": m.t[i], "max_infl": m.infl[j], "max_infl_t": m.t[j]})
    u = jst(isos=["USA"]).set_index("year").unemp
    k.update({"unemp1979": round(u[1979], 1), "unemp1982": round(u[1982], 1)})
    for y in (1980, 1981, 1983, 2009, 2021, 2022, 2023, 2024):
        k[f"rule{y}"] = round(r.loc[y, "rule"], 1)
        k[f"actual{y}"] = round(r.loc[y, "actual"], 2)
        k[f"pi{y}"] = round(r.loc[y, "pi"], 1)
    return pd.DataFrame([k])


def brenland():
    a = country.load("accounts").set_index("year")
    lg = np.log(a.real_gdp)
    b = np.polyfit(a.index, lg, 1)
    gap = 100 * (lg - np.polyval(b, a.index))
    infl = 100 * (a.cpi / a.cpi.shift(1) - 1)
    d = pd.DataFrame({"year": a.index, "rate": a.policy_rate, "infl": infl.round(1), "gap": gap.round(1)}).loc[2015:2025]
    d["rule"] = (2 + d.infl + 0.5 * (d.infl - 2) + 0.5 * d.gap).round(2)
    d["diff"] = (d.rule - d.rate).round(2)
    return d.reset_index(drop=True), round(100 * (np.exp(b[0]) - 1), 2)


if __name__ == "__main__":
    write_table(monthly(), __file__, "fedfunds")
    r = annual()
    write_table(pd.DataFrame({"year": r.index, "actual": r.actual.round(2).values, "rule": r.rule.round(2).values}), __file__, "taylor")
    write_table(key(r), __file__, "policy_key")
    b, g = brenland()
    write_table(b, __file__, "brenland")
