#!/usr/bin/env python3
"""Derive compact, tidy tables from data/raw/ into data/derived/.

Run once after tools/fetch_data.py (the main session does it; writers never need
to). Every table is long ("tidy"): one row per (entity, year[, variable]).
Large sources are read in chunks so that no step needs more than ~1.5 GB.

    .venv/bin/python -I tools/derive_data.py [step ...]

Steps: maddison pwt jst gapminder wdi pip eurostat bls ceds eia faostat gravity nsw

Licence filters applied here (sources/DATA_SOURCES_TO_APPROVE.md):
  * WDI: only indicators whose WDISeries "License Type" is CC BY 4.0 (the six
    SIPRI-licensed military indicators are left out).
  * CEPII Gravity: only the BACI trade flow (CEPII's own product). The UN
    Comtrade and IMF flows carried in the file have their own terms: dropped.
  * Gapminder: kept whole here; figdata/lib/econdata.py serves it for years
    before 1950 only (after 1950 the underlying data are IHME's and the UN's).
"""
from __future__ import annotations

import gzip
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "derived"


def w(df: pd.DataFrame, name: str) -> None:
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False, float_format="%.6g")
    print(f"  {name}: {len(df):,} rows")


def maddison() -> None:
    f = RAW / "maddison2023" / "mpd2023_web.xlsx"
    full = pd.read_excel(f, sheet_name="Full data")
    full = full.rename(columns={"countrycode": "iso3", "gdppc": "gdppc", "pop": "pop"})
    w(full[["iso3", "country", "region", "year", "gdppc", "pop"]], "maddison_countries.csv")
    reg = pd.read_excel(f, sheet_name="Regional data", header=None)
    w(reg, "maddison_regional_raw.csv")   # the sheet as published (two header rows)


def pwt() -> None:
    d = pd.read_excel(RAW / "pwt110" / "pwt110.xlsx", sheet_name="Data")
    w(d.rename(columns={"countrycode": "iso3"}), "pwt110.csv")


def jst() -> None:
    d = pd.read_excel(RAW / "jst_r6" / "JSTdatasetR6.xlsx", sheet_name="Sheet1")
    w(d.rename(columns={"iso": "iso3"}), "jst_r6.csv")


def gapminder() -> None:
    g = RAW / "gapminder_fasttrack"
    geo = pd.read_csv(g / "geo_country.csv")
    geo = geo[["country", "name", "iso3166_1_alpha3", "world_4region", "world_6region"]]
    frames = []
    for ind in ("lex", "child_mortality_0_5_year_olds_dying_per_1000_born",
                "children_per_woman_total_fertility", "pop", "gdp_pcap"):
        d = pd.read_csv(g / f"{ind}.csv").rename(columns={"time": "year", ind: "value"})
        d["variable"] = ind
        frames.append(d)
    d = pd.concat(frames).merge(geo, on="country", how="left")
    d = d.rename(columns={"iso3166_1_alpha3": "iso3"})
    w(d[["iso3", "name", "world_4region", "world_6region", "year", "variable", "value"]],
      "gapminder.csv")


def wdi() -> None:
    base = RAW / "wdi" / "WDI_CSV_2026_11_11_extracted"
    ser = pd.read_csv(base / "WDISeries.csv", encoding="utf-8-sig")
    lic = ser["License Type"].str.replace(" ", "").str.upper()
    ok = ser[lic == "CCBY-4.0"].copy()
    ok = ok.rename(columns={"Series Code": "code", "Indicator Name": "name",
                            "Unit of measure": "unit", "Source": "source",
                            "License Type": "license", "Topic": "topic"})
    w(ok[["code", "name", "topic", "unit", "source", "license"]], "wdi_series.csv")
    w(pd.read_csv(base / "WDICountry.csv", encoding="utf-8-sig"), "wdi_countries.csv")
    keep = set(ok["code"])
    outdir = OUT / "wdi"
    outdir.mkdir(parents=True, exist_ok=True)
    n = 0
    for chunk in pd.read_csv(base / "WDICSV.csv", encoding="utf-8-sig", chunksize=20000):
        chunk = chunk[chunk["Indicator Code"].isin(keep)]
        years = [c for c in chunk.columns if c.isdigit()]
        long = chunk.melt(id_vars=["Country Code", "Country Name", "Indicator Code"],
                          value_vars=years, var_name="year", value_name="value").dropna()
        long = long.rename(columns={"Country Code": "iso3", "Country Name": "country",
                                    "Indicator Code": "code"})
        for code, part in long.groupby("code"):
            p = outdir / f"{code}.csv"
            part[["iso3", "country", "year", "value"]].to_csv(
                p, mode="a", header=not p.exists(), index=False, float_format="%.8g")
            n += len(part)
    print(f"  wdi/: {n:,} rows in {len(list(outdir.glob('*.csv')))} indicator files")


