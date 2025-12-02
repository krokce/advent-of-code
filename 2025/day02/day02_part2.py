with open('input.txt', 'r') as file:
	lines = [list(map(int, l.split("-"))) for l in file.readline().split(',')]

ret = 0
for first, last in lines:
	for i in range(first, last + 1):
		str_i = str(i)
		for chunk_length in range(1, len(str_i) // 2 + 1):
			if len(str_i) % chunk_length == 0:
				chunks = [str_i[j:j + chunk_length] for j in range(0, len(str_i), chunk_length)]

				if len(set(chunks)) == 1:
					ret = ret + i
					break

print(ret)