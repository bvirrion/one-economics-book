"""Loaders for the series' approved datasets (data/derived/, written by tools/derive_data.py).

Every chart script under figdata/<year>/NN-<slug>/ reads its data through these
functions, never from data/raw/ directly. Each returns a pandas DataFrame in
long form. The SOURCE dict gives the line to print under a chart
(\\begin{omchart}{caption}{<source line>}); the full citation lives in
frontmatter/data-credits.tex.

    from econdata import maddison, wdi, SOURCE
    d = maddison(["GBR", "USA"], since=1820)

Licence filters are applied in tools/derive_data.py (WDI: CC BY 4.0 indicators
only; Gravity: BACI flows only) and here (Gapminder: years before 1950 only).
A dataset not loaded here is not approved: ask the main session.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DER = ROOT / "data" / "derived"

SOURCE = {
    "maddison": "Maddison Project Database 2023",
    "pwt": "Penn World Table 11.0",
    "wdi": "World Bank, World Development Indicators",
    "pip": "World Bank, Poverty and Inequality Platform",
    "jst": "Jord\\`a--Schularick--Taylor Macrohistory Database",
    "gapminder": "Gapminder",
    "eurostat": "Eurostat",
    "bls": "U.S. Bureau of Labor Statistics",
    "ceds": "Community Emissions Data System (CEDS)",
    "eia": "U.S. Energy Information Administration",
    "faostat": "FAOSTAT",
    "gravity": "CEPII Gravity database",
    "nsw": "National Supported Work samples (Dehejia and Wahba)",
    "statsmodels": "statsmodels bundled data (public domain)",
    "bls_ap": "U.S. Bureau of Labor Statistics, Average Price Data",
    "jolts": "U.S. Bureau of Labor Statistics, Job Openings and Labor Turnover Survey",
    "cex": "U.S. Bureau of Labor Statistics, Consumer Expenditure Surveys",
    "fed": "Board of Governors of the Federal Reserve System",
    "ecb": "European Central Bank",
}

GAPMINDER_LAST_YEAR = 1949


def _need(p: Path) -> Path:
    if not p.exists():
        raise FileNotFoundError(
            f"{p} is missing: data/derived/ is built by tools/derive_data.py (main session)")
    return p


def _isos(d: pd.DataFrame, isos, col="iso3") -> pd.DataFrame:
    if isos is None:
        return d
    if isinstance(isos, str):
        isos = [isos]
    return d[d[col].isin(list(isos))]


def _years(d: pd.DataFrame, since, until, col="year") -> pd.DataFrame:
    if since is not None:
        d = d[d[col] >= since]
    if until is not None:
        d = d[d[col] <= until]
    return d


@lru_cache(maxsize=None)
def _maddison() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "maddison_countries.csv"))


def maddison(isos=None, since=None, until=None) -> pd.DataFrame:
    """Columns iso3, country, region, year, gdppc (2011 international dollars), pop (thousands)."""
    return _years(_isos(_maddison(), isos), since, until).copy()


REGIONS = ["East Asia", "Eastern Europe", "Latin America", "Middle East and North Africa",
           "South and South East Asia", "Sub Saharan Africa", "Western Europe", "Western Offshoots"]


@lru_cache(maxsize=None)
def _maddison_regions() -> pd.DataFrame:
    raw = pd.read_csv(_need(DER / "maddison_regional_raw.csv"), header=None, skiprows=3)
    rows = []
    for _, r in raw.iterrows():
        year = int(float(r[0]))
        for j, name in enumerate(REGIONS + ["World"]):
            rows.append(dict(year=year, region=name, gdppc=r[1 + j], pop=r[11 + j]))
    d = pd.DataFrame(rows)
    d["gdppc"] = pd.to_numeric(d.gdppc, errors="coerce")
    d["pop"] = pd.to_numeric(d["pop"], errors="coerce")
    return d.dropna(subset=["gdppc"]).reset_index(drop=True)


def maddison_regions(regions=None, since=None, until=None) -> pd.DataFrame:
    """Maddison's OWN regional and world estimates (sheet "Regional data"): year, region,
    gdppc (2011 international dollars), pop (thousands). region in REGIONS or "World".
    Use this for a world or regional line: it is the database's published aggregate,
    with no gaps from changing country coverage. The World row exists for 21 years only
    (1820, 1850, 1870, 1900, 1920, 1940, every ten years 1950-2010, then 2015-2022):
    check .year before plotting, and draw it with marks or as a line through those points."""
    d = _maddison_regions()
    if regions is not None:
        d = d[d.region.isin([regions] if isinstance(regions, str) else list(regions))]
    return _years(d, since, until).copy()


def maddison_world(since=None, until=None, region=None) -> pd.DataFrame:
    """Population-weighted GDP per person over the countries with both series in a year.

    Columns year, gdppc, pop, n (countries). The country set changes from year to
    year, which makes jumps before 1950: for a world or regional LINE use
    maddison_regions() (the database's own estimate). This one is for a balanced
    panel you build yourself (pass the countries through region=).
    """
    d = _maddison().dropna(subset=["gdppc", "pop"])
    if region is not None:
        d = d[d["region"] == region]
    g = d.assign(gdp=d.gdppc * d["pop"]).groupby("year").agg(
        gdp=("gdp", "sum"), pop=("pop", "sum"), n=("iso3", "count")).reset_index()
    g["gdppc"] = g.gdp / g["pop"]
    return _years(g[["year", "gdppc", "pop", "n"]], since, until)


@lru_cache(maxsize=None)
def _pwt() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "pwt110.csv"))


def pwt(isos=None, since=None, until=None, cols=None) -> pd.DataFrame:
    """PWT 11.0 (iso3, country, year, rgdpe, rgdpo, pop, emp, avh, hc, rnna, ctfp, labsh, ...)."""
    d = _years(_isos(_pwt(), isos), since, until)
    if cols:
        d = d[["iso3", "country", "year", *cols]]
    return d.copy()


@lru_cache(maxsize=None)
def wdi_series() -> pd.DataFrame:
    """The approved WDI indicators: code, name, topic, unit, source, license."""
    return pd.read_csv(_need(DER / "wdi_series.csv"))


@lru_cache(maxsize=None)
def wdi_countries() -> pd.DataFrame:
    """WDICountry.csv: Country Code, Short Name, Region, Income Group, ... (aggregates have no Region)."""
    return pd.read_csv(_need(DER / "wdi_countries.csv"))


def wdi(code: str, isos=None, since=None, until=None, countries_only=False) -> pd.DataFrame:
    """One WDI indicator, long: iso3, country, year, value. countries_only drops aggregates (WLD, HIC...)."""
    p = DER / "wdi" / f"{code}.csv"
    if not p.exists():
        if code in set(wdi_series().code):
            raise FileNotFoundError(f"{p} missing: rerun tools/derive_data.py wdi")
        raise KeyError(f"{code} is not an approved WDI indicator (see data/derived/wdi_series.csv)")
    d = pd.read_csv(p)
    if countries_only:
        c = wdi_countries()
        real = set(c.loc[c["Region"].notna(), "Country Code"])
        d = d[d.iso3.isin(real)]
    return _years(_isos(d, isos), since, until).copy()


@lru_cache(maxsize=None)
def _jst() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "jst_r6.csv"))


def jst(isos=None, since=None, until=None, cols=None) -> pd.DataFrame:
    """JST R6: year, country, iso3, pop, rgdpmad, gdp, cpi, stir, ltrate, debtgdp, imports, exports, unemp, crisisJST, ..."""
    d = _years(_isos(_jst(), isos), since, until)
    if cols:
        d = d[["year", "country", "iso3", *cols]]
    return d.copy()


@lru_cache(maxsize=None)
def _gapminder() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "gapminder.csv"))


def gapminder(variable: str, isos=None, since=None, until=GAPMINDER_LAST_YEAR) -> pd.DataFrame:
    """Gapminder Fast Track, years up to 1949 only (licence ruling): iso3 (upper case), name,
    world_4region, world_6region, year, value. variable in: lex,
    child_mortality_0_5_year_olds_dying_per_1000_born, children_per_woman_total_fertility,
    pop, gdp_pcap."""
    if until is None or until > GAPMINDER_LAST_YEAR:
        raise ValueError("Gapminder is used for the years before 1950 only; use wdi() after")
    d = _gapminder()
    d = d[d.variable == variable].drop(columns="variable")
    d = d.assign(iso3=d.iso3.str.upper())
    return _years(_isos(d, isos), since, until).copy()


def pip_percentiles(isos=None, years=None) -> pd.DataFrame:
    """PIP world_100bin (2021 PPP): iso3, year, reporting_level, welfare_type, percentile,
    avg_welfare ($/day), pop_share, welfare_share, quantile, pop."""
    d = pd.read_csv(_need(DER / "pip_percentiles_2021ppp.csv"))
    d = _isos(d, isos)
    if years is not None:
        d = d[d.year.isin(list(years) if not isinstance(years, int) else [years])]
    return d.copy()


def eurostat(dataset: str) -> pd.DataFrame:
    """One Eurostat table, long, with its own dimension columns plus time, value, flag.
    dataset in: prc_hicp_aind, prc_hicp_manr, une_rt_a, gov_10dd_edpt1, nama_10_gdp, and (approved
    2026-11-20) jvs_q_nace2 (job vacancies), une_rt_q, ilc_di12, ilc_di12b, ilc_di12c (Gini before
    and after transfers), ilc_pw01 (life satisfaction), bd_size (business demography)."""
    return pd.read_csv(_need(DER / f"eurostat_{dataset}.csv"), low_memory=False)


@lru_cache(maxsize=None)
def _bls() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "bls_cpi_all_items.csv"), dtype={"item_code": str})


def bls_cpi(series_id: str = "CUUR0000SA0") -> pd.DataFrame:
    """One BLS CPI-U series: series_id, series_title, item_code, item_name, year, period
    (M01..M12; M13 = annual average; S01/S02 half years), value (numeric).
    Default CUUR0000SA0: all items, U.S. city average, not seasonally adjusted, 1982-84=100.
    Series ids: CU + U (not seasonally adjusted) or S + R (monthly) + area 0000 (U.S. city
    average) + item code, e.g. CUUR0000SETG01 airline fares, CUUR0000SAS services,
    CUUR0000SAC commodities, CUUR0000SEEE01 computers. Find codes with bls_cpi_items()."""
    d = _bls()
    out = d[d.series_id == series_id]
    if out.empty:
        raise KeyError(f"{series_id}: not in the downloaded CPI files (see bls_cpi_items())")
    return out.copy()


def bls_cpi_items(pattern: str = "") -> pd.DataFrame:
    """The CPI series available (U.S. city average): series_id, item_code, item_name, seasonal,
    first and last year. pattern filters item_name (case-insensitive regex)."""
    d = _bls()
    d = d[d.area_code == "0000"]
    if pattern:
        d = d[d.item_name.str.contains(pattern, case=False, regex=True, na=False)]
    return (d.groupby(["series_id", "item_code", "item_name", "seasonal"]).year
            .agg(["min", "max"]).reset_index())


def ceds(pollutant: str = "co2", by: str = "country", isos=None, since=None, until=None):
    """CEDS emissions, kt per year: iso3 (upper case), year, value (+ sector for by='country_sector')."""
    d = pd.read_csv(_need(DER / f"ceds_{pollutant}_by_{by}.csv"))
    d["iso3"] = d.pop("iso3_lower").str.upper()
    return _years(_isos(d, isos), since, until).copy()


def eia_energy(series: str = "Energy consumption per capita", units=None, isos=None,
               since=None, until=None) -> pd.DataFrame:
    """EIA international: iso3 (WLD = world; a region is a "+"-joined list of codes), series,
    units, year, value. series in:
    'Total energy consumption', 'Energy consumption per capita', 'Primary energy consumption',
    'Total energy production', 'Crude oil including lease condensate production',
    'Petroleum and other liquids production', 'Petroleum and other liquids consumption',
    'Refined petroleum products consumption' (oil: units 'thousand barrels per day' and others;
    always pass units=)."""
    d = pd.read_csv(_need(DER / "eia_energy.csv"))
    d = d[d.series == series]
    if units is not None:
        d = d[d.units == units]
    return _years(_isos(d, isos), since, until).copy()


def faostat_crops(item: str = "Cereals, primary", element: str = "Yield") -> pd.DataFrame:
    """FAOSTAT crops: Area, m49, Item, Element, Year, Unit, Value, Flag (yield in kg/ha)."""
    d = pd.read_csv(_need(DER / "faostat_crops.csv"), dtype={"m49": str})
    return d[(d.Item == item) & (d.Element == element)].copy()


def gravity(since=None, until=None, columns=None) -> pd.DataFrame:
    """CEPII Gravity, BACI flows only (thousands of current US dollars), one row per
    (year, iso3_o, iso3_d). Large: pass columns= and a year range."""
    d = pd.read_csv(_need(DER / "gravity_baci.csv.gz"), usecols=columns)
    return _years(d, since, until).copy()


def nsw(sample: str = "nsw_dw") -> pd.DataFrame:
    """NSW / LaLonde samples: nsw, nsw_dw, cps_controls, psid_controls (treat, age, education,
    black, hispanic, married, nodegree, re74, re75, re78)."""
    return pd.read_csv(_need(DER / f"nsw_{sample}.csv"))


# statsmodels' bundled datasets: they ship with the package (no download). Only those whose
# COPYRIGHT says public domain are allowed (sync 2026-11-20); "used with permission",
# "???" and World-Bank-terms datasets (ccard, committee, copper, cpunish, fair, fertility,
# scotland, spector, star98, cancer, heart, china_smoking, interest_inflation) are not.
SM_ALLOWED = {"anes96", "co2", "danish_data", "elec_equip", "elnino", "engel", "grunfeld",
              "longley", "macrodata", "modechoice", "nile", "randhie", "stackloss",
              "statecrime", "strikes", "sunspots"}


def sm_dataset(name: str) -> pd.DataFrame:
    """A public-domain statsmodels bundled dataset as a DataFrame (e.g. macrodata: US quarterly
    1959Q1-2009Q3; grunfeld; randhie; engel). Source line: SOURCE["statsmodels"] plus the
    dataset's own SOURCE note (statsmodels.datasets.<name>.SOURCE)."""
    if name not in SM_ALLOWED:
        raise KeyError(f"{name}: not an allowed statsmodels dataset ({sorted(SM_ALLOWED)})")
    import importlib
    mod = importlib.import_module(f"statsmodels.datasets.{name}")
    return mod.load_pandas().data.copy()


# ---- second approval, 2026-11-20 (sources/DATA_SOURCES_TO_APPROVE.md, section C) ----

@lru_cache(maxsize=1)
def _bls_ap() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "bls_ap.csv"), dtype={"item_code": str, "area_code": str})


