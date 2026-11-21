"""Asset returns 1950-2020, JST Macrohistory Database (Book 4, chapter 4).

Writes
  out/cumulative.csv  year, then <iso>_<asset> for USA, GBR, FRA, JPN and the three
                      assets: the value of 1 unit of real wealth invested at the end of
                      1949, all income reinvested (1949 = 1).
  out/riskreturn.csv  iso3, asset, mean, sd: mean and standard deviation of annual real
                      returns, per cent, 1950-2020, for every country with all three
                      series complete (15 countries).
  out/riskreturn_wide.csv  the same, one row per country: iso3, <asset>_mean,
                      <asset>_sd.
  out/autocorr.csv    pos, iso3, rho1: first-order autocorrelation of annual real
                      equity returns, 1950-2020.
  out/summary.csv     one row: n_countries; years; band (2/sqrt(years));
                      n_outside_band; median_eq_mean, median_bill_mean and
                      median_premium (per cent); eq_sd_mean_corr (across countries,
                      equity standard deviation with equity mean); for the USA:
                      usa_premium (equity minus bill, per cent), usa_eq_sd,
                      usa_dc_sd (real consumption growth per person), usa_corr,
                      usa_cov (per cent squared), usa_gamma (premium / cov),
                      usa_sharpe (premium / sd of equity),
                      usa_gamma_bound (sharpe / sd of consumption growth: the smallest
                      gamma, reached with a correlation of one), and the final values of
                      the cumulative index for USA equity and bills.
"""

import numpy as np
import pandas as pd
from figout import write_table
from jstreturns import ASSETS, real_returns

FOUR = ["USA", "GBR", "FRA", "JPN"]


def cumulative():
    d = real_returns()
    out = pd.DataFrame({"year": range(1949, 2021)})
    for iso in FOUR:
        s = d[d.iso3 == iso].set_index("year")
        for a in ASSETS:
            v = np.concatenate([[1.0], (1 + s[a]).cumprod().values])
            out[f"{iso}_{a}"] = np.round(v, 4)
    return out


def riskreturn():
    d = real_returns()
    rows = []
    for (iso, a), s in d.melt(["iso3", "year"], list(ASSETS), "asset").groupby(
        ["iso3", "asset"]
    ):
        rows.append(
            {
                "iso3": iso,
                "asset": a,
                "mean": round(100 * s.value.mean(), 2),
                "sd": round(100 * s.value.std(), 2),
            }
        )
    return pd.DataFrame(rows)


def autocorr():
    d = real_returns()
    r = d.groupby("iso3").equity.apply(lambda s: s.autocorr(1)).round(3)
    r = r.sort_values().reset_index()
    r.columns = ["iso3", "rho1"]
    r.insert(0, "pos", range(1, len(r) + 1))
    return r


def summary():
    d = real_returns()
    rr = riskreturn().pivot(index="iso3", columns="asset", values="mean")
    ac = autocorr()
    years = d.year.nunique()
    band = 2 / np.sqrt(years)
    u = d[d.iso3 == "USA"].dropna(subset=["dc"])
    prem = 100 * (u.equity - u.bill).mean()
    cov = 1e4 * np.cov(u.dc, u.equity)[0, 1]
    c = cumulative().iloc[-1]
    return pd.DataFrame(
        [
            {
                "n_countries": d.iso3.nunique(),
                "years": years,
                "band": round(band, 3),
                "n_outside_band": int((ac.rho1.abs() > band).sum()),
                "median_eq_mean": round(rr.equity.median(), 2),
                "median_bill_mean": round(rr.bill.median(), 2),
                "median_premium": round((rr.equity - rr.bill).median(), 2),
                "eq_sd_mean_corr": round(
                    riskreturn_wide()[["equity_sd", "equity_mean"]].corr().iloc[0, 1], 2
                ),
                "usa_premium": round(prem, 2),
                "usa_eq_sd": round(100 * u.equity.std(), 2),
                "usa_dc_sd": round(100 * u.dc.std(), 2),
                "usa_corr": round(np.corrcoef(u.dc, u.equity)[0, 1], 3),
                "usa_cov": round(cov, 2),
                "usa_gamma": round(prem / cov * 100, 1),
                "usa_sharpe": round(prem / (100 * u.equity.std()), 3),
                "usa_gamma_bound": round(prem / (100 * u.equity.std()) / u.dc.std(), 1),
                "usa_eq_final": round(c.USA_equity, 1),
                "usa_bill_final": round(c.USA_bill, 2),
            }
        ]
    )


def riskreturn_wide():
    w = riskreturn().pivot(index="iso3", columns="asset", values=["mean", "sd"])
    w.columns = [f"{a}_{m}" for m, a in w.columns]
    return w.reset_index()


if __name__ == "__main__":
    write_table(cumulative(), __file__, "cumulative")
    write_table(riskreturn(), __file__, "riskreturn")
    write_table(riskreturn_wide(), __file__, "riskreturn_wide")
    write_table(autocorr(), __file__, "autocorr")
    write_table(summary(), __file__, "summary")
