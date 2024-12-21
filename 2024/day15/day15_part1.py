with open('input.txt', 'r') as file:
	lines = [l.strip() for l in file.read().split("\n\n")]

print(lines)

M = {}

for y, l in enumerate(lines[0].split("\n")):
	for x, c in enumerate(l):
		M[(x,y)] = c
		if c == "@":
			robot_position = (x,y)
			M[robot_position] = "."

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
			print(M[(x,y)], end='')
		print()
	print()

def move(position, move):
	dx, dy = D[DP.index(move)]
	new_position = (position[0]+dx, position[1]+dy)
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
for m in moves:
	robot_position = move(robot_position, m)
print_maze()

ret = 0
for (x,y), m in M.items():
	if m == "O":
		ret = ret + x + 100*y

print(ret)