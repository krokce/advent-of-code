import math 
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
	lines = [list(map(int, line.strip().split(","))) for line in file.readlines()]


def get_euclidian_distance(p, q):
	return math.sqrt(pow(p[0]-q[0], 2) + pow(p[1]-q[1], 2) + pow(p[2]-q[2], 2))

M = []
C = []

for i in range(len(lines)):
	C.append({i})
	for j in range(i+1, len(lines)):
		M.append((get_euclidian_distance(lines[i], lines[j]), i, j))

def get_group_id(box_id):
	for connect_group_id, connected_group_set in enumerate(C):
		if box_id in connected_group_set:
			return connect_group_id

def merge_groups(g1, g2):
	if g1 != g2:
		C[g1] = C[g1] | C[g2]
		C.pop(g2)

for cnt, (distance, p, q) in enumerate(sorted(M)):
	merge_groups(get_group_id(p), get_group_id(q))
	
	# 1
	if cnt == 1000:
		print(reduce(mul, sorted([len(i) for i in C])[-3:]))
	
	# 2
	if len(C) == 1:
		print(lines[q][0] * lines[p][0])
		break