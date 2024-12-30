from collections import defaultdict
from itertools import combinations

with open('input.txt', 'r') as file:
	lines = [l.strip().split("-") for l in file.readlines()]

M = defaultdict(set)

for c1, c2 in lines:
	M[c1].add(c2)
	M[c2].add(c1)

S = set()
for m1 in M.keys():
	for m2 in M[m1]:
		for m3 in M[m2]:
			if m1 in M[m3]:
				S.add(frozenset([m1,m2,m3]))

print(len([e for e in S if any(t.startswith("t") for t in e)]))