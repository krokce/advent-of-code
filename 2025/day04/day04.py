from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()
max_row = len(lines)
max_col = len(lines[0])

for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col] 

def get_neighbors_count(row, col):
	neighbors = []
	directions = [-1, 0, 1]
	for dr in directions:
		for dc in directions:
			if dr == 0 and dc == 0:
				continue
			r, c = row + dr, col + dc
			if 0 <= r < max_row and 0 <= c < max_col and M[(r, c)] == '@':
				neighbors.append((r, c))
	return len(neighbors)

def remove_rolls():
	to_remove = set()
	for r, c in M.keys():
		if M[(r, c)] == '@':
			neighbors = get_neighbors_count(r, c)
			if neighbors < 4:
				to_remove.add((r, c))

	for n in to_remove:
		M[n] = 'x'

	return len(to_remove)

ret = 0
while True:
	removed = remove_rolls() 
	if ret == 0:
		# 1 - first removal cycle
		print(removed)
	ret = ret + removed
	if removed == 0:
		break

# 2
print(ret)