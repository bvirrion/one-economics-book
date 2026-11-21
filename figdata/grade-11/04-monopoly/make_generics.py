"""Generic drug prices relative to the brand price, by number of generic producers (cited table).

Grade 11, chapter 4 (monopoly). Conrad and Lutter (2019), FDA, technical appendix: generic-to-brand price ratios for US
drugs with a first generic entry in 2015-2017; average manufacturer price (AMP) quartiles and the invoice-based median;
the last row is 10 or more producers. Typed into src/generics.csv; every number is in its ledger row.
Writes:
  out/generics.csv  producers, amp_p25, amp_median, amp_p75, invoice_median, pct (AMP median as % of brand),
                    err_lo, err_hi (distance from the median to the quartiles, in %)
"""
from cited import load_cited
from figout import write_table


def generics():
    d = load_cited(__file__, "generics").drop(columns="ledger")
    d["pct"] = (100 * d.amp_median).round(1)
    d["err_lo"] = (100 * (d.amp_median - d.amp_p25)).round(1)
    d["err_hi"] = (100 * (d.amp_p75 - d.amp_median)).round(1)
    return d


if __name__ == "__main__":
    write_table(generics(), __file__, "generics")
