with open('input.txt', 'r') as file:
	lines = [l.split("\n") for l in file.read().split("\n\n") if l != ""]

fresh_ranges = [list(map(int, l.split("-"))) for l in lines[0]]
ingredients = [int(l) for l in lines[1] if l != '']

def is_fresh(ingredient):
	for r in fresh_ranges:
		if ingredient >= r[0] and ingredient <= r[1]:
			return True
	return False

ret = 0 
for ingredient in ingredients:
	if is_fresh(ingredient):
		ret += 1

# 1
print(ret)

cnt = 0
last_range = None
for r in sorted(fresh_ranges):
	if last_range is None:
		last_range = r
		continue
	if r[0] <= last_range[1]:
		last_range[1] = max(last_range[1], r[1])
	else:
		cnt = cnt + (last_range[1] - last_range[0] + 1)
		last_range = r
cnt = cnt + (last_range[1] - last_range[0] + 1)		

# 2
print(cnt)