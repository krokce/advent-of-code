with open('input.txt', 'r') as file:
	lines = [list(map(int, l.split("-"))) for l in file.readline().split(',')]

ret = 0
for first, last in lines:
	for i in range(first, last + 1):
		str_i = str(i)
		if len(str_i) % 2 == 0 and i // pow(10, len(str_i) // 2) == i % pow(10, len(str_i) // 2):
			ret = ret + i

print(ret)