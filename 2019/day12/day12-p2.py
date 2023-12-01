import re
from itertools import product
import math

with open('day12.txt', 'r') as file:
    p = [list(map(int, re.findall("[\d|-]+", l.strip()))) for l in file.readlines()]

v = [[0 for x in range(3)] for y in range(len(p))]

def get_deltas(p1, p2):
    ret = [0,0,0]
    for i in range(3):
        if p2[i] > p1[i]:
            ret[i] = 1
        elif p2[i] < p1[i]:
            ret[i] = -1
        else:
            ret[i] = 0
    return tuple(ret)

D = {}
t = 0
found = [0, 0, 0]

while True:

    # hash each position and velocity x, y, z components
    key = [[0],[1],[2]]
    for i in range(len(p)):
        for j in range(3): 
            key[j].append(p[i][j])
            key[j].append(v[i][j])

    # find where each x, y, z start repeating
    for k in range(3):
        if not found[k] and (k, tuple(key[k])) in D:
            print(t, k, key[k])
            found[k] = t
        elif not found[k]:
            D[(k, tuple(key[k]))] = t
    if found.count(0) == 0:
        break

    # Update position and velocity
    for p1, p2 in [(p1,p2) for p1, p2 in product(enumerate(p), enumerate(p)) if p1 != p2]:
        dx, dy, dz = get_deltas(p1[1], p2[1])
        v[p1[0]][0] += dx
        v[p1[0]][1] += dy
        v[p1[0]][2] += dz

    for i in range(len(p)):
        p[i][0] += v[i][0]
        p[i][1] += v[i][1]
        p[i][2] += v[i][2]
    
    t += 1

#2 
print(math.lcm(*found))