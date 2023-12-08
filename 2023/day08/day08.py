import re
import math
from itertools import cycle

with open('day08.txt', 'r') as file:
	lines = [l.strip().split('=') for l in file.readlines() if l != "\n"]


I = {}
for l_no, l in enumerate(lines):
	if l_no == 0:
		steps = l[0]
	else:
		I[l[0].strip()] = l[1].strip().replace('(', '').replace(')', '').split(', ')

#1
ret = 0
position = 'AAA'
for step in cycle(steps):
	next_step = 0 if step == 'L' else 1
	position = I[position][next_step]
	ret += 1
	if position == 'ZZZ':
		break

print(ret)

#2
positions = [p for p in I.keys() if p[-1] == 'A']
ends = [[] for i in range(len(positions))]

def find_lcm(numbers):
	lcm = numbers[0]
	for num in numbers[1:]:
		lcm = lcm * num // math.gcd(lcm, num)
	return lcm

step_no = 0
while True:
	step_no += 1
	step_position = (step_no-1) % len(steps) 
	next_step = 0 if steps[step_position] == 'L' else 1

	new_positions = []
	for position_no, position in enumerate(positions):
		new_position = I[position][next_step]
		new_positions.append(new_position)
		if new_position[-1] == 'Z':
			ends[position_no].append(step_no)
	positions = new_positions

	# if found at least one end per starting ghost position
	if len(ends) == len([1 for i in ends if len(i)>0]):
		break

print(find_lcm([end[0] for end in ends]))