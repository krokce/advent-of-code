import heapq 

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

V = set()
Q = []

# Start search towards East (0)
heapq.heappush(Q, (0, [start, 0], 0, start[0], start[1]))

while True:
	loss, steps, direction, row, col = heapq.heappop(Q)

	if (direction, row, col) in V:
		continue

	V.add((direction, row, col))

	if (row, col) == end:
		# print_maze(steps)
		# print(steps)
		print(loss)

		break

	for next_direction_id, next_direction in enumerate(D):
		if next_direction_id == direction:
			add_loss = 1 
			next_row, next_col = row + next_direction[0], col + next_direction[1]
		else:
			add_loss = 1000 
			next_row, next_col = row, col

		# not allowed to step out of the maze
		if (next_row, next_col) not in M:
			continue
		# not allowed to step in the wall
		if M[(next_row, next_col)] == "#":
			continue
		# not alowed back
		if (direction, next_direction_id) in [(0,1), (1,0), (2,3), (3,2)]:
			continue 

		heapq.heappush(Q, (loss + add_loss, steps + [(next_row, next_col), next_direction_id], next_direction_id, next_row, next_col))