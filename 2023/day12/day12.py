with open('day12.txt', 'r') as file:
	lines = [l.strip().split() for l in file.readlines()]

D = {}

def get_count(record, contiguous_group, damaged_segments):
	cnt = 0

	if (record, contiguous_group, damaged_segments) in D:
		return D[(record, contiguous_group, damaged_segments)]
	
	# no more groups to fill
	if len(contiguous_group) == 0:
		if '#' not in record:
			return 1
		else:
			return 0
	
	# end of record
	if len(record) == 0:
		if len(contiguous_group) == 1 and contiguous_group[0] == damaged_segments:
			return 1
		else:
			return 0

	# cgroup count fits counted damaged segments, 
	# start new cgroup aand reset damaged_segments counter
	if damaged_segments == contiguous_group[0]:
		if record[0] != '#':
			cnt += get_count(record[1:], contiguous_group[1:], 0)
	
	# damaged segments count in progress
	if damaged_segments > 0:
		if record[0] in '#?':
			cnt += get_count(record[1:], contiguous_group, damaged_segments+1)
	
	# not in cgroup, start new damaged segments counter or/and skip character
	if damaged_segments == 0:
		if record[0] in '#?':
			cnt += get_count(record[1:], contiguous_group, 1)
		if record[0] in '.?':
			cnt += get_count(record[1:], contiguous_group, 0)

	D[(record, contiguous_group, damaged_segments)] = cnt
	return cnt

#1
ret = 0
for l in lines:
	record = l[0]
	cgroup = tuple(map(int, l[1].split(',')))
	ret += get_count(record, cgroup, 0)
print(ret)

#2
ret = 0
for l in lines:
	record = l[0]
	cgroup = list(map(int, l[1].split(',')))
	record = '?'.join([record] * 5)
	cgroup = tuple(cgroup * 5)
	ret += get_count(record, cgroup, 0)

print(ret)