def bls_ap(pattern: str = "", area_code: str = "0000", annual: bool = False) -> pd.DataFrame:
    """BLS average retail prices in dollars (food and gasoline), monthly, U.S. city average by default.
    `pattern` is a case-insensitive regex on item_name ("Bread, white", "Gasoline, unleaded regular").
    annual=True returns the mean of the twelve months, for complete years only.
    Source line: SOURCE["bls_ap"]."""
    d = _bls_ap()
    d = d[(d["area_code"] == area_code) & d["item_name"].str.contains(pattern, case=False, regex=True)].copy()
    d["month"] = d["period"].str[1:].astype(int)
    if annual:
        g = d.groupby(["series_id", "item_name", "year"])["value"]
        d = g.mean().where(g.count() == 12).dropna().reset_index()
    return d.reset_index(drop=True)


def bls_ap_items(pattern: str = "") -> pd.DataFrame:
    """The items with a U.S. city average price series, with their first and last year."""
    d = _bls_ap()
    d = d[(d["area_code"] == "0000") & d["item_name"].str.contains(pattern, case=False, regex=True)]
    return d.groupby(["item_code", "item_name"])["year"].agg(["min", "max"]).reset_index()


@lru_cache(maxsize=1)
def _jolts() -> pd.DataFrame:
    return pd.read_csv(_need(DER / "bls_jolts.csv"),
                       dtype={"industry_code": str, "sizeclass_code": str})


