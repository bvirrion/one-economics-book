"""Charts of b1 ch. 21.

sources: growth accounting, eight economies, from 1960 or the first year with an observed
labour share, to 2019 (PWT 11.0). PWT fills the years before a country's first
labour-share observation with that value; those years are left out (start: Japan and
Korea 1970, India 1975, Germany and Singapore 1980, Brazil and China 1992). Singapore's
share is carried forward from 2015 in the table and is used as it stands. For each year,
dln Y = a dln K + (1 - a)(dln L + dln H) + dln A, with a = 1 - labsh averaged over the
two adjacent years (Tornqvist), L = emp (persons engaged), H = hc; the residual is TFP.
Averages of the yearly terms, per cent a year. hours: the same for the United States
and Germany with L = emp x avh.
china: China 1952-2019: output per worker, capital per worker and TFP (rtfpna),
indices 1978 = 100.
devacc: development accounting in 2019 (cgdpo, cn, emp, hc): y = Y/emp, k = K/emp,
y_KH = k^(1/3) h^(2/3); success = Var(ln y_KH) / Var(ln y).
"""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

ISOS = ["CHN", "KOR", "JPN", "USA", "DEU", "IND", "BRA", "SGP"]
NAMES = {"CHN": "China", "KOR": "Korea", "JPN": "Japan", "USA": "United States", "DEU": "Germany",
         "IND": "India", "BRA": "Brazil", "SGP": "Singapore"}


def account(g, hours=False):
    g = g.sort_values("year").reset_index(drop=True)
    lab = g.emp * g.avh if hours else g.emp
    dy = np.log(g.rgdpna).diff()
    dk = np.log(g.rnna).diff()
    dl = np.log(lab).diff()
    dh = np.log(g.hc).diff()
    a = 1 - (g.labsh + g.labsh.shift()) / 2
    cap = a * dk
    labc = (1 - a) * dl
    hum = (1 - a) * dh
    tfp = dy - cap - labc - hum
    m = lambda s: round(100 * s.iloc[1:].mean(), 2)  # noqa: E731
    return {"output": m(dy), "capital": m(cap), "labour": m(labc), "human": m(hum), "tfp": m(tfp),
            "alpha": round(a.iloc[1:].mean(), 3)}


p = pwt(ISOS, 1950, 2019, ["rgdpna", "rnna", "emp", "avh", "hc", "labsh", "rtfpna"])


def first_share_year(iso):
    """Last year of the opening run of identical labour shares: the first observation."""
    g = p[p.iso3 == iso].dropna(subset=["labsh"]).sort_values("year")
    v = g.labsh.to_numpy()
    k = 0
    while k + 1 < len(v) and v[k + 1] == v[0]:
        k += 1
    return int(g.year.iloc[k])


START = {iso: max(1960, first_share_year(iso)) for iso in ISOS}
rows = []
for iso in ISOS:
    g = p[(p.iso3 == iso) & (p.year >= START[iso])]
    r = account(g)
    r.update({"iso3": iso, "country": NAMES[iso], "start": START[iso]})
    rows.append(r)
src = pd.DataFrame(rows)[["iso3", "country", "start", "output", "capital", "labour", "human", "tfp", "alpha"]]
src["tfp_share"] = (100 * src.tfp / src.output).round(1)
write_table(src, __file__, "sources")

hrs = []
for iso in ["USA", "DEU"]:
    g = p[(p.iso3 == iso) & (p.year >= START[iso])]
    a, b = account(g), account(g, hours=True)
    hrs.append({"iso3": iso, "labour_persons": a["labour"], "tfp_persons": a["tfp"],
                "labour_hours": b["labour"], "tfp_hours": b["tfp"]})
write_table(pd.DataFrame(hrs), __file__, "hours")

c = p[p.iso3 == "CHN"].sort_values("year").copy()
c["y"] = c.rgdpna / c.emp
c["k"] = c.rnna / c.emp
base = c[c.year == 1978].iloc[0]
ch = pd.DataFrame({"year": c.year, "y": (100 * c.y / base.y).round(1), "k": (100 * c.k / base.k).round(1),
                   "tfp": (100 * c.rtfpna / base.rtfpna).round(1)})
ch = ch.dropna(subset=["y"])
write_table(ch[["year", "y", "k"]], __file__, "china")
write_table(ch.dropna(subset=["tfp"])[["year", "tfp"]], __file__, "china_tfp")
pre = c[(c.year >= 1956) & (c.year <= 1978)]
post = c[(c.year >= 1978) & (c.year <= 2019)]
gr = lambda s, y: round(100 * np.log(s.iloc[-1] / s.iloc[0]) / (y.iloc[-1] - y.iloc[0]), 2)  # noqa: E731
write_table(pd.DataFrame([{"period": "1956-1978", "y": gr(pre.y, pre.year), "k": gr(pre.k, pre.year),
                           "tfp": gr(pre.rtfpna, pre.year)},
                          {"period": "1978-2019", "y": gr(post.y, post.year), "k": gr(post.k, post.year),
                           "tfp": gr(post.rtfpna, post.year)}]), __file__, "china_growth")

d = pwt(None, 2019, 2019, ["cgdpo", "cn", "emp", "hc"]).dropna()
d = d[(d.emp > 0) & (d.cn > 0)]
d["y"] = d.cgdpo / d.emp
d["k"] = d.cn / d.emp
d["ykh"] = d.k ** (1 / 3) * d.hc ** (2 / 3)
d["pred"] = d.ykh * np.exp(np.log(d.y).mean() - np.log(d.ykh).mean())
d["country"] = d.country.str.replace(",", "")
out = d[["iso3", "country", "y", "pred"]].round(0)
write_table(out, __file__, "devacc")
us = d[d.iso3 == "USA"].iloc[0]
st = {"n": len(d), "success": round(np.log(d.ykh).var() / np.log(d.y).var(), 3),
      "corr": round(np.corrcoef(np.log(d.y), np.log(d.ykh))[0, 1], 3)}
pts = d[d.iso3.isin(["USA", "IND", "CHN", "NER", "BRA", "DEU"])].copy()
pts["y_rel"] = (pts.y / us.y).round(3)
pts["ykh_rel"] = (pts.ykh / us.ykh).round(3)
pts["a_rel"] = (pts.y_rel / pts.ykh_rel).round(3)
write_table(pts[["iso3", "country", "y_rel", "ykh_rel", "a_rel"]], __file__, "devacc_points")
lab = d[d.iso3.isin(["USA", "IND", "CHN", "NER"])][["iso3", "country", "y", "pred"]].round(0)
write_table(lab, __file__, "devacc_labels")
write_table(pd.DataFrame([st]), __file__, "devacc_stats")
