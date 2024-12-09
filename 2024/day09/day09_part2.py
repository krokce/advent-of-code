with open('input.txt', 'r') as file:
	lines = list(map(int, [list(line.strip()) for line in file][0]))

F = []
for i in range(0, len(lines), 2):
	F.append([lines[i], int(i/2)])
	if i < len(lines)-1:
		F.append([lines[i+1], -1])

p1 = len(F)-1
while p1 > 0:
	for i in range(p1):
		if F[i][1] > -1 or F[i][0] < F[p1][0]:
			continue
		if F[i][0] == F[p1][0]:
			F[i] = F[p1]
			F[p1] = [F[p1][0], -1]
			break
		else:
			F[i][0] = F[i][0] - F[p1][0]
			F.insert(i, F[p1])
			if i < p1:
					p1 = p1 + 1
			F[p1] = [F[p1][0], -1]
			break
	p1 = p1 - 1
	while F[p1][1] < 0:
		p1 = p1 - 1

id = 0
sum = 0
for cnt, file_id in F:
	for k in range(cnt):
		if file_id > -1:
			sum = sum + (file_id * id)
		id = id + 1

print(sum)