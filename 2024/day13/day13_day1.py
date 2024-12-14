import re
from z3 import *

with open('input.txt', 'r') as file:
	lines = file.read()

ret = 0
for l in lines.split("\n\n"):
	ax, ay, bx, by, px, py = list(map(int, re.findall(r'\d+', l)))
	a, b = Ints("a b")
	s = Solver()
	s.add(a * ax + b * bx == px)
	s.add(a * ay + b * by == py)
	result = s.check()
	if result == sat:
		m = s.model()
		ret = ret + m[a].as_long()*3 + m[b].as_long()

print(ret)