def jolts(element: str = "JO", rate: bool = True, industry_code: str = "000000",
          seasonal: str = "S", sizeclass_code: str = "00") -> pd.DataFrame:
    """BLS JOLTS, United States, monthly from 2000-12. element: JO job openings, HI hires,
    TS total separations, QU quits, LD layoffs and discharges, OS other separations.
    rate=True gives the rate in percent; False the level in thousands. Industry 000000 is total
    nonfarm. Columns: year, month, value. Source line: SOURCE["jolts"]."""
    d = _jolts()
    d = d[(d["dataelement_code"] == element) & (d["ratelevel_code"] == ("R" if rate else "L"))
          & (d["industry_code"] == industry_code) & (d["seasonal"] == seasonal)
          & (d["sizeclass_code"] == sizeclass_code)].copy()
    if d.empty:
        raise KeyError(f"no JOLTS series for {element}, rate={rate}, {industry_code}, {seasonal}")
    d["month"] = d["period"].str[1:].astype(int)
    return d[["year", "month", "value"]].sort_values(["year", "month"]).reset_index(drop=True)


CEX_TABLES = {
    ("mean-item-share-average-standard-error", 2012), ("mean-item-share-average-standard-error", 2015),
    ("mean-item-share-average-standard-error", 2025), ("aggregate-group-share", 2015),
    ("aggregate-group-share", 2025),
}


