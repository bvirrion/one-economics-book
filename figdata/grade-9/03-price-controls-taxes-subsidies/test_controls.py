import re
from pathlib import Path

from make_controls import LEDGER, equilibrium

LEDGER_FILE = Path(__file__).resolve().parents[3] / "sources" / "ledger" / "book1.md"


def test_ledger_rows_exist():
    text = LEDGER_FILE.read_text()
    for rid, v in LEDGER.values():
        m = re.search(r"^\| " + re.escape(rid) + r" \|[^|]*\| ([^|]+) \|", text, re.M)
        assert m, rid
        assert re.sub(r"[^0-9.]", "", m.group(1)) == f"{abs(v):g}"


def test_tax_split():
    p0, _ = equilibrium(120, 4, 20, 6)
    pb, q = equilibrium(120, 4, -10, 6)
    assert (p0, pb, q) == (10, 13, 68) and pb - 5 == 8
