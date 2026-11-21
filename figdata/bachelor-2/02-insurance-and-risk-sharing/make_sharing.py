"""Do countries share risk? Household consumption against GDP, per country, 1991-2023.

World Bank WDI, two indicators: NE.CON.PRVT.PC.KD.ZG (growth of household final
consumption expenditure per person, constant prices) and NY.GDP.PCAP.KD.ZG (growth of
GDP per person, constant prices). Countries only (no aggregates), years 1991-2023 with
both series, kept if they have at least 25 such years.

Writes
  out/volatility.csv    iso3, sd_gdp, sd_cons, ratio  (standard deviations of the
                        annual growth rates, percentage points) -- opening chart;
  out/correlation.csv   iso3, corr_gdp, corr_cons  (correlation of the country's growth
                        with the World aggregate's growth of the same indicator);
  out/summary.csv       one row: n, share_ratio_above_1, median_ratio,
                        share_cons_corr_below_gdp, median_corr_gdp, median_corr_cons,
                        world_sd_cons (the World aggregate's consumption growth),
                        n_sd_gdp_below_world, and the median ratio among low-income
                        and among high-income countries (World Bank income groups).
Book 4, chapter 2: opening chart and chart 2.
"""

import pandas as pd
from econdata import wdi, wdi_countries
from figout import write_table

CONS, GDP = "NE.CON.PRVT.PC.KD.ZG", "NY.GDP.PCAP.KD.ZG"
SINCE, UNTIL, MIN_YEARS = 1991, 2023, 25


def panel():
    c = wdi(CONS, since=SINCE, until=UNTIL, countries_only=True)
    y = wdi(GDP, since=SINCE, until=UNTIL, countries_only=True)
    d = c.merge(y, on=["iso3", "country", "year"], suffixes=("_c", "_y")).dropna()
    world = (
        wdi(CONS, isos=["WLD"], since=SINCE, until=UNTIL)[["year", "value"]]
        .rename(columns={"value": "wc"})
        .merge(
            wdi(GDP, isos=["WLD"], since=SINCE, until=UNTIL)[["year", "value"]].rename(
                columns={"value": "wy"}
            ),
            on="year",
        )
    )
    d = d.merge(world, on="year")
    n = d.groupby("iso3").year.transform("size")
    return d[n >= MIN_YEARS].sort_values(["iso3", "year"])


def tables():
    d = panel()
    rows = []
    for iso, g in d.groupby("iso3"):
        rows.append(
            {
                "iso3": iso,
                "sd_gdp": g.value_y.std(),
                "sd_cons": g.value_c.std(),
                "corr_gdp": g.value_y.corr(g.wy),
                "corr_cons": g.value_c.corr(g.wc),
            }
        )
    s = pd.DataFrame(rows)
    s["ratio"] = s.sd_cons / s.sd_gdp
    wsd = d.drop_duplicates("year").wc.std()
    inc = wdi_countries().set_index("Country Code")["Income Group"]
    grp = s.iso3.map(inc)
    vol = s[["iso3", "sd_gdp", "sd_cons", "ratio"]].round(3)
    cor = s[["iso3", "corr_gdp", "corr_cons"]].round(3)
    summ = pd.DataFrame(
        [
            {
                "n": len(s),
                "share_ratio_above_1": round(100 * (s.ratio > 1).mean(), 1),
                "median_ratio": round(s.ratio.median(), 2),
                "share_cons_corr_below_gdp": round(
                    100 * (s.corr_cons < s.corr_gdp).mean(), 1
                ),
                "median_corr_gdp": round(s.corr_gdp.median(), 2),
                "median_corr_cons": round(s.corr_cons.median(), 2),
                "world_sd_cons": round(wsd, 2),
                "n_sd_gdp_below_world": int((s.sd_gdp < wsd).sum()),
                "median_ratio_low_income": round(
                    s.ratio[grp == "Low income"].median(), 2
                ),
                "median_ratio_high_income": round(
                    s.ratio[grp == "High income"].median(), 2
                ),
            }
        ]
    )
    return vol, cor, summ


if __name__ == "__main__":
    vol, cor, summ = tables()
    write_table(vol, __file__, "volatility")
    write_table(cor, __file__, "correlation")
    write_table(summ, __file__, "summary")