def cex_table(table: str, year: int) -> pd.DataFrame:
    """A BLS Consumer Expenditure table by quintile of income before taxes, as the raw grid of the
    published workbook (every cell is text; row 0.. are the BLS headers). Locate rows by their label
    in column 0, and convert the cells you need with pd.to_numeric. Available: CEX_TABLES (the
    2005 aggregate table was rejected at download). Source line: SOURCE["cex"]."""
    if (table, year) not in CEX_TABLES:
        raise KeyError(f"{table} {year}: not downloaded ({sorted(CEX_TABLES)})")
    return pd.read_csv(_need(DER / f"bls_cex_{table}-{year}.csv"), dtype=str)


@lru_cache(maxsize=2)
def _fed(rel: str) -> pd.DataFrame:
    return pd.read_csv(_need(DER / f"fed_{rel}.csv"), parse_dates=["date"])


def fed_series(rel: str, series: str) -> pd.DataFrame:
    """One series of a Federal Reserve release, `rel` "h15" or "h41". H.15: every monthly (.M) and
    annual (.A) series, plus the fed funds rate daily (RIFSPFF_N.B), weekly (RIFSPFF_N.WW) and monthly
    (RIFSPFF_N.M), in percent. H.4.1: the consolidated (non-district) series, in millions of dollars;
    total assets, Wednesday level, is RESPPMA_N.WW. Find codes with fed_find(). Columns: date, value."""
    d = _fed(rel)
    d = d[d["series"] == series]
    if d.empty:
        raise KeyError(f"{rel}: no series {series}")
    return d[["date", "value"]].sort_values("date").reset_index(drop=True)


def fed_find(rel: str, pattern: str) -> pd.DataFrame:
    """Series codes and descriptions of a release whose description matches `pattern` (regex)."""
    d = _fed(rel)[["series", "description"]].drop_duplicates()
    return d[d["description"].fillna("").str.contains(pattern, case=False, regex=True)].reset_index(drop=True)


def ecb_total_assets() -> pd.DataFrame:
    """Eurosystem consolidated balance sheet, total assets, weekly (ECB series
    ILM.W.U2.C.T000000.Z5.Z01), in millions of euro, from 1999. Columns: week ("1999-W01"), eur_million.
    Source line: SOURCE["ecb"]; say that any derived number is ours."""
    return pd.read_csv(_need(DER / "ecb_total_assets.csv"))
