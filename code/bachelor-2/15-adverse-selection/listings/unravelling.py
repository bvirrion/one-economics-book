"""An insurance market that unravels, step by step.

Buyers are ranked by willingness to pay; the q-th has willingness to pay
900 - 500 q and expected cost 800 - 600 q (dalens a year), so those who value
cover most also cost most. Each year the insurer charges the average cost of
last year's buyers, and everyone whose willingness to pay covers it buys.
"""


def willing(price):
    return min(max((900 - price) / 500, 0.0), 1.0)  # share who buy


def average_cost(share):
    return 800 - 300 * share  # mean of 800 - 600 q over [0, share]


price = average_cost(1.0)  # start as if everyone buys
for year in range(1, 9):
    share = willing(price)
    print(f"year {year}: premium {price:6.1f}, share insured {share:.3f}")
    price = average_cost(share)
q_star = (900 - 800) / (500 - 300)  # where demand meets average cost
print(f"equilibrium: premium {average_cost(q_star):.1f}, share insured {q_star:.3f}")
lost = sum((100 + 100 * (0.5 + (i + 0.5) / 2000)) / 2000 for i in range(1000))
print(f"welfare lost per person {lost:.2f} dalens a year")
