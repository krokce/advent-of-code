import re
from z3 import *

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
	
	# extract comma-separated numbers in braces like "{3,5,4,7}"
	b = re.search(r'\{([^}]*)\}', l)
	joltage = [int(x.strip()) for x in b.group(1).split(',')] if b else []

	M.append({'I': indicator, 'B': buttons, 'J': joltage})

def find_button_press_count(buttons, joltage_targets):
	s = Solver()
	for button_id in range(len(buttons)):
		button_var = Int(f"button_{button_id}")
		s.add(button_var >= 0)

	for joltage_position, joltage_target in enumerate(joltage_targets):
		btns = []
		for button_id in range(len(buttons)):

			if joltage_position in buttons[button_id]:
				btns.append(button_id)

		s.add(Sum([Int(f"button_{btn_id}") for btn_id in btns]) == joltage_target)

	solutions = []
	while s.check() == sat:
		m = s.model()
		# block this model and find next solution
		# s.add(Or([v != m[v] for v in (Int(f"button_{i}") for i in range(len(buttons)))]))
		s.add(Or([v < m[v] for v in (Int(f"button_{i}") for i in range(len(buttons)))]))
		solutions.append(sum([m[Int(f"button_{i}")].as_long() for i in range(len(buttons))]))
	return min(solutions)

ret = 0
for idx, m in enumerate(M):
	number_of_clicks = find_button_press_count(m['B'], m['J'])
	print(f"{idx} - Solution with {number_of_clicks} clicks")
	ret = ret + number_of_clicks

print(ret)