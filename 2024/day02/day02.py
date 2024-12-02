with open('input.txt', 'r') as file:
	lines = [list(map(int, l.strip().split()))  for l in file.readlines()]

def get_order(a, b):
	if a > b:
		return 1
	elif a < b:
		return -1
	else:
		return 0

def safe(r):
	last = r[0]
	order = get_order(r[0], r[1])
	for l in range(1, len(r)):
		if order != get_order(last, r[l]) or not 1 <= abs(last-r[l]) <=3:
			return False
		last = r[l]
	return True

#1
ret = 0
for report in lines:
	ret = ret + (1 if safe(report) else 0)
print(ret)

def safe_minus_one(r):
	tmp = r.copy()
	for i in range(len(r)):
		tmp.pop(i)
		if safe(tmp):
			return True
		tmp = r.copy()
	return False

# 2
ret = 0
for report in lines:
	if safe_minus_one(report):
		ret = ret + 1
print(ret)
