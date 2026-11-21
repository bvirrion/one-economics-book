"""Chart 2: average annual hours worked per person employed (Penn World Table, avh),
1950-2023, six economies. Some early stretches of avh grow at a constant rate year
after year: they are interpolated between benchmark years, or back-cast before the
first one, not observed. `interpolated` finds them (three or more years of the same
log growth) and the chart and the text leave them out: Germany 1950-59, Japan 1950-52,
Korea 1953-62 and 1971-79. Writes out/hours.csv, out/hours_points.csv,
out/hours_masked.csv and out/hours_growth.csv (ratio of 2023 to the first observed
year of hours and of output per hour, rgdpo / (emp avh))."""
import numpy as np
import pandas as pd
from econdata import pwt
from figout import write_table

ISO = ["USA", "DEU", "FRA", "GBR", "JPN", "KOR"]
TOL = 1e-4


def interpolated(s, tol=TOL, run=3):
    """Years of series s (indexed by year) that lie inside a run of at least `run`
    years of equal log growth; a run that starts at the series' first year is
    back-cast from its end, so its first year is dropped too."""
    s = s.dropna()
    g = np.log(s).diff()
    years, out, i = list(s.index), set(), 1
    while i < len(years):
        j = i
        while j + 1 < len(years) and abs(g.iloc[j + 1] - g.iloc[i]) < tol:
            j += 1
        if j - i + 1 >= run:
            a, b = years[i - 1], years[j]
            out.update(range(a if i == 1 else a + 1, b))
        i = j + 1
    return sorted(out)


def table():
    p = pwt(cols=["avh"])
    w = p[p.iso3.isin(ISO)].pivot(index="year", columns="iso3", values="avh")
    w = w.loc[1950:2023, ISO].copy()
    for iso in ISO:
        w.loc[interpolated(w[iso]), iso] = np.nan
    return w.reset_index()


def masked():
    p = pwt(cols=["avh"])
    rows = []
    for iso in ISO:
        s = p[p.iso3 == iso].set_index("year").avh.loc[1950:2023]
        m = interpolated(s)
        if m:
            rows.append((iso, len(m), m[0], m[-1]))
    return pd.DataFrame(rows, columns=["iso3", "years", "first", "last"])


def growth():
    t = table().set_index("year")
    p = pwt(cols=["avh", "rgdpo", "emp"]).dropna(subset=["avh", "rgdpo", "emp"])
    p["yh"] = p.rgdpo / (p.emp * p.avh)
    rows = []
    for iso in ISO:
        s = p[p.iso3 == iso].set_index("year")
        y0 = int(t[iso].dropna().index.min())
        rows.append((iso, y0, s.avh[y0], s.avh[2023] / s.avh[y0], s.yh[2023] / s.yh[y0]))
    return pd.DataFrame(rows, columns=["iso3", "first", "hours_first", "hours_ratio",
                                       "yh_ratio"])


if __name__ == "__main__":
    write_table(growth(), __file__, "hours_growth")
    write_table(masked(), __file__, "hours_masked")
    t = table()
    # "nan", not an empty cell, so that pgfplots breaks the line (unbounded coords=jump)
    gaps = t.round(2).astype(object).where(t.notna(), "nan")
    write_table(gaps, __file__, "hours")
    write_table(t[t.year.isin([1950, 1960, 1963, 1969, 2000, 2023])].reset_index(drop=True),
                __file__, "hours_points")
