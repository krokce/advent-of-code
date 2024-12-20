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

# print(M)
# print(moves)

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

def move(position, move):
	dx, dy = D[DP.index(move)]
	new_position = (position[0]+dx, position[1]+dy)
	boxes_to_move = []
	if new_position not in M or M[new_position] == "#":
		return position
	if M[new_position] == "O":
		scan_position = new_position
		while True:
			scan_position = (scan_position[0]+dx, scan_position[1]+dy)
			if M[scan_position] == ".":
				M[scan_position] = "O"
				M[new_position] = "."
				return new_position
			elif scan_position not in M or M[scan_position] == "#":
				return position
			else:
				continue
	return new_position
	
print_maze()
