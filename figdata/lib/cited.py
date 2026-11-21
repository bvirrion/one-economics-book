"""Charts of published numbers: a small table whose every row is a ledger fact.

    from cited import load_cited
    d = load_cited(__file__, "estimates")      # reads src/estimates.csv beside the script

The table lives at figdata/<year>/NN-<slug>/src/<name>.csv. It is typed by hand from a
published TABLE or text (a paper's table, an agency's published table), never read off
a figure. It has a column `ledger` holding one ledger id per row; every other numeric
cell of the row must appear, exactly as written, among the numbers of that ledger row's
`value` cell (sources/data_ledger.md, sources/ledger/book<N>.md). So a chart of cited
numbers can only show what the ledger records, with its source and access date.

Checked here, on every load (so tools/figdata.sh checks it):
  - every id exists in a ledger file;
  - every numeric cell is one of the numbers of its row's value cell;
  - the ledger row does not say the value was read off a figure.
The chart's source line names the studies (author, year); the Data Credits page is not
involved. The returned frame keeps the `ledger` column; drop it before write_table().
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
NUM = re.compile(r"[-−–]?\d[\d   ,]*(?:\.\d+)?")


def _norm(x: str) -> str:
    x = x.replace("−", "-").replace("–", "-")
    x = re.sub(r"[   ,]", "", x)
    try:
        return repr(float(x))
    except ValueError:
        return x


@lru_cache(maxsize=None)
def ledger_rows() -> dict[str, list[str]]:
    rows = {}
    files = [ROOT / "sources" / "data_ledger.md", *sorted((ROOT / "sources" / "ledger").glob("*.md"))]
    for f in files:
        section = None
        for line in f.read_text(encoding="utf8").splitlines():
            if line.startswith("## "):
                section = line[3:].strip().lower()
            elif section == "rows" and line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if cells and ":" in cells[0] and not set(cells[0]) <= set("-"):
                    rows[cells[0]] = cells
    return rows


def load_cited(script: str, name: str) -> pd.DataFrame:
    p = Path(script).resolve().parent / "src" / f"{name}.csv"
    d = pd.read_csv(p, dtype=str, keep_default_na=False)
    if "ledger" not in d.columns:
        raise ValueError(f"{p}: no `ledger` column")
    rows = ledger_rows()
    errors = []
    for i, r in d.iterrows():
        rid = r["ledger"].strip()
        if rid not in rows:
            errors.append(f"row {i + 2}: ledger id {rid!r} has no row")
            continue
        cells = rows[rid]
        if len(cells) < 6:
            errors.append(f"row {i + 2}: ledger row {rid} is malformed")
            continue
        if re.search(r"read off|read from (?:a|the) (?:figure|chart|graph)", " ".join(cells), re.I):
            errors.append(f"row {i + 2}: {rid} was read off a figure (not allowed)")
        allowed = {_norm(m.group(0)) for m in NUM.finditer(cells[2])}
        for c in d.columns:
            if c == "ledger":
                continue
            v = r[c].strip()
            if v and NUM.fullmatch(v) and _norm(v) not in allowed:
                errors.append(f"row {i + 2}: {c}={v} is not in the value cell of {rid} ({cells[2]!r})")
    if errors:
        raise ValueError(f"{p}:\n  " + "\n  ".join(errors))
    for c in d.columns:
        if c != "ledger":
            conv = pd.to_numeric(d[c], errors="coerce")
            if conv.notna().all():
                d[c] = conv
    return d
