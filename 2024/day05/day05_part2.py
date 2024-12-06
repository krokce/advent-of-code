from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [line.strip() for line in file]

R = []
U = []
for l in lines:
	if l == "":
		break
	R.append(list(map(int, l.split("|"))))

for i in range(len(R)+1, len(lines)):
	U.append(list(map(int, lines[i].split(","))))

def is_correct(update):
	for rule in R:
		if rule[0] not in update or rule[1] not in update:
			continue
		idx_a = update.index(rule[0])
		idx_b = update.index(rule[1])
		if idx_a > idx_b:
			return False
	return True

def fix(update):
	update = update.copy()
	for rule in R:
		if rule[0] not in update or rule[1] not in update:
			continue
		idx_a = update.index(rule[0])
		idx_b = update.index(rule[1])
		if idx_a > idx_b:
			element = update.pop(idx_b)
			update.insert(idx_a, element)
	if not is_correct(update):
		return fix(update)
	else:
		return update

ret = 0
for update in U:
	if not is_correct(update):
		update = fix(update)
		ret = ret + update[(int(len(update)/2))]

print(ret)