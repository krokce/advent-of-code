from collections import defaultdict
from functools import cache

with open('input.txt', 'r') as file:
	lines = [line.strip().split(": ") for line in file.readlines()]

M = defaultdict(list)
for line in lines:
	M[line[0]] = line[1].split(" ")

@cache
def count_nodes(start, end, fft_node, dac_node):
	if start == "out" and fft_node and dac_node:
		return 1

	ret = 0
	for node in M[start]:
		ret += count_nodes(node, end, fft_node or node == "fft", dac_node or node == "dac")
	return ret

print(count_nodes("svr", "out", False, False))