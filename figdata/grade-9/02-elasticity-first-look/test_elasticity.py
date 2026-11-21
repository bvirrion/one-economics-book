import re
from pathlib import Path

from make_elasticity import LEDGER, revenue

LEDGER_FILE = Path(__file__).resolve().parents[3] / "sources" / "ledger" / "book1.md"


def test_values_match_ledger():
    text = LEDGER_FILE.read_text()
    for good, (rid, v, _) in LEDGER.items():
        m = re.search(r"^\| " + re.escape(rid) + r" \|[^|]*\| ([^|]+) \|", text, re.M)
        assert m, rid
        assert abs(abs(float(m.group(1).strip())) - v) < 1e-9, (rid, m.group(1))


def test_revenue_peak():
    r = revenue().set_index("price")
    assert r.revenue.idxmax() == 6 and r.revenue[6] == 3600
