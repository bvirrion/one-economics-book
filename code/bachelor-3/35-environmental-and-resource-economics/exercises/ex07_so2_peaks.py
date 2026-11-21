"""Exercise 7: the peak of sulphur dioxide emissions per person, 1850--2019, for
France, Italy and Spain (CEDS emissions; Maddison Project population and GDP per
person, 2011 dollars): the year, the level and income per person at the peak, and
the level in 2019."""
from econdata import ceds, maddison

for iso, name in [("FRA", "France"), ("ITA", "Italy"), ("ESP", "Spain")]:
    s = ceds("so2", isos=[iso], since=1850, until=2019)[["year", "value"]]
    m = maddison(isos=[iso], since=1850, until=2019)[["year", "gdppc", "pop"]]
    d = s.merge(m, on="year").dropna().set_index("year")
    kg = 1000 * d.value / d["pop"]
    t = kg.idxmax()
    print(f"{name:6s} peak {t}: {kg[t]:5.1f} kg per person at "
          f"{d.gdppc[t]:7,.0f} dollars; 2019: {kg[2019]:4.1f} kg")
