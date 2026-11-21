"""Weekend problem: Brenland's tax reform. Writes out/brenland_stats.csv."""
import pandas as pd
from brenland_tax import (ETI, PROJECT_RETURN, THRESHOLD, VAT_MCPF, VAT_RATE,
                          mcpf_upper, pareto_a, tax, upper)
from country import load
from figout import write_table


def stats():
    h = load("households")
    z, rates = upper()
    mech, beh, mcpf = mcpf_upper()
    _, _, mcpf50 = mcpf_upper(0.5)
    a = pareto_a()
    cut = 0.02 * mech  # static loss of cutting every upper rate by 2 points
    offset = 0.02 * beh  # first-order behavioural gain
    net = cut - offset
    cons = h.consumption.sum()
    vat_rise = 100 * net / cons
    rows = {"households": len(h), "n_upper": len(z), "mean_upper": z.mean(),
            "share_upper": 100 * len(z) / len(h), "tax_total": h.tax.sum(),
            "tax_upper_bands": sum(tax(x) - tax(THRESHOLD) for x in z),
            "tax_60000": tax(60_000), "avg_60000": 100 * tax(60_000) / 60_000,
            "tax_25000": tax(25_000), "avg_25000": 100 * tax(25_000) / 25_000,
            "mech_per_point": 0.01 * mech, "beh_per_point": 0.01 * beh,
            "mcpf": mcpf, "meb": mcpf - 1, "mcpf_e50": mcpf50, "pareto_a": a,
            "tau_star": 100 / (1 + a * ETI), "static_cut": cut, "offset": offset,
            "net_loss": net, "consumption": cons, "vat_rise_points": vat_rise,
            "vat_rate": 100 * VAT_RATE, "vat_mcpf": VAT_MCPF,
            "welfare_gain": net * (mcpf - VAT_MCPF), "project_return": PROJECT_RETURN}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


if __name__ == "__main__":
    write_table(stats(), __file__, "brenland_stats")
