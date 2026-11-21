"""Life satisfaction against income across European countries; hours worked against income; life expectancy against income;
five invented countries for the weekend problem.

Grade 12, chapter 15 (income and wellbeing).
Eurostat ilc_pw01 (mean overall life satisfaction, scale 0-10, all persons aged 16 or more, all levels of education), 2018,
the year with most countries (38 national codes; EL is Greece, UK the United Kingdom, XK Kosovo), matched to WDI
NY.GDP.PCAP.PP.KD (GDP per person at constant purchasing power, 2018); fit s = a + b ln y; the gain per doubling is b ln 2.
Penn World Table avh (average annual hours worked by persons engaged): across countries against rgdpe/pop in 2019 (key
values only); over time, 1950-2019, for Germany, France, the United Kingdom, Japan, South Korea and the United States, with
rgdpna/pop growth over the same years.
WDI SP.DYN.LE00.IN (life expectancy at birth) against NY.GDP.PCAP.PP.KD, 2019 (the Central African Republic left out: its
series is erratic): correlation with ln income; a composite of the two
for thirteen countries (life expectancy rescaled between 20 and 85 years, ln income between ln 100 and ln 75,000, capped at 1,
equal weights), ranked against income alone.
CEDS CO2 emissions by country (kt, 2019) over WDI SP.POP.TOTL: tonnes per person, against NY.GDP.PCAP.PP.KD, countries of
a million people or more; WDI NY.ADJ.DCO2.GN.ZS
(adjusted savings: carbon dioxide damage, % of GNI), 2019, for the same thirteen countries.
Two invented countries with the same mean income of 20,000 (one equal, one spread 5, 10, 15, 25, 45 thousand): average
satisfaction under the fitted log relation of the opening chart.
Five invented countries A-E (seeded, SEED 20261121): incomes 4,000 to 64,000 dollars, doubling each step; satisfaction
5.0 + 0.6 per doubling, hours, life expectancy, each with a small seeded noise, rounded.
Writes:
  out/lifesat.csv      geo, iso3, gdppc, lifesat
  out/hours.csv        iso3, gdppc, hours (2019 cross-section)
  out/hours_ts.csv     year, DEU, FRA, GBR, JPN, KOR, USA
  out/fit.csv          gdppc, lifesat (the fitted line at 10,000 and 140,000 dollars)
  out/five.csv         country, income, hours, lifeexp, lifesat
  out/well_key.csv     values quoted
  out/lifeexp.csv      iso3, gdppc, le (2019, every country with both)
  out/composite.csv    iso3, name, gdppc, le, i_le, i_y, comp, r_y, r_c, dmg (CO2 damage, % of GNI)
  out/co2.csv          iso3, gdppc, t (tonnes of CO2 per person, 2019)
  out/dist.csv         case, mean, geo_mean, sat_gap (points below the equal country)
  out/nature_key.csv   n_co2, corr_co2, slope_co2
"""
import numpy as np
import pandas as pd

from econdata import ceds, eurostat, pwt, wdi
from figout import write_table

SEED = 20261121
ISO = {"AL": "ALB", "AT": "AUT", "BE": "BEL", "BG": "BGR", "CH": "CHE", "CY": "CYP", "CZ": "CZE", "DE": "DEU", "DK": "DNK",
       "EE": "EST", "EL": "GRC", "ES": "ESP", "FI": "FIN", "FR": "FRA", "HR": "HRV", "HU": "HUN", "IE": "IRL", "IS": "ISL",
       "IT": "ITA", "LT": "LTU", "LU": "LUX", "LV": "LVA", "ME": "MNE", "MK": "MKD", "MT": "MLT", "NL": "NLD", "NO": "NOR",
       "PL": "POL", "PT": "PRT", "RO": "ROU", "RS": "SRB", "SE": "SWE", "SI": "SVN", "SK": "SVK", "TR": "TUR", "UK": "GBR",
       "XK": "XKX"}


def lifesat():
    d = eurostat("ilc_pw01")
    x = d[(d.isced11 == "TOTAL") & (d.sex == "T") & (d.age == "Y_GE16") & (d.time == 2018) & d.geo.isin(list(ISO))]
    x = x[["geo", "value"]].rename(columns={"value": "lifesat"})
    x["iso3"] = x.geo.map(ISO)
    y = wdi("NY.GDP.PCAP.PP.KD", isos=list(ISO.values()), since=2018, until=2018)[["iso3", "value"]]
    m = x.merge(y, on="iso3").dropna().rename(columns={"value": "gdppc"})
    m["gdppc"] = m.gdppc.round(0)
    return m[["geo", "iso3", "gdppc", "lifesat"]].sort_values("gdppc").reset_index(drop=True)


