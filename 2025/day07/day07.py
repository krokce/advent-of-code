from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [list(line.strip()) for line in file]

M = defaultdict()
max_row = len(lines)
max_col = len(lines[0])
tachion_beams =	[]
S = None
for row in range(len(lines)):
	for col in range(len(lines[row])):
		M[(row, col)] = lines[row][col]
		if lines[row][col] == 'S':
			tachion_beams.append(col)
			S = (row, col)

P = {}
def get_beams(b):
	if b not in B:
		return 1
	else:
		total = 0
		for nb in B[b]:
			if nb not in P:
				P[nb] = get_beams(nb)
			total = total + P[nb]
		return total

ret = 0
B = defaultdict(list)
for r in range(max_row):
	new_beams = set()
	for beam in tachion_beams:
		if M[(r, beam)] == '^':
			B[(r, beam)].append((r+1, beam-1))
			B[(r, beam)].append((r+1, beam+1))
			new_beams.add(beam-1)
			new_beams.add(beam+1)
			ret = ret + 1
		else:
			new_beams.add(beam)
			B[(r, beam)].append((r+1, beam))
	tachion_beams = list(new_beams)

# 1
print(ret)

# 2
print(get_beams(S))