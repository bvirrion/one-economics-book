import numpy as np
from econdata import jst, wdi, wdi_countries


def test_ex08_two_years(run_exercise):
    out, _ = run_exercise("ex08_wagner")
    lines = out.splitlines()
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    for line, year in zip(lines, (2000, 2019)):
        s = wdi("GC.XPN.TOTL.GD.ZS", since=year, until=year).set_index("iso3").value
        y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).set_index("iso3").value
        keep = [i for i in s.index if i in real and i in y.index
                and np.isfinite(s[i]) and np.isfinite(y[i])]
        slope, icpt = np.polyfit(np.log(y[keep]), s[keep], 1)
        r2 = np.corrcoef(np.log(y[keep]), s[keep])[0, 1] ** 2
        assert line.startswith(f"{year}: {len(keep)} countries")
        assert abs(float(line.split("slope ")[1].split()[0]) - slope) < 0.006
        assert abs(float(line.split("R-squared ")[1]) - r2) < 0.006


def _demean(x, groups):
    return x - x.groupby(groups).transform("mean")


def test_ex12_within_by_hand(run_exercise):
    out, _ = run_exercise("ex12_wagner_within")
    lines = out.splitlines()
    j = jst(cols=["expenditure", "gdp", "rgdpmad"])
    j = j[j.year.between(1870, 2020)].copy()
    j["s"], j["ly"] = 100 * j.expenditure / j.gdp, np.log(j.rgdpmad)
    d = j.dropna(subset=["s", "ly"])
    s1, x1 = _demean(d.s, d.iso3), _demean(d.ly, d.iso3)
    b1 = (s1 * x1).sum() / (x1 ** 2).sum()
    # two-way effects on an unbalanced panel: alternate the two demeanings
    s2, x2 = d.s.copy(), d.ly.copy()
    for _ in range(200):
        s2, x2 = _demean(_demean(s2, d.iso3), d.year), _demean(_demean(x2, d.iso3), d.year)
    b2 = (s2 * x2).sum() / (x2 ** 2).sum()
    assert lines[0] == f"observations: {len(d)}, economies: {d.iso3.nunique()}"
    assert abs(float(lines[1].split("slope ")[1].split()[0]) - b1) < 0.006
    assert abs(float(lines[2].split("slope ")[1].split()[0]) - b2) < 0.006
