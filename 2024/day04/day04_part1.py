from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()

for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col] 

directions = [1, 0, -1]

def get_count(position, direction):
	if direction == (0, 0):
		return 0
	ret = ''
	for i in range(len('XMAS')):
		if (position[0]+i*direction[0], position[1]+i*direction[1]) not in M:
			return 0
		ret = ret + M[(position[0]+i*direction[0], position[1]+i*direction[1])]
	if ret == 'XMAS':
		return 1
	return 0

ret = 0
for position in M.keys():
	for direction_x in directions: 
		for direction_y in directions:
			ret = ret + get_count(position, (direction_x, direction_y))

print(ret)