def hours():
    p = pwt(since=2019, until=2019, cols=["avh", "rgdpe", "pop"]).dropna()
    return pd.DataFrame({"iso3": p.iso3, "gdppc": (p["rgdpe"] / p["pop"]).round(0), "hours": p.avh.round(0)}).reset_index(drop=True)


SIXH = ["DEU", "FRA", "GBR", "JPN", "KOR", "USA"]


def hours_ts():
    p = pwt(since=1950, until=2019, cols=["avh", "rgdpna", "pop"])
    p = p[p.iso3.isin(SIXH)]
    h = p.pivot(index="year", columns="iso3", values="avh")[SIXH].round(0).reset_index()
    y = p.assign(ypc=p["rgdpna"] / p["pop"]).pivot(index="year", columns="iso3", values="ypc")
    k = {f"h1950_{c}": h.set_index("year").loc[1950, c] for c in ("DEU", "FRA", "USA")}
    k.update({f"h2019_{c}": h.set_index("year").loc[2019, c] for c in SIXH})
    k.update({"h1960_KOR": h.set_index("year").loc[1960, "KOR"], "ymult_DEU": round(float(y.loc[2019, "DEU"] / y.loc[1950, "DEU"]), 1),
              "ymult_USA": round(float(y.loc[2019, "USA"] / y.loc[1950, "USA"]), 1)})
    return h, k


LE_DROP = ["CAF"]   # WDI's series for the Central African Republic jumps between 19 and 57 years from one year to the next


