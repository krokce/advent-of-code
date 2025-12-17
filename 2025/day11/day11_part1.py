from collections import defaultdict

with open('input.txt', 'r') as file:
	lines = [line.strip().split(": ") for line in file.readlines()]

M = defaultdict(list)
for line in lines:
	M[line[0]] = line[1].split(" ")

def count_paths(start, end):
	if start == end:
		return 1

	ret = 0
	for node in M[start]:
		ret += count_paths(node, end)
	return ret

print(count_paths("you", "out"))