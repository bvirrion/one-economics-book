"""Opening chart: Japan's net trade of 1868--75 valued at its autarky prices of 1851--53
(Bernhofen and Brown 2004, Table 2; cited numbers, ledger b3rt:bb04.t2.<year>).
Imports (three components) and exports (two) are summed here (our arithmetic on the
printed components); the total is the paper's printed inner product.
Writes out/japan.csv (year, imports, exports, total, sum_components)."""
import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "japan").drop(columns="ledger").astype(float)
    imp = (d.obs_imports + d.wool_imports + d.approx_imports).round(2)
    exp = (d.obs_exports + d.approx_exports).round(2)
    return pd.DataFrame({"year": d.year.astype(int), "imports": imp, "exports": exp,
                         "total": d.total, "sum_components": (imp + exp).round(2)})


if __name__ == "__main__":
    write_table(table(), __file__, "japan")