def lifeexp():
    le = wdi("SP.DYN.LE00.IN", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    le = le[~le.iso3.isin(LE_DROP)]
    y = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    m = le.merge(y, on="iso3", suffixes=("_le", "_y")).dropna()
    return len(m), float(np.corrcoef(np.log(m.value_y), m.value_le)[0, 1])


COMP = {"USA": "United States", "DEU": "Germany", "SAU": "Saudi Arabia", "ESP": "Spain", "JPN": "Japan", "RUS": "Russia",
        "CHL": "Chile", "CRI": "Costa Rica", "CHN": "China", "LKA": "Sri Lanka", "ZAF": "South Africa", "NGA": "Nigeria",
        "IND": "India"}


def lifeexp_table():
    le = wdi("SP.DYN.LE00.IN", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    le = le[~le.iso3.isin(LE_DROP)]
    y = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    m = le.merge(y, on="iso3", suffixes=("_le", "_y")).dropna()
    return pd.DataFrame({"iso3": m.iso3, "gdppc": m.value_y.round(0), "le": m.value_le.round(1)}).sort_values("iso3").reset_index(drop=True)


def composite(lt):
    m = lt[lt.iso3.isin(COMP)].copy()
    m.insert(1, "name", m.iso3.map(COMP))
    m["i_le"] = ((m["le"] - 20) / 65).round(3)
    m["i_y"] = ((np.log(m.gdppc) - np.log(100)) / (np.log(75000) - np.log(100))).clip(upper=1).round(3)
    m["comp"] = ((m.i_le + m.i_y) / 2).round(3)
    m["r_y"] = m.gdppc.rank(ascending=False).astype(int)
    m["r_c"] = m.comp.rank(ascending=False, method="min").astype(int)
    d = wdi("NY.ADJ.DCO2.GN.ZS", isos=list(COMP), since=2019, until=2019)[["iso3", "value"]].rename(columns={"value": "dmg"})
    m = m.merge(d, on="iso3", how="left")
    m["dmg"] = m.dmg.round(1)
    return m.sort_values("r_y").reset_index(drop=True)


def co2():
    c = ceds("co2", since=2019, until=2019)[["iso3", "value"]]
    pop = wdi("SP.POP.TOTL", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    y = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019, countries_only=True)[["iso3", "value"]]
    z = c.merge(pop, on="iso3", suffixes=("_kt", "_pop")).merge(y.rename(columns={"value": "gdppc"}), on="iso3").dropna()
    z["t"] = z.value_kt * 1000 / z.value_pop
    z = z[(z.t > 0) & (z.value_pop >= 1e6)]   # small territories: CEDS books some of them with their parent country
    out = pd.DataFrame({"iso3": z.iso3, "gdppc": z.gdppc.round(0), "t": z.t.round(2)}).sort_values("iso3").reset_index(drop=True)
    lx, ly = np.log(out.gdppc), np.log(out.t)
    k = pd.DataFrame([{"n_co2": len(out), "corr_co2": round(float(np.corrcoef(lx, ly)[0, 1]), 2),
                       "slope_co2": round(float(np.polyfit(lx, ly, 1)[0]), 2)}])
    return out, k


def dist(b):
    spread = np.array([5000.0, 10000, 15000, 25000, 45000])
    gm = float(np.exp(np.mean(np.log(spread))))
    return pd.DataFrame({"case": ["equal", "spread"], "mean": [20000.0, float(spread.mean())], "geo_mean": [20000.0, round(gm, 0)],
                         "sat_gap": [0.0, round(float(b * np.log(20000 / gm)), 2)]})


def five():
    rng = np.random.default_rng(SEED)
    inc = np.array([4000, 8000, 16000, 32000, 64000])
    k = np.arange(5)
    sat = (5.0 + 0.6 * k + rng.normal(0, 0.12, 5)).round(1)
    hrs = (2300 - 160 * k + rng.normal(0, 40, 5)).round(-1)
    le = (64 + 4.5 * k + rng.normal(0, 1.2, 5)).round(0)
    return pd.DataFrame({"country": list("ABCDE"), "income": inc, "hours": hrs.astype(int), "lifeexp": le.astype(int),
                         "lifesat": sat})


def key(ls, hr, f, kh):
    b = np.polyfit(np.log(ls.gdppc), ls.lifesat, 1)[0]
    h = np.polyfit(np.log(hr.gdppc), hr.hours, 1)[0]
    x = np.log2(f.income / 1000)
    bf = float(((x - x.mean()) * f.lifesat).sum() / ((x - x.mean()) ** 2).sum())
    n_le, c_le = lifeexp()
    g = ls.set_index("geo")
    return pd.DataFrame([{"n_ls": len(ls), "b_ln": round(float(b), 3), "per_doubling": round(float(b * np.log(2)), 2),
                          "corr_ls": round(float(np.corrcoef(np.log(ls.gdppc), ls.lifesat)[0, 1]), 2),
                          "lo_geo": ls.geo.iloc[0], "lo_y": ls.gdppc.iloc[0], "lo_s": ls.lifesat.iloc[0],
                          "hi_geo": ls.geo.iloc[-1], "hi_y": ls.gdppc.iloc[-1], "hi_s": ls.lifesat.iloc[-1],
                          "fi_s": g.loc["FI", "lifesat"], "fi_y": g.loc["FI", "gdppc"], "ro_s": g.loc["RO", "lifesat"],
                          "ro_y": g.loc["RO", "gdppc"], "bg_s": g.loc["BG", "lifesat"], "bg_y": g.loc["BG", "gdppc"],
                          "tr_s": g.loc["TR", "lifesat"], "tr_y": g.loc["TR", "gdppc"],
                          "n_hr": len(hr), "hours_per_doubling": round(float(h * np.log(2)), 0),
                          "corr_hr": round(float(np.corrcoef(np.log(hr.gdppc), hr.hours)[0, 1]), 2),
                          "n_le": n_le, "corr_le": round(c_le, 2), "five_slope": round(bf, 3), **kh}])


if __name__ == "__main__":
    ls = lifesat()
    write_table(ls, __file__, "lifesat")
    b, a = np.polyfit(np.log(ls.gdppc), ls.lifesat, 1)
    xs = np.array([10000.0, 140000.0])
    write_table(pd.DataFrame({"gdppc": xs, "lifesat": (a + b * np.log(xs)).round(3)}), __file__, "fit")
    hr = hours()
    write_table(hr, __file__, "hours")
    f = five()
    write_table(f, __file__, "five")
    h, kh = hours_ts()
    write_table(h, __file__, "hours_ts")
    write_table(key(ls, hr, f, kh), __file__, "well_key")
    lt = lifeexp_table()
    write_table(lt, __file__, "lifeexp")
    write_table(composite(lt), __file__, "composite")
    c, ck = co2()
    write_table(c, __file__, "co2")
    write_table(ck, __file__, "nature_key")
    write_table(dist(b), __file__, "dist")
