import re
from itertools import product

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

for t in range(1000):

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

#1
print(sum([sum(map(abs, p[i])) * sum(map(abs, v[i])) for i in range(len(p))]))