def pip() -> None:
    d = pd.read_csv(RAW / "pip_percentiles" / "world_100bin_2021ppp.csv")
    w(d.rename(columns={"country_code": "iso3"}), "pip_percentiles_2021ppp.csv")


def eurostat() -> None:
    for f in sorted([*(RAW / "eurostat").glob("*.tsv.gz"), *(RAW / "eurostat2").glob("*.tsv.gz")]):
        with gzip.open(f, "rt", encoding="utf-8") as h:
            d = pd.read_csv(h, sep="\t")
        key = d.columns[0]
        dims = key.split("\\")[0].split(",")
        d[dims] = d[key].str.split(",", expand=True)
        d = d.drop(columns=[key]).melt(id_vars=dims, var_name="time", value_name="raw")
        d["time"] = d["time"].str.strip()
        d["value"] = pd.to_numeric(d["raw"].astype(str).str.extract(r"([-0-9.]+)")[0],
                                   errors="coerce")
        d["flag"] = d["raw"].astype(str).str.extract(r"[-0-9.:]+\s*([a-z]*)")[0]
        w(d.drop(columns=["raw"]).dropna(subset=["value"]),
          f"eurostat_{f.name.replace('.tsv.gz', '')}.csv")


def bls() -> None:
    """Every CPI-U series of the downloaded cu.data.* files, values numeric.

    bls_cpi_all_items.csv keeps its name (all files, not only all items) for the
    loader; item_code and item_name come from cu.series and cu.item."""
    b = RAW / "bls_cpi"
    parts = []
    for f in sorted(b.glob("cu.data.*")):
        d = pd.read_csv(f, sep="\t", dtype=str)
        d.columns = [c.strip() for c in d.columns]
        parts.append(d)
    d = pd.concat(parts, ignore_index=True)
    for c in d.columns:
        d[c] = d[c].astype(str).str.strip()
    d["year"] = d["year"].astype(int)
    d["value"] = pd.to_numeric(d["value"], errors="coerce")
    d = d.dropna(subset=["value"]).drop_duplicates(["series_id", "year", "period"])
    s = pd.read_csv(b / "cu.series", sep="\t", dtype=str)
    s.columns = [c.strip() for c in s.columns]
    for c in s.columns:
        s[c] = s[c].astype(str).str.strip()
    it = pd.read_csv(b / "cu.item", sep="\t", dtype=str)
    it.columns = [c.strip() for c in it.columns]
    it = it.rename(columns={"item_name": "item_name"})[["item_code", "item_name"]]
    for c in it.columns:
        it[c] = it[c].astype(str).str.strip()
    s = s.merge(it, on="item_code", how="left")
    d = d.merge(s[["series_id", "series_title", "area_code", "item_code", "item_name", "seasonal",
                   "base_period"]], on="series_id")
    w(d[["series_id", "series_title", "area_code", "item_code", "item_name", "seasonal",
         "base_period", "year", "period", "value"]], "bls_cpi_all_items.csv")


def ceds() -> None:
    base = next((RAW / "ceds_2025").glob("*_extracted")) / "CEDS_v_2025_03_18_aggregate"
    for em in ("CO2", "SO2"):
        for kind in ("by_country", "by_country_sector"):
            f = base / f"{em}_CEDS_estimates_{kind}_v_2025_03_18.csv"
            d = pd.read_csv(f)
            ids = [c for c in d.columns if not c.startswith("X")]
            d = d.melt(id_vars=ids, var_name="year", value_name="value")
            d["year"] = d["year"].str[1:].astype(int)
            w(d.rename(columns={"country": "iso3_lower"}), f"ceds_{em.lower()}_{kind}.csv")


