import heapq 
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [tuple(map(int, l.strip().split(","))) for l in file.readlines()]

start = (0,0)
# end = (6,6)
end = (70,70)
# size = 12
size = 1024

D = [(0,1), (0,-1), (-1,0), (1,0)]

def print_maze(steps):
	for y in range(end[1]+1):
		for x in range(end[0]+1):
			if (x, y) in steps:
				print('*', end='')
			else:
				print(M[(x,y)], end='')
		print()
	print()

M = {}

for y in range(end[1]+1):
	for x in range(end[0]+1):
		M[(x,y)] = '.'

for b in lines[0:size]:
	M[b] = '#'

V = set()
Q = []
heapq.heappush(Q, (0, start, [start]))

while True:
	distance, position, steps = heapq.heappop(Q)

	if (position) in V:
		continue

	V.add(position)

	if position == end:
		print_maze(steps)
		# print(steps)
		print(distance)
		break

	for next_direction_id, next_direction in enumerate(D):
		next_x, next_y = position[0] + next_direction[0], position[1] + next_direction[1]
		add_distance = 1 

		# not allowed to step out of the maze
		if (next_x, next_y) not in M:
			continue
		# not allowed to step in the wall
		if M[(next_x, next_y)] == "#":
			continue

		heapq.heappush(Q, (distance + 1, (next_x, next_y), steps + [(next_x, next_y)]))