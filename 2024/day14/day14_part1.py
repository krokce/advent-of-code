import re
from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines()]

x_max = 101
y_max = 103
t = 100

def quadrant(x,y):
	q1, q2 = (-1,-1)
	if 0 <= x < x_max//2:
		q1 = 0
	if x_max//2 < x < x_max:
		q1 = 1
	if 0 <= y < y_max//2:
		q2 = 0
	if y_max//2 < y < y_max:
		q2 = 1
	return (q1, q2)

M = defaultdict(int)
R = defaultdict(int)

for l in lines:
	px, py, vx, vy = list(map(int, re.findall(r'-?\d+', l)))
	px1 = (px+vx*t)%x_max
	py1 = (py+vy*t)%y_max

	M[(px1, py1)] = M[(px1, py1)] + 1
	q = quadrant(px1, py1)
	if q[0] > -1 and q[1] > -1:
		R[q] = R[q] + 1

ret = 1
for i in R.values():
	ret = ret * i

print(ret)