def eia() -> None:
    rows = []
    wanted = ("Total energy consumption, ", "Energy consumption per capita, ",
              "Primary energy consumption, ", "Total energy production, ",
              "Crude oil including lease condensate production, ",
              "Petroleum and other liquids production, ",
              "Petroleum and other liquids consumption, ",
              "Refined petroleum products consumption, ")
    with open(next((RAW / "eia_intl").glob("*_extracted")) / "INTL.txt", encoding="utf-8") as h:
        for line in h:
            s = json.loads(line)
            name = s.get("name", "")
            if not name.startswith(wanted) or s.get("f") != "A" or "data" not in s:
                continue
            for yr, v in s["data"]:
                if isinstance(v, (int, float)):
                    rows.append((s.get("geography"), name.split(", ")[0], s.get("units"),
                                 int(yr), v))
    w(pd.DataFrame(rows, columns=["iso3", "series", "units", "year", "value"]), "eia_energy.csv")


def faostat() -> None:
    base = next((RAW / "faostat_qcl").glob("*_extracted"))
    f = base / "Production_Crops_Livestock_E_All_Data_(Normalized).csv"
    items = {"Cereals, primary", "Wheat", "Rice", "Maize (corn)", "Potatoes", "Soya beans",
             "Barley", "Sorghum", "Millet"}
    keep = []
    for chunk in pd.read_csv(f, chunksize=500000, encoding="latin-1",
                             usecols=["Area Code (M49)", "Area", "Item", "Element", "Year",
                                      "Unit", "Value", "Flag"]):
        keep.append(chunk[chunk["Item"].isin(items) &
                          chunk["Element"].isin(["Yield", "Production", "Area harvested"])])
    d = pd.concat(keep)
    d["m49"] = d.pop("Area Code (M49)").str.strip("'")
    w(d, "faostat_crops.csv")


def gravity() -> None:
    f = next((RAW / "cepii_gravity").glob("*_extracted")) / "Gravity_V202211.csv"
    cols = ["year", "iso3_o", "iso3_d", "country_exists_o", "country_exists_d", "dist",
            "distw_harmonic", "contig", "comlang_off", "comcol", "col45", "fta_wto",
            "gatt_o", "gatt_d", "wto_o", "wto_d", "eu_o", "eu_d", "pop_o", "pop_d",
            "gdp_o", "gdp_d", "tradeflow_baci"]
    keep = []
    for chunk in pd.read_csv(f, usecols=cols, chunksize=400000, low_memory=False):
        chunk = chunk[chunk["tradeflow_baci"].notna() & (chunk["tradeflow_baci"] > 0)]
        keep.append(chunk)
    d = pd.concat(keep)
    p = OUT / "gravity_baci.csv.gz"
    d.to_csv(p, index=False, float_format="%.6g", compression="gzip")
    print(f"  gravity_baci.csv.gz: {len(d):,} rows")


def nsw() -> None:
    for name in ("nsw", "nsw_dw", "cps_controls", "psid_controls"):
        w(pd.read_stata(RAW / "nsw_dehejia" / f"{name}.dta"), f"nsw_{name}.csv")



# ---- second approval, 2026-11-20 (DATA_SOURCES_TO_APPROVE.md section C) ----

def _bls_flat(path: Path) -> pd.DataFrame:
    d = pd.read_csv(path, sep="\t", dtype=str)
    d.columns = [c.strip() for c in d.columns]
    return d.apply(lambda c: c.str.strip())


def bls_ap() -> None:
    """BLS average retail prices (food, gasoline): one row per series and month."""
    r = RAW / "bls_ap"
    data = pd.concat([_bls_flat(r / f) for f in ("ap.data.3.Food", "ap.data.2.Gasoline")])
    data["value"] = pd.to_numeric(data["value"], errors="coerce")
    data["year"] = data["year"].astype(int)
    ser = _bls_flat(r / "ap.series")[["series_id", "area_code", "item_code"]]
    item = _bls_flat(r / "ap.item")
    area = _bls_flat(r / "ap.area")[["area_code", "area_name"]]
    d = data.merge(ser, on="series_id").merge(item, on="item_code").merge(area, on="area_code")
    d = d[d["period"].str.match(r"M(0[1-9]|1[0-2])$")]
    w(d[["series_id", "item_code", "item_name", "area_code", "area_name", "year", "period", "value"]]
      .dropna(subset=["value"]), "bls_ap.csv")


