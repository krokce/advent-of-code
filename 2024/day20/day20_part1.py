import heapq 
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(l.strip()) for l in file.readlines()]

M = {}
for y, l in enumerate(lines):
	for x, c in enumerate(lines[y]):
		M[(x,y)] = c
		if M[(x,y)] == "S":
			start = (x,y)
		if M[(x,y)] == "E":
			end = (x,y)

D = [(0,1), (0,-1), (-1,0), (1,0)]
x_max = max([x for x,y in M.keys()])
y_max = max([y for x,y in M.keys()])

V = {}
def solve(start):
	Q = []
	heapq.heappush(Q, (0, start, [start]))
	
	while Q:
		distance, position, steps = heapq.heappop(Q)

		if (position) in V:
			continue

		V[position] = distance

		if position == end:
			return steps

		for next_direction_id, next_direction in enumerate(D):
			next_x, next_y = position[0] + next_direction[0], position[1] + next_direction[1]

			# not allowed to step in the wall
			if M[(next_x, next_y)] == "#":
				continue

			# not allowed to step out of the maze
			if (next_x, next_y) not in M:
				continue

			heapq.heappush(Q, (distance + 1, (next_x, next_y), steps + [(next_x, next_y)]))
	return []

path = solve(start)
base_time = len(path)

time_saves = []
for position in path:
	for next_direction_id, next_direction in enumerate(D):
		next_x, next_y = position[0] + 2*next_direction[0], position[1] + 2*next_direction[1]
		if (next_x, next_y) in V:
			time_saves.append(V[position] - 2 - V[(next_x, next_y)])

print(len([t for t in time_saves if t >= 100]))