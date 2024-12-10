from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(map(int, list(line.strip()))) for line in file]

M = defaultdict()
S = defaultdict()

max_row = len(lines)
max_col = len(lines[0])

for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col] 
		if lines[row][col] == 0:
			S[(row, col)] = []

directions = [(0,1), (1,0), (-1,0), (0,-1)]

def trail(start, step, step_cnt):
	if step not in M or M[step] != step_cnt:
		return 0

	if M[step] == 9 and step not in S[start]:
		S[start].append(step)

	for d in directions:
		trail(start, (step[0]+d[0], step[1]+d[1]), step_cnt+1)

for s in S.keys():
	trail(s, s, 0)

print(sum([len(scores) for scores in S.values()]))