def jolts() -> None:
    """BLS JOLTS, national and total-nonfarm/private industries, all size classes, levels and rates."""
    r = RAW / "bls_jolts"
    data = _bls_flat(r / "jt.data.1.AllItems")
    ser = _bls_flat(r / "jt.series")
    ser = ser[(ser["state_code"] == "00") & (ser["area_code"] == "00000")]
    d = data.merge(ser[["series_id", "seasonal", "industry_code", "sizeclass_code", "dataelement_code",
                        "ratelevel_code"]], on="series_id")
    for f, k in (("jt.industry", "industry"), ("jt.dataelement", "dataelement"), ("jt.sizeclass", "sizeclass")):
        m = _bls_flat(r / f).iloc[:, :2]
        d = d.merge(m, on=f"{k}_code", how="left")
    d["value"] = pd.to_numeric(d["value"], errors="coerce")
    d["year"] = d["year"].astype(int)
    d = d[d["period"].str.match(r"M(0[1-9]|1[0-2])$")]
    w(d.drop(columns=["footnote_codes"], errors="ignore").dropna(subset=["value"]), "bls_jolts.csv")


def cex() -> None:
    """BLS Consumer Expenditure tables by income fifth: every sheet cell kept as text, one CSV per workbook."""
    for f in sorted((RAW / "bls_cex").glob("*.xlsx")):
        x = pd.read_excel(f, sheet_name=0, header=None, dtype=str, engine="openpyxl")
        w(x, f"bls_cex_{f.stem}.csv")


def _fed_xml(path: Path, keep) -> pd.DataFrame:
    import xml.etree.ElementTree as ET
    rows, cur, desc = [], None, None
    for ev, el in ET.iterparse(path, events=("start", "end")):
        tag = el.tag.rsplit("}", 1)[-1]
        if ev == "start" and tag == "Series":
            cur, desc = el.attrib.get("SERIES_NAME"), None
        elif ev == "end" and tag == "AnnotationText" and desc is None:
            desc = el.text
        elif ev == "end" and tag == "Obs" and cur and keep(cur, desc or ""):
            rows.append((cur, desc, el.attrib.get("TIME_PERIOD"), el.attrib.get("OBS_VALUE")))
        elif ev == "end" and tag == "Series":
            el.clear()
    d = pd.DataFrame(rows, columns=["series", "description", "date", "value"])
    d["value"] = pd.to_numeric(d["value"], errors="coerce")
    return d.dropna(subset=["value"])


def fed() -> None:
    """Fed H.15 (all monthly and annual series, plus the daily and weekly fed funds rate) and
    H.4.1 (consolidated, non-district series: total assets, securities, reserves, currency)."""
    h15 = _fed_xml(RAW / "fed_h15" / "FRB_h15_xml_extracted" / "H15_data.xml",
                   lambda s, d: s.endswith((".M", ".A")) or s.startswith("RIFSPFF_N."))
    w(h15, "fed_h15.csv")
    h41 = _fed_xml(RAW / "fed_h41" / "FRB_h41_xml_extracted" / "H41_data.xml",
                   lambda s, d: "District" not in (d or ""))
    w(h41, "fed_h41.csv")


def ecb() -> None:
    d = pd.read_csv(RAW / "ecb_ilm" / "ILM_W_U2_C_T000000_Z5_Z01.csv", usecols=["TIME_PERIOD", "OBS_VALUE"])
    d.columns = ["week", "eur_million"]
    w(d, "ecb_total_assets.csv")

STEPS = {f.__name__: f for f in (bls_ap, jolts, cex, fed, ecb, maddison, pwt, jst, gapminder, wdi, pip, eurostat, bls, ceds,
                                 eia, faostat, gravity, nsw)}


def main(argv: list[str]) -> int:
    steps = argv or list(STEPS)
    OUT.mkdir(parents=True, exist_ok=True)
    for s in steps:
        print(f"[{s}]")
        if s == "wdi":
            wd = OUT / "wdi"
            if wd.exists() and any(wd.iterdir()):
                print("  data/derived/wdi/ is not empty: remove its files by name first")
                continue
        STEPS[s]()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
