with open('day10.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

directions = [
	(0, 1), 	# 0 - up 
	(1, 0), 	# 1 - right
	(0, -1), 	# 2 - down
	(-1, 0)		# 3 - left
]

from_pipe = {
	'S': [0, 1, 2, 3],
	'|': [0, 2],
	'-': [1, 3],
	'F': [2, 1],
	'L': [0, 1],
	'7': [3, 2],
	'J': [3, 0]
}

to_pipe = {
	'S': [0, 1, 2, 3],
	'|': [0, 2],
	'-': [1, 3],
	'F': [0, 3],
	'L': [2, 3],
	'7': [1, 0],
	'J': [1, 2]
}

M = {} 	# map
V = {}	# visited

p = None
for y, l in enumerate(lines):
	for x, pipe in enumerate(l):
		M[(x, len(lines)-y-1)] = pipe
		if pipe == 'S':
			p = (x, len(lines)-y-1)

def is_possible(from_p, to_p):
	dx = to_p[0] - from_p[0]
	dy = to_p[1] - from_p[1]
	for i in to_pipe[M[to_p]]:
		if (dx, dy) == directions[i]:
			return True
	return False

V[p] = 0
distance = 0
while True:
	distance += 1
	for d_from in from_pipe[M[p]]:
		dx, dy = directions[d_from]
		to_p = (p[0]+dx, p[1]+dy)
		if to_p in M and M[to_p] != '.' and to_p not in V and is_possible(p, to_p):
			V[to_p] = distance
			p = to_p
			break
		# back to start
		if to_p in V and M[to_p] == 'S' and distance>2:
			break
	if M[to_p] == 'S':
		break

#1
print(distance//2)

HIN = set()
VIN = set()

# horizontal
for y in range(len(lines)):
	is_in = 0
	for x in range(len(lines[0])):
		if (x,y) in V and M[(x,y)] in '|':
			is_in += 1
		if (x,y) in V and M[(x,y)] in 'FJ':
			is_in += 0.5	
		if (x,y) in V and M[(x,y)] in 'L7':
			is_in += 1.5	
		if (x,y) not in V and is_in%2 == 1:
			HIN.add((x,y))

# vertical
for x in range(len(lines[0])):
	is_in = 0
	for y in range(len(lines)):
		if (x,y) in V and M[(x,y)] in '-':
			is_in += 1
		if (x,y) in V and M[(x,y)] in 'L7':
			is_in += 0.5
		if (x,y) in V and M[(x,y)] in 'FJ':
			is_in += 1.5
		if (x,y) not in V and is_in%2 == 1:
			VIN.add((x,y))

#2
print(len(HIN | VIN))