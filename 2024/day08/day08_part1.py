from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()
R = defaultdict()
max_row = len(lines)
max_col = len(lines[0])

for row in range(len(lines)):
	for col in range(len(lines[row])):
		if lines[row][col] != '.':
			M[(row, col)] = lines[row][col] 

for node1, freq1 in M.items():
	for node2, freq2 in M.items():
		if node1 != node2 and freq1 == freq2:
			dr = node2[0] - node1[0]
			dc = node2[1] - node1[1]
			R[(node1[0]-dr, node1[1]-dc)] = '#'
			R[(node2[0]+dr, node2[1]+dc)] = '#'

print(len([k for k in R.keys() if 0<=k[0]<max_row and 0<=k[1]<max_col]))