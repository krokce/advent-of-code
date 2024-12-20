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

def man_dist(p1, p2):
	return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

path = solve(start)
base_time = len(path)

def find_cheats(position, cheat_duration):
	ret = []
	for sx in range(max(0, position[0]-cheat_duration-1),  min(x_max, position[0]+cheat_duration+1)):
		for sy in range(max(0, position[1]-cheat_duration-1),  min(y_max, position[1]+cheat_duration+1)):
			if (sx, sy) in V and man_dist(position, (sx,sy)) <= cheat_duration:
				ret.append((sx,sy))
	# return [k for k in V.keys() if man_dist(position, k) <= cheat_duration]
	return ret

time_saves = []
for position in path:
	cheats = find_cheats(position, 20)
	for c in cheats:
		time_save = V[position] - man_dist(position, c) - V[c]
		if time_save >= 100:
			time_saves.append(time_save)

print(len([t for t in time_saves if t >= 100]))