import heapq 
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [l.strip() for l in file.read().split("\n\n")]

# print(lines)

M = {}

box = 0
for y, l in enumerate(lines[0].split("\n")):
	for x, c in enumerate(l):
		x = 2*x
		if c == "@":
			robot_position = (x,y)
			M[(x,y)] = "."
			M[(x+1,y)] = "."
		elif c == "#":
			M[(x,y)] = "#"
			M[(x+1,y)] = "#"
		elif c == "O":
			box = box + 1
			M[(x,y)] = (box, -1)
			M[(x+1,y)] = (box, 1)
		else:
			M[(x,y)] = "."
			M[(x+1,y)] = "."

max_x = max([x for x,y in M.keys()])
max_y = max([y for x,y in M.keys()])

moves = []
for m in lines[1].split("\n"):
	moves = moves + list(m)

D = [(0,1), (0,-1), (-1,0), (1,0)]
DP = list("v^<>")

def print_maze():
	for y in range(max_y+1):
		for x in range(max_x+1):
			m = M[(x,y)]
			if (x,y) == robot_position:
				print('@', end='')
				continue
			if len(m) > 1:
				if m[1] < 0:
					print('[', end='')
				else:
					print(']', end='')
			else:
				print(m, end='')
		print()
	print()

def get_new_position(position, move):
	dx, dy = D[DP.index(move)]
	return (position[0]+dx, position[1]+dy)

def get_connected_blocks(position, move):
	new_position = get_new_position(position, move)
	v = M[new_position]
	ret = []

	if v in list("#."):
		return list(set(ret))
	
	if len(v) > 1 and move in list("v^"): 
		ret.append(new_position)
		# hitting the right - add the left
		if v[1] > 0:
			ret.append((new_position[0]-1,new_position[1]))
		# hitting the left - add the right 
		else:
			ret.append((new_position[0]+1,new_position[1]))
		
		ret = ret + get_connected_blocks(ret[-1], move) + get_connected_blocks(ret[-2], move)
	
	if len(v) > 1 and move in list("<>"):
		ret.append(new_position)
		# hitting the right - add the right
		if v[1] > 0:
			ret.append((new_position[0]-1,new_position[1]))
		# hitting the left - add the right
		else:
			ret.append((new_position[0]+1,new_position[1]))
		ret = ret + get_connected_blocks(ret[-1], move)
	return list(set(ret))

def can_move(blocks, move):
	for b in blocks:
		new_position = get_new_position(b,move)
		if M[new_position] != "." and new_position not in blocks:
			return False
	return True

def move(position, move):
	new_position = get_new_position(position, move)

	if M[new_position] == "#":
		return position
	
	if len(M[new_position]) > 1:
		blocks = get_connected_blocks(position, move)
		if can_move(blocks, move):
			dx, dy = D[DP.index(move)]
			tmp = {}
			for b in blocks:
				tmp[b] = M[b]
				M[b] = "."

			for b in blocks:
				M[(b[0]+dx,b[1]+dy)] = tmp[b]

			return new_position
		else:
			return position
	
	return new_position

print_maze()
for m in moves:
	robot_position = move(robot_position, m)
print_maze()

ret = 0
for (x,y), m in M.items():
	if len(m) > 1 and m[1] < 0:
		ret = ret + x + 100*y

print(ret)