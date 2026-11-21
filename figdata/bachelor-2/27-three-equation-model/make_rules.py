"""Rules and rates, chapter 27.

Opening chart: the federal funds rate (H.15 RIFSPFF_N.M, quarterly average of monthly
values) against the rule of Taylor (1993), r = p + 0.5 y + 0.5 (p - 2) + 2, quarterly
1960-Q1 to 2008-Q4. p is CPI inflation over the previous four quarters and y the per
cent deviation of real GDP from trend, both from statsmodels macrodata; the trend is a
Hodrick-Prescott filter with smoothing 1600 over 1959-Q1 to 2009-Q3 (Taylor used a
linear trend over 1984-92).
Chart 2: US CPI-U inflation over twelve months (BLS, not seasonally adjusted) and the
federal funds rate, monthly, January 2019 to the last common month.
Writes
  out/rule.csv         t, ffr, rule, gap, infl
  out/rule_dec.csv     decade (1960 ... 2000), mean of ffr - rule, mean absolute gap
  out/rule_summary.csv one row: mean abs. deviation 1960-79 and 1987-2007, corr in each
  out/recent.csv       t, infl, ffr
  out/recent_summary.csv one row: CPI peak and month, ffr at the peak, first month the
                       ffr is above 0.5, ffr peak and its first month, last month, both
"""

import numpy as np
import pandas as pd
from econdata import bls_cpi, fed_series, sm_dataset
from figout import write_table
from statsmodels.tsa.filters.hp_filter import hpfilter


def _ffr_monthly():
    f = fed_series("h15", "RIFSPFF_N.M")
    f["year"], f["month"] = f.date.dt.year, f.date.dt.month
    return f


def rule():
    m = sm_dataset("macrodata").copy()
    m["t"] = m.year + (m.quarter - 1) / 4
    m["infl"] = 100 * (m.cpi / m.cpi.shift(4) - 1)
    cycle, _ = hpfilter(np.log(m.realgdp), lamb=1600)
    m["gap"] = 100 * cycle
    f = _ffr_monthly()
    f["q"] = (f.month - 1) // 3 + 1
    fq = f.groupby(["year", "q"]).value.mean().rename("ffr").reset_index()
    m = m.merge(fq, left_on=["year", "quarter"], right_on=["year", "q"])
    m["rule"] = m.infl + 0.5 * m.gap + 0.5 * (m.infl - 2) + 2
    m = m[(m.t >= 1960) & (m.t < 2009)]
    return m[["t", "ffr", "rule", "gap", "infl"]].round(3).reset_index(drop=True)


def rule_dec():
    d = rule()
    d["decade"] = (d.t // 10 * 10).astype(int)
    d["dev"] = d.ffr - d.rule
    g = d.groupby("decade").dev
    return pd.DataFrame(
        {"decade": g.mean().index, "mean": g.mean().round(2).values,
         "mad": g.apply(lambda x: x.abs().mean()).round(2).values}
    )  # fmt: skip


def rule_summary():
    d = rule()
    a = d[(d.t >= 1960) & (d.t < 1980)]
    b = d[(d.t >= 1987) & (d.t < 2008)]
    return pd.DataFrame(
        [{"mad6079": round((a.ffr - a.rule).abs().mean(), 2),
          "mad8707": round((b.ffr - b.rule).abs().mean(), 2),
          "corr6079": round(np.corrcoef(a.ffr, a.rule)[0, 1], 2),
          "corr8707": round(np.corrcoef(b.ffr, b.rule)[0, 1], 2)}]
    )  # fmt: skip


def recent():
    b = bls_cpi()
    b = b[b.period.str.match(r"M(0[1-9]|1[0-2])")].copy()
    b["month"] = b.period.str[1:].astype(int)
    b = b.sort_values(["year", "month"]).reset_index(drop=True)
    b["infl"] = 100 * (b.value / b.value.shift(12) - 1)
    d = b.merge(_ffr_monthly().rename(columns={"value": "ffr"}), on=["year", "month"])
    d["t"] = d.year + (d.month - 1) / 12
    d = d[d.year >= 2019].dropna(subset=["infl", "ffr"])
    return d[["t", "year", "month", "infl", "ffr"]].round(3).reset_index(drop=True)


def recent_summary():
    d = recent()

    def ym(row):
        return f"{int(row.year)}-{int(row.month):02d}"

    pk = d.loc[d.infl.idxmax()]
    up = d[(d.ffr > 0.5) & (d.year >= 2021)].iloc[0]
    fp = d.loc[d.ffr.idxmax()]
    last = d.iloc[-1]
    return pd.DataFrame(
        [{"cpi_peak": round(pk.infl, 1), "cpi_peak_ym": ym(pk),
          "ffr_at_peak": round(pk.ffr, 2),
          "first_above": ym(up),
          "ffr_peak": round(fp.ffr, 2), "ffr_peak_ym": ym(fp),
          "last_ym": ym(last),
          "last_infl": round(last.infl, 1), "last_ffr": round(last.ffr, 2)}]
    )  # fmt: skip


if __name__ == "__main__":
    write_table(rule(), __file__, "rule")
    write_table(rule_dec(), __file__, "rule_dec")
    write_table(rule_summary(), __file__, "rule_summary")
    write_table(recent(), __file__, "recent")
    write_table(recent_summary(), __file__, "recent_summary")
