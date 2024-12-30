from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [int(l.strip()) for l in file.readlines()]

M = defaultdict(int)

def new_secret(num):
	a = num * 64
	ret = num ^ a
	ret = ret % 16777216
	b = int(ret / 32)
	ret = ret ^ b
	ret = ret % 16777216
	c = ret * 2048
	ret = ret ^ c
	ret = ret % 16777216
	return ret

for id, num in enumerate(lines):
	done = []
	changes = []
	last_price = num % 10
	for i in range(2000):
		num = new_secret(num)
		price = num % 10
		changes.append(price-last_price)
		last_price = price
		if len(changes) >= 4:
			changes_id = tuple(changes[-4:])
			if (changes_id) not in done:
				M[changes_id] = M[changes_id] + price
				done.append(changes_id)
	print(id, num)

max_key = max(M, key=M.get)
print(max_key, M[max_key])