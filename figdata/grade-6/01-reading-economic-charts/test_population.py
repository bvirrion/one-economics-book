import pandas as pd
from make_population import BAR_YEARS, tables
from econdata import REGIONS


def test_world_population_points():
    pop, _ = tables()
    assert list(pop.year)[:3] == [1820, 1850, 1870] and pop.year.max() == 2022
    assert len(pop) == 21
    assert 1.0 < pop.set_index("year").pop_bn[1820] < 1.1
    assert 7.7 < pop.set_index("year").pop_bn[2022] < 7.9


def test_shares_sum_to_100_and_regions_complete():
    _, s = tables()
    assert list(s.year) == BAR_YEARS
    assert s.notna().all().all()
    total = s.drop(columns="year").sum(axis=1)
    assert ((total - 100).abs() <= 0.3).all()
    assert len(s.columns) == 1 + len(REGIONS)


def test_asia_share_falls_then_africa_rises():
    _, s = tables()
    s = s.set_index("year")
    assert s.east_asia[1820] > s.east_asia[2022]
    assert s.ssa[2022] > 2 * s.ssa[1950]


def test_written_tables_match():
    pop, s = tables()
    out = pd.read_csv(__file__.replace("test_population.py", "out/population_shares.csv"))
    assert (out.year == s.year).all()
