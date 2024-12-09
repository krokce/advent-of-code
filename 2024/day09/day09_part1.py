from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = list(map(int, [list(line.strip()) for line in file][0]))

F = []
B = []
for i in range(0, len(lines), 2):
	F.append(lines[i])
	if i < len(lines)-1:
		B.append(lines[i+1])

p1 = 0
p2 = len(F)-1
pb = 0

ret = []
mode = 'file'
while True:
	if mode == 'file':
		ret.append((p1, F[p1]))
		p1 = p1 + 1
		mode = 'blank'
	else:
		if B[pb] >= F[p2]:
			ret.append((p2, F[p2]))
			B[pb] = B[pb] - F[p2]
			p2 = p2 - 1
		elif B[pb] < F[p2]:
			ret.append((p2, B[pb]))
			F[p2] = F[p2] - B[pb]
			B[pb] = 0

		if B[pb] == 0:
			pb = pb + 1
			mode = 'file'
	if p1 > p2:
		break

id = 0
sum = 0
for file_id, cnt in ret:
	for k in range(cnt):
		sum = sum + (file_id * id)
		id = id + 1

print(sum)