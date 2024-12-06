from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()

for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col] 

directions1 = [(-1,-1), (0, 0), (1, 1)]
directions2 = [(-1, 1), (0, 0), (1, -1)]

def get_count(position):
	ret = ''
	if M[position] != 'A':
		return 0
	for direction in directions1:
		if (position[0]+direction[0], position[1]+direction[1]) not in M:
			return 0
		ret = ret + M[(position[0]+direction[0], position[1]+direction[1])]
	if ret not in ['MAS', 'SAM']:
		return 0
	
	ret = ''
	for direction in directions2:
		if (position[0]+direction[0], position[1]+direction[1]) not in M:
			return 0
		ret = ret + M[(position[0]+direction[0], position[1]+direction[1])]
	if ret not in ['MAS', 'SAM']:
		return 0
	return 1

ret = 0
for position in M.keys():
	ret = ret + get_count(position)

print(ret)