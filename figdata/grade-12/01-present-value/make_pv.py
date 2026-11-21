"""Long-term government bond yields, the price of a perpetuity, bond total returns; Brenland's bridge.

Grade 12, chapter 1 (present value).
Jorda-Schularick-Taylor Macrohistory Database, USA and GBR, 1980-2020: `ltrate` (long-term government bond yield, per
cent a year); the price of a perpetuity paying 1 a year computed from it as 100 / ltrate (a computation, not a market
price); `bond_tr` (nominal total return on government bonds in the year) cumulated into an index, end of 1979 = 100, and
the same index deflated by `cpi` (1979 = 100).
Brenland's bridge (invented): it costs 100 (millions of dalens) now and yields a net 7 a year (tolls 8, maintenance 1) at
the end of each of 30 years. NPV(r) = -100 + 7 (1 - (1 + r)^-30) / r; the break-even rate is found by bisection.
Writes:
  out/yields.csv       year, usa_lt, gbr_lt, usa_perp, gbr_perp
  out/bond_index.csv   year, usa_nom, gbr_nom, usa_real, gbr_real
  out/bridge_npv.csv   r, npv            (r in per cent, 0 to 8 by 0.25)
  out/bridge_key.csv   npv2, npv4, npv6, af4, irr, bis5, bis55, bis575
"""
import numpy as np
import pandas as pd

from econdata import jst
from figout import write_table

COST, NET, YEARS = 100.0, 7.0, 30


def npv(r):
    if r == 0:
        return -COST + NET * YEARS
    return -COST + NET * (1 - (1 + r) ** -YEARS) / r


def bisect(lo=0.04, hi=0.06, tol=1e-10):
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if npv(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def compute():
    j = jst(isos=["USA", "GBR"])
    y = {}
    idx = {}
    for iso in ["USA", "GBR"]:
        x = j[(j.iso3 == iso) & (j.year >= 1979) & (j.year <= 2020)].set_index("year")
        y[iso] = x.ltrate.loc[1980:]
        tr = x.bond_tr.loc[1980:]
        nom = 100 * (1 + tr).cumprod()
        real = nom / (x.cpi.loc[1980:] / x.cpi.loc[1979])
        idx[iso] = (nom, real)
    yields = pd.DataFrame({
        "year": y["USA"].index,
        "usa_lt": y["USA"].values.round(2), "gbr_lt": y["GBR"].values.round(2),
        "usa_perp": (100 / y["USA"]).values.round(1), "gbr_perp": (100 / y["GBR"]).values.round(1),
    })
    bonds = pd.DataFrame({
        "year": idx["USA"][0].index,
        "usa_nom": idx["USA"][0].values.round(0), "gbr_nom": idx["GBR"][0].values.round(0),
        "usa_real": idx["USA"][1].values.round(0), "gbr_real": idx["GBR"][1].values.round(0),
    })
    rs = np.arange(0, 8.0001, 0.25)
    curve = pd.DataFrame({"r": rs, "npv": [round(npv(r / 100), 2) for r in rs]})
    key = pd.DataFrame([{
        "npv2": round(npv(0.02), 1), "npv4": round(npv(0.04), 1), "npv6": round(npv(0.06), 1),
        "af4": round((1 - 1.04 ** -YEARS) / 0.04, 3), "irr": round(100 * bisect(), 2),
        "bis5": round(npv(0.05), 1), "bis55": round(npv(0.055), 1), "bis575": round(npv(0.0575), 1),
    }])
    return yields, bonds, curve, key


if __name__ == "__main__":
    yields, bonds, curve, key = compute()
    write_table(yields, __file__, "yields")
    write_table(bonds, __file__, "bond_index")
    write_table(curve, __file__, "bridge_npv")
    write_table(key, __file__, "bridge_key")
