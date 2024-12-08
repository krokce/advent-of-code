from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()
R = defaultdict()
max_row = len(lines)
max_col = len(lines[0])

for row in range(max_row):
	for col in range(max_col):
		if lines[row][col] != '.':
			M[(row, col)] = lines[row][col] 

for node1, freq1 in M.items():
	for node2, freq2 in M.items():
		if node1 != node2 and freq1 == freq2:
			dr = node2[0] - node1[0]
			dc = node2[1] - node1[1]
			n1 = node1
			n2 = node2
			R[n1] = '#'
			R[n2] = '#'
			while 0 <= n1[0] < max_row and 0 <= n1[1] < max_col:
				n1 = (n1[0]-dr, n1[1]-dc)
				R[n1] = '#'
			while 0 <= n1[0] < max_row and 0 <= n1[1] < max_col:
				n2 = (n2[0]+dr, n2[1]+dc)
				R[n2] = '#'

print(len([k for k in R.keys() if 0<=k[0]<max_row and 0<=k[1]<max_col]))