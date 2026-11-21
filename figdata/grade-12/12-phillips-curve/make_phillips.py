"""US inflation against unemployment: 1960-1969, 1970-1983, 2015-2025; the 1979-1986 disinflation.

Grade 12, chapter 12 (the Phillips curve and its breakdown).
Inflation: BLS CPI-U all items (CUUR0000SA0), change in the annual average, per cent (the same measure as chapter 10).
Unemployment: Jorda-Schularick-Taylor Macrohistory Database (unemp) to 1986; World Development Indicators
SL.UEM.TOTL.NE.ZS (national estimate) for 2015-2025, since the JST file ends in 2020.
Disinflation table 1979-1986 with a natural rate of 6 % (given in the problem, not estimated); cumulative unemployment
above it from 1980 to 1986 (point-years); fall of inflation from 1980 to 1986; their ratio.
Writes:
  out/phil6069.csv, out/phil7083.csv, out/phil1525.csv   year, u, pi
  out/volcker.csv       year, u, pi, excess
  out/phillips_key.csv  values quoted
"""
import pandas as pd

from econdata import bls_cpi, jst, wdi
from figout import write_table

UN = 6.0


def inflation():
    # Annual average of the monthly CPI-U values present; for 2025 the BLS file has eleven months (no October).
    c = bls_cpi()
    c = c[c.period.str.fullmatch(r"M(0[1-9]|1[0-2])")]
    a = c.groupby("year").value.mean()
    return (100 * (a / a.shift(1) - 1)).round(1)


def tables():
    pi = inflation()
    uj = jst(isos=["USA"]).set_index("year").unemp.round(1)
    uw = wdi("SL.UEM.TOTL.NE.ZS", isos=["USA"], since=2015, until=2025).dropna().set_index("year").value.round(1)
    def t(u, a, b):
        return pd.DataFrame({"year": range(a, b + 1), "u": [u[y] for y in range(a, b + 1)], "pi": [pi[y] for y in range(a, b + 1)]})
    p1, p2, p3 = t(uj, 1960, 1969), t(uj, 1970, 1983), t(uw, 2015, 2025)
    v = t(uj, 1979, 1986)
    v["excess"] = (v.u - UN).clip(lower=0).round(1)
    return p1, p2, p3, v


def key(v, p3):
    V = v.set_index("year")
    excess = round(float(V.loc[1980:1986, "excess"].sum()), 1)
    fall = round(float(V.loc[1980, "pi"] - V.loc[1986, "pi"]), 1)
    P3 = p3.set_index("year")
    return pd.DataFrame([{"un": UN, "excess_8086": excess, "pi1980": V.loc[1980, "pi"], "pi1986": V.loc[1986, "pi"], "fall": fall,
                          "ratio": round(excess / fall, 2), "u2019": P3.loc[2019, "u"], "pi2019": P3.loc[2019, "pi"],
                          "u2022": P3.loc[2022, "u"], "pi2022": P3.loc[2022, "pi"], "u2025": P3.loc[2025, "u"],
                          "pi2025": P3.loc[2025, "pi"]}])


if __name__ == "__main__":
    p1, p2, p3, v = tables()
    write_table(p1, __file__, "phil6069")
    write_table(p2, __file__, "phil7083")
    write_table(p3, __file__, "phil1525")
    write_table(v, __file__, "volcker")
    write_table(key(v, p3), __file__, "phillips_key")
