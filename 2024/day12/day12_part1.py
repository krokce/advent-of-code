from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()

max_row = len(lines)
max_col = len(lines[0])

for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col] 

directions = [(0,1), (1,0), (-1,0), (0,-1)]

def garden(plot, type, G):
	for d in directions:
		next_plot = (plot[0]+d[0], plot[1]+d[1])
		if next_plot in M and M[next_plot] == type and next_plot not in G:
			G.append(next_plot)
			garden(next_plot, type, G)
	return G

def fence(type):
	ret = 0
	for p in gardens[type]:
		for d in directions:
			if (p[0]+d[0], p[1]+d[1]) not in gardens[type]:
				ret = ret + 1
	return ret

done = []
gardens = {}
for p in M.keys():
	if p not in done:
		gardens[p] = garden(p, M[p], [p])
		done = done + gardens[p]

ret = 0
for g in gardens.keys():
	ret = ret + len([p for p in gardens[g]]) * fence(g)

print(ret)