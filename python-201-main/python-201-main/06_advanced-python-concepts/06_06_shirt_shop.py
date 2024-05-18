# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# listcomp = [(a, b) for a in sizes for b in colors]
# print(listcomp)

# using itertools.product()
from itertools import product

listcomp = list(product(sizes, colors))
print(listcomp)