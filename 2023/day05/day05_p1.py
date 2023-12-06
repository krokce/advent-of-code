import re
from collections import defaultdict

with open('day05.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines() if l != "\n"]

M=defaultdict(list)

map_id = 0
seeds = []
for l in lines:
	if l.find("seeds:") > -1:
		seeds = list(map(int, re.findall(r"\d+", l)))
	elif l.find(":") > -1:
		map_id += 1
	else:
		M[map_id].append(list(map(int, re.findall(r"\d+", l))))

L = {}
ret = None
for seed in seeds:
	output_value = seed
	for map_id, map_rule_list in M.items():
		for destination_range, source_range, range_length in map_rule_list:
			if source_range + range_length >= output_value >= source_range:
				output_value += destination_range - source_range 
				break
	L[seed, ] = output_value
	ret = min(ret, output_value) if ret is not None else output_value

#1
print(ret)