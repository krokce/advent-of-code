import re
import math

with open('day02.txt', 'r') as file:
	lines = [l.strip().replace(" ", "").split(":") for l in file.readlines()]

colors = ('red', 'green', 'blue')

def is_possible(counts):
	max_check = (12,13,14)
	for p, cnt in enumerate(counts):
		if max_check[p] < cnt:
			return False
	return True

ret1 = 0
ret2 = 0
for l in lines:
	counts = [0,0,0]
	game_id = int(l[0].replace('Game', ''))
	seen = re.findall(r'((\d+)(red|green|blue)),*;*', l[1])
	for i in seen:
		cnt, color = int(i[1]), i[2]
		p = colors.index(color)
		counts[p] = max(counts[p], cnt)
	if is_possible(counts):
		ret1 += game_id
	ret2 += math.prod(counts) 

#1
print(ret1)

#2
print(ret2)
