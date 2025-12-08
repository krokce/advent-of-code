from collections import defaultdict
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
	lines = [list(line) for line in file]

positions = []
for i, l in enumerate(lines[len(lines)-1]):
	if l != '\n' and l != ' ':
		positions.append(i)

def get_cpehalophod_number(id):
	from_char = positions[id]
	to_char = positions[id + 1] if id + 1 < len(positions) else len(lines[0])
	ret = []
	for i in range(from_char, to_char-1):
		number = ''
		for line_id in range(len(lines)-1):
			if lines[line_id][i] != ' ' and lines[line_id][i] != '\n':
				number = number + lines[line_id][i]
		ret.append(int(number))
	return ret

ret = 0
for id, p in enumerate(positions):
	if lines[len(lines)-1][p] == '+':
		ret = ret + sum(get_cpehalophod_number(id))
	elif lines[len(lines)-1][p] == '*':
		ret = ret + reduce(mul, get_cpehalophod_number(id))

print(ret)