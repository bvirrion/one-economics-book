"""World population and its regional shares, 1820-2022 (Maddison's own regional estimates).

Writes
  out/world_population.csv  year, pop_bn (billions), for the 21 years with a World row;
  out/population_shares.csv  label, then one column per Maddison region (percent of the
                             World row), for five years where all eight regions have an
                             estimate (1820, 1870, 1950, 1990, 2022).
Grade 6, chapter 1, charts 1 and 2.
"""
from econdata import REGIONS, maddison_regions
from figout import write_table

COLS = {
    "East Asia": "east_asia",
    "South and South East Asia": "south_se_asia",
    "Middle East and North Africa": "mena",
    "Sub Saharan Africa": "ssa",
    "Western Europe": "western_europe",
    "Eastern Europe": "eastern_europe",
    "Western Offshoots": "western_offshoots",
    "Latin America": "latin_america",
}
BAR_YEARS = [1820, 1870, 1950, 1990, 2022]


def tables():
    d = maddison_regions()
    p = d.pivot(index="year", columns="region", values="pop")
    world = p["World"].dropna()
    pop = (world / 1e6).round(3).rename("pop_bn").reset_index()
    shares = p.loc[BAR_YEARS, list(COLS)].div(p.loc[BAR_YEARS, "World"], axis=0).mul(100).round(1)
    shares = shares.rename(columns=COLS).reset_index()
    return pop, shares


if __name__ == "__main__":
    pop, shares = tables()
    write_table(pop, __file__, "world_population")
    write_table(shares, __file__, "population_shares")
