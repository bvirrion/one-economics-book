"""Output and capital per worker across countries; labour shares; growth accounting; Brenland's growth accounts.

Grade 12, chapter 4 (growth and the production function).
Penn World Table 11.0:
  - 2019, output-side real GDP at current PPPs (cgdpo) and capital stock at current PPPs (cn), per person engaged (emp),
    countries with at least one million people (pop >= 1); thousands of 2021 dollars per worker; slope of log y on log k;
  - labsh (share of labour compensation in GDP at current national prices), USA GBR FRA JPN KOR, 1950-2023;
  - growth accounting 1960-2019 for USA, JPN, KOR, GBR, FRA: output per worker rgdpna/emp, capital per worker rnna/emp,
    alpha = 1 - mean labsh over the period; average annual log growth (per cent); capital's contribution alpha * g_k and
    the residual (TFP) g_y - alpha * g_k.
Brenland (code/shared/country accounts.csv, invented): real investment I / deflator * 100; capital by perpetual inventory,
K(2000) = 3 x real GDP, K(t+1) = (1 - 0.05) K(t) + I(t); alpha = 0.35; output and capital per employed person 2000-2025.
Writes:
  out/cross.csv       iso3, k, y          (2021 dollars per worker, 2019)
  out/cross_key.csv   n, slope, usa_y, usa_k, ind_y, ind_k
  out/labsh.csv       year, USA, GBR, FRA, JPN, KOR
  out/accounts.csv    x, iso3, gy, alpha, cap, tfp, tfp_share
  out/bren.csv        year, real_gdp, employed, I_real, K, y, k
  out/bren_key.csv    gy, gk, cap, tfp, tfp_share, tfp_share_k25, K0, K2025
"""
import numpy as np
import pandas as pd

import country
from econdata import pwt
from figout import write_table

ISOS = ["USA", "JPN", "KOR", "GBR", "FRA"]
ALPHA_B, DELTA_B = 0.35, 0.05


def cross():
    p = pwt(since=2019, until=2019, cols=["cgdpo", "cn", "emp", "pop"]).dropna(subset=["cgdpo", "cn", "emp", "pop"])
    p = p[(p["pop"] >= 1) & (p.emp > 0)]
    t = pd.DataFrame({"iso3": p.iso3.values, "k": (p.cn / p.emp).round(1).values, "y": (p.cgdpo / p.emp).round(1).values})
    slope = float(np.polyfit(np.log(t.k), np.log(t.y), 1)[0])
    g = t.set_index("iso3")
    key = pd.DataFrame([{"n": len(t), "slope": round(slope, 3), "usa_y": g.loc["USA", "y"], "usa_k": g.loc["USA", "k"],
                         "ind_y": g.loc["IND", "y"], "ind_k": g.loc["IND", "k"]}])
    return t, key


def labour_shares():
    p = pwt(isos=["USA", "GBR", "FRA", "JPN", "KOR"], since=1950, until=2023, cols=["labsh"])
    t = p.pivot(index="year", columns="iso3", values="labsh")[["USA", "GBR", "FRA", "JPN", "KOR"]].round(3)
    t.columns.name = None
    # PWT fills the years before a country's first observed share with that first value (a flat run: the United Kingdom
    # 1950-1970, Japan 1950-1970, Korea 1953-1970). The chart starts each line at the last year of that run.
    for c in t.columns:
        v = t[c].dropna()
        run = (v == v.iloc[0]).cumprod().astype(bool)
        if run.sum() > 1:
            t.loc[run[run].index[:-1], c] = np.nan
    return t.reset_index().astype(object).where(t.reset_index().notna(), "nan")


def accounts():
    p = pwt(isos=ISOS, since=1960, until=2019, cols=["rgdpna", "rnna", "emp", "labsh"]).set_index(["iso3", "year"])
    rows = []
    for x, iso in enumerate(ISOS):
        d = p.loc[iso]
        y, k = d.rgdpna / d.emp, d.rnna / d.emp
        gy = 100 * np.log(y.loc[2019] / y.loc[1960]) / 59
        gk = 100 * np.log(k.loc[2019] / k.loc[1960]) / 59
        alpha = 1 - d.labsh.loc[1960:2019].mean()
        cap = alpha * gk
        rows.append({"x": x, "iso3": iso, "gy": round(gy, 2), "alpha": round(alpha, 3), "cap": round(cap, 2),
                     "tfp": round(gy - cap, 2), "tfp_share": round((gy - cap) / gy, 3)})
    return pd.DataFrame(rows)


def bren_capital(k0_ratio):
    a = country.load("accounts").set_index("year")
    i_real = a.I / a.deflator * 100
    K = {2000: k0_ratio * a.real_gdp.loc[2000]}
    for t in range(2000, 2025):
        K[t + 1] = (1 - DELTA_B) * K[t] + i_real.loc[t]
    return a, i_real, pd.Series(K)


def brenland():
    a, i_real, K = bren_capital(3.0)
    y, k = a.real_gdp / a.employed, K / a.employed
    t = pd.DataFrame({"year": a.index, "real_gdp": a.real_gdp.values, "employed": a.employed.values,
                      "I_real": i_real.round(0).values, "K": K.round(0).values,
                      "y": y.round(2).values, "k": k.round(2).values})

    def shares(kk):
        gy = 100 * np.log(y.loc[2025] / y.loc[2000]) / 25
        gk = 100 * np.log(kk.loc[2025] / kk.loc[2000]) / 25
        return gy, gk, ALPHA_B * gk, gy - ALPHA_B * gk

    gy, gk, cap, tfp = shares(k)
    _, _, K25 = bren_capital(2.5)
    _, _, _, tfp25 = shares(K25 / a.employed)
    key = pd.DataFrame([{"gy": round(gy, 2), "gk": round(gk, 2), "cap": round(cap, 2), "tfp": round(tfp, 2),
                         "tfp_share": round(tfp / gy, 3), "tfp_share_k25": round(tfp25 / gy, 3),
                         "K0": round(K.loc[2000]), "K2025": round(K.loc[2025])}])
    return t, key


if __name__ == "__main__":
    t, key = cross()
    write_table(t, __file__, "cross")
    write_table(key, __file__, "cross_key")
    write_table(labour_shares(), __file__, "labsh")
    write_table(accounts(), __file__, "accounts")
    b, bkey = brenland()
    write_table(b, __file__, "bren")
    write_table(bkey, __file__, "bren_key")
