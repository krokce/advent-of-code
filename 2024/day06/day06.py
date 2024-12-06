from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

directions = [(0, -1), (1,0), (0, 1), (-1, 0)]

M = defaultdict()
for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(col, row)] = lines[row][col] 
		if M[(col, row)] == "^":
			start = (col, row)

R = defaultdict()
R[start] = "X"

def is_loop(np):
	P = start
	D = 0
	seen = defaultdict()
	while True:
		if (P, D) in seen:
			return True
		next_p = (P[0]+directions[D][0], P[1]+directions[D][1])
		if next_p in M:
			if M[next_p] == '#' or next_p == np:
				D = (D + 1) % 4
			else:
				seen[(P, D)] = 1
				P = next_p
		else:
			return False

P = start
D = 0
while True:
	next_p = (P[0]+directions[D][0], P[1]+directions[D][1])
	if next_p in M:
		if M[next_p] == '#':
			D = (D + 1) % 4
		else:
			R[next_p] = "X"
			P = next_p
	else:
		break

ret = 0
for np in R.keys():
	if is_loop(np):
		ret = ret + 1

# 1
print(len(R))

# 2
print(ret)