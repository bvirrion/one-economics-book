"""Exercise 11: a price cap over five years. The regulated price starts at 100 and may
rise each year by inflation (2 %) less X (3 %). Unit cost starts at 90 and falls 4 % a
year in nominal terms. Output is 1,000 units a year throughout. The script prints the
price, unit cost and profit each year, then the same under rate-of-return pricing,
where the price is reset each year to cost plus 10."""
price, cost = 100.0, 90.0
for year in range(1, 6):
    price *= 1 + 0.02 - 0.03
    cost *= 1 - 0.04
    print(f"year {year}: cap price {price:6.2f}, unit cost {cost:6.2f}, "
          f"profit {1000 * (price - cost):8.0f}")
print(f"rate of return, year 5: price {cost + 10:6.2f}, profit {1000 * 10:8.0f}")
