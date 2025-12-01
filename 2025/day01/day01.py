with open('input.txt', 'r') as file:
	lines = [(k[0], int(k[1:])) for k in [l.strip() for l in file.readlines()]]

position = 50
res1 = 0
res2 = 0

for direction, steps in lines:
	if direction == 'R':
		res2 = res2 + (position + steps) // 100
		position = (position + steps) % 100
	if direction == 'L':
		res2 = res2 + (1 if position > 0 and position - steps <= 0 else 0) + abs(position-steps) // 100
		position = (position - steps) % 100
	if position == 0:
		res1 = res1 + 1

print(res1)
print(res2)