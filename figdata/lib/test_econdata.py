"""Sanity checks of the loaders against facts that must hold in any vintage."""
import pytest

import econdata as ed


def test_maddison_uk_and_world():
    uk = ed.maddison("GBR", since=1820, until=1820)
    assert 2500 < float(uk.gdppc.iloc[0]) < 4500
    w = ed.maddison_world(since=2022, until=2022)
    assert 14000 < float(w.gdppc.iloc[0]) < 22000


def test_pwt_columns():
    d = ed.pwt("USA", since=2019, until=2019, cols=["rgdpo", "pop", "hc"])
    assert len(d) == 1 and d["pop"].iloc[0] > 300


def test_wdi_life_expectancy_world():
    d = ed.wdi("SP.DYN.LE00.IN", "WLD", since=2019, until=2019)
    assert 70 < float(d.value.iloc[0]) < 75


def test_wdi_rejects_unapproved():
    with pytest.raises(KeyError):
        ed.wdi("MS.MIL.XPND.GD.ZS")   # SIPRI-licensed: excluded


def test_wdi_countries_only_drops_aggregates():
    d = ed.wdi("NY.GDP.PCAP.KD", since=2020, until=2020, countries_only=True)
    assert "WLD" not in set(d.iso3) and "USA" in set(d.iso3)


def test_gapminder_before_1950_only():
    d = ed.gapminder("lex", "SWE", since=1800)
    assert d.year.max() <= 1949 and 30 < d.value.iloc[0] < 45
    with pytest.raises(ValueError):
        ed.gapminder("lex", until=2000)


def test_jst():
    d = ed.jst("USA", since=1929, until=1933, cols=["cpi", "unemp"])
    assert len(d) == 5 and d.cpi.iloc[-1] < d.cpi.iloc[0]   # the deflation of 1929-33


def test_pip_shares_sum_to_one():
    d = ed.pip_percentiles("BRA", years=2019)
    one = d[d.reporting_level == "national"]
    assert abs(one.welfare_share.sum() - 1) < 0.01


def test_bls_cpi_rises():
    d = ed.bls_cpi()
    a = d[d.period == "M13"].set_index("year").value
    assert a.loc[2023] > a.loc[2000] > a.loc[1970]


def test_eurostat_hicp():
    d = ed.eurostat("prc_hicp_manr")
    assert {"geo", "time", "value"} <= set(d.columns)


def test_ceds_co2_world_rises():
    d = ed.ceds("co2", isos=None)
    tot = d.groupby("year").value.sum()
    assert tot.loc[2019] > 10 * tot.loc[1900] > 0


def test_eia_world_per_capita():
    d = ed.eia_energy("Energy consumption per capita", isos="WLD", since=2019, until=2019)
    assert len(d) >= 1


def test_faostat_cereal_yield():
    d = ed.faostat_crops()
    w = d[d.Area == "World"].set_index("Year").Value
    assert w.loc[2020] > 2 * w.loc[1961]


def test_gravity_baci_only():
    d = ed.gravity(since=2019, until=2019, columns=["year", "iso3_o", "iso3_d", "dist",
                                                     "tradeflow_baci"])
    assert len(d) > 10000 and (d.tradeflow_baci > 0).all()


def test_nsw():
    d = ed.nsw("nsw_dw")
    assert len(d) == 445 and d.treat.sum() == 185


def test_maddison_regions_world():
    w = ed.maddison_regions("World")
    assert w.year.min() == 1820 and 1000 < w.gdppc.iloc[0] < 1300
    assert w.set_index("year").gdppc.loc[2022] > 15000
    assert set(ed.maddison_regions().region) == set(ed.REGIONS) | {"World"}


def test_bls_items_numeric():
    d = ed.bls_cpi("CUUR0000SETG01")
    a = d[d.period == "M13"].set_index("year").value
    assert a.dtype.kind == "f" and a.loc[2000] > a.loc[1990]
    assert len(ed.bls_cpi_items("airline")) >= 1


def test_eia_crude():
    d = ed.eia_energy("Crude oil including lease condensate production",
                      units="thousand barrels per day", isos="USA", since=2020, until=2020)
    assert 8000 < d.value.iloc[0] < 14000


def test_statsmodels_allowlist():
    m = ed.sm_dataset("macrodata")
    assert {"realgdp", "realcons", "infl"} <= set(m.columns)
    with pytest.raises(KeyError):
        ed.sm_dataset("star98")


def test_second_approval_loaders():
    import econdata as e
    ff = e.fed_series("h15", "RIFSPFF_N.M")
    assert ff["date"].min().year == 1954 and ff["value"].between(0, 25).all()
    ta = e.fed_series("h41", "RESPPMA_N.WW")
    assert ta["value"].max() > 8e6          # millions of dollars: peak near 9 trillion in 2022
    bread = e.bls_ap("Bread, white, pan", annual=True)
    assert bread["value"].between(0.3, 5).all()
    jo = e.jolts("JO")
    assert jo["year"].min() == 2000 and jo["value"].between(1, 10).all()
    ecb = e.ecb_total_assets()
    assert ecb["week"].iloc[0].startswith("1998") and ecb["eur_million"].max() > 8e6
    assert {"mean-item-share-average-standard-error", "aggregate-group-share"} == {t for t, _ in e.CEX_TABLES}
    eu = e.eurostat("jvs_q_nace2")
    assert len(eu) > 1000
