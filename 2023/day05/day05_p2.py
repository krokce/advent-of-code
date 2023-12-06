import re
import copy
from collections import defaultdict

with open('day05.txt', 'r') as file:
	lines = [l.strip() for l in file.readlines() if l != "\n"]

M=defaultdict(list)

map_id = 0
for l in lines:
	if l.find("seeds:") > -1:
		seeds_pairs = re.findall(r"\d+ \d+", l)
	elif l.find(":") > -1:
		map_id += 1
	else:
		M[map_id].append(list(map(int, re.findall(r"\d+", l))))

seed_ranges = []
for seed in seeds_pairs:
	seed_from, seed_to = list(map(int, seed.split(" ")))
	seed_ranges.append((seed_from, seed_from+seed_to))

def map_range(r1, r2, d1, d2, delta):
	mapped = []
	unmapped = []
	if r2 <= d1 or r1 >= d2:
		unmapped += [(r1, r2)]
	elif r1 >= d1 and r2 <= d2:
		mapped += [(r1+delta, r2+delta)]
	elif  r1 < d1 and r2 > d2:
		unmapped += [(r1,d1), (d2, r2)]
		mapped += [(d1+delta, d2+delta)]
	elif  r1 < d1 and r2 <= d2: 
		unmapped += [(r1,d1)]
		mapped += [(d1+delta, r2+delta)]
	elif  r1 >= d1 and r2 > d2:
		unmapped += [(d2, r2)]
		mapped += [(r1+delta, d2+delta)]
	else:
		print("Range error:", r1, r2, d1, d2)
	return mapped, unmapped

def map_level(ranges, map_id):
	ret = []
	for r1, r2 in ranges:
		for destination_range, source_range, range_length in M[map_id]:
			d1 = source_range
			d2 = source_range + range_length
			delta = destination_range - source_range
			mapped, unmapped = map_range(r1, r2, d1, d2, delta)
			ret = list(set(ret + mapped))

			if len(unmapped) == 0:
				break
			if len(mapped) > 0:
				for u in unmapped:
					if u != (r1, r2):
						ranges.append(u)
				unmapped = []
				break
		ret = list(set(ret + mapped + unmapped))
	return ret

for map_id in range(1,8):
	seed_ranges = map_level(seed_ranges, map_id)

#2
print(min(seed_ranges)[0])