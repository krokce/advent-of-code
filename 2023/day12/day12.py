from functools import cache

with open('day12.txt', 'r') as file:
	lines = [l.strip().split() for l in file.readlines()]

@cache
def get_count(record, cgroups, in_group_count):
	cnt = 0

	# no more groups to fill
	if len(cgroups) == 0:
		if '#' not in record:
			return 1
		else:
			return 0
	
	# end of record
	if len(record) == 0:
		if len(cgroups) == 1 and cgroups[0] == in_group_count:
			return 1
		else:
			return 0

	# impossible to fit remaining groups in the rest of the record from this position
	if len(record) + in_group_count < sum(cgroups) + len(cgroups) - 1:
		return 0

	if in_group_count > 0:
		# group count exausted
		if in_group_count == cgroups[0]:
			if record[0] != '#':
				cnt += get_count(record[1:], cgroups[1:], 0)
		else:
			if record[0] in '#?':
				cnt += get_count(record[1:], cgroups, in_group_count+1)
	else:
		if record[0] == '#':
			cnt += get_count(record[1:], cgroups, in_group_count+1)
		elif record[0] == '.':
			cnt += get_count(record[1:], cgroups, 0)
		elif record[0] == '?':
			cnt += get_count(record[1:], cgroups, in_group_count+1) + get_count(record[1:], cgroups, 0)
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