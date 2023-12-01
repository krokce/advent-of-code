from collections import defaultdict
from copy import deepcopy
import math 

with open('day14.txt', 'r') as file:
  i = [l.strip().split(" => ") for l in file.readlines()]

R = {}

for r in i:
    q, e = r[1].split()
    R[e] = (int(q), [])
    for req in r[0].split(", "):
        rq, re = req.split()
        R[e][1].append((int(rq), re))

I = defaultdict(int)

def ore_cost(quantity, item):

    # done if ORE
    if item == "ORE":
        return quantity
    # we have it in inventory
    elif I[item] >= quantity:
        I[item] -= quantity
        return 0
    # recursive call based on recipe
    else:
        pq, ri = R[item]
        prod_multiplier = math.ceil((quantity - I[item])/pq)
        I[item] += prod_multiplier * pq - quantity
        return sum([ore_cost(prod_multiplier * req_quantity, req_item) for req_quantity, req_item in ri])

#1
print(ore_cost(1, "FUEL"))

#2
fuel = 1
ore = 1000000000000
while True:
    I = defaultdict(int)
    cost = ore_cost(fuel, "FUEL")
    new_fuel = int(ore / (cost / fuel))

    if new_fuel == fuel:
        print(fuel)
        break

    fuel = new_fuel