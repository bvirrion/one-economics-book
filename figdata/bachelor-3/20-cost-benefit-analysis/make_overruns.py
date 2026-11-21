"""Opening chart: average cost overrun of 258 transport projects by type and region
(Flyvbjerg, Holm and Buhl 2002, Tables 1 and 2; cited numbers). Writes one table
per region, out/overruns_<region>.csv, with x positions 0-3 for the types."""
from cited import load_cited
from figout import write_table

TYPES = ["Rail", "Fixed links", "Roads", "All"]
REGIONS = {"Europe": "europe", "North America": "namerica", "Other": "other",
           "All": "all"}


def tables():
    d = load_cited(__file__, "overruns").drop(columns="ledger")
    d["pos"] = d.type.map({t: i for i, t in enumerate(TYPES)})
    return {k: d[d.region == r][["pos", "type", "n", "mean"]].reset_index(drop=True)
            for r, k in REGIONS.items()}


if __name__ == "__main__":
    for k, t in tables().items():
        write_table(t, __file__, f"overruns_{k}")
