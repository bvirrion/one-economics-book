"""Search and unemployment, chapter 26.

Opening chart: the euro area's Beveridge curve, quarterly 2009-Q1 to 2025-Q4: the job
vacancy rate (Eurostat jvs_q_nace2, JVR, industry, construction and services B-S, all
sizes, seasonally adjusted) against the unemployment rate (une_rt_q, ages 15-74, per
cent of the labour force, seasonally adjusted), geo EA21 in both.
Writes
  out/beveridge.csv     time, t (year + (quarter - 1) / 4), u, v, period (1 before 2020)
  out/bev_points.csv    labelled quarters: time, u, v
  out/bev_summary.csv   one row per labelled quarter: time, u, v, theta (v / u)
"""

from econdata import eurostat
from figout import write_table

LABELS = ["2009-Q1", "2013-Q1", "2019-Q4", "2020-Q3", "2022-Q2", "2025-Q4"]


def beveridge():
    e = eurostat("jvs_q_nace2")
    v = e[
        (e.indic_em == "JVR")
        & (e.nace_r2 == "B-S")
        & (e.sizeclas == "TOTAL")
        & (e.geo == "EA21")
        & (e.s_adj == "SA")
    ][["time", "value"]].rename(columns={"value": "v"})
    u = eurostat("une_rt_q")
    u = u[
        (u.age == "Y15-74")
        & (u.unit == "PC_ACT")
        & (u.sex == "T")
        & (u.geo == "EA21")
        & (u.s_adj == "SA")
    ][["time", "value"]].rename(columns={"value": "u"})
    d = u.merge(v, on="time").dropna()
    d = d[(d.time >= "2009-Q1") & (d.time <= "2025-Q4")].sort_values("time")
    d["t"] = d.time.str[:4].astype(int) + (d.time.str[-1].astype(int) - 1) / 4
    d["period"] = (d.t < 2020).astype(int)
    return d[["time", "t", "u", "v", "period"]].reset_index(drop=True)


def bev_points():
    d = beveridge()
    return d[d.time.isin(LABELS)][["time", "u", "v"]]


def bev_summary():
    d = bev_points().copy()
    d["theta"] = (d.v / d.u).round(3)
    return d


if __name__ == "__main__":
    write_table(beveridge(), __file__, "beveridge")
    write_table(bev_points(), __file__, "bev_points")
    write_table(bev_summary(), __file__, "bev_summary")
