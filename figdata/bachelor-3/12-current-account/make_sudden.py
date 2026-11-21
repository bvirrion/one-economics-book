"""Chart 3: current-account balance (percent of GDP, WDI BN.CAB.XOKA.GD.ZS) from three
years before to three years after a sudden stop: Mexico 1994, Thailand 1997, Greece
2010. Writes out/sudden.csv (k = year minus stop year, one column per country)."""
import pandas as pd
from econdata import wdi
from figout import write_table

EPISODES = {"MEX": 1994, "THA": 1997, "GRC": 2010}


def table():
    out = pd.DataFrame({"k": range(-3, 4)})
    for iso, y in EPISODES.items():
        d = wdi("BN.CAB.XOKA.GD.ZS", isos=[iso], since=y - 3, until=y + 3)
        out[iso] = d.sort_values("year").value.to_numpy()
    return out


if __name__ == "__main__":
    write_table(table(), __file__, "sudden")
