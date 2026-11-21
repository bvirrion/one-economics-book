"""Average tariffs, 1988-2022; the weekend problem's tariff, quota and retaliation.

Grade 12, chapter 13 (trade beyond Ricardo, and trade policy).
World Development Indicators TM.TAX.MRCH.WM.AR.ZS: tariff rate, applied, weighted mean, all products, per cent; Brazil,
China, India, Mexico, South Korea and the European Union, 1988-2022 (years with data only; the lines join them). The United
States is left out: its 2019 value (13.8) is inconsistent with every other year of its series (1.5 to 4.0).
Kestria (invented): cloth demand Qd = 100 - P, supply Qs = P - 20, world price 40, a 20 % tariff; grain supply Qs = 2P - 20,
demand Qd = 80 - 2P, export price falling from 30 to 27 after Brenland's retaliation.
Writes:
  out/tariffs.csv       year, BRA, CHN, EUU, IND, KOR, MEX (nan where missing)
  out/tariff_key.csv    first and last values quoted, the US anomaly
  out/kestria_key.csv   the problem's numbers
"""
import numpy as np
import pandas as pd

from econdata import wdi
from figout import write_table

ISOS = ["BRA", "CHN", "EUU", "IND", "KOR", "MEX"]


def tariffs():
    d = wdi("TM.TAX.MRCH.WM.AR.ZS", isos=ISOS + ["USA"], since=1988, until=2022)
    p = d.pivot(index="year", columns="iso3", values="value").reindex(range(1988, 2023))
    k = {"chn1992": p.loc[1992, "CHN"], "chn2022": p.loc[2022, "CHN"], "ind1990": p.loc[1990, "IND"], "ind2022": p.loc[2022, "IND"],
         "bra1989": p.loc[1989, "BRA"], "bra2022": p.loc[2022, "BRA"], "euu2022": p.loc[2022, "EUU"], "kor2022": p.loc[2022, "KOR"],
         "mex2022": p.loc[2022, "MEX"], "usa2019": p.loc[2019, "USA"],
         "usa_other_min": p.USA.drop(2019).min(), "usa_other_max": p.USA.drop(2019).max()}
    t = p[ISOS].round(1).reset_index()
    return t, pd.DataFrame([{a: round(float(b), 1) for a, b in k.items()}])


def kestria():
    pw, tau = 40.0, 0.20
    pt = pw * (1 + tau)
    qd0, qs0, qd1, qs1 = 100 - pw, pw - 20, 100 - pt, pt - 20
    m0, m1 = qd0 - qs0, qd1 - qs1
    cs_loss = (pt - pw) * (qd0 + qd1) / 2
    ps_gain = (pt - pw) * (qs0 + qs1) / 2
    rev = (pt - pw) * m1
    dwl = cs_loss - ps_gain - rev
    g0, g1 = 30.0, 27.0
    s0, s1, d0, d1 = 2 * g0 - 20, 2 * g1 - 20, 80 - 2 * g0, 80 - 2 * g1
    gp_loss = (g0 - g1) * (s0 + s1) / 2
    gc_gain = (g0 - g1) * (d0 + d1) / 2
    grain = gp_loss - gc_gain
    return pd.DataFrame([{"pt": pt, "qd0": qd0, "qs0": qs0, "m0": m0, "qd1": qd1, "qs1": qs1, "m1": m1, "cs_loss": cs_loss,
                          "ps_gain": ps_gain, "rev": rev, "dwl": dwl, "dwl_prod": 0.5 * (pt - pw) * (qs1 - qs0),
                          "dwl_cons": 0.5 * (pt - pw) * (qd0 - qd1), "x0": s0 - d0, "x1": s1 - d1, "gp_loss": gp_loss,
                          "gc_gain": gc_gain, "grain_loss": grain, "net_loss": dwl + grain}])


if __name__ == "__main__":
    t, k = tariffs()
    write_table(t, __file__, "tariffs")
    write_table(k, __file__, "tariff_key")
    write_table(kestria(), __file__, "kestria_key")
