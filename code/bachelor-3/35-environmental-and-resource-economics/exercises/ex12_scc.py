"""Exercise 12: the social cost of a tonne of CO2 emitted today. The tonne causes
damage of 1.5 dollars in year 1, growing 2 % a year, for 300 years. Its present value at
three constant discount rates, and with a rate that falls from 3 % to 1.5 % over the
first century and stays there."""
import numpy as np

t = np.arange(1, 301)
damage = 1.5 * 1.02 ** (t - 1)
for r in (0.014, 0.03, 0.05):
    print(f"constant {100 * r:.1f} %: {np.sum(damage / (1 + r) ** t):7.1f} dollars")
rate = np.where(t <= 100, 0.03 - 0.015 * (t - 1) / 99, 0.015)
factor = np.cumprod(1 / (1 + rate))
print(f"declining 3 % to 1.5 %: {np.sum(damage * factor):7.1f} dollars")
