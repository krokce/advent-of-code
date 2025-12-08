from collections import defaultdict
from functools import reduce
from operator import mul

with open('input.txt', 'r') as file:
	lines = [list(line.split()) for line in file]

ret = 0
for j in range(len(lines[0])):
	if lines[len(lines)-1][j] == '+':
		ret = ret + sum([int(lines[k][j]) for k in range(len(lines)-1)])
	elif lines[len(lines)-1][j] == '*':
		ret = ret + reduce(mul, [int(lines[k][j]) for k in range(len(lines)-1)])

print(ret)