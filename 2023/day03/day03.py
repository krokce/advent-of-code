import re

with open('day03.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

num_reg = re.compile(r'\d+')
r_max = len(lines)
c_max = len(lines[0])
G = {}

def is_part(l_no, start, end, n):
	ret = False
	for r in range(max(0, l_no-1), min(r_max, l_no+2)):
		for c in range(max(0, start-1), min(c_max, end+1)):
			# handle gear parts (#2)
			if lines[r][c] == '*':
				if (r,c) in G:
					G[(r,c)].append(n)
				else:
					G[(r,c)] = [n]

			if lines[r][c] != '.' and not lines[r][c].isdigit():
				ret = True
	return ret

ret = 0
for l_no, l in enumerate(lines):
	numbers = num_reg.finditer(l)
	for n in numbers:
		if is_part(l_no, n.start(), n.end(), int(n.group())):
			ret += int(n.group())

#1
print(ret)

#2
print(sum([g1 * g2 for g1, g2 in [g for g in G.values() if len(g) == 2] ]))