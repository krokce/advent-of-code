import heapq 

with open('day17.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

def print_city(steps):
	for row in range(max_row):
		for col in range(max_col):
			if (row, col) in steps:
				print('*', end='')
			else:
				print(C[(row, col)], end='')
		print()
	print()

max_row = len(lines)
max_col = len(lines[0])

C = {}
for row in range(max_row):
	for col in range(max_col):
		C[(row, col)] = int(lines[row][col])

# E, W, N, S
D = [(0,1), (0,-1), (-1,0), (1,0)]

V = set()
Q = []

# Start search both towards East (0) and South (3)
heapq.heappush(Q, (0, [(0,0)], 0, 1, 0, 0))
heapq.heappush(Q, (0, [(0,0)], 3, 1, 0, 0))

while True:
	loss, steps, direction, blocks, row, col = heapq.heappop(Q)

	if (row, col, direction, blocks) in V:
		continue
	V.add((row, col, direction, blocks))

	if (row, col) == (max_row-1, max_col-1) and blocks >= 4:
		print_city(steps)
		print(loss)
		break

	for next_direction_id, next_direction in enumerate(D):
		next_row, next_col = row + next_direction[0], col + next_direction[1]
		next_blocks = blocks + 1 if next_direction_id == direction else 1

		# step out of the city
		if (next_row, next_col) not in C:
			continue
		# not alowed more than 10 steps in same direction
		if next_blocks > 10:
			continue
		# must go at least 4 steps before changing direction
		if blocks < 4 and direction != next_direction_id:
			continue
		# not alowed back
		if (direction, next_direction_id) in [(0,1), (1,0), (2,3), (3,2)]:
			continue 

		heapq.heappush(Q, (loss + C[(next_row, next_col)], steps + [(next_row, next_col)], next_direction_id, next_blocks, next_row, next_col))