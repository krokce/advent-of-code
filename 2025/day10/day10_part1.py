from itertools import combinations
import re

with open('input.txt', 'r') as file:
	lines = [line.strip() for line in file.readlines()]

M = []
for l in lines:
	# extract content inside square brackets (e.g. [.##.])
	s = re.search(r'\[([^\]]*)\]', l)
	indicator = s.group(1) if s else ''

	# convert . and # to binary string and reverse order
	indicator = indicator[::-1]
	indicator = indicator.replace('.', '0').replace('#', '1')
	indicator = int(indicator, 2) 

	# extract each parenthesis group like "(1,3)" -> [[1], [1,3], ...]
	p = re.findall(r'\(([^)]*)\)', l)
	buttons = [[int(x.strip()) for x in g.split(',') if x.strip()] for g in p]
	# convert each array to integer - each number represents a bit position to set
	for i in range(len(buttons)):
		bitmask = 0
		for pos in buttons[i]:
			bitmask |= (1 << pos)
		buttons[i] = bitmask

	# extract comma-separated numbers in braces like "{3,5,4,7}"
	b = re.search(r'\{([^}]*)\}', l)
	joltage = [int(x.strip()) for x in b.group(1).split(',')] if b else []

	M.append({'I': indicator, 'B': buttons, 'J': joltage})

def generate_xor_sequence(result, list_of_numbers):
	for number_of_clicks in range(1, len(list_of_numbers) + 1):
		for buttons in combinations(range(len(list_of_numbers)), number_of_clicks):
			res = result
			for b in buttons:
				res ^= list_of_numbers[b]
			if res == 0:
				print(f"Solution with {number_of_clicks} clicks: {[list_of_numbers[b] for b in buttons]}")
				return [list_of_numbers[b] for b in buttons]

ret = 0
for idx, m in enumerate(M):
	ret = ret + len(generate_xor_sequence(m['I'], m['B']))

print(ret)