# Brenland and Kestria: the series' invented economies

Exercises with invented data use these two countries, so that their numbers are clean, consistent from chapter to chapter, and
owned by the series. Real countries carry real data from `data/derived/`, and the two are never mixed in one table.

- **Brenland** is a small open economy. Its currency is the **dalen** (`\dal{120}` prints "120 dalens"). Its capital is
  Brenmoor, the town of the computer science series.
- **Kestria** is its trading neighbour. Its currency is the **kest** (`\kst{80}`).

`python -m country` (run from `code/shared/`, or `make country`) rewrites `data/country/*.csv` from the seed. The tests check
that the files are unchanged, that every identity holds exactly, and that the ranges are plausible. **This package is frozen
from the sync on.** Report a defect; never edit it.

## Tables (`data/country/`)

| File | One row per | Columns |
|---|---|---|
| `accounts.csv` | year 2000–2025 | `year`, `pop` (thousands), `labour_force`, `employed` (thousands), `unemp_rate` (%), `real_gdp` (millions of 2015 dalens), `gdp` (millions of dalens, current), `deflator` (2015 = 100), `C`, `I`, `G`, `X`, `M` (millions, current; `gdp = C + I + G + X - M` exactly), `cpi` (2015 = 100), `policy_rate` (%), `revenue`, `spending`, `deficit`, `debt` (millions, current; `deficit = spending - revenue`, `debt` = last year's `debt` + `deficit`) |
| `basket.csv` | year × good | `year`, `good`, `qty_2015` (the 2015 basket, units per household per year), `price` (dalens per unit); the CPI in `accounts.csv` is the Laspeyres index of this basket, 2015 = 100, rounded to 0.1 |
| `households.csv` | household, survey of 2025 (2,000 rows) | `hh`, `size`, `age_head`, `school_years`, `hours` (per year, the head), `gross_income`, `tax`, `transfers`, `disposable` (= gross − tax + transfers), `food`, `consumption` (dalens per year), `owner` (0/1) |
| `firms.csv` | firm, census of 2025 (500 rows) | `firm`, `sector` (farming, manufacturing, services), `workers`, `capital`, `output`, `wage_bill`, `other_costs`, `profit` (= output − wage_bill − other_costs) (thousands of dalens) |
| `ricardo.csv` | country × good | `country`, `good` (cloth, grain), `hours_per_unit`: Brenland has the absolute advantage in both goods and the comparative advantage in grain |
| `trade.csv` | year | `year`, `exports_to_kestria`, `imports_from_kestria` (millions of dalens), `rate` (dalens per kest) |

The tax schedule of the household survey is written out in `country/__init__.py` (`TAX_BANDS`), so that a tax chapter can
print the same schedule.

## Conventions fixed after the package was frozen (documentation only, 2026-11-20)

- **Kestria's income per person.** The package has no Kestria GDP or population. Book 1 (g8-02, g8-04, g9-05) fixes it
  at **30,000 kests in 2025**, which is about **27,700 dalens of 2015**: 30,000 × 1.242 (the package's 2025 rate) ÷ 1.345
  (Brenland's 2025 deflator, 2015 = 1). Book 1's g8-04 chart takes it back to 2000 at 4 % a year. Any later chapter that
  states Kestria's income uses these values, or states none.
- **The CPI basket** (`basket.csv`) has five goods, so rent weighs far more than in a real index. Say so wherever the
  basket's weights are shown.
- **Kestria's consumer prices.** The package has no Kestria CPI. Book 2 g12-14 generates one in its figdata script
  (seeded, 2.5 % ± 0.8 % a year), which gives the dalen a 1.7 % real appreciation against the kest over its window. Later
  chapters that need Kestria's prices reuse that table, or state none.
