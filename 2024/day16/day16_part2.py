import heapq 
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

def print_maze(steps):
	for row in range(max_row):
		for col in range(max_col):
			if (row, col) in steps:
				print('*', end='')
			else:
				print(M[(row, col)], end='')
		print()
	print()

max_row = len(lines)
max_col = len(lines[0])

M = {}
for row in range(max_row):
	for col in range(max_col):
		M[(row, col)] = lines[row][col]
		if M[(row, col)] == "S":
			start = (row, col)
		if M[(row, col)] == "E":
			end = (row, col)

# E, W, N, S
D = [(0,1), (0,-1), (-1,0), (1,0)]

V = defaultdict(lambda: float('inf')) 
P = defaultdict(list)
P[0, start[0], start[1]] = [[start]]
Q = []

# Start search towards East (0)
heapq.heappush(Q, (0, 0, start[0], start[1]))

while Q:
	score, direction, row, col = heapq.heappop(Q)

	for next_direction_id, next_direction in enumerate(D):
		if next_direction_id == direction:
			add_score = 1 
			next_row, next_col = row + next_direction[0], col + next_direction[1]
		else:
			add_score = 1000 
			next_row, next_col = row, col

		# not allowed to step out of the maze
		if (next_row, next_col) not in M:
			continue
		# not allowed to step in the wall
		if M[(next_row, next_col)] == "#":
			continue
		# not allowed back
		if (direction, next_direction_id) in [(0,1), (1,0), (2,3), (3,2)]:
			continue 

		new_score = score + add_score

		if new_score < V[(next_direction_id, next_row, next_col)]:
			V[(next_direction_id, next_row, next_col)] = new_score
			heapq.heappush(Q, (new_score, next_direction_id, next_row, next_col))
			P[(next_direction_id, next_row, next_col)] = [path + [(next_row, next_col)] for path in P[(direction, row, col)]]

		elif new_score == V[(next_direction_id, next_row, next_col)]:
			P[(next_direction_id, next_row, next_col)].extend([path + [(next_row, next_col)] for path in P[(direction, row, col)]])

path_lengths = [V[d, end[0], end[1]] for d in range(4)]
shortest_path = path_lengths.index(min(path_lengths))

res = set()
for path in P[(shortest_path, end[0], end[1])]:
	for e in path:
		res.add(e)

print(len(res))