import re
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

x_max = 101
y_max = 103

def position(t):
	M = defaultdict(int)
	for l in lines:
		px, py, vx, vy = list(map(int, re.findall(r'-?\d+', l)))
		px1 = (px+vx*t)%x_max
		py1 = (py+vy*t)%y_max
		M[(px1, py1)] = M[(px1, py1)] + 1
	return M

def print_map(M):
	for x in range(x_max):
		for y in range(y_max):
			print('#' if (x,y) in M else '.', end='')
		print()

directions = [(0,1), (1,0), (-1,0), (0,-1)]

def area(point, M, G):
	for d in directions:
		next_point = (point[0]+d[0], point[1]+d[1])
		if next_point in M and next_point not in G:
			G.append(next_point)
			area(next_point, M, G)
	return G

def count_areas(M):
	done = []
	areas = {}
	for p in M.keys():
		if p not in done:
			areas[p] = area(p, M, [p])
			done = done + areas[p]
		if len(areas) > 150:
			return False
	return True

t = 1
while True:
	m = position(t)
	print(t)
	if count_areas(m):
		break
	t = t + 1

print_map(m)
print(t)