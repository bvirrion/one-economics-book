"""Chart 3: consumer prices in six euro-area economies, 1999--2015 (HICP, annual
average index, rebased to 1999 = 100; Eurostat prc_hicp_aind). Writes
out/euro_prices.csv and out/euro_prices_points.csv (2008 and 2015)."""
from econdata import eurostat
from figout import write_table

GEOS = ["DE", "FR", "EL", "ES", "IE", "PT"]


def table():
    e = eurostat("prc_hicp_aind")
    e = e[(e.unit == "INX_A_AVG") & (e.coicop == "CP00") & e.geo.isin(GEOS)]
    w = e.pivot(index="time", columns="geo", values="value").loc[1999:2015, GEOS]
    w = 100 * w / w.loc[1999]
    return w.reset_index().rename(columns={"time": "year"})


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "euro_prices")
    write_table(t[t.year.isin([2008, 2015])].reset_index(drop=True), __file__,
                "euro_prices_points")
