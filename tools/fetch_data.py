#!/usr/bin/env python3
"""Download the datasets the user approved (2026-11-20), with safety checks.

Only the sources listed in SOURCES are fetched. Their list and licences are in
sources/DATA_SOURCES_TO_APPROVE.md, section A. A new source needs the user's
approval first (workspace rule) before it is added here.

The user's safety rules, 2026-11-20:
  1. Official domains only. Every URL and every redirect hop must be HTTPS and on
     ALLOWED_HOSTS.
  2. No macros. A workbook carrying VBA (xl/vbaProject.bin, or a macroEnabled
     content type) is rejected. Workbooks are read only with pandas/openpyxl,
     which never run macros.
  3. No executables. An archive is listed BEFORE extraction and is rejected
     whole if any member has a forbidden extension, is a symlink, escapes the
     target directory, or is unreasonably large. Only data and documentation
     extensions are extracted. Every file kept is then checked for executable
     magic bytes (MZ, ELF, #!).
  4. A virus scan follows: Windows Defender over data/raw (tools/scan_data.sh).

Run from the repo root as   .venv/bin/python -I tools/fetch_data.py [key ...]
(-I: never import anything from the data directories). Each source lands in its
own new directory data/raw/<key>/. A directory that already exists is skipped
unless --force is given. The manifest goes to data/MANIFEST.json and
data/MANIFEST.md.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import http.client
import json
import stat
import sys
import urllib.parse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
UA = "one-course-data-fetch/1.0"

ALLOWED_HOSTS = {
    "dataverse.nl", "objectstore.surf.nl",                 # Maddison, PWT (GGDC on DataverseNL / SURF)
    "datacatalogfiles.worldbank.org",                      # WDI, PIP
    "www.macrohistory.net", "sfff5b3ac9317c4be.jimcontent.com",  # JST (site and its own file host)
    "raw.githubusercontent.com",                           # Gapminder's open-numbers repositories
    "ec.europa.eu",                                        # Eurostat
    "download.bls.gov",                                    # BLS
    "zenodo.org",                                          # CEDS
    "www.eia.gov",                                         # EIA
    "bulks-faostat.fao.org",                               # FAOSTAT
    "www.cepii.fr",                                        # CEPII Gravity
    "users.nber.org",                                      # Dehejia NSW
    # second approval, 2026-11-20 (DATA_SOURCES_TO_APPROVE.md section C)
    "www.bls.gov",                                         # BLS Consumer Expenditure tables
    "www.federalreserve.gov",                              # Fed H.15, H.4.1 (release XML zips)
    "data-api.ecb.europa.eu",                              # ECB Data Portal API
    "api.worldbank.org",                                   # World Bank API (ICP 2021, source 90)
}
# Path restrictions for shared-infrastructure hosts: only these prefixes are fetched.
PATH_PREFIX = {
}
GITHUB_OWNER_PREFIX = "/open-numbers/"                     # raw.githubusercontent.com: this owner only

DATA_EXT = {".csv", ".tsv", ".txt", ".dta", ".xlsx", ".xls", ".md", ".json", ".gz", ".xml"}
FORBIDDEN_EXT = {
    ".exe", ".bat", ".cmd", ".com", ".scr", ".pif", ".js", ".jse", ".vbs", ".vbe", ".wsf",
    ".wsh", ".ps1", ".psm1", ".sh", ".bash", ".py", ".pyc", ".pyw", ".pl", ".rb", ".php",
    ".jar", ".class", ".msi", ".msp", ".dll", ".so", ".dylib", ".lnk", ".hta", ".reg",
    ".xlsm", ".xlsb", ".xltm", ".xlam", ".docm", ".dotm", ".pptm", ".potm", ".ppam",
    ".app", ".apk", ".deb", ".rpm", ".bin", ".elf", ".cpl", ".inf", ".iso", ".img", ".vhd",
}
EXEC_MAGIC = (b"MZ", b"\x7fELF", b"#!", b"\xca\xfe\xba\xbe", b"\xcf\xfa\xed\xfe")
MAX_DOWNLOAD = 400 * 2**20          # bytes per file
MAX_UNCOMPRESSED = 3 * 2**30        # bytes per archive
MAX_RATIO = 200                     # zip-bomb guard (uncompressed / compressed, per member)

ES = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/{}/?format=TSV&compressed=true"
GM = ("https://raw.githubusercontent.com/open-numbers/ddf--gapminder--fasttrack/master/"
      "countries_etc_datapoints/ddf--datapoints--{}--by--country--time.csv")
BLS = "https://download.bls.gov/pub/time.series/cu/{}"
NSW = "https://users.nber.org/~rdehejia/data/{}"

# key -> list of (url, filename, kind); kind in xlsx | csv | zip | dta | tsvgz | text
SOURCES: dict[str, list[tuple[str, str, str]]] = {
    "maddison2023": [("https://dataverse.nl/api/access/datafile/421302?format=original",
                      "mpd2023_web.xlsx", "xlsx")],
    "pwt110": [("https://dataverse.nl/api/access/datafile/554105?format=original",
                "pwt110.xlsx", "xlsx")],
    "wdi": [("https://datacatalogfiles.worldbank.org/ddh-published/0037712/DR0095335/"
             "WDI_CSV_2026_11_11.zip", "WDI_CSV_2026_11_11.zip", "zip")],
    "pip_percentiles": [("https://datacatalogfiles.worldbank.org/ddh-published/0063646/"
                         "DR0090357/world_100bin.csv", "world_100bin_2021ppp.csv", "csv")],
    "jst_r6": [("https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.xlsx"
                "?t=1763503850", "JSTdatasetR6.xlsx", "xlsx")],
    "gapminder_fasttrack": [
        (GM.format(i), f"{i}.csv", "csv") for i in (
            "lex", "child_mortality_0_5_year_olds_dying_per_1000_born",
            "children_per_woman_total_fertility", "pop", "gdp_pcap")
    ] + [("https://raw.githubusercontent.com/open-numbers/ddf--gapminder--fasttrack/master/"
          "ddf--entities--geo--country.csv", "geo_country.csv", "csv")],
    "eurostat": [(ES.format(d), f"{d}.tsv.gz", "tsvgz") for d in (
        "prc_hicp_aind", "prc_hicp_manr", "une_rt_a", "gov_10dd_edpt1", "nama_10_gdp")],
    # Second approval (2026-11-20, DATA_SOURCES_TO_APPROVE.md section C, C1)
    "eurostat2": [(ES.format(d), f"{d}.tsv.gz", "tsvgz") for d in (
        "jvs_q_nace2", "une_rt_q", "ilc_di12", "ilc_di12b", "ilc_di12c", "ilc_pw01", "bd_size")],
    "bls_ap": [("https://download.bls.gov/pub/time.series/ap/" + f, f, "text") for f in (
        "ap.data.3.Food", "ap.data.2.Gasoline", "ap.series", "ap.item", "ap.area")],
    "bls_jolts": [("https://download.bls.gov/pub/time.series/jt/" + f, f, "text") for f in (
        "jt.data.1.AllItems", "jt.series", "jt.dataelement", "jt.industry", "jt.ratelevel",
        "jt.sizeclass", "jt.state", "jt.area")],
    "bls_cex": [
        (f"https://www.bls.gov/cex/tables/calendar-year/{t}/cu-income-quintiles-before-taxes-{y}.xlsx",
         f"{t}-{y}.xlsx", "xlsx")
        for t, ys in (("mean-item-share-average-standard-error", (2012, 2015, 2025)),
                      ("aggregate-group-share", (2015, 2025))) for y in ys],
    # aggregate-group-share-2005.xlsx was rejected (a binary part); it is not used.
    "fed_h15": [("https://www.federalreserve.gov/releases/h15/data/FRB_h15_xml.zip",
                 "FRB_h15_xml.zip", "zip")],
    "fed_h41": [("https://www.federalreserve.gov/releases/h41/data/FRB_h41_xml.zip",
                 "FRB_h41_xml.zip", "zip")],
    "ecb_ilm": [("https://data-api.ecb.europa.eu/service/data/ILM/W.U2.C.T000000.Z5.Z01?format=csvdata",
                 "ILM_W_U2_C_T000000_Z5_Z01.csv", "text")],
    # USGS DS 140: dropped 2026-11-20. Every workbook carries a binary part (printerSettings.bin); the user
    # rules that no file with a binary or macro part is used, whatever the part is.
    "bls_cpi": [(BLS.format(f), f, "text") for f in (
        "cu.data.1.AllItems", "cu.series", "cu.item", "cu.area", "cu.footnote",
        # item indexes (2026-11-20 sync: airline fares, services/commodities, food, computers)
        "cu.data.2.Summaries", "cu.data.11.USFoodBeverage", "cu.data.14.USTransportation",
        "cu.data.17.USEducationAndCommunication", "cu.data.20.USCommoditiesServicesSpecial")],
    "ceds_2025": [("https://zenodo.org/records/15059443/files/"
                   "CEDS_v_2025_03_18_aggregate.zip?download=1",
                   "CEDS_v_2025_03_18_aggregate.zip", "zip")],
    "eia_intl": [("https://www.eia.gov/opendata/bulk/INTL.zip", "INTL.zip", "zip")],
    "faostat_qcl": [("https://bulks-faostat.fao.org/production/"
                     "Production_Crops_Livestock_E_All_Data_(Normalized).zip",
                     "Production_Crops_Livestock_E_All_Data_Normalized.zip", "zip")],
    "cepii_gravity": [("https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip",
                       "Gravity_csv_V202211.zip", "zip")],
    "nsw_dehejia": [(NSW.format(f), f, "dta") for f in (
        "nsw.dta", "nsw_dw.dta", "cps_controls.dta", "psid_controls.dta")],
}


class Rejected(Exception):
    pass


def check_url(url: str) -> urllib.parse.SplitResult:
    u = urllib.parse.urlsplit(url)
    if u.scheme != "https":
        raise Rejected(f"not https: {url}")
    if u.hostname not in ALLOWED_HOSTS:
        raise Rejected(f"host not allowed: {u.hostname}")
    if u.hostname == "raw.githubusercontent.com" and not u.path.startswith(GITHUB_OWNER_PREFIX):
        raise Rejected(f"GitHub path outside open-numbers: {u.path}")
    if u.hostname in PATH_PREFIX and not u.path.startswith(PATH_PREFIX[u.hostname]):
        raise Rejected(f"path outside {PATH_PREFIX[u.hostname]} on {u.hostname}: {u.path}")
    return u


def download(url: str, dest: Path) -> list[str]:
    """GET with manual redirects; every hop is checked against the allowlist."""
    hops = []
    for _ in range(6):
        u = check_url(url)
        hops.append(url.split("?X-Amz")[0])
        conn = http.client.HTTPSConnection(u.hostname, timeout=120)
        path = u.path + (("?" + u.query) if u.query else "")
        conn.request("GET", path, headers={"User-Agent": UA})
        r = conn.getresponse()
        if r.status in (301, 302, 303, 307, 308):
            url = urllib.parse.urljoin(url, r.getheader("Location"))
            r.read()
            conn.close()
            continue
        if r.status != 200:
            raise Rejected(f"HTTP {r.status} for {url}")
        n = 0
        with open(dest, "wb") as f:
            while chunk := r.read(1 << 20):
                n += len(chunk)
                if n > MAX_DOWNLOAD:
                    raise Rejected(f"larger than {MAX_DOWNLOAD} bytes")
                f.write(chunk)
        conn.close()
        return hops
    raise Rejected("too many redirects")


def head_bytes(p: Path, n: int = 8) -> bytes:
    with open(p, "rb") as f:
        return f.read(n)


def no_exec_magic(p: Path) -> None:
    h = head_bytes(p)
    if any(h.startswith(m) for m in EXEC_MAGIC):
        raise Rejected(f"executable magic bytes in {p.name}")


def check_xlsx(p: Path) -> None:
    if not zipfile.is_zipfile(p):
        raise Rejected(f"{p.name} is not an OOXML (zip) workbook")
    with zipfile.ZipFile(p) as z:
        names = z.namelist()
        if "[Content_Types].xml" not in names:
            raise Rejected(f"{p.name}: no [Content_Types].xml")
        if any("vbaProject" in n or n.lower().endswith(".bin") for n in names):
            raise Rejected(f"{p.name}: contains a VBA/binary part (macros)")
        ct = z.read("[Content_Types].xml").decode("utf-8", "replace")
        if "macroEnabled" in ct or "vbaProject" in ct:
            raise Rejected(f"{p.name}: macro-enabled content type")
        for n in names:
            if Path(n).suffix.lower() in FORBIDDEN_EXT:
                raise Rejected(f"{p.name}: embedded {n}")


def check_text(p: Path) -> None:
    no_exec_magic(p)
    with open(p, "rb") as f:
        sample = f.read(1 << 16)
    if b"\x00" in sample:
        raise Rejected(f"{p.name}: binary content in a text file")
    sample.decode("utf-8", "replace")


def check_dta(p: Path) -> None:
    h = head_bytes(p, 11)
    # Stata 13+ starts with "<stata_dta>"; older formats start with a version byte 0x66-0x73.
    if not (h.startswith(b"<stata_dta>") or h[0] in range(0x66, 0x74)):
        raise Rejected(f"{p.name}: not a Stata file")


def check_gz(p: Path) -> None:
    if head_bytes(p, 2) != b"\x1f\x8b":
        raise Rejected(f"{p.name}: not gzip")


def safe_extract(p: Path, outdir: Path) -> list[str]:
    """List first; reject the whole archive on any bad member; then extract data files only."""
    if not zipfile.is_zipfile(p):
        raise Rejected(f"{p.name}: not a zip")
    kept, skipped = [], []
    with zipfile.ZipFile(p) as z:
        infos = z.infolist()
        total = 0
        for i in infos:
            name = i.filename
            mode = i.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise Rejected(f"{p.name}: symlink member {name}")
            pp = Path(name)
            if pp.is_absolute() or ".." in pp.parts or name.startswith(("/", "\\")):
                raise Rejected(f"{p.name}: path escape {name}")
            if pp.suffix.lower() in FORBIDDEN_EXT:
                raise Rejected(f"{p.name}: forbidden member {name}")
            total += i.file_size
            if i.compress_size and i.file_size / i.compress_size > MAX_RATIO and i.file_size > 2**20:
                raise Rejected(f"{p.name}: compression ratio of {name} too high")
        if total > MAX_UNCOMPRESSED:
            raise Rejected(f"{p.name}: {total} bytes uncompressed")
        for i in infos:
            if i.is_dir():
                continue
            if Path(i.filename).suffix.lower() not in DATA_EXT or i.filename.startswith("__MACOSX/") \
                    or Path(i.filename).name.startswith("._"):
                skipped.append(i.filename)
                continue
            target = (outdir / i.filename).resolve()
            if outdir.resolve() not in target.parents:
                raise Rejected(f"{p.name}: path escape {i.filename}")
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(i) as src, open(target, "wb") as dst:
                while chunk := src.read(1 << 20):
                    dst.write(chunk)
            no_exec_magic(target)
            if target.suffix.lower() == ".xlsx":
                check_xlsx(target)
            kept.append(i.filename)
    if skipped:
        print(f"    not extracted (not a data extension): {skipped}")
    return kept


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    return h.hexdigest()


def fetch(key: str, force: bool) -> dict:
    d = RAW / key
    if d.exists() and any(d.iterdir()) and not force:
        print(f"[skip] {key}: {d} is not empty")
        return {}
    d.mkdir(parents=True, exist_ok=True)
    rec = {"key": key, "date": dt.date.today().isoformat(), "files": []}
    for url, fname, kind in SOURCES[key]:
        dest = d / fname
        print(f"[get ] {key}: {fname}")
        hops = download(url, dest)
        try:
            if kind == "xlsx":
                check_xlsx(dest)
            elif kind in ("csv", "text"):
                check_text(dest)
            elif kind == "dta":
                check_dta(dest)
            elif kind == "tsvgz":
                check_gz(dest)
            elif kind == "zip":
                extracted = safe_extract(dest, d / (dest.stem + "_extracted"))
                print(f"    extracted {len(extracted)} data files")
        except Rejected:
            dest.unlink()          # one named file: the download just made
            raise
        rec["files"].append({"name": fname, "url": url, "hops": hops,
                             "bytes": dest.stat().st_size, "sha256": sha256(dest)})
    return rec


def write_manifest(recs: list[dict]) -> None:
    mj = ROOT / "data" / "MANIFEST.json"
    old = json.loads(mj.read_text()) if mj.exists() else {}
    for r in recs:
        if r:
            old[r["key"]] = r
    mj.write_text(json.dumps(old, indent=1, sort_keys=True) + "\n")
    lines = ["# data/raw manifest (written by tools/fetch_data.py)", "",
             "Approved by the user 2026-11-20; licences in sources/DATA_SOURCES_TO_APPROVE.md.", "",
             "| Key | File | Bytes | sha256 | Downloaded | URL |", "|---|---|---:|---|---|---|"]
    for k in sorted(old):
        for f in old[k]["files"]:
            lines.append(f"| {k} | {f['name']} | {f['bytes']:,} | `{f['sha256'][:16]}…` | "
                         f"{old[k]['date']} | {f['url'].split('?X-Amz')[0]} |")
    (ROOT / "data" / "MANIFEST.md").write_text("\n".join(lines) + "\n")


def main(argv: list[str]) -> int:
    force = "--force" in argv
    keys = [a for a in argv if not a.startswith("--")] or list(SOURCES)
    recs, bad = [], []
    for k in keys:
        if k not in SOURCES:
            print(f"unknown source {k}")
            return 2
        try:
            recs.append(fetch(k, force))
        except (Rejected, OSError, http.client.HTTPException) as e:
            print(f"[FAIL] {k}: {e}")
            bad.append(k)
    write_manifest(recs)
    print("rejected or failed:", bad